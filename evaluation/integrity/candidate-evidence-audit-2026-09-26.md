# Candidate evidence audit — 2026-09-26

Owners: #110, #111 and #113. Status: **verified bounded checkpoint; final assurance and publication binding remain open**.

## Candidate and inspected execution evidence

The audited pre-change candidate is `cd7cdedbb032596192f054d88a634fb95c29de52`.
`candidate-source-bindings-2026-09-26.csv` inventories all **419 tracked blobs** at that exact commit. Each comparison records Git blob identity, not a claim that every file was executed or scientifically validated. There are no deleted files relative to the three compared trees.

| Layer | Successful run | Inspected job | Exact checkout read from job log | Matching candidate blobs |
|---|---:|---:|---|---:|
| Semantic | 36145965757 | 108107100885 | `6e18964c3267a36fa4bef80ac8ed7e0419d32f37` | 393/419 |
| Relational/application | 36215963073 | 108331868986 | `ed76e7fc42d12a6a33bea9cab30bf453132b9ed4` | 418/419 |
| Manuscript claim guard | 36215839277 | 108331514044 | `6b30cfaf84eb5531b96ca9c641bc40feb2e2c61b` | 415/419 |

Both the run/job conclusions and checkout log lines were inspected. The semantic log contains the R1, R2 formal, R2 temporal-owner, R4, R5 and R7 PASS markers. The relational log contains R6 migration/governance/integrity, R3 governance/co-ownership, R5 identity, R7 case, data-load, E2E, P49 parity, negative-control and CQ governance PASS markers. The claim job contains both existing claim-guard PASS markers.

Run URLs:
- https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36145965757
- https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36215963073
- https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36215839277

## Dependency and change relevance

All **41/41 representative primary paths** in the existing R1–R8 ledger match both the inspected semantic and relational checkouts. This resolves inclusion/version ambiguity at these later runs; it does not turn a primary-path match into a scientific validation result.

The full-tree comparison strengthens the earlier primary-only checkpoint:

- Every ontology module, import catalog, shape, rule and tracked test fixture is unchanged from the semantic checkout. The semantic workflow and the test scripts it invokes are unchanged. The 26 later additions/changes are audit/narrative documents, manuscript/claim tables, formal-reference/Wiki documentation, and the new manuscript/figure tooling. They do not change the reasoner inputs. The complete changed set is recoverable from `semantic_blob_match=False` in the inventory.
- The relational checkout includes all current files except `docs/wiki/p1-r2-wiki-source-map-v0.1.md`; all relational schema/load/test sources, fixtures, migration and governance inputs are byte-identical. The Wiki map is not an input to its executed checks.
- The claim checkout differs only in the Wiki map, the figure notes/SVG and its generator. Its five checked manuscript/claim inputs and workflow are unchanged at the audited candidate. Figure-caption review and final publication binding remain separate.
- R2 #76 fixture changes are present in the later semantic and relational sources; R2 formal/rule and parity markers were observed. R2 #77 workflow coverage is present for push events, but inspection found the two R2 script paths missing from **pull_request** filters; this checkpoint repairs that asymmetry.
- R4→R5/R6 standards changes are present with the R4/R5 guards executed in the semantic run. This confirms the encoded governance checks, not missing clause/section correctness (#13).
- R6→R7 evidence-role changes are present with R6 governance and R7 case/domain checks. DS-002 remains a protected cross-domain stress candidate; no independent shortage holdout is inferred.
- R8 parity reconciliation uses the current eight-task CSV and the inspected P49 task execution. The newer #31 readiness CSV is documentary reconciliation; it does not execute E11.

The historical ledger and dated audits are preserved. Its 41 issue rows continue to distinguish simulated reviewer-originated remediation from independent human validation. Do not report “41 independently validated issues.” At this checkpoint **0/41 primary bindings require a blob recheck**; full publication-claim acceptance remains subject to manual relevance review and #54. No new global PASS_BOUNDED count is assigned to the entire 41-issue scientific scope.

## Executed repairs for #111 / #113

1. Reproduced two false negatives in the textual guard: an unrelated `not` or `not only` could suppress an affirmative overclaim. Restricted negation handling to bounded direct nonclaims and constrained nonclaim lists. Added three unsafe context fixtures and two safe negation fixtures; the baseline manuscript and prior seven unsafe controls still behave as intended.
2. Added `tools/paper1_vveaa_evidence_guard.py`. It checks all nine claim IDs, required denominators/methods/results/counterevidence/ceilings, VVEAA and E1–E11 vocabulary, current assessment states, repository-contained evidence paths, and actual Git blob hashes. Nine negative controls cover absent/duplicate claims, invented transfer PASS, missing adverse evidence, invalid layer/function, missing/wrong-hash evidence and escaping paths.
3. Replaced SR-CL03's indirect claim-table pointer with the actual EA capability/nonclaim evidence matrix and its existing blob SHA. The assessment remains PARTIAL.
4. Added VVEAA matrix, checker and evidence inputs to both claim workflow event filters, retained read-only repository permission, and added an exact-run JSON assessment/limitation artifact.
5. Added the two missing R2 test-script paths to the Semantic CI pull-request filter. Push and pull-request path lists now agree.

Local checks executed successfully:
- `python3 tools/author_review_claim_guard.py --selftest`
- `python3 tools/paper1_vveaa_evidence_guard.py --selftest --report /tmp/semrisk-vveaa-report.json`

The new checker detects integrity drift. Updating a hash or declared assessment does not establish evidence sufficiency. The textual checker has finite phrase coverage and cannot replace scientific reading of all headline locations. CI results for these **new changes** must be appended after the exact commit finishes; historical runs above are not reused as their test results.

## Remaining decisions and ownership

- #110: final issue-by-issue manual coverage/residual disposition and consumption by #54; this inventory/checkpoint is not the final scholarly reproducibility bundle.
- #111/#113: final candidate/run/release binding and #53/#54 integration; compare exact Commentium/CM4DI methods before attribution. Full natural-language claim adequacy remains a manual gate.
- #51: real reviewer responses absent. Simulated reviews do not satisfy this gate.
- #13/#14: source locator and closest-work extraction debt remains.
- #17/#31: DS-004 blocked; independent shortage-domain E11 unexecuted.
- #53/#54/#55: final claim calibration, integrated assurance and publication release remain OPEN.

No semantic model, dataset, expert judgment or transferability result was invented by this checkpoint.
