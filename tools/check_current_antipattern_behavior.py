#!/usr/bin/env python3
"""Selected behavioral countermodels and reference joins; never full antipattern acceptance."""
import argparse,copy,csv,hashlib,json,platform,subprocess
from pathlib import Path
import rdflib,pyshacl,yaml
from rdflib import Graph,Namespace,URIRef,BNode,Literal,RDF,RDFS,OWL,XSD
from pyshacl import validate
from check_rc4_extension import closure,clone,c,r,AC,GUFO,SR
ROOT=Path(__file__).resolve().parents[1];DIR=ROOT/'evaluation/antipatterns/0.2.0-rc.4/behavioral'
TEST=Namespace('urn:semrisk:test:fap:');OLD=Namespace('urn:semrisk:run4:');SH=Namespace('http://www.w3.org/ns/shacl#');SKOS=Namespace('http://www.w3.org/2004/02/skos/core#')
PROTOCOL_SHA='4b053d8107d62a1952a5aaddff5603a001171151032b58a5a4cd25b016882fa5'
def require(ok,message):
 if not ok:raise ValueError(message)
def csvrows(p):return list(csv.DictReader((ROOT/p).open()))
def source_check(protocol):
 require(hashlib.sha256((DIR/'protocol.json').read_bytes()).hexdigest()==PROTOCOL_SHA,'PROTOCOL_DRIFT')
 for p,h in protocol['source_sha256'].items():require(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'SOURCE_DRIFT: '+p)
EXPECTED_MAPPING_DECISIONS={'BR-C001': ('BRIDGE_ONLY_NOT_EQUIVALENCE', 'ACTIVE'), 'BR-C002': ('RISK_CONTEXT_TARGET', 'ACTIVE'), 'BR-C003': ('EXTERNAL_OWNER_CLOSE_MAPPING', 'ACTIVE'), 'BR-C004': ('EXTERNAL_OWNER_PROFILE_NARROWING', 'ACTIVE'), 'BR-C005': ('RISK_CONTEXT_TARGET', 'ACTIVE'), 'BR-C006': ('RISK_CONTEXT_TARGET', 'ACTIVE'), 'BR-C007': ('RISK_CONTEXT_TARGET', 'ACTIVE'), 'BR-C008': ('POTENTIAL_ROLE_BEARER', 'ACTIVE'), 'BR-C009': ('POTENTIAL_ROLE_BEARER', 'ACTIVE'), 'BR-C010': ('RELATED_ACTIVITY_EXTERNAL_OWNER', 'ACTIVE'), 'BR-C011': ('PLATFORM_PRODUCES_OR_HOSTS_EVIDENCE', 'ACTIVE'), 'BR-C012': ('RELATED_NOT_EQUIVALENT', 'ACTIVE'), 'BR-C013': ('NO_DIRECT_MAPPING', 'REJECT_EQUIVALENCE'), 'BR-C014': ('UNMAPPED_EXTERNAL_TERMINOLOGY_GAP', 'UNMAPPED'), 'BR-C015': ('UNMAPPED_EXTERNAL_TERMINOLOGY_GAP', 'UNMAPPED'), 'BR-C016': ('UNMAPPED_EXTERNAL_ENTERPRISE_OWNER', 'UNMAPPED')}
def bridge_check(audit,bridge,gaps,catalog,manifest,g):
 require(catalog['model_release']==manifest['release']=='v1.0.0','EXTERNAL_RELEASE')
 concepts=catalog['concepts'];byid={x['id']:x for x in concepts};require(len(concepts)==len(byid)==manifest['semantic_inventory']['canonical_concepts']==39,'EXTERNAL_CATALOG_IDS')
 expected={'CMPE-C0001','CMPE-C0005','CMPE-C0015','CMPE-C0011','CMPE-C0032','CMPE-C0003','CMPE-C0008','CMPE-C0028','CMPE-C0038','CMPE-C0010','CMPE-C0036','CMPE-C0025'}
 require(len(audit)==12 and {x['audit_id'] for x in audit}=={f'CAT-{i:03}' for i in range(1,13)} and {x['cmpe_id'] for x in audit}==expected,'CATEGORY_AUDIT_IDS')
 for row in audit:
  actual=byid.get(row['cmpe_id']);require(actual is not None and row['frozen_stereotype']==actual['stereotype'] and row['label']==actual['label'],'CATEGORY_PRESERVATION')
 flag=byid['CMPE-C0025'];row=next(x for x in audit if x['cmpe_id']=='CMPE-C0025')
 require(flag.get('review_flag')=='stereotype-conflict' and flag.get('conflicting_source_stereotype')=='mode' and row['status']=='PASS_WITH_FLAG' and row['preservation_result']=='PRESERVED_WITH_SOURCE_FLAG','SOURCE_CONFLICT_FLAG')
 require(len(bridge)==16 and {x['bridge_id'] for x in bridge}=={f'BR-C{i:03}' for i in range(1,17)},'BRIDGE_IDS')
 for row in bridge:
  require((row['mapping_semantics'],row['status'])==EXPECTED_MAPPING_DECISIONS[row['bridge_id']],'BRIDGE_MAPPING_DECISION')
  if row['cmpe_id']:
   actual=byid.get(row['cmpe_id']);require(actual is not None and row['cmpe_term']==actual['label'] and row['cmpe_stereotype']==actual['stereotype'],'BRIDGE_CATEGORY')
 bybridge={x['bridge_id']:x for x in bridge}
 for id in ['BR-C014','BR-C015','BR-C016']:
  row=bybridge[id];require(row['status']=='UNMAPPED' and not row['cmpe_id'] and row['mapping_semantics'].startswith('UNMAPPED_EXTERNAL_'),'FABRICATED_UNMAPPED_BRIDGE')
 require(bybridge['BR-C013']['status']=='REJECT_EQUIVALENCE' and bybridge['BR-C013']['mapping_semantics']=='NO_DIRECT_MAPPING','HAZARD_REQUIREMENT_NON_EQUIVALENCE')
 gaps_byid={x['finding_id']:x for x in gaps};require(gaps_byid['PH-BG-001']['status']==gaps_byid['PH-BG-006']['status']=='OPEN_GOVERNED' and gaps_byid['PH-BG-002']['status']=='OPEN_BOUNDED','GAPS_ERASED')
 require(not any(p==OWL.imports and 'cm-pharme' in str(o).lower() for s,p,o in g),'EXTERNAL_IMPORT')
 refs={x for triple in g for x in triple if isinstance(x,URIRef) and str(x).startswith('urn:cm-pharme:')}
 expected_refs={URIRef('urn:cm-pharme:v1.0.0:'+i) for i in ['CMPE-C0001','CMPE-C0005','CMPE-C0011','CMPE-C0015','CMPE-C0032']}
 require(refs==expected_refs,'REFERENCE_NAMESPACE')
 require(all((s,RDF.type,SKOS.Concept) in g and (s,RDF.type,OWL.Class) not in g for s in refs),'REFERENCE_NOT_CLASS')
 for s,p,o in g:
  require(not (p in [OWL.equivalentClass,OWL.equivalentProperty,OWL.sameAs] and (s in refs or o in refs)),'EXTERNAL_EQUIVALENCE')
  require(not (p==OWL.imports and 'cm-pharme' in str(o).lower()),'EXTERNAL_IMPORT')
 return True

def run(robot,external,out):
 protocol=json.loads((DIR/'protocol.json').read_text());source_check(protocol)
 require(hashlib.sha256(robot.read_bytes()).hexdigest()==protocol['formal_protocol']['robot_sha256'],'REASONER_BYTES')
 require(not external.resolve().is_relative_to(out.resolve()),'EXTERNAL_INPUTS_MUST_NOT_BE_OUTPUT_ARTIFACTS')
 out.mkdir(parents=True,exist_ok=True);tests=[];adverse=[];owner_trace=[]
 runtime={'python':platform.python_version(),'rdflib':rdflib.__version__,'pyshacl':pyshacl.__version__,'pyyaml':yaml.__version__};(out/'runtime.json').write_text(json.dumps(runtime,indent=2)+'\n')
 require(runtime['rdflib']=='7.6.0' and runtime['pyshacl']=='0.40.1' and runtime['pyyaml']=='6.0.2','TOOLCHAIN')
 def test(id,ok,detail):require(ok,id+': '+detail);tests.append({'id':id,'passed':True,'detail':detail})
 def rejected(id,fn,marker):
  try:fn()
  except ValueError as exc:test(id,marker in str(exc),str(exc));return
  raise ValueError('NEGATIVE_ACCEPTED: '+id)
 ontology,seen=closure();local=Graph()
 for m in ['core','enterprise','method','governance','pharma','mappings','assessment-context']:local.parse(ROOT/'ontology/releases/0.2.0-rc.4'/(m+'.ttl'))
 shapes=Graph()
 for p in ['assessment-context-v0.2.0-rc.1','semantic-identity-v0.2.0-rc.3','exposure-scale-v0.2.0-rc.4']:shapes.parse(ROOT/'shapes'/(p+'.ttl'))
 def shape(g):return validate(g,shacl_graph=shapes,inference='none',meta_shacl=True)
 # Ownership-only current-query experiment, avoiding historical scale migration debt.
 full=Graph().parse(ROOT/'testdata/temporal/qualified-context-v0.2.0-rc.1.ttl');owners=Graph();assignments=set(full.subjects(RDF.type,c(31)))
 require(len(assignments)==6,'ASSIGNMENT_FIXTURE_COUNT')
 for s in assignments:
  for t in full.triples((s,None,None)):owners.add(t)
 owners.add((OLD.risk,RDF.type,c(1)));query=(ROOT/'rules/enterprise/risk-owners-at-v0.2.0-rc.1.rq').read_text()
 def owner_answers(g,instant=None,q=query):return sorted(tuple(map(str,row)) for row in g.query(q,initBindings={'asOf':Literal(instant,datatype=XSD.dateTime)} if instant else {}))
 test('F006_PROFILE_POSITIVE',shape(owners)[0],'Ownership-only data conforms to current composed explicit-data shapes.')
 for i,(instant,actors) in enumerate(protocol['FAP-006']['expected_actor_pairs'].items(),1):
  expected=sorted((protocol['FAP-006']['risk_iri'],protocol['FAP-006']['actor_namespace']+a) for a in actors)
  actual=owner_answers(owners,instant);test(f'F006_EXACT_PAIRS_{i}',actual==expected,'Exact actor pairs at '+instant);owner_trace.append({'instant':instant,'expected':expected,'actual':actual})
 boundary='2026-10-05T08:00:00Z';expected=owner_answers(owners,boundary)
 test('F006_UNBOUND',owner_answers(owners)==[],'No ambient time or unbound ownership assertion.')
 h=clone(owners)
 for _,p,o in owners.triples((OLD['owner-active'],None,None)):h.add((TEST.duplicateAssignment,p,o))
 test('F006_DUPLICATE_PATH',owner_answers(h,boundary)==expected,'DISTINCT answers survive duplicate assignment path.')
 h=clone(owners);h.add((OLD['owner-active'],GUFO.mediates,TEST.counterpart))
 test('F006_COUNTERPART_NOT_OWNER',owner_answers(h,boundary)==expected,'Additional mediation counterpart is not projected as assignee.')
 for name,p,o in [('TYPE',RDF.type,c(31)),('RISK',r(27),None),('ACTOR',r(28),None),('START',AC.validFrom,None)]:
  h=clone(owners);h.remove((OLD['owner-active'],p,o));test('N006_MISSING_'+name,owner_answers(h,boundary)==[(str(OLD.risk),str(OLD['actor-b']))],'Only the selected active assignment pair disappears.')
 h=clone(owners);h.add((OLD.risk,r(26),TEST.primitiveOwner));test('N006_PRIMITIVE_OWNER',owner_answers(h,boundary)==expected,'Primitive hasRiskOwner triple cannot substitute for qualifying assignment.')
 mutant=query.replace('SELECT DISTINCT ?risk ?actor','SELECT DISTINCT ?risk (sr:SR-CPT-030 AS ?ownerClass)');wrong=owner_answers(owners,boundary,mutant)
 test('N006_WRONG_QUERY_TARGET',bool(wrong) and all(row[1]==str(c(30)) for row in wrong) and wrong!=expected,'Executed SELECT mutant returns role-class IRI and fails exact expected answers.')
 h=clone(owners);h.set((OLD['owner-active'],r(28),c(30)));observed=owner_answers(h,boundary);conforms,adverse_report,_=shape(h)
 h.serialize(out/'class-assignee-data.ttl',format='turtle');adverse_report.serialize(out/'class-assignee-shape-report.ttl',format='turtle');owners.serialize(out/'ownership-fixture.ttl',format='turtle');(out/'ownership-observations.json').write_text(json.dumps(owner_trace,indent=2)+'\n')
 require((c(30),RDF.type,OWL.Class) in local and (c(30),RDF.type,GUFO.RoleMixin) in local,'KNOWN_OWNER_CLASS')
 require(conforms and (str(OLD.risk),str(c(30))) in observed,'ADVERSE_ASSIGNEE_OBSERVATION_CHANGED')
 adverse.append({'finding':'FAP-006','status':'OBSERVED_LIMITATION','observation':'IRI-only explicit-data assignee shape accepts the known Risk Owner class IRI, and the query returns it. Universal class-as-assignee rejection is not established.','shape_conforms':conforms,'actual_pairs':observed})
 # Focus/path/component-specific profile boundary and actual countermodels.
 worlds={};expected_consistency={}
 zero=Graph();zero.add((TEST.zeroExposure,RDF.type,c(10)))
 multi=Graph();multi.add((TEST.multiExposure,RDF.type,c(10)))
 for s in [TEST.subjectA,TEST.subjectB]:multi.add((s,RDF.type,c(2)));multi.add((TEST.multiExposure,r(39),s))
 multi.add((TEST.source,RDF.type,c(3)));multi.add((TEST.multiExposure,r(40),TEST.source));multi.add((TEST.subjectA,OWL.differentFrom,TEST.subjectB))
 for key,data in [('zero_endpoint',zero),('two_subjects',multi)]:
  ok,report,_=shape(data);oracle=protocol['FAP-012']['shape_oracle'][key]
  data.serialize(out/(key+'-shape-data.ttl'),format='turtle');report.serialize(out/(key+'-shape-report.ttl'),format='turtle')
  result_nodes=list(report.subjects(RDF.type,SH.ValidationResult))
  actual={(str(report.value(res,SH.focusNode)),str(report.value(res,SH.resultPath)),str(report.value(res,SH.sourceConstraintComponent))) for res in result_nodes}
  expected={(oracle['focus'],p,oracle['component']) for p in oracle['paths']}
  test('F012_SHACL_'+key,not ok and actual==expected and len(actual)==len(result_nodes)==oracle['expected_violation_count'],'Only exact expected focus/path/component violations occur.')
 h=clone(ontology);h+=zero
 for prop in [r(39),r(40)]:
  z=BNode();h.add((z,RDF.type,OWL.Restriction));h.add((z,OWL.onProperty,prop));h.add((z,OWL.maxCardinality,Literal(0,datatype=XSD.nonNegativeInteger)));h.add((TEST.zeroExposure,RDF.type,z))
 worlds['zero-endpoints']=h;expected_consistency['zero-endpoints']=True
 h=clone(ontology);h+=multi;worlds['two-subjects']=h;expected_consistency['two-subjects']=True
 h=clone(worlds['zero-endpoints']);z=BNode();h.add((z,RDF.type,OWL.Restriction));h.add((z,OWL.onProperty,r(39)));h.add((z,OWL.minCardinality,Literal(1,datatype=XSD.nonNegativeInteger)));h.add((c(10),RDFS.subClassOf,z));worlds['injected-global-min']=h;expected_consistency['injected-global-min']=False
 h=clone(worlds['two-subjects']);h.add((r(39),RDF.type,OWL.FunctionalProperty));worlds['injected-functionality']=h;expected_consistency['injected-functionality']=False
 test('F012_LOCAL_POLICY',all((r(i),RDF.type,OWL.FunctionalProperty) not in local for i in [39,40]),'Selected local endpoint properties are not globally functional; imported restrictions are not prohibited.')
 # Causal non-entailment requires a consistent world that explicitly denies causes.
 for name,prop,typ in [('association',r(9),c(1)),('state-sequence',r(32),c(35))]:
  h=clone(ontology);a=TEST[name+'A'];b=TEST[name+'B'];h.add((a,RDF.type,typ));h.add((b,RDF.type,typ));h.add((a,OWL.differentFrom,b));h.add((a,prop,b))
  if name=='state-sequence':h.add((TEST.risk,RDF.type,c(1)));h.add((TEST.risk,r(31),a));h.add((TEST.risk,r(31),b))
  n=BNode();h.add((n,RDF.type,OWL.NegativePropertyAssertion));h.add((n,OWL.sourceIndividual,a));h.add((n,OWL.assertionProperty,r(8)));h.add((n,OWL.targetIndividual,b))
  worlds[name]=h;expected_consistency[name]=True
  hh=clone(h);hh.add((prop,RDFS.subPropertyOf,r(8)));worlds[name+'-causal-shortcut']=hh;expected_consistency[name+'-causal-shortcut']=False
  if name=='association':hh=clone(h);hh.add((a,r(8),b));worlds['direct-cause-contradiction']=hh;expected_consistency['direct-cause-contradiction']=False
 require(len(worlds)==9 and sum(expected_consistency.values())==4,'WORLD_PROTOCOL_COUNT')
 for name,g in worlds.items():
  print('Reasoning world: '+name,flush=True);inp=out/(name+'.owl');g.serialize(inp,format='xml')
  p=subprocess.run(['java','-jar',str(robot),'validate-profile','--profile','DL','--input',str(inp),'--output',str(out/(name+'-dl.txt'))],text=True,capture_output=True,timeout=180);(out/(name+'-profile.log')).write_text(p.stdout+p.stderr);test('DL_'+name,p.returncode==0,'Actual OWL 2 DL profile validation precedes reasoning.')
  p=subprocess.run(['java','-jar',str(robot),'reason','--reasoner','HermiT','--input',str(inp),'--output',str(out/(name+'-reasoned.owl'))],text=True,capture_output=True,timeout=180);log=p.stdout+p.stderr;(out/(name+'.log')).write_text(log)
  if expected_consistency[name]:test('CONSISTENT_'+name,p.returncode==0,'Actual HermiT-consistent selected countermodel.')
  else:test('N_INCONSISTENT_'+name,p.returncode!=0 and ('inconsistent' in log.lower() or 'inconsistency' in log.lower()),'Actual HermiT inconsistency; parser/profile failure is not accepted.')
 # Pinned external inputs stay outside the repository/output artifact.
 parsed={}
 for name,meta in protocol['FAP-014']['source_files'].items():
  b=(external/name).read_bytes();require(hashlib.sha256(b).hexdigest()==meta['sha256'],'EXTERNAL_SHA256');require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==meta['git_blob'],'EXTERNAL_GIT_BLOB');parsed[name]=yaml.safe_load(b)
 audit=csvrows('conceptualization/pharma/cm-pharme-category-preservation-audit.csv');bridge=csvrows('conceptualization/pharma/cm-pharme-concept-bridge-v0.1.csv');gaps=csvrows('conceptualization/pharma/unresolved-pharma-bridge-register.csv');catalog=parsed['concepts.yaml'];manifest=parsed['manifest.yaml']
 bridge_check(audit,bridge,gaps,catalog,manifest,local);test('F014_PINNED_CATEGORY_JOIN',True,'12 audit rows, 16 bridge decisions and 5 marker references match the pinned 39-concept release; source conflict and unmapped gaps retained.')
 def mutate_mode(a,b,g,c,m,o):next(x for x in a if x['frozen_stereotype']=='mode')['frozen_stereotype']='kind'
 def wrong_namespace(a,b,g,c,m,o):
  old=URIRef('urn:cm-pharme:v1.0.0:CMPE-C0001');new=URIRef('urn:cm-pharme:v9:CMPE-C0001')
  for s,p,obj in list(o.triples((old,None,None))):o.remove((s,p,obj));o.add((new,p,obj))
 cases=[('N014_OBJECT_ONLY_WRONG_NAMESPACE',lambda a,b,g,c,m,o:o.add((SR['SR-CPT-002'],SKOS.relatedMatch,URIRef('urn:cm-pharme:v9:CMPE-C0001'))),'REFERENCE_NAMESPACE'),('N014_MAPPING_TYPE',lambda a,b,g,c,m,o:b[1].update(mapping_semantics='EQUIVALENCE'),'BRIDGE_MAPPING_DECISION'),('N014_MODE_AS_KIND',mutate_mode,'CATEGORY_PRESERVATION'),('N014_UNKNOWN_ID',lambda a,b,g,c,m,o:a[0].update(cmpe_id='CMPE-C9999'),'CATEGORY_AUDIT_IDS'),('N014_WRONG_NAMESPACE',wrong_namespace,'REFERENCE_NAMESPACE'),('N014_DROP_SOURCE_FLAG',lambda a,b,g,c,m,o:next(x for x in a if x['cmpe_id']=='CMPE-C0025').update(status='PASS'),'SOURCE_CONFLICT_FLAG'),('N014_LOCAL_EQUIVALENCE',lambda a,b,g,c,m,o:o.add((SR['SR-CPT-002'],OWL.equivalentClass,URIRef('urn:cm-pharme:v1.0.0:CMPE-C0001'))),'EXTERNAL_EQUIVALENCE'),('N014_EXTERNAL_IMPORT',lambda a,b,g,c,m,o:o.add((URIRef('urn:semrisk:ontology:mappings'),OWL.imports,URIRef('urn:cm-pharme:v1.0.0'))),'EXTERNAL_IMPORT'),('N014_MARKER_AS_CLASS',lambda a,b,g,c,m,o:o.add((URIRef('urn:cm-pharme:v1.0.0:CMPE-C0001'),RDF.type,OWL.Class)),'REFERENCE_NOT_CLASS')]
 for bid in ['BR-C014','BR-C015','BR-C016']:
  def fabricated(a,b,g,c,m,o,bid=bid):next(x for x in b if x['bridge_id']==bid).update(cmpe_id='CMPE-C0001',cmpe_term='Pharmaceutical Enterprise',cmpe_stereotype='kind')
  cases.append(('N014_FABRICATED_'+bid,fabricated,'FABRICATED_UNMAPPED_BRIDGE'))
 cases += [('N014_MISSING_AUDIT',lambda a,b,g,c,m,o:a.pop(),'CATEGORY_AUDIT_IDS'),('N014_DUPLICATE_BRIDGE',lambda a,b,g,c,m,o:b.append(copy.deepcopy(b[0])),'BRIDGE_IDS')]
 for name,mut,marker in cases:
  args=[copy.deepcopy(audit),copy.deepcopy(bridge),copy.deepcopy(gaps),copy.deepcopy(catalog),copy.deepcopy(manifest),clone(local)];mut(*args);rejected(name,lambda:bridge_check(*args),marker)
 prior=json.loads((ROOT/'evaluation/antipatterns/0.2.0-rc.4/results.json').read_text())
 require(len(prior['findings'])==15 and {x['finding_id'] for x in prior['findings']}=={f'FAP-{i:03}' for i in range(1,16)} and all(x['full_antipattern_status']=='NOT_ESTABLISHED' for x in prior['findings']),'FULL_VERDICTS_MUST_REMAIN_UNESTABLISHED')
 # Source-level absence/subset checks remain separate and are not promoted here.
 source_check(protocol)
 result={'result':'PASS_SELECTED_BEHAVIOR_WITH_RETAINED_LIMITS','protocol_sha256':PROTOCOL_SHA,'source_files':20,'external_source_commit':protocol['FAP-014']['catalog_commit'],'external_source_sha256':{n:m['sha256'] for n,m in protocol['FAP-014']['source_files'].items()},'runtime_versions':{**runtime,'python':'.'.join(runtime['python'].split('.')[:2])},'tests':tests,'total':len(tests),'passed':len(tests),'negative_controls':sum(t['id'].startswith('N') for t in tests),'observed_limitations':adverse,'reasoner_worlds':{'owl2dl':9,'consistent':4,'inconsistent':5},'findings':{fid:{'selected_evidence':'EXECUTED_BOUNDED','full_antipattern_status':'NOT_ESTABLISHED'} for fid in protocol['finding_ids']},'all_fifteen_full_verdicts':'NOT_ESTABLISHED','limits':protocol['acceptance_limits']}
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--robot',type=Path,required=True);p.add_argument('--external-inputs',type=Path,required=True);p.add_argument('--build-dir',type=Path,default=ROOT/'build/current-antipattern-behavior');p.add_argument('--write',action='store_true');a=p.parse_args();result=run(a.robot,a.external_inputs,a.build_dir);text=json.dumps(result,indent=2)+'\n'
 if a.write:(DIR/'results.json').write_text(text)
 else:require((DIR/'results.json').read_text()==text,'RESULT_DRIFT')
 print(text,end='')
