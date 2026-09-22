# W2 #19 Ubiquitous Language Acceptance Audit

**Date:** 2026-09-22
**Issue:** #19
**Result:** PASS

## Deliverables
- `conceptualization/ul/ubiquitous-language-candidate-registry.csv` — 43 preferred/provisional UL terms.
- `conceptualization/ul/source-definition-comparison-matrix.csv` — 25 source-definition comparison rows.
- `conceptualization/ul/terminology-conflict-false-friend-registry.csv` — 20 governed conflict/false-friend rows.
- `conceptualization/ul/anti-concept-registry.csv` — 22 anti-concepts/conflations.
- `conceptualization/ul/language-to-candidate-mapping.csv` — 29 language→candidate mappings.
- `conceptualization/ul/rename-deprecation-migration-lineage.csv` — 15 lineage records.
- `conceptualization/ul/domain-profile-meaning-notes.md` — scope and profile interpretation rules.

## Acceptance verification
- Every preferred term carries evidence refs or explicit G1 design rationale.
- Source-native variants are preserved in the registry and mapping tables.
- Label similarity never forces equivalence; conflict/false-friend registry preserves polysemy.
- Risk, Risk Event, Risk Scenario, Scenario Description, Risk Register Entry, Assessment Activity, Assessment Result, Risk State and Workflow State are explicitly distinguishable.
- Required families explicitly covered: Risk, Threat, Hazard, Opportunity, Risk Source, Trigger, Predisposing Condition, Consequence, Harm, Likelihood, Assessment, Inherent/Residual, Control/Treatment, Appetite/Tolerance/Criteria, Vulnerability/Exposure, Issue/Incident, Evidence/Observation/Signal, Record/Register, State, Owner/Responsibility.
- Database/UI/report artifacts and common semantic conflations are captured as anti-concepts.
- Pharma/Health/Enterprise/Governance/Method/Data meanings are scoped instead of silently generalized.
- Minority/conflicting meanings are retained as OPEN_W2/OPEN_PROFILE where appropriate.
- Rename/migration history is explicit; provisional IDs will migrate under #43 without erasing provenance.
- Module/domain naming note enforces no `and` / no `&` labels.

## Negative-criteria verification
- No dictionary-only definitions are used as scientific grounding.
- No term was selected by frequency alone.
- Rejected/ambiguous/conflicting terms remain recoverable in provenance/conflict/mapping registries.

## Important boundary
PASS means the **vocabulary foundation is stable enough for W2**, not that ontology classes, UFO stereotypes, equivalences or final IRIs are canonical. Those remain owned by #3/#20/#21/#25/#43 and G2.