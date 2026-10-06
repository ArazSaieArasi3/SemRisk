# rc.4 offline Wiki draft

> Offline rc.4 documentation candidate. Not a live Wiki update, deployed Pages site, final scholarly release, full OntoUML acceptance or independent domain validation.

The existing live Wiki still represents its historical P1-R2 snapshot. This is a separate source projection; Pages remains disabled. The bundled guide and term index have no assigned public URL.

# SemRisk formal ontology description: 0.2.0-rc.4

**State:** current candidate reference, not a scholarly release. **Authority:** version-bound OWL sources, SHACL and queries, with their governed conceptual decisions. This document is a read-only projection, never a second semantic source. The historical [P1-R2 reference](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/ontology/formal-ontology-description-p1-r2-v0.2.md) remains unchanged and describes 0.1.0-rc.1 only.

The [generated reference](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/formal/0.2.0-rc.4/generated-reference.md), [116-entity inventory](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/formal/0.2.0-rc.4/entity-inventory.csv), [canonical asserted graph](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/formal/0.2.0-rc.4/asserted-closure.nt) and [source manifest](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/formal/0.2.0-rc.4/source-manifest.json) are reproduced offline by `python tools/generate_rc4_formal_reference.py --check`. Every source row records SHA-256 and Git blob identity. The composition binds unchanged constituent shape/query versions; matching composition does not mean renaming them to rc.4.

## FD-A — Identity, language, profile and dependencies

Candidate identity is **0.2.0-rc.4**, based on seven Turtle/OWL modules in `ontology/releases/0.2.0-rc.4/`. Each ontology has an unversioned `urn:semrisk:ontology:<module>` IRI and a version IRI ending `:0.2.0-rc.4`. Entity identifiers persist across revisions: `urn:semrisk:entity:SR-CPT-*` and `SR-REL-*`. Assessment and information helpers have separate namespaces `urn:semrisk:profile:assessment-context:` and `urn:semrisk:profile:information-state:`.

The local catalog resolves all declared imports to the seven versioned modules and `ontology/vendor/gufo-v1.0.0.ttl`. Thus the complete asserted import closure has **eight source files**. PROV, SKOS and Dublin Core vocabulary declarations in the local modules are not claims to import their complete ontologies. Mappings retain external ownership. No remote import fetch, persistent scholarly IRI or publication license decision is implied. OWL 2 DL validation is an executed reasoner/tool check, not inferred merely from Turtle parsing.

## FD-B — Module architecture

| Module | Boundary |
| --- | --- |
| core | Risk, event/scenario distinction, assessment and treatment semantics, managed information identity, Exposure endpoints |
| enterprise | Registers/entries, descriptions, scheme-qualified workflow values and assignments |
| method | Assessment method specifications; Risk Criteria is not locally declared |
| governance | Indicator/threshold references |
| pharma | Bounded external application bridge, not a comprehensive Pharma ontology |
| mappings | External-owner references and selected alignment metadata |
| assessment-context | Qualified numeric assessments, temporal attributes, responsibility evidence and scale specification versions |

The generated module table lists exact ontology/version IRIs and imports. The manifest binds all files, including the catalog, conceptual/helper registries, selected shape composition and queries. Helper registry `version` fields inherited from rc.2 record their earlier registry identity; they do not override the actual rc.4 module headers. This document does not rewrite frozen historical releases.

## FD-C — Classes

There are **46 locally declared OWL classes**: 35 domain classes plus 11 operational helpers. The 47 conceptual rows consist of 35 local classes, four SKOS markers and eight not-locally-declared slots. Helpers are not additional domain concepts. The 17 information-related domain rows have the identity decisions recorded in `foundational/semantic-identity-v0.2.0-rc.3/decisions.md`.

Critical distinctions are source-bound as follows (full IRIs use the namespace above):

| Selected term(s) | Asserted commitment and boundary |
| --- | --- |
| SR-CPT-001 Risk / SR-CPT-033 Register Entry | Distinct classes; the entry is an information artifact concerning risk and is explicitly disjoint from Risk. No record-count-to-risk-count inference. |
| SR-CPT-006 Scenario / SR-CPT-007 Event | Scenario subclasses gUFO SituationType; Event subclasses gUFO Event; they are disjoint. A scenario individual may have a separately declared punned class facet; no realized event is created by declaration. |
| SR-CPT-011 Assessment Activity / SR-CPT-013 Result | The activity subclasses gUFO Event and is disjoint from the issued result artifact. Equal scores do not identify assessments. |
| SR-CPT-035 Risk State / SR-CPT-036 Workflow State | A risk state subclasses gUFO Situation; workflow values subclass gUFO QualityValue. They are disjoint. Closing an entry does not eliminate its Risk. |
| SR-CPT-026 Strategy / SR-CPT-027 Plan / SR-CPT-028 Treatment Activity / SR-CPT-029 Control | Specifications inherit ArtifactVersion identity, activity concerns execution, and control is separately represented. No automatic success or reduction of risk follows from a plan or a control assertion. |
| SR-CPT-010 Exposure | A gUFO Situation with explicit subject/source relations. It is not an assessment score and does not automatically produce a consequence. |
| assessment-context:NumericScale | Subkind of information-state:ArtifactVersion, inheriting managed-artifact identity. Equal bounds do not identify two issued scale versions. |

No additional disjointness, existential witness, key or global cardinality is asserted by this prose. Literal selected axioms are checked by `tools/check_rc4_formal_reference.py`; all other assertions are inspectable in the canonical graph.

## FD-D — Object properties

The local declaration inventory has **50 object properties**: 39 registered domain properties and 11 helpers. The 40 relation-decision rows include those 39 object properties and one annotation property, `SR-REL-038 profileExtendsCoreConcept`. It remains in the complete 116-term inventory. A relation row is not necessarily an OWL object-property declaration.

`SR-REL-039` has asserted domain Exposure and range Risk Subject; `SR-REL-040` has domain Exposure and range Risk Source. Neither is globally functional. Domain/range assertions infer classifications under OWL; they do not reject missing or mistyped database fields as a closed-world validator would. `information-state:versionOf` and `expressesContent` do not assert inverse functionality, hash identity or content-equivalence detection. Anonymous restrictions and imported axioms are available in the full asserted graph rather than flattened into invented simple cardinalities.

## FD-E — Datatype properties

Eight local datatype properties occur in the assessment-context namespace: `assessedAt`, `referenceTime`, `methodVersion`, `numericValue`, `minimum`, `maximum`, `validFrom`, `validTo`. Date-time properties have `xsd:dateTime` ranges, numeric properties use `xsd:decimal`, and methodVersion uses `xsd:string`. Timezone presence, completeness and interval ordering are additional shape/query policies, not consequences of an `xsd:dateTime` range alone. These are separate from external `prov:invalidatedAtTime`.

## FD-F — Individuals, values and examples

Seven controlled named individuals are local: BeforeControl, AfterControl; Likelihood, Impact, RiskLevel; Observed, Projected. The three enumeration classes use `owl:oneOf`, with explicit `owl:AllDifferent` lists within their respective groups. This is not a universal closed enterprise workflow scheme. Workflow values are scheme-qualified application data, not these seven assessment individuals.

Four SKOS concept markers remain separately counted. Test individuals are synthetic fixture data outside the ontology inventory. The literature pilot's 24 source-local statements are a different evidential unit and cannot be substituted for formal test cases or expert responses.

## FD-G — OWL axioms, SHACL, queries and governance

The strict rc.4 operational shape composition is:

1. `shapes/assessment-context-v0.2.0-rc.1.ttl`
2. `shapes/semantic-identity-v0.2.0-rc.3.ttl`
3. `shapes/exposure-scale-v0.2.0-rc.4.ttl`

The 12 named shapes of this composition are generated in the manifest. The optional grounded-responsibility shape `shapes/foundational-evidence-v0.2.0-rc.2.ttl` and the historical five-shape profile are separately bound, not silently activated as one universal profile. Shapes are applied with inference disabled and MetaSHACL enabled in the bounded harness; they validate explicitly represented application data. They do not silently replace the historical five-shape Paper-1 profile. Opt-in version completeness requires an explicit artifact parent, abstract content and explicit difference from the series artifact; cross-revision content immutability remains a governance/application rule that a single RDF snapshot cannot prove.

A strict Exposure record requires one named subject and one named source with explicit appropriate types. Its interval is optional. If present, dates must be timezone-qualified and ordered. ScaleVersionShape composes ScaleShape and VersionShape. WorkflowAssignment requires a record, value, scheme and start; it rejects overlapping assignments for the same record/scheme. Half-open intervals allow adjacent assignments.

Three version-bound as-of SELECT queries cover ownership, workflow and exposure (exact paths in the manifest). They require a caller-bound timezone-aware `asOf`; there is no ambient NOW(). Missing onset is not evidence of a current interval. The old unqualified owner CONSTRUCT and snapshot workflow relation remain historical contracts, not aliases for these qualified queries.

SQL NOT NULL, uniqueness, foreign keys and migrations are separate application constraints. This synchronization makes **no full SQL/SPARQL equivalence or helper round-trip claim**. #125 is deferred. See [migration and consumer matrix](https://github.com/ArazSaieArasi3/SemRisk/blob/bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6/docs/formal/migration-to-rc4.md).

### Readable paper example

Let `e` be a recorded Exposure, `s` its subject and `q` its source. The ontology asserts the domain/range of `SR-REL-039` and `SR-REL-040`, so assertions `e SR-REL-039 s` and `e SR-REL-040 q` support Exposure/subject/source classification. The strict profile separately requires exactly one explicit named endpoint of each kind. An OWL model with an Exposure and no endpoint assertions is not rejected solely for missing those records; the bounded countermodel explicitly constrains their cardinalities to zero and remains consistent. This distinction prevents a data-completeness requirement from becoming an invented universal ontology axiom. Exposure alone also does not entail a consequence.

## FD-H — Entailments, non-entailments and actual assurance

Historical rc.4 evidence is bound in `evaluation/exposure-scale/v0.2.0-rc.4/ci-evidence.json`, implementation `418b8e3a8ebe14e73fbc8e1d820e452f3afa1ec7`: actual OWL 2 DL validation, four type entailments, two consistent countermodels and two correctly rejected category contradictions. These are bounded synthetic verification results, not complete semantic correctness, domain validation or an independent human review. The rc.3 suite separately records 21 entailments and its scenario/information/workflow scope; those numbers must not be presented as one new rc.4 test count.

The rc.4 four tested type consequences are NumericScale instance → ArtifactVersion, ManagedInformationArtifact and gUFO FunctionalComplex, and Exposure instance → gUFO Situation. The countermodels establish no forced consequence and no required endpoint existence for an incomplete Exposure. They are actual satisfiable-model checks, not a claim derived merely from an absent asserted triple. Inconsistent probes add AbstractIndividual to a scale and QualityValue to an Exposure.

Reproduction uses Python, RDFLib 7.6.0, PySHACL 0.40.1, ROBOT 1.9.10 with SHA-256 `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`, and embedded HermiT 1.4.5.456. The dedicated formal synchronization workflow repeats the relevant bounded checks on its exact checked-out head. The asserted-reference generator itself does **not** run a reasoner. An exact-head CI result must be consulted before claiming the new documentation batch passed CI.

## FD-I — Concept-to-formal traceability

The current 87-row registry contains **47 conceptual IDs + 40 relation IDs**, all accounted for against current declarations/dispositions. The generated 116-local-entity inventory is a different denominator (including helpers and named individuals). The historical 71-critical-ID and 76-declaration metrics remain tied to 0.1.0-rc.1. Neither is relabeled as current rc.4 completeness.

Read `ontology/releases/0.2.0-rc.4/conceptual-iri-register.csv`, the two separate helper registries, and `foundational/exposure-scale-v0.2.0-rc.4/*-audit.csv`. Empty declared structural fields mean not asserted locally, not disproved under the imported closure. Eight not-locally-declared concepts must remain visibly distinct from the four declared markers.

## FD-J — Competency questions and answer interpretation

The preserved original CQ classification has 40 rows: 26 executable, seven partially executable, six conceptual-only and one deferred. It is a historical result classification, **not a fresh full rc.4 execution claim**. Supplementary temporal/identity/exposure probes do not create additional original CQs. Query answers are set-valued and depend on explicit profile data, bound time and selected inference regime. Unknown/missing times, missing method identity and unresolved mappings remain unknown or partial rather than invented values.

The as-of suites test their stated fixture scopes: the rc.4 Exposure suite covers boundary instants, equivalent timezone representations and unbound-time behavior; the rc.3 workflow suite covers before/boundary and snapshot behavior. These are not universal query guarantees. The frozen eight paired SQL/SPARQL tasks and 17 covered CQs do not establish full rc.4 parity. Scope expansions need new declared expected answers and SQL work under #125, which this batch does not perform.

## Completeness, negative states and remaining gates

| Dimension | Candidate documentation result | Evidence |
| --- | --- | --- |
| FD-A | Documented | Exact version/catalog/source manifest |
| FD-B | Documented | Seven-module generated architecture |
| FD-C | Documented | 46 local classes, selected checked distinctions |
| FD-D | Documented | 50 local properties; no invented functionality |
| FD-E | Documented | Eight local datatype properties |
| FD-F | Documented | Seven controlled individuals; four separate markers |
| FD-G | Documented | Explicit shape/query composition and governance separation |
| FD-H | Bounded, not universal | Source-bound historical evidence plus exact-head workflow |
| FD-I | Documented | 87 disposition rows, 116 separate declaration inventory |
| FD-J | Historical classification and bounded probes | 40 preserved CQ rows; no full rc.4 SQL rerun |

All **10/10 dimensions are documented** at the stated candidate scope; this is not a quality percentage or package/issue closure. #115 additionally retains live Wiki/Pages parity (#117) and final release binding (#55). P07 dependency acceptance must be checked separately, and no final-paper, license, independent-review or submission gate is waived. Existing historical documents and release bytes are preserved. Downstream paper consumers must use this current reference with these limits rather than silently transplant old counts.
