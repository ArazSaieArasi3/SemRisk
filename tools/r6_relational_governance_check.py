#!/usr/bin/env python3
from pathlib import Path
import csv,re

ROOT=Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit("FAIL R6 relational governance: "+msg)

coverage=list(csv.DictReader((ROOT/"evaluation/data/r6-parity-cq-coverage-v1.0.csv").open(encoding="utf-8",newline="")))
if len(coverage)!=40 or len({r["cq_id"] for r in coverage})!=40:
    fail("CQ parity coverage matrix must contain exactly 40 unique CQs")
direct=[r for r in coverage if r["parity_scope"]=="DIRECT_P49_TASK"]
if len(direct)!=17:
    fail(f"expected 17 CQs directly represented by frozen P49 tasks, got {len(direct)}")
if len({r["p49_pair"] for r in direct})!=8:
    fail("direct CQ coverage must resolve to exactly 8 P49 tasks")

reg=list(csv.DictReader((ROOT/"evaluation/parity/p49-paired-query-registry-v1.0.csv").open(encoding="utf-8",newline="")))
if len(reg)!=8:
    fail("P49 denominator drifted from 8 tasks")
if any(r["expected_parity_class"]!="equivalent_for_task" for r in reg):
    fail("R6 direct-identity parity contract still contains normalized/partial expected classes")
if any("normalize" in r["comparison_rule"].lower() for r in reg):
    fail("identity-erasing normalization remains in a P49 comparison rule")

v001=(ROOT/"relational/sql/V001__paper1_projection.sql").read_text(encoding="utf-8")
m=re.search(r"CREATE TABLE core\.risk\s*\((.*?)\);",v001,re.I|re.S)
if not m:
    fail("core.risk table not found")
risk_body=m.group(1).lower()
for forbidden in ("owner_id","status_code","risk_score","inherent_score","residual_score","current_score"):
    if forbidden in risk_body:
        fail(f"performance/application shortcut leaked into core.risk: {forbidden}")

views=(ROOT/"relational/sql/V001__views.sql").read_text(encoding="utf-8")
if "FROM enterprise.risk_responsibility" not in views or "CREATE OR REPLACE VIEW enterprise.v_risk_owner" not in views:
    fail("Risk Owner is no longer derived from responsibility")

v6=(ROOT/"relational/sql/V006__r6_projection_integrity.sql").read_text(encoding="utf-8")
for token in ("actor_iri","enforce_state_transition_scope","enforce_prior_assessment_lineage","enforce_result_supersession_lineage","staging.v_lineage_reconciliation"):
    if token not in v6:
        fail(f"R6 migration missing {token}")
if "COALESCE(a.ended_at, a.started_at, si.created_at) DESC" not in v6:
    fail("latest-result view is not temporally grounded")

arch=list(csv.DictReader((ROOT/"architecture/g2/module-profile-registry-v0.1.csv").open(encoding="utf-8",newline="")))
data=next(r for r in arch if r["module_id"]=="MOD-DATA")
if data["type"]!="application_projection" or "cannot determine Core ontology semantics" not in data["forbidden_dependency_direction"]:
    fail("DataProjection semantic-authority boundary drifted")

man=(ROOT/"publications/2026-icae/manuscript-working-draft-v0.1.md").read_text(encoding="utf-8").lower()
for forbidden in ("lossless global ontology-to-database equivalence","database is the semantic source of truth"):
    if forbidden in man:
        fail(f"unsafe manuscript wording detected: {forbidden}")

print("PASS: parity denominator is 8 predeclared tasks covering 17 CQs directly")
print("PASS: no identity-erasing normalization remains in the P49 expected contract")
print("PASS: forbidden primitive owner/status/score shortcuts are absent from core.risk")
print("PASS: latest-result semantics are time-grounded and DataProjection remains non-authoritative")
print("SEM_RISK_R6_RELATIONAL_GOVERNANCE_PASS")
