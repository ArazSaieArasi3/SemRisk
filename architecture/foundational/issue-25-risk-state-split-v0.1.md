# SemRisk Issue #25 — Risk State semantic split v0.1

Status: CHECKPOINT / NOT A SEMANTIC FREEZE  
Work item: #25  
Canonical IDs under review: `SR-CPT-035 Risk State`, `SR-REL-031 hasRiskState`  
Upstream analysis: `issue-25-foundational-analysis-v0.1.md` FQ-07  
Method frame: UFO/gUFO + OntoUML; OGCM-RF remains method authority.

## Purpose

Resolve the ambiguity identified in FQ-07 far enough to prevent `Risk State` from collapsing three ontologically different things. This checkpoint defines candidate replacements and migration rules for the current Paper-1 model. It does **not** approve a semantic freeze, release, or stable #26 formalization.

## Problem statement

The label `Risk State` is currently overloaded. At least three readings are possible:

1. a real-world risk-relevant state of affairs;
2. a temporally qualified state of an assessed risk configuration;
3. a workflow/lifecycle status of a Risk Record or assessment record.

These readings have different identity, dependence, temporal and representation conditions. A single undifferentiated class or relation would make workflow changes appear to be changes in the underlying risk phenomenon and would also conflate assessment context with documentary state.

## Candidate semantic split

| Candidate | Foundational category | Identity / dependence | Intended bearer / referent | Information-layer status | Recommended disposition |
|---|---|---|---|---|---|
| `RiskSituationState` | Situation / state of affairs | Depends on the participating real-world entities, conditions and relevant temporal context; identity is not inherited from a record identifier. | Risk-relevant configuration/situation | May be described by records, but is not itself a record. | **RETAIN as a real-world candidate**, subject to final alignment with the selected Risk pattern and COVER semantics. |
| `RiskAssessmentState` | Assessment-context/result state; modeled as a temporally qualified assessment condition rather than an independent rigid object | Depends on an assessed subject/configuration, assessment method/context and assessment time. | Assessment of a risk configuration | Representations/values belong in `AssessmentResult`; the assessment state is not identical to the result document. | **RETAIN as a bounded candidate**; #26 must choose a precise pattern after CQ/mapping recheck. |
| `RiskRecordStatus` | Information/workflow status | Depends on the Risk Record (or another governed information artifact) and its lifecycle/workflow. | `RiskRecord` / register entry / assessment record | Explicitly information-layer. | **RETAIN and rename explicitly**; never use as evidence that the real-world risk changed. |

## Canonical-ID migration rule

`SR-CPT-035 Risk State` must not be promoted unchanged into stable formalization. Before #26 is treated as stable, one of the following must be recorded in the canonical registry:

- **preferred:** deprecate/supersede the overloaded label and introduce distinct stable IDs for the required meanings above; or
- **bounded fallback:** narrow `SR-CPT-035` to exactly one meaning and introduce separate stable IDs for every other meaning actually required by Paper-1.

`SR-REL-031 hasRiskState` must be split or narrowed in lockstep. The relation name alone is insufficient. Its domain/range and temporal semantics must identify which state layer is intended.

## Relation candidates

| Relation candidate | Domain → range | Relation type / rationale | Cardinality stance |
|---|---|---|---|
| `hasSituationState` | Risk configuration/situation → `RiskSituationState` | Real-world situation/state relation; must preserve temporal qualification and participant dependence. | No hard numeric cardinality asserted here. |
| `hasAssessmentState` | assessed risk configuration + assessment context → `RiskAssessmentState` | Contextual/temporal assessment relation; must not erase method/time/control baseline. | No one-current-state rule asserted ontologically. |
| `hasRecordStatus` | `RiskRecord` → `RiskRecordStatus` | Information/workflow relation. | Any one-current-status constraint is an application/data constraint unless separately justified. |

## Invariants for #26 and the conceptual figure

1. `RiskRecordStatus` must never be a subclass/equivalent of a real-world risk situation/state.
2. A record-status transition must not entail a change in `RiskSituationState` or `RiskAssessmentState`.
3. A new assessment may change an asserted assessment state/result without implying that the underlying real-world situation changed.
4. Real-world situation changes may occur without a contemporaneous record-status change.
5. Every diagram edge derived from `SR-REL-031` must resolve to one explicit semantic layer; no generic `hasRiskState` edge may survive merely for visual convenience.
6. Inherent/residual labels remain assessment-context/result qualifiers and must not be smuggled back as generic `RiskState` subclasses.
7. External COVER/ROSE categories are not renamed or flattened to fit this local split; alignment is checked after local meanings are explicit.

## CQ-oriented regression probes

The next integrated model/CQ batch should be able to distinguish these cases:

- **CQ-RS-01:** Can the system represent a Risk Record moving from Draft to Approved while the represented risk situation is unchanged?
- **CQ-RS-02:** Can two assessments at different times/methods report different assessment states/results for the same risk configuration without creating two documentary workflow states by implication?
- **CQ-RS-03:** Can a real-world risk-relevant situation change before any Risk Record is updated?
- **CQ-RS-04:** Can inherent and residual assessments coexist for one risk configuration under different control baselines without typing the risk itself as two rigid subclasses?
- **CQ-RS-05:** Can every use of the legacy `SR-REL-031 hasRiskState` be classified as situation, assessment, or record/workflow semantics?

Failure of any probe indicates the split has not been preserved in the integrated model.

## Anti-pattern recheck additions

| AP | Finding | Severity | Required disposition |
|---|---|---:|---|
| AP-25-10 | One `RiskState` class carries world, assessment and workflow meanings | HIGH | Split/narrow before stable formalization. |
| AP-25-11 | `hasRiskState` has mixed domains/ranges across semantic layers | HIGH | Split/narrow relation and bind every use to an explicit layer. |
| AP-25-12 | Record-status transition interpreted as evidence of world-state transition | CRITICAL | Prohibit entailment/interpretation; keep referent and information lifecycle separate. |
| AP-25-13 | “current state” cardinality imported from UI/database design as ontological necessity | MEDIUM | Keep application/data constraint separate unless independently justified. |

## Decision status

- `SR-CPT-035`: **BLOCKING-AS-OVERLOADED → BOUNDED-BY-SPLIT**, but not yet stable.
- `SR-REL-031`: **BLOCKING-AS-AMBIGUOUS → BOUNDED-BY-RELATION-SPLIT**, but not yet stable.
- Critical anti-pattern AP-25-12 has an explicit prohibition, but must be rechecked against the integrated OntoUML model and CQ results before #25 completion.

## Next required batch

1. propagate this split into the foundational category/stereotype registry and canonical-ID migration proposal;
2. project the three layers into the integrated OntoUML/conceptual model with no diagram-only constructs;
3. run the full anti-pattern register including AP-25-10..13;
4. recheck COVER/ROSE/CM-PharmE category preservation;
5. execute the Paper-1 CQ regression including CQ-RS-01..05;
6. only then reassess whether #25 acceptance criteria and the handoff to #26 are satisfied.
