# E10 claim-unit source comparison — bounded P1-R2 candidate v0.1

Date: 2026-09-28. Owner: #31. Candidate: P1-R2/0.1.0-rc.1 with source/manifests linked through `evaluation/e10/semrisk-p1-r2-self-row-v0.1.csv`. Closest-work source package: #14 closed at commit `41053cd5d82c7a11f88b31deb95f2de8b77e77a0`, `literature/issue-14-claim-source-reuse-handoff-v0.1.md`. This report and `claim-unit-source-comparison-v0.1.csv` are a **source-level comparative result**, not an independent comparator software rerun, final #55 release comparison, or proof that a complete chain is unique.

## Method and denominators

Seven claim units are drawn from the Paper-1 contribution and claim register. For each unit the CSV names the common semantic/operational question, selected comparator source IDs, exact external ledger audit IDs, exact current SemRisk self-cell IDs, positive prior-art evidence, SemRisk's observed source/task result, an explicit adverse/unassessed ceiling and a next action. The selected locator ledger has 93 units (71 from 187 historical external cells; 22 added sources outside that denominator). The unconverted 116 historical cells retain generic locators and cannot count as negative evidence or an E10 success denominator. No feature totals, weights, ranking or winner were computed.

Source-level means inspecting publications/formal assets and the P1-R2 bound source/result manifests; reported results are attributed to their authors. Only SemRisk's own declared selected E8/E9 tasks were executed in this repository. Where the systems have no shared dataset, task, artifact or ontological identity criterion, the head-to-head state is `NOT_ASSESSED`, even if one has publicly available code and another does not.

## Result by claim unit

| Unit | Finding | Claim consequence |
| --- | --- | --- |
| E10-U01: phenomenon/event/scenario/record | COVER/ROSE/Oliveira/PA-006 already distinguish event/type/scenario concerns; NIST and MedSupplyKG distinguish record/detail or report/shortage information objects. SemRisk's explicit four-way P1-R2 class pattern is observed in its source and selected negative test. | SR-CL01 can describe its implemented selected pattern. SR-CL07 integrated distinctiveness remains provisional; no class absence is inferred for peers. |
| E10-U02: assessment/result/residual | IOF has formal RiskAssessmentProcess→RiskAssessmentResult and residual estimate after reduction; RisKG has rating nodes; NIST documents current/post-response assessments. AIRO's `hasResidualRisk` relates Risk→Risk rather than SemRisk contextual results. | Remove any standalone first activity/result claim. Record AIRO as semantic conflict requiring #21 alignment, not as an error or inferior model. |
| E10-U03: risk/workflow state and reassessment | RiskHub/NIST operational status, IOF review, and PA-006 lineage queries are relevant prior art; SemRisk's state split and supersession are source/test observed on selected synthetic fixtures. | Descriptive difference, not a proof of unique state ontology or longitudinal utility. |
| E10-U04: enterprise links/ownership | PA-009 EA risk, PA-006 process/goal/capability, RisKG/RiskHub project/function/owner and NIST RDR owner/business unit are strong prior art. | SR-CL03 remains partial: selected external-owner/responsibility links exist, general EA path/conformance unbound. |
| E10-U05: execution/projection | PA-010 OWL→Neo4j/Python, RisKG register→KG, RiskHub register→12-table MySQL/dashboard, RISKMAN OWL+SHACL all predate generic formal/operational execution. SemRisk 8/8 frozen SQL↔SPARQL pairs hold after R6. | Report only SemRisk task-bounded parity. No common task or superiority verdict over conceptually different external systems. |
| E10-U06: Pharma | PH-011/008, IOF, RISKMAN and MedSupplyKG establish medicines/Health risk ontology, assessment/result, treatment and shortage graph prior art. | SR-CL05 stays a constructed bounded CM-PharmE federation, not a first Pharma ontology; SR-CL06 independent transfer remains insufficient. |
| E10-U07: formal/reproducibility | COVER/ROSE/AIRO/RISKMAN/IOF have pinned formal assets; RiskHub reports 12-academic feedback. SemRisk E9 public/synthetic clean CI is bounded by private Jira data. | No overall reproducibility ranking; #51 real SemRisk reviewers and final #55 release are pending. |

## Adverse evidence and publication handoff

The #53 preliminary calibration and working manuscript have already been narrowed to include IOF, NIST, AIRO, RisKG/RiskHub and Pharma counterexamples. The VVEAA results table now labels E10 as source-level bounded. The exact current candidate is formally checked, but semantic validity, exclusive novelty, head-to-head measured utility and independent transferability remain unproven.

Next E10 gate: freeze #55 release/ref and rerun current SemRisk rows/guards, reconcile the final #53 prose against the seven units, and either execute a genuinely common comparator task with permission and exact inputs or retain `NOT_ASSESSED`. E11 DS-004 file-level shortage robustness is blocked by version/license/files/checksums/schema; DS-002 record-level FAERS stress remains protected/unopened, and it is a different domain task. #31 cannot close from this source comparison alone.
