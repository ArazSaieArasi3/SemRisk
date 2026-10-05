#!/usr/bin/env python3
"""Bind successor sources; preserve historical candidate and offline resolution."""
import argparse,csv,hashlib,json
from pathlib import Path
from xml.etree import ElementTree
from rdflib import Graph,RDF,OWL,URIRef

ROOT=Path(__file__).resolve().parents[1];V='0.2.0-rc.1';D=ROOT/'ontology/releases'/V
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def source_paths():
 return [f'ontology/releases/{V}/{m}.ttl' for m in MODULES]+[
  f'ontology/releases/{V}/catalog.xml','ontology/vendor/gufo-v1.0.0.ttl',
  f'shapes/assessment-context-v{V}.ttl',f'rules/enterprise/risk-owners-at-v{V}.rq',
  'relational/sql/V007__qualified_assessment_context.sql','relational/sql/rollback/U007__qualified_assessment_context.sql',
  'relational/scripts/qualified_context_io.py','tools/check_qualified_context.py','tools/check_qualified_context_postgres.py',
  'tools/requirements-qualified-context.txt',f'testdata/temporal/qualified-context-v{V}.ttl']
def manifest():
 return {'candidate_version':V,'state':'OPERATIONAL_PROFILE_CANDIDATE_NOT_PUBLICATION_RELEASE',
  'baseline_commit':'6598291896e900efc92b6d6a9cf583a3f4a41e44',
  'change_classes':{'six_base_modules':'NON_SEMANTIC_VERSION_AND_TRIGGER_ANNOTATION','assessment_context':'ADDITIVE_COMPATIBLE','qualified_shapes':'CONSTRAINT_CHANGE_OPT_IN','projection':'PROJECTION_ONLY_ADDITIVE'},
  'modules':[{'name':m,'path':f'ontology/releases/{V}/{m}.ttl','ontology_iri':f'urn:semrisk:ontology:{m}','version_iri':f'urn:semrisk:ontology:{m}:{V}'} for m in MODULES],
  'legacy_candidate':'ontology/p1-r2-candidate-manifest.yaml','legacy_evidence_preserved':True,
  'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths()},
  'evidence_directory':f'evaluation/temporal/v{V}/','publication_ready':False,'original_cq_count':40,
  'limits':['Synthetic numeric-profile execution only','No new empirical risk records or expert responses','No general conservative-extension/concurrency theorem','Full OntoUML and final manuscript remain open']}
def assemble():
 catalog=ElementTree.parse(D/'catalog.xml');ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'}
 bindings={x.attrib['name']:(D/x.attrib['uri']).resolve() for x in catalog.findall('c:uri',ns)}
 inputs=[D/f'{m}.ttl' for m in MODULES];seen=set();g=Graph()
 while inputs:
  path=inputs.pop()
  if path in seen:continue
  seen.add(path);part=Graph().parse(path)
  for iri in part.objects(None,OWL.imports):
   if str(iri) not in bindings:raise ValueError('unresolved import '+str(iri))
   inputs.append(bindings[str(iri)])
  g+=part
 # All imports already materialized from exact offline bindings. Strip only
 # import directives to prevent a reasoner from doing ambient network I/O.
 g.remove((None,OWL.imports,None));g.parse(ROOT/f'testdata/temporal/qualified-context-v{V}.ttl')
 output=ROOT/'build/qualified-context';output.mkdir(parents=True,exist_ok=True)
 g.serialize(destination=str(output/'closure.owl'),format='xml')
 (output/'assembly.json').write_text(json.dumps({'source_files':sorted(str(x.relative_to(ROOT)) for x in seen),'asserted_triples_with_fixture':len(g),'imports_resolved_offline':True},indent=2)+'\n')
 print('Successor closure assembled from',len(seen),'exact files.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--assemble',action='store_true');a=p.parse_args()
 text=json.dumps(manifest(),indent=2)+'\n';path=D/'manifest.json'
 if a.check:
  assert path.read_text()==text,'Candidate source hashes drifted; review/version the source delta before regenerating.'
 else:path.write_text(text)
 if a.assemble:assemble()
 print('Candidate binding verified' if a.check else 'Candidate binding generated')
