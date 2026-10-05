# Run 6 — implemented semantic identity decisions

The three pending decisions from Run 5 are now executable in `0.2.0-rc.3`. The version is a tested candidate, not a publication-ready ontology or final manuscript. [Decision contract](../../../foundational/semantic-identity-v0.2.0-rc.3/decisions.md) (repository-root path: `foundational/semantic-identity-v0.2.0-rc.3/decisions.md`).

| Delivered | Actual scope | Evidence |
|---|---|---|
| Scenario type level | Higher-order situation type; explicit class-facet adapter; no automatically created occurrence | rc.3 Core; adapter and scenario probes |
| Information identity | Seventeen concept dispositions; artifact, immutable version and abstract content separated | rc.3 modules; 47-row audit; source/registry definition check |
| Workflow history | Scheme-qualified reusable values; separate record-specific intervals; exact as-of query | Enterprise module; SHACL; query; synthetic cases |
| Verification | 31/31 bounded checks including 17 negative data cases; 21 actual inferred type assertions; one non-entailment countermodel; three expected inconsistencies | `evaluation/semantic-identity/v0.2.0-rc.3/results.json` and `ci-evidence.json` |
| Preservation | Old rc.1/rc.2 files frozen; 29 prior foundational checks and 32 native PostgreSQL checks successful | New manifest's historical hashes; workflow logs |
| Continuation | Seven package prompts, shared execution prompt, registry, reader catalog and requirement evidence synchronized | Execution-control register and issue readback |

## Progress and limits

- Current bounded semantic batch: **3/3 decisions implemented and tested**. A decision count measures this sub-batch only.
- Accepted complete package contracts: **3/19 (15.8%)**, unchanged. P06/P07/P08/P11 remain in progress; no whole-package completion is inferred from the new tests.
- Author requirements: **90/90 routed; 18/90 verified in bounded scope (20%)**, unchanged. Existing evidence gained depth; no unperformed manuscript requirement was marked complete.
- Ontology counts stay **47 concept dispositions (35 local classes, four markers, eight undeclared)** and **38 registered relation decisions**. Helpers are separately counted: 26 existing terms plus 11 new terms (five classes, six properties).
- Full OntoUML rendering, the new helper SQL projection, literature-derived case, actual expert validation and revised Word/PDF remain open. Zero expert responses and zero new empirical case records are reported in this run.

The initial remote source-binding check detected newline conversion in three transferred CSVs. Exact byte-preserving transfer corrected that deployment defect; the formal workflow then passed. It was not an ontology inconsistency. Final source verification uses raw Git blob hashes, not normalized text.

## Next bounded batch

Produce the **full editable OntoUML source and readable Figure 1**, with complete coverage, supported stereotypes, named relations and justified cardinalities. Use separately labeled broad-pattern and external/deferred views instead of assigning fake stereotypes. Deliver SVG/PDF, editable source, coverage mapping and caption; verify at the actual IEEE print size. Keep the 7-page target and 8-page absolute ceiling for the later integrated manuscript.

Continue through the remaining case/projection/evaluation and manuscript gates without asking the author to reapprove routine choices. The framework-specific temporal SQL parity already tested does not cover the new helper vocabulary. P10 must implement and test the additive extension before claiming full candidate projection.
