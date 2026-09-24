#!/usr/bin/env python3
"""R2 formal-semantics regression guardrails.

These checks prevent specific OWL modeling regressions identified in the
specialist-style simulated R2 review. They are not independent expert
validation and do not establish domain correctness.
"""
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, OWL

ROOT=Path(__file__).resolve().parents[1]
SR="urn:semrisk:entity:"

g=Graph()
for p in sorted((ROOT/"ontology").glob("*/*.ttl")):
    g.parse(p,format="turtle")

concerns=URIRef(SR+"SR-REL-001")
entry=URIRef(SR+"SR-CPT-033")
risk=URIRef(SR+"SR-CPT-001")
result=URIRef(SR+"SR-CPT-013")

def fail(m):
    raise SystemExit("FAIL R2 guardrail: "+m)

# #73: global domain would infer every concernsRisk subject to Risk Register Entry.
if any(True for _ in g.objects(concerns,RDFS.domain)):
    fail("SR-REL-001 concernsRisk has a global rdfs:domain; validation must remain profile/SHACL scoped")
if (concerns,RDFS.range,risk) not in g:
    fail("SR-REL-001 no longer has the justified Risk range")

# #74: claim-critical phenomenon vs assessment-result artifact distinction.
if (risk,OWL.disjointWith,result) not in g and (result,OWL.disjointWith,risk) not in g:
    fail("Risk and Risk Assessment Result are not explicitly owl:disjointWith")

print("PASS: concernsRisk has no global OWL domain and retains Risk range")
print("PASS: Risk is explicitly disjoint with Risk Assessment Result")
print("SEM_RISK_R2_FORMAL_GUARDRAILS_PASS")
