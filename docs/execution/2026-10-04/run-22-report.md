# Run 22 — bounded opt-in ownership repair

Baseline: `6aed4e8719b71f799bf71d7a94442456e4f82a20`. The previous adverse result is preserved. The [new optional entrypoint](../../../evaluation/grounded-ownership/v1/README.md) closes the demonstrated class-token and missing-mediated-assignee cases only for explicitly selected grounded records.

The protocol, shape/query and synthetic fixture were committed before execution at `233add41aa5776017842089d30f5899c0334bcce`. The actual local regression has **39 checks, including 20 negative controls**, plus three separately labeled simulated tool-error controls. Eight applicable cases are actually reasoner-consistent; three are actually inconsistent. No mock is counted as a formal verdict.

The new workflow validates before producing owner answers, requires the existing named/distinct Endurant evidence plus assignee mediation, and checks the entire supplied graph against the pinned current ontology/gUFO closure. It preserves benign OWL punning instead of blacklisting every class IRI. Failed validation/tool/consistency paths omit owners; legacy-only data returns NOT_APPLICABLE with consistency NOT_ASSESSED. Mixed non-opted application data remains outside grounding shape targets, while logical inconsistency still blocks an applicable result.

Canonical ontology, historical profiles and the old query are unchanged. The new shape and filtered query have separate versioned paths. No default policy, external actor taxonomy, SQL projection, public manuscript or published-site byte is changed.

The original experiment used the baseline above. Publication reconciliation on 7 October uses main `6244084eac6c47b3f870d464b378d599b982049a`: public bounded requirements remain **40/90** and completed packages **5/19**. The completed #53/#111/#124/#126 scopes and the private manuscript handoff remain intact. This optional repair adds no new requirement or whole-issue acceptance and leaves full FAP-006 NOT_ESTABLISHED. Exact-head CI, independent proof review, artifact/source verification and merged-main readback are required for durable integration.
