#!/usr/bin/env python3
"""Version-bound, synthetic tests for the two rc.4 corrections."""
import argparse,csv,json,hashlib
from pathlib import Path
from rdflib import Graph,Namespace,RDF,RDFS,OWL,Literal,XSD,URIRef,BNode
from pyshacl import validate
ROOT=Path(__file__).resolve().parents[1];V='0.2.0-rc.4';D=ROOT/'ontology/releases'/V
SR=Namespace('urn:semrisk:entity:');AC=Namespace('urn:semrisk:profile:assessment-context:');I=Namespace('urn:semrisk:profile:information-state:');G=Namespace('http://purl.org/nemo/gufo#');EX=Namespace('urn:semrisk:run8:')
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def c(n):return SR[f'SR-CPT-{n:03}']
def r(n):return SR[f'SR-REL-{n:03}']
def fixture():return Graph().parse(ROOT/f'testdata/foundational/exposure-scale-v{V}.ttl')
def clone(g):h=Graph();h+=g;return h
def shapes():
 g=Graph()
 for p in ['assessment-context-v0.2.0-rc.1.ttl','semantic-identity-v0.2.0-rc.3.ttl',f'exposure-scale-v{V}.ttl']:g.parse(ROOT/'shapes'/p)
 return g
def check(g):return validate(g,shacl_graph=shapes(),inference='none',meta_shacl=True)
def at(g,t):return sorted(tuple(map(str,x)) for x in g.query((ROOT/f'rules/core/exposure-at-v{V}.rq').read_text(),initBindings={'asOf':Literal(t,datatype=XSD.dateTime)}))
def run():
 tests=[]
 def test(id,ok,detail):
  tests.append(dict(id=id,passed=bool(ok),detail=detail))
  if not ok:raise AssertionError(id+': '+str(detail))
 d=fixture();ok,_,msg=check(d);test('POSITIVE',ok,msg)
 cases=[('E01','missing subject','MinCountConstraintComponent'),('E02','missing source','MinCountConstraintComponent'),('E03','two subjects','MaxCountConstraintComponent'),('E04','literal source','NodeKindConstraintComponent'),('E05','untyped subject','ClassConstraintComponent'),('E06','untyped source','ClassConstraintComponent'),('E07','reversed interval','LessThanConstraintComponent'),('E08','timezone missing','PatternConstraintComponent'),('E09','exposure as assessment result','NotConstraintComponent'),('E10','endpoint relation without exposure type','ClassConstraintComponent'),('S01','scale missing artifact parent','MinCountConstraintComponent'),('S02','scale missing abstract content','MinCountConstraintComponent'),('S03','scale self-version','VERSION_SELF'),('S04','scale as abstract value','NotConstraintComponent'),('S05','reversed scale bounds','LessThanOrEqualsConstraintComponent'),('S06','scale dimension missing','MinCountConstraintComponent'),('S07','version identity not explicit','VERSION_SELF')]
 for id,desc,marker in cases:
  h=clone(d)
  if id=='E01':h.remove((EX.exposureA,r(39),None))
  if id=='E02':h.remove((EX.exposureA,r(40),None))
  if id=='E03':h.add((EX.otherSubject,RDF.type,c(2)));h.add((EX.exposureA,r(39),EX.otherSubject))
  if id=='E04':h.set((EX.exposureA,r(40),Literal('source')))
  if id=='E05':h.remove((EX.subject,RDF.type,c(2)))
  if id=='E06':h.remove((EX.source,RDF.type,c(3)))
  if id=='E07':h.set((EX.exposureA,AC.validTo,Literal('2026-09-30T00:00:00Z',datatype=XSD.dateTime)))
  if id=='E08':h.set((EX.exposureA,AC.validFrom,Literal('2026-10-01T00:00:00',datatype=XSD.dateTime)))
  if id=='E09':h.add((EX.exposureA,RDF.type,c(13)))
  if id=='E10':h.remove((EX.exposureA,RDF.type,c(10)))
  if id=='S01':h.remove((EX.scaleA,I.versionOf,None))
  if id=='S02':h.remove((EX.scaleA,I.expressesContent,None))
  if id=='S03':h.set((EX.scaleA,I.versionOf,EX.scaleA))
  if id=='S04':h.add((EX.scaleA,RDF.type,G.AbstractIndividual))
  if id=='S05':h.set((EX.scaleA,AC.minimum,Literal('2.0',datatype=XSD.decimal)))
  if id=='S06':h.remove((EX.scaleA,AC.dimension,None))
  if id=='S07':h.remove((EX.scaleA,OWL.differentFrom,EX.series))
  ok,_,msg=check(h);test(id,not ok and marker in msg,desc+' rejected by '+marker)
 test('INTERVAL-BEFORE',[x[0] for x in at(d,'2026-10-04T23:59:59Z')]==[str(EX.exposureA)],'Before boundary only A holds.')
 test('INTERVAL-BOUNDARY',[x[0] for x in at(d,'2026-10-05T00:00:00Z')]==[str(EX.exposureB)],'Adjacent interval, not two active copies.')
 test('INTERVAL-ZONE',at(d,'2026-10-05T03:30:00+03:30')==at(d,'2026-10-05T00:00:00Z'),'Same instant, same answers.')
 h=clone(d);h.remove((EX.exposureB,AC.validFrom,None));test('UNKNOWN-START',not at(h,'2026-10-05T00:00:00Z'),'Unknown onset is not fabricated as current exposure.')
 test('UNBOUND-TIME',not list(d.query((ROOT/f'rules/core/exposure-at-v{V}.rq').read_text())),'No implicit wall-clock time.')
 h=clone(d);h.add((EX.exposureC,RDF.type,c(10)));h.add((EX.exposureC,r(39),EX.subject));h.add((EX.exposureC,r(40),EX.source));test('ATEMPORAL-ALLOWED',check(h)[0],'Strict endpoint profile allows unknown periods; as-of query remains narrower.')
 g=Graph()
 for m in MODULES:g.parse(D/f'{m}.ttl')
 test('SCALE-IDENTITY',(AC.NumericScale,RDFS.subClassOf,I.ArtifactVersion) in g and (AC.NumericScale,RDF.type,G.SubKind) in g,'Specific inherited identity; no invented stereotype.')
 anc=set(g.transitive_objects(AC.NumericScale,RDFS.subClassOf));providers={x for x in anc if (x,RDF.type,G.Kind) in g};bad={G.Role,G.RoleMixin,G.Phase,G.PhaseMixin}
 test('SCALE-SORTAL-CONSTRAINTS',providers=={I.ManagedInformationArtifact} and not any((x,RDF.type,t) in g for x in anc for t in bad),'Subkind has one named identity provider and no anti-rigid ancestor in the local taxonomy.')
 test('EXPOSURE-ENDPOINTS',all((r(n),RDFS.domain,c(10)) in g and (r(n),RDFS.range,c(t)) in g for n,t in [(39,2),(40,3)]),'Registered endpoint semantics.')
 test('NO-FUNCTIONALITY',all((r(n),RDF.type,OWL.FunctionalProperty) not in g for n in [39,40]),'SHACL maxima not global OWL keys.')
 test('NO-IDENTITY-KEY',not list(g.triples((None,OWL.hasKey,None))),'Equal score/bounds do not collapse issued versions.')
 rows=list(csv.DictReader((ROOT/f'foundational/exposure-scale-v{V}/relation-formal-audit.csv').open()));test('RELATION-RETENTION',len(rows)==40 and {x['relation_id'] for x in rows}=={f'SR-REL-{i:03}' for i in range(1,41)},'All old 38 retained plus exactly two.')
 # Frozen prior tests remain distinct from new semantic guarantees.
 from check_semantic_identity import run as old_run
 old=old_run();test('RC3-REGRESSION',old['passed']==old['total']==31,'31 previous bounded tests pass unchanged.')
 return dict(version=V,total=len(tests),passed=sum(x['passed'] for x in tests),negative_cases=len(cases),tests=tests,limits=['Synthetic fixtures only','Full OntoUML antipattern/native-editor checks remain open','Scale/content and workflow SQL parity remains incomplete'])

def assemble():
 from xml.etree import ElementTree as ET
 ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'};cat=ET.parse(D/'catalog.xml');binding={x.attrib['name']:(D/x.attrib['uri']).resolve() for x in cat.findall('c:uri',ns)}
 g=Graph();todo=[D/f'{m}.ttl' for m in MODULES];seen=set()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p);h=Graph().parse(p)
  for iri in h.objects(None,OWL.imports):
   if str(iri) not in binding:raise ValueError('Unbound import '+str(iri))
   todo.append(binding[str(iri)])
  g+=h
 g.remove((None,OWL.imports,None));g+=fixture();out=ROOT/'build/exposure-scale';out.mkdir(parents=True,exist_ok=True)
 g.serialize(out/'positive.owl',format='xml')
 expected=[(EX.scaleA,I.ArtifactVersion),(EX.scaleA,I.ManagedInformationArtifact),(EX.scaleA,G.FunctionalComplex),(EX.exposureA,G.Situation)]
 (out/'expected-entailments.json').write_text(json.dumps([[str(s),str(t)] for s,t in expected],indent=2)+'\n')
 # Actual satisfiable countermodels, not simple absence from an asserted graph.
 h=clone(g);z=BNode();h.add((z,RDF.type,OWL.Restriction));h.add((z,OWL.onProperty,r(4)));h.add((z,OWL.maxCardinality,Literal(0,datatype=XSD.nonNegativeInteger)));h.add((EX.exposureA,RDF.type,z));h.serialize(out/'no-forced-consequence.owl',format='xml')
 h=clone(g);h.add((EX.incompleteExposure,RDF.type,c(10)))
 for prop in [r(39),r(40)]:
  z=BNode();h.add((z,RDF.type,OWL.Restriction));h.add((z,OWL.onProperty,prop));h.add((z,OWL.maxCardinality,Literal(0,datatype=XSD.nonNegativeInteger)));h.add((EX.incompleteExposure,RDF.type,z))
 h.serialize(out/'open-world-incomplete.owl',format='xml')
 for name,subject,typ in [('scale-as-abstract',EX.scaleA,G.AbstractIndividual),('exposure-as-value',EX.exposureA,G.QualityValue)]:
  h=clone(g);h.add((subject,RDF.type,typ));h.serialize(out/(name+'.owl'),format='xml')
 (out/'assembly.json').write_text(json.dumps(dict(source_files=sorted(str(p.relative_to(ROOT)) for p in seen),positive_triples=len(g),type_entailments=4,consistent_countermodels=2,inconsistent_probes=2,distinct_equal_scales='owl:differentFrom asserted in positive world'),indent=2)+'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--assemble',action='store_true');a=p.parse_args();result=run();(ROOT/f'evaluation/exposure-scale/v{V}/results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='tests'},indent=2))
 if a.assemble:assemble()
