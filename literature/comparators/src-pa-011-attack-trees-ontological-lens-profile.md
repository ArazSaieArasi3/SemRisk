# SRC-PA-011 Technical Deep Profile — An Ontological Lens on Attack Trees

**Source ID:** SRC-PA-011  
**Venue:** FOIS 2025, pp. 151–165  
**DOI:** 10.3233/FAIA250491  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — publisher full-text HTML inspected; figures/formal companion artifacts still require exact binding.

## 1. Material contribution

The paper applies UFO/COVER-based ontological analysis to Attack Trees and identifies four central defects:
1. ambiguous syntax/semantic overload;
2. ontological deficit / missing domain concepts;
3. insufficient modeling guidance;
4. poor semantic interoperability.

## 2. Foundational commitments

The paper explicitly distinguishes Types vs Individuals and, among concrete individuals, Events, Situations, Objects and Aspects/Dispositions/Qualities. Events manifest dispositions in situations and involve participating objects.

For risk, it adopts COVER commitments:
- risk is relative to Risk Subjects;
- risk relates to impact on goals/intentions;
- risk is experiential;
- Objects at Risk and Threat Objects participate in Risk Events;
- risk is contextual;
- uncertainty/likelihood concerns possible event types;
- incidents are realized occurrences of risks.

## 3. Attack-tree semantic overload

Attack-tree nodes can ambiguously denote:
- Intentions;
- propositions/goals;
- Objects;
- Situations;
- Events/actions;
- Event Types.

The same generic node construct therefore overloads multiple ontological categories and hides domain semantics in labels.

## 4. Ontological-analysis method

The paper operationalizes four mismatch classes:
- construct deficit / ontological incompleteness;
- construct overload;
- construct redundancy;
- construct excess.

This method lineage is directly relevant to SemRisk #23 and means SemRisk cannot claim novelty from merely using foundational ontology to diagnose a modeling language.

## 5. SemRisk implications

Already prior art:
- attack/risk-language semantic disambiguation through UFO/COVER;
- Event vs Situation vs Object vs Disposition distinctions;
- Risk Scenario / possible event vs Incident / realized occurrence;
- semantic-overload analysis;
- formal-language redesign motivated by ontology.

Candidate SemRisk differentiation remains in cross-source operational risk-register semantics, assessment-result provenance, risk-state/workflow-state separation, governed evidence traceability and bounded enterprise/Pharma projection.

## 6. Current decision

Mandatory E10/method comparator. Do not import attack-tree-specific constructs into SemRisk Core by default; classify them under Security/Assessment-Method profiles unless cross-source evidence supports Core status.