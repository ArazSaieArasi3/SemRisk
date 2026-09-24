# W4 #29 Acceptance Audit — E1–E4 Evaluation

**Date:** 2026-09-24  
**Result:** PASS_WITH_BOUNDED_FORMAL_SCOPE / CLOSED

All declared E1–E4 checks are exact-version bound and separately recorded by layer. Latest governed Semantic CI run `35990633287` passed on commit `dc8147968adbe7cf39cee930a662814b6fc30128`.

### E1
RDF parsing, OWL 2 DL profile and candidate/tool/version binding: PASS.

### E2
HermiT consistency/classification, explicit named-class satisfiability, expected entailments/non-entailment, SHACL positive/negative behavior and owner derivation rule: PASS for declared checks.

### E3
71/71 release-critical IDs present; identity uniqueness, mapping/test/dependency integrity and checksum inventory checks: PASS.

### E4
#25 foundational baseline remains PASS: 33/33 release-critical concepts, 38/38 relations, 7/7 HIGH foundational conditions; anti-pattern/alternative records preserved.

### Detector sensitivity
#50 negative controls demonstrate representative failures are detectable; the evaluation is not merely a green run on the canonical ontology.

### Boundary
Formal/foundational PASS is **not** semantic/domain validation. #30/#51 remain required for human semantic validation, and #31 remains required for higher-level application/comparative/transferability claims.
