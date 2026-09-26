# P1-R2 curated formal reference — local-source QA checkpoint

Owner: #115. This is a source cross-check at the current candidate, **not** a complete imported-ontology generated reference or the #55 publication-bound release.

`tools/formal_reference_qa.py` parses the six local Turtle modules using pinned RDFLib 7.6.0 and compares `p1-r2-formal-source-entity-reference-v0.1.csv` against actual declarations. It checks Git blob SHA, canonical IRI, type, label, asserted subclass/domain/range/inverse, CQ annotations, and the complete local declaration set per source. It also checks nine selected explicit cross-file disjointness pairs from FD-G, the absence of local `owl:equivalentClass`, five named SHACL node shapes, implemented owner-rule tokens, 71 release-critical conceptual IDs, the 40 CQ rows and their 26/7/6/1 status breakdown, the FD-A–FD-J headings, and that every declared import has an existing local catalog target.

Local result on 2026-09-26: **PASS** — 76/76 distinct source declarations (35 classes, 37 object properties, 4 SKOS markers), 9/9 selected pairs, 5 shapes, 1 rule, 71/71 critical IDs, 40/40 CQs and catalog-resolved declared imports. No discrepancy was found in those checked fields. The check is now in `.github/workflows/paper1-formal-reference-qa.yml` for push/PR source changes; record its exact run after execution.

## Remaining #115 work

- Compare a machine-generated **exhaustive imported closure** reference with curated interpretation, including cross-file/inferred statements that cannot be read from one declaration. The local catalog resolution check is only a prerequisite.
- Bind the formal page, ontology, catalog/vendor import and CI evidence to the final #55 publication release, then reconcile with #117 Pages output.
- Keep the 76 local declarations separate from 71 conceptual release-critical IDs and from external CM-PharmE nodes. Neither count is a quality score.

The checker confirms internal source correspondence. It does not certify the intended risk semantics, infer domain correctness from OWL consistency, or replace the expert review in #51.
