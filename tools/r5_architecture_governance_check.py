#!/usr/bin/env python3
"""R5 Enterprise/Business Architecture federation governance guard.

This guard enforces external ownership, dependency direction and bounded EA
claims identified by the specialist-style simulated R5 review. It is not
independent human expert validation and does not establish TOGAF/ArchiMate
conformance.
"""
from pathlib import Path
import csv
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, SKOS

ROOT=Path(__file__).resolve().parents[1]
SR="urn:semrisk:entity:"

def fail(msg):
    raise SystemExit("FAIL R5 architecture guard: "+msg)

g=Graph()
g.parse(ROOT/"ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl",format="turtle")
for sid in ("SR-CPT-037","SR-CPT-038","SR-CPT-039"):
    s=URIRef(SR+sid)
    if (s,RDF.type,OWL.Class) in g:
        fail(f"{sid} became a local owl:Class")
    if (s,RDF.type,SKOS.Concept) not in g:
        fail(f"{sid} is no longer a governed external-owner SKOS marker")

with (ROOT/"evaluation/architecture/external-enterprise-ownership-state-v1.0.csv").open(encoding="utf-8",newline="") as f:
    own={r["semantic_id"]:r for r in csv.DictReader(f)}
for sid in ("SR-CPT-037","SR-CPT-038","SR-CPT-039"):
    if own[sid]["paper1_binding_state"]!="UNBOUND_EXTERNAL_FAMILY":
        fail(f"{sid} generic owner was prematurely resolved")
if own["SR-CPT-038"]["profile_owner"] and "CM-PharmE v1.0.0" not in own["SR-CPT-038"]["profile_owner"]:
    fail("Capability profile ownership lost exact CM-PharmE version")
if own["SR-CPT-039"]["profile_owner"] and "CM-PharmE v1.0.0" not in own["SR-CPT-039"]["profile_owner"]:
    fail("Business Process profile ownership lost exact CM-PharmE version")

with (ROOT/"architecture/g2/module-profile-registry-v0.1.csv").open(encoding="utf-8",newline="") as f:
    mods={r["module_id"]:r for r in csv.DictReader(f)}
if mods["MOD-DATA"]["type"]!="application_projection":
    fail("DataProjection is no longer an application projection")
if "cannot determine Core ontology semantics" not in mods["MOD-DATA"]["forbidden_dependency_direction"]:
    fail("DataProjection reverse-dependency prohibition is missing")
if "Core must not depend on Enterprise" not in mods["MOD-ENT"]["forbidden_dependency_direction"]:
    fail("Core→Enterprise reverse dependency guard missing")
if "Core must not depend on Pharma" not in mods["MOD-PHARMA"]["forbidden_dependency_direction"]:
    fail("Core→Pharma reverse dependency guard missing")

core=Graph()
core.parse(ROOT/"ontology/core/semrisk-core-v0.1.0-rc.1.ttl",format="turtle")
bad_imports=[]
for o in core.objects(None,OWL.imports):
    v=str(o).lower()
    if any(x in v for x in ("enterprise","pharma","mappings","data")):
        bad_imports.append(str(o))
if bad_imports:
    fail(f"Core imports downstream modules: {bad_imports}")

sql=(ROOT/"relational/sql/V001__paper1_projection.sql").read_text(encoding="utf-8")
if "Semantic authority remains the SemRisk ontology" not in sql:
    fail("RDB projection no longer declares ontology semantic authority")

with (ROOT/"evaluation/standards/paper1-standards-version-status-register-v1.0.csv").open(encoding="utf-8",newline="") as f:
    std={r["standard_id"]:r for r in csv.DictReader(f)}
r=std["STD-011"]
if r["current_status"]!="CURRENT_REFERENCE_BOUND" or "ArchiMate Specification 3.2" not in r["publication_version"] or "TOGAF Standard 10th Edition" not in r["publication_version"]:
    fail("TOGAF/ArchiMate current reference binding is incomplete")

with (ROOT/"evaluation/architecture/ea-capability-nonclaim-matrix-v1.0.csv").open(encoding="utf-8",newline="") as f:
    caps={r["ea_capability_id"]:r for r in csv.DictReader(f)}
for cid in ("EA-005","EA-006","EA-007","EA-008","EA-009","EA-010","EA-011"):
    if caps[cid]["paper1_state"]!="NOT_DEMONSTRATED":
        fail(f"{cid} must remain NOT_DEMONSTRATED")

v5=(ROOT/"relational/sql/V005__r5_architecture_federation.sql").read_text(encoding="utf-8")
for token in ("ref.external_entity_mapping","enterprise.architecture_context_link","anticipated","realized","SR-REL-010"):
    if token not in v5:
        fail(f"R5 projection extension missing {token}")

print("PASS: Objective/Capability/Business Process remain external reference concepts")
print("PASS: generic EA owner remains intentionally unbound; profile ownership is version-bound")
print("PASS: Core/profile/DataProjection dependency direction is preserved")
print("PASS: TOGAF 10 / ArchiMate 3.2 are bounded reference sources, not semantic owners")
print("PASS: advanced EA capabilities remain explicit Paper-1 nonclaims")
print("SEM_RISK_R5_ARCHITECTURE_GOVERNANCE_PASS")
