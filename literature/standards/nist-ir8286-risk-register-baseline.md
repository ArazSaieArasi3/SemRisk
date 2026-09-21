# NIST IR 8286 Current Risk-Register Semantic Baseline

**Primary governed sources:** SRC-ST-007, SRC-ST-008, SRC-ST-009  
**Current editions:** NIST IR 8286 Rev.1 (Dec 2025), IR 8286A Rev.1 (Dec 2025), IR 8286B Updated 1 (Feb 2025)  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — current official versions and central register/RDR semantics inspected; full clause-by-clause standards extraction remains open under #13.

## 1. Risk Register as information artifact

NIST explicitly treats the cybersecurity risk register as the document/repository for recording and sharing information about risks. This is strong authoritative evidence that a Risk Register is an information-management artifact and should not be ontologically identified with the risk phenomenon itself.

## 2. Snapshot + iterative lifecycle

NIST states that a register represents risks at a single point in time but must be used consistently and iteratively. As responses are applied, an updated state becomes the new current state in the next assessment cycle.

SemRisk implication:
- preserve time-indexed assessment/state history;
- do not equate one register-row snapshot with timeless Risk identity;
- distinguish state of assessed risk from workflow state of the record.

## 3. Current notional register fields

NIST IR 8286A Rev.1 presents a notional register including:
- ID;
- Priority;
- Risk Description;
- Risk Category;
- Current Assessment: Likelihood, Impact, Exposure Rating;
- Risk Response Type;
- Risk Response Cost;
- Risk Response Description;
- Risk Owner;
- Status.

These are authoritative operational-schema evidence, not automatic ontology classes.

## 4. Risk Detail Record

NIST distinguishes the compact register from a richer Risk Detail Record (RDR). The RDR can preserve:
- historical risk-related information;
- detailed risk-analysis data;
- individual/organizational accountability;
- additional information that does not fit in the compact register.

This strongly reinforces SemRisk's candidate separation among:
- Risk Register Entry;
- assessment/results;
- evidence/history;
- responsibility/accountability.

## 5. Scenario construction

NIST IR 8286A Rev.1 describes risk identification using combined inputs such as:
- enterprise asset/objective context;
- threats;
- vulnerabilities/predisposing conditions;
- adverse/positive impacts;
assembled into risk scenarios recorded in the Risk Description.

SemRisk implication: a Risk Description or Scenario Description is an information representation of possible events/conditions and should not be equated automatically with the event itself.

## 6. Enterprise aggregation

System/organizational cybersecurity risk registers can be aggregated into an enterprise cybersecurity risk register and then into broader enterprise risk registers/risk profiles.

SemRisk implication:
- aggregation/projection is operational prior art;
- enterprise register integration is not novelty by itself;
- scope/context and source-record lineage must be preserved.

## 7. Assessment and response lifecycle

The current NIST series separates identification/analysis from prioritization/response. IR 8286B adds risk priority and response information. This supports modeling:
- Assessment Activity/Result;
- prioritization/evaluation decisions;
- Response/Treatment decisions;
- monitoring/reassessment cycles;
as distinct but linked management artifacts/activities.

## 8. Novelty consequence

SemRisk cannot claim novelty for:
- maintaining a risk register;
- current-assessment fields;
- risk owner/status/response fields;
- risk-detail/history records;
- register aggregation to enterprise level;
- iterative update/reassessment.

The candidate SemRisk contribution remains ontological disambiguation and governed traceability across these operational constructs.

## 9. Downstream routing

- #13 standards/framework mining;
- #18 G1 reconciliation;
- #19 UL/conflict registry;
- #20 state/lifecycle registry;
- #22 standards crosswalk;
- #45/#46 RDB projection;
- #53 claim calibration.

## 10. Remaining #13 debt

- exact clause/section locator extraction for all central definitions;
- supplemental JSON/XLSX schema field-level extraction;
- IR 8286B response/prioritization field mining;
- edition-lineage comparison with superseded 2020/2021/2022 versions;
- mapping semantics classified as exact/near/broader/narrower/related/operationalizes.