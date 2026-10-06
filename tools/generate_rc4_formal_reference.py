#!/usr/bin/env python3
"""Offline, read-only projection of rc.4. Never changes semantic source files."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET
from rdflib import BNode, Graph, URIRef
from rdflib.compare import to_canonical_graph
from rdflib.namespace import OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.2.0-rc.4'
RELEASE = Path('ontology/releases') / VERSION
OUT = Path('docs/formal') / VERSION
MODULES = ['core', 'enterprise', 'method', 'governance', 'pharma', 'mappings', 'assessment-context']
SHAPES = ['shapes/assessment-context-v0.2.0-rc.1.ttl', 'shapes/semantic-identity-v0.2.0-rc.3.ttl', 'shapes/exposure-scale-v0.2.0-rc.4.ttl']
RULES = ['rules/enterprise/risk-owners-at-v0.2.0-rc.1.rq', 'rules/enterprise/workflow-at-v0.2.0-rc.3.rq', 'rules/core/exposure-at-v0.2.0-rc.4.rq']
NS = ['urn:semrisk:entity:', 'urn:semrisk:profile:assessment-context:', 'urn:semrisk:profile:information-state:']
KINDS = {OWL.Class: 'class', OWL.ObjectProperty: 'object_property', OWL.DatatypeProperty: 'datatype_property', OWL.NamedIndividual: 'named_individual', OWL.AnnotationProperty: 'annotation_property', SKOS.Concept: 'marker'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def closure(root=ROOT):
    directory = root / RELEASE
    catalog = ET.parse(directory / 'catalog.xml')
    bindings = {}
    for entry in catalog.findall('{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri'):
        target = (directory / entry.attrib['uri']).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError('CATALOG_ESCAPE: ' + str(target))
        if entry.attrib['name'] in bindings:
            raise ValueError('DUPLICATE_IMPORT_BINDING')
        bindings[entry.attrib['name']] = target
    graphs, visiting = {}, set()
    def visit(path):
        path = path.resolve()
        if path in visiting:
            raise ValueError('IMPORT_CYCLE')
        if path in graphs:
            return
        visiting.add(path)
        g = Graph().parse(data=path.read_bytes(), format='turtle')
        for iri in g.objects(None, OWL.imports):
            if str(iri) not in bindings:
                raise ValueError('UNBOUND_IMPORT: ' + str(iri))
            visit(bindings[str(iri)])
        visiting.remove(path)
        graphs[path] = g
    for module in MODULES:
        visit(directory / (module + '.ttl'))
    if len(graphs) != 8:
        raise ValueError('CLOSURE_FILE_COUNT: expected seven modules plus gUFO')
    return graphs


def build(root=ROOT):
    graphs = closure(root)
    union, local = Graph(), Graph()
    declarations = defaultdict(set)
    for path, graph in graphs.items():
        union += graph
        if path.parent == (root / RELEASE).resolve():
            local += graph
            for typ, kind in KINDS.items():
                for subject in graph.subjects(RDF.type, typ):
                    if any(str(subject).startswith(ns) for ns in NS):
                        declarations[str(subject)].add((kind, path.relative_to(root).as_posix()))
    counts = Counter(kind for values in declarations.values() for kind, _ in values)
    expected = {'class': 46, 'object_property': 50, 'datatype_property': 8, 'named_individual': 7, 'marker': 4, 'annotation_property': 1}
    if counts != expected or len(declarations) != 116:
        raise ValueError('DECLARATION_DRIFT: ' + str(counts))
    registry = list(csv.DictReader((root / RELEASE / 'conceptual-iri-register.csv').open()))
    if len(registry) != 87 or len({r['id'] for r in registry}) != 87:
        raise ValueError('CONCEPT_RELATION_DENOMINATOR')
    statuses = Counter(row['formal_status'] for row in registry)
    if statuses != {'LOCAL_CLASS':35, 'OWL_OBJECT_PROPERTY':39, 'EXTERNAL_OR_PATTERN_MARKER':4, 'NOT_LOCALLY_DECLARED':8, 'PATTERN_OR_METADATA':1}:
        raise ValueError('REGISTRY_DISPOSITION_DRIFT: ' + str(statuses))
    for row in registry:
        if row['version'] != VERSION or row['iri'] != 'urn:semrisk:entity:' + row['id']:
            raise ValueError('REGISTRY_IDENTITY_DRIFT: ' + row['id'])
        subject = URIRef(row['iri'])
        if row['formal_status'] == 'NOT_LOCALLY_DECLARED' and row['iri'] in declarations:
            raise ValueError('UNDECLARED_STATUS_DRIFT: ' + row['id'])
        expected_type = {'LOCAL_CLASS': OWL.Class, 'OWL_OBJECT_PROPERTY': OWL.ObjectProperty, 'EXTERNAL_OR_PATTERN_MARKER': SKOS.Concept, 'PATTERN_OR_METADATA': OWL.AnnotationProperty}.get(row['formal_status'])
        if expected_type and (subject, RDF.type, expected_type) not in local:
            raise ValueError('REGISTRY_TYPE_DRIFT: ' + row['id'])
    canonical = to_canonical_graph(union)
    nt = '\n'.join(sorted(canonical.serialize(format='nt').splitlines())) + '\n'
    csv_file = io.StringIO(newline='')
    writer = csv.DictWriter(csv_file, lineterminator='\n', fieldnames=['iri', 'kind', 'source_path', 'source_sha256', 'asserted_types', 'asserted_superclasses', 'asserted_domain', 'asserted_range', 'anonymous_expression_targets'])
    writer.writeheader()
    for iri, values in sorted(declarations.items()):
        subject = URIRef(iri)
        def uris(predicate):
            return ';'.join(sorted(str(o) for o in local.objects(subject, predicate) if isinstance(o, URIRef)))
        for kind, path in sorted(values):
            writer.writerow(dict(iri=iri, kind=kind, source_path=path, source_sha256=digest((root/path).read_bytes()), asserted_types=uris(RDF.type), asserted_superclasses=uris(RDFS.subClassOf), asserted_domain=uris(RDFS.domain), asserted_range=uris(RDFS.range), anonymous_expression_targets=sum(isinstance(o, BNode) for _,_,o in local.triples((subject,None,None)))))
    extra = [str(RELEASE/'catalog.xml'), str(RELEASE/'manifest.json'), str(RELEASE/'conceptual-iri-register.csv'), str(RELEASE/'profile-iri-registry.csv'), str(RELEASE/'information-state-iri-registry.csv'), *SHAPES, *RULES, 'shapes/foundational-evidence-v0.2.0-rc.2.ttl', 'shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl', 'rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq', 'evaluation/cq/issue52-cq-results-v1.0.csv', 'foundational/exposure-scale-v0.2.0-rc.4/concept-category-audit.csv', 'foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv']
    source_paths = sorted(set([p.relative_to(root).as_posix() for p in graphs] + extra))
    sources = []
    for path in source_paths:
        data = (root/path).read_bytes()
        sources.append({'path':path,'sha256':digest(data),'git_blob_sha':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
    sg=Graph()
    for path in SHAPES: sg.parse(root/path)
    sh=URIRef('http://www.w3.org/ns/shacl#NodeShape')
    named_shapes=sorted(str(s) for s in sg.subjects(RDF.type,sh) if isinstance(s,URIRef))
    cq=Counter(r['state'] for r in csv.DictReader((root/'evaluation/cq/issue52-cq-results-v1.0.csv').open()))
    report={'version':VERSION,'projection':'asserted import closure, not entailment closure','publication_ready':False,'module_count':7,'closure_file_count':len(graphs),'asserted_triples':len(canonical),'canonical_nt_sha256':digest(nt.encode()),'declared_entity_count':len(declarations),'declaration_counts':dict(sorted(counts.items())),'conceptual_rows':47,'registered_relation_rows':40,'named_shapes':named_shapes,'separately_bound_profiles':{'optional_grounding':'shapes/foundational-evidence-v0.2.0-rc.2.ttl','historical_legacy':'shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl'},'query_paths':RULES,'historical_cq_classification':dict(sorted(cq.items())),'sources':sources,'limits':['No new OWL reasoning result is produced by this generator','Shape files retain their original versions; composition is explicitly bound','Historical CQ counts are not an rc.4 full SQL parity rerun','No live Wiki/Pages parity, scholarly release or independent expert validation']}
    md=['# rc.4 generated asserted reference','','This is a read-only source projection. The [curated FD-A–FD-J reference](../formal-ontology-description-rc4.md) explains scope and interpretation.','','- Seven modules and one pinned local gUFO file','- '+str(len(canonical))+' unique asserted triples; 116 declared local entities','- 47 conceptual rows and 40 registered relation rows; helpers have separate identity','- The [complete canonical graph](asserted-closure.nt) includes anonymous expressions and imported statements.','- The [entity inventory](entity-inventory.csv) includes all local declarations and URI-target structural assertions from all local modules. It is not an entailment inventory.','','## Source-bound modules','','| Module | Ontology/version IRIs | Direct imports |','| --- | --- | --- |']
    for module in MODULES:
        graph=graphs[(root/RELEASE/(module+'.ttl')).resolve()]
        ontologies=sorted(str(s) for s in graph.subjects(RDF.type,OWL.Ontology))
        versions=sorted(str(o) for o in graph.objects(None,OWL.versionIRI))
        imports=sorted(str(o) for o in graph.objects(None,OWL.imports))
        md.append('| '+module+' | '+', '.join(ontologies+versions)+' | '+', '.join(imports)+' |')
    md += ['','## Complete local entity index','']
    for iri,values in sorted(declarations.items()):
        subject=URIRef(iri)
        md += ['### `'+iri+'`','',', '.join(kind+' in `'+path+'`' for kind,path in sorted(values)), '']
        for pred in [RDF.type,RDFS.subClassOf,RDFS.domain,RDFS.range,OWL.disjointWith,OWL.inverseOf]:
            vals=sorted(str(o) for o in local.objects(subject,pred) if isinstance(o,URIRef))
            if vals: md.append('- `'+str(pred)+'`: '+', '.join('`'+v+'`' for v in vals))
        md.append('')
    return {OUT/'asserted-closure.nt':nt,OUT/'entity-inventory.csv':csv_file.getvalue(),OUT/'source-manifest.json':json.dumps(report,indent=2,sort_keys=True)+'\n',OUT/'generated-reference.md':'\n'.join(md).rstrip()+'\n'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    outputs=build()
    for path,value in outputs.items():
        target=ROOT/path
        if args.check:
            if not target.exists() or target.read_text()!=value: raise SystemExit('RC4_FORMAL_REFERENCE_DRIFT: '+str(path))
        else:
            target.parent.mkdir(parents=True,exist_ok=True);target.write_text(value)
    print('RC4_ASSERTED_REFERENCE_PASS: 7 modules; 8 closure files; 116 declared local entities; 87 conceptual/relation rows')
if __name__=='__main__':main()
