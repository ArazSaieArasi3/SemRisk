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
| RO-13 | GAP | No integrated reader-facing research journey/decision trace | #118 |
| RO-14 | PARTIAL | Release train exists; Wiki evolution/lineage route incomplete | #118 |
| RO-15 | PARTIAL | Citation is explicitly pending release/availability | #55/#56 |
| RO-16 | PARTIAL | Banners and threats source exist; dedicated claim-linked route incomplete | #118 |
| RO-17 | PARTIAL | Executable semantic build linked; Wiki tutorial route untested | #118 |
| RO-18 | BOUNDED | 76-ID atlas, 37-property SVG and scope statement | #116 |
| RO-19 | PENDING_PAGES | No deployed WIDOCO/equivalent Pages explorer | #117/#119 |
| RO-20 | BOUNDED | Wiki history and source manifest/read-back | #116 |
| RO-21 | PARTIAL | Hash/CI/read-back done; QN/QL conformance not assessed | #118 |
| RO-22 | GAP | Research + Data/Engineering profile declaration absent | #118 |
| RO-23 | GAP | Academic and engineer reader paths not explicit | #118 |
| RO-24 | GAP | No OGCM surface-allocation manifest found | #118 |
| RO-25 | PARTIAL | Authority stated in pages; implementation profile stale | #118 |
| RO-26 | GAP | No current documentation adoption/conformance record | #118 |
| RO-27 | GAP | No governed REF corpus contract/coverage evidence found | #118 |
| RO-28 | PARTIAL | Wiki candidate manifest and Pages registry; no release snapshot | #55/#118 |
| RO-29 | PARTIAL | FD/source QA and offline reference; final parity/reasoning gate open | #115/#117 |
| RO-30 | GAP | Dual-audience usability audit/route absent | #118 |

**Count:** 7 BOUNDED, 14 PARTIAL, 7 GAP, 2 PENDING_PAGES. These are triage categories, not a weighted progress percentage. RO-13/22–27/30 require actual adoption artifacts or evidence before closure. PT-01…PT-10 and RW-01…RW-26 remain to be dispositioned under #118; this table alone does not pass RW-24.

**Stale governance:** `.research/manifest.yaml` and `.research/ogcm-rf-profile.yaml` were last reviewed 2026-09-17 and still describe pre-Core G1/W2, absent canonical ontology/reasoner/SHACL and a framework ref `4f2615d`. They must be reconciled with the current P1-R2 candidate, CI, Wiki/Pages and pinned documentation profile without silently promoting semantic release or OGCM conformance. Portfolio lifecycle ownership remains separate from OGCM documentation conformance.

**Critical path:** #116 Wiki bounded completion → #118 adoption/authority and missing reader routes; #115 exact formal description → #117 offline reference/render/access QA → #119 WebVOWL explorer feasibility → #55/#56 publication identity/access → Pages public deployment and final conformance review. #51/#31/#53/#54 retain their evidence gates. A future documentation baseline must trigger read-back and drift checks.
