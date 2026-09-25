# R4 Risk Standards & Frameworks Review Remediation Acceptance Audit — 2026-09-25

**Issues:** #85, #86, #87, #88, #89, #90  
**Origin:** specialist-style simulated Risk Standards & Frameworks review (R4), used as an adversarial review aid. This is **not independent human expert validation**.

## Decision
**PASS / CLOSED for the six R4 remediations.**

R4 strengthens version lineage, mapping discipline and manuscript claim ceilings. It does not close the broader #13 clause/page/section extraction work.

## #85 — version/status lineage
Implemented:
- `evaluation/standards/paper1-standards-version-status-register-v1.0.csv`
- current published vs under-development states are explicit;
- ISO 31000:2018 is bound as current published and ISO/CD 31000 Edition 3 is tracked separately;
- ISO 31073:2022, IEC 31010:2019 Ed.2, COSO ERM 2017, OCEG 3.5, Risk IT 2nd Edition, ICH Q9(R1) and current NIST editions are explicitly bound.

## #86 — controlled mapping strength
Implemented:
- `evaluation/standards/standard-mapping-strength-policy-v1.0.md`
- allowed values: EXACT, CLOSE, BROADER, NARROWER, RELATED, OPERATIONALIZES, PROFILE_SUPPORT, COVERAGE_BENCHMARK;
- current crosswalk normalized to controlled values;
- no current Paper-1 row asserts EXACT;
- lexical match does not authorize OWL equivalence.

## #87 — NIST IR 8286 calibration
Implemented:
- NIST status changed from blanket `covered` to `SUPPORTED_BOUNDED`;
- current NIST register/RDR/schema evidence remains authoritative operational evidence;
- NIST Status→SemRisk Workflow State is explicitly source/profile mapping rather than exact ontology identity;
- no NIST field is automatically promoted to an ontology class.

## #88 — ICH Q9(R1) boundary
Implemented:
- current EMA Step 5 Revision 2 / Corr.2 and 2023-07-26 effective date bound;
- bounded Pharma alignment covers assessment, treatment/control/review and product-availability context;
- Hazard/Harm are explicitly recognized but remain deferred SemRisk profile concepts;
- no ICH compliance/conformance claim is authorized.

## #89 — governance terminology boundaries
Implemented:
- `evaluation/standards/governance-term-boundary-v1.0.md`
- Appetite ≠ Tolerance;
- Tolerance ≠ Threshold by default;
- Indicator/KRI ≠ Threshold;
- Risk Criteria ≠ Appetite;
- framework/method evidence is required before stronger mappings.

## #90 — standards evidence-coverage gate
Implemented:
- `evaluation/standards/standards-evidence-coverage-v1.0.csv`
- access class, locator depth, clause/section completeness and Paper-1 claim ceiling are explicit;
- `tools/r4_standards_governance_check.py` added;
- Semantic CI path coverage extended to standards/crosswalk/manuscript guard inputs;
- manuscript and prohibited-wording register calibrated.

## Validation
Initial run **36116665638** failed before creating any job because the workflow path list contained literal `\n` strings. This was a CI YAML syntax defect, not an ontology/evidence failure. It was corrected explicitly.

Final Semantic CI run **36116720075**: **SUCCESS**.

R4 guard passed:
- standards/framework versions and current/draft lineage frozen;
- crosswalk controlled non-equivalence mapping strengths;
- NIST bounded operational/profile evidence;
- ICH Q9(R1) excludes deferred Hazard/Harm coverage;
- access/locator limitations constrain claim ceilings;
- governance-term boundaries remain framework/method sensitive;
- marker: `SEM_RISK_R4_STANDARDS_GOVERNANCE_PASS`.

The same run also passed OWL 2 DL profile validation, HermiT consistency/classification, expected entailments and existing negative controls.

## #13 residual state
Issue #13 remains **OPEN**. Its remaining debt is clause/page/section and detailed extraction completeness, especially for access-limited ISO/IEC/COSO/OCEG/Risk IT/EA sources. R4 removes version ambiguity and uncontrolled claim strength; it does not fabricate inaccessible clause evidence.

## Claim boundary
SemRisk may make bounded terminology/process/profile/operational-alignment statements supported by the exact source/evidence register. It may not claim standards conformance, complete framework coverage, or semantic equivalence solely from terminology overlap.
