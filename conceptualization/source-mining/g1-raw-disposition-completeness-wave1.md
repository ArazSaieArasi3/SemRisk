# G1 Raw-Item Disposition Completeness — Reconciliation Wave 1

**Date:** 2026-09-22

## Governed raw extraction baseline
- Raw/source candidate rows currently in the five mined source families: **274**.
- Source distribution: SRC-PH-001 66; SRC-PA-001 31; SRC-OP-001 121; SRC-PH-005 34; SRC-PH-004 22.
- Current semantic dispositions: 145 `CANDIDATE`, 89 `PROFILE_OR_MAPPING`, 24 `METHOD_PROFILE`, 10 `DATA_OR_PRODUCT`, 5 `DATA_ONLY`, 1 `DESIGN_INPUT`.
- Follow-up flags: 257 `RECONCILE_BEFORE_CANONICAL`, 8 `CM_PHARME_MAPPING_REQUIRED`, 3 `ROSE_ALIGNMENT_REQUIRED`, 2 `COVER_ALIGNMENT_REQUIRED`, 3 `METHOD_COMPARISON_INPUT`, 1 `DATASET_QUALIFICATION_REQUIRED`.

## Wave-1 result
Fifteen cross-source reconciliation clusters now cover the highest-risk identity/conflict areas for Paper 1: Risk vs record, scenario/event, assessment/result, inherent/residual, risk/workflow state, owner/role, control/treatment, evidence/provenance, causation/correlation, scales, taxonomy, enterprise goals/capabilities, Pharma ownership, and threat/opportunity polarity.

## Important limitation
This is **not yet full 274-row final disposition**. Wave 1 resolves the semantic backbone and establishes routing rules. The remaining raw rows still require row-level mapping to one reconciliation cluster, profile/method/data disposition, or explicit defer/reject decision before G1 can PASS.

## Gate effect
Major hidden Core-identity conflicts are now explicit rather than implicit. G1 remains open until row-level coverage and source-delta completeness are finished.