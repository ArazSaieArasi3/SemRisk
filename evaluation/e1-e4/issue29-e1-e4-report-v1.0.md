# SemRisk E1–E4 Formal / Logical / Structural / Foundational Evaluation

**Issue:** #29  
**Candidate:** P1-R2 / 0.1.0-rc.1  
**Evaluated semantic commit:** `dc8147968adbe7cf39cee930a662814b6fc30128`  
**Semantic CI run:** `35990633287`  
**Foundational baseline:** #25 PASS (2026-09-23)

## Tool binding
- Python 3.13.15 in evaluated run
- RDFLib 7.6.0
- PySHACL 0.40.1
- ROBOT 1.9.10, pinned jar SHA-256 from semantic tool manifest
- HermiT bundled/invoked by ROBOT 1.9.10
- gUFO v1.0.0 pinned to governed dependency binding

## Results
All **21 declared E1–E4 evaluation records** in `issue29-e1-e4-results-v1.0.csv` are PASS for their bounded criteria.

Key automated observations:
- 14 governed Turtle inputs parse successfully.
- 71/71 release-critical semantic IDs are present.
- 2/2 deliberately fake trace IDs are detected as missing.
- canonical semantic IDs and IRIs are unique.
- 0 unapproved OWL equivalence mappings are present.
- positive SHACL fixture conforms; 5/5 known-negative SHACL fixtures fail as expected.
- HermiT consistency/classification succeeds for the governed closure.
- expected entailments are present.
- Risk Register Entry is not inferred equivalent to Risk.
- explicit satisfiability check reports **no named SemRisk class classified as owl:Nothing**.
- the governed `hasRiskOwner` rule derives the expected test triple.

E4 reuses the frozen #25 foundational audit:
- 33/33 release-critical concepts reviewed;
- 38/38 release-critical relations reviewed;
- 7/7 G2 HIGH foundational conditions resolved;
- 15 anti-pattern findings and 7 alternative categorizations retained.

## Negative-control sensitivity
#50 supplies representative detector evidence for malformed syntax, SHACL constraint failures, unsupported equivalence, missing entailment, logical inconsistency, unresolved dependency, stale RDB mapping and application-level semantic mutations. Therefore E1–E4 evidence is not based solely on the current candidate passing.

## Non-PASS findings
No Critical/High E1–E4 failure remains in the declared evaluated subset. Six medium/low foundational implementation/profile questions from #25 remain explicitly nonblocking and must not be represented as resolved universal semantics.

## Interpretation
#29 establishes bounded **formal/structural/foundational verification evidence** for P1-R2. It does not establish expert semantic validity, operational/domain correctness, standards conformance, cross-domain generalizability or overall ontology quality. Those conclusions remain owned by #30/#31/#51/#53.
