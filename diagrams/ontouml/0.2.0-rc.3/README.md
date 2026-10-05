# SemRisk rc.3 editable conceptual diagram package

This is the complete **candidate inventory atlas**, not a claim that all inventory entries are fully classified OntoUML entities. It binds the unchanged seven ontology modules at baseline `0417f1d7f0237904f8b57a65ddc5385aeab85fb0`. The scientific limitations below remain open.

## Files

| File | Purpose |
|---|---|
| `SemRisk-rc3.ontouml.json` | Editable model, diagrams and geometry using the pinned official OntoUML schema 1.0.2 |
| `SemRisk-rc3.drawio` | Fifteen editable views; import/open in diagrams.net |
| `SemRisk-rc3-complete.svg` | Complete tiled vector atlas of every conceptual/helper node and every modeled link |
| `SemRisk-rc3-review-atlas.pdf` | Fifteen A3 landscape review pages; **not the conference manuscript** |
| `SemRisk-rc3-paper-panel.svg` / `.pdf` | 170 mm scenario panel; explicitly a subset, not Figure 1 replacement approval |
| `concept-coverage.csv`, `relation-coverage.csv` | Exact 47-concept and 38-registered-relation coverage |
| `multiplicity-evidence.csv` | Scoped endpoints and cardinality basis |
| `source-manifest.json`, `validation-results.json` | Exact source binding and executable bounded checks |
| `render-metrics.json`, `visual-review.md` | Physical font estimates and inspected pages |

The canonical source is `tools/build_ontouml_atlas.py` plus the bound registries/OWL. Edit semantic inputs and regenerate; direct edits of exported diagrams are review changes until reconciled with that source. The source at `conceptualization/ontouml/README.md` and reader route at `docs/ontology/diagrams/ontouml-rc3.md` point here, avoiding independent competing diagrams.

## Reading the notation

Bold names identify concepts. Hollow triangles point from a subclass to its superclass. Ordinary associations have no causal/directional arrow. Relation names are retained, including the derived `/hasRiskOwner`. Mediation is only drawn for explicitly grounded responsibility. The dashed extension link is metadata represented as a Note and anchors in the editable model, not an adopted OWL property.

Blue nodes are implemented, green nodes are operational profile helpers, amber nodes are broad patterns or an unclassified helper, and violet nodes are external/planned references or endpoint boundaries. Labels carry the distinction even without color. There are 47 registry concepts (35 local OWL classes, four markers, eight undeclared slots), 11 helper classes and seven explicit endpoint boundaries. The 98 graph edges include scoped projections, helper properties, generalizations and one metadata link; **they are not 98 domain relation types**.

Unqualified `0..*` ends mean that the diagram imposes no global bound. Green qualified profile links retain opt-in SHACL bounds; these are not universal OWL or database constraints. Eight datatype helper properties appear as ten contextual attribute uses; seven controlled individuals are displayed as enumeration literals. Datatype hints are recorded in custom properties, not invented datatype classes.

## Verification and limits

The official unmodified schema is vendored with license and commit. Project validation uses the Project entry point. Individual Diagram objects use the upstream Diagram definition plus common named-element fields, because the top-level OntoumlElement union does not include Diagram; other objects use the main entry point. Reference, coverage, cardinality and direction checks are additional to JSON schema. The six fault injections exercise material corruption paths. These checks do **not** constitute a full OntoUML/UFO antipattern analysis or a native Visual Paradigm import/export round-trip.

Remaining gates:

1. Exposure has no dedicated registered link; its isolation is shown rather than repaired with an invented relation.
2. NumericScale's foundational category is not settled; external RoleMixin sortal specializations are not supplied by this core.
3. Broad Risk/Risk Source patterns and external boundaries are deliberately not assigned fictitious stereotypes.
4. The full tiled diagram is unreadable at 170 mm. The readable complete companion atlas is supplied, but article integration and Figure 1 are still open. The article remains targeted at seven pages, maximum eight including references.
5. Native-editor round-trip and full pattern/antipattern checking remain unexecuted. This package is an editable, schema-checked candidate, not certified tool interoperability.

No ontology release bytes, empirical cases, expert responses or manuscript results were changed by this run. Rebuild with the pinned Python requirements and `@viz-js/viz@3.25.0`, then run the build, render, package and check scripts in that order. Layout can vary with installed fonts; semantic specification parity is checked separately from rendering.
