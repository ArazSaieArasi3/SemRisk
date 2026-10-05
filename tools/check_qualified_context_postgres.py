#!/usr/bin/env python3
"""Run only against a disposable PostgreSQL regression database, pre-V007."""
import argparse
import json
import sys
from pathlib import Path
import psycopg
from psycopg import sql
from rdflib import Literal, XSD
from check_qualified_context import ROOT,V,EX,fixture,owner_rows,validate_graph
sys.path.insert(0,str(ROOT/'relational/scripts'))
from qualified_context_io import uid,load_graph,export_graph,normalized_triples

def main():
 conn=psycopg.connect('',autocommit=True)
 conn.execute("SET TIME ZONE 'UTC'")
 tests=[]
 def record(id_,ok,detail):
  tests.append({'id':id_,'passed':bool(ok),'details':detail})
  if not ok:raise AssertionError(json.dumps(tests[-1]))
 tables=conn.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema IN ('meta','ref','core','assessment','enterprise','governance','pharma','staging','treatment') ORDER BY 1,2").fetchall()
 columns={}
 for schema,table in tables:
  columns[(schema,table)]=[x[0] for x in conn.execute('SELECT column_name FROM information_schema.columns WHERE table_schema=%s AND table_name=%s ORDER BY ordinal_position',(schema,table))]
 def snapshots():
  result={}
  for (schema,table),cols in columns.items():
   q=sql.SQL("SELECT count(*),md5(coalesce(string_agg(row_to_json(t)::text,'' ORDER BY row_to_json(t)::text),'')) FROM (SELECT {} FROM {}.{}) t").format(sql.SQL(',').join(map(sql.Identifier,cols)),sql.Identifier(schema),sql.Identifier(table))
   result[schema+'.'+table]=list(conn.execute(q).fetchone())
  return result
 before=snapshots()
 record('MIGRATION-POPULATED',sum(v[0] for v in before.values())>0,'Regression database contains the governed legacy fixture before V007.')
 migration=(ROOT/'relational/sql/V007__qualified_assessment_context.sql').read_text()
 rollback=(ROOT/'relational/sql/rollback/U007__qualified_assessment_context.sql').read_text()
 conn.execute(migration)
 record('MIGRATION-PRESERVES-ROWS',snapshots()==before,{'legacy_tables':len(before),'legacy_rows':sum(v[0] for v in before.values())})
 record('MIGRATION-NO-INVENTED-CONTEXT',conn.execute('SELECT count(*) FROM assessment.result_context').fetchone()[0]==0,'No automatic context or score backfill.')
 conn.execute(rollback)
 record('ROLLBACK-EMPTY',snapshots()==before,'Empty-profile rollback preserves all original columns and rows.')
 conn.execute(migration)
 g=fixture()
 with conn.transaction():load_graph(conn,g)
 count=conn.execute('SELECT count(*) FROM assessment.result_context').fetchone()[0]
 record('LOAD-QUALIFIED',count==5,{'synthetic_results':count})
 out=export_graph(conn,str(EX))
 a,b=normalized_triples(g),normalized_triples(out)
 record('ROUNDTRIP-ALL-FIELDS',a==b,{'expected_triples':len(a),'actual_triples':len(b),'missing':list(map(str,a-b))[:5],'extra':list(map(str,b-a))[:5]})
 ok,_,txt=validate_graph(out)
 record('ROUNDTRIP-SHACL',ok,txt.strip())
 stamps=['2026-09-30T23:59:59Z','2026-10-01T00:00:00Z','2026-10-04T00:00:00Z','2026-10-05T08:00:00Z','2026-10-06T00:00:00Z','2026-10-05T11:30:00+03:30']
 for i,stamp in enumerate(stamps,1):
  expected=owner_rows(g,stamp)
  actual=[list(x) for x in conn.execute('SELECT risk_iri,actor_iri FROM enterprise.risk_owners_at(assessment.parse_zoned_timestamp(%s)) WHERE risk_iri=%s ORDER BY 1,2',(stamp,str(EX.risk)))]
  record(f'OWNER-PARITY-{i}',actual==expected,{'at':stamp,'rows':actual})
 rows=conn.execute('SELECT dimension,control_baseline,evaluation_basis,count(*) FROM assessment.v_qualified_result_context WHERE risk_iri=%s GROUP BY 1,2,3 ORDER BY 1,2,3',(str(EX.risk),)).fetchall()
 record('ORTHOGONAL-AXES',rows==[('Impact','AfterControl','Observed',1),('Likelihood','AfterControl','Observed',2),('Likelihood','AfterControl','Projected',1),('Likelihood','BeforeControl','Projected',1)],rows)

 class AcceptedInvalid(Exception):pass
 def rejected(id_,action,code,marker):
  try:
   with conn.transaction():
    action();raise AcceptedInvalid()
  except AcceptedInvalid:record(id_,False,'Invalid data accepted')
  except psycopg.Error as e:
   record(id_,e.sqlstate==code and marker in str(e),{'sqlstate':e.sqlstate,'expected_marker':marker,'observed':str(e).splitlines()[0]})
 def execute(q,args=None):return lambda:conn.execute(q,args)
 def new_result_context(tag,**changes):
  s=EX['negative-'+tag];rid=uid(s)
  conn.execute('INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,evidence_role,synthetic_flag) VALUES(%s,%s,%s,%s,true)',(rid,str(s),'SR-CPT-018','synthetic_test'))
  risk=changes.pop('risk',uid(EX.risk));value=changes.pop('value','0.4');prior=changes.pop('prior',None)
  conn.execute('INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,value_numeric,supersedes_result_id) VALUES(%s,%s,%s,%s,%s,%s)',(rid,uid(EX.assessment),risk,'residual',value,prior))
  context={'dimension':'Likelihood','control_baseline':'AfterControl','evaluation_basis':'Observed','scale_iri':str(EX.scale),'method_id':uid(EX.method),'method_version':'synthetic-method-1','assessed_at':'2026-10-05T08:30:00Z','reference_time':'2026-10-04T08:00:00Z'}
  context.update(changes)
  conn.execute('INSERT INTO assessment.result_context VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(rid,*context.values()))
 rejected('SQL-N01',execute("SELECT assessment.parse_zoned_timestamp('2026-10-05T08:00:00')"),'23514','explicit timestamp timezone')
 rejected('SQL-N02',execute('UPDATE enterprise.risk_responsibility SET valid_to=%s WHERE responsibility_id=%s',('2026-09-30T00:00:00Z',uid(EX['owner-active']))),'23514','ck_risk_responsibility_period')
 rejected('SQL-N03',lambda:new_result_context('missing',dimension=None),'23502','dimension')
 rejected('SQL-N04',lambda:new_result_context('basis',evaluation_basis='Unknown'),'23514','evaluation_basis_check')
 rejected('SQL-N05',lambda:new_result_context('value',value='1.5'),'23514','incompatible with scale')
 rejected('SQL-N06',lambda:new_result_context('scale',scale_iri=str(EX['impact-scale'])),'23514','incompatible with scale')
 rejected('SQL-N07',lambda:new_result_context('version',method_version='unknown'),'23514','method/version mismatch')
 other=EX['other-risk']
 with conn.transaction():
  conn.execute('INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,evidence_role,synthetic_flag) VALUES(%s,%s,%s,%s,true)',(uid(other),str(other),'SR-CPT-001','synthetic_test'))
  conn.execute('INSERT INTO core.risk(risk_id) VALUES(%s)',(uid(other),))
 rejected('SQL-N08',lambda:new_result_context('risk',risk=uid(other)),'23514','activity/risk/method/version mismatch')
 rejected('SQL-N09',lambda:new_result_context('supersede',risk=uid(other),prior=uid(EX.observed)),'23514','same Risk')
 rejected('SQL-N10',lambda:new_result_context('chronology',prior=uid(EX.observed),assessed_at='2026-10-05T07:00:00Z'),'23514','precedes predecessor')
 rejected('SQL-N11',lambda:new_result_context('type',control_baseline='BeforeControl'),'23514','contradicts legacy result kind')
 rejected('SQL-N12',execute('UPDATE assessment.assessment_result SET value_numeric=0.9 WHERE result_id=%s',(uid(EX.observed),)),'23514','history is immutable')
 rejected('SQL-N13',execute('UPDATE assessment.assessment_method SET version_ref=%s WHERE method_id=%s',('changed',uid(EX.method))),'23514','history is immutable')
 rejected('SQL-N14',execute('UPDATE assessment.numeric_scale SET maximum=2.0 WHERE scale_iri=%s',(str(EX.scale),)),'23514','history is immutable')
 rejected('SQL-N15',execute('UPDATE assessment.assessment_activity SET risk_id=%s WHERE assessment_id=%s',(uid(other),uid(EX.assessment))),'23514','history is immutable')
 rejected('SQL-N16',execute('DELETE FROM assessment.result_context WHERE result_id=%s',(uid(EX.observed),)),'23514','append-only')
 # Run guard in a transaction, without nested BEGIN/COMMIT from the standalone script.
 guarded_rollback=rollback.replace('\nBEGIN;\n','\n',1).rsplit('COMMIT;',1)[0]
 rejected('SQL-N17',execute(guarded_rollback),'23514','rollback refused')
 record('NEGATIVES-ROLLED-BACK',normalized_triples(export_graph(conn,str(EX)))==a,'All rejected mutations leave qualified source records unchanged.')
 # Restore only the extra test risk, outside the qualified projection.
 conn.execute('DELETE FROM core.risk WHERE risk_id=%s',(uid(other),));conn.execute('DELETE FROM meta.semantic_instance WHERE instance_id=%s',(uid(other),))
 outdir=ROOT/f'evaluation/temporal/v{V}';outdir.mkdir(parents=True,exist_ok=True)
 result={'profile_version':V,'postgres_version':conn.execute('SHOW server_version').fetchone()[0],
  'driver_version':psycopg.__version__,'total':len(tests),'passed':sum(t['passed'] for t in tests),
  'tests':tests,'negative_controls':17,'legacy_snapshot':before,'synthetic_only':True,
  'production_migration_performed':False,'general_concurrency_proof':False}
 conn.close();return result
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
 result=main()
 if args.write:(ROOT/f'evaluation/temporal/v{V}/postgres-results.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
 print('QUALIFIED_CONTEXT_RESULT_JSON='+json.dumps(result,default=str))
