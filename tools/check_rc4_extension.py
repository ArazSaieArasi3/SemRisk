#!/usr/bin/env python3
"""Finite synthetic rc.4 extension compatibility; no universal conservation claim."""
import argparse,csv,hashlib,json,subprocess,platform
import rdflib,pyshacl
from pathlib import Path
from xml.etree import ElementTree as ET
from rdflib import Graph,Namespace,URIRef,Literal,RDF,RDFS,OWL,XSD
from pyshacl import validate
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/'evaluation/extension/0.2.0-rc.4'
SR=Namespace('urn:semrisk:entity:');AC=Namespace('urn:semrisk:profile:assessment-context:');IST=Namespace('urn:semrisk:profile:information-state:');GUFO=Namespace('http://purl.org/nemo/gufo#');EX=Namespace('urn:semrisk:run8:');TEST=Namespace('urn:semrisk:test:extension:pharma:')
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def c(i):return SR[f'SR-CPT-{i:03}']
def r(i):return SR[f'SR-REL-{i:03}']
def clone(g):h=Graph();h+=g;return h
def require(ok,message):
 if not ok:raise ValueError(message)
def source_check(protocol):
 for name,h in protocol['new_fixture_sha256'].items():require(hashlib.sha256((DIR/name).read_bytes()).hexdigest()==h,'FIXTURE_DRIFT: '+name)
 for p,h in protocol['source_sha256'].items():require(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'SOURCE_DRIFT: '+p)
def inventories(concepts,relations,inventory):
 require(len(concepts)==47 and {x['semantic_id'] for x in concepts}=={f'SR-CPT-{i:03}' for i in range(1,48)},'CONCEPT_INVENTORY')
 require(len(relations)==40 and {x['relation_id'] for x in relations}=={f'SR-REL-{i:03}' for i in range(1,41)},'RELATION_INVENTORY')
 require(len(inventory)==116 and len({x['iri'] for x in inventory})==116,'DECLARATION_INVENTORY')
def extension_check(g):
 expected={(TEST.PharmaceuticalExposure,RDF.type,OWL.Class),(TEST.PharmaceuticalExposure,RDFS.subClassOf,c(10)),(TEST.PharmaceuticalRiskSource,RDF.type,OWL.Class),(TEST.PharmaceuticalRiskSource,RDFS.subClassOf,c(3))}
 require(set(g)==expected,'EXTENSION_AXIOM_ALLOWLIST')
def closure():
 d=ROOT/'ontology/releases/0.2.0-rc.4';ns={'c':'urn:oasis:names:tc:entity:xmlns:xml:catalog'}
 bindings={x.attrib['name']:(d/x.attrib['uri']).resolve() for x in ET.parse(d/'catalog.xml').findall('c:uri',ns)}
 todo=[d/(m+'.ttl') for m in MODULES];seen=set();g=Graph()
 while todo:
  p=todo.pop().resolve()
  if p in seen:continue
  seen.add(p);h=Graph().parse(p)
  for iri in h.objects(None,OWL.imports):
   require(str(iri) in bindings,'UNBOUND_IMPORT: '+str(iri));todo.append(bindings[str(iri)])
  g+=h
 require(len(seen)==8,'IMPORT_CLOSURE_COUNT');g.remove((None,OWL.imports,None));return g,seen

def run(robot,out):
 require(hashlib.sha256((DIR/'protocol.json').read_bytes()).hexdigest()=='c56e87d36673b80581f94ea11c0aafe170fd37d0ad7a5a4540cf7433ecab885d','PREDECLARED_PROTOCOL_DRIFT')
 protocol=json.loads((DIR/'protocol.json').read_text());source_check(protocol)
 require(hashlib.sha256(robot.read_bytes()).hexdigest()==protocol['formal_validation']['robot_sha256'],'REASONER_BYTES')
 out.mkdir(parents=True,exist_ok=True);tests=[]
 runtime={'python':platform.python_version(),'rdflib':rdflib.__version__,'pyshacl':pyshacl.__version__}
 (out/'runtime.json').write_text(json.dumps(runtime,indent=2)+'\n')
 require(runtime['rdflib']=='7.6.0' and runtime['pyshacl']=='0.40.1','PYTHON_TOOLCHAIN')
 def test(id,ok,detail):
  require(ok,id+': '+detail);tests.append({'id':id,'passed':True,'detail':detail})
 def rejected(id,fn,marker):
  try:fn()
  except ValueError as exc:test(id,marker in str(exc),str(exc));return
  raise ValueError('NEGATIVE_ACCEPTED: '+id)
 extension=Graph().parse(DIR/'pharma-extension.ttl');extension_check(extension)
 ontology,seen=closure();base=Graph().parse(ROOT/'testdata/foundational/exposure-scale-v0.2.0-rc.4.ttl');extended=clone(base)
 for s,t in [(EX.exposureA,TEST.PharmaceuticalExposure),(EX.exposureB,TEST.PharmaceuticalExposure),(EX.source,TEST.PharmaceuticalRiskSource)]:extended.add((s,RDF.type,t))
 test('BASELINE_TRIPLES',set(base)<=set(extended) and len(extended)-len(base)==3,'All baseline triples preserved; exactly three test-domain type assertions added.')
 shapes=Graph()
 for name in protocol['application_validation']['shapes']:shapes.parse(ROOT/'shapes'/(name+'.ttl'))
 for name,data in [('baseline',base),('extended',extended)]:
  ok,_,message=validate(data,shacl_graph=shapes,inference='none',meta_shacl=True);test('SHACL_'+name.upper(),ok,'Current strict composition conforms with inference=none.')
 core_query=(ROOT/'rules/core/exposure-at-v0.2.0-rc.4.rq').read_text();domain_query=(DIR/'pharma-exposure-at.rq').read_text()
 def answers(g,query,instant=None):return sorted(tuple(map(str,row)) for row in g.query(query,initBindings={'asOf':Literal(instant,datatype=XSD.dateTime)} if instant else {}))
 for i,(instant,episode) in enumerate(protocol['instants'].items(),1):
  expected=[(str(EX[episode]),*protocol['expected_tuple_tail'])]
  test(f'CORE_ANSWERS_{i}',answers(base,core_query,instant)==answers(extended,core_query,instant)==expected,'Exact predeclared full tuples preserved at '+instant)
  test(f'DOMAIN_ANSWERS_{i}',answers(extended,domain_query,instant)==expected,'Domain question uses both test-only specialization types at '+instant)
 test('UNBOUND_TIME',all(answers(g,q)==[] for g,q in [(base,core_query),(extended,core_query),(extended,domain_query)]),'No implicit wall-clock time.')
 differences=[(EX.exposureB,OWL.differentFrom,EX.exposureA),(EX.scaleA,OWL.differentFrom,EX.scaleB),(EX.scaleA,OWL.differentFrom,EX.series),(EX.scaleB,OWL.differentFrom,EX.series)]
 test('IDENTITY_ASSERTIONS',all(t in base and t in extended for t in differences),'Episode and equal-content issued-scale distinctions preserved.')
 h=clone(extended);h.set((EX.exposureA,AC.validTo,Literal('2026-10-04T00:00:00Z',datatype=XSD.dateTime)))
 ok,_,_=validate(h,shacl_graph=shapes,inference='none',meta_shacl=True)
 test('N_CHANGED_ANSWER',ok and answers(h,core_query,'2026-10-04T23:59:59Z')!=answers(base,core_query,'2026-10-04T23:59:59Z'),'Shape-valid earlier episode end changes the exact finite answer set.')
 h=clone(extended);h.remove((EX.source,RDF.type,TEST.PharmaceuticalRiskSource))
 test('N_MISSING_DOMAIN_TYPE',answers(h,domain_query,'2026-10-05T00:00:00Z')==[],'Removing the domain source type loses the domain-specific answer.')
 mutations={
  'N_CORE_REDEFINITION':(c(10),RDFS.subClassOf,TEST.PharmaceuticalExposure),
  'N_REVERSE_SUBCLASS':(c(3),RDFS.subClassOf,TEST.PharmaceuticalRiskSource),
  'N_EQUIVALENCE_FORWARD':(TEST.PharmaceuticalExposure,OWL.equivalentClass,c(10)),
  'N_EQUIVALENCE_REVERSE':(c(10),OWL.equivalentClass,TEST.PharmaceuticalExposure),
  'N_NEW_KEY':(TEST.PharmaceuticalExposure,OWL.hasKey,RDF.nil),
  'N_FUNCTIONALITY':(r(39),RDF.type,OWL.FunctionalProperty),
  'N_PROPERTY_CHAIN':(r(39),OWL.propertyChainAxiom,RDF.nil),
 }
 for name,triple in mutations.items():
  h=clone(extension);h.add(triple);rejected(name,lambda:extension_check(h),'EXTENSION_AXIOM_ALLOWLIST')
 for p in [(TEST.PharmaceuticalExposure,RDFS.subClassOf,c(10)),(TEST.PharmaceuticalRiskSource,RDFS.subClassOf,c(3))]:
  h=clone(extension);h.remove(p);rejected('N_ALLOWLIST_MISSING_'+str(p[0]).rsplit(':',1)[-1],lambda:extension_check(h),'EXTENSION_AXIOM_ALLOWLIST')
 def rows(p):return list(csv.DictReader((ROOT/p).open()))
 concepts=rows('foundational/exposure-scale-v0.2.0-rc.4/concept-category-audit.csv');relations=rows('foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv');inventory=rows('docs/formal/0.2.0-rc.4/entity-inventory.csv')
 inventories(concepts,relations,inventory);test('CANONICAL_INVENTORIES',True,'47/40/116 unchanged; two test-only classes separate.')
 rejected('N_INVENTORY_DRIFT',lambda:inventories(concepts[:-1],relations,inventory),'CONCEPT_INVENTORY')
 bad=json.loads(json.dumps(protocol));bad['source_sha256'][next(iter(bad['source_sha256']))]='0'*64
 rejected('N_SOURCE_DRIFT',lambda:source_check(bad),'SOURCE_DRIFT')
 worlds={'baseline':clone(ontology),'extended':clone(ontology)};worlds['baseline']+=base;worlds['extended']+=extended;worlds['extended']+=extension
 witness=clone(ontology);witness+=extension;witness.add((TEST.exposureWitness,RDF.type,TEST.PharmaceuticalExposure));witness.add((TEST.sourceWitness,RDF.type,TEST.PharmaceuticalRiskSource));worlds['inheritance']=witness
 for name,triple in [('missing-exposure',(TEST.PharmaceuticalExposure,RDFS.subClassOf,c(10))),('missing-source',(TEST.PharmaceuticalRiskSource,RDFS.subClassOf,c(3)))]:
  h=clone(witness);h.remove(triple);worlds[name]=h
 h=clone(worlds['extended']);h.add((TEST.PharmaceuticalExposure,RDFS.subClassOf,GUFO.QualityValue));worlds['contradictory']=h
 reasoned={}
 for name,g in worlds.items():
  print('Reasoning world: '+name,flush=True)
  inp=out/(name+'.owl');g.serialize(inp,format='xml')
  profile=subprocess.run(['java','-jar',str(robot),'validate-profile','--profile','DL','--input',str(inp),'--output',str(out/(name+'-dl.txt'))],text=True,capture_output=True,timeout=180)
  (out/(name+'-profile.log')).write_text(profile.stdout+profile.stderr);test('DL_'+name,profile.returncode==0,'Actual ROBOT OWL 2 DL profile check.')
  cmd=['java','-jar',str(robot),'reason','--reasoner','HermiT','--axiom-generators','SubClass ClassAssertion','--include-indirect','true','--input',str(inp),'--output',str(out/(name+'-reasoned.owl'))]
  proc=subprocess.run(cmd,text=True,capture_output=True,timeout=180);log=proc.stdout+proc.stderr;(out/(name+'.log')).write_text(log)
  if name=='contradictory':test('N_ACTUAL_INCONSISTENCY',proc.returncode!=0 and ('inconsistent' in log.lower() or 'inconsistency' in log.lower()),'Instantiated Exposure/QualityValue specialization produces genuine reasoner inconsistency.');continue
  test('CONSISTENT_'+name,proc.returncode==0,'Actual HermiT consistency and materialized class assertions.');reasoned[name]=Graph().parse(out/(name+'-reasoned.owl'))
 required=[(EX.scaleA,IST.ArtifactVersion),(EX.scaleA,IST.ManagedInformationArtifact),(EX.scaleA,GUFO.FunctionalComplex),(EX.exposureA,GUFO.Situation)]
 test('CORE_ENTAILMENTS',all((s,RDF.type,t) not in base and (s,RDF.type,t) in reasoned['baseline'] and (s,RDF.type,t) in reasoned['extended'] for s,t in required),'Four selected inherited core types remain actually entailed.')
 required_inheritance=[(TEST.exposureWitness,c(10)),(TEST.exposureWitness,GUFO.Situation),(TEST.sourceWitness,c(3))]
 test('ISOLATED_INHERITANCE',all((s,RDF.type,t) not in witness and (s,RDF.type,t) in reasoned['inheritance'] for s,t in required_inheritance),'Fresh relation-free subtype witnesses inherit required parent types.')
 test('N_MISSING_EXPOSURE_INHERITANCE',(TEST.exposureWitness,RDF.type,c(10)) not in reasoned['missing-exposure'],'Removed subclass loses isolated required Exposure inference.')
 test('N_MISSING_SOURCE_INHERITANCE',(TEST.sourceWitness,RDF.type,c(3)) not in reasoned['missing-source'],'Removed subclass loses isolated required RiskSource inference.')
 individuals={x for t in base for x in (t[0],t[2]) if isinstance(x,URIRef) and str(x).startswith(str(EX))};types={x for x in ontology.subjects(RDF.type,OWL.Class) if isinstance(x,URIRef)}
 def projection(g):return {(str(s),str(t)) for s,t in g.subject_objects(RDF.type) if s in individuals and t in types}
 before=projection(reasoned['baseline']);after=projection(reasoned['extended']);test('FINITE_TYPE_PROJECTION',bool(before) and before==after,'Named baseline-individual/current-class assertion projection unchanged; no universal conservation claim.')
 pairs=json.dumps({'before':sorted(before),'after':sorted(after)},indent=2)+'\n';(out/'finite-projection.json').write_text(pairs)
 source_check(protocol)
 return {'runtime_versions':{'python_major_minor':'.'.join(runtime['python'].split('.')[:2]),'rdflib':runtime['rdflib'],'pyshacl':runtime['pyshacl']},'finite_projection_sha256':hashlib.sha256(pairs.encode()).hexdigest(),'result':'PASS_FINITE_SYNTHETIC_RC4_EXTENSION','requirement':'1.9','protocol_sha256':hashlib.sha256((DIR/'protocol.json').read_bytes()).hexdigest(),'source_files':len(protocol['source_sha256']),'ontology_closure_files':len(seen),'tests':tests,'total':len(tests),'passed':len(tests),'negative_controls':sum(t['id'].startswith('N_') for t in tests),'finite_type_projection_rows':len(before),'canonical_inventory':{'concepts':47,'relations':40,'declarations':116},'test_only_classes':2,'reasoner':'HermiT 1.4.5.456 / ROBOT 1.9.10','shacl_inference':'none','limits':protocol['nonclaims'],'acceptance_ceiling':protocol['acceptance_ceiling']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--robot',type=Path,required=True);p.add_argument('--build-dir',type=Path,default=ROOT/'build/extension-rc4');p.add_argument('--write',action='store_true');args=p.parse_args();result=run(args.robot,args.build_dir);text=json.dumps(result,indent=2)+'\n'
 if args.write:(DIR/'results.json').write_text(text)
 else:require((DIR/'results.json').read_text()==text,'RESULT_DRIFT')
 print(text,end='')
