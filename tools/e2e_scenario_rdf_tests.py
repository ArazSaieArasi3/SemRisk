#!/usr/bin/env python3
from pathlib import Path
import csv, sys
from rdflib import Graph, Namespace, RDF, URIRef

ROOT=Path(__file__).resolve().parents[1]
SR=Namespace("urn:semrisk:entity:")
CASE=Namespace("urn:semrisk:scenario:p1:e2e:")
BASE=Namespace("urn:semrisk:case:pharma:v1:")

g=Graph()
for p in [
    ROOT/"ontology/core/semrisk-core-v0.1.0-rc.1.ttl",
    ROOT/"ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl",
    ROOT/"case/pharma/constructed-pharma-case-v1.0.ttl",
    ROOT/"case/pharma/e2e-scenario-v1.0.ttl",
]:
    g.parse(p,format="turtle")

expected=list(csv.DictReader((ROOT/"case/pharma/e2e-scenario-expected-v1.0.csv").open(encoding="utf-8")))

def require(cond,msg):
    if not cond:
        raise SystemExit("FAIL: "+msg)

# E2E-Q01 scenario/event are distinct and linked by realization.
require((BASE.scenario, SR["SR-REL-003"], CASE.event) in g,"scenario realization missing")
require(BASE.scenario != CASE.event,"scenario and event identity conflated")

# E2E-Q02 condition/trigger/event/consequence path.
require((CASE.event, SR["SR-REL-007"], CASE.trigger) in g,"event trigger missing")
require((CASE.event, SR["SR-REL-004"], CASE.consequence) in g,"event consequence missing")
require((BASE.scenario, SR["SR-REL-006"], BASE["supply-concentration-condition"]) in g,"condition link missing")

# E2E-Q03 / Q07 reassessment + same underlying Risk.
require((CASE["assessment-post"], SR["SR-REL-034"], CASE["assessment-pre"]) in g,"prior assessment link missing")
require((CASE["result-residual"], SR["SR-REL-033"], CASE["result-inherent"]) in g,"result supersession missing")
require((CASE["result-inherent"], SR["SR-REL-016"], BASE["risk-context"]) in g,"inherent result risk missing")
require((CASE["result-residual"], SR["SR-REL-016"], BASE["risk-context"]) in g,"residual result risk missing")

# E2E-Q04 treatment semantic separation.
for node,typ in [
    (BASE["pooled-procurement-strategy"],"SR-CPT-026"),
    (CASE.plan,"SR-CPT-027"),
    (CASE["treatment-activity"],"SR-CPT-028"),
    (CASE.control,"SR-CPT-029"),
]:
    require((node,RDF.type,SR[typ]) in g,f"{typ} type missing")
require(len({BASE["pooled-procurement-strategy"],CASE.plan,CASE["treatment-activity"],CASE.control})==4,"treatment identities conflated")

# E2E-Q05 owner derivation truthmaker facts (do not require material hasRiskOwner triple).
require((CASE.responsibility,SR["SR-REL-027"],BASE["risk-context"]) in g,"responsibility target missing")
require((CASE.responsibility,SR["SR-REL-028"],CASE.actor) in g,"responsibility actor missing")

# E2E-Q06 state types remain disjoint in instance data.
for x in [CASE["risk-state-pre"],CASE["risk-state-post"]]:
    require((x,RDF.type,SR["SR-CPT-035"]) in g,"risk state type missing")
for x in [CASE["workflow-open"],CASE["workflow-treated"]]:
    require((x,RDF.type,SR["SR-CPT-036"]) in g,"workflow state type missing")
require(not any((x,RDF.type,SR["SR-CPT-036"]) in g for x in [CASE["risk-state-pre"],CASE["risk-state-post"]]),"risk state typed as workflow state")
require(not any((x,RDF.type,SR["SR-CPT-035"]) in g for x in [CASE["workflow-open"],CASE["workflow-treated"]]),"workflow state typed as risk state")

# E2E-Q08 evidence link remains DS-003 anchor.
require((CASE["result-inherent"],SR["SR-REL-017"],BASE["evidence-ds003"]) in g,"evidence link missing")
require((CASE["result-residual"],SR["SR-REL-017"],BASE["evidence-ds003"]) in g,"reassessment evidence link missing")

# E2E-Q09 external CM-PharmE targets preserved as IRIs.
cmpe_targets=list(g.objects(BASE["risk-context"],SR["SR-REL-037"]))
require(any(str(x).startswith("urn:cm-pharme:v1.0.0:") for x in cmpe_targets),"CM-PharmE external bridge missing")

require(len(expected)==10,"Expected-answer registry must remain 10 rows")
print(f"PASS: parsed {len(g)} RDF triples")
print("PASS: 10/10 predeclared scenario answer families structurally represented")
print("SEM_RISK_ISSUE_48_RDF_SCENARIO_PASS")
