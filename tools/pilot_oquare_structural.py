#!/usr/bin/env python3
"""Bounded OQuaRE-compatible raw structural pilot over exact asserted closure.

This is an independent, explicitly scoped formula implementation, not an
execution of the upstream OQuaRE Java engine or a semantic-quality verdict.
"""
import argparse
import hashlib
import json
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, OWL, URIRef, XSD

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/ontology/generated/p1-r2-closure-manifest.json'
GRAPH = ROOT / 'docs/ontology/generated/p1-r2-asserted-closure.nt'
OUT = ROOT / 'evaluation/oquare'
OQUO = Namespace('https://purl.org/oquo#')
ER = Namespace('http://purl.org/net/EvaluationResult#')
OBOE = Namespace('http://ecoinformatics.org/oboe/oboe.1.2/oboe-core.owl#')
QM = Namespace('http://purl.org/net/QualityModel#')
PILOT = Namespace('urn:semrisk:evaluation:oquare-pilot:')
METRICS_REF = 'tecnomod-um/oquare@3c870b504c799bfb7598912d1b29cab7f44d12ac'
OQUO_REF = 'tecnomod-um/oquo@a43fe72aabe2bbff0b2d10cebd67e89c8049c9ff'


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def metrics(g, classes):
    # Asserted URI-valued direct parents only; no anonymous restrictions or
    # inferred superclasses. The denominator follows OQuaRE TMOnto (C - 1).
    multiple = sum(sum(isinstance(p, URIRef) for p in g.objects(c, RDFS.subClassOf)) > 1
                   for c in classes)
    annotations = sum(sum(1 for _ in g.objects(c, pred))
                      for c in classes for pred in (RDFS.label, RDFS.comment))
    tangle = multiple / (len(classes) - 1)
    # Published TMOnto bands at the pinned OQuaRE documentation ref.
    band = 1 if tangle > .4 else 2 if tangle > .3 else 3 if tangle > .2 else 4 if tangle > .1 else 5
    return {'local_class_count': len(classes), 'multiple_direct_parent_classes': multiple,
            'tangledness_raw': tangle, 'tangledness_5point_band': band,
            'label_comment_assertions': annotations,
            'annotation_richness_raw': annotations / len(classes)}


def render_rdf(result):
    g = Graph()
    for prefix, namespace in [('oquo', OQUO), ('er', ER), ('oboe', OBOE),
                              ('qm', QM), ('pilot', PILOT)]:
        g.bind(prefix, namespace)
    subject = PILOT['semrisk-p1-r2-asserted-closure']
    evaluation = PILOT['evaluation-baseline']
    observation = PILOT['observation-baseline']
    g.add((evaluation, RDF.type, ER.Evaluation))
    g.add((evaluation, ER.evaluatedSubject, subject))
    g.add((evaluation, ER.inputData, subject))
    g.add((observation, RDF.type, OBOE.Observation))
    g.add((observation, OBOE.ofEntity, subject))
    g.add((evaluation, OQUO.hasObservation, observation))
    for name, kind, scale, value in [
        ('tangledness', OQUO.TanglednessMetric, OQUO.TanglednessMetricScale,
         result['baseline']['tangledness_raw']),
        ('annotation-richness', OQUO.AnnotationRichnessMetric,
         OQUO.AnnotationRichnessMetricScale,
         result['baseline']['annotation_richness_raw'])]:
        measure = PILOT['measurement-' + name]
        quality_value = PILOT['raw-value-' + name]
        g.add((measure, RDF.type, kind))
        g.add((measure, RDF.type, OBOE.Measurement))
        g.add((measure, QM.hasScale, scale))
        g.add((measure, OBOE.measurementFor, observation))
        g.add((observation, OBOE.hasMeasurement, measure))
        g.add((measure, OBOE.hasValue, quality_value))
        g.add((quality_value, RDF.type, ER.QualityValue))
        g.add((quality_value, RDF.type, OBOE.MeasuredValue))
        g.add((quality_value, ER.forMeasure, measure))
        g.add((quality_value, ER.hasLiteralValue, Literal(value, datatype=XSD.double)))
        g.add((quality_value, ER.isMeasuredOnScale, scale))
        g.add((quality_value, ER.obtainedFrom, evaluation))
        g.add((evaluation, ER.producedQualityValue, quality_value))
    # Sorted N-Triples is deterministic and does not require network imports.
    return ''.join(sorted(g.serialize(format='nt').splitlines(keepends=True)))


def build():
    manifest = json.loads(MANIFEST.read_text())
    raw = GRAPH.read_bytes()
    assert sha256(raw) == manifest['canonical_nt_sha256']
    for source in manifest['files']:
        assert git_blob((ROOT / source['path']).read_bytes()) == source['git_blob_sha']
    g = Graph(); g.parse(data=raw.decode(), format='nt')
    assert len(g) == manifest['unique_asserted_triples'] == 1409
    classes = sorted({c for c in g.subjects(RDF.type, OWL.Class)
                      if isinstance(c, URIRef) and str(c).startswith('urn:semrisk:')}, key=str)
    assert len(classes) == 35
    baseline = metrics(g, classes)
    # Reversible, in-memory annotation change. Keep semantic identifiers fixed.
    safe_target = classes[0]
    g.add((safe_target, RDFS.comment, Literal('Pilot explanatory annotation; fixture only.')))
    safe = metrics(g, classes)
    g.remove((safe_target, RDFS.comment, Literal('Pilot explanatory annotation; fixture only.')))
    # A deliberate extra direct parent, chosen on a class with exactly one URI
    # parent. This is a diagnostic tangle, never a claim of inconsistency.
    child = next(c for c in classes if sum(isinstance(p, URIRef)
                 for p in g.objects(c, RDFS.subClassOf)) == 1)
    old_parent = next(p for p in g.objects(child, RDFS.subClassOf) if isinstance(p, URIRef))
    second = next(c for c in classes if c not in (child, old_parent))
    g.add((child, RDFS.subClassOf, second))
    adverse = metrics(g, classes)
    g.remove((child, RDFS.subClassOf, second))
    assert metrics(g, classes) == baseline and len(g) == 1409
    assert safe['annotation_richness_raw'] > baseline['annotation_richness_raw']
    assert safe['tangledness_raw'] == baseline['tangledness_raw']
    assert adverse['tangledness_raw'] > baseline['tangledness_raw']
    assert baseline['tangledness_5point_band'] == adverse['tangledness_5point_band'] == 5
    assert adverse['annotation_richness_raw'] == baseline['annotation_richness_raw']
    result = {
        'status': 'BOUNDED_RAW_STRUCTURAL_PILOT',
        'candidate': manifest['candidate'],
        'source_ref': 'c17cc111f02309270a60474623259cefcf907c6f',
        'input': str(GRAPH.relative_to(ROOT)), 'input_sha256': sha256(raw),
        'source_files': [{'path': s['path'], 'git_blob_sha': s['git_blob_sha']}
                         for s in manifest['files']],
        'scope': 'Seven-file catalog-resolved asserted closure; 35 locally declared OWL classes; no inferred axioms.',
        'implementation': 'tools/pilot_oquare_structural.py, RDFLib 7.6.0; formulas from ' + METRICS_REF,
        'representation': OQUO_REF + ', OQUO-QASAR example; raw values only',
        'formulae': {
            'TMOnto': 'local classes with >1 direct URI superclass / (local classes - 1)',
            'ANOnto': 'asserted rdfs:label plus rdfs:comment count on local classes / local classes'},
        'baseline': baseline,
        'safe_fixture': {'change': 'one extra rdfs:comment, in memory', 'class': str(safe_target), 'result': safe},
        'adverse_fixture': {'change': 'one extra direct named superclass, in memory',
                            'class': str(child), 'added_parent': str(second), 'result': adverse},
        'scaling': 'TMOnto 1–5 published bands applied descriptively: both baseline and one-parent adverse fixture remain in band 5, showing insensitivity. ANOnto 1–5 conversion NOT_APPLIED because its published percentage bands are not interpretable for the observed mean of two label/comment assertions per class. No overall score.',
        'limitations': ['No upstream OQuaRE Java engine executed.',
                        'Tangledness is not a semantic inconsistency test; an extra parent can be legitimate.',
                        'Annotation count does not assess correctness of descriptions; ANOnto scale needs upstream clarification.',
                        'No expert review, domain validation or overall score.']}
    return json.dumps(result, indent=2, ensure_ascii=False) + '\n', render_rdf(result)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    report, rdf = build()
    files = {OUT / 'p1-r2-structural-pilot-v0.1.json': report,
             OUT / 'p1-r2-structural-pilot-v0.1.nt': rdf}
    for path, content in files.items():
        if args.check:
            assert path.read_text() == content, f'generated drift: {path}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content)
    print('SEM_RISK_OQUARE_RAW_PILOT_PASS: 35 local classes, two raw metrics, two in-memory sensitivity fixtures')


if __name__ == '__main__':
    main()
