# SemRisk Responsibility / Ownership Pattern v0.1

## Pattern
`Risk / Risk Register Entry → hasRiskOwner → External Actor`

where `hasRiskOwner` is derived from the qualified assignment:
`Risk Responsibility → responsibilityAssignedTo → Actor/Role`
`Risk Responsibility → assignsResponsibilityFor → Risk / Risk Register Entry / Treatment Plan`

## Invariants
- Risk Owner is a role type borne by the external Actor in the assignment context; it is not modeled as a separate role individual.
- Responsibility assignment is a contextual/governance relation or relator candidate.
- Reassignment changes the assignment lifecycle, not the identity of the Actor or Risk.
- Ownership recorded in a Risk Register Entry may be evidence of the assignment but is not itself the responsibility relation.

## Temporal semantics
Assignments may have start/end/supersession and historical reassignment.

## CQ coverage
`CQ-009`, `CQ-025`, `CQ-038`.