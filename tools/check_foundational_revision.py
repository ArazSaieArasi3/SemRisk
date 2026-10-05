#!/usr/bin/env python3
"""Bounded source/shape regressions. Not a complete OntoUML antipattern detector."""
from pathlib import Path
import argparse,csv,json,re,hashlib
from rdflib import Graph,RDF,RDFS,OWL,SKOS,Namespace,URIRef,Literal
from rdflib.compare import isomorphic
from pyshacl import validate
from check_qualified_context import owner_rows,fixture as temporal_fixture,validate_graph as temporal_validate
ROOT=Path(__file__).resolve().parents[1];V='0.2.0-rc.2';OLD='0.2.0-rc.1'
D=ROOT/'ontology/releases'/V;E=ROOT/'evaluation/foundational/2026-10-05'
SR=Namespace('urn:semrisk:entity:');AC=Namespace('urn:semrisk:profile:assessment-context:');EX=Namespace('urn:semrisk:run5:');GUFO=Namespace('http://purl.org/nemo/gufo#')
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def c(n):return SR[f'SR-CPT-{n:03}']
def r(n):return SR[f'SR-REL-{n:03}']
def graph():
 g=Graph()
 for m in MODULES:g.parse(D/f'{m}.ttl')
 return g
def data():return Graph().parse(ROOT/f'testdata/foundational/grounded-responsibility-v{V}.ttl')
def clone(g):h=Graph();h+=g;return h
def check_shape(g):
 # Only generic Endurant category is required in this explicit evidence profile.
 # No inference is used to invent missing witnesses.
 return validate(g,shacl_graph=Graph().parse(ROOT/f'shapes/foundational-evidence-v{V}.ttl'),inference='none',meta_shacl=True)
def canonical(g):
 h=Graph()
 for s,p,o in g:
  if isinstance(s,URIRef):s=URIRef(str(s).replace(V,OLD))
  if isinstance(o,URIRef):o=URIRef(str(o).replace(V,OLD))
  if isinstance(o,Literal) and str(o)==V:o=Literal(OLD,lang=o.language,datatype=o.datatype)
  h.add((s,p,o))
 return h
def run():
 out=[]
 def test(id_,ok,detail):
  out.append(dict(id=id_,passed=bool(ok),details=detail))
  if not ok:raise AssertionError(id_+': '+str(detail))
 delta=json.loads((ROOT/'foundational/revision-2026-10-05/definition-delta.json').read_text());g=graph()
 for m in MODULES:
  old=Graph().parse(ROOT/f'ontology/releases/{OLD}/{m}.ttl');new=canonical(Graph().parse(D/f'{m}.ttl'))
  for id_ in delta['definitions']:
   iri=SR[id_]
   if (iri,RDF.type,OWL.Class) in old:
    new.remove((iri,RDFS.comment,None))
    for o in old.objects(iri,RDFS.comment):new.add((iri,RDFS.comment,o))
  if m=='core':new.remove((c(30),RDF.type,GUFO.RoleMixin));new.add((c(30),RDF.type,GUFO.Role))
  if m=='assessment-context':new.remove((AC.GroundedRiskResponsibility,None,None))
  test('DELTA-'+m,isomorphic(old,new),'Only declared definitions, owner metatype and opt-in helper differ, modulo version metadata.')
 reg={x['semantic_id']:x for x in csv.DictReader((ROOT/'conceptualization/core/core-concept-registry-v0.1.csv').open())}
 for id_,definition in delta['definitions'].items():test('DEF-'+id_,str(g.value(SR[id_],RDFS.comment))==definition==reg[id_]['definition'],'Exact registry/OWL definition match.')
 test('OWNER-METATYPE',(c(30),RDF.type,GUFO.RoleMixin) in g and (c(30),RDF.type,GUFO.Role) not in g,'Heterogeneous owner role classification has no fabricated common kind.')
 cats=list(csv.DictReader((ROOT/'foundational/revision-2026-10-05/concept-category-audit.csv').open()))
 test('CONCEPT-COVERAGE',len(cats)==47 and {x['semantic_id'] for x in cats}==set(reg),'All conceptual rows, including markers/deferred rows.')
 test('CONCEPT-COUNTS',[sum(x['formal_status']==s for x in cats) for s in ['LOCAL_CLASS','EXTERNAL_OR_PATTERN_MARKER','NOT_LOCALLY_DECLARED']]==[35,4,8],'35 local classes; 4 markers; 8 undeclared, excluding operational helpers.')
 rel=list(csv.DictReader((ROOT/'foundational/revision-2026-10-05/relation-formal-audit.csv').open()))
 registered=list(csv.DictReader((ROOT/'conceptualization/core/relation-registry-v0.1.csv').open()))
 test('RELATION-COVERAGE',len(rel)==38 and {x['relation_id'] for x in rel}=={x['rel_id'] for x in registered},'38 decisions; 37 OWL properties and 1 architecture relation, not missing SR-REL-010/011 inventions.')
 test('DIAGRAM-BOUNDARIES',any(x['diagram_gate']=='BLOCKED_TYPE_INSTANCE_LEVEL' for x in cats) and all(x['ontouml_stereotype_if_supported'] not in ['information object','derived pattern','situationType','quality/value'] for x in cats),'Do not claim placeholder words are OntoUML stereotypes or suppress type-level ambiguity.')
 valid=data();ok,report,msg=check_shape(valid);test('GROUND-POSITIVE',ok,msg[-250:])
 cases=[]
 for id_,description,marker in [('G01','missing counterpart','MinCountConstraintComponent'),('G02','missing distinctness evidence','GROUND_DISTINCT'),('G03','sameAs alias','GROUND_DISTINCT'),('G04','event participant','ClassConstraintComponent'),('G05','risk as mediated target','GROUND_ABOUTNESS'),('G06','missing assignee','MinCountConstraintComponent'),('G07','literal participant','NodeKindConstraintComponent')]:
  h=clone(valid)
  if id_=='G01':h.remove((EX.responsibility,GUFO.mediates,EX.organization))
  if id_=='G02':h.remove((EX.person,OWL.differentFrom,EX.organization))
  if id_=='G03':h.add((EX.person,OWL.sameAs,EX.organization))
  if id_=='G04':h.remove((EX.organization,RDF.type,GUFO.Endurant));h.add((EX.organization,RDF.type,GUFO.Event))
  if id_=='G05':h.add((EX.responsibility,GUFO.mediates,EX.risk));h.add((EX.risk,RDF.type,GUFO.Endurant))
  if id_=='G06':h.remove((EX.responsibility,r(28),None))
  if id_=='G07':h.add((EX.responsibility,GUFO.mediates,Literal('unnamed person')))
  ok,report,msg=check_shape(h);test(id_,not ok and marker in msg,description+' rejected by '+marker)
 # Generic legacy responsibility is not silently claimed complete or rejected as a migration side effect.
 h=clone(valid);h.remove((EX.responsibility,RDF.type,AC.GroundedRiskResponsibility));h.remove((EX.responsibility,GUFO.mediates,EX.organization))
 test('OPT-IN-BOUNDARY',check_shape(h)[0],'Old unqualified records are outside the stricter evidence profile, not declared fully grounded.')
 t=temporal_fixture();test('TEMPORAL-SHAPE-UNCHANGED',temporal_validate(t)[0],'Existing qualified numeric data profile still conforms.')
 # Adding counterpart metadata must not change assignee-derived owner answers.
 enriched=clone(t)
 for a in list(t.subjects(r(28),None)):
  enriched.add((a,GUFO.mediates,EX.organization))
 for instant in ['2026-09-30T00:00:00Z','2026-10-05T08:00:00Z','2026-10-06T00:00:00Z']:
  test('OWNER-PRESERVATION-'+instant,owner_rows(t,instant)==owner_rows(enriched,instant),'Counterpart is not automatically an owner; exact owner pairs preserved.')
 result=dict(candidate_version=V,total=len(out),passed=sum(x['passed'] for x in out),negative_cases=7,concept_rows=47,relation_rows=38,tests=out,limits=['No complete OntoUML model/checker','No expert validation','Named-witness profile not yet projected into SQL','Synthetic fixtures only'])
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();result=run()
 if a.write:E.mkdir(parents=True,exist_ok=True);(E/'results.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='tests'},indent=2))
