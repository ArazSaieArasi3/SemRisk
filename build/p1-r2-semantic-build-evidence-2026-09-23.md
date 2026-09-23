# P1-R2 deterministic semantic build evidence — 2026-09-23

## Bound execution
- Workflow: `SemRisk Semantic CI`
- Workflow run: `35849810091`
- Run number: `2`
- Exact commit: `a9a655b3bf95092039dda75181604823213a62cc`
- Conclusion: **SUCCESS**
- Artifact ID: `10744687751`
- Artifact name: `semrisk-semantic-ci-a9a655b3bf95092039dda75181604823213a62cc`
- Artifact SHA-256 digest: `702cec4b8457cadb38acd82a114f71d087b3deaa7c70e52271ebebc598de4114`
- Artifact retention expiry: `2026-10-23T10:37:16Z`

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
