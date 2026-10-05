#!/usr/bin/env python3
"""Run in a disposable native PostgreSQL database only."""
import sys,json
import psycopg
from rdflib import RDF
from check_exposure_scale import ROOT,EX,AC,fixture,clone,at,c,r
sys.path.insert(0,str(ROOT/'relational/scripts'))
from exposure_io import load_graph,export_graph,normalized,at_sql,uid
def main():
 tests=[];conn=psycopg.connect('',autocommit=True);conn.execute("SET TIME ZONE 'UTC'")
 def test(id,ok):
  tests.append({'id':id,'passed':bool(ok)})
  if not ok:raise AssertionError(id)
 d=fixture()
 with conn.transaction():load_graph(conn,d)
 test('EXPOSURE-ROUNDTRIP',normalized(d)==normalized(export_graph(conn,str(EX))))
 with conn.transaction():load_graph(conn,d)
 test('IDEMPOTENT-LOAD',len(list(export_graph(conn,str(EX)).subjects(RDF.type,c(10))))==2)
 for i,t in enumerate(['2026-09-30T23:59:59Z','2026-10-04T23:59:59Z','2026-10-05T00:00:00Z','2026-10-05T03:30:00+03:30'],1):test('ASOF-'+str(i),at_sql(conn,t,str(EX))==at(d,t))
 for id,mut in [('MISSING-SUBJECT',lambda h:h.remove((EX.exposureA,r(39),None))),('UNTYPED-SOURCE',lambda h:h.remove((EX.source,RDF.type,c(3)))),('HISTORY-REWRITE',lambda h:h.remove((EX.exposureA,AC.validTo,None)))]:
  h=clone(d);mut(h)
  try:
   with conn.transaction():load_graph(conn,h)
  except ValueError:test(id,True)
  else:test(id,False)
 try:
  with conn.transaction():conn.execute('UPDATE core.exposure SET valid_to=valid_from WHERE exposure_id=%s',(uid(EX.exposureA),))
 except psycopg.errors.CheckViolation:test('DATABASE-INTERVAL-GUARD',True)
 else:test('DATABASE-INTERVAL-GUARD',False)
 test('NEGATIVES-PRESERVE-ROWS',normalized(d)==normalized(export_graph(conn,str(EX))))
 result=dict(version='0.2.0-rc.4',total=len(tests),passed=sum(x['passed'] for x in tests),represented_triples=len(normalized(d)),exposure_rows=2,tests=tests,scope='Existing V001 exposure table; synthetic endpoints and intervals only; scale/workflow parity excluded',postgres=conn.execute('SELECT version()').fetchone()[0]);(ROOT/'evaluation/exposure-scale/v0.2.0-rc.4/postgres-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
