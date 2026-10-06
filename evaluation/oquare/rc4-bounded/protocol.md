# SQL-independent metric selection protocol

Selected before executing the new rc.4 metric calculations. The historical P1-R2 TMOnto/ANOnto pilot and current inventory counts were already known; **this is not blinded selection**. Source baseline: `da148b2508f1eb820a37099cc135a794a290063b`. The separate protocol commit is recorded by the runner after publication. This batch performs no SQL work; #125 remains deferred.

## Four selected diagnostics

For each population S with size N, use only asserted triples from the seven local rc.4 modules. Imported gUFO is retained for closure/provenance checks but contributes no denominator members or annotation numerators. Calculate each diagnostic separately for domain classes D and helper classes H; never pool them as a domain-quality score.

D is the set of concept registry rows whose formal_status is LOCAL_CLASS. H is the union of class IRIs in the two explicit helper registries. D and H must be disjoint, declared locally as owl:Class, and together exhaust the local class declarations. A mismatch fails rather than reducing a denominator.

| ID / formula version | Numerator | Denominator and empty case | Unit / meaning |
| --- | --- | --- | --- |
| TMOnto_asserted_scoped / 1 | Classes in S with more than one distinct directly asserted URI-valued rdfs:subClassOf parent | N−1; N<2 gives null / UNDEFINED_POPULATION_LT_2 | Raw multiple-parent diagnostic. Exclude anonymous restrictions, inference/transitivity, equivalence expansion and rdf:type stereotypes. A parent may be external without joining S. |
| ANOnto_assertion_density_scoped / 1 | Distinct asserted triples with subject in S and predicate rdfs:label or rdfs:comment | N; N=0 gives null / UNDEFINED_EMPTY_POPULATION | Assertions/class, possibly >1. Includes different values/languages, empty literals and URI objects as raw assertions; identical duplicate triples collapse. |
| Local_nonempty_label_coverage / 1 | Classes in S with at least one literal rdfs:label whose trimmed lexical value is nonempty | N; N=0 gives null / UNDEFINED_EMPTY_POPULATION | Binary presence ratio [0,1], not label correctness. No language restriction; languages retained in ledger. |
| Local_nonempty_comment_coverage / 1 | Classes in S with at least one literal rdfs:comment whose trimmed lexical value is nonempty | N; N=0 gives null / UNDEFINED_EMPTY_POPULATION | Binary comment presence, not semantic-definition adequacy. No substitution by labels, scope notes, descriptions or imported text. |

Record integer numerator/denominator, raw value/null, status, population/member-list hash, formula version and missing class IDs. Keep all class-level annotation and named-parent evidence. No rounding before stored division, clamping, weighted aggregation, one-to-five scoring or percentage interpretation of annotation density.

## Reuse and attribution

Preserve `evaluation/oquare/p1-r2-structural-pilot-v0.1.*` and `tools/pilot_oquare_structural.py` unchanged. The two metric families reuse the historical pilot and pinned primary OQuaRE definitions: https://github.com/tecnomod-um/oquare/blob/3c870b504c799bfb7598912d1b29cab7f44d12ac/oquare_docs/quality_metrics.md (Git blob `5163873f96960c15de49af6660d023d07175c9c9`).

The asserted-only local populations and exact counting policies are explicit **local operationalizations**, not verified equivalence to the official Java engine. The two coverage metrics are local diagnostics, not invented official OQuaRE/OQF metrics. The root-subtraction convention N−1 is preserved for pilot comparability but does not make the selected local population a theoretically normalized hierarchy. A value above one must not be clamped. Multiple inheritance can be justified. Annotation volume or nonempty prose cannot prove semantic correctness. No full OQuaRE/OQF adoption, OQUO conformance or overall scientific-quality score is claimed.

Connectivity is not selected because it would need a separate policy for OWL domain/range, inherited restrictions, SHACL links and imported hubs. CQ statuses remain historical and are not relabeled a new rc.4 execution result. Corpus statistics remain separate from ontology metrics.

## Preselected sensitivity and rejection tests

Use a synthetic graph separate from the candidate, with exact expected fractions:

- A second named parent changes the multiple-parent numerator; a third parent for that same class does not. This blind spot is reported.
- Anonymous restriction or foundational rdf:type does not change named-parent count.
- Removing the sole label/comment lowers the corresponding coverage and density; adding another useful annotation raises density only.
- Empty/whitespace or URI-valued annotations raise raw density but not nonempty-literal coverage.
- Replacing a nonempty comment with nonsense may leave every numeric result unchanged; report that failure of semantic sensitivity.
- Duplicate triples do not change results. Imported annotations do not change domain/helper measurements. Helper-only annotation change cannot affect domain measurement.
- Empty/singleton populations return the specified nulls, never NaN/infinity/fabricated scores.
- Reject a missing registry class, unexpected local class, source-hash drift, unbound import and generated-result drift.
- All mutation graphs are isolated; source bytes and original historical pilot outputs remain unchanged.

Run the preselected synthetic tests before calculating the candidate. Bind results to this protocol's commit/hash, source hashes, script hash and actual tool version. All subsequent modifications to this protocol need an explicit explanation; do not retrofit it to desirable candidate results.
