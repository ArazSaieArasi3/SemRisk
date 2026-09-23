# P1-R2 deterministic semantic build evidence — 2026-09-23

## Bound execution
- Workflow: `SemRisk Semantic CI`
- Workflow run: `35850078877`
- Run number: `5`
- Exact commit: `8fa6e221d4e2e7cf36817e666bf374ba11a921b7`
- Conclusion: **SUCCESS**
- Artifact ID: `10744654947`
- Artifact name: `semrisk-semantic-ci-8fa6e221d4e2e7cf36817e666bf374ba11a921b7`
- Artifact SHA-256 digest: `f8a5fd06d12faef23aca0095fe5877a507cf1673755037525a73328faffeaca6`
- Artifact retention expiry: `2026-10-23T10:40:17Z`

## Executed checks
- RDF/Turtle parsing: PASS
- conceptual↔formal traceability: PASS
- stable-ID/IRI uniqueness: PASS
- forbidden equivalence mapping check: PASS
- test-data leakage check: PASS
- exact dependency binding check: PASS
- positive SHACL fixture: PASS
- five known-negative SHACL fixtures: detected as expected
- SR-RULE-001 derived ownership rule: PASS
- OWL 2 DL profile validation: PASS
- HermiT consistency/classification: PASS
- expected entailment checks: PASS
- critical non-entailment check: PASS
- known-inconsistent reasoner fixture: rejected as expected
- exact checksum inventory: PASS
- tracked source drift after build: none

## Toolchain
- Python runtime: 3.13.x family, exact runner version captured in workflow artifact
- RDFLib 7.6.0
- PySHACL 0.40.1
- ROBOT 1.9.10, jar SHA-256 `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`
- HermiT invoked through pinned ROBOT 1.9.10
- Java 17 runtime exact version captured in artifact

## Interpretation
This is **verification evidence for the declared formal/build checks**, not independent semantic/domain validation. It establishes that the P1-R2 formal candidate is reproducibly parseable, OWL-2-DL-profile compatible under the declared toolchain, reasoner-consistent for the tested closure, SHACL-testable, and traceable to the governed conceptual subset.

It does not establish expert validity, transferability, application/RDB parity or overall ontology quality; those remain W4/W3A work.

## Finalization note
The final governed run above validates the post-fix candidate manifest in which exact CI evidence is externalized to this record, avoiding a self-referential manifest→run→manifest loop.
