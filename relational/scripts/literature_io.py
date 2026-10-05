"""Idempotent, immutable source-local literature staging on existing V001/V002 DDL.

This adapter preserves evidence payloads. It is NOT a complete rc.4 domain projection.
"""
import json,uuid,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
from build_pharma_literature_pilot import BASE
from check_pharma_literature_pilot import validate
NS=uuid.UUID('cfe631d1-051e-5549-bfb4-1cb76f1bd195')
BATCH_CODE='PHARMA_LITERATURE_0_1_0'
def uid(key):return uuid.uuid5(NS,key)
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def load(conn,rows,mappings,sources):
 validate(rows,mappings,sources)
 mm={m['statement_id']:m for m in mappings};ss={s['source_id']:s for s in sources}
 with conn.transaction():
  bid=uid(BATCH_CODE)
  existing=conn.execute('SELECT source_record_key,raw_semantic_summary FROM staging.source_record WHERE load_batch_id=%s',(bid,)).fetchall()
  expected={r['statement_id']:canonical(dict(statement=r,mapping=mm[r['statement_id']],source=ss[r['source_id']])) for r in rows}
  if existing:
   if dict(existing)!=expected:raise ValueError('IMMUTABLE_BATCH_REWRITE')
   return len(existing)
  conn.execute('INSERT INTO staging.load_batch(load_batch_id,batch_code,pipeline_version,status,source_scope,repository_commit,notes) VALUES (%s,%s,%s,%s,%s,%s,%s)',(bid,BATCH_CODE,'0.1.0','started','Source-local pharmaceutical literature statements','231a82cde3a43ccbafc06afa744ea9df35af7c26','Information staging only; no source row is an observed incident.'))
  for s in sources:
   conn.execute('INSERT INTO meta.source_artifact(source_artifact_id,source_kind,locator,version_ref,license,evidence_role,accessed_at) VALUES (%s,%s,%s,%s,%s,%s,%s)',(uid(s['source_id']),'primary-research-publication','https://doi.org/'+s['doi'],s['version'],s['rights_note'],'bounded_case',s['accessed_at']))
  for r in rows:
   sid=r['statement_id'];m=mm[sid];a=uid(sid);source=uid(r['source_id'])
   conn.execute('INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag) VALUES (%s,%s,%s,%s,%s,false)',(a,BASE+sid,'urn:semrisk:profile:information-state:ManagedInformationArtifact',source,'bounded_case'))
   conn.execute('INSERT INTO meta.instance_provenance(instance_provenance_id,instance_id,source_artifact_id,derivation_note) VALUES (%s,%s,%s,%s)',(uid(sid+':provenance'),a,source,'AI-assisted paraphrase; source-local locator in staging; no expert validation.'))
   conn.execute('INSERT INTO staging.source_record(source_record_id,load_batch_id,source_artifact_id,source_record_key,source_locator,raw_semantic_summary,transform_rule_id,target_instance_iri,disposition) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(uid(sid+':record'),bid,source,sid,r['source_locator'],expected[sid],'literature-pilot-v0.1.0',BASE+sid,'partial' if m['mapping_status']=='partial' else 'context_only'))
  conn.execute('UPDATE staging.load_batch SET status=%s,completed_at=transaction_timestamp() WHERE load_batch_id=%s',('completed',bid))
 return len(rows)
def export(conn):
 rows=conn.execute('SELECT raw_semantic_summary FROM staging.source_record WHERE load_batch_id=%s ORDER BY source_record_key',(uid(BATCH_CODE),)).fetchall()
 payload=[json.loads(r[0]) for r in rows];sources={r['source']['source_id']:r['source'] for r in payload}
 return [r['statement'] for r in payload],[r['mapping'] for r in payload],[sources[k] for k in sorted(sources)]
