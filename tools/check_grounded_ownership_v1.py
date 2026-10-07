#!/usr/bin/env python3
"""Predeclared regression evidence for the optional ownership entrypoint."""
import argparse,copy,hashlib,json,subprocess,sys
from pathlib import Path
from unittest.mock import patch
from rdflib import Graph,Namespace,URIRef,Literal,RDF,OWL,XSD
from pyshacl import validate
from query_grounded_owners_v1 import guarded_query,scoped_shapes,source_contract,ROOT,DIR,AC,c,SH
from check_rc4_extension import clone,r,GUFO
EX=Namespace('urn:semrisk:test:grounded-owner:')
def require(ok,message):
 if not ok:raise ValueError(message)
def run(robot,out):
 protocol=source_contract();out.mkdir(parents=True,exist_ok=True);require(not any(out.iterdir()),'BUILD_DIRECTORY_MUST_BE_EMPTY')
 base=Graph().parse(DIR/'positive.ttl');query_text=(ROOT/'rules/enterprise/risk-owners-grounded-v1.rq').read_text();old_query=(ROOT/'rules/enterprise/risk-owners-at-v0.2.0-rc.1.rq').read_text()
 header='# Opt-in projection only. Invoke through query_grounded_owners_v1.py; direct execution is unchecked.\n'
 require(query_text.removeprefix(header).replace(' ?assignment a ac:GroundedRiskResponsibility .\n','')==old_query,'QUERY_ADAPTER_DRIFT')
 tests=[];boundary='2026-10-05T00:00:00Z';original_query=Graph.query
 def test(id,ok,detail):require(ok,id+': '+detail);tests.append({'id':id,'passed':True,'detail':detail})
 def invoke(name,g,instant=boundary):
  called=[]
  def traced(graph,q,*args,**kwargs):
   if isinstance(q,str) and q==query_text:called.append(True)
   return original_query(graph,q,*args,**kwargs)
  work=out/name
  with patch.object(Graph,'query',traced):result=guarded_query(g,instant,robot,work)
  work.mkdir(exist_ok=True);(work/'response.json').write_text(json.dumps(result,indent=2)+'\n')
  if result['status']=='VALIDATED_QUERY_RESULT':require(len(called)==1,name+': QUERY_EXECUTION_COUNT')
  else:require('owners' not in result and not called,name+': FAILURE_MUST_NOT_QUERY_OR_RETURN_OWNERS')
  return result
 def bad(name,g,stage,code=None,component=None):
  result=invoke(name,g);ok=result['status']=='VALIDATION_FAILED' and result['stage']==stage
  if code:ok=ok and result['code']==code
  if component:ok=ok and any(component in x for x in result.get('components',[]))
  test(name,ok,'Explicit '+stage+' failure; no ownership query or owners field.');return result
 test('QUERY_ADAPTER',True,'Only the explicit opt-in filter and warning header are added to the frozen SELECT.')
 for i,(instant,actors) in enumerate(protocol['expected_opted_answers'].items(),1):
  response=invoke('positive-'+str(i),base,instant);expected=sorted((protocol['expected_risk_iri'],protocol['expected_actor_namespace']+a) for a in actors)
  test('POSITIVE_EXACT_TUPLES_'+str(i),response['status']=='VALIDATED_QUERY_RESULT' and response['owners']==expected and response['opted_assignment_count']==2 and response['explicit_legacy_assignment_count']==1,'Exact full risk/actor tuples; co-ownership and half-open boundaries preserved at '+instant)
  test('LEGACY_AND_COUNTERPART_EXCLUDED_'+str(i),all(actor!=str(c(30)) and actor!=str(EX.board) for _,actor in response['owners']),'Neither ungrounded legacy class token nor mediation-only board appears.')
 old=list(base.query(old_query,initBindings={'asOf':Literal(boundary,datatype=XSD.dateTime)}));test('LEGACY_BEHAVIOR_UNCHANGED',any(str(row[1])==str(c(30)) for row in old),'Frozen unguarded query retains its documented permissive legacy result.')
 h=clone(base);h.add((EX.person,RDF.type,OWL.Class));res=invoke('benign-punning',h)
 test('BENIGN_OWL_PUNNING_ALLOWED',res['status']=='VALIDATED_QUERY_RESULT','OWL class declaration alone is not a blacklist; no conflicting gUFO Type commitment is invented.')
 h=clone(base);h.remove((EX.organizationAssignment,AC.validFrom,None));res=invoke('unknown-start',h)
 test('UNKNOWN_START_REPORTED',res['status']=='VALIDATED_QUERY_RESULT' and res['owners']==[(str(EX.risk),str(EX.person))] and res['unknown_start_assignments']==[str(EX.organizationAssignment)],'Missing start is reported and does not fabricate a current owner.')
 h=clone(base);h.add((EX.incompleteLegacy,RDF.type,c(31)));res=invoke('mixed-incomplete-legacy',h)
 test('MIXED_LEGACY_SCOPE',res['status']=='VALIDATED_QUERY_RESULT' and res['explicit_legacy_assignment_count']==2 and res['legacy_grounding']=='NOT_ASSESSED_BY_OPT_IN_WORKFLOW','Unrelated non-opted application incompleteness is outside shape targets; whole data still passes consistency.')
 h=Graph();h.add((EX.incompleteLegacy,RDF.type,c(31)));res=invoke('legacy-only',h)
 test('LEGACY_ONLY_NOT_APPLICABLE',res['status']=='NOT_APPLICABLE' and res['code']=='NO_OPTED_ASSIGNMENTS' and res['consistency']=='NOT_ASSESSED','Legacy-only graph is not labeled grounded and supplies no owner result.')
 h=Graph();h.add((EX.inconsistentLegacy,RDF.type,c(31)));h.add((EX.inconsistentLegacy,RDF.type,GUFO.Type));res=invoke('inconsistent-legacy-only',h)
 test('INCONSISTENT_LEGACY_NOT_ASSESSED',res['status']=='NOT_APPLICABLE' and res['consistency']=='NOT_ASSESSED','No consistency claim or owner answer is made for inapplicable legacy-only data.')
 h=clone(base);h.add((EX.inconsistentLegacy,RDF.type,c(31)));h.add((EX.inconsistentLegacy,RDF.type,GUFO.Type));bad('N_MIXED_LEGACY_INCONSISTENCY',h,'CONSISTENCY','ONTOLOGY_INCONSISTENT')
 opted=set(base.subjects(RDF.type,AC.GroundedRiskResponsibility));scoped=scoped_shapes(opted)
 test('SHAPE_TARGET_SCOPE',not list(scoped.triples((None,SH.targetClass,None))) and set(scoped.objects(None,SH.targetNode))==opted,'Only opted nodes are targeted; existing constraint closures are copied unchanged.')
 # Isolate the missing-membership hole: two valid mediated Endurants remain.
 h=clone(base);h.remove((EX.personAssignment,GUFO.mediates,EX.person));h.add((EX.personAssignment,GUFO.mediates,EX.board))
 old_ok,_,_=validate(h,shacl_graph=scoped_shapes(opted,include_membership=False),inference='none',meta_shacl=True)
 result=bad('N_ASSIGNEE_NOT_MEDIATED',h,'SHACL',component='SPARQLConstraintComponent')
 test('MEMBERSHIP_REPAIR_ISOLATED',old_ok and any('GOWN_ASSIGNEE_MEDIATION' in m for m in result.get('messages',[])),'Old opted shapes conform; the separately versioned participant constraint rejects the exact missing assignee membership.')
 # Replace only the first assignment's holder, preserving membership/distinctness.
 def holder(target,extra_types=()):
  h=clone(base);h.set((EX.personAssignment,r(28),target));h.remove((EX.personAssignment,GUFO.mediates,EX.person));h.add((EX.personAssignment,GUFO.mediates,target));h.add((target,OWL.differentFrom,EX.organization))
  for typ in extra_types:h.add((target,RDF.type,typ))
  return h
 bad('N_BARE_ROLE_CLASS',holder(c(30)),'SHACL',component='ClassConstraintComponent')
 bad('N_FORGED_ROLE_ENDURANT',holder(c(30),[GUFO.Endurant]),'CONSISTENCY','ONTOLOGY_INCONSISTENT')
 h=clone(base);h.remove((EX.personAssignment,RDF.type,c(31)));bad('N_MISSING_EXPLICIT_PARENT',h,'INPUT_CONTRACT','EXPLICIT_PARENT_TYPE_REQUIRED')
 h=clone(base);h.remove((EX.person,RDF.type,GUFO.Endurant));bad('N_MISSING_PARTICIPANT_TYPE',h,'SHACL',component='ClassConstraintComponent')
 h=clone(base);h.remove((EX.personAssignment,GUFO.mediates,EX.organization));bad('N_MISSING_COUNTERPART',h,'SHACL',component='MinCountConstraintComponent')
 h=clone(base);h.remove((EX.person,OWL.differentFrom,EX.organization));bad('N_MISSING_DISTINCTNESS',h,'SHACL',component='SPARQLConstraintComponent')
 h=clone(base);h.set((EX.personAssignment,r(28),Literal('person')));bad('N_LITERAL_ASSIGNEE',h,'SHACL',component='NodeKindConstraintComponent')
 bad('N_EVENT_PARTICIPANT',holder(EX.event,[GUFO.Event]),'SHACL',component='ClassConstraintComponent')
 bad('N_FORGED_EVENT_ENDURANT',holder(EX.event,[GUFO.Event,GUFO.Endurant]),'CONSISTENCY','ONTOLOGY_INCONSISTENT')
 h=clone(base);h.add((EX.person,OWL.sameAs,EX.organization));bad('N_SAMEAS_ALIAS',h,'SHACL',component='SPARQLConstraintComponent')
 h=clone(base);h.set((EX.personAssignment,AC.validTo,Literal('2026-09-30T00:00:00Z',datatype=XSD.dateTime)));bad('N_REVERSED_INTERVAL',h,'SHACL',component='LessThanConstraintComponent')
 h=clone(base);h.set((EX.personAssignment,AC.validFrom,Literal('2026-10-01T00:00:00',datatype=XSD.dateTime)));bad('N_DATA_TIMEZONE',h,'SHACL',component='PatternConstraintComponent')
 for i,instant in enumerate([None,'2026-10-05T00:00:00','2026-02-30T00:00:00Z','2026-10-05T00:00:00+15:00'],1):
  res=invoke('bad-asof-'+str(i),base,instant);test('N_ASOF_'+str(i),res['status']=='VALIDATION_FAILED' and res['stage']=='INPUT_CONTRACT','Invalid or missing caller time fails explicitly before querying.')
 h=clone(base);h.add((EX.input,OWL.imports,URIRef('https://invalid.example/never-fetch')))
 res=bad('N_DATA_IMPORT',h,'INPUT_CONTRACT','DATA_IMPORTS_FORBIDDEN');test('NO_IMPORT_REASONER_CALL',not (out/'N_DATA_IMPORT'/'validation-world.owl').exists(),'Rejected imports never reach the reasoner.')
 # Exercise the actual command-line delivery, not only the Python function.
 cli_good=subprocess.run([sys.executable,str(ROOT/'tools/query_grounded_owners_v1.py'),'--data',str(DIR/'positive.ttl'),'--as-of',boundary,'--robot',str(robot),'--work-dir',str(out/'cli-positive')],text=True,capture_output=True,timeout=180)
 good=json.loads(cli_good.stdout);test('CLI_VALIDATED_RESULT',cli_good.returncode==0 and good['status']=='VALIDATED_QUERY_RESULT' and len(good['owners'])==2,'Actual CLI returns validated bounded owner pairs.')
 badpath=out/'bare-role-input.ttl';holder(c(30)).serialize(badpath,format='turtle')
 cli_bad=subprocess.run([sys.executable,str(ROOT/'tools/query_grounded_owners_v1.py'),'--data',str(badpath),'--as-of',boundary,'--robot',str(robot),'--work-dir',str(out/'cli-invalid')],text=True,capture_output=True,timeout=180)
 bad_result=json.loads(cli_bad.stdout);test('N_CLI_INVALID_NO_OWNERS',cli_bad.returncode==2 and bad_result['status']=='VALIDATION_FAILED' and 'owners' not in bad_result,'Actual CLI rejection is explicit, never an empty successful owner result.')
 (out/'cli-results.json').write_text(json.dumps({'positive':good,'negative':bad_result},indent=2)+'\n')
 # Explicitly simulated tool failures are software controls, not formal verdicts.
 mocked=[]
 for name,effects,stage in [
  ('mock-profile-error',[subprocess.CompletedProcess([],1,'','SIMULATED_PROFILE_TOOL_ERROR')],'OWL_PROFILE'),
  ('mock-reasoner-error',[subprocess.CompletedProcess([],0,'',''),subprocess.CompletedProcess([],1,'','SIMULATED_REASONER_TOOL_ERROR')],'TOOLCHAIN'),
  ('mock-timeout',[subprocess.TimeoutExpired(['java'],180)],'TOOLCHAIN')]:
  with patch('query_grounded_owners_v1.subprocess.run',side_effect=effects):res=invoke(name,base)
  require(res['status']=='VALIDATION_FAILED' and res['stage']==stage and 'owners' not in res,'MOCK_FAILURE_PATH: '+name)
  mocked.append({'id':name,'passed':True,'kind':'SIMULATED_TOOL_FAILURE_ONLY','stage':stage})
 source_contract()
 return {'mocked_software_controls':mocked,'result':'PASS_OPT_IN_VALIDATION_FIRST_OWNERSHIP','protocol_sha256':hashlib.sha256((DIR/'protocol.json').read_bytes()).hexdigest(),'tests':tests,'total':len(tests),'passed':len(tests),'negative_controls':sum(t['id'].startswith('N_') for t in tests),'legacy_bytes_unchanged':True,'default_profile_changed':False,'full_FAP006_status':'NOT_ESTABLISHED','scope':'Only the explicitly opted, validated and consistent supplied records; no real-world identity or authority guarantee.','source_sha256':protocol['source_sha256']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--robot',type=Path,required=True);p.add_argument('--build-dir',type=Path,default=ROOT/'build/grounded-ownership-v1');p.add_argument('--write',action='store_true');a=p.parse_args();result=run(a.robot,a.build_dir);text=json.dumps(result,indent=2)+'\n'
 if a.write:(DIR/'results.json').write_text(text)
 else:require((DIR/'results.json').read_text()==text,'RESULT_DRIFT')
 print(text,end='')
