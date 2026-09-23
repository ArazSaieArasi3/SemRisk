# SemRisk Paper-1 Foundational Conceptual Model v0.1

**Source of truth:** `foundational-category-registry-v0.1.csv` and `foundational-relation-rationale-v0.1.csv`.  
This diagram is a projection; it introduces no new semantic IDs.

```mermaid
flowchart LR
  R["SR-CPT-001 Risk<br/>«derived pattern»"]
  RS["SR-CPT-002 Risk Subject<br/>«roleMixin»"]
  V["SR-CPT-009 Vulnerability<br/>«intrinsic mode/disposition»"]
  PC["SR-CPT-004 Predisposing Condition<br/>«situation»"]
  TR["SR-CPT-005 Trigger<br/>«event role»"]
  SC["SR-CPT-006 Risk Scenario<br/>«situationType»"]
  EV["SR-CPT-007 Risk Event<br/>«event»"]
  CO["SR-CPT-008 Consequence<br/>«situation»"]
  RA["SR-CPT-011 Assessment Activity<br/>«event/action»"]
  RR["SR-CPT-013 Assessment Result<br/>«information object»"]
  EVd["SR-CPT-020 Evidence Item<br/>«information object + evidence role»"]
  TP["SR-CPT-027 Treatment Plan<br/>«information object»"]
  TA["SR-CPT-028 Treatment Activity<br/>«event/action»"]
  CM["SR-CPT-029 Control Mechanism<br/>«roleMixin»"]
  OW["SR-CPT-030 Risk Owner<br/>«role»"]
  RESP["SR-CPT-031 Risk Responsibility<br/>«relator»"]
  RE["SR-CPT-033 Risk Register Entry<br/>«information object»"]
  SD["SR-CPT-034 Scenario Description<br/>«information object»"]
  RST["SR-CPT-035 Risk State<br/>«situation»"]
  WST["SR-CPT-036 Workflow State<br/>«quality/value»"]

  RE -->|SR-REL-001 concernsRisk| R
  SD -->|SR-REL-002 describesScenario| SC
  SC -->|SR-REL-003 realizedAs| EV
  EV -->|SR-REL-004 hasConsequence| CO
  RS -->|SR-REL-012 hasVulnerability| V
  SC -->|SR-REL-006 predisposedBy| PC
  EV -->|SR-REL-007 triggeredBy| TR
  RA -->|SR-REL-013 performedAssessmentOf| R
  RA -->|SR-REL-015 producesAssessmentResult| RR
  RR -->|SR-REL-016 concerns| R
  RR -->|SR-REL-017 supportedByEvidence| EVd
  TA -->|SR-REL-023 executes| TP
  TA -->|SR-REL-024 usesControl| CM
  R -->|SR-REL-031 hasRiskState| RST
  RE -->|SR-REL-030 hasWorkflowState| WST
  RESP -->|SR-REL-027 about responsibility for| RE
  RESP -->|SR-REL-028 mediates/assignedTo| OW
```

## Foundational invariants
1. Information artifacts are not real-world events/situations.
2. Assessment Activity is an event; Assessment Result is an information object.
3. Vulnerability is an intrinsic disposition; Predisposing Condition is a situation.
4. Risk Owner is a role; Risk Responsibility is the assignment relator/context.
5. Risk State is a situation; Workflow State is an information/workflow quality.
6. Core Trigger is event-role semantics; threshold triggers stay Method/Application.
7. Risk remains a derived domain pattern rather than being forced into COVER's Quality model or a single UFO primitive.
