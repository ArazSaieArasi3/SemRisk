#!/usr/bin/env python3
"""R7 Pharma/Health domain governance guard.

This guard operationalizes findings from the specialist-style simulated
Pharmaceutical / Health Risk Domain review. It is not independent human
expert validation and does not establish Pharma-wide validity.
"""
from pathlib import Path
import csv
from rdflib import Graph, Namespace, RDF, URIRef
from rdflib.namespace import PROV

ROOT=Path(__file__).resolve().parents[1]
SR=Namespace("urn:semrisk:entity:")
CASE=Namespace("urn:semrisk:scenario:p1:e2e:")
BASE=Namespace("urn:semrisk:case:pharma:v1:")

def fail(msg):
    raise SystemExit("FAIL R7 Pharma governance: "+msg)

# Constructed case v1.1 must remain non-occurrence evidence.
cg=Graph()
cg.parse(ROOT/"case/pharma/constructed-pharma-case-v1.1.ttl",format="turtle")
for typ in ("SR-CPT-005","SR-CPT-007","SR-CPT-008"):
    hits=list(cg.subjects(RDF.type,SR[typ]))
    if hits:
        fail(f"constructed DS-003 case contains occurrence/consequence type {typ}: {hits}")

if (BASE["pooled-procurement-strategy"],RDF.type,SR["SR-CPT-026"]) not in cg:
    fail("pooled procurement lost proposed Risk Treatment Strategy typing")
if (BASE["transparency-response-candidate"],RDF.type,SR["SR-CPT-026"]) in cg:
    fail("transparency response candidate is still overtyped as Risk Treatment Strategy")

# E2E synthetic execution must be explicitly generated.
eg=Graph()
eg.parse(ROOT/"case/pharma/e2e-scenario-v1.1.ttl",format="turtle")
synthetic_nodes=[
    CASE.trigger, CASE.event, CASE.consequence, CASE.register, CASE.entry,
    CASE["scenario-description"], CASE.responsibility, CASE.actor,
    CASE.plan, CASE["treatment-activity"], CASE.control,
    CASE["assessment-pre"], CASE["result-inherent"],
    CASE["assessment-post"], CASE["result-residual"],
    CASE["risk-state-pre"], CASE["risk-state-post"],
    CASE["workflow-open"], CASE["workflow-treated"],
]
for node in synthetic_nodes:
    if (node,PROV.wasGeneratedBy,CASE["synthetic-generation"]) not in eg:
        fail(f"synthetic E2E node lacks synthetic-generation provenance: {node}")

# DS-004 must remain fully blocked for file-level robustness.
ds4=list(csv.DictReader((ROOT/"datasets/ds004-activation-gate-v1.0.csv").open(encoding="utf-8",newline="")))
if len(ds4)!=8 or any(r["current_state"]!="BLOCKED" for r in ds4):
    fail("DS-004 activation gate is not fully BLOCKED")

# Pharma identity gaps must remain external/profile, not Core leakage.
gaps=list(csv.DictReader((ROOT/"case/pharma/pharma-external-identity-gap-v1.0.csv").open(encoding="utf-8",newline="")))
required={"Active pharmaceutical ingredient / INN","Medicinal/drug product identity",
          "Manufacturer / marketing-authorisation-holder identity","Jurisdiction / geography",
          "ATC / therapeutic class","Administration route","Shortage record / registry record",
          "Criticality / essentiality classification"}
present={r["domain_anchor"] for r in gaps}
if not required.issubset(present):
    fail(f"missing Pharma external identity gaps: {sorted(required-present)}")
for r in gaps:
    if r["domain_anchor"] in required and "Core" in r["semrisk_disposition"]:
        fail(f"Pharma-specific anchor leaked toward Core: {r['domain_anchor']}")

# Coverage matrix must keep known omitted stress dimensions visible.
cov=list(csv.DictReader((ROOT/"case/pharma/pharma-case-coverage-nonclaim-matrix-v1.0.csv").open(encoding="utf-8",newline="")))
by={r["semantic_area"]:r["paper1_case_state"] for r in cov}
for term in ("Risk Source","Vulnerability","Exposure","Indicator / Threshold"):
    if by.get(term)!="NOT_EXERCISED":
        fail(f"{term} must remain explicit NOT_EXERCISED in current Pharma case")
if by.get("Assessment Method")!="NOT_POPULATED":
    fail("Assessment Method must remain NOT_POPULATED in current Pharma case")
if by.get("Control effectiveness / assurance")!="NOT_DEMONSTRATED":
    fail("Control effectiveness / assurance must remain explicit NOT_DEMONSTRATED")

# DS-002 role must be cross-domain stress, never direct shortage validation.
stress=(ROOT/"evaluation/e11/ds002-cross-domain-pharma-stress-contract-v1.0.md").read_text(encoding="utf-8").lower()
for phrase in ("not a drug-shortage dataset","cross-domain pharmaceutical stress candidate",
               "must not be described as direct validation of antibiotic-shortage semantics"):
    if phrase not in stress:
        fail(f"DS-002 cross-domain boundary missing: {phrase}")

# Manuscript must preserve bounded Pharma claims.
man=(ROOT/"publications/2026-icae/manuscript-working-draft-v0.1.md").read_text(encoding="utf-8").lower()
required_man=[
    "bounded pharma case",
    "ds-004 remains blocked",
    "cross-domain pharma stress candidate",
    "does not support prevalence",
]
for phrase in required_man:
    if phrase not in man:
        fail(f"R7 manuscript boundary missing: {phrase}")

print("PASS: constructed Pharma case contains no fabricated Trigger/RiskEvent/Consequence")
print("PASS: all E2E synthetic execution nodes carry synthetic-generation provenance")
print("PASS: pooled procurement remains proposed strategy; transparency remains context-typed response candidate")
print("PASS: DS-004 file-level robustness gate remains fully blocked")
print("PASS: DS-002 is protected for cross-domain Pharma stress, not shortage validation")
print("PASS: Pharma-specific identity gaps remain external/profile scoped")
print("SEM_RISK_R7_PHARMA_GOVERNANCE_PASS")
