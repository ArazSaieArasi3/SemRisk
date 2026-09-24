# W4 #50 Acceptance Audit — Negative Controls and Semantic Mutation Tests

**Date:** 2026-09-24  
**Result:** PASS_WITH_DECLARED_COVERAGE / CLOSED

## Executed evidence

### Semantic CI
Successful run: `35955902962` (commit `4a3c7e8211ebea4c76cfa165170dcb19491957f5`)

Verified detector families:
- malformed RDF/Turtle parser failure;
- SHACL negative fixtures: entry/risk trace, duplicate current workflow state, missing responsibility assignee, missing assessment trace, wrong Pharma target;
- semantic-equivalence mutations for Risk Register Entry/Risk, Workflow State/Risk State and unsupported assessment-result/Risk equivalence;
- HermiT inconsistency negative fixture;
- expected-entailment removal;
- unresolved import/catalog reference.

### Cross-layer relational/application CI
Successful run: `35990074932` (commit `74ff26d3ef9094bfc8e99a144cc25f248bd97597`)

Verified:
- `NC-RDB-001`: stale ontology↔RDB target detected;
- `NC-CQ-001`: expected-answer mismatch detected;
- `NC-SCEN-001`: missing reassessment supersession detected;
- `NC-STATE-001`: Workflow State/Risk State type conflation detected.

Marker: `SEM_RISK_ISSUE_50_CROSSLAYER_NEGATIVE_CONTROLS_PASS`.

## Coverage statement
The governed manifest contains representative positive/negative controls across syntax, SHACL/profile constraints, reasoning/inconsistency, entailment regression, semantic conflation, dependency binding, ontology↔RDB mapping, CQ expectation, scenario temporal semantics and state-family separation.

This is **declared representative coverage**, not exhaustive defect-space coverage. No claim is made that every possible ontology, SHACL, reasoning, mapping or implementation defect is detectable.

## False-positive / false-negative status
No false-positive or false-negative was observed in the currently declared fixture set. This does not estimate an external error rate because the fixture corpus is deliberately constructed and bounded.

## Acceptance conclusion
#50 demonstrates detector sensitivity beyond merely passing the current SemRisk candidate. Mutation/test artifacts remain isolated from domain evidence and canonical ontology sources.
