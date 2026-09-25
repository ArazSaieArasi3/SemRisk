#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
MAN=ROOT/"relational/design/migration-manifest-v1.0.csv"

def fail(msg):
    raise SystemExit("FAIL R6 migration governance: "+msg)

def git_blob_sha(path: Path):
    data=path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

rows=list(csv.DictReader(MAN.open(encoding="utf-8",newline="")))
if [int(r["order_id"]) for r in rows] != list(range(1,len(rows)+1)):
    fail("order_id sequence is not contiguous")

for r in rows:
    p=ROOT/r["path"]
    if not p.exists():
        fail(f"missing governed migration artifact: {r['path']}")
    actual=git_blob_sha(p)
    if actual != r["git_blob_sha"]:
        fail(f"immutable artifact drift: {r['path']} expected={r['git_blob_sha']} actual={actual}")

schema_versions=[int(r["version"]) for r in rows if r["role"]=="schema_migration"]
if schema_versions != sorted(schema_versions) or schema_versions != [1,2,5,6]:
    fail(f"unexpected schema migration order: {schema_versions}")

wf=(ROOT/".github/workflows/semrisk-relational-ci.yml").read_text(encoding="utf-8")
positions={}
for v in ("V001__paper1_projection.sql","V002__data_load_support.sql","V005__r5_architecture_federation.sql","V006__r6_projection_integrity.sql"):
    positions[v]=wf.find(v)
    if positions[v] < 0:
        fail(f"workflow does not execute {v}")
if not (positions["V001__paper1_projection.sql"] < positions["V002__data_load_support.sql"] < positions["V005__r5_architecture_federation.sql"] < positions["V006__r6_projection_integrity.sql"]):
    fail(f"workflow migration order drifted: {positions}")

print("PASS: relational migration manifest paths and immutable Git blob hashes match")
print("PASS: schema migration order is V001 -> V002 -> V005 -> V006")
print("SEM_RISK_R6_MIGRATION_GOVERNANCE_PASS")
