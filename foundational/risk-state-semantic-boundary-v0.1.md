# SemRisk Risk State Semantic Boundary v0.1

**Owner:** Issue #70  
**Status:** FROZEN_POLICY

## Core meaning
`Risk State` (SR-CPT-035) is reserved for a **time- and context-bound state-of-affairs concerning the governed Risk context**. It is modeled as a Situation.

It is not:
- a Risk Register workflow status;
- an administrative processing state;
- a management attention/escalation classification;
- an assessment result or risk rating;
- a monitoring task/status;
- evidence of treatment effectiveness.

## Separate state/representation families
1. **Risk State:** real-world/situational state-of-affairs concerning the Risk context.
2. **Assessment Result:** information/assertion about the Risk under a method/time/evidence context.
3. **Workflow State:** state of the managed record/workflow.
4. **Management/Monitoring classification:** if later required, belongs in an Enterprise/Governance profile and MUST NOT be silently encoded as Core Risk State.

## Paper-1 fixture rule
The E2E synthetic fixture may instantiate Risk State only with labels/descriptions that denote synthetic situational context. It must not use management/workflow labels such as:
`open`, `closed`, `analyzed`, `treated`, `attention_required`, `escalated`, or `treated_monitoring` as Core Risk State codes.

The fixture uses:
- `supply_disruption_context_realized`
- `supply_disruption_context_persists_after_treatment_activity`

The second state explicitly does **not** claim improvement, deterioration or treatment effectiveness; it only keeps a synthetic post-activity risk-relevant situation in scope.

## Transition rule
SR-REL-032 may order states only within the same state family/dimension. It must never be used to bridge Workflow State and Risk State as if they were one lifecycle.

## Claim boundary
The policy supports the distinction `Risk State ≠ Workflow State`; it does not claim a universal taxonomy of all possible risk-state dimensions.
