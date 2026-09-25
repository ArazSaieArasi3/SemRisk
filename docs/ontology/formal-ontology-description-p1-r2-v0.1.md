# SemRisk formal ontology description — Paper-1 P1-R2 candidate

**Status:** v0.1 curated, source-checked *initial* description; FD-A…FD-J completion audit pending #115.  
**Semantic authority:** the Turtle ontology/SHACL/rules at exact evaluated ref. This page is documentation, not a replacement ontology.  
**Method:** OGCM-RF `framework/documentation/formal-ontology-description-standard.md` (FD-A…FD-J).  
**Candidate:** `0.1.0-rc.1`; source blob of Core read for this page: `cf20fe78687a4db4dcffc21e75297f6801cc5cb4`. A complete import-closure/CI commit and release checksum are still to be bound under #55.

## FD-A — Identity, language and imported semantics

The Core source `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` declares ontology IRI `urn:semrisk:ontology:core`, version IRI `urn:semrisk:ontology:core:0.1.0-rc.1`, and `owl:versionInfo "0.1.0-rc.1"`. It imports `http://purl.org/nemo/gufo#/1.0.0`. Local entity IRIs use `urn:semrisk:entity:` plus governed IDs. Turtle is the inspected serialization. The external import resolution/hash and complete OWL profile execution are recorded by the semantic CI candidate, rather than inferred from the IRI alone.

## FD-B — Architecture

The candidate separates Core (`ontology/core/`), Enterprise (`ontology/enterprise/`), Method (`ontology/method/`), mapping (`ontology/mappings/`), and profile-level SHACL (`shapes/`). External gUFO and CM-PharmE identity are mapped or imported under governed boundaries, not copied into local SemRisk ownership. See `ontology/formal-entity-inventory-v0.1.csv` and `ontology/formal-traceability-report-v0.1.csv`. Full import/derivation graph and file checksums remain for the #115 completion audit.

## FD-C — Selected classes and actual commitments

| Governed ID | Inspected IRI | Actual formal assertion in Core | Intended distinction |
| --- | --- | --- | --- |
| SR-CPT-001 Risk | `urn:semrisk:entity:SR-CPT-001` | `owl:Class`; no gUFO superclass asserted in the inspected declaration | risk phenomenon distinct from mutable record/score/workflow. |
| SR-CPT-006 Risk Scenario | `urn:semrisk:entity:SR-CPT-006` | `owl:Class`; `rdf:type gufo:SituationType` | possible/hypothetical scenario, distinct from realized event and description. |
| SR-CPT-007 Risk Event | `urn:semrisk:entity:SR-CPT-007` | `owl:Class`; `rdfs:subClassOf gufo:Event` | realized occurrence. |
| SR-CPT-011 Risk Assessment Activity | `urn:semrisk:entity:SR-CPT-011` | `owl:Class`; `rdfs:subClassOf gufo:Event` | assessment activity, distinct from produced result. |
| SR-CPT-013 Risk Assessment Result | `urn:semrisk:entity:SR-CPT-013` | `owl:Class`; no asserted gUFO superclass in inspected declaration | contextual result; likelihood/impact/inherent/residual result classes separately described. |
| SR-CPT-017 / 018 | corresponding `urn:semrisk:entity:` IRIs | both `rdfs:subClassOf` SR-CPT-013 | pre-/post-treatment result contexts, not two Risk identities. |
| SR-CPT-031 Risk Responsibility | `urn:semrisk:entity:SR-CPT-031` | `owl:Class`; `rdfs:subClassOf gufo:Relator` | concrete assignment relation, not a single unique-owner assumption. |
| SR-CPT-035 Risk State | `urn:semrisk:entity:SR-CPT-035` | `owl:Class`; `rdfs:subClassOf gufo:Situation` | risk-context state distinct from register workflow snapshot. |
| SR-CPT-021 Provenance | `urn:semrisk:entity:SR-CPT-021` | `skos:Concept` marker, deliberately not a local `owl:Class` | formal provenance uses qualified external PROV patterns. |

These are *selected* declarations, not an exhaustive class listing. OntoUML/gUFO annotation is not silently converted to an OWL disjointness/equivalence claim.

## FD-D/E/F — Relations, data values and individuals

`SR-REL-001 concernsRisk` is an `owl:ObjectProperty` linking a record or scenario description to the Risk it concerns. Its Core declaration explicitly **does not assert a global OWL domain**; doing so would infer that every subject is a register entry. The source and `SR-SHP-001` illustrate why a profile-specific completeness constraint is separate from an OWL property declaration. Remaining object/datatype property characteristics, literal units and example individual roles require exhaustive source extraction in #115; unspecified is retained as unspecified.

## FD-G — Logical versus validation commitments

OWL class/property axioms use open-world entailment. SHACL validates a selected graph/profile. For instance, `shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl` declares `SR-SHP-001` with `sh:targetClass SR-CPT-033`, path `SR-REL-001` and `sh:minCount 1` for an evaluated register entry; `SR-SHP-002` constrains a *named enterprise workflow snapshot* to one current workflow state, not all history. `SR-SHP-004` requires assessment-result trace paths in the evaluated profile. These are SHACL constraints, **not** OWL axioms. SQL FK/NOT NULL and application workflow rules remain a third/fourth implementation layer; their equivalence to an OWL statement must be argued per mapping.

No uninspected universal disjointness, qualified cardinality, property chain, or sufficient definition is asserted by this page.

## FD-H — Reasoning and limits

Semantic CI has reported OWL 2 DL profile, HermiT consistency/named-class satisfiability, expected entailment/non-entailment and negative-control results on the previous tested candidate (#44). #115 must attach the exact workflow run, resolved import fingerprints, reasoner version, target commit and any rerun after changes. Logical consistency answers whether the asserted theory is coherent under the chosen regime; it does not establish expert acceptance or real-world risk coverage.

## FD-I — Conceptual-to-formal trace

The governed `ontology/formal-traceability-report-v0.1.csv` maps `SR-CPT-001` to `urn:semrisk:entity:SR-CPT-001` and CQ-001/002/016; `SR-CPT-006` to CQ-003/004/021; `SR-CPT-007` to CQ-003/012/021; and `SR-CPT-013` to CQ-005/006/007/015/022/031. A conceptual ID need not be one `owl:Class` (see Provenance). The inventory is the complete register; this page is an explanatory view.

## FD-J — CQ/query semantics

The paper retains 40 conceptual CQs: 26 executable, 7 partial, 6 conceptual-only, and 1 deferred. Eight frozen SQL↔SPARQL task pairs have been reported directly equivalent for those tasks, directly representing 17 CQs. Query output depends on the exact instance graph/database snapshot and the semantics/normalization specified per task. An answer in the relational projection does not prove global equivalence or semantic validity.

## Completion matrix

| Dimension | Initial page status | Remaining proof for #115 |
| --- | --- | --- |
| FD-A/B | PARTIAL | exact import closure and per-module/release ref |
| FD-C | PARTIAL | all critical classes, actual restrictions/disjointness, checked examples |
| FD-D/E/F | PARTIAL | complete property/individual/reference extraction and applicability |
| FD-G | PARTIAL | source-linked axiom/shape/rule inventory and examples |
| FD-H | PARTIAL | exact tested commit/run/tool and changed-candidate rerun |
| FD-I | PARTIAL | all release-critical ID-to-formal traces reviewed |
| FD-J | PARTIAL | CQ-by-CQ asserted/inferred/data/query preconditions and result |

This is documentation coverage only. Publication in Wiki (#116) and generated Pages (#117) follows source/version QA; neither surface changes ontology semantics.
