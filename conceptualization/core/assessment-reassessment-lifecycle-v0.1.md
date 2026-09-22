# SemRisk Assessment / Reassessment Lifecycle Pattern v0.1

## Primary pattern
`Risk → Risk Assessment Activity → Risk Assessment Result`

with contextual links to:
- `Risk Assessment Method`;
- `Evidence Item`;
- `Provenance`;
- time/context;
- optional `Assessment Confidence`.

## Pre/post-treatment
`Inherent Risk Assessment Result` and `Residual Risk Assessment Result` are result/context refinements concerning the same underlying Risk by default. They do not create a second Risk identity unless explicit evidence says so.

## Reassessment
A later `Risk Assessment Activity` may `basedOnPriorAssessment` and produce a newer result. `supersedesAssessmentResult` preserves history; superseded results are not deleted from semantic history.

## Lifecycle invariants
1. Activity ≠ Result.
2. Result ≠ Risk.
3. Pre-treatment result ≠ a second Risk.
4. Reassessment may change results without changing Risk identity.
5. Method/evidence/time/context must remain recoverable where modeled.

## CQ coverage
`CQ-005`, `CQ-006`, `CQ-007`, `CQ-015`, `CQ-022`, `CQ-023`, `CQ-031`, `CQ-038`.