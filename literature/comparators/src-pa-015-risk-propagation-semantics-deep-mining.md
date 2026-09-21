# SRC-PA-015 Deep Mining — On the Semantics of Risk Propagation

**Source ID:** SRC-PA-015  
**Citation:** Fumagalli et al. (2023), *On the Semantics of Risk Propagation*, RCIS 2023, LNBIP 476, pp. 69–86, DOI 10.1007/978-3-031-33080-3_5  
**Mining date:** 2026-09-21  
**Status:** DEEP-MINED v0.1 — full 17-page paper inspected; source locators recorded at section/page granularity.

## 1. Source role

- comparative
- conceptual-foundation
- discovery/design input
- lineage predecessor to SRC-PA-010 and SRC-PA-006
- not independent validation of SemRisk

## 2. Central ontological position

The paper argues that 'risk propagation' is conceptually overloaded and misleading when understood as if Risk were a physical object or scalar substance moving through a graph. Using COVER, it reframes propagation as changes in the Risk Assessor's judgment about possible events and their outcomes.

### Locator evidence
- Section 2.1 / pp. 2–3: risk is relative, goal-dependent, experiential, contextual and uncertainty-grounded.
- Section 2.2 / pp. 4–5: COVER risk-assessment, event, object, vulnerability/threat-capability and likelihood commitments.
- Section 4.1 / pp. 8–10: propagation interpreted as belief/judgment update via observation or simulation.
- Section 4.2 / pp. 10–13: semantic decomposition of graph nodes/links.
- Section 5 / pp. 13–16: expressivity and accuracy implications.

## 3. Core semantic findings

### 3.1 Risk is an assessment-related quantitative attribution
The paper treats Risk as a quantitative measure attributed to Risk Assessment, not as an entity physically propagating through nodes.

### 3.2 Risk propagation is belief/judgment updating
Propagation is best understood as an event in which a subject's judgment changes because likelihoods and related assessment inputs are updated. Probability propagation alone is insufficient to explain risk because risk also depends on loss/impact and goal importance.

### 3.3 Observation-driven reassessment
When new evidence indicates that an event has occurred, related event probabilities and risk assessments are updated. This provides prior art for evidence-triggered reassessment semantics.

### 3.4 Simulation-driven reassessment
Risk may also be updated by simulating possible event occurrences. In this case, the assessor constructs an imaginative risk experience over correlated Event Types. This is prior art for scenario/simulation-driven reassessment.

### 3.5 Event type vs event occurrence is essential
The paper explicitly warns against conflating event occurrences, event types and objects. Likelihood attaches to event types, while occurrences instantiate those types.

### 3.6 Risk propagation models are projections of a richer risk experience
Probabilistic graphs can be viewed as projections supporting probability inference; they do not by themselves carry the full semantics of objects, events, goals, dispositions and assessment context.

## 4. Graph-relation semantics

The paper distinguishes multiple link semantics that flat propagation graphs often conflate:

### Type-to-type
1. event/event correlation;
2. event/event causal or historical dependence;
3. object/event participation;
4. object/object parthood.

### Instance-to-type
5. individual/event participation;
6. property/event characterization.

This is highly relevant to SemRisk because a generic edge such as `affects`, `propagatesTo` or `dependsOn` would be semantically under-specified.

## 5. Causation vs correlation

The paper emphasizes that correlation and causation must not be collapsed. Causal links are materially different for treatment/mitigation reasoning because intervening on a cause may alter an effect, whereas correlation alone does not justify that conclusion.

SemRisk consequence: causal relations, statistical association, dependency and operational linkage must be separately modeled or explicitly typed; a single generic propagation relation is unacceptable.

## 6. Objects, events and dispositions

The paper shows that object-to-object propagation often hides:
- part-whole structures;
- vulnerabilities and threat capabilities;
- implicit risk-event types in which objects participate;
- activation/manifestation of dispositions.

SemRisk consequence: object risk cannot be modeled as a simple scalar property copied between objects.

## 7. Evidence and reassessment implication

The observation case is especially important for SemRisk: new evidence instantiates/updates knowledge about events and leads to an updated Risk Assessment. This does not yet give the full SemRisk Evidence/Assessment Result provenance model, but it is clear prior art for dynamic evidence-triggered risk reassessment.

Therefore SemRisk cannot claim novelty merely from 'risk updates when new evidence arrives'.

## 8. Query/expressivity findings

Five cybersecurity experts were consulted to identify queries poorly supported by mainstream propagation graphs. Representative needs included determining risk for:
- an object from events in which it participates;
- an event from connected events;
- an object from connected objects;
- an event sharing objects with other events;
- an object participating in event chains with other objects;
- an event given properties of correlated events.

The paper argues that ontology-backed knowledge representation is necessary to answer such queries without flattening object/event/relation semantics.

## 9. Direct SemRisk novelty impact

### SR-C1
**RETAINED / FURTHER NARROWED.**

Already prior art:
- risk as assessor-relative/contextual;
- evidence/observation causing reassessment;
- simulation causing reassessment;
- event type vs event occurrence separation;
- object/event/type/instance disambiguation;
- causation vs correlation distinction;
- participation/parthood semantics;
- ontology-backed risk queries.

SemRisk's remaining candidate differentiation must focus on the integrated operational/information architecture:
**risk-relevant phenomenon/event pattern → scenario description → Risk Register Entry → Assessment Activity → Assessment Result + provenance → Risk State → Workflow State → Evidence/Observation → Treatment/Responsibility**.

### SR-C2
Object/goal/event/relationship reasoning is prior art; enterprise novelty must rely on explicit architecture ownership, operational record/workflow/accountability semantics and bounded executable projection.

### SR-C3
No direct invalidation; Pharma federation remains a separate bounded claim.

## 10. Lineage reconciliation

Treat as one evolving programme:
1. SRC-PA-015 — conceptual semantics of propagation;
2. SRC-PA-010 — process-aware ontology-driven propagation proof-of-concept;
3. SRC-PA-006 — richer assessment taxonomy/query model and ProbLog implementation.

These sources should be cited independently when their distinct contributions matter, but never counted as three independent demonstrations of the same novelty gap.

## 11. Design constraints carried forward to W2

Do not canonize before G1, but preserve these constraints for #19/#20/#7:
- no `Risk` entity that literally flows;
- separate event type from event occurrence;
- separate causation from correlation;
- represent object participation explicitly;
- represent parthood explicitly;
- distinguish observation-driven from simulation-driven reassessment;
- preserve assessor/goal context;
- treat probabilities/likelihoods as assessment inputs/results, not intrinsic timeless properties.

## 12. Gate consequence

Propagation-family semantic saturation is now substantially stronger. Remaining debt is primarily exact formal-artifact binding, PA-010 implementation details and comparison with PA-006/PA-012 rather than discovery of the foundational semantics themselves.