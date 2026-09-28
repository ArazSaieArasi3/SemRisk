# E10 claim-critical locator checkpoint v0.1

Date: 2026-09-28. Scope: #14/#31/#53; **partial source comparison**, not final E10 or publication assurance.

## What was replaced

The historical #22 matrix remains immutable: 12 rows × 17 dimensions = 204 cells, comprising 11 external rows (187 cells) and the older SemRisk self-row (17 cells). Its one repeated generic locator per comparator is not a feature-level citation.

- `semrisk-p1-r2-self-row-v0.1.csv` crosswalks `CELL-188…204` to 17 current P1-R2 dimensions, scoped results, exact repository `path@Git-blob-SHA` evidence and residuals. It **does not** claim that every dimension is validated: D06/D08/D09/D14/D17 remain PARTIAL; all others have bounded support with explicit ceilings. Three current Core/Enterprise/Pharma module blobs match the asserted-closure manifest.
- `claim-critical-external-locator-ledger-v0.1.csv` records **46** selected claim-critical publication/artifact locators: 5 COVER, 7 ROSE, 8 PA-006, 10 RiskHub and 8 RISKMAN cells within the historical 187 external cells, plus 4 PA-009 and 4 PH-003 locators outside that old 12-row snapshot. It preserves the legacy cell status separately from the new source-level judgement; it does not overwrite the old index or present these 46 as complete comparator saturation.
- The most consequential correction is `CELL-059 / CMP-004 / D08`. Historical status `not_in_scope` is contradicted by PA-006 §3, PDF P4: its scope explicitly includes an object such as a business process/model, assessor, intended goal, capability and control context. This is positive prior art for selected enterprise/goal/process links. It is not proof of full ArchiMate/TOGAF integration or exact equivalence to SemRisk's external-owner architecture.
- PA-009's exact printed pp. 157–162 and PH-003's PDF pp. 9–20 remain targeted additional comparators. The PH-003 Report→Shortage relationship is not an exact mapping to Risk Register Entry→Risk Event.

## Evidence and limits

COVER primary paper: `https://www.inf.ufes.br/~gguizzardi/ER2018-Risk.pdf`, §5 Figs. 2–5; formal source at pinned commit above. ROSE primary publication: DOI `10.1007/978-3-031-17995-2_26`; corrected formal source/erratum at pinned repository above. PA-006 primary article: `https://ceur-ws.org/Vol-4176/shields-2.pdf`, §3, Fig. 2 and equations (1)–(5), §§4–5.1, footnote 5. PA-009 primary article: `https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/ontological_analysis_and_redesign_of_risk_modeling_in_archimate_2018.pdf`, Figs. 5–10 and Tables 2–3. RiskHub primary article: `https://link.springer.com/article/10.1007/s43069-026-00666-7`, §§5–7, Figs. 7–17 and publisher supplementary F1. RISKMAN primary paper: `https://iccl.inf.tu-dresden.de/w/images/4/4a/Gorczyca-et-al2025supporting-risk-management-for-medical-devices-via-the-riskman-ontology-and-shapes.pdf`, Table 1/Figs. 1 and 4; exact OWL/SHACL sources at pinned commit below. PH-003 primary article: `https://publikationen.bibliothek.kit.edu/1000181579/159785046`, Tables 2–3/Fig. 4, §4 and data availability. The ledger specifies page and capability for each selected row. Published outcomes are authors' reports, not independent executions.

`tools/e10_locator_guard.py` checks exact 17-row self-ID/dimension crosswalk, controlled status, nonempty unit/ceiling, primary evidence bytes by Git blob SHA, 38 historical external cell/status mappings, unique audit IDs and the adverse `CELL-059` correction. Its self-test injects eight negative cases including invalid hashes, identities, statuses, missing limits and malformed CSV rows. A pass verifies ledger integrity, **not** the semantic judgement, article text, scientific novelty, expert validation or overall comparison.

## COVER and ROSE exact artifact checkpoint

COVER (SRC-ON-001) adds five old-cell locators (D02–D04, D13, D16) from the 2018 paper and pinned public `owl/cover.ttl` at commit `898a7d87d1da0f8c292620d966754a630ae3b57b` / blob `185064e68ac63b602bf97247da92e10b729a77fa` (Apache-2.0). ROSE (SRC-ON-002) adds seven (D02–D04, D06, D13, D16, D17) from the 2022 publication and corrected `owl/rose_gufo.owl` at commit `50ef107989d747a5d38cba1653c5309bff328048` / blob `63a522e452c5c15dcdc0bef0b013a8bd93bc5b71` (MIT). The repository README records the Intention characterization cardinality erratum. The OWL files support structural claims, while the papers support conceptual interpretations; no clean independent comparator run is claimed. Similar class names are not exact mappings.

## RiskHub publication-level checkpoint

RiskHub (SRC-PA-017) adds ten old-cell locators (D03–D05, D07–D08, D13–D17). The 2026 paper's §5.2 maps its conceptual model to 12 relational tables, §5.3 implements MySQL, §6.1 reports an exploratory panel of 12 academics, and §7 presents dashboard queries. This is substantial prior art for ontology-informed register/RDB design and human feedback. The publisher's F1 JPG is a high-resolution diagram; the cited 2021 thesis repository is a predecessor rather than the 2026 platform release. Exact 2026 executable/schema/data refs remain unknown, and no shared SQL↔SPARQL head-to-head task is claimed.

## RISKMAN formal artifact checkpoint

RISKMAN (SRC-ON-004) adds eight old-cell locators (D03–D04, D11–D14, D16–D17). The paper and release 1.0.0 formal artifacts distinguish analyzed/controlled risk with initial/residual levels, connect safe-design arguments to evidence and constrain medical-device risk documents through OWL EL plus SHACL. The exact commit `c046c5d1d5f13abc4241e6f7c0e48f0828df01df` binds ontology blob `aff89433467b60a78b7cf3f039b3fc2171629098` and shapes blob `befee38dbd478f7a90d54b9f058d4129f2010218` (ontology annotation CC BY 4.0). This is material formal/Health prior art; its device-safety context and published example are not an independent SemRisk Pharma transfer test or a shared execution benchmark.

## Publication crossfeed

SR-CL02–SR-CL05, SR-CL07 and SR-CL08 rows in `publications/2026-icae/claim-calibration-preliminary-v0.1.csv` and `author-review-claim-evidence-v0.2.csv` now record PA-006/PA-009/RiskHub/RISKMAN counterevidence and the corrected CELL-059 interpretation. The working manuscript's Related Work states this explicitly. The publication claim guard passes on this textual update, but final citations, comparator saturation, semantic review and release assurance remain pending.

## Next source-work boundary

Remaining: the other **149/187** historical external cells still lack this exact-locator treatment, although not all 149 are claim-critical. Prioritize the claim-bearing D03–D05 and D13–D16 units for the Oliveira risk-ontology programme, RisKG and the Pharma ontology lineage; apply a documented N-A/UNKNOWN status where material source text cannot support a positive judgment. Then re-evaluate the E10 shortlist against the exact #55 publication candidate and synthesize SR-CL03/05/07 without feature-count scoring. #14 and #31 remain OPEN.
