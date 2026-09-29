# SemRisk foundational analysis — Issue #25 checkpoint v0.1

Status: CHECKPOINT / NOT A SEMANTIC FREEZE
Work item: #25
Method frame: UFO/gUFO + OntoUML, with OGCM-RF as method authority.
Upstream gate: #24 G2 CONDITIONAL_PASS.

## Purpose
This checkpoint resolves or bounds the seven HIGH foundational questions handed forward by G2. It is an analysis artifact, not proof of correctness and not authorization for semantic release. Stable #26 formalization remains conditional on rechecking these decisions against the canonical registries, reuse/alignment evidence, CQs, and the full release-critical relation set.

## Decision principles
1. Separate real-world phenomena from information artifacts that describe them.
2. Separate events/activities from their results, qualities, values and records.
3. Do not model contextual assessment labels (for example inherent/residual) as rigid Risk subtypes without identity justification.
4. Treat roles as anti-rigid and externally dependent; do not turn Risk Owner into a rigid person/organization kind.
5. Distinguish material relations that require a relational truthmaker/relator from implementation-level foreign keys.
6. Reuse COVER/ROSE semantics by alignment/reference where G2 assigns external ownership; local convenience does not authorize flattening or copying.
7. Cardinalities below are ontological claims only when justified; database multiplicities belong to later implementation design.

## Seven HIGH questions

| ID | Construct | Foundational disposition | Consequence / recheck |
|---|---|---|---|
| FQ-01 | SemRisk Risk vs COVER Risk | Treat SemRisk Risk as a context-dependent risk situation/relational configuration, not as an independent substantial object. Preserve COVER ownership where its Risk concept is reused; SemRisk should specialize/align only when identity and dependence criteria are compatible. | Do not assert `owl:equivalentClass` by name similarity. #26 must use the #21 alignment decision and CQ evidence to choose narrower mapping or local specialization. |
| FQ-02 | Assessment Activity / Assessment Result vs COVER/ROSE RiskAssessment | Split the assessment occurrence from its output. `RiskAssessmentActivity` is an Event/Activity; `AssessmentResult` is an information object that records/asserts assessment findings and can bear reported values. A single class must not play both categories. | #26 must avoid collapsing process and result. External `RiskAssessment` terms require scoped mapping according to their source semantics. |
| FQ-03 | Likelihood result vs COVER Likelihood | Likelihood is not an assessment event and not automatically an information object. Model the underlying likelihood/probability as a quality/value-bearing assessment dimension; its asserted numeric/ordinal representation belongs to the Assessment Result/measurement information layer. | Keep the phenomenon/value/record distinction explicit; map to COVER Likelihood only after checking whether COVER denotes quality, value, or information representation. |
| FQ-04 | RiskEvent type vs occurrence | Distinguish `RiskEventType` from `RiskEventOccurrence`. The type is a repeatable event universal/type; an occurrence is a perdurant/event instance participating entities at a time. Scenario descriptions may reference event types without asserting an occurrence. | #26 and the conceptual figure must not conflate a possible event type, a scenario, and an observed event occurrence. |
| FQ-05 | ControlMechanism vs ROSE SecurityMechanism | Treat a concrete control/security mechanism as a substantial/functional bearer capable of playing a risk-treatment role; a control specification/description is an information object. Preserve ROSE external ownership and use alignment rather than local semantic copying where applicable. | Recheck whether the local Core needs a generic `ControlMechanism` category or only a profile/mapping reference. No equivalence until intension and dependence match. |
| FQ-06 | Vulnerability vs Predisposing Condition | Treat vulnerability as a dependent disposition/predisposition of a bearer (or a structured configuration grounding such a disposition), not as a free-standing object. `PredisposingCondition` is broader: a situation/condition that can ground or manifest increased susceptibility and need not be identical to the disposition itself. | Prefer a narrower relation such as grounding/characterization over equivalence unless #21 evidence establishes identity. Preserve bearer dependence. |
| FQ-07 | Risk State bearer/category | Do not create a free-standing rigid `RiskState` object merely to encode workflow status. Distinguish (a) real-world risk-relevant situation/state of affairs, (b) temporal state of an assessed risk configuration, and (c) workflow/record status of a Risk Record. | #26 must name these separately. Record lifecycle status must not be used as evidence that the underlying risk phenomenon changed. |

## Additional release-critical distinctions

### Risk Owner
`RiskOwner` is a role played by an eligible actor (person, organizational unit, organization, or another governed agentive entity). The role is anti-rigid and externally dependent on an ownership/responsibility context. The actor retains its identity independently of playing the role.

### Ownership / responsibility assignment
Do not treat assignment as an unexplained binary property when accountability provenance matters. Model an `OwnershipAssignment` / `ResponsibilityAssignment` relator or information-backed social relator that mediates the Risk Owner and the governed Risk/Risk Record according to the policy context. Whether the relator is social/intentional versus merely documentary must be decided from the source semantics; the record that documents it is not the relator itself.

### Risk Scenario and Scenario Description
A Risk Scenario is a possible/configured situation involving relevant conditions, participants and possible event types. `ScenarioDescription` is an information object describing that scenario. Neither is identical to a Risk Event occurrence.

### Risk Record / Register Entry
A Risk Record (register entry) is an information artifact. It can refer to a risk configuration, assessment activity/result, owner assignment, controls and evidence. Its identity/versioning rules are documentary and must not be inherited by the real-world Risk phenomenon.

### Inherent and residual risk
Treat `inherent` and `residual` primarily as assessment context/result qualifiers relative to a control/treatment configuration and assessment time. They are not automatically rigid subclasses of Risk. A comparison requires explicit context: assessed subject, control baseline, method, time and result.

### Evidence
Evidence artifacts are information objects (or references to observable artifacts) used to support an assessment/assertion. Evidence acceptance remains a Human Gate where expert-evidence acceptance is required; this analysis does not promote evidence to accepted truth.

## Relation-type guidance
- `playsRole(actor, RiskOwner)` — characterization/classification of an actor by an anti-rigid role; avoid encoding actor identity through the role.
- `mediates(OwnershipAssignment, Actor/RiskContext)` — material relation truthmaker when an assignment genuinely constitutes responsibility.
- `participatesIn(entity, RiskEventOccurrence)` — participation relation; event occurrence has temporal extent.
- `describes(ScenarioDescription, RiskScenario)` and `records(RiskRecord, AssessmentResult)` — information-to-referent relations; do not collapse referent and representation.
- `characterizes(Vulnerability, bearer)` — vulnerability depends on its bearer; exact gUFO pattern must be checked against the selected reuse profile.
- `grounds(PredisposingCondition, Vulnerability)` — candidate relation, contingent on source semantics; not asserted as universal equivalence.

Cardinality policy: this checkpoint intentionally avoids hard numeric cardinalities where the G2 evidence does not establish ontological necessity. Implementation constraints such as one-current-owner, one-latest-result or mandatory record fields must be modeled later as data/application constraints unless independently justified as ontological truth.

## Anti-pattern register

| AP | Finding | Severity | Disposition |
|---|---|---:|---|
| AP-25-01 | Risk Owner modeled as a rigid actor type | HIGH | Reject; use role + actor identity. |
| AP-25-02 | Assessment activity and result collapsed | HIGH | Reject; split event/activity from information/result/value. |
| AP-25-03 | Risk Event type and occurrence collapsed | HIGH | Reject; maintain universal/type vs occurrence distinction. |
| AP-25-04 | Risk Record treated as the risk phenomenon | HIGH | Reject; preserve information-object/referent distinction. |
| AP-25-05 | Inherent/residual encoded as rigid Risk subtypes | HIGH | Reject unless future identity evidence proves subtype semantics. |
| AP-25-06 | Vulnerability equated to any predisposing condition | HIGH | Reject broad equivalence; preserve disposition/bearer and grounding distinction. |
| AP-25-07 | Workflow record status used as Risk State | HIGH | Reject; separate record lifecycle from world state. |
| AP-25-08 | External COVER/ROSE classes copied into Core for convenience | HIGH | Reject; follow governed reuse/alignment ownership. |
| AP-25-09 | Database cardinality presented as ontological truth | MEDIUM | Keep implementation constraints separate and evidence-link true cardinality claims. |

## Contested alternatives retained
- Risk may ultimately be represented as a Situation, a relationally dependent configuration, or a more specific externally aligned category depending on the exact COVER semantics. This checkpoint rejects only the unsupported independent-object interpretation.
- Vulnerability may be represented directly as a disposition/mode or via a structured situation that grounds a disposition. The selected formal pattern must preserve bearer dependence and the #21 reuse decision.
- Ownership may require a social relator, an assignment information object plus normative relation, or both. The final choice depends on whether SemRisk claims the social commitment itself or only records an externally governed assignment.
- Likelihood may be modeled as a quality with a value region or as an assessment dimension whose result is represented informationally; external mapping must determine which layer COVER denotes.

## Gate consequence
The seven HIGH questions are **bounded for continuation**, not semantically frozen. No Critical category error is knowingly left unbounded in this checkpoint. Before #25 can be declared complete, the decisions must be propagated to stable semantic IDs in the canonical concept/relation registries, represented in the integrated OntoUML/conceptual model, and rechecked against COVER/ROSE/CM-PharmE mappings and the Paper-1 CQ set. #26 may prepare against these bounded distinctions but must not treat affected formalization as stable until that recheck is recorded.

## Validation checklist for next #25 batch
- map each decision above to canonical concept/relation IDs;
- produce the foundational-category/stereotype registry for every release-critical Core entity/relation or explicit N-A rationale;
- update relation/cardinality rationale with source/evidence links;
- project the registry into the OntoUML conceptual figure (no diagram-only semantics);
- rerun the anti-pattern register after model remediation;
- audit COVER/ROSE/CM-PharmE alignments for category preservation;
- re-evaluate the seven G2 conditions and record RESOLVED / BOUNDED / BLOCKING individually.
