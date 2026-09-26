# SemRisk P1-R2 documentation rollout disposition — 2026-09-26

Pinned profile: `OGCM-RF-DOC-RO 0.1`, `ArazSaieArasi3/OGCM-RF@4822b1a1b7978e94e66bd6a283024bac78b6a0b8`. Research ID R-022; parent #112. This is an M4-scoped *candidate* for the formal ontology plus relational twin. An evaluated, publication-bound M5 documentation state has not been established. See `ogcm-rf-adoption-gap-audit-2026-09-26.md` for all RO-01…RO-30. No row below asserts full profile conformance.

## Authority and profile composition

Research/Ontology is primary. Data/Engineering applies to the relational projection, mapping and task-bounded parity only; it consumes SemRisk's ontology definitions. Software/Product and Business documentation are not active Paper-1 documentation profiles; reassess if a product/API or independent business process becomes material. `docs/documentation/profile-composition.yaml` records the owners and audience paths. OWL/RDF, SHACL, registries and evidence in the repository define their respective semantics or observations. `docs/wiki/pages/` is curated explanation published to the private Wiki; `site/ontology/0.1.0-rc.1/` is an offline generated candidate. Neither publication surface changes semantic authority. The source-controlled Wiki manifest, 8/8 live read-back, generated asserted closure, Pages registry and surface manifest are the present evidence. Wiki is private, Pages is not deployed.

## Reader journeys and page types

| Reader / type | Actual route | State / gap | Owner |
|---|---|---|---|
| Academic: PT-01 overview | Wiki Home → Scope and Contributions | Live private Wiki; source and rendered read-back completed | #116 |
| Academic: PT-02 research explanation | Scope and Contributions → Evidence and VVEAA → Pharma Case | Partial: integrated evidence→decision→model research journey and explicit limitations route still needed | #118, #53, #54 |
| Academic: PT-05 evaluation/evidence | Evidence and VVEAA → repository evaluation records | Bounded candidate results; expert and independent holdout remain pending | #113, #51, #31, #54 |
| Academic: PT-06 evolution/lineage | Reproduce and Release → release train | Partial: decision/lineage narrative and semantic-vs-label changes are not yet a reader page | #118, #55 |
| Academic: PT-09 governance/status/history | Home → Reproduce and Release; Wiki history; source manifest | Partial: candidate state explicit, frozen baseline and public read-back absent | #118, #55, #56 |
| Engineer: PT-03 ontology/module | Semantic Architecture → canonical six modules and gUFO import | Live explanation and pinned source; complete module interpretation remains scoped | #115, #118 |
| Engineer: PT-04 concept/property | Formal Reference → 76-entity generated index and asserted graph | Bounded source correspondence; not complete reader-facing formal or reasoned reference | #115, #117 |
| Engineer: PT-07 index/reference | Formal Reference → offline `/ontology/0.1.0-rc.1/` candidate | Offline only; live versioned Pages and explorer absent | #117, #119 |
| Engineer: PT-08 tutorial | Reproduce and Release → semantic-build instructions | Partial: version-specific end-to-end tutorial/browser verification still needed | #118, #117 |
| Engineer: PT-10 mapping/realization | Relational Projection → task-bounded mapping/parity | Bounded relational twin; no KG/API realization claim | #116, #118 |

Both journeys share semantic definitions, version state, evidence and limitations. Home now displays both routes in the signed-in private Wiki, with source/live body parity and revision `9827a5211d864bc1b6a2eda587ca5741a2f64f0f` recorded in `docs/wiki/p1-r2-live-wiki-readback-2026-09-26.md`. This is a rendered route check, not a usability study or public access result.

## Rollout factory reverse mapping

States: `bounded` means evidence exists for a narrow slice, `partial` means acceptance has open checks, `blocked` means a named gate prevents completion, and `N/A` needs a trigger. None means the strict RW issue contract has been independently passed.

| RW | Applicability / trigger | Current state and evidence or gap | Issue / next action |
|---|---|---|---|
| 01 Assessment | Mandatory | partial: RO matrix and source/surface inventory; full current audit and maturity record here | #118 verify paths/ref |
| 02 Profile adoption | Mandatory | partial: pinned adoption YAML and schema-checked profile composition; full quality/deviation review pending | #118 |
| 03 Epic/plan | Mandatory | partial: #112 and this reverse map; children predate strict factory format | #112/#118 link gates and closure |
| 04 Authority | Mandatory | partial: surface manifest; stale implementation profile | #118 refresh governance |
| 05 Surface allocation | Mandatory | partial: source/Wiki/Pages mapped; Pages checks false | #118/#117 |
| 06 IA/journeys | Mandatory | partial: dual-audience Home route is live and source-matched; usability/coverage review pending | #118 |
| 07 Editorial integrity | Mandatory | partial: source-to-Wiki exact parity; E0–E4 editorial review absent | #118/#55 |
| 08 References/citation | Mandatory, scholarly | missing: governed REF corpus and manuscript membership proof | #118 with #53/#55 |
| 09 Research journey/evolution | Mandatory | missing: integrated decision/lineage reader route | #118 |
| 10 Ontology/module | Mandatory | bounded: architecture Wiki and source module links | #115/#118 |
| 11 Entity reference | Mandatory, stable candidate entities | partial: 76 local inventory, generated index; conceptual/formal coverage caveat | #115/#117 |
| 12 Formal semantics | Conditional, OWL/SHACL exists | partial: FD-A…FD-J and local QA; reasoned effects/release binding pending | #115 |
| 13 Generated reference | Conditional, formal ontology exists | blocked: offline versioned reference exists, Pages and WebVOWL absent | #117/#119 |
| 14 Visual documentation | Recommended, diagrams exist | partial: 76-ID atlas and 37-property map; diagram manifest/accessibility audit missing | #118/#119 |
| 15 Evaluation/reproducibility | Mandatory, claim-bearing | partial: VVEAA and build records; independent validation/assurance pending | #113/#54 |
| 16 Data/RDB/KG mapping | Conditional, relational twin exists | partial: RDB projection and parity; no KG/API claim | #118/#117 |
| 17 Software/Product | N/A, no Paper-1 product/API scope | no product surface; reassess on product/API commitment | #112 scope review |
| 18 Business/domain | N/A, no independent business-profile scope | Pharma case is research evidence; reassess on independent business process scope | #112 scope review |
| 19 Tutorial/how-to | Conditional, executable build exists | partial: semantic build instructions; reader reproduction check pending | #118 |
| 20 Documentation baseline | Conditional, candidate baseline exists | partial: Wiki hashes and Pages version registry; no frozen release baseline | #118/#117/#55 |
| 21 QN/QL assessment | Mandatory before conformance | missing: no frozen rubric/evidence-based QN plus qualitative review | #118; keep adoption partial |
| 22 Publication/render | Conditional, private Wiki exists | partial: 8/8 Wiki read-back passed; Pages not deployed/rendered | #116 done for Wiki; #117 |
| 23 Snapshot/read-back | Conditional on frozen/release-bound docs | blocked: no frozen scholarly baseline; Wiki read-back is candidate-only | #55/#56 then #117 |
| 24 Adoption closure | Mandatory | blocked: RO Mandatory/Conditional and RW gaps remain | #118 |
| 25 Release/freeze binding | Conditional on real release | blocked: #55 release identity and #56 access unresolved | #55/#56 |
| 26 Refresh/upgrade | Mandatory | partial: triggers below; implementation/profile manifest refresh and owner recording pending | #118 |

Gate state: G-DOC-0 `partial` (#118); G-DOC-1 `partial` (#118/#117); G-DOC-2 `blocked` (#115/#117/#118); G-DOC-3 `partial` (#113/#118); G-DOC-4 `blocked` (QN/QL and Pages); G-DOC-5 `blocked` (#118); G-DOC-6 `blocked` (real #55/#56 release). This is a reverse mapping of existing issues, not 26 newly created issues. #119 is the focused WebVOWL work item under RW-13/14.

## Refresh and closure order

1. #118: complete the remaining RO/PT/RW evidence, research journey, reference corpus, diagram manifest, editorial and QN/QL checks. `.research` authority/status, composition and private Wiki academic/engineering Home route have candidate-level records.
2. #115/#113 and related evidence gates: complete exact formal/reasoning and VVEAA claims at the candidate ref.
3. #119/#117: reproducible offline WebVOWL, Pages privacy/access and rendered versioned reference checks. Existing `0.1.0-rc.1` route is immutable.
4. #55/#56: decide actual publication identity, licensing/access and frozen baseline, then deploy/read back if authorized by those gates.
5. Reassess RW-21/24/26 and close #118/#112 only from evidence; no issue closure itself makes a release.

Reassess on OGCM profile upgrade, semantic candidate/release change, evaluation rerun, Wiki source or live drift, diagram change, new RDB/KG/API surface, Pages deployment, reference corpus change, or publication binding. Owner: #118 until documentation governance is assigned to a durable release process. The audit and manifest should be updated together.
