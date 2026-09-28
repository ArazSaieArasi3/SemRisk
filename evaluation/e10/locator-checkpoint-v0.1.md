# E10 claim-critical locator checkpoint v0.1

Date: 2026-09-28. Scope: #14/#31/#53; **partial source comparison**, not final E10 or publication assurance.

## What was replaced

The historical #22 matrix remains immutable: 12 rows × 17 dimensions = 204 cells, comprising 11 external rows (187 cells) and the older SemRisk self-row (17 cells). Its one repeated generic locator per comparator is not a feature-level citation.

- `semrisk-p1-r2-self-row-v0.1.csv` crosswalks `CELL-188…204` to 17 current P1-R2 dimensions, scoped results, exact repository `path@Git-blob-SHA` evidence and residuals. It **does not** claim that every dimension is validated: D06/D08/D09/D14/D17 remain PARTIAL; all others have bounded support with explicit ceilings. Three current Core/Enterprise/Pharma module blobs match the asserted-closure manifest.
- `claim-critical-external-locator-ledger-v0.1.csv` records **16** claim-critical publication-level locators: eight PA-006 cells within the historical 187 external cells, four PA-009 and four PH-003 locators outside that old 12-row snapshot. It preserves the legacy cell status separately from the new source-level judgement; it does not overwrite the old index or present these 16 as complete comparator saturation.
- The most consequential correction is `CELL-059 / CMP-004 / D08`. Historical status `not_in_scope` is contradicted by PA-006 §3, PDF P4: its scope explicitly includes an object such as a business process/model, assessor, intended goal, capability and control context. This is positive prior art for selected enterprise/goal/process links. It is not proof of full ArchiMate/TOGAF integration or exact equivalence to SemRisk's external-owner architecture.
- PA-009's exact printed pp. 157–162 and PH-003's PDF pp. 9–20 remain targeted additional comparators. The PH-003 Report→Shortage relationship is not an exact mapping to Risk Register Entry→Risk Event.

## Evidence and limits

PA-006 primary article: `https://ceur-ws.org/Vol-4176/shields-2.pdf`, §3, Fig. 2 and equations (1)–(5), §§4–5.1, footnote 5. PA-009 primary article: `https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/ontological_analysis_and_redesign_of_risk_modeling_in_archimate_2018.pdf`, Figs. 5–10 and Tables 2–3. PH-003 primary article: `https://publikationen.bibliothek.kit.edu/1000181579/159785046`, Tables 2–3/Fig. 4, §4 and data availability. The ledger specifies page and capability for each selected row. Published outcomes are authors' reports, not independent executions.

`tools/e10_locator_guard.py` checks exact 17-row self-ID/dimension crosswalk, controlled status, nonempty unit/ceiling, primary evidence bytes by Git blob SHA, eight historical external cell/status mappings, unique audit IDs and the adverse `CELL-059` correction. Its self-test injects invalid hashes, identities, statuses and missing limits. A pass verifies ledger integrity, **not** the semantic judgement, article text, scientific novelty, expert validation or overall comparison.

## Publication crossfeed

SR-CL03 and SR-CL07 rows in `publications/2026-icae/claim-calibration-preliminary-v0.1.csv` and `author-review-claim-evidence-v0.2.csv` now record PA-006/PA-009 counterevidence and the corrected CELL-059 interpretation. The working manuscript's Related Work states this explicitly. The publication claim guard passes on this textual update, but final citations, comparator saturation, semantic review and release assurance remain pending.

## Next source-work boundary

Remaining: the other **179/187** historical external cells still lack this exact-locator treatment, although not all 179 are claim-critical. Prioritize the claim-bearing D03–D05 and D13–D16 units for COVER/ROSE, RiskHub/RisKG and the Pharma ontology lineage; apply a documented N-A/UNKNOWN status where material source text cannot support a positive judgment. Then re-evaluate the E10 shortlist against the exact #55 publication candidate and synthesize SR-CL03/05/07 without feature-count scoring. #14 and #31 remain OPEN.
