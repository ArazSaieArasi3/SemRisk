# #3 Core Concept Inventory v0.1 — Handoff Contract

**Date:** 2026-09-22

## To #20 — relations/events/states
- Use `core-concept-registry-v0.1.csv` semantic IDs as participant candidates; do not mint duplicate noun concepts to make relations convenient.
- Resolve causal/source/condition/trigger/event/consequence, assessment lifecycle, treatment/control, ownership/responsibility, evidence/provenance and temporal/state patterns.
- Preserve Risk State vs Workflow State and Assessment Activity vs Result invariants.
- Any proposed relation that requires a new concept must trace back to G1/#7 evidence and update #3 under change control.

## To #21 — reuse/alignment
- Prioritize exact decisions for COVER Risk/value patterns, ROSE Control/Security Mechanism/Vulnerability patterns, PROV-O provenance, RISKMAN Health concepts and OpenPVSignal profile semantics.
- Concepts marked `ALIGN_EXTERNAL_BEFORE_NEW`, `ALIGN_AND_REFINE`, `REUSE_ALIGN` or `EXTERNAL_OWNER` may not be called novel until #21 is complete.

## To #25 — foundationalization
- Resolve candidate categories for Risk, Risk Subject, Predisposing Condition, Trigger, Risk Scenario, Risk Event, Consequence, Vulnerability, Risk Assessment Activity/Result, Risk State, Risk Responsibility and information artifacts.
- Preserve information artifact vs event/activity/state distinctions from G1/UL/CQs.

## To #24 — G2 architecture gate
G2 must review the Core/Profile/External ownership matrix, unresolved conflict register and #20/#21/#25 outputs. HIGH unresolved items marked `blocks_g2_if_unresolved=YES` prevent affected G2 PASS.

## Stability
`SR-CPT-*` IDs are stable provisional semantic IDs for W2. #43 may mint final IRIs/IDs, but label changes must preserve migration lineage.