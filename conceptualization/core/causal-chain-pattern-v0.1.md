# SemRisk Causal-Chain Pattern v0.1

**Pattern:** `Risk Source → Predisposing Condition → Trigger → Risk Scenario → Risk Event → Consequence`

## Semantics
- `Risk Source` is a neutral source/context anchor; it does not imply universal causality.
- `Predisposing Condition` enables/increases susceptibility without necessarily being a direct cause.
- `Trigger` initiates/activates a transition or occurrence; it is not automatically the root cause.
- `Risk Scenario` is possible/hypothesized; `Risk Event` is realized.
- `Consequence` is the outcome/effect; `Impact Assessment Result` is an assessment of severity/magnitude and is not the consequence itself.

## Relation-strength rule
`causes` requires explicit evidence/model rationale. `associatedWith` or dependency relations must remain weaker when causal support is absent. Sequence in time never implies causation by itself.

## Temporal rule
Sources/conditions can persist over intervals; triggers/events occur at/over intervals; consequences can follow events; all claims may be contextual/versioned.

## Formalization boundary
No transitivity, universal causal closure or cardinality is asserted at W2. #26 determines OWL/SHACL/rule placement; #25 determines foundational categories.

## CQ coverage
`CQ-003`, `CQ-012`, `CQ-021`, `CQ-028`.