#!/usr/bin/env python3
"""R4 standards/framework evidence-governance checks.

This guard enforces version/status lineage, controlled mapping strengths and
manuscript claim ceilings identified by the specialist-style simulated R4
standards/framework review. It is not evidence of independent human validation
or standards conformance.
"""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]

def read_csv(path):
    with (ROOT/path).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def fail(msg):
    raise SystemExit("FAIL R4 standards guard: "+msg)

versions={r["standard_id"]:r for r in read_csv("evaluation/standards/paper1-standards-version-status-register-v1.0.csv")}
required=set(f"STD-{i:03d}" for i in range(1,12))
if set(versions)!=required:
    fail(f"version/status register IDs mismatch: {sorted(set(versions)^required)}")

if "2018 Edition 2" not in versions["STD-001"]["publication_version"] or "ISO/CD 31000" not in versions["STD-001"]["under_development_successor"]:
    fail("ISO 31000 current-vs-draft lineage is not frozen")
if "3.5" not in versions["STD-006"]["publication_version"]:
    fail("OCEG GRC Capability Model 3.5 is not version-bound")
if "2nd Edition" not in versions["STD-007"]["publication_version"]:
    fail("Risk IT Framework 2nd Edition is not version-bound")
if "Revision 2" not in versions["STD-008"]["publication_version"] or "2023-07-26" not in versions["STD-008"]["publication_version"]:
    fail("ICH Q9(R1) current Revision 2/effective-date binding is incomplete")

cross=read_csv("conceptualization/comparison/standard-framework-crosswalk-v0.1.csv")
allowed={"EXACT","CLOSE","BROADER","NARROWER","RELATED","OPERATIONALIZES","PROFILE_SUPPORT","COVERAGE_BENCHMARK"}
for row in cross:
    toks={x.strip() for x in row["mapping_relation"].split(";") if x.strip()}
    if not toks or not toks.issubset(allowed):
        fail(f"{row['crosswalk_id']} has uncontrolled mapping relation {row['mapping_relation']}")
    if "EXACT" in toks:
        fail(f"{row['crosswalk_id']} asserts EXACT without a dedicated inspected-definition assertion register")

byid={r["crosswalk_id"]:r for r in cross}
if byid["STD-004"]["status"]!="SUPPORTED_BOUNDED":
    fail("NIST row must remain SUPPORTED_BOUNDED, not blanket covered")
if "Workflow State" in byid["STD-004"]["semrisk_constructs"] and "profile" not in byid["STD-004"]["semrisk_constructs"].lower():
    fail("NIST Status/Workflow mapping is not explicitly profile-scoped")
if "Hazard" in byid["STD-008"]["semrisk_constructs"] or "Harm" in byid["STD-008"]["semrisk_constructs"]:
    fail("ICH row incorrectly claims Paper-1 Hazard/Harm construct coverage")
if "deferred" not in byid["STD-008"]["limitation_nonclaim"].lower():
    fail("ICH row does not explicitly retain Hazard/Harm deferral")

coverage=read_csv("evaluation/standards/standards-evidence-coverage-v1.0.csv")
for row in coverage:
    if row["clause_or_section_completeness"] in {"INCOMPLETE","PARTIAL","PARTIAL_STRONG"}:
        ceiling=row["paper1_claim_ceiling"].lower()
        for forbidden in ("conformant","compliant","fully aligned","complete alignment"):
            if forbidden in ceiling:
                fail(f"{row['standard_id']} claim ceiling is too strong: {row['paper1_claim_ceiling']}")

boundary=(ROOT/"evaluation/standards/governance-term-boundary-v1.0.md").read_text(encoding="utf-8")
for phrase in ["Appetite ≠ Tolerance","Tolerance ≠ Threshold","Indicator/KRI ≠ Threshold","Risk Criteria ≠ Risk Appetite"]:
    if phrase not in boundary:
        fail(f"governance-term non-equivalence missing: {phrase}")

man=(ROOT/"publications/2026-icae/manuscript-working-draft-v0.1.md").read_text(encoding="utf-8")
if "five task-equivalent results" in man:
    fail("stale pre-R2 parity count remains in manuscript")
for required_phrase in [
    "ISO 31000:2018 remains the current published edition",
    "NIST register fields are treated as operational/profile evidence rather than ontology identities",
    "Hazard/Harm semantics are not claimed as Paper-1 Core coverage",
]:
    if required_phrase not in man:
        fail(f"required R4 bounded manuscript statement missing: {required_phrase}")

print("PASS: standards/framework versions and current/draft lineage are frozen")
print("PASS: crosswalk uses controlled non-equivalence mapping strengths")
print("PASS: NIST alignment remains bounded operational/profile evidence")
print("PASS: ICH Q9(R1) alignment excludes deferred Hazard/Harm coverage")
print("PASS: access/locator limitations constrain manuscript claim ceilings")
print("PASS: governance-term boundaries remain framework/method sensitive")
print("SEM_RISK_R4_STANDARDS_GOVERNANCE_PASS")
