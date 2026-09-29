# Paper-1 E10 source-result → claim-calibration handoff

**Owner:** #53. **Evidence state:** bounded source comparison, not final assurance. **Target:** P1-R2/0.1.0-rc.1. **Source baseline:** #14 handoff at `41053cd5d82c7a11f88b31deb95f2de8b77e77a0`; seven-unit #31 result at `cf96d17ce73957ae2e2a65fcd56f76f1ac26a6ce`. The exact unit-to-source audit IDs and current SemRisk cells are in `evaluation/e10/claim-unit-source-comparison-v0.1.csv`; the current self row and 93 selected external locators are controlled by the E10 guard.

The historical #22 matrix has 187 external cells plus 17 SemRisk cells. Only 71 historical external cells have been selected for exact-locator conversion; 22 additional source locators lie outside that original matrix. The 116 other historical external cells retain generic locators and cannot be used to prove missing capabilities. These denominators are evidence coverage, not a comparative score.

| Claim | E10 units and adverse evidence | Current #53 calibration consequence |
| --- | --- | --- |
| SR-CL01 | U01–U03: COVER/ROSE/Oliveira/PA-006 and IOF already distinguish selected event/scenario/assessment concerns; NIST has record/detail and reassessment fields. | Keep `supported_with_narrower_scope` for the implemented P1-R2 distinctions. No first process/result or semantic-validation claim. |
| SR-CL02 | U04: RiskHub, RisKG and NIST already cover selected register, owner and operational links. | Keep `supported_with_narrower_scope` for 27 governed schema dispositions; no 100% correctness or generic register novelty. |
| SR-CL03 | U04: EA/process/goal and owner prior art; SemRisk generic external owner and full EA path remain unbound. | Keep `partially_supported`; describe selected external-ownership and control links only. |
| SR-CL04 | U05: PA-010/RisKG/RiskHub prior graph and RDB execution; no shared parity benchmark. | Keep `supported_with_narrower_scope` for 8/8 frozen SemRisk task pairs, no global/lossless equivalence or peer advantage. |
| SR-CL05 | U02/U06: PH-008/011, IOF, MedSupplyKG and RISKMAN prior art; one constructed Pharma case plus synthetic extension. | Keep `supported_with_narrower_scope`; no first Pharma ontology/process-result/shortage-report claim or Pharma validation. |
| SR-CL06 | U06: no clean independent shortage-domain holdout. | Keep `insufficient_evidence` for transferability; state bounded cross-context applicability only. |
| SR-CL07 | U01–U07: overlap, AIRO residual-risk semantic conflict, RiskHub human-feedback strength, 116 generic historical cells and no head-to-head. | Keep `partially_supported/provisional`. Describe an observed integrated P1-R2 pattern; exclusivity, overall winner and measured superiority remain `NOT_ASSESSED`. |
| SR-CL08 | U07: comparator formal artifacts exist, including OWL/SHACL. | Keep `supported_as_worded` only for exact formal-consistency scope; no generic first formal risk ontology. |
| SR-CL09 | U07: public formal peers exist and SemRisk private Jira bytes restrict full public reconstruction. | Keep `supported_with_narrower_scope` for public/synthetic CI reconstruction with access limits; no reproducibility ranking. |

**Manuscript consequence.** The author-review draft now acknowledges the seven-unit source result in Related Work, Results and the VVEAA table. Prior-art overlap and the absence of a common task are visible beside the SemRisk task result. The 2026-09-24 preliminary report retains its historical text and carries a dated correction; its CSV row SR-CL07 contains the current provisional wording.

**Remaining gates.** #51/#30 real human semantic evidence is still missing; #31 E11 independent shortage robustness has not executed; #13 standards locators and a current source refresh remain; #53 final judgment and #54/#55 release-bound assurance follow. A genuinely common comparator task may be executed only with exact shared inputs and permission; otherwise keep `NOT_ASSESSED`. None of these gates is silently counted as success.
