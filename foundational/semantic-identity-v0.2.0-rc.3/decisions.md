# Scenario, information identity and workflow decisions

Baseline main: `7d95a05f1b5ef7c67f9750e09e2da9f8d4e5d78c`. Candidate: `0.2.0-rc.3`. These are SemRisk design commitments, not claims that a cited source supplies this domain ontology. All demonstrations are synthetic. This document supersedes the three pending decisions in the Run 5 handoff; the Run 5 version-bound evidence stays unchanged.

## D1: Scenario denotes a type, not an occurred situation

`SR-CPT-006 rdfs:subClassOf gufo:SituationType` replaces the previous `rdf:type gufo:SituationType` metadata assertion. Thus a scenario IRI denotes a situation type, with a separately declared OWL class facet subclassing `gufo:Situation`. It need not have any instances. `RiskScenario` itself is a higher-order type (`type` in the editable OntoUML view), not a situation. A represented scenario remains different from its descriptions and realized events. `realizedAs` records supported realization; it is not a rule that creates an event or instantiates the scenario class. OWL punning does not make instance metadata a theorem about a class extension. No modal logic, exhaustive possible worlds or automatic event recognition is claimed.

The explicit adapter `tools/adapt_scenario_declarations.py` adds only the two required class-facet declarations to an input scenario graph. It preserves scenario IRIs and source triples, writes a different output and is idempotent. Old evidence files are not silently rewritten. Each legacy scenario must be reviewed under the new interpretation before deployment. The strict scenario shape rejects missing declarations, while OWL alone does not enforce this syntactic metamodel discipline.

Primary anchor: gUFO 1.0.0, usage scenarios 3/4 and the higher-order type examples, distinguishes metatype assertions, subclassing and OWL punning: https://nemo-ufes.github.io/gufo/ (accessed 2026-10-05). The chosen risk-specific interpretation is ours. The schema change is semantic, not asserted backward-equivalent to rc.2.

## D2: Governed artifacts, immutable versions and content

A `ManagedInformationArtifact` is an issued/maintained social information object with a governed identifier and managing context. It is a `kind` specializing `gufo:FunctionalComplex`. This decision concerns managed artifacts with structured components, not all possible information or all physical carriers. An `ArtifactVersion` is a `subkind`: its issuance and version identity persist, but its content-bearing revision is immutable by the application contract. Changed content requires a new version IRI. `InformationContent` is abstract; copying or translating a file is neither evidence of a new semantic artifact nor proof of identical meaning. Carrier representation and automated content-equivalence detection are outside this profile.

`versionOf` connects an immutable issued version to a persistent artifact. `expressesContent` connects versions to content. Neither property is inverse-functional; there are no content-, hash-, label- or score-derived identity keys. Distinct artifact versions can express the same content. Repeated assertions of equal numeric results do not merge assessment identities. IRIs and explicit provenance carry the operational identity decision; a single RDF snapshot does not enforce cross-revision immutability.

The 17 audited information rows now have explicit identity dispositions:

| Concepts | Identity and OntoUML decision |
|---|---|
| 012 assessment method; 024 indicator; 025 threshold | Issued specification versions, `subkind` of ArtifactVersion; a new method/definition version receives a new IRI. |
| 013 assessment result; 014 likelihood; 015 impact; 016 risk level; 017 inherent; 018 residual | Immutable issued result artifacts, not bare numbers. Their production and assessment basis determine versioned context. These subkinds can overlap across independent dimensions; no new disjointness is imposed. |
| 019 confidence; 023 observation result | Recorded confidence qualification and issued observation result, respectively; both inherit artifact-version identity. Neither is an intrinsic Risk quality. |
| 026 strategy; 027 plan; 034 scenario description | Issued specification/description versions, `subkind`; execution, realization and meaning remain separate. |
| 032 register; 033 entry | Persistent governed artifacts, `subkind` of ManagedInformationArtifact. Register identity survives changes in membership. The register is an organizing artifact, not the extensional set of entries; do not add an unsupported collection stereotype. |
| 020 evidence | Context-dependent `role` of a ManagedInformationArtifact. Losing evidential use does not destroy the artifact. A supporting-use association supplies the contextual dependency; classification does not prove truth, source quality or independent validation. |

The complete 47-row audit includes per-row explanations. No `information object` pseudo-stereotype remains in these decisions. There are exactly **17** information rows; immutable-version membership includes **14**, evidence **1**, persistent register/entry **2**. Helpers remain separate from the domain inventory.

Primary type constraints: OntoUML Kind (identity provider), Subkind (inherited rigid identity) and Role (context-dependent classification), https://ontouml.readthedocs.io/en/latest/classes/sortals/kind/index.html , https://ontouml.readthedocs.io/en/latest/classes/sortals/subkind/index.html , https://ontouml.readthedocs.io/en/latest/classes/sortals/role/index.html (accessed 2026-10-05). These sources support the stereotype constraints; the managed-artifact pattern is an explicit local design decision, not an imported complete information ontology.

## D3: Reusable workflow values and record-specific history

`SR-CPT-036` denotes scheme-qualified nominal values and specializes `gufo:QualityValue`; it is not `gufo:Quality`. A scheme version defines interpretation; identical labels in different schemes need not denote the same value. In the conceptual view values use `abstract` (an enumeration is allowed only in a genuinely closed application scheme). No universal Open/Closed lifecycle is imposed.

`WorkflowAssignment` is a record-specific temporal `situation`, with one record, one value and one scheme in the strict data profile. It is not the shared value and not an intrinsic quality object. A value can be reused by many assignments. The profile requires timezone-qualified start, optional later end, matching scheme and no overlapping assignments for the same record and scheme. Half-open `[start,end)` intervals allow adjacent assignments. These are explicit application completeness rules, not unconditional OWL cardinalities that force anonymous data or equality.

`SR-REL-030` is an unqualified snapshot. The as-of query uses only qualified assignments. Closed does not entail absence of Risk, treatment success or a change to Risk State. The positive fixture deliberately retains the Risk while its entry becomes Closed.

Primary value/situation anchor: gUFO 1.0.0's quality-value distinction and temporal attribution patterns, https://nemo-ufes.github.io/gufo/ . We use a local explicit situation with record/value/scheme links; we do not claim equivalence to the complete gUFO quality-attribution pattern or fabricate an unimplemented reified bearer quality.

## Compatibility, SQL and next step

Seven modules remain; domain inventory stays 35 local OWL classes + 4 markers + 8 undeclared candidates. Existing operational inventory has 26 terms; the new namespace adds **5 classes and 6 object properties**. All 38 registered conceptual relations remain inventoried. New helper relations are separately registered. Old release files and old 121-triple temporal SQL round-trip contract remain frozen.

The relational `core.risk_scenario` key can continue identifying a scenario type. Its export must add the two declarations; that export is not yet wired into the existing temporal-only importer. Existing `enterprise.workflow_state_history` has row identity and periods but no explicit scheme-version binding. New helper triples are **not** covered by the old SQL round-trip claim. P09/P10 must add explicit scheme mapping and version/content storage, using an additive migration with data-preserving upgrade/rollback tests. Do not describe existing SQL as a complete projection of rc.3.

The next task is the full editable OntoUML model plus print-readable rendering: preserve these decisions, all concept dispositions, helper generalizations, external identity owners and relation/cardinality evidence. Risk and Risk Source remain separate broad pattern views. A schema-valid drawing is not automatically semantically valid; no finished Figure 1 is claimed here.

## Reproduction and scientific scope

Run `python tools/build_semantic_identity_candidate.py --check --assemble` and `python tools/check_semantic_identity.py --write`. The workflow `paper1-semantic-identity.yml` executes ROBOT 1.9.10 / embedded HermiT 1.4.5.456, pinned to the existing SHA-256, checks OWL 2 DL, verifies 21 newly entailed type assertions, checks a consistent no-realization countermodel, and rejects three separate deliberate inconsistencies. SHACL runs with inference disabled and MetaSHACL enabled; the shape scope is explicit-data validation, not a substitute for reasoning. Historical scenario types need adaptation before adoption; information version completeness is opted into by explicit profile typing.

Formal tool references and pin rationale: [Run 5 formal protocol](../../evaluation/foundational/2026-10-05/formal-protocol.md). The actual CI evidence records its exact tested commit separately. No complete OntoUML antipattern evaluation, expert validation, field case result or publication readiness follows from these tests.
