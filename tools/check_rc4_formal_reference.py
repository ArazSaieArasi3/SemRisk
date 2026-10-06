#!/usr/bin/env python3
"""Check the current formal source projection and reject deliberate corruptions."""
import json
import re
import shutil
import tempfile
from pathlib import Path
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL
from generate_rc4_formal_reference import ROOT, OUT, RELEASE, MODULES, build, closure

SR=Namespace('urn:semrisk:entity:');AC=Namespace('urn:semrisk:profile:assessment-context:');IST=Namespace('urn:semrisk:profile:information-state:');GUFO=Namespace('http://purl.org/nemo/gufo#')


def check(root=ROOT):
    outputs=build(root)
    for path,expected in outputs.items():
        if not (root/path).is_file() or (root/path).read_text()!=expected:
            raise ValueError('GENERATED_DRIFT: '+str(path))
    doc=(root/'docs/formal/formal-ontology-description-rc4.md').read_text()
    for letter in 'ABCDEFGHIJ':
        if not re.search(r'^## FD-'+letter+r'\b',doc,re.M):raise ValueError('MISSING_FD_'+letter)
    g=Graph()
    for module in MODULES:g.parse(root/RELEASE/(module+'.ttl'))
    asserted=[(SR['SR-CPT-006'],RDFS.subClassOf,GUFO.SituationType),(SR['SR-CPT-007'],RDFS.subClassOf,GUFO.Event),(SR['SR-CPT-011'],RDFS.subClassOf,GUFO.Event),(SR['SR-CPT-035'],RDFS.subClassOf,GUFO.Situation),(SR['SR-CPT-036'],RDFS.subClassOf,GUFO.QualityValue),(AC.NumericScale,RDFS.subClassOf,IST.ArtifactVersion),(AC.NumericScale,RDF.type,GUFO.SubKind),(SR['SR-REL-038'],RDF.type,OWL.AnnotationProperty)]
    for s,p,o in asserted:
        if (s,p,o) not in g:raise ValueError('CURATED_AXIOM_DRIFT: '+str((s,p,o)))
    for a,b in [(1,33),(6,7),(11,13),(35,36)]:
        s,o=SR[f'SR-CPT-{a:03}'],SR[f'SR-CPT-{b:03}']
        if (s,OWL.disjointWith,o) not in g and (o,OWL.disjointWith,s) not in g:raise ValueError('CURATED_DISJOINTNESS_DRIFT')
    for n,target in [(39,2),(40,3)]:
        p=SR[f'SR-REL-{n:03}']
        if (p,RDFS.domain,SR['SR-CPT-010']) not in g or (p,RDFS.range,SR[f'SR-CPT-{target:03}']) not in g:raise ValueError('EXPOSURE_ENDPOINT_DRIFT')
        if (p,RDF.type,OWL.FunctionalProperty) in g:raise ValueError('INVENTED_FUNCTIONALITY')
    if list(g.triples((None,OWL.hasKey,None))):raise ValueError('INVENTED_KEY')
    report=json.loads(outputs[OUT/'source-manifest.json'])
    if report['historical_cq_classification']!={'conceptual_only':6,'deferred':1,'executable':26,'partially_executable':7}:raise ValueError('HISTORICAL_CQ_DRIFT')
    if report['declared_entity_count']!=116 or len(report['named_shapes'])!=12:raise ValueError('PROFILE_COUNT_DRIFT')
    # Explicit guardrails in the projection, checked separately from actual semantics.
    for phrase in ['#125 is deferred','not a fresh full rc.4 execution claim','not an assessment score','inference disabled','#117','10/10 dimensions are documented']:
        if phrase not in doc:raise ValueError('MISSING_SCOPE_BOUNDARY: '+phrase)
    return report


def negative_controls():
    # Mutate only fresh temporary copies, never the checked-out sources.
    cases=['generated_inventory','missing_section','missing_import','escaping_import','omitted_module','changed_axiom','removed_metadata','shape_drift','cq_drift']
    failures=[]
    markers={'generated_inventory':'GENERATED_DRIFT', 'missing_section':'MISSING_FD_H', 'missing_import':'UNBOUND_IMPORT', 'escaping_import':'CATALOG_ESCAPE', 'omitted_module':'No such file', 'changed_axiom':'CURATED_AXIOM_DRIFT', 'removed_metadata':'DECLARATION_DRIFT', 'shape_drift':'GENERATED_DRIFT', 'cq_drift':'HISTORICAL_CQ_DRIFT'}
    manifest=json.loads((ROOT/OUT/'source-manifest.json').read_text())
    required={r['path'] for r in manifest['sources']}|{str(p) for p in build()}|{'docs/formal/formal-ontology-description-rc4.md'}
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='semrisk-formal-negative-') as td:
            root=Path(td)
            for path in required:
                dest=root/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/path,dest)
            if case=='generated_inventory':
                p=root/OUT/'entity-inventory.csv';p.write_text(p.read_text().replace('annotation_property','object_property'))
            elif case=='missing_section':
                p=root/'docs/formal/formal-ontology-description-rc4.md';p.write_text(p.read_text().replace('## FD-H','## REMOVED-H'))
            elif case=='missing_import':
                p=root/RELEASE/'catalog.xml';p.write_text(p.read_text().replace('http://purl.org/nemo/gufo#/1.0.0','urn:unbound:gufo'))
            elif case=='escaping_import':
                p=root/RELEASE/'catalog.xml';p.write_text(p.read_text().replace('../../vendor/gufo-v1.0.0.ttl','../../../../../outside.ttl'))
            elif case=='omitted_module':(root/RELEASE/'pharma.ttl').unlink()
            elif case=='changed_axiom':
                p=root/RELEASE/'assessment-context.ttl';p.write_text(p.read_text().replace('rdfs:subClassOf ist:ArtifactVersion','rdfs:subClassOf ist:InformationContent'))
            elif case=='removed_metadata':
                p=root/RELEASE/'mappings.ttl';p.write_text(p.read_text().replace('owl:AnnotationProperty','owl:ObjectProperty'))
            elif case=='shape_drift':
                p=root/'shapes/exposure-scale-v0.2.0-rc.4.ttl';p.write_text(p.read_text().replace('sh:minCount 1','sh:minCount 0'))
            elif case=='cq_drift':
                p=root/'evaluation/cq/issue52-cq-results-v1.0.csv';p.write_text(p.read_text().replace('conceptual_only','executable',1))
            if case in ['changed_axiom','cq_drift']:
                for path,value in build(root).items():(root/path).write_text(value)
            try:check(root)
            except (ValueError,AssertionError,FileNotFoundError) as exc:
                if markers[case] not in str(exc):raise AssertionError('WRONG_REJECTION: '+case+': '+str(exc))
                failures.append(case)
            else:raise AssertionError('NEGATIVE_ACCEPTED: '+case)
    return failures

if __name__=='__main__':
    report=check();neg=negative_controls()
    print(json.dumps({'result':'PASS_BOUNDED_FORMAL_REFERENCE','dimensions':10,'local_declarations':report['declared_entity_count'],'asserted_triples':report['asserted_triples'],'rejected_corruptions':neg,'negative_count':len(neg),'limits':['Documentation/source projection only','No scholarly release or full SQL parity','Reasoning is executed separately']},indent=2))
