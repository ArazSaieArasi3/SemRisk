# SemRisk–CM-PharmE Bounded Pharma Case v0.1

**Case purpose:** evaluate whether SemRisk Core semantics can be federated into a pharmaceutical ecosystem context while preserving CM-PharmE ownership.

## Case frame
`Pharmaceutical ecosystem supply disruption → affected enterprise capability / pharmaceutical business process / supply capacity → risk scenario/event/consequence → assessment/evidence → treatment/control → residual/reassessment → responsible actor → risk-register workflow`

## External Pharma context from CM-PharmE v1.0.0
- `CMPE-C0001 Pharmaceutical Enterprise` — kind.
- `CMPE-C0005 Enterprise Capability` — mode.
- `CMPE-C0015 Pharmaceutical Business Process` — perdurant.
- `CMPE-C0010 Ecosystem Demand Signal` — mode.
- `CMPE-C0011 Ecosystem Supply Capacity` — mode.
- `CMPE-C0032 Supply Chain Relationship` — relator.
- `CMPE-C0003 Organizational Stakeholder` / `CMPE-C0008 Ecosystem Actor` — roles.
- `CMPE-C0028 Risk Management Activity` — perdurant.

## SemRisk-owned pattern
- Risk, Risk Source, Predisposing Condition, Trigger, Risk Scenario, Risk Event, Consequence;
- Risk Assessment Activity / Result, Likelihood / Impact / Inherent / Residual result;
- Evidence Item and Provenance;
- Risk Treatment Strategy / Plan / Activity / Control Mechanism;
- Risk Owner / Risk Responsibility;
- Risk Register Entry, Risk State, Workflow State.

## Example semantic sequence
1. A `Supply Chain Relationship` and `Ecosystem Supply Capacity` establish external Pharma context.
2. A SemRisk `Risk Source` and/or `Predisposing Condition` concerns that context.
3. A `Risk Scenario` represents a possible pharmaceutical supply disruption.
4. A realized disruption is represented as `Risk Event`, not as a Risk Register Entry.
5. The event/scenario may `affect` `Enterprise Capability`, `Pharmaceutical Business Process`, `Ecosystem Supply Capacity` or `Pharmaceutical Enterprise`.
6. A `Risk Assessment Activity` uses evidence and method to produce contextual assessment results.
7. A treatment strategy/plan/activity may involve a CM-PharmE `Risk Management Activity` as external Pharma process context plus SemRisk control/treatment semantics.
8. An `Organizational Stakeholder` or `Ecosystem Actor` may bear the SemRisk `Risk Owner` role.
9. A `Risk Register Entry` records the management view; its Workflow State remains distinct from Risk State.
10. Reassessment may supersede prior results while preserving history/provenance.

## Evidence-role discipline
- CM-PharmE v1.0.0: design/federation evidence; not independent validation of the bridge it determines.
- Pharma literature/standards used to define the case: design/reconciliation evidence.
- DS-003: bounded qualitative design/case evidence.
- DS-004: preferred structured case/mapping evidence after exact file freeze; currently not file-level evaluation-ready.
- DS-002: optional record-level transferability holdout candidate only under its frozen protocol.
- Synthetic fixtures: regression/illustration only.

## Important correction
`Active Pharmaceutical Ingredient`, medicine/product identity, dosage form and related product-level terminology are **not present in the frozen 39-concept CM-PharmE v1.0.0 catalog**. They therefore must not be represented as CM-PharmE-owned classes in the Paper-1 bridge. If DS-004 product/API-level records are used later, #28/#47 must bind an appropriate external terminology or retain an explicit unmapped-data status.

## Nonclaims
This case does not validate all Pharma, Health or supply-chain domains. It does not prove universal Core transferability and does not turn CM-PharmE into a risk ontology.