# Import / Reference / Mapping Policy v0.1

## Import classes
1. `IMPORT`: allowed only for exact immutable external releases whose semantic fit and license are approved.
2. `REFERENCE`: SemRisk uses the external concept as prior art/owner without loading its ontology closure.
3. `ALIGN`: governed mapping such as related/close match; not equivalence.
4. `EXTERNAL_OWNER_BRIDGE`: SemRisk relates to externally owned entities without duplicating their identity.

## Current W3 decisions
- **COVER:** REFERENCE + ALIGN; no bulk import.
- **ROSE:** REFERENCE + ALIGN/profile specialization; no bulk Core import.
- **CM-PharmE v1.0.0:** EXTERNAL_OWNER_BRIDGE; no redistribution/import assumption until license decision.
- **PROV-O:** intended selective REUSE/IMPORT only after #43 exact version binding.
- **gUFO:** intended foundational dependency only after #43 exact version/IRI binding and #27 import-closure test.
- **OWL-Time:** optional temporal reuse; exact decision deferred to #27/#43.

## Equivalence burden
`owl:equivalentClass` / `owl:equivalentProperty` requires: exact target version, identity-condition compatibility, #21 evidence, #25 foundational compatibility, regression against relevant #7 CQs, and explicit approval in mapping registry.

## Moving references
`main`, `latest` or unversioned remote ontology URLs cannot be scholarly semantic identity. If a moving reference is unavoidable during development, it must be labeled `UNBOUND_DEV_ONLY` and cannot support publication-bound evaluation.