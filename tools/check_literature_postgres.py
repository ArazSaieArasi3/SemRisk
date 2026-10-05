#!/usr/bin/env python3
import copy,json,sys
import psycopg
from build_pharma_literature_pilot import ROOT,DATA,read,write,graph
sys.path.insert(0,str(ROOT/'relational/scripts'))
from literature_io import load,export,uid,BATCH_CODE

def main():
 rows=read('statements.json');maps=read('mappings.json');sources=read('sources.json');tests=[]
 def test(n,ok):tests.append(dict(id=n,passed=bool(ok)));assert ok,n
 with psycopg.connect('',autocommit=True) as c:
  test('NATIVE-LOAD',load(c,rows,maps,sources)==24)
  test('IDEMPOTENT-LOAD',load(c,rows,maps,sources)==24)
  r,m,s=export(c);test('PAYLOAD-ROUNDTRIP',(r,m,s)==(rows,maps,sources))
  test('RDF-RECONSTRUCTION',set(graph(r,m,s))==set(graph(rows,maps,sources)))
  test('PROVENANCE-ROWS',c.execute('SELECT count(*) FROM meta.instance_provenance').fetchone()[0]==24)
  test('NO-DOMAIN-INCIDENTS',c.execute('SELECT count(*) FROM core.risk_event').fetchone()[0]==0)
  for field,expected in [('source_id',{'PLS-001':8,'PLS-002':4,'PLS-003':4,'PLS-004':3,'PLS-005':3,'PLS-006':2}),('source_role',{'design_reused':15,'evaluation_new':9})]:
   got=dict(c.execute("SELECT raw_semantic_summary::jsonb->'statement'->>%s,count(*) FROM staging.source_record WHERE load_batch_id=%s GROUP BY 1",(field,uid(BATCH_CODE))).fetchall())
   test('SQL-GROUP-'+field,got==expected)
  got=dict(c.execute("SELECT raw_semantic_summary::jsonb->'mapping'->>'mapping_status',count(*) FROM staging.source_record WHERE load_batch_id=%s GROUP BY 1",(uid(BATCH_CODE),)).fetchall());test('SQL-MAPPING-GROUP',got=={'partial':12,'ambiguous':11,'unmapped':1})
  for name,mut in [('REWRITE',lambda r,m,s:r[0].update(statement_paraphrase='changed existing version')),('MISSING-PROVENANCE',lambda r,m,s:r[0].update(source_locator='')),('FALSE-HOLDOUT',lambda r,m,s:s[0].update(independent_validation=True))]:
   a,b,d=copy.deepcopy((rows,maps,sources));mut(a,b,d)
   try:load(c,a,b,d)
   except (ValueError,AssertionError):test('NEGATIVE-'+name,True)
   else:test('NEGATIVE-'+name,False)
  test('AFTER-REJECTION-UNCHANGED',export(c)==(rows,maps,sources))
  result=dict(result='PASS_NATIVE_INFORMATION_STAGING',total=len(tests),passed=sum(t['passed'] for t in tests),postgres=c.execute('SELECT version()').fetchone()[0],records=24,sources=6,reconstructed_rdf_triples=len(graph(rows,maps,sources)),tests=tests,boundary='RDF reconstruction uses complete JSON source/statement/mapping payloads retained in staging, not native columns for every domain relation. No temporal assessment/scale/workflow SQL parity or clinical validation claim.')
 write('postgres-results.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
