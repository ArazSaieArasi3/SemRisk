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
