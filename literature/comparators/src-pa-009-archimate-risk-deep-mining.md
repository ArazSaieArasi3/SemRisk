# SRC-PA-009 Deep Mining — Ontological Analysis and Redesign of Risk Modeling in ArchiMate

Source ID: SRC-PA-009
Citation: Sales et al. (2018), Ontological Analysis and Redesign of Risk Modeling in ArchiMate, IEEE EDOC 2018, DOI 10.1109/EDOC.2018.00028
Mining date: 2026-09-20
Status: DEEP-MINED v0.1 — full text inspected; final locator normalization remains.

## Why this source is material

This is a direct closest-work comparator for SR-RQ2 / SR-C2 because it applies ontological analysis to risk modeling in an Enterprise Architecture language and proposes a redesign of ArchiMate risk-related concepts using well-founded ontological distinctions.

SemRisk therefore must not claim novelty merely for connecting risk to Enterprise Architecture, grounding EA risk constructs in foundational ontology, or distinguishing risk-related modeling constructs through ontological analysis.

## Material semantic findings

1. Risk semantics require ontological clarification rather than direct reuse of a generic EA modeling primitive.
2. Event, situation and disposition-like distinctions are material to risk modeling.
3. Assets, value and objectives are central to risk semantics.
4. Threat and vulnerability have prior ontological treatments and cannot be treated as simple labels.
5. EA notation can hide ontological overload; this supports SemRisk anti-pattern checks for Risk vs Risk Record, Risk Event vs Scenario Description, Risk Assessment vs Assessment Result, and Risk State vs Workflow State.

## Comparator strengths relative to SemRisk

The source is stronger or already established in explicit Enterprise Architecture context, formal ontological analysis of an established EA language, redesign of risk-related EA constructs, and connection between ontological analysis and modeling-language improvement. These strengths must remain visible in E10 and novelty calibration.

## SemRisk differentiation that remains plausible

Candidate differentiators still requiring evidence are: operational risk-register information artifacts and workflow semantics; Assessment Activity vs Assessment Result; Risk State vs Workflow State; governed source-to-canonical traceability; relational projection with SQL/SPARQL parity; bounded Pharma/CM-PharmE federation; and release-bound claim calibration.

## Claim impact

- SR-CL03 Enterprise semantics: NARROWED. Ontologically grounded EA-risk linking is prior art.
- SR-CL07 Differentiation: HIGHER EVIDENCE BURDEN. This source must be included explicitly in E10.
- SR-C2: RETAINED BUT REFRAMED around the combined operationalization from well-founded Core to EA context to operational register/assessment/workflow semantics to executable projection.

## Candidate mappings for W2

- Risk Event: prior event semantics; align/reuse.
- Threat: compare COVER/ROSE/ArchiMate redesign.
- Vulnerability: align disposition semantics.
- Asset/Object at Risk: compare ownership with Business/Architecture ontologies.
- Objective/Value linkage: treat as reused/aligned context, not novelty.
- Risk Register Entry, Assessment Result, Workflow State: remain candidate differentiation points requiring direct comparison.

## Remaining extraction debt

Before G1: normalize exact page/figure/table locators; reconcile terminology against COVER/ROSE; record exact ArchiMate constructs and redesign relations in comparator registry; check newer ArchiMate-risk work for supersession/extensions.
