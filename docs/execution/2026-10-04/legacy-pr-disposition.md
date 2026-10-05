> Run 3 update: all four retained foundational PRs have an individual 71-row semantic disposition and five executed regression probes. See `foundational/legacy-pr-58-61-resolution-2026-10-05.md`. PR #129 is merged; PRs #58–#61 are now closed without merge as superseded, with branch/history retained. Exact state and body readbacks are in `run-3-readback.json`. The old review below is retained as history.

# Legacy PR dispositions — 2026-10-04

Compared against `f37cf41f6987d9887d9b96e913174a718f41439d` using commit comparisons and source readback. A branch ahead count does not imply missing scientific value. No stale branch is merged wholesale.

| PR | Ahead / behind main | Reviewed content and disposition | Follow-up owner |
|---|---|---|---|
| #58 | 1 / 628 | Foundational-analysis checkpoint exists only under the old branch path. KEEP OPEN for semantic reconciliation against current `foundational/` registries; old path absence is not proof of missing semantics | P06 #123 |
| #59 | 2 / 628 | Includes #58 and stable-ID mapping checkpoint. KEEP OPEN; compare proposed category/stereotype dispositions with current category and relation registries | P06 #123 |
| #60 | 3 / 628 | Includes earlier checkpoints and full coverage CSV. KEEP OPEN; preserve unresolved relation truthmaker questions and map each relevant row to current decisions before closure | P06 #123 |
| #61 | 4 / 628 | Includes earlier checkpoints and Risk State split proposal. KEEP OPEN; current state-boundary and identity contracts already separate risk situation, assessment result and workflow. Reconcile the old assessment-state proposal and five regression probes rather than reintroducing obsolete semantics | P06 #123, P11 #113 |
| #62 | 1 / 522 | Its only changed file, `evaluation/negative-controls/issue-50-baseline-and-gap-register-v0.1.md`, is byte-identical on main. CLOSE as already incorporated; preserve branch/history | #8 |
| #63 | 3 / 522 | Baseline register and mutation TTL are byte-identical on main. Current `tools/issue50_semantic_mutation_check.py` retains all earlier mutation checks and adds parser/import controls, with the entailment test delegated to the current harness. CLOSE as incorporated and extended; no new scientific test is claimed here | #8; P11 for actual revised-candidate execution |

The four foundational PRs share one stacked lineage. P06 reviews the maximal #61 content once and records per-file/per-question dispositions for #58-#61, avoiding four redundant analyses. Closure then requires either exact integrated evidence or a documented rejection/supersession rationale. Four retained PRs are follow-up inputs, not permission to replace current main with their old trees.

Reviewed current counterparts: `foundational/risk-identity-continuity-contract-v0.1.md`, `foundational/risk-state-semantic-boundary-v0.1.md`, `foundational/foundational-category-registry-v0.1.csv`, `foundational/foundational-relation-rationale-v0.1.csv`, `foundational/foundational-antipattern-register.csv`.
