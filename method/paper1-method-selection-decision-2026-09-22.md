# SemRisk Paper-1 Method Selection Decision

**Date:** 2026-09-22
**Issue:** #23
**Decision:** `SELECTED / W2 METHOD PROFILE FROZEN`

## 1. Scientific design
Ontology-engineering design research with evidence synthesis, bounded operational/Pharma cases, executable projection and claim-dependent evaluation.

## 2. Orchestration framework
OGCM-RF is the upstream research-engineering framework. SemRisk does not fork or redefine OGCM-RF; it records one bounded implementation profile and deviations.

## 3. Selected ontology-engineering flow
1. governed evidence discovery/mining and stopping;
2. cross-source reconciliation;
3. UL/anti-concepts;
4. semantic requirements + pre-implementation CQs;
5. Core concepts + relation/event/state design;
6. external reuse/alignment;
7. standards/prior-work comparison;
8. UFO/gUFO + OntoUML foundational analysis;
9. modular OWL/RDF formalization;
10. SHACL for closed-world/local constraints;
11. explicit rule/application layer for workflow/business logic;
12. governed operational schema mapping;
13. PostgreSQL projection + SQL↔SPARQL parity/loss analysis;
14. claim-dependent E1–E11 evaluation;
15. immutable release/publication binding.

## 4. Technology separation
- **OWL/RDF/Turtle:** open-world semantic commitments and reasoning.
- **SHACL:** closed-world/local structural/data constraints.
- **Rules/application logic:** workflow, formulas and business logic not justified as universal ontology truth.
- **PostgreSQL/SQL:** executable relational projection; never semantic source of truth.
- **OntoUML/UFO/gUFO:** conceptual/foundational analysis; not merely diagramming.

## 5. Evaluation selection
Formal verification, foundational review, bounded expert validation, mapping validation, CQ regression, application/query utility, reproducibility, comparative evaluation and bounded transferability are selected only where the related claim survives. No arithmetic global score is used.

## 6. Explicitly deferred method families
Theorem proving, model checking, probabilistic risk propagation and a full Risk Intelligence runtime are deferred beyond Paper 1. They are established prior art and are not needed to support the bounded ICAE claims.

## 7. Critical method rule
A stronger method is adopted where it matches the claim burden. For example, RISKMAN informs OWL+SHACL validation, COVER/ROSE inform foundational/reuse analysis, the Oliveira programme informs ontological mismatch diagnostics, and RiskHub informs operational RDB/application engineering. SemRisk does not claim its method is globally better than these alternatives.

## 8. Change control
Any change to foundational ontology, formal language/profile, CQ semantics, evidence independence, projection architecture or evaluation class after this freeze requires downstream impact review and rerun of affected gates/evidence.