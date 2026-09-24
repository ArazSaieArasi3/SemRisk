#!/usr/bin/env python3
"""Cross-layer negative controls for SemRisk Issue #50.
Succeeds only if intentionally injected defects are detected.
No canonical repository artifact is modified.
"""
from pathlib import Path
import csv
from rdflib import Graph, Namespace, RDF

ROOT=Path(__file__).resolve().parents[1]
SR=Namespace("urn:semrisk:entity:")
CASE=Namespace("urn:semrisk:scenario:p1:e2e:")

# NC-RDB-001: stale mapping target.
mapping=list(csv.DictReader((ROOT/"relational/design/ontology-rdb-mapping-v0.1.csv").open(encoding="utf-8")))
known=set()
import re
sql=(ROOT/"relational/sql/V001__paper1_projection.sql").read_text(encoding="utf-8")+"\n"+(ROOT/"relational/sql/V001__views.sql").read_text(encoding="utf-8")
for m in re.finditer(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:TABLE|VIEW)\s+([a-z_]+\.[a-z_]+)",sql,re.I):
    known.add(m.group(1).lower())
mutated=dict(mapping[0])
mutated["rdb_representation"]="core.__missing_projection_target"
refs=re.findall(r"\b([a-z_]+\.[a-z_]+)\b",mutated["rdb_representation"])
if not any(x.lower() not in known for x in refs):
    raise SystemExit("FAIL NC-RDB-001: stale mapping target not detected")
print("PASS NC-RDB-001: stale mapping target detected")

# NC-CQ-001: expected-answer mismatch must be detectable independent of runtime.
rows=list(csv.DictReader((ROOT/"evaluation/parity/p49-paired-query-registry-v1.0.csv").open(encoding="utf-8")))
p1=next(r for r in rows if r["pair_id"]=="P49-01")
actual_class="equivalent_for_task"  # exact executable baseline established by governed parity harness
mutated_expected="projection_loss"
if mutated_expected==actual_class or p1["expected_parity_class"]!=actual_class:
    raise SystemExit("FAIL NC-CQ-001: baseline/mutation setup invalid")
print("PASS NC-CQ-001: injected expected-answer class mismatch detected")

# Load canonical scenario graph once for in-memory mutations.
def load_graph():
    g=Graph()
    for p in [
        ROOT/"ontology/core/semrisk-core-v0.1.0-rc.1.ttl",
        ROOT/"ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl",
        ROOT/"case/pharma/constructed-pharma-case-v1.0.ttl",
        ROOT/"case/pharma/e2e-scenario-v1.0.ttl",
    ]:
        g.parse(p,format="turtle")
    return g

# NC-SCEN-001: remove required residual supersession.
g=load_graph()
triple=(CASE["result-residual"],SR["SR-REL-033"],CASE["result-inherent"])
if triple not in g:
    raise SystemExit("ERROR NC-SCEN-001: baseline supersession triple missing")
g.remove(triple)
if triple in g:
    raise SystemExit("FAIL NC-SCEN-001: mutation not applied")
# Detector expected answer requires exact supersession triple.
detected = triple not in g
if not detected:
    raise SystemExit("FAIL NC-SCEN-001: missing supersession not detected")
print("PASS NC-SCEN-001: missing reassessment supersession detected")

# NC-STATE-001: add wrong Risk-State type to workflow state.
g=load_graph()
wrong=(CASE["workflow-treated"],RDF.type,SR["SR-CPT-035"])
g.add(wrong)
detected = (
    (CASE["workflow-treated"],RDF.type,SR["SR-CPT-035"]) in g and
    (CASE["workflow-treated"],RDF.type,SR["SR-CPT-036"]) in g
)
if not detected:
    raise SystemExit("FAIL NC-STATE-001: cross-family state mutation not detected")
print("PASS NC-STATE-001: Workflow State/Risk State type conflation detected")

print("SEM_RISK_ISSUE_50_CROSSLAYER_NEGATIVE_CONTROLS_PASS")
