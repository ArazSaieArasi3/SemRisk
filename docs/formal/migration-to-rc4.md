# Cumulative adoption and consumer matrix: 0.2.0-rc.4

This is documentation of the reviewed candidate lineage, not an automatic data migration, a compatibility theorem or an SQL-parity implementation. Source baseline for this synchronization is `b2047f6eb72dc2253e7536644573cfd4929ad5fa`; no frozen ontology, shape, query, source-data or earlier evaluation bytes are changed.

| Transition | Semantic/data impact | Safe adoption and negative boundary | Evidence / consumers |
| --- | --- | --- | --- |
| 0.1.0-rc.1 → 0.2.0-rc.1 | Qualified numeric results, method/scale context, assessed/reference times and temporal responsibility | Preserve unknown times and methods. Opt in only with supplied evidence; do not fabricate historical completeness. Half-open intervals and explicit as-of parameter apply. | `formalization/qualified-context-contract-v0.2.0-rc.1.md`; temporal tests and original V007 contract. The existing bounded SQL result stays historically scoped. |
| rc.1 → rc.2 | Definition/category clarifications, RiskOwner RoleMixin, grounded responsibility profile | Grounded participant evidence is explicitly opted into; do not turn two anonymous OWL witnesses into two recorded named participants. | `foundational/revision-2026-10-05/decisions.md`; `shapes/foundational-evidence-v0.2.0-rc.2.ttl`; foundational tests. |
| rc.2 → rc.3 | Scenario metatype/class-facet distinction, managed artifact/version/content identity, reusable workflow values and temporal assignments | Review scenario meaning before adaptation. `tools/adapt_scenario_declarations.py INPUT OUTPUT` preserves source triples/IRIs and adds class-facet declarations to a different file; it does not create a realized situation/event. No hash-based identity, same-score identity, automatic meaning equivalence or complete SQL helper projection. | `foundational/semantic-identity-v0.2.0-rc.3/decisions.md`; identity tests and shape/query pair. |
| rc.3 → rc.4 | Exposure subject/source properties SR-REL-039/040; NumericScale inherits ArtifactVersion | Reuse existing endpoint identities only with evidence. A legacy scale needs a real managed parent and abstract content identity, with explicit difference; equal numeric bounds are insufficient. Unknown endpoints or parent/content remain incomplete. No automatic consequence or global endpoint functionality. | `foundational/exposure-scale-v0.2.0-rc.4/decisions.md`; rc.4 tests, 40-row relation register and 47-row concept register. |

A data adopter should (1) preserve its original graph and provenance, (2) select the exact successor profile, (3) review the above changed meanings, (4) supply evidence-backed new identities/values, (5) validate the selected shape composition, (6) compare task answers with declared expected outcomes, and (7) record rejected/unknown cases and migration provenance. Rejection of incomplete data is not permission to invent values. Reverting adoption means restoring the preserved data/profile selection; this document promises no universal semantics-preserving rollback.

## Consumer dispositions for this batch

| Consumer | Current binding / disposition |
| --- | --- |
| OWL | Seven unchanged rc.4 modules and catalog; generated asserted closure is eight files including gUFO. |
| Conceptual/formal registers | 47 concepts + 40 relations; domain, helpers and markers retain distinct denominators. |
| SHACL | Explicit three-file rc.4 operational composition; optional grounded-responsibility shape remains separately identified. Legacy five-shape profile is historical and separately bound. |
| Rules / queries | Temporal ownership, workflow and exposure queries retain original versions. Historical owner CONSTRUCT is not silently promoted to qualified temporal semantics. |
| Formal reference | Current FD-A–FD-J page and complete source-derived asserted index. Historical P1-R2 page and generated files remain intact. |
| Editable diagrams | `diagrams/ontouml/0.2.0-rc.4/` consumes the 47/40 registries. Full 170 mm readability remains a #33 gate; subset panels are not complete diagrams. |
| CQ evidence | Original 40-row classification preserved; supplementary probes reported separately. No new full CQ/SQL pass is claimed. |
| Relational projection | Existing temporal and exposure-only results remain bounded. Scale/version/content and workflow parity are incomplete; #125 explicitly deferred. No SQL edits in this batch. |
| Manuscript | Must cite current source/version, separate verification from validation, and use current entity counts with their units. Final page-fit, reference and integration acceptance belong to #32/#34. |
| Wiki / Pages | Current local source reference is available; live cross-surface parity is not established by it. #115/#117 remain open for that acceptance. |
| Scholarly release | Candidate only. #55 identity/license/release approval and final publication binding remain separate. |

## Tested and untested claims

The new synchronization checker verifies import containment, complete source inventory, selected actual assertions, preserved CQ classification, deterministic generation and deliberate corruption rejection. The exact-head workflow re-executes bounded rc.4 formal and shape tests. Its old `RC3-REGRESSION` call executes the unchanged rc.3 suite against rc.3, not a new 31-test rc.4 result. No conservative-extension proof, full OntoUML certification, human review, dataset-license clearance or publication acceptance is implied.
