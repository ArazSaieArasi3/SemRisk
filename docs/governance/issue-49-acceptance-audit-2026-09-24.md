# W3A/W4 #49 Acceptance Audit — SQL↔SPARQL Semantic Parity

**Date:** 2026-09-24
**Result:** PASS_WITH_DECLARED_PARTIALITY / CLOSED
**Validated CI run:** 35989736313
**Validated commit:** 9a799e46fa914bd4f84d1d1039c9e783a5fce1d7

## Frozen comparison set
Eight paired tasks were declared before execution in `evaluation/parity/p49-paired-query-registry-v1.0.csv`, including expected semantic answers, comparison rules and OWA/CWA caveats.

## Results
- equivalent_for_task: **5/8**
- equivalent_after_declared_normalization: **2/8**
- partial: **1/8**
- implementation_bug: **0**
- ontology_gap: **0**
- data_gap: **0**
- not_comparable: **0** for this bounded set

Runtime marker: `SEM_RISK_ISSUE_49_SQL_SPARQL_PARITY_PASS`.

## Material asymmetries retained
1. Actor identity: RDF represents a synthetic external Actor by IRI; current RDB `actor_ref` preserves a stable UUID/label but not a `semantic_instance` IRI. Task comparison therefore requires declared normalization.
2. Assessment-evidence support role: RDB explicitly stores `support_role=context`; the current RDF scenario fixture only asserts `supportedByEvidence`. Pair P49-07 is therefore **partial**, not promoted to equivalence.
3. SQL FKs/CHECKs/current-state views are closed-world application constraints and are not OWL entailments.
4. RDF absence remains graph absence under OWA; SQL fixture absence is closed-world only for the frozen snapshot.

## Decision
The relational projection preserves the intended meaning for the tested Paper-1 tasks with two declared normalizations and one explicit partial representation. This does **not** justify a blanket claim that ontology and RDB are semantically equivalent.


## R2 remediation addendum — 2026-09-24

A specialist-style simulated Semantic Web/KR review identified that P49-07 was partial because PostgreSQL carried `support_role=context` while the RDF fixture did not.

Issue #76 remediated this by adding a qualified RDF fixture representation of the evidence-support role and extending the paired query to compare result + evidence + support role explicitly.

Validated Relational CI run: **36015300327** — SUCCESS.

Updated results:
- equivalent_for_task: **6/8**
- equivalent_after_declared_normalization: **2/8**
- partial: **0/8**
- implementation_bug: **0**
- ontology_gap: **0**
- data_gap: **0**

P49-07 now returns `equivalent_for_task` for 2 RDF rows and 2 SQL rows.

The global claim boundary is unchanged: this is task-bounded parity for eight governed queries and does **not** establish lossless ontology↔RDB equivalence.


## R6 amendment — 2026-09-25

The historical results above record the evolution of the #49 parity package and are intentionally retained.

R6 data-architecture remediation eliminated the two remaining representation normalizations without changing the frozen eight-task denominator:

- **P49-05** now preserves and compares the stable synthetic actor IRI directly in RDF and PostgreSQL; no label-based identity normalization is used.
- **P49-08** now compares the exact CM-PharmE target IRI directly by resolving the versioned `ref.external_entity` reference through `meta.semantic_instance`; no owner-ID shortening normalization is used.

Validated Relational CI run **36123602513** reports:

- `equivalent_for_task`: **8/8**
- `equivalent_after_declared_normalization`: **0/8**
- `partial`: **0/8**
- implementation bug: **0/8**

Marker: `SEM_RISK_ISSUE_49_SQL_SPARQL_PARITY_PASS`.

This supersedes the current-result totals above but does **not** broaden the claim denominator. The eight tasks directly cover 17 competency questions according to `evaluation/data/r6-parity-cq-coverage-v1.0.csv`. The result remains task-bounded and does not establish global or lossless ontology↔RDB equivalence.
