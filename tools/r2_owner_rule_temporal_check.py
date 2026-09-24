#!/usr/bin/env python3
from pathlib import Path
from rdflib import Graph, URIRef

ROOT=Path(__file__).resolve().parents[1]

g=Graph()
for p in [
    ROOT/"testdata/p1-r2-positive-smoke-v0.1.ttl",
    ROOT/"testdata/negative/rule-historical-owner.ttl",
]:
    g.parse(p,format="turtle")

q=(ROOT/"rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq").read_text(encoding="utf-8")
constructed=g.query(q)
out=Graph()
for t in constructed:
    out.add(t)

risk=URIRef("urn:semrisk:test:risk-001")
pred=URIRef("urn:semrisk:entity:SR-REL-026")
active=URIRef("urn:semrisk:test:actor-001")
old=URIRef("urn:semrisk:test:actor-old")

if (risk,pred,active) not in out:
    raise SystemExit("FAIL: active/uninvalidated responsibility did not derive owner")
if (risk,pred,old) in out:
    raise SystemExit("FAIL: invalidated historical responsibility leaked into derived owner")
if len(list(out.triples((risk,pred,None)))) != 1:
    raise SystemExit("FAIL: expected exactly one derived owner for governed fixture")

print("PASS: active responsibility derives owner")
print("PASS: explicitly invalidated historical responsibility does not derive owner")
print("SEM_RISK_R2_OWNER_TEMPORAL_RULE_PASS")
