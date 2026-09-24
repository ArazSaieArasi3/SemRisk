# SemRisk Paper-1 Expert Review Package v1.0

**Issue:** #51  
**Candidate:** P1-R2 / ontology 0.1.0-rc.1  
**Relational companion:** 0.1.0-rc.1  
**Data snapshot:** P1-DATA-0.1.0-rc.1  
**Review package:** EV-PACK-1.0  
**Status:** VERSION-BOUND PACKAGE READY FOR REAL REVIEWERS

## 1. Reviewer purpose

This package asks reviewers to assess whether the selected SemRisk distinctions, definitions, relations and profile boundaries are semantically defensible for the bounded Paper-1 scope.

The review is **not** a request to:
- certify SemRisk as universally correct;
- approve every risk domain;
- validate standards conformance;
- assess software quality;
- infer treatment effectiveness from the Pharma scenario;
- convert formal consistency into domain validity.

A reviewer may mark an item **NA / Not Assessed** whenever it falls outside their expertise or the evidence supplied is insufficient.

## 2. Scope of SemRisk Paper 1

Paper 1 evaluates three bounded contributions:
1. **SR-C1:** a well-founded operational risk semantic pattern;
2. **SR-C2:** enterprise operationalization and an executable relational projection;
3. **SR-C3:** one bounded Pharma federation case with CM-PharmE v1.0.0.

Broad Health, Risk Intelligence, Newsium/Commentium runtime integration, universal risk-domain coverage and predictive risk propagation are out of scope.

## 3. Core semantic definitions for review

### Risk — SR-CPT-001
A context-dependent risk phenomenon or pattern concerning possible effects on value/objectives, distinct from records, descriptions, scores and workflow artifacts.

### Risk Source — SR-CPT-003
A risk-relevant origin, source or contextual contributor that may participate in a scenario or event; causal status is not implied by the label alone.

### Predisposing Condition — SR-CPT-004
A contextual state or disposition that increases susceptibility to a risk-relevant event/effect without necessarily directly causing it.

### Trigger — SR-CPT-005
A condition or occurrence that initiates or activates a transition in a risk-relevant scenario, event, monitoring or response process.

### Risk Scenario — SR-CPT-006
A possible or hypothesized risk-relevant configuration or event pattern used for analysis, distinct from descriptions and realized events.

### Risk Event — SR-CPT-007
A realized occurrence relevant to a risk context, distinct from a possible scenario and information artifacts describing it.

### Consequence — SR-CPT-008
A risk-relevant outcome or effect of an event/scenario; its magnitude or severity may be assessed separately.

### Vulnerability — SR-CPT-009
A disposition or condition that increases susceptibility to a risk-relevant event/effect.

### Exposure — SR-CPT-010
A context-dependent condition or relation indicating how a subject/value is exposed to a risk-relevant source/event; assessment scores remain separate.

### Risk Assessment Activity — SR-CPT-011
An activity applying a method, context and evidence to produce one or more risk assessment results.

### Risk Assessment Method — SR-CPT-012
A method or technique governing how assessment evidence/context is transformed into one or more assessment results.

### Risk Assessment Result — SR-CPT-013
A contextual, time-bound information or measurement result produced by a Risk Assessment Activity concerning a risk subject/context.

### Likelihood Assessment Result — SR-CPT-014
An assessment result concerning estimated likelihood/probability/frequency under a specified method and context.

### Impact Assessment Result — SR-CPT-015
An assessment result concerning magnitude/severity of effects under a specified assessment method/context. It is distinct from the Consequence itself.

### Inherent Risk Assessment Result — SR-CPT-017
A risk assessment result representing a pre-treatment/pre-control assessment context; not a separate timeless Risk entity by default.

### Residual Risk Assessment Result — SR-CPT-018
A risk assessment result representing a post-treatment/control assessment context; not a second underlying Risk by default.

### Evidence Item — SR-CPT-020
An information artifact used in context to support, challenge or contextualize a risk-related assertion, assessment or decision.

### Provenance — SR-CPT-021
Information about origin, derivation, version, agent, time and transformation history of an artifact/assertion/result.

### Risk Treatment Strategy — SR-CPT-026
A decision/information artifact specifying a high-level selected approach for addressing a risk.

### Risk Treatment Plan — SR-CPT-027
An information artifact specifying planned treatment activities, responsibilities, timing or resources.

### Risk Treatment Activity — SR-CPT-028
An activity performed to modify risk-relevant conditions, likelihood, consequences or preparedness.

### Control Mechanism — SR-CPT-029
A persistent mechanism, capability or implemented measure used in prevention, detection, protection or risk treatment.

### Risk Owner — SR-CPT-030
A context-dependent role borne by an actor with responsibility/accountability for specified risk-management obligations.

### Risk Responsibility — SR-CPT-031
A responsibility/accountability assignment connecting an actor/role to a risk-management obligation or artifact.

### Risk Register — SR-CPT-032
A managed repository/collection of Risk Register Entries for a defined organizational or analytical scope.

### Risk Register Entry — SR-CPT-033
A governed information artifact in a risk register recording risk-related description, assessments, ownership, treatment and workflow information.

### Scenario Description — SR-CPT-034
An information artifact describing a Risk Scenario, event chain, assumptions or consequences; it is not the scenario or realized event itself.

### Risk State — SR-CPT-035
A modeled state/context of the underlying Risk across time.

### Workflow State — SR-CPT-036
An operational state of a record/workflow process; it does not by itself state that the underlying Risk has ceased or changed ontological identity.

## 4. Claim-critical distinctions

Reviewers should pay particular attention to whether these distinctions are defensible:
- Risk ≠ Risk Register Entry;
- Risk Scenario ≠ Risk Event ≠ Scenario Description;
- Risk Assessment Activity ≠ Risk Assessment Result;
- Consequence ≠ Impact Assessment Result;
- Inherent/Residual Risk are contextual assessment-result interpretations concerning one Risk by default;
- Risk State ≠ Workflow State;
- Actor ≠ Risk Owner role ≠ Risk Responsibility assignment;
- Treatment Strategy ≠ Treatment Plan ≠ Treatment Activity ≠ Control Mechanism;
- source/condition/trigger/causal relation are not interchangeable;
- external enterprise/Pharma concepts retain external semantic ownership.

## 5. Module/profile boundaries

- **Core:** domain-neutral risk/scenario/event/assessment/evidence/treatment/responsibility semantics.
- **Enterprise:** register, workflow, ownership and operational application semantics.
- **Method:** assessment methods, scales, thresholds and method-specific values.
- **Governance:** appetite, tolerance, criteria and governance refinements.
- **Pharma:** bounded domain profile/federation; CM-PharmE entities remain externally owned.
- **DataProjection:** relational/application projection only; database structure is not ontology truth.
- **RiskIntelligence / broad Health:** deferred beyond Paper 1.

## 6. Operational mapping context

The selected Jira-style operational schema contains 27 governed attributes. All 27 have semantic dispositions, but this is **mapping coverage rather than proof of semantic correctness**. Review item EV-015 asks whether the mapping strategy avoids mechanically turning spreadsheet/database fields into ontology classes while preserving useful operational semantics.

## 7. Bounded Pharma case

The Pharma case uses:
- DS-003 v4 as a bounded source for conditions, evidence and proposed treatment strategies;
- CM-PharmE v1.0.0 as external semantic owner;
- explicitly synthetic trigger/event/control/workflow/reassessment artifacts to execute the model.

Reviewers must not treat the synthetic scenario portion as evidence of real treatment effectiveness, prevalence or prediction.

Pharma-specific review items:
- EV-017 — SemRisk↔CM-PharmE federation boundary;
- EV-018 — semantic plausibility of the DS-003 bounded case mappings.

## 8. Response scale

For each item:
- **A** — Accept as semantically adequate for reviewed scope
- **B** — Accept with minor clarification/revision
- **C** — Major semantic revision required
- **D** — Reject / semantically incorrect for reviewed scope
- **NA** — Not assessed / insufficient expertise or evidence

Additional dimensions:
- clarity: clear / needs clarification / unclear / NA
- scope placement: Core correct / Profile correct / should move / NA
- relation/cardinality: appropriate / questionable / incorrect / NA
- evidence sufficiency: sufficient / insufficient / NA

Any C or D response should identify the exact semantic target and rationale where possible.

## 9. Review items

The authoritative item set is:
`evaluation/expert/expert-review-instrument-v1.0.csv`

It contains **20 frozen questions (EV-001…EV-020)** linked to semantic IDs, competency questions and contribution IDs.

## 10. Reviewer metadata / independence

The review records only methodological metadata:
- pseudonymous reviewer ID;
- expertise dimensions;
- experience bracket;
- academic/practitioner context;
- prior SemRisk or CM-PharmE involvement;
- independence classification;
- conflict note if applicable;
- package/version reviewed.

A reviewer does not need to disclose personal information beyond what is necessary for methodological reporting.

## 11. Finding and re-review rule

Critical/High semantic objections cannot be averaged away. They remain open until disposition/remediation and, where required, re-review. Any material ontology change triggered by expert review must rerun the affected formal, negative-control, CQ and application regression gates.

## 12. Current nonclaims shown to reviewers

The current candidate does not claim:
- universal or complete risk-domain semantics;
- universal Health/Pharma validity;
- standards certification;
- independent transferability across domains;
- lossless database equivalence;
- treatment effectiveness or prediction;
- overall superiority over prior ontologies.

## 13. Submission of review

Reviewer responses should use:
`evaluation/expert/expert-response-template-v1.0.csv`

Raw individual judgments are preserved before any summary or adjudication.
