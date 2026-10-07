#!/usr/bin/env python3
"""Opt-in validation-first ownership. No change to frozen/default rc.4 behavior."""
import argparse,hashlib,json,platform,re,subprocess,tempfile
from datetime import datetime
from pathlib import Path
import rdflib,pyshacl
from rdflib import Graph,Namespace,URIRef,BNode,Literal,RDF,OWL,XSD
from pyshacl import validate
from check_rc4_extension import closure,c,AC
ROOT=Path(__file__).resolve().parents[1];DIR=ROOT/'evaluation/grounded-ownership/v1'
SH=Namespace('http://www.w3.org/ns/shacl#');FS=Namespace('urn:semrisk:shape:foundational-evidence:')
GOWN=Namespace('urn:semrisk:shape:grounded-ownership:v1:')
PROTOCOL_SHA='337459943ef5c1b12eb0cd4be106ef3336ea379e90fa2fda0ef377b7bcbde505'
def failure(stage,code,**extra):return {'status':'VALIDATION_FAILED','stage':stage,'code':code,**extra}
def source_contract():
 raw=(DIR/'protocol.json').read_bytes()
 if hashlib.sha256(raw).hexdigest()!=PROTOCOL_SHA:raise ValueError('PROTOCOL_DRIFT')
 p=json.loads(raw)
 for name,digest in {**p['source_sha256'],**p['new_artifact_sha256']}.items():
  if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:raise ValueError('SOURCE_DRIFT: '+name)
 return p

def time_value(value):
 if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})',value):raise ValueError('AS_OF_REQUIRED_AWARE_DATETIME')
 if not value.endswith('Z'):
  hours,minutes=map(int,value[-5:].split(':'))
  if minutes>59 or hours>14 or (hours==14 and minutes):raise ValueError('AS_OF_TIMEZONE_RANGE')
 parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
 if parsed.tzinfo is None:raise ValueError('AS_OF_TIMEZONE_REQUIRED')
 return Literal(value,datatype=XSD.dateTime)

def scoped_shapes(opted,include_membership=True):
 """Copy existing constraints unchanged; only target selection is scoped."""
 specs=[('shapes/assessment-context-v0.2.0-rc.1.ttl',AC.ResponsibilityShape),('shapes/foundational-evidence-v0.2.0-rc.2.ttl',FS.GroundedResponsibilityShape)]
 if include_membership:specs.append(('shapes/grounded-ownership-entrypoint-v1.ttl',GOWN.OptedAssignmentShape))
 result=Graph()
 for path,root in specs:
  source=Graph().parse(ROOT/path);todo=[root];seen=set()
  if (root,RDF.type,SH.NodeShape) not in source:raise ValueError('SHAPE_ROOT_MISSING: '+str(root))
  while todo:
   node=todo.pop()
   if node in seen:continue
   seen.add(node)
   for triple in source.triples((node,None,None)):
    result.add(triple)
    if isinstance(triple[2],BNode):todo.append(triple[2])
  for target in [SH.targetClass,SH.targetNode,SH.targetSubjectsOf,SH.targetObjectsOf]:result.remove((root,target,None))
  for assignment in opted:result.add((root,SH.targetNode,assignment))
 return result

def guarded_query(data,as_of,robot,work_dir):
 """Return owners only after explicit input, shape, DL and consistency success."""
 try:
  protocol=source_contract();instant=time_value(as_of)
  runtime={'python':platform.python_version(),'rdflib':rdflib.__version__,'pyshacl':pyshacl.__version__}
  if runtime['python'].split('.')[:2]!=['3','12'] or runtime['rdflib']!='7.6.0' or runtime['pyshacl']!='0.40.1':return failure('TOOLCHAIN','PYTHON_LIBRARY_VERSION')
  if not isinstance(data,Graph):return failure('INPUT_CONTRACT','RDF_GRAPH_REQUIRED')
  if any(data.triples((None,OWL.imports,None))):return failure('INPUT_CONTRACT','DATA_IMPORTS_FORBIDDEN')
  if not robot.is_file() or hashlib.sha256(robot.read_bytes()).hexdigest()!=protocol['toolchain']['robot_sha256']:return failure('TOOLCHAIN','ROBOT_BYTES')
 except (ValueError,OSError) as exc:return failure('INPUT_CONTRACT',str(exc))
 opted=set(data.subjects(RDF.type,AC.GroundedRiskResponsibility));legacy=set(data.subjects(RDF.type,c(31)))-opted
 counts={'opted_assignment_count':len(opted),'explicit_legacy_assignment_count':len(legacy),'legacy_grounding':'NOT_ASSESSED_BY_OPT_IN_WORKFLOW'}
 if not opted:return {'status':'NOT_APPLICABLE','code':'NO_OPTED_ASSIGNMENTS','consistency':'NOT_ASSESSED',**counts}
 if any((s,RDF.type,c(31)) not in data for s in opted):return failure('INPUT_CONTRACT','EXPLICIT_PARENT_TYPE_REQUIRED',**counts)
 try:
  work_dir.mkdir(parents=True,exist_ok=True)
  if any(work_dir.iterdir()):return failure('INPUT_CONTRACT','WORK_DIRECTORY_MUST_BE_EMPTY')
  (work_dir/'runtime.json').write_text(json.dumps(runtime,indent=2)+'\n')
  shapes=scoped_shapes(opted);shapes.serialize(work_dir/'scoped-shapes.ttl',format='turtle');data.serialize(work_dir/'data.ttl',format='turtle')
  ok,report,message=validate(data,shacl_graph=shapes,inference='none',meta_shacl=True)
  if not isinstance(report,Graph):return failure('TOOLCHAIN','SHACL_ENGINE_FAILURE',**counts)
  report.serialize(work_dir/'shape-report.ttl',format='turtle');(work_dir/'shape-report.txt').write_text(message)
  if not ok:
   components=sorted({str(x) for x in report.objects(None,SH.sourceConstraintComponent)})
   messages=sorted({str(x) for x in report.objects(None,SH.resultMessage)})
   return failure('SHACL','SHAPE_CONSTRAINT',components=components,messages=messages,**counts)
  ontology,seen=closure();ontology+=data;ontology.serialize(work_dir/'validation-world.owl',format='xml')
  profile=subprocess.run(['java','-jar',str(robot),'validate-profile','--profile','DL','--input',str(work_dir/'validation-world.owl'),'--output',str(work_dir/'dl.txt')],text=True,capture_output=True,timeout=180)
  (work_dir/'profile.log').write_text(profile.stdout+profile.stderr)
  if profile.returncode:return failure('OWL_PROFILE','OWL2DL_FAILED',**counts)
  proc=subprocess.run(['java','-jar',str(robot),'reason','--reasoner','HermiT','--input',str(work_dir/'validation-world.owl'),'--output',str(work_dir/'reasoned.owl')],text=True,capture_output=True,timeout=180)
  log=proc.stdout+proc.stderr;(work_dir/'reasoner.log').write_text(log)
  if proc.returncode:
   if 'the ontology is inconsistent' in log.lower():return failure('CONSISTENCY','ONTOLOGY_INCONSISTENT',**counts)
   return failure('TOOLCHAIN','REASONER_FAILED',**counts)
  query=(ROOT/'rules/enterprise/risk-owners-grounded-v1.rq').read_text()
  owners=sorted(tuple(map(str,row)) for row in data.query(query,initBindings={'asOf':instant}))
  unknown=sorted(str(s) for s in opted if not list(data.objects(s,AC.validFrom)))
  return {'status':'VALIDATED_QUERY_RESULT','as_of':as_of,'owners':owners,**counts,'unknown_start_assignments':unknown,'source_protocol_sha256':PROTOCOL_SHA,'ontology_closure_files':len(seen),'scope':'Only opted records with explicit query evidence; no universal owner absence, real-world identity or authority claim.'}
 except Exception as exc:return failure('TOOLCHAIN','EXECUTION_FAILED',detail=type(exc).__name__,**counts)

def cli():
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--as-of',required=True);p.add_argument('--robot',type=Path,required=True);p.add_argument('--work-dir',type=Path);args=p.parse_args()
 try:
  if not args.data.is_file():raise ValueError('LOCAL_DATA_FILE_REQUIRED')
  data=Graph().parse(args.data.resolve(),format='turtle')
 except Exception as exc:
  result=failure('INPUT_PARSE','INVALID_TURTLE',detail=type(exc).__name__);print(json.dumps(result,indent=2));return 2
 if args.work_dir:result=guarded_query(data,args.as_of,args.robot,args.work_dir)
 else:
  with tempfile.TemporaryDirectory(prefix='semrisk-grounded-') as d:result=guarded_query(data,args.as_of,args.robot,Path(d))
 print(json.dumps(result,indent=2));return 0 if result['status']=='VALIDATED_QUERY_RESULT' else 2
if __name__=='__main__':raise SystemExit(cli())
