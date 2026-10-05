# SemRisk rc.4 editable conceptual diagram package

This is the complete **candidate inventory atlas**, not a claim that all inventory entries are fully classified OntoUML entities. It binds seven successor ontology modules derived from baseline `6d619c5bbcb3532d68e250e2c27a9a3232fd06f9`. The scientific limitations below remain open.

## Files

| File | Purpose |
|---|---|
| `SemRisk-rc4.ontouml.json` | Editable model, diagrams and geometry using the pinned official OntoUML schema 1.0.2 |
| `SemRisk-rc4.drawio` | Fifteen editable views; import/open in diagrams.net |
| `SemRisk-rc4-complete.svg` | Complete tiled vector atlas of every conceptual/helper node and every modeled link |
| `SemRisk-rc4-review-atlas.pdf` | Fifteen A3 landscape review pages; **not the conference manuscript** |
| `SemRisk-rc4-paper-panel.svg` / `.pdf` | 170 mm scenario panel; explicitly a subset, not Figure 1 replacement approval |
| `concept-coverage.csv`, `relation-coverage.csv` | Exact 47-concept and 40-registered-relation coverage |
| `multiplicity-evidence.csv` | Scoped endpoints and cardinality basis |
| `source-manifest.json`, `validation-results.json` | Exact source binding and executable bounded checks |
| `render-metrics.json`, `visual-review.md` | Physical font estimates and inspected pages |

The canonical source is `tools/build_ontouml_atlas_rc4.py` plus the bound registries/OWL. Edit semantic inputs and regenerate; direct edits of exported diagrams are review changes until reconciled with that source. The source at `conceptualization/ontouml/README.md` and reader route at `docs/ontology/diagrams/ontouml-rc4.md` point here, avoiding independent competing diagrams.

## Reading the notation

Bold names identify concepts. Hollow triangles point from a subclass to its superclass. Ordinary associations have no causal/directional arrow. Relation names are retained, including the derived `/hasRiskOwner`. Mediation is only drawn for explicitly grounded responsibility. The dashed extension link is metadata represented as a Note and anchors in the editable model, not an adopted OWL property.

Blue nodes are implemented, green nodes are operational profile helpers, amber nodes are broad patterns or an unclassified helper, and violet nodes are external/planned references or endpoint boundaries. Labels carry the distinction even without color. There are 47 registry concepts (35 local OWL classes, four markers, eight undeclared slots), 11 helper classes and seven explicit endpoint boundaries. The 101 graph edges include scoped projections, helper properties, generalizations and one metadata link; **they are not 101 domain relation types**.

Unqualified `0..*` ends mean that the diagram imposes no global bound. Green qualified profile links retain opt-in SHACL bounds; these are not universal OWL or database constraints. Eight datatype helper properties appear as ten contextual attribute uses; seven controlled individuals are displayed as enumeration literals. Datatype hints are recorded in custom properties, not invented datatype classes.

## Verification and limits

The official unmodified schema is vendored with license and commit. Project validation uses the Project entry point. Individual Diagram objects use the upstream Diagram definition plus common named-element fields, because the top-level OntoumlElement union does not include Diagram; other objects use the main entry point. Reference, coverage, cardinality and direction checks are additional to JSON schema. The six fault injections exercise material corruption paths. These checks do **not** constitute a full OntoUML/UFO antipattern analysis or a native Visual Paradigm import/export round-trip.

Remaining gates:

1. Broad Risk/Risk Source patterns and external RoleMixin specializations retain explicit scope boundaries; no fictitious stereotype is added.
2. The complete tiled atlas is unreadable at 170 mm. The readable companion and an explicitly scoped panel are supplied; final article figure integration remains open.
3. Native-editor round-trip and full pattern/antipattern analysis remain unexecuted. Schema/reference tests do not certify full UFO conformance.

Run 8 resolves the prior Exposure isolation through two registered subject/source properties. Numeric Scale Version now specializes ArtifactVersion and is displayed with its justified subkind stereotype. The 40-relation coverage is 38 retained decisions plus two additions; 47 conceptual IDs and 11 helper classes are unchanged. Diagram endpoints remain globally unconstrained; the stricter pair-profile bounds are documented in the new SHACL profile and decision table. No global functionality is implied.

Old release bytes remain unchanged. The seven-module rc.4 successor contains the two explicit semantic corrections; no empirical cases, expert responses or manuscript results were added. Rebuild with the pinned Python requirements and `@viz-js/viz@3.25.0`, then run the build_ontouml_atlas_rc4.py, render_ontouml_views_rc4.cjs, package_ontouml_atlas_rc4.py and check_ontouml_atlas_rc4.py scripts in that order. Layout can vary with installed fonts; semantic specification parity is checked separately from rendering.
