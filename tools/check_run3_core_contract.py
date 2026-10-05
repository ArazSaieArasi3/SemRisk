#!/usr/bin/env python3
"""Bounded asserted-graph regressions, not OWL proofs or empirical validation."""
import argparse
import hashlib
import json
import platform
from datetime import datetime
from pathlib import Path
import rdflib
from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD, Literal

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evaluation/core-contract/2026-10-05'
SR = Namespace('urn:semrisk:entity:')
EX = Namespace('urn:semrisk:run3:')
TP = Namespace('urn:semrisk:profile:temporal:v0.1:')
C = Namespace('urn:semrisk:scenario:p1:e2e:')
B = Namespace('urn:semrisk:case:pharma:v1:')
PH = Namespace('urn:semrisk:profile:pharma-test:v0.1:')
DCT = Namespace('http://purl.org/dc/terms/')
def c(n): return SR[f'SR-CPT-{n:03}']
def r(n): return SR[f'SR-REL-{n:03}']
def clone(g):
    h = Graph()
    for t in g: h.add(t)
    return h
def values(g, s, p): return set(g.objects(s, p))
def rows(g, q): return sorted([[str(x) for x in row] for row in g.query(q)])
def one(g, s, p):
    a = values(g, s, p)
    if len(a) != 1: raise ValueError(f'exactly one {p} required for {s}')
    return next(iter(a))
def timestamp(v):
    d = v.toPython() if isinstance(v, Literal) else None
    if not (isinstance(v, Literal) and v.datatype == XSD.dateTime and
            isinstance(d, datetime) and d.tzinfo is not None and d.utcoffset() is not None):
        raise ValueError('timezone-aware xsd:dateTime required')
    return d
def state_errors(g):
    return [str(o) for _, _, o in g.triples((None, r(31), None))
            if (o, RDF.type, c(35)) not in g or (o, RDF.type, c(36)) in g]
def temporal_errors(g):
    errors = []
    for result in set(g.subjects(RDF.type, c(13))):
        try:
            target = one(g, result, r(16))
            for p in [TP.assessedAt, TP.referenceTime]: timestamp(one(g, result, p))
            for p, allowed in [(TP.dimension, {TP.Likelihood, TP.Impact, TP.RiskLevel}),
                               (TP.controlBaseline, {TP.BeforeControl, TP.AfterControl}),
                               (TP.evaluationBasis, {TP.Observed, TP.Projected})]:
                if one(g, result, p) not in allowed: raise ValueError('unknown context value')
            scale = one(g, result, TP.scale)
            number = one(g, result, TP.numericValue).toPython()
            minimum, maximum = (one(g, scale, p).toPython() for p in [TP.minimum, TP.maximum])
            if not minimum <= number <= maximum: raise ValueError('value outside scale')
            activities = set(g.subjects(r(15), result))
            if len(activities) != 1: raise ValueError('one producing activity required')
            activity = next(iter(activities))
            if one(g, activity, r(13)) != target: raise ValueError('activity/result risk mismatch')
            method = one(g, activity, r(14))
            one(g, method, DCT.hasVersion)
        except (ValueError, TypeError, AttributeError) as e: errors.append(str(e))
    for assignment in set(g.subjects(RDF.type, c(31))):
        try:
            starts, ends = values(g, assignment, TP.validFrom), values(g, assignment, TP.validTo)
            if len(starts) > 1 or len(ends) > 1: raise ValueError('multiple validity bounds')
            start = timestamp(next(iter(starts))) if starts else None
            end = timestamp(next(iter(ends))) if ends else None
            if start and end and start >= end: raise ValueError('reversed/empty validity interval')
        except ValueError as e: errors.append(str(e))
    for new, _, old in g.triples((None, r(33), None)):
        if len(values(g, new, r(16))) != 1 or values(g, new, r(16)) != values(g, old, r(16)):
            errors.append('cross-risk or unqualified supersession')
    return errors
def extension_errors(g):
    errors = []
    for s, p, o in g:
        if str(s).startswith(str(SR)): errors.append('core subject redefinition')
        if p in {OWL.equivalentClass, OWL.equivalentProperty, OWL.sameAs}:
            errors.append('equivalence shortcut outside selected extension policy')
    return errors

def run():
    protocol = json.loads((OUT / 'protocol.json').read_text())
    base = Graph().parse(ROOT / 'case/pharma/e2e-scenario-v1.1.ttl')
    temporal = Graph().parse(OUT / 'temporal-positive.ttl')
    extension = Graph().parse(OUT / 'pharma-extension.ttl')
    answers = {}
    def check(id_, condition, details):
        answers[id_] = {'id': id_, 'passed': bool(condition), 'details': details}

    # Controlled before/after graph edits exercise the three distinct histories.
    g = clone(base); g.add((C.entry, r(30), EX['workflow-reviewed']))
    g.add((EX['workflow-reviewed'], RDF.type, c(36)))
    check('R1', values(g, C.entry, r(30)) != values(base, C.entry, r(30)) and
          values(g, B['risk-context'], r(31)) == values(base, B['risk-context'], r(31)),
          'Added workflow state; same two situational-state links. Asserted graph only.')
    g = clone(base); g.add((EX['new-result'], r(33), C['result-residual']))
    g.add((EX['new-result'], RDF.type, c(18))); g.add((EX['new-result'], r(16), B['risk-context']))
    g.add((EX['new-assessment'], r(15), EX['new-result']))
    g.add((EX['new-assessment'], r(13), B['risk-context']))
    g.add((EX['new-assessment'], r(34), C['assessment-post']))
    check('R2', len(list(g.triples((None, r(33), None)))) == 2 and
          values(g, B['risk-context'], r(31)) == values(base, B['risk-context'], r(31)) and
          values(g, C.entry, r(30)) == values(base, C.entry, r(30)),
          'Added assessment and successor result; both state families unchanged.')
    g = clone(base); g.add((B['risk-context'], r(31), EX['new-situation']))
    g.add((EX['new-situation'], RDF.type, c(35)))
    check('R3', not state_errors(g) and
          values(g, B['risk-context'], r(31)) != values(base, B['risk-context'], r(31)) and
          values(g, C.entry, r(30)) == values(base, C.entry, r(30)),
          'Added situational state; workflow links unchanged.')
    check('R4', values(base, C['result-inherent'], r(16)) ==
          values(base, C['result-residual'], r(16)) == {B['risk-context']} and
          set(base.subjects(RDF.type, c(1))) == {B['risk-context']}, 'One risk identity, two result contexts.')
    check('R5', len(list(base.triples((None, r(31), None)))) == 2 and not state_errors(base),
          'Both existing state links target situational family, not workflow family.')
    observed = set(temporal.subjects(TP.evaluationBasis, TP.Observed))
    projected = set(temporal.subjects(TP.evaluationBasis, TP.Projected))
    check('T1', observed == {EX.observed} and projected == {EX.projected} and
          values(temporal, EX.observed, r(16)) == values(temporal, EX.projected, r(16)) == {EX.risk},
          'Observed and projected residual estimates separated; score difference is not a treatment effect.')
    owner_rows = rows(temporal, (OUT / 'owner-at-time.rq').read_text())
    check('T2', owner_rows == [[str(EX['actor-a'])], [str(EX['actor-b'])]],
          {'actual': owner_rows, 'excluded': ['future start', 'end boundary', 'unknown start']})
    check('T3', not temporal_errors(temporal), {'errors': temporal_errors(temporal)})
    comparison = json.loads((ROOT / 'evaluation/e10/controlled-distinction-study-v1/protocol.json').read_text())
    extended = base + extension
    comparisons = [{'task': t['id'], 'same_expected_answers':
                    rows(base, t['query']) == rows(extended, t['query']) == sorted(t['expected'])}
                   for t in comparison['tasks']]
    check('E1', len(comparisons) == 4 and all(x['same_expected_answers'] for x in comparisons), comparisons)
    new_answers = set(extended.subjects(RDF.type, PH.SupplyDisruptionAssessment))
    check('E2', new_answers == {C['result-residual']} and
          (PH.SupplyDisruptionAssessment, RDFS.subClassOf, c(13)) in extension,
          sorted(str(x) for x in new_answers))
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in protocol['source_hashes']}
    check('E3', hashes == protocol['source_hashes'] and not extension_errors(extension),
          {'module_count': len(hashes), 'core_bytes_unchanged': hashes == protocol['source_hashes'],
           'policy_errors': extension_errors(extension), 'formal_conservative_extension_proof': False})
    g = clone(base); g.add((B['risk-context'], r(31), C['workflow-open']))
    check('N1', bool(state_errors(g)), state_errors(g))
    g = clone(temporal); g.set((EX.observed, TP.assessedAt, Literal('2026-10-05T08:00:00', datatype=XSD.dateTime)))
    check('N2', 'timezone-aware xsd:dateTime required' in temporal_errors(g), temporal_errors(g))
    g = clone(temporal); g.set((EX['owner-active'], TP.validTo, Literal('2026-09-30T00:00:00Z', datatype=XSD.dateTime)))
    check('N3', 'reversed/empty validity interval' in temporal_errors(g), temporal_errors(g))
    g = clone(temporal); g.add((EX.observed, r(33), EX['other-result']))
    g.add((EX['other-result'], r(16), EX['other-risk']))
    check('N4', 'cross-risk or unqualified supersession' in temporal_errors(g), temporal_errors(g))
    g = clone(temporal); g.set((EX.observed, TP.numericValue, Literal('1.5', datatype=XSD.decimal)))
    check('N5', 'value outside scale' in temporal_errors(g), temporal_errors(g))
    g = clone(extension); g.add((c(1), RDFS.subClassOf, PH.SupplyDisruptionAssessment))
    check('N6', 'core subject redefinition' in extension_errors(g), extension_errors(g))
    g = clone(extension); g.add((PH.SupplyDisruptionAssessment, OWL.equivalentClass, c(1)))
    check('N7', 'equivalence shortcut outside selected extension policy' in extension_errors(g), extension_errors(g))
    assert set(answers) == {t['id'] for t in protocol['tests']}, 'Unexecuted or unregistered test'
    ordered = [{**t, **answers[t['id']]} for t in protocol['tests']]
    return {'scope': protocol['design'], 'baseline_commit': protocol['baseline_commit'],
            'python_version': platform.python_version(), 'rdflib_version': rdflib.__version__,
            'total': len(ordered), 'passed': sum(x['passed'] for x in ordered), 'tests': ordered,
            'original_cq_total_unchanged': 40, 'canonical_owl_or_sql_promoted': False,
            'expert_validation': False, 'peer_benchmark': False, 'formal_reasoner_run': False,
            'formal_conservative_extension_proof': False}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--write', action='store_true')
    args = parser.parse_args(); result = run()
    if args.write: (OUT / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] == result['total'] else 1)
