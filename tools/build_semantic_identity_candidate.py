#!/usr/bin/env python3
"""Exact source binding and isolated reasoner probes for rc.3."""
import argparse,hashlib,json
from pathlib import Path
from rdflib import Graph,RDF,RDFS,OWL,BNode,Literal,XSD,URIRef
from xml.etree import ElementTree
from check_semantic_identity import ROOT,V,D,MODULES,EX,I,G,SR,fixture

def sources():
 return [f'ontology/releases/{V}/{m}.ttl' for m in MODULES]+[f'ontology/releases/{V}/catalog.xml',f'ontology/releases/{V}/profile-iri-registry.csv',f'ontology/releases/{V}/information-state-iri-registry.csv',
 'ontology/vendor/gufo-v1.0.0.ttl',f'shapes/semantic-identity-v{V}.ttl',f'testdata/foundational/semantic-identity-v{V}.ttl',f'rules/enterprise/workflow-at-v{V}.rq',
 'tools/check_semantic_identity.py','tools/build_semantic_identity_candidate.py','tools/adapt_scenario_declarations.py',f'foundational/semantic-identity-v{V}/decisions.md',f'foundational/semantic-identity-v{V}/concept-category-audit.csv',f'foundational/semantic-identity-v{V}/relation-formal-audit.csv',f'evaluation/semantic-identity/v{V}/acceptance-contract.md','.github/workflows/paper1-semantic-identity.yml']
def manifest():
 old=ROOT/'ontology/releases'
 return dict(candidate_version=V,previous_candidate='0.2.0-rc.2',baseline_commit='7d95a05f1b5ef7c67f9750e09e2da9f8d4e5d78c',publication_ready=False,module_count=7,domain_concepts=dict(local_classes=35,markers=4,undeclared=8),operational_helpers=dict(existing_terms=26,new_classes=5,new_object_properties=6),
 semantic_changes=['Scenario is now a subclass of SituationType; explicit punned declarations for scenario types','Managed information artifact, immutable version and abstract content are distinct','Workflow values are QualityValues; temporal attribution situations are separate'],
 source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources()},
 historical_release_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for v in ['0.2.0-rc.1','0.2.0-rc.2'] for p in sorted((old/v).rglob('*')) if p.is_file()},
 limits=['Full editable OntoUML pending','New helpers not yet in SQL round-trip','No new real case or expert evidence'])
def assemble():
 cat=ElementTree.parse(D/'catalog.xml');ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'}
 bind={x.attrib['name']:(D/x.attrib['uri']).resolve() for x in cat.findall('c:uri',ns)};todo=[D/f'{m}.ttl' for m in MODULES];seen=set();g=Graph()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p);part=Graph().parse(p)
  for iri in part.objects(None,OWL.imports):
   if str(iri) not in bind:raise ValueError('Unresolved import '+str(iri))
   todo.append(bind[str(iri)])
  g+=part
 g.remove((None,OWL.imports,None));g+=fixture()
 # Infer every information row's artifact membership from the conceptual class alone.
 expected=[]
 for n in [12,13,14,15,16,17,18,19,20,23,24,25,26,27,32,33,34]:
  x=EX[f'information{n}'];g.add((x,RDF.type,SR[f'SR-CPT-{n:03}']));expected.append([str(x),str(I.ManagedInformationArtifact)])
 expected.extend([[str(EX.scenario),str(G.SituationType)],[str(EX.open),str(G.QualityValue)],[str(EX.assignmentA),str(G.Situation)],[str(EX.event),str(SR['SR-CPT-007'])]])
 out=ROOT/'build/semantic-identity';out.mkdir(parents=True,exist_ok=True)
 g.serialize(out/'positive.owl',format='xml')
 # Satisfiable worlds establish non-entailments, not merely absence from the asserted graph.
 h=Graph();h+=g;b=BNode();h.add((b,RDF.type,OWL.Restriction));h.add((b,OWL.onProperty,SR['SR-REL-003']));h.add((b,OWL.maxCardinality,Literal(0,datatype=XSD.nonNegativeInteger)));h.add((EX.scenario,RDF.type,b));h.serialize(out/'no-realization.owl',format='xml')
 for name,subject,typ in [('content-as-artifact',EX.content,I.ManagedInformationArtifact),('value-as-quality',EX.open,G.Quality),('scenario-as-individual',EX.scenario,G.Individual)]:
  h=Graph();h+=g;h.add((subject,RDF.type,typ));h.serialize(out/f'{name}.owl',format='xml')
 (out/'expected-entailments.json').write_text(json.dumps(expected,indent=2)+'\n')
 (out/'assembly.json').write_text(json.dumps(dict(version=V,source_files=sorted(str(p.relative_to(ROOT)) for p in seen),offline=True,positive_triples=len(g),expected_new_type_assertions=len(expected),countermodels=1,inconsistent_worlds=3),indent=2)+'\n')
 print('SEMANTIC_IDENTITY_ASSEMBLED',len(seen),'sources;',len(expected),'expected entailments')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--assemble',action='store_true');a=p.parse_args();s=json.dumps(manifest(),indent=2)+'\n'
 if a.check:assert (D/'manifest.json').read_text()==s,'Candidate or frozen release bytes changed'
 else:(D/'manifest.json').write_text(s)
 if a.assemble:assemble()
 print('SEMANTIC_IDENTITY_BINDING_PASS')
