#!/usr/bin/env python3
"""Behavioral checks for rc.3 identity semantics; synthetic, bounded and reproducible."""
import argparse,csv,json
from pathlib import Path
from rdflib import Graph,RDF,RDFS,OWL,Namespace,Literal,XSD
from pyshacl import validate
from adapt_scenario_declarations import adapt
ROOT=Path(__file__).resolve().parents[1];V='0.2.0-rc.3';D=ROOT/'ontology/releases'/V
SR=Namespace('urn:semrisk:entity:');I=Namespace('urn:semrisk:profile:information-state:');AC=Namespace('urn:semrisk:profile:assessment-context:');G=Namespace('http://purl.org/nemo/gufo#');EX=Namespace('urn:semrisk:run6:')
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def fixture():return Graph().parse(ROOT/f'testdata/foundational/semantic-identity-v{V}.ttl')
def clone(g):h=Graph();h+=g;return h
def check(g):return validate(g,shacl_graph=Graph().parse(ROOT/f'shapes/semantic-identity-v{V}.ttl'),inference='none',meta_shacl=True)
def at(g,instant):
 return sorted(tuple(str(x).removeprefix(str(EX)) for x in row) for row in g.query((ROOT/f'rules/enterprise/workflow-at-v{V}.rq').read_text(),initBindings={'asOf':Literal(instant,datatype=XSD.dateTime)}))
def run():
 tests=[]
 def test(id_,ok,detail):
  tests.append(dict(id=id_,passed=bool(ok),detail=detail))
  if not ok:raise AssertionError(id_+': '+str(detail))
 d=fixture();ok,_,msg=check(d);test('POSITIVE',ok,msg)
 cases=[('S01','scenario lacks class declaration','HasValueConstraintComponent'),('S02','scenario lacks Situation superclass','HasValueConstraintComponent'),('S03','scenario confused with individual','NotConstraintComponent'),('I01','version missing parent','MinCountConstraintComponent'),('I02','version missing content','MinCountConstraintComponent'),('I03','version is its parent','VERSION_SELF'),('I04','version aliases its parent','VERSION_SELF'),('I05','content is only a concrete artifact','ClassConstraintComponent'),('W01','missing scheme','MinCountConstraintComponent'),('W02','value is a bearer quality','NotConstraintComponent'),('W03','value is RiskState','NotConstraintComponent'),('W04','scheme mismatch','WORKFLOW_SCHEME'),('W05','missing interval start','MinCountConstraintComponent'),('W06','timezone missing','PatternConstraintComponent'),('W07','zero interval','LessThanConstraintComponent'),('W08','overlapping assignments','WORKFLOW_OVERLAP'),('W09','multiple record bearers','MaxCountConstraintComponent')]
 for id_,desc,marker in cases:
  h=clone(d)
  if id_=='S01':h.remove((EX.scenario,RDF.type,OWL.Class))
  if id_=='S02':h.remove((EX.scenario,RDFS.subClassOf,G.Situation))
  if id_=='S03':h.add((EX.scenario,RDF.type,G.Individual))
  if id_=='I01':h.remove((EX.versionA,I.versionOf,None))
  if id_=='I02':h.remove((EX.versionA,I.expressesContent,None))
  if id_=='I03':h.set((EX.versionA,I.versionOf,EX.versionA))
  if id_=='I04':h.add((EX.versionA,OWL.sameAs,EX.entryA))
  if id_=='I05':h.remove((EX.content,RDF.type,I.InformationContent));h.add((EX.content,RDF.type,I.ManagedInformationArtifact))
  if id_=='W01':h.remove((EX.open,I.inScheme,None))
  if id_=='W02':h.add((EX.open,RDF.type,G.Quality))
  if id_=='W03':h.add((EX.open,RDF.type,SR['SR-CPT-035']))
  if id_=='W04':h.add((EX.otherScheme,RDF.type,I.WorkflowSchemeVersion));h.set((EX.assignmentA,I.scheme,EX.otherScheme))
  if id_=='W05':h.remove((EX.assignmentA,AC.validFrom,None))
  if id_=='W06':h.set((EX.assignmentA,AC.validFrom,Literal('2026-10-01T00:00:00',datatype=XSD.dateTime)))
  if id_=='W07':h.set((EX.assignmentA,AC.validTo,Literal('2026-10-01T00:00:00Z',datatype=XSD.dateTime)))
  if id_=='W08':h.set((EX.assignmentC,AC.validFrom,Literal('2026-10-04T00:00:00Z',datatype=XSD.dateTime)))
  if id_=='W09':h.add((EX.assignmentA,I.record,EX.entryB))
  ok,_,msg=check(h);test(id_,not ok and marker in msg,desc+' rejected by '+marker)
 test('HALF-OPEN-BEFORE',at(d,'2026-10-04T23:59:59Z')==[('entryA','scheme','open'),('entryB','scheme','open')],'One reusable Open value applies to two different records.')
 test('HALF-OPEN-BOUNDARY',at(d,'2026-10-05T00:00:00Z')==[('entryA','scheme','closed'),('entryB','scheme','open')],'Exact boundary excludes expired assignment.')
 h=clone(d);h.add((EX.entryA,SR['SR-REL-030'],EX.open));test('SNAPSHOT-NOT-HISTORY',at(h,'2026-10-05T00:00:00Z')==at(d,'2026-10-05T00:00:00Z'),'Unqualified snapshot does not overwrite historical answers.')
 # A legacy scenario adapter adds only metadata, never occurrence or realization assertions.
 h=Graph();h.add((EX.legacy,RDF.type,SR['SR-CPT-006']));a=adapt(h)
 test('ADAPTER-EXACT',set(a)-set(h)=={(EX.legacy,RDF.type,OWL.Class),(EX.legacy,RDFS.subClassOf,G.Situation)},'Exactly two declaration triples; no occurrence invented.')
 test('ADAPTER-IDEMPOTENT',set(a)==set(adapt(a)),'Rerunning adapter does not mutate identity.')
 g=Graph()
 for m in MODULES:g.parse(D/f'{m}.ttl')
 test('SCENARIO-LEVEL',(SR['SR-CPT-006'],RDFS.subClassOf,G.SituationType) in g and (SR['SR-CPT-006'],RDF.type,G.SituationType) not in g,'Instance level corrected; not a metadata relabel.')
 rows=list(csv.DictReader((ROOT/f'foundational/semantic-identity-v{V}/concept-category-audit.csv').open()))
 test('47-CONCEPT-COVERAGE',len(rows)==47 and len({r['semantic_id'] for r in rows})==47,'47 unique domain concept dispositions.')
 canonical={r['semantic_id']:r for r in csv.DictReader((ROOT/'conceptualization/core/core-concept-registry-v0.1.csv').open())}
 test('REGISTRY-DEFINITIONS',all(r['definition']==canonical[r['semantic_id']]['definition'] and (r['formal_status']!='LOCAL_CLASS' or str(g.value(SR[r['semantic_id']],RDFS.comment))==r['definition']) for r in rows),'All audit definitions match canonical registry; all 35 declared class definitions also match OWL.')
 pending={'NEEDS_INFORMATION_IDENTITY_PATTERN','BLOCKED_TYPE_INSTANCE_LEVEL','NEEDS_VALUE_VS_QUALITY_VIEW'}
 test('3-DECISIONS-RESOLVED',not any(r['diagram_gate'] in pending for r in rows),'Editable-model gate remains explicit.')
 rel=list(csv.DictReader((ROOT/f'foundational/semantic-identity-v{V}/relation-formal-audit.csv').open()));test('38-RELATION-COVERAGE',len(rel)==38,'All original registered relation decisions retained.')
 test('NO-IDENTITY-KEY',not list(g.triples((None,OWL.hasKey,None))) and not list(g.triples((I.expressesContent,RDF.type,OWL.InverseFunctionalProperty))),'No equality from content or mutable fields.')
 # Existing temporal profile actually executed against its original data contract.
 from check_qualified_context import fixture as tf,validate_graph,owner_rows
 t=tf();test('TEMPORAL-PROFILE',validate_graph(t)[0],'Existing temporal SHACL data remains valid.')
 test('OWNER-ANSWERS',owner_rows(t,'2026-10-05T08:00:00Z')==owner_rows(t+d,'2026-10-05T08:00:00Z'),'New workflow/type/content fixture does not change assignee-derived owners.')
 return dict(candidate_version=V,total=len(tests),passed=sum(x['passed'] for x in tests),negative_cases=len(cases),tests=tests,limits=['Synthetic fixtures only','No complete OntoUML validation','New helpers not included in SQL round-trip contract','Immutability across storage revisions is a governance contract, not enforced by OWL or a single SHACL snapshot'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=run()
 if a.write:(ROOT/f'evaluation/semantic-identity/v{V}/results.json').write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:v for k,v in r.items() if k!='tests'},indent=2))
