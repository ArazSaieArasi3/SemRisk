# R6 Data Architecture / Relational Modeling / Knowledge Graph Engineering Review Remediation Acceptance Audit — 2026-09-25

**Issues:** #97, #98, #99, #100, #101, #102  
**Origin:** specialist-style simulated Data Architecture / Relational Modeling / Knowledge Graph Engineering review (R6), used as an adversarial review aid. This is **not independent human expert validation**.

## Decision
**PASS WITH BOUNDED PROJECTION / EVOLUTION SCOPE.**

The R6 remediation strengthens projection identity, temporal/reassessment integrity, staging lineage, migration governance, SQL↔SPARQL parity discipline and the database-source-of-truth boundary. It does not claim production-scale performance validation, complete bitemporal/event-sourcing semantics, or global lossless ontology↔RDB equivalence.

## Review result
The 15 R6 review questions were completed. The strongest initial findings concerned avoidable actor-identity loss, underconstrained state transitions, reassessment/supersession cycles and cross-Risk links, UUID-based "latest" semantics, migration-order/checksum governance, staging target reconciliation and parity-claim scope.

No Critical finding required rejection of the relational architecture. The principal findings were High-severity hardening items and were remediated below.

## #97 — Stable actor identity / direct parity
Implemented:
- additive `enterprise.actor_ref.actor_iri` with uniqueness for non-null values;
- governed Paper-1 fixtures now preserve stable actor IRIs;
- P49-05 now compares Risk IRI + actor IRI directly rather than actor label;
- P49-08 now resolves the exact external target IRI through `ref.external_entity.instance_id → meta.semantic_instance.instance_iri`.

Final parity result:
- P49-01..P49-08: **8/8 `equivalent_for_task`**
- normalization cases: **0/8**
- partial: **0/8**
- implementation bug: **0/8**

This is a task-bounded result for the frozen eight tasks, not a global projection-equivalence claim.

## #98 — State-history/transition integrity
Implemented in `relational/sql/V006__r6_projection_integrity.sql`:
- state-transition self-loop rejection;
- risk-state endpoints must be actual Risk State rows concerning the same Risk;
- workflow-state endpoints must be actual Workflow State rows concerning the same Register Entry;
- wrong-family and cross-target transitions are rejected;
- known `valid_from` order cannot be reversed;
- Risk State overlap is not globally prohibited because the ontology does not justify universal non-overlap;
- Paper 1 remains a bounded single-workflow-scheme projection unless a future profile introduces explicit scheme identity.

## #99 — Reassessment/supersession lineage and latest result
Implemented:
- prior assessment must concern the same Risk;
- superseded result must concern the same Risk;
- recursive predecessor/supersession cycles are rejected;
- valid branching from a common prior assessment remains allowed;
- `assessment.v_latest_result_by_kind` no longer uses UUID ordering as time semantics; it orders by assessment end/start time with projection-created time fallback, with UUID only as a deterministic final tie-breaker.

Negative regression covers cross-Risk links, multi-hop cycles and a UUID-order-vs-time counterexample.

## #100 — Migration evolution governance
Implemented:
- `relational/design/migration-manifest-v1.0.csv`;
- immutable Git blob hashes for evaluated migration/companion artifacts;
- machine-checked migration dependencies/order;
- clean CI build now executes:
  `V001 → V002 → V005 → V006`;
- `tools/r6_migration_governance_check.py` detects path/hash/order drift;
- historical evaluated migrations remain immutable; changes require a new migration.

Marker:
`SEM_RISK_R6_MIGRATION_GOVERNANCE_PASS`.

## #101 — Staging lineage / evidence-role compatibility
Implemented:
- `staging.v_lineage_reconciliation` for source-record → transform-rule → target-instance reconciliation;
- statuses distinguish missing target IRI, unresolved target, missing transformation rule, forbidden target for blocked/protected/rejected records, and OK;
- `evaluation/data/r6-evidence-role-compatibility-v1.0.csv`;
- regression proves the governed snapshot reconciles, an injected unresolved target is detected, DS-002 protected holdout has no record-level semantic instance, and synthetic evidence cannot carry `independent_validation`.

Staging remains intentionally allowed to precede target creation; reconciliation is therefore a post-load gate rather than an insert-time FK.

## #102 — Parity coverage / OWA-CWA / semantic-authority guard
Implemented:
- `evaluation/data/r6-parity-cq-coverage-v1.0.csv` with all **40/40** CQs;
- frozen P49 denominator remains **8 tasks**, directly covering **17 CQs**;
- all other CQs are explicitly outside the P49 denominator even if they have other executable evidence;
- `tools/r6_relational_governance_check.py` rejects primitive Risk owner/status/score shortcuts, identity-erasing P49 normalization, migration of DataProjection into semantic authority, and loss of the task-bounded manuscript nonclaim;
- database constraints remain bounded closed-world application/profile controls and are not interpreted as OWL negation/entailment.

Marker:
`SEM_RISK_R6_RELATIONAL_GOVERNANCE_PASS`.

## Validation
Authoritative substantive R6 run:
**Relational CI 36123602513 — SUCCESS**  
Validated commit: `7d3915c7c211f9a7a7cc6b827a80ccd3d5bca047`.

Observed markers:
- `SEM_RISK_R6_MIGRATION_GOVERNANCE_PASS`
- `SEM_RISK_R6_RELATIONAL_GOVERNANCE_PASS`
- `SEM_RISK_R6_PROJECTION_INTEGRITY_PASS`
- `SEM_RISK_ISSUE_49_SQL_SPARQL_PARITY_PASS`
- `SEM_RISK_ISSUE_50_CROSSLAYER_NEGATIVE_CONTROLS_PASS`
- `SEM_RISK_ISSUE_52_CQ_REGRESSION_GOVERNANCE_PASS`

The run also retained the R3 co-ownership and R5 federation regressions.

## Failure/remediation history
Several intermediate R6 commits triggered expected CI failures while migrations/fixtures were incomplete. Two failures were especially informative:

1. The first relational-governance manuscript guard rejected the phrase "lossless global ontology-to-database equivalence" even when the manuscript explicitly said the results **do not establish** it. The guard was corrected to require the explicit nonclaim rather than reject safe wording.
2. The first cross-Risk state negative test accidentally used a second Risk State belonging to the same Risk. The model correctly accepted it. The negative fixture was corrected to create a genuinely different Risk and state; the final regression then passed.

These failures are retained as engineering evidence and were not counted as model PASS results.

## Current parity amendment
Historical #49 and R2 audit results are preserved. A dated R6 amendment records the current result:
**8/8 direct task-equivalence**, no declared identity normalization.

The denominator remains the eight predeclared tasks / 17 directly represented CQs. OWA/CWA mismatch, foundational-role projection loss, bounded provenance representation and external-taxonomy non-reconstruction remain documented semantic losses.

## Residual limitations
- no enterprise-scale performance/load benchmark;
- no full bitemporal/event-sourcing correction model;
- rollback/backward-compatibility across deployed production versions is not exercised;
- external license/provenance is linked through governed source artifacts rather than duplicated onto every external reference;
- P49 parity covers eight frozen tasks, not the entire ontology or all CQs;
- SQL integrity is intentionally stricter than OWL open-world semantics in selected application-profile contexts.

## Acceptance
The six R6 remediation issues satisfy their bounded acceptance criteria. Closure does not substitute for #51 real expert semantic validation and does not authorize universal semantic correctness, global relational equivalence or production-scale performance claims.
