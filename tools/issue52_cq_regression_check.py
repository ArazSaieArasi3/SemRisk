#!/usr/bin/env python3
"""Governance/regression gate for SemRisk Issue #52.
Underlying executable CQ evidence is produced by Semantic CI and the #48/#49/#50
relational/RDF harnesses. This gate prevents CQ deletion, silent state drift, or
undefined release-critical dispositions.
"""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
src=list(csv.DictReader((ROOT/"conceptualization/requirements/conceptual-cq-registry.csv").open(encoding="utf-8")))
res=list(csv.DictReader((ROOT/"evaluation/cq/issue52-cq-results-v1.0.csv").open(encoding="utf-8")))

allowed={"conceptual_only","executable","partially_executable","deferred","not_applicable","failed"}
src_ids=[r["cq_id"] for r in src]
res_ids=[r["cq_id"] for r in res]

if len(src)!=40 or len(set(src_ids))!=40:
    raise SystemExit(f"FAIL: canonical CQ registry expected 40 unique CQs, found {len(src)}/{len(set(src_ids))}")
if set(src_ids)!=set(res_ids) or len(res)!=40:
    missing=sorted(set(src_ids)-set(res_ids)); extra=sorted(set(res_ids)-set(src_ids))
    raise SystemExit(f"FAIL: CQ result denominator drift; missing={missing}, extra={extra}, rows={len(res)}")

byid={r["cq_id"]:r for r in res}
for s in src:
    r=byid[s["cq_id"]]
    if r["state"] not in allowed:
        raise SystemExit(f"FAIL: invalid state {r['state']} for {s['cq_id']}")
    if not r["evaluation_result"] or not r["semantic_review"] or not r["claim_consequence"]:
        raise SystemExit(f"FAIL: incomplete disposition for {s['cq_id']}")
    if s["paper1_subset"]=="DEFERRED" and r["state"]!="deferred":
        raise SystemExit(f"FAIL: deferred Paper-1 boundary changed for {s['cq_id']}")
    if s["paper1_subset"]!="DEFERRED" and r["state"] in {"deferred","not_applicable"}:
        raise SystemExit(f"FAIL: applicable CQ silently deferred: {s['cq_id']}")

counts={k:0 for k in allowed}
for r in res: counts[r["state"]]+=1
expected={"executable":26,"partially_executable":7,"conceptual_only":6,"deferred":1,"not_applicable":0,"failed":0}
if any(counts[k]!=v for k,v in expected.items()):
    raise SystemExit(f"FAIL: disposition-count drift; expected={expected}, actual={counts}")

# Predeclared E2E and parity registries must remain present because they provide
# executable evidence for claim-critical CQ subsets.
e2e=list(csv.DictReader((ROOT/"case/pharma/e2e-scenario-expected-v1.0.csv").open(encoding="utf-8")))
p49=list(csv.DictReader((ROOT/"evaluation/parity/p49-paired-query-registry-v1.0.csv").open(encoding="utf-8")))
if len(e2e)!=10 or len(p49)!=8:
    raise SystemExit(f"FAIL: executable expected-answer registries drifted: e2e={len(e2e)}, parity={len(p49)}")

print("PASS: 40/40 original CQs retained and dispositioned")
print("PASS: applicable denominator=39; executable=26; partial=7; conceptual_only=6; deferred=1; failed=0")
print("PASS: predeclared executable answer registries remain 10 E2E + 8 parity tasks")
print("SEM_RISK_ISSUE_52_CQ_REGRESSION_GOVERNANCE_PASS")
