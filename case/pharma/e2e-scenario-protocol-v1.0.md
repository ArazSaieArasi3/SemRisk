# SemRisk Paper-1 End-to-End Scenario Protocol v1.0

Issue: #48

## Scenario question
Can one governed SemRisk risk context preserve, across RDF and PostgreSQL, the distinctions among source/condition/trigger, scenario/event/consequence, assessment/result/evidence, treatment execution, responsibility, Risk State and Workflow State while maintaining explicit provenance and a reassessment path?

## Source-grounded core
The bounded domain context is the DS-003 antibiotic-shortage case already governed under #28/#47:
- supply concentration / limited suppliers → constructed Predisposing Condition;
- forecasting/demand-estimation challenge → constructed Predisposing Condition;
- pooled procurement → constructed proposed Risk Treatment Strategy;
- DS-003 v4 → Evidence Item/source anchor;
- CM-PharmE v1.0.0 → externally owned supply-capacity/demand/supply-chain context.

These are constructed from source-supported study-level summaries and are **not raw empirical records**.

## Synthetic extension required for executable path
DS-003 does not justify inventing a dated realized shortage event, executed control, organizational owner, workflow history or measured residual risk. Therefore the following are explicitly generated as `synthetic_test` fixtures:
- Trigger;
- realized Risk Event;
- Consequence;
- Risk Register / Entry / Scenario Description;
- owner Actor + Risk Responsibility;
- Treatment Plan / Activity / Control;
- initial and treated Workflow States;
- pre-treatment assessment/result and post-treatment reassessment/residual result;
- pre/post Risk States.

The synthetic extension tests semantic/application behavior only. It is not empirical evidence of causal strength, treatment effectiveness, prevalence, prediction or generalizability.

## Temporal story used only for deterministic testing
- T0: bounded Risk/Scenario exists.
- T1: synthetic trigger/event realizes the scenario and has a consequence.
- T2: synthetic pre-treatment assessment produces an inherent-context result.
- T3: pooled-procurement strategy is selected; synthetic plan/activity/control represent execution.
- T4: synthetic reassessment is explicitly based on the prior assessment and produces a residual-context result that supersedes the prior result.
- T5: Risk State history changes from `supply_disruption_context_realized` to `supply_disruption_context_persists_after_treatment_activity`; independently, record Workflow State changes from `open` to `treated`.

The Risk State labels denote synthetic situational contexts rather than management/monitoring classifications. No numeric magnitude, improvement or treatment effectiveness is asserted; the transition only exercises model semantics.

## Predeclared expected outcomes
Canonical expected answers are frozen in `e2e-scenario-expected-v1.0.csv` before execution. CI must test those outcomes without rewriting them after observing results.

## Failure/edge control
The scenario test must reject/detect at least:
1. treating Workflow State as Risk State;
2. creating primitive `owner_id` on Risk instead of responsibility-derived ownership;
3. treating strategy, plan, activity and control as one object;
4. treating inherent/residual assessment contexts as two underlying Risk identities.

## Claim boundary
A PASS supports bounded executable representation and projection testing only. It is not independent semantic validation and does not establish real-world treatment effect or predictive capability.
