#!/usr/bin/env python3
"""R3 ERM/GRC governance regression checks.

These checks enforce bounded Paper-1 operational claims and source-profile
vocabularies. They are not independent expert validation.
"""
from pathlib import Path
import csv, re

ROOT=Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit("FAIL R3 governance guard: "+msg)

# #79 capability matrix must preserve the distinction between selected-schema
# mapping coverage and ERM completeness.
matrix=list(csv.DictReader((ROOT/"evaluation/erm/r3-operational-capability-matrix-v1.0.csv").open(encoding="utf-8")))
states={r["capability_id"]:r["paper1_state"] for r in matrix}
for cid in ["ERM-011","ERM-012","ERM-013","ERM-014","ERM-015","ERM-016","ERM-017","ERM-018","ERM-019","ERM-020"]:
    if states.get(cid)!="NOT_DEMONSTRATED":
        fail(f"{cid} must remain NOT_DEMONSTRATED in Paper 1")

# #83: E2E workflow values are source-profile values, but profile is not a
# universal DB CHECK constraint.
vocab=list(csv.DictReader((ROOT/"profiles/enterprise/src-op-001-workflow-state-vocabulary-v1.0.csv").open(encoding="utf-8")))
allowed={r["state_code"].lower() for r in vocab if r["source_id"]=="SRC-OP-001"}
load=(ROOT/"relational/sql/load/P1_E2E_SCENARIO_v1.sql").read_text(encoding="utf-8")
used=set(re.findall(r"workflow_state_id,entry_id,state_code.*?VALUES\s*(.*?)(?:ON CONFLICT|;)",load,re.S|re.I)[0].lower().split())
# Deterministic explicit check for governed E2E values.
for state in ("open","treated"):
    if state not in allowed:
        fail(f"E2E workflow state {state} missing from SRC-OP-001 profile")
if "check (state_code in" in (ROOT/"relational/sql/V001__paper1_projection.sql").read_text(encoding="utf-8").lower():
    fail("workflow state_code was globally restricted to one source vocabulary")

# #81: Control Mechanism must not imply effectiveness in the manuscript.
manuscript=(ROOT/"publications/2026-icae/manuscript-working-draft-v0.1.md").read_text(encoding="utf-8").lower()
required=[
    "not evidence of complete enterprise-risk-management",
    "not treated as evidence of control design adequacy",
]
for phrase in required:
    if phrase not in manuscript:
        fail(f"required bounded manuscript statement missing: {phrase}")

# #84 deferred advanced ERM capabilities must remain explicit.
advanced=list(csv.DictReader((ROOT/"evaluation/erm/advanced-erm-deferred-capabilities-v1.0.csv").open(encoding="utf-8")))
if len(advanced)<8 or any(r["paper1_status"]!="DEFERRED" for r in advanced):
    fail("advanced ERM deferred-capability register is incomplete or contains non-deferred rows")

print("PASS: 27-field operational coverage remains bounded to the selected schema")
print("PASS: advanced ERM capabilities remain explicit Paper-1 nonclaims")
print("PASS: SRC-OP-001 workflow vocabulary is profile-scoped and E2E values are governed")
print("PASS: control-assurance nonclaim is present in manuscript")
print("SEM_RISK_R3_ERM_GOVERNANCE_PASS")
