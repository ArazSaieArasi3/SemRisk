# Current bounded antipattern evidence

This companion rechecks selected **asserted local-source predicates** for the 15 findings in `foundational/foundational-antipattern-register.csv`. The historical CSV remains unchanged. Its old PASS values are not inherited as complete rc.4 antipattern acceptance.

Run `python tools/check_current_antipattern_evidence.py`. Eleven explicit predicate groups pass and eighteen in-memory predicate/register corruptions reject. Four findings are not assessed by this subset. **All fifteen full antipattern verdicts remain NOT_ESTABLISHED.** The output binds the exact seven local module files, current diagram view specification, concept-category registry and historical register by SHA-256. No inferred closure, native editor or external checker is used.

## Two historical descriptions that must not be reused unchanged

- FAP-005: rc.4 deliberately classifies Risk Owner as `gufo:RoleMixin`, not the historical `Role`. The missing local sortal realizations are still an open conformance question.
- FAP-015: the current diagram has 47 conceptual IDs, 11 explicitly registered helper IDs and seven labeled boundary nodes. These are separate units, not 65 domain concepts. The canonical-ID-only historical wording is too narrow for the current governed model.

## Scope and adverse outcomes

The predicates in `checks()` are the exact acceptance surface, not the full prose meaning of each historical finding. For example, FAP-007 checks the Relator superclass only; it does not establish every assignment has two valid grounded participants. FAP-006 owner-query behavior, FAP-012 complete cardinality layering, FAP-013 causal non-entailment and FAP-014 external category revalidation are explicitly not assessed by this new subset. Existing historical tests retain their original versions and do not become fresh rc.4 results by citation.

Negative controls remove a required category assertion, add an impermissible direct identity/category assertion, or introduce an ungoverned diagram helper. These are developer-selected regressions. Their rejection neither estimates detector sensitivity nor implements the complete OntoUML antipattern catalog. Absence of a local equivalence assertion is not proof of general logical non-equivalence.

#33 remains open for the declared full pattern/antipattern scope, native-editor import/save/reopen/export evidence, and readable complete representation. The full atlas still fails 170 mm readability. No ontology, source profile, SQL adapter, historical result, manuscript or release decision is changed.
