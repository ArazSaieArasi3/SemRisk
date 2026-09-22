# SemRisk External Ontology Reuse Architecture Decision — W2 #21

**Date:** 2026-09-22
**Decision:** `REFERENCE_AND_ALIGN_BY_DEFAULT; IMPORT_ONLY_AFTER_FOUNDATIONAL_AND_LICENSE_GATES`

## Primary decision
SemRisk Paper-1 W2 will **not bulk-import COVER or ROSE**. It will bind exact immutable external artifacts, retain external ownership, and publish explicit alignment/mapping decisions. This is a deliberate architectural decision, not a failure to reuse.

### Why COVER is referenced/aligned rather than imported now
- Exact commit is bound and Apache-2.0 permits reuse.
- No governed semantic release/tag was identified; the W1 reference is commit-bound.
- The pinned Turtle has a source-level `thttps://` ontology-declaration anomaly.
- Several high-value lexical overlaps are not semantics-equivalent: notably `Risk`, `RiskAssessment`, `Likelihood`, `TriggerEvent`.
- SemRisk's dominant contribution depends on preserving information-artifact/activity/result/state distinctions that COVER does not directly provide in the same form.
- #25 must establish foundational compatibility before any equivalence/import policy.

### Why ROSE is referenced/profile-aligned rather than imported now
- Exact corrected commit is bound and MIT-licensed.
- The repository corrects the published cardinality erratum; exact state is reproducible.
- ROSE is a security-engineering specialization and contains strong reusable patterns for Vulnerability, Security Mechanism, Control Capability/Event and causation.
- SemRisk's Control Mechanism is deliberately cross-domain; copying ROSE's hierarchy into Core would make security semantics look universal.
- #25 must resolve which ROSE/gUFO patterns can be reused directly versus mapped as profile specializations.

## Allowed W2 mapping strengths
- `REFERENCE`: external construct is relevant but no semantic bridge asserted.
- `ALIGN_BRIDGE`: explicit related/close semantic mapping; **not** OWL equivalence.
- `EXTEND_PROFILE`: external construct is treated as a narrower/profile specialization or external owner.
- `IMPORT`: prohibited at this stage unless a later #25/#26 decision demonstrates semantic compatibility and #43 records exact version/license.

## Equivalence rule
No `owl:equivalentClass` / `owl:equivalentProperty` is authorized by #21. Exact/equivalence mappings require #25 foundational justification and regression against #7 CQs before formalization.

## License/release rule
External ontology licenses apply to the exact artifact reused, not to related papers. Mutable `main` is never a release identity. Every imported dependency, if later approved, must be represented in #43/#55 with exact commit/release/versionIRI/license.

## Novelty rule
A SemRisk construct mapped as `REFERENCE`, `ALIGN_BRIDGE` or `EXTEND_PROFILE` cannot be called novel merely because its label/structure differs. Novelty can only attach to the governed combination/distinctions/federation/evaluation after #22/#53.

## CQ protection
Reuse must not erase SemRisk's required CQ distinctions. Any import/alignment causing Risk/Record, Assessment/Result, Risk State/Workflow State, treatment/control or evidence/provenance collapse is rejected or must be wrapped by a SemRisk semantic pattern.