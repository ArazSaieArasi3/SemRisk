# W4 #52 Acceptance Audit — Competency-Question Regression

**Date:** 2026-09-24  
**Result:** PASS_WITH_MIXED_EXECUTABILITY / CLOSED  
**Validated relational/RDF regression run:** `35990496034`

## Canonical denominator
The original #7 registry contains **40/40 retained CQs**. No CQ was removed, renamed or rewritten after execution to improve coverage.

Paper-1 applicability:
- applicable: **39**
- explicitly deferred: **1 (CQ-039)**

Execution-state distribution:
- executable: **26**
- partially executable: **7**
- conceptual-only: **6**
- deferred: **1**
- failed: **0**

For the applicable denominator (39):
- executable: **66.7%**
- partially executable: **17.9%**
- conceptual-only: **15.4%**

These percentages describe **executability**, not ontology correctness or domain validity.

## Execution evidence
The regression package reuses predeclared expected-answer evidence rather than inventing post-hoc CQs:
- 10 end-to-end expected-answer families from #48;
- 8 SQL↔SPARQL parity tasks from #49;
- semantic/negative controls from #50;
- source/mapping/provenance evidence from #47/#68.

CI gate output:
- `40/40 original CQs retained and dispositioned`
- `applicable denominator=39; executable=26; partial=7; conceptual_only=6; deferred=1; failed=0`
- `SEM_RISK_ISSUE_52_CQ_REGRESSION_GOVERNANCE_PASS`

## Material partials retained
CQ-006, CQ-012, CQ-013, CQ-028, CQ-035, CQ-037 and CQ-038 remain partially executable for declared reasons. They were not promoted to PASS-executable by adding artificial fixtures after result inspection.

## Conceptual-only items retained
CQ-002, CQ-004, CQ-017, CQ-019, CQ-030 and CQ-032 remain conceptual-only. Their expected capabilities are governed and semantically reviewed, but the specific multiplicity/method/profile fixtures required for executable evidence are not present.

## Boundary
This gate establishes CQ preservation, semantic review, bounded answerability and executable regression for the declared subset. It does not replace expert semantic validation (#51/#30), comparative/transferability evaluation (#31), or claim calibration (#53).
