# SemRisk R1–R8 simulated expert Meta-Review — 2026-09-25

**Status:** completed cross-role synthesis and remediation re-audit; **Paper-1 submission gate: NOT READY**.  
**Nature:** specialist-style *simulated* adversarial review. This is not independent human expert validation, certification, or a substitute for #51.  
**Snapshot:** current repository evidence after R8/#109 closure. This document is an evidence-index and claim decision, not a claim that all source code or all GitHub run logs were independently rerun here.

## Method and disposition

For each role, inspect its remediation acceptance audit, issue closure range, reported executable check and residual boundary. Treat a closed remediation as a **bounded fix**, not as clearance of the parent's evaluation or publication gate. Reconcile cross-role overlaps by assigning one authoritative owner to each residual finding. Preserve negative, partial and inaccessible evidence. Do not infer global correctness from CI green or reviewer-style scores.

| Role | Closed corrective issues | Audited evidence | Surviving boundary |
|---|---|---|---|
| R1 Foundational | #69–#72 (4) | `docs/governance/r1-remediation-acceptance-audit-2026-09-24.md`; semantic/relational guards | Derived Risk pattern, Risk State, responsibility and PROV-O remain bounded; no universal metaphysical validity |
| R2 OWL/SHACL/KR | #73–#78 (6) | `docs/governance/r2-remediation-acceptance-audit-2026-09-24.md`; OWL 2 DL, HermiT, negative and fixture guards | SHACL/profile checks are not OWL entailments; historical 6+2 parity superseded by R6 8/8 |
| R3 ERM/GRC | #79–#84 (6) | `docs/governance/r3-remediation-acceptance-audit-2026-09-25.md`; co-ownership and governance markers | 27/27 is selected Jira schema disposition, not ERM completeness; no control effectiveness or advanced ERM |
| R4 Standards | #85–#90 (6) | `docs/governance/r4-remediation-acceptance-audit-2026-09-25.md`; version/mapping/claim guard | #13 source locators and detailed mappings remain open; alignment is not conformance |
| R5 EA/Business | #91–#96 (6) | `docs/governance/r5-remediation-acceptance-audit-2026-09-25.md`; external identity/dependency guards | generic external family unbound; no EA causality or full architecture propagation |
| R6 Data/KG | #97–#102 (6) | `docs/governance/r6-remediation-acceptance-audit-2026-09-25.md`; migration, integrity, lineage and parity guards | 8/8 direct equivalence only for frozen eight tasks (17 directly represented CQs); not global OWL↔RDB equivalence |
| R7 Pharma/Health | #103–#108 (6) | `docs/governance/r7-remediation-acceptance-audit-2026-09-25.md`; constructed/synthetic guards | DS-004 activation BLOCKED, DS-002 unopened, no independent shortage-domain holdout |
| R8 Method | #109 (1) | `evaluation/integrity/r8-simulated-method-review-2026-09-25.md`; dated parity addenda and documented CI | 18/18 questions reviewed; #51, E11, #13/#14 and final claim/assurance decisions remain open |

**Count: 41 closed reviewer-originated corrective issues (4 + 6 + 6 + 6 + 6 + 6 + 6 + 1).** This count is about remediation issue dispositions, not expert agreement, study validity or readiness to submit.

### Remediation re-audit: what passed and what was not tested

1. **Concept identity/semantic categories (R1↔R2↔R6):** R1 contracts and R2 axioms/guards preserved Risk vs Assessment Result, situational Risk State and qualified owner derivation; R6 rejects cross-risk history/cycles and identity-erasing SQL normalization. Evidence supports bounded structural consistency and the named regression families. It does not establish domain truth, universal identity criteria or full temporal semantics.
2. **Governance/control/standards (R3↔R4):** Co-ownership passes with two current owners; source-specific workflow labels, proposed treatments, control mechanisms, appetite/tolerance and standards mapping strength have guarded boundaries. Control presence does not prove effectiveness; selected 27 fields and bounded NIST/ICH alignment do not prove comprehensive ERM or conformance. #13 still owns locator depth.
3. **Federation/external identity (R2↔R5↔R7):** Local Core excludes external EA/Pharma concepts; owner-qualified IDs preserve same-label/different-owner entities; Pharma terminology gaps remain explicit. The generic EA owner remains UNBOUND_EXTERNAL_FAMILY and structured Pharma file activation remains blocked. No lexical synonym or SKOS link authorizes OWL identity.
4. **Data and evaluation roles (R6↔R7↔R8):** Staging lineage/role compatibility and constructed-vs-synthetic guards pass on governed fixtures; R8 corrected stale parity text. This supports deterministic application testing, not independent validation, causal effectiveness or independent transfer. DS-003 and Jira influenced design; E11 cannot treat them as clean holdouts.
5. **CI evidence ceiling:** Acceptance audits report successful runs and markers, including R7 semantic 36145965757 and relational 36145811696, R6 relational 36123602513, and #109 documentation-linked run 36156336036. This meta-review inspected their repository audit records, not the raw log of every historical run. Recheck exact candidate/CI markers before #54/#55 binding.

### Cross-role conflicts and their resolution

| Apparent conflict | Meta-review resolution | Owner |
|---|---|---|
| R2 historical parity 6 direct + 2 normalized versus R6 current 8 direct | Both are true for different evaluated revisions. Quote 8/8 for the current frozen tasks with date/ref; preserve history and eight-task denominator. | #53, #55 |
| R3 co-ownership versus singular “Risk Owner” wording | Role permits concurrent assignments; never infer one canonical unique owner. | #53 |
| R3 treatment/control versus R7 Pharma transparency response | Source-specific transparency remains a response candidate, not automatically treatment/control or effective intervention. | #28, #53 |
| R4 standards alignment versus R5 external EA owner | TOGAF/ArchiMate are reference/alignment sources, not a canonical external ontology owner; #13 resolves missing locator strength. | #13, #53 |
| R6 executable application versus R8 independent transfer | SQL/RDF parity and E2E fixtures test implementation; they do not turn design-used data into independent evidence. | #31, #53, #56 |
| R1–R8 simulated critique versus real expert validation | Simulated critiques are methodological stress tests. Human response collection/adjudication belongs exclusively to #51/#30. | #51, #30 |

## Consolidated findings and actions

| ID / severity | Decision and concrete next action | Existing owner or new action | Submission implication |
|---|---|---|---|
| MR-01 / Blocker | Recruit eligible independent specialists, collect real answers using frozen EV-PACK-1.0, report disagreement/negative evidence and adjudicate claims. Never relabel simulated R1–R8 as human validation. | #51 → #30 → #53 | Expert-validated claim blocked until completed; otherwise remove/narrow claim |
| MR-02 / High | Choose a genuinely independent, predeclared test with role/contamination audit for E11; if no valid shortage holdout is available, reword RQ3/SR-CL06 as bounded application/federation and mark transfer untested. DS-002 FAERS cannot serve as shortage holdout. | #31 → #53/#56 | Independent transfer claim blocked |
| MR-03 / High | Complete closest-work artifact/source tail and E10, and exact accessible standards/EA locators; log inaccessible sources and restrict novelty/conformance wording. | #14, #13, #31 → #53 | Strong novelty and standards claims blocked |
| MR-04 / High | Make a machine-checkable claim matrix for every Abstract/Results/Conclusion headline statement, binding claim, evidence role, exact release, denominator, nonclaim, owner and CI trigger; fail on forbidden generalization or stale parity. | New cross-role claim-control issue | #53/#54 cannot freeze unsupported wording |
| MR-05 / Medium | Reconcile all 41 reviewer-originated issues against audit row, exact artifact/ref, relevant run marker, changed-since-test status, and surviving limit. Repair the R2 audit's “five” versus six issue count, and record any weak or unverified link without hiding it. | New remediation-ledger issue | #54 must consume a consistent ledger |
| MR-06 / High | Bind the final evaluated candidate, human/independent evidence decisions, threats, negative results, and licensed/private access limits before assurance and scholarly release. | #53 → #54 → #55 → #56 → #35 | Submission remains blocked on unmet gates |

### Execution order and gate

1. Build MR-05 ledger and reconcile historical correction, then MR-04 claim checks against the current manuscript/claim register. These are author-controlled now.
2. Continue #13/#14/E10 and predeclare E11 protocol (#31) without using design evidence as a holdout; implement or explicitly narrow the independent transfer claim.
3. Execute real #51 reviewer protocol and resolve #30; negative judgments can reopen R1–R7 remediations.
4. Recalibrate #53 and #56, assess exact candidate #54, freeze #55, audit #35. A failed human/independent finding must not be averaged out by CI PASS.

**Meta-review verdict:** reviewer-originated bounded remediations are internally coherent on the inspected audit evidence; two new cross-role maintenance actions are warranted. Paper 1 remains **MAJOR REVISION / NOT SUBMISSION READY** for its current stronger expert-validation, independent-transfer, novelty and standards claims. The bounded architecture, selected schema mapping, task parity and constructed Pharma application may be reported with exact scope and release identity. No post-review change may silently inherit a historical PASS.
