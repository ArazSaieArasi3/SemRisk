# SemRisk Paper-1 Relational Projection Design v0.1

**Issue:** #45  
**Target DBMS:** PostgreSQL 16+  
**Status:** DESIGN_FROZEN_FOR_IMPLEMENTATION  
**Semantic authority:** SemRisk ontology/concept/relation registries remain canonical. This schema is an application projection only.

## 1. Design goals
The projection exists to execute Paper-1 application tasks while preserving the distinctions required by SR-C1/SR-C2/SR-C3. It is intentionally not a mechanical class→table or property→column translation.

The design must preserve:
- Risk vs Risk Scenario vs realized Risk Event;
- Scenario Description vs scenario/event;
- Risk Register Entry vs Risk;
- Risk Assessment Activity vs Assessment Result;
- Consequence vs Impact Assessment Result;
- inherent/residual as contextual assessment-result refinements;
- Risk State vs Workflow State;
- Risk Owner role vs actor identity, with Risk Responsibility as assignment truthmaker;
- treatment strategy vs plan vs activity vs control mechanism;
- external semantic ownership for Objective/Capability/Business Process and CM-PharmE entities;
- provenance, evidence role, source version and synthetic/constructed status.

## 2. Schemas
- `meta`: stable projection identities, source artifacts, provenance, state-transition helper.
- `ref`: externally owned semantic entities.
- `core`: Risk, scenarios, events, conditions, consequences, vulnerabilities, exposure and selected cross-category relations.
- `assessment`: method, assessment activity, results, evidence, observation, confidence.
- `treatment`: strategy, plan, activity, controls and protection/use relations.
- `enterprise`: register/entry/description, workflow/risk-state histories, actors, responsibility and derived owner view.
- `governance`: indicators/thresholds and related profile semantics.
- `pharma`: bounded CM-PharmE bridge links only.
- `staging`: reserved for #47 raw/normalized load states; no semantic ownership.

## 3. Shared projection identity
`meta.semantic_instance` gives each persisted domain/application instance a stable UUID plus:
- instance IRI;
- SemRisk semantic type ID;
- source artifact;
- evidence role;
- synthetic/constructed flag.

It is **not an EAV table**: arbitrary domain attributes are forbidden. Domain state lives in typed tables.

## 4. External ownership
`ref.external_entity` caches only the minimum identity required to reference external owners:
- owner namespace/system;
- external semantic ID;
- exact version/ref;
- label for readability;
- optional stereotype/category metadata.

It does not reproduce CM-PharmE or an Enterprise/EA ontology locally.

## 5. Cross-category relations
Only relations whose domain/range are intentionally heterogeneous use `core.semantic_relation_assertion`, and its relation ID is whitelisted initially to:
- SR-REL-008 causes;
- SR-REL-009 associatedWith;
- SR-REL-010 affects.

This table is not a generic graph store and cannot accept arbitrary predicates.

## 6. Temporal model
Historical state and reassessment are first-class:
- `enterprise.risk_state_history`;
- `enterprise.workflow_state_history`;
- `assessment.assessment_result.supersedes_result_id`;
- `assessment.assessment_activity.prior_assessment_id`;
- `meta.state_transition` when an explicit predecessor/successor assertion is needed.

Current-state views/constraints are application conveniences and do not erase history.

## 7. Provenance
Every evaluated source is registered in `meta.source_artifact`. Instance-level derivation may be represented through `meta.instance_provenance`. The relational model preserves only the PROV subset required by Paper 1; richer provenance remains available in RDF/source artifacts.

## 8. Assessment/value model
Assessment result identity is independent of its value representation. A result row may hold a bounded typed projection:
- `value_numeric`;
- `value_text`;
- `value_code`.

`result_kind` distinguishes generic/likelihood/impact/inherent/residual result semantics. It does **not** create a second Risk row.

## 9. Responsibility/owner model
`enterprise.risk_responsibility` is the primitive assignment projection. The actor is referenced through `actor_id`, and the target is a risk, register entry or treatment plan.

`enterprise.v_risk_owner` is derived from active responsibility assignments. No primitive `risk.owner_id` column is allowed.

## 10. State model
Risk state and workflow state use separate histories. No query or constraint may infer:
`workflow_state='closed' ⇒ risk ceased / residual risk absent`.

## 11. Pharma bridge
`pharma.context_link` references exact external CM-PharmE v1.0.0 IDs through `ref.external_entity`. It cannot mint API/INN/product concepts that are absent from CM-PharmE v1.0.0.

## 12. Open-world vs closed-world
PostgreSQL integrity constraints implement the selected application profile under closed-world assumptions. Missing SQL rows/NULLs do not automatically mean ontological negation. #49 must explicitly interpret every SQL↔SPARQL difference.

## 13. Versioning
The projection receives an independent semantic implementation version under #46. Every evaluated DB state binds:
- ontology candidate/version;
- relational schema version/migration;
- data snapshot;
- mapping package version;
- exact repository commit.

## 14. Prohibited design shortcuts
- no one-table-per-OWL-class mechanical export;
- no generic EAV attribute table;
- no primitive owner column on Risk;
- no status column on Risk Register Entry used as Risk State;
- no inherent/residual duplicate Risk rows;
- no external ontology concepts copied into Core;
- no hidden JSON blob carrying ungoverned semantic fields in evaluated paths.

## 15. Canonical design artifacts
- `schema-table-catalog-v0.1.csv`
- `constraint-catalog-v0.1.csv`
- `ontology-rdb-mapping-v0.1.csv`
- `semantic-loss-register-v0.1.csv`
- ERDs under `relational/design/`
- `ddl-implementation-plan-v0.1.md`
- `query-test-plan-v0.1.csv`
