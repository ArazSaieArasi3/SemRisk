# OGCM-RF documentation adoption gap audit — SemRisk P1-R2, 2026-09-26

**Provisional disposition:** PARTIAL, not `core_conforming`. Pinned method source: `ArazSaieArasi3/OGCM-RF@4822b1a1b7978e94e66bd6a283024bac78b6a0b8`, `framework/documentation/research-ontology-documentation-profile.md` (RO-01…RO-30) and `templates/documentation/rollout-issue-pack.md`. Project baseline: private Wiki eight-page live read-back in `docs/wiki/p1-r2-live-wiki-readback-2026-09-26.md`; source navigation commit `84b2a7f3b237f6a2cd6509e7f4bee14b57aefd38`; offline Pages version `0.1.0-rc.1`. This is a gap triage, not a QN/QL score or full conformance test.

`BOUNDED` means a narrow artifact exists, not full RO acceptance. `PARTIAL` means implementation or proof is incomplete. `GAP` means the current OGCM-specific deliverable/reader route was not found. `PENDING_PAGES` means only an offline candidate exists. Every row is applicable or provisionally applicable; no N/A was used to hide debt.

| Capability | State | Observed evidence / missing check | Owner |
|---|---|---|---|
| RO-01 | BOUNDED | Wiki Home; 8-page read-back | #116 |
| RO-02 | PARTIAL | Scope page, RQ/CQ and method require reader route | #118 |
| RO-03 | PARTIAL | Evidence/VVEAA links; source basis not fully narrated | #118 |
| RO-04 | PARTIAL | Conceptual registry/atlas linked; semantics and diagram role audit | #118 |
| RO-05 | BOUNDED | Semantic Architecture and canonical module refs | #116 |
| RO-06 | BOUNDED | FD-A…FD-J page with source limits | #115 |
| RO-07 | PENDING_PAGES | Offline generated reference only | #117 |
| RO-08 | BOUNDED | 76-entity source index and selected Wiki links | #115 |
| RO-09 | PARTIAL | Pharma dataset provenance linked; breadth/limits audit | #118 |
| RO-10 | BOUNDED | Relational projection and task-bounded parity | #116 |
| RO-11 | PARTIAL | VVEAA page; #51/#54 remain open | #112 |
| RO-12 | PARTIAL | Build instructions and candidate status; final bundle pending | #55 |
| RO-13 | PARTIAL | Four-step evidence→boundary→model→check→claim route live on Scope Wiki; decision-level trace/lineage depth pending | #118 |
| RO-14 | PARTIAL | Release train exists; Wiki evolution/lineage route incomplete | #118 |
| RO-15 | PARTIAL | Citation is explicitly pending release/availability | #55/#56 |
| RO-16 | PARTIAL | Banners and threats source exist; dedicated claim-linked route incomplete | #118 |
| RO-17 | PARTIAL | Executable semantic build linked; Wiki tutorial route untested | #118 |
| RO-18 | BOUNDED | 76-ID atlas, 37-property SVG and schema-checked diagram manifest; independent semantic/accessibility review pending | #118 |
| RO-19 | PENDING_PAGES | Source-bound WebVOWL viewer passes static CI and private desktop/mobile render smoke; combined/mobile readability and deployed Pages explorer absent | #117/#119 |
| RO-20 | BOUNDED | Wiki history and source manifest/read-back | #116 |
| RO-21 | PARTIAL | `p1-r2-documentation-quality-audit-2026-09-27.yaml` inventories 18 QN + 18 QL criteria; two mechanical Wiki ratings, no QN/QL totals or expert verdict | #118 |
| RO-22 | PARTIAL | Schema-checked composition manifest declares Research/Ontology primary, Data/Engineering secondary, other profiles N/A with triggers; full review pending | #118 |
| RO-23 | PARTIAL | Academic/engineering routes published in private Wiki Home at revision `9827a52`; source task/route audit recorded, target-reader validation pending | #118 |
| RO-24 | PARTIAL | Staged surface manifest at `docs/documentation/documentation-surfaces.yaml`; allocation and Pages checks remain false | #118 |
| RO-25 | PARTIAL | Authority stated in pages; implementation profile stale | #118 |
| RO-26 | PARTIAL | Pinned partial adoption YAML exists; capability evidence and QN/QL closure pending | #118 |
| RO-27 | PARTIAL | Seven REF seed identities; 2026-09-27 official landing-page review corrected RISKMAN to conference paper, checked four institutional links, and recorded three DOI resolver gaps. Manuscript placement, source coverage, DOI resolution and IEEE QA pending | #118/#53 |
| RO-28 | PARTIAL | Wiki candidate manifest and Pages registry; no release snapshot | #55/#118 |
| RO-29 | PARTIAL | FD/source QA and offline reference; final parity/reasoning gate open | #115/#117 |
| RO-30 | PARTIAL | Bounded task/route audit at `docs/documentation/p1-r2-dual-audience-route-audit-2026-09-27.md`; target-reader/mobile and Pages/WebVOWL usability checks pending | #118/#117/#119 |

**Count:** 7 BOUNDED, 21 PARTIAL, 0 GAP, 2 PENDING_PAGES. These are triage categories, not a weighted progress percentage. RO-27 has a bounded seed corpus and a dated source-identity check, but no complete/verified citation coverage; RO-30 has a source-level route audit but no target-reader usability result. RO-13 has a bounded reader route but not a complete decision/lineage record. PT-01…PT-10 and RW-01…RW-26 have provisional disposition in `docs/documentation/p1-r2-documentation-rollout-2026-09-26.md`; this does not pass RW-24.

**Governance refresh:** `.research/manifest.yaml` and `.research/ogcm-rf-profile.yaml` were refreshed on 2026-09-26 to replace the obsolete pre-Core/G2-pending narrative and pin the documentation profile ref. Semantic release is still `none`, OGCM overall conformance remains `not_assessed`, documentation adoption is `partial`, and Pages remains offline. Portfolio lifecycle ownership remains separate from OGCM documentation conformance.

**Critical path:** #116 Wiki bounded completion → #118 adoption/authority and missing reader routes; #115 exact formal description → #117 offline reference/render/access QA and #119 WebVOWL module-scope/usability review → #55/#56 publication identity/access → Pages public deployment and final conformance review. #51/#31/#53/#54 retain their evidence gates. A future documentation baseline must trigger read-back and drift checks. The WebVOWL offline candidate passes private desktop/mobile smoke at [run 36312545968](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312545968); no public deployment or reader usability pass follows from that check.

## Dated audit closure handoff — 2026-09-29

The 2026-09-26 triage above remains the historical baseline. #118's bounded **assessment/adoption gap audit** is now complete in `ogcm-rf-adoption-audit-closure-2026-09-29.md` and the 66-ID evidence map. The adopter remains `partial` and RO-07/RO-19 Pages capabilities remain pending. Newly focused #121 owns research journey/citation/quality gaps; #122 owns reader routes/tutorial/visual-access checks. #115/#117/#119 and #54/#55/#56 retain formal, Pages/viewer, assurance, release and access gates. RW-24 final conformance stays under #112. No public Pages link or all-green score follows from closing an audit issue.
