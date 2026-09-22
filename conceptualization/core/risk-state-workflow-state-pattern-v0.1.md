# SemRisk Risk-State vs Record-Workflow Pattern v0.1

## Two state dimensions
1. `Risk State` — state of the risk-relevant situation/context.
2. `Workflow State` — state of the management record/workflow.

## Hard invariant
`Workflow State = Closed` **does not entail** that the Risk ceased, became false or has no residual relevance.

## History
Both dimensions may have historical states. State ordering/transitions are time/context dependent and cannot be inferred from database status codes alone.

## Formalization rule
Workflow transition rules belong primarily to state-machine/application/rule validation layers. They are not universal OWL truths unless separately justified.

## CQ coverage
`CQ-008`, `CQ-024`, `CQ-038`.