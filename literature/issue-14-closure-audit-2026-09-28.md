# Issue #14 closure audit — bounded closest-work evidence

Date: 2026-09-28. Decision: **OPEN / MATERIAL PROGRESS**. This audits #14 against its own acceptance criteria; it does not treat the earlier #40 search stop or the new E10 shortlist as a completed comparative evaluation. Exact current source refs are in `conceptualization/source-mining/source-register.csv`, `literature/ontology-artifact-binding-registry.csv` and comparator profiles.

| #14 criterion | Current disposition | Evidence / remaining work |
| --- | --- | --- |
| Scientific closeness rather than citation count | MET for bounded Paper-1 shortlist | `paper1-comparator-shortlist-e10-v0.1.md` includes strong counterexamples: COVER/ROSE, PA-009, propagation lineage, RisKG/RiskHub, NIST and Pharma lineages. |
| Publication and implementation version linkage | PARTIAL | COVER/ROSE, AIRO, RISKMAN, IOF, RisKG and several others have pinned refs. PA-006 matching coauthor-associated prototype commit `76cf94d` is bound, but the paper's PURL redirect to that repository is unverified; PA-010 source code and PH-008/009/011 OWL assets remain unknown; RiskHub 2026 executable is unknown. |
| Every material judgment source-backed or UNKNOWN | PARTIAL | The E10 locator ledger now has 30/187 historical external cells with selected exact publication/formal-artifact locators (COVER 5, ROSE 7, PA-006 8, RiskHub 10), plus 8 targeted locators outside the historical index (PA-009 4, PH-003 4). These are selected units, not complete source saturation. Remaining 157 historical cells and conditional comparators still require material-claim locator/reuse audit. |
| Missing documentation not treated as capability absence | MET | `UNKNOWN/NOT_REPORTED` controls in queue and shortlist; no negative capability inference from missing artifact. |
| No lexical-only equivalence | MET in bounded E10 contract | Shortlist requires exact semantic relation and separates lexical/structural/semantic/instance evidence; downstream #21 mapping decisions must preserve this. |
| License/version/dependency implications | PARTIAL | Pinned licenses for central formal assets; PA-006 repository CC BY-NC-SA 4.0 differs from CEUR article CC BY 4.0. Open Risk member reuse and some Pharma artifact licenses are unresolved. |
| Current search and stopping | MET for Paper-1 bounded search | #40 final stopping decision; `saturation-stopping-registry.csv` records deferred/conditional tails and reopening triggers. |
| Strengths, criticism, negative evidence | PARTIAL | Deep profiles preserve PA-009 assessment semantics, PA-006 richer query model, RisKG/RiskHub operational implementations, RISKMAN OWL+SHACL. Final E10 output still must compare observed units at a release ref and retain contrary outcomes. |
| Novelty claims may be reduced | MET as a constraint, outcome pending | #53 comments and shortlist remove generic ontology+propagation, EA-risk redesign, register→KG/RDB and first Pharma-risk-ontology claims. Actual integrated-chain superiority remains unproven. |

## Stop/next rule

#14 can close when a reviewer can inspect all **material** closest-work profiles at the unit of each Paper-1 claim, every unresolved implementation is either pinned or explicitly bounded in the final E10 handoff, license/dependency consequences are audited, and the comparison has a source-locator-to-claim trace. An independent run is required only for a *reproduction* claim; it is not a prerequisite to cite the publication as prior art. Do not let #14 closure assert #31 E10 execution, #51 real expert evidence or #55 release.

Next focus: resolve the PA-006 PURL redirect or keep author-associated ref distinct; finish PA-010 code availability and Pharma OWL artifact disposition; audit comparator matrix rows for missing locators/reuse decision. #15 separately owns source-complete Pharma extraction; PH-012 publisher abstract is bounded and cannot supply section-level claims.
