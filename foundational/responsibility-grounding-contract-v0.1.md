# SemRisk Risk Responsibility Grounding Contract v0.1

**Owner:** Issue #71  
**Status:** FROZEN_POLICY

## Purpose
Clarify the UFO/gUFO grounding of SR-CPT-030 Risk Owner, SR-CPT-031 Risk Responsibility and SR-REL-026..028 without forcing the derived SemRisk Risk pattern to behave as an endurant participant.

## Commitments
### Risk Owner
Risk Owner is an anti-rigid Role borne by an external Actor in a responsibility context. It is not an actor kind and is not a role individual stored on Risk.

### Risk Responsibility
Risk Responsibility is a concrete normative assignment/relator context that:
- depends on and mediates the Actor/bearer and any explicitly modeled endurant governance/assignment participants;
- carries validity/history and may support reassignment/co-ownership;
- is **about** the governed Risk, Risk Register Entry, Treatment Plan or obligation it concerns.

### Risk as aboutness target
Because SR-CPT-001 Risk is a derived SemRisk domain pattern rather than a locally asserted endurant kind, SemRisk does **not** assert that Risk is a mediated endurant relatum merely to fit an implementation schema.

SR-REL-027 `assignsResponsibilityFor` therefore expresses responsibility-about/for the Risk/artifact/obligation target.

SR-REL-028 `responsibilityAssignedTo` expresses the participant/mediation side toward the Actor/role bearer.

## Derived ownership
SR-REL-026 `hasRiskOwner` is a derived material relation:
Risk/context → Actor
that is truthmade by a valid Risk Responsibility assignment.

No primitive `owner_id` on Risk is authoritative ontology truth.

## Relational projection
The current relational `enterprise.risk_responsibility.risk_id` is a projection shortcut for **responsibility-about-Risk**. It must not be interpreted as a claim that the Risk pattern is a UFO-mediated endurant.

## Temporal and multiplicity rules
- co-owners are allowed;
- assignments may be time bounded;
- reassignment history is preserved;
- absence of one current assignment under OWA does not prove there is no owner universally;
- application-level completeness may be enforced through SHACL/RDB where scoped.

## Nonclaims
This contract does not introduce a new organization/obligation ontology and does not claim a universal deontic theory. It freezes the minimum semantics required to avoid the role/relator/derived-pattern category error in Paper 1.
