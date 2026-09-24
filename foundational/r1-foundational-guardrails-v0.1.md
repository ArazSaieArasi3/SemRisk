# R1 Foundational Guardrails v0.1

**Owner:** Issue #72  
**Status:** FROZEN_GUARDRAILS

## Guardrail G-R1-01 — Risk Source is cross-category
SR-CPT-003 Risk Source is a contextual/source role pattern that may be played by entities from different foundational categories. Canonical SemRisk ontology sources MUST NOT:
- make Risk Source a subclass/equivalent class of one gUFO primitive such as Event, Situation, Endurant, Object, Relator, Quality or IntrinsicMode;
- use lexical source labels as evidence for causal semantics.

Typed/profile refinements may specialize source roles where the underlying category is known.

## Guardrail G-R1-02 — Provenance is PROV-O pattern, not local domain class
SR-CPT-021 Provenance remains a governed conceptual marker whose formal realization reuses qualified PROV-O patterns. Canonical ontology sources MUST NOT declare `urn:semrisk:entity:SR-CPT-021` as a local `owl:Class`.

Source mappings may continue to map operational fields to the conceptual semantic ID SR-CPT-021 for traceability.

## Guardrail G-R1-03 — Risk remains unstereotyped by convenience
SR-CPT-001 Risk MUST NOT acquire a single gUFO primitive merely to satisfy OWL/RDB convenience. Any future foundational revision requires a separate governed decision and impact analysis.

## Guardrail G-R1-04 — tests are prevention, not proof
Passing these checks prevents specific anti-pattern regressions; it does not prove the universal correctness of the SemRisk foundational model.
