# SemRisk formal ontology description — Paper-1 P1-R2 v0.2

**Documentation state:** source-checked candidate reference; publication-release binding and final generated reference pending #55/#115/#117.  
**Semantic authority:** exact Turtle OWL modules, SHACL shapes and SPARQL rule, never this page.  
**Documentation standard:** OGCM-RF `framework/documentation/formal-ontology-description-standard.md`, FD-A…FD-J.  
**Evaluated candidate:** P1-R2 / `0.1.0-rc.1`. The build evidence records successful SemRisk Semantic CI at commit `8fa6e221d4e2e7cf36817e666bf374ba11a921b7`, run `35850078877`, artifact digest `f8a5fd06d12faef23aca0095fe5877a507cf1673755037525a73328faffeaca6`. Later E1–E4 result rows refer to run `35990633287`. A newer independently inspected Semantic CI job, run `36145965757`, checked out commit `6e18964c3267a36fa4bef80ac8ed7e0419d32f37` and completed successfully. All six current local ontology module blobs, the SHACL file and the implemented owner rule (8/8 compared paths) match that tested commit exactly. The final publication-bound release and any later changed dependencies still require #55 binding. Source file blobs inspected for this page are listed below, so the reader can distinguish source inspection from an evaluated workflow run.

## FD-A — Identity, language and dependency policy

The Core ontology IRI is `urn:semrisk:ontology:core`, with version IRI `urn:semrisk:ontology:core:0.1.0-rc.1` and `owl:versionInfo "0.1.0-rc.1"`. Each other local module declares its corresponding `urn:semrisk:ontology:<module>:0.1.0-rc.1` version IRI. Canonical local entity IRIs use `urn:semrisk:entity:SR-CPT-...` or `SR-REL-...`; shape IRIs use `urn:semrisk:shape:`. The canonical source serialization is Turtle/OWL and the profile-specific constraints are SHACL Core. The only implemented derived rule is SPARQL 1.1 CONSTRUCT. The Core imports gUFO v1.0.0; the candidate manifest binds its external commit to `12b098158a9244179c5e0e2534cd85254a2d3b7e`. PROV-O and OWL-Time bindings are controlled in the dependency registry/catalog; external entities retain their owner.

## FD-B — Formal module architecture

| Module | Source blob SHA (inspected) | Imports / boundary |
| --- | --- | --- |
| Core `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` | `cf20fe78687a4db4dcffc21e75297f6801cc5cb4` | gUFO; base risk semantics. |
| Enterprise `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` | `b3c559b520442423a175db72e32f8fd7384d02cb` | Core; register/description/workflow profile. |
| Method `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` | `a265e500ee210ec3bb4bbb065524a875a8402c9b` | Core; assessment method/criteria. |
| Governance `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl` | `3e6e1ec0824f266052e7c8dbcfc402b2ecdcac93` | Core + Method; indicator/threshold references. |
| Pharma `ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl` | `0fddc6e7be7db52ab75f18389a8ce7ad937cf410` | Core + Enterprise; bounded external bridge. |
| Mappings `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` | `459145e4a1d7d1f20377b4eb2ed89b3d43e3420e` | Core + Enterprise + Pharma; external-owner markers/mappings. |

The candidate manifest is `ontology/p1-r2-candidate-manifest.yaml` (inspected blob `41033f26912d7b14853583a1545095d7d11e0176`). The complete controlled build process is documented in `docs/reproducibility/semantic-build.md`. Ontology source files, mappings, shapes, rules, test individuals and SQL tables are distinct artifacts.

## FD-C — Classes; FD-D — Object properties; FD-E — Datatype properties; FD-F — Individuals and enumerations

The four dimensions share one source-derived inventory, but remain distinct in the completeness assessment below.

`docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv` enumerates **76 locally declared semantic IDs** directly from the six inspected modules: **35 `owl:Class`**, **37 `owl:ObjectProperty`**, **four `skos:Concept` markers**; no local `owl:DatatypeProperty` or `owl:NamedIndividual` declaration was found in those six files. Each row records actual type, label, module, asserted subclass/domain/range/inverse *in its declaration*, CQ annotation, source path and blob. Empty fields mean **not asserted in that declaration**; cross-module statements and import-closure inference are separate. The five externally owned CM-PharmE reference nodes in Mappings are not counted as locally owned classes. These source counts differ in unit and purpose from the **71/71 release-critical conceptual IDs** checked by E3: do not report either as an ontology-quality score.

Selected critical commitments, checked in source:

| ID | Source assertion | Interpretation |
| --- | --- | --- |
| `SR-CPT-001` Risk | `owl:Class`; no gUFO superclass asserted in its declaration | Risk identity is not its register record, score or workflow status. |
| `SR-CPT-006` Risk Scenario | `owl:Class` and `rdf:type gufo:SituationType`; explicitly disjoint from `SR-CPT-007` | A possible/hypothesized pattern is distinguished from a realized event. |
| `SR-CPT-007` Risk Event | `rdfs:subClassOf gufo:Event` | Realized occurrence. |
| `SR-CPT-011` / `SR-CPT-013` | Activity subclass of `gufo:Event`; explicitly disjoint from Assessment Result | Doing an assessment differs from its contextual result. |
| `SR-CPT-017` / `SR-CPT-018` | Both subclasses of Assessment Result `SR-CPT-013` | Inherent/residual concern result context, not separate timeless Risks. |
| `SR-CPT-031` Risk Responsibility | `rdfs:subClassOf gufo:Relator` | Responsibility assignment grounds derived owner relation. |
| `SR-CPT-035` Risk State | `rdfs:subClassOf gufo:Situation`; disjoint from Enterprise `SR-CPT-036` Workflow State | Risk state versus workflow snapshot. |
| `SR-CPT-021` Provenance | `skos:Concept` marker, not local `owl:Class` | External qualified provenance pattern, not a duplicated local class. |
| `SR-REL-001` concernsRisk | `owl:ObjectProperty` with **no global domain** in Core; Enterprise asserts range Risk | A property use does not by itself infer every subject as Register Entry; completeness is a profile shape. |

For every relation, its *asserted* domain/range is a logical inference rule rather than a closed-world rejection test. The absence of a domain/range, inverse or property characteristic must remain visible. No local datatype property, unit definition or local OWL named individual is claimed from the inspected six files; example individuals are in separate test/case graphs and must carry their own provenance.

## FD-G — Logical axioms, constraints and rules

The inspected Core and Enterprise files explicitly include pairwise disjointness for: Assessment Activity/Result; Risk/Assessment Result; Consequence/Impact Assessment Result; Predisposing Condition/Vulnerability; Scenario/Event; Register Entry/Risk; Scenario Description/Scenario and /Event; Workflow State/Risk State. This is a **selected explicit list**; no unasserted pair is described as formally disjoint. No `owl:equivalentClass` axiom is asserted in the six inspected local module source files. Statements in imports may have other axioms and are not summarized by that local claim.

The evaluated SHACL file `shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl` (blob `f9228985e84c62065f9b9da32f5fecab337c2c0e`) defines five named node shapes:

| Shape | Evaluation-profile constraint, not an OWL axiom |
| --- | --- |
| SR-SHP-001 | A selected register entry has at least one `SR-REL-001 concernsRisk`. |
| SR-SHP-002 | A named Enterprise snapshot has exactly one current Workflow State through `SR-REL-030`; historical facts are outside the shape. |
| SR-SHP-003 | A selected Risk Responsibility has `SR-REL-027` and `SR-REL-028` paths. |
| SR-SHP-004 | A selected Assessment Result has required assessed-risk/activity/evidence trace paths, including inverse `SR-REL-015`. |
| SR-SHP-005 | A selected Pharma bridge target is an IRI matching the CM-PharmE v1.0.0 identity pattern. |

`rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq` (blob `6cb0350206874fbd23682223a9327790fe7ef77a`) derives `SR-REL-026 hasRiskOwner` from `SR-CPT-031` and `SR-REL-027/028`. It excludes explicitly invalidated assignments by `FILTER NOT EXISTS prov:invalidatedAtTime` in the governed application graph; missing invalidation is **not** a universal OWL proof of present ownership. `SR-RULE-002` scoring and `SR-RULE-003` workflow ordering are deferred in the rule registry. SQL FK, NOT NULL, uniqueness and application checks are separate implementation constraints and require explicit mapping to any conceptual relation.

## FD-H — Reasoning and formal assurance

The bound 2026-09-23 semantic build record reports RDF parse, OWL 2 DL profile validation, HermiT consistency/classification, expected entailments, a critical non-entailment, five rejected negative SHACL fixtures, a rejected known-inconsistent ontology, one derived-owner rule and checksum/source-drift controls. Tool manifest: RDFLib 7.6.0, PySHACL 0.40.1, ROBOT 1.9.10 (jar digest `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`) invoking bundled HermiT, Python 3.13. `evaluation/e1-e4/issue29-e1-e4-results-v1.0.csv` records a later semantic run `35990633287`, 14 Turtle inputs and 5/5 known-negative SHACL fixtures. The later run `36145965757` was inspected directly: semantic-validation job SUCCESS, with OWL 2 DL, HermiT, expected consequences and negative-control steps successful. Its checkout SHA is recorded above and the eight inspected local source blobs match. These are **bounded version-bound verification results**; #55 still must bind a final publication release and any new source/dependency change triggers recheck. Neither logical consistency nor a SHACL pass proves the intended domain semantics.

## FD-I — Conceptual/formal traceability

`ontology/formal-traceability-report-v0.1.csv` and `ontology/formal-entity-inventory-v0.1.csv` own the conceptual-to-formal mapping, including entities intentionally represented as markers or external alignments rather than local classes. E3 records 71/71 release-critical semantic IDs present, plus uniqueness and forbidden-equivalence controls. `governance/identity/formal-helper-id-iri-map-v0.1.csv` records five shape IDs and the rule as formal helpers. The 76 local declarations in the source-derived reference are a different denominator. For example, `SR-CPT-001 → urn:semrisk:entity:SR-CPT-001 → CQ-001/002/016`, while `SR-CPT-021` is a conceptual Provenance marker. A diagram or Wiki page must preserve the source type and module boundary.

## FD-J — CQ/query semantics

`evaluation/cq/issue52-cq-results-v1.0.csv` (inspected blob `7304224b745a8eee5d562ddab0dc3a8110261470`) retains all 40 original CQs: 26 executable, seven partially executable, six conceptual-only, one deferred. Examples: CQ-001 tests Register Entry→Risk identity; CQ-002 is conceptual-only for multiple entries concerning one Risk; CQ-003 executes Scenario/Event/Description via RDF+SQL; CQ-006 is partial because assessment method is unpopulated in the bounded fixture. All CQ-specific prerequisites/result limits remain in the CSV. The P49 file reports eight of eight `equivalent_for_task` for frozen paired SQL↔SPARQL tasks representing 17 directly covered CQs; it does not establish global/lossless equivalence. Asserted/inferred answers and database closed-world conditions must be explained per query before stronger reasoning claims.

## Documentation completeness and gate

| FD dimension | Current evidence | Status for P1-R2 candidate | Before publication-bound release |
| --- | --- | --- | --- |
| FD-A/B | IRIs, versions, imports, module paths, blobs and build record | DOCUMENTED_CANDIDATE | #55 exact full dependency/release ref and generated doc ref |
| FD-C/D | 35 class + 37 object-property declaration rows; selected interpretation | DOCUMENTED_CANDIDATE | review cross-file axioms and import-closure effects on curated reference |
| FD-E/F | zero local datatype-property/NamedIndividual declarations in six module sources; external/test nodes distinguished | DOCUMENTED_WITH_APPLICABILITY | state separately for other future modules/instance datasets |
| FD-G | local disjointness, five SHACL shapes, one rule and two deferred rules | DOCUMENTED_CANDIDATE | exact axiom/shape/rule release binding and examples |
| FD-H | reported CI runs/tool manifest and negative controls | CONDITIONAL | final #55 release/ref binding; recheck after semantic/dependency change |
| FD-I | 71/71 critical IDs with separate 76 source declarations | DOCUMENTED_CANDIDATE | final conceptual-to-formal impact review |
| FD-J | 40 CQ outcome records plus eight paired tasks | DOCUMENTED_CANDIDATE | selected query prerequisite/answer review at exact release |

This table is *documentation coverage*, not a quality score, OGCM-RF conformance certification, independent human validation or #54 assurance PASS. A deterministic [generated asserted import-closure reference](generated/p1-r2-generated-reference.md), [complete canonical N-Triples graph](generated/p1-r2-asserted-closure.nt) and [source/graph manifest](generated/p1-r2-closure-manifest.json) now list all direct assertions in the six modules and locally catalog-bound gUFO file. This generated layer is **asserted**, not an OWL reasoner entailment closure, and does not replace canonical source or the #55 release identity. #115 remains open for review of the generated layer and final release binding; Wiki #116 and Pages #117 may project this page only with its candidate status visible.
