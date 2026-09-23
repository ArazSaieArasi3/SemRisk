# E4 Foundational/OntoUML Baseline — SemRisk Paper 1

**Date:** 2026-09-23
**Issue owner:** #25
**Baseline result:** `PASS_FOR_FOUNDATIONAL_DESIGN`

## Scope
This E4 baseline evaluates whether the Paper-1 conceptual subset has explicit foundational analysis sufficient to guide formalization. It is not an independent expert validation and does not establish overall ontology correctness.

## Coverage
- Release-critical concepts reviewed: **33/33**.
- Release-critical relations reviewed: **38/38**.
- G2 HIGH foundational conditions resolved: **7/7**.
- Foundational anti-patterns recorded/rechecked: **15**, all remediated or controlled.
- Alternative categorizations preserved: **7**.
- Remaining foundational questions: **6 nonblocking**.

## Key resolved distinctions
- Risk remains a derived domain pattern rather than forced into COVER's Quality model.
- Risk Scenario is type/pattern-level; Risk Event is occurrence-level Event; Scenario Description is Information Object.
- Assessment Activity is Event/Action; Assessment Result and likelihood/impact/inherent/residual results are Information Objects.
- Vulnerability is intrinsic disposition; Predisposing Condition is Situation.
- Control Mechanism is a cross-domain RoleMixin with optional control-capability helper; ROSE SecurityMechanism is a narrower specialization/reference.
- Risk Owner is Role; Risk Responsibility is Relator; ownership relation is derived from assignment context.
- Risk State is Situation; Workflow State is a quality/value of a managed information/workflow artifact.

## Evidence
- exact pinned COVER artifact;
- exact corrected ROSE artifact;
- G1/UL/CQ/Core/relations registries;
- CM-PharmE v1.0.0 category-preservation bridge;
- OntoUML/UFO/gUFO role/relator/event/situation/quality patterns.

## Limitation
E4 here is design-time foundational verification. It must be rechecked against the actual OntoUML/OWL artifacts and later independent/domain evaluation. Use of UFO/gUFO/OntoUML is not itself proof of semantic validity.