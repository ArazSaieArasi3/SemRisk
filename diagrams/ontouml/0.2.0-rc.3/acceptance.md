# Run 7 diagram acceptance contract

Baseline main: 0417f1d7f0237904f8b57a65ddc5385aeab85fb0; ontology 0.2.0-rc.3. Fixed before authoring the diagram.

- Account for all 47 conceptual rows and all 38 registered relations. Separate the 35 local OWL classes, four registry markers and eight undeclared external/planned rows. Account for all 11 helper classes and 11 object-property helpers; include the eight data-property helpers and seven controlled individuals.
- Use only justified standard stereotypes; unclassified patterns, external references and NumericScale must be visibly marked without a fabricated stereotype. A schema-valid mixed-boundary model is not complete UFO validation.
- Use bold class names, hollow-triangle generalizations, ordinary associations unless a special stereotype is supported, explicit relation names and multiplicities. Unconstrained ends use 0..* (absence of a bound); SHACL/profile cardinalities remain in explicitly labeled profile views. No guessed global functionality, no invented material Risk-to-Actor relation.
- Provide actual editable OntoUML schema 1.0.2 JSON with class/relation/generalization/view/shape objects; validate against a pinned upstream schema and check references semantically. Provide readable SVG views, a complete tiled master SVG and a vector PDF review atlas. No substitution by Mermaid or WebVOWL.
- Produce exact coverage, multiplicity-source and source-version reports; automatically catch missing nodes/edges, fake stereotypes, broken references and incorrect generalization direction. Inspect every rendered PDF page.
- Record whether a complete view remains readable at 170 mm IEEE width. If not, disclose that and supply the full companion diagram plus an explicitly scoped paper view; do not relabel a subset as the complete ontology.
- Preserve all ontology release bytes. Do not claim expert validation, complete antipattern checking or final paper readiness from these diagram tests.
