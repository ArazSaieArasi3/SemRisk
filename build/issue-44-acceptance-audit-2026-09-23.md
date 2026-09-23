# W3 #44 Acceptance Audit — Deterministic Build and Regression Pipeline

**Date:** 2026-09-23
**Result:** PASS

## Deliverables completed
- deterministic path-filtered GitHub Actions semantic CI;
- pinned Python semantic-validator dependencies;
- pinned ROBOT 1.9.10 jar with exact SHA-256 verification;
- exact gUFO v1.0.0 vendored dependency + license/attribution + import catalog;
- deterministic parser/traceability/mapping/identity/SHACL/rule checker;
- OWL 2 DL profile validation;
- HermiT consistency/classification;
- expected entailment/non-entailment checks;
- 5 SHACL negative fixtures + 1 reasoner-inconsistency fixture + trace-mismatch fixture;
- checksum/tool/runtime evidence outputs;
- machine-readable evidence schema;
- reproducibility instructions;
- exact successful run evidence bound to commit and workflow artifact.

## Successful governed run
- Run: 35849810091
- Commit: a9a655b3bf95092039dda75181604823213a62cc
- Conclusion: SUCCESS
- Artifact: 10744687751
- Artifact digest: sha256:702cec4b8457cadb38acd82a114f71d087b3deaa7c70e52271ebebc598de4114

## Acceptance findings
- Same governed semantic sources have a deterministic parse/assembly/check path and exact checksum inventory.
- Generated merged/reasoned artifacts live only under build evidence, never as competing authoring sources.
- RDF parse, OWL profile, HermiT reasoning, SHACL and rule results are separate checks.
- Known-negative fixtures prove release-critical failure detection.
- Conceptual/formal trace mismatch is detectable.
- External dependency and forbidden equivalence/mutable-reference drift is detectable.
- Semantic source changes trigger full CI; ordinary documentation outside governed semantic paths does not.
- Exact tool versions/ref/checksums are evidence-bound.
- The first run exposed one CI-source-drift false positive; that defect was fixed and the second run passed end-to-end.

## Negative acceptance verification
- Green CI is not labeled complete ontology validity.
- No mutable latest/master dependency is used as scholarly identity.
- Build-generated files do not mutate tracked semantic source.

## Consequence
P1-R2 is now a **reproducible semantic candidate**. This does not complete W3A application projection or W4 semantic/domain evaluation.
