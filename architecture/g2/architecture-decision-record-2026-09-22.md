# ADR-G2-001 — SemRisk Paper-1 Conceptual Architecture

**Date:** 2026-09-22
**Gate:** G2
**Decision:** `CONDITIONAL_PASS`

## Architecture decision
Paper 1 uses one governed semantic architecture with a domain-neutral `Core`, bounded application/profile modules, explicit external-owner mappings and later application projections. Profiles are views/extensions over Core; they are not independent competing ontologies.

## Core inclusion rule
A concept/relation belongs to Core only when it expresses reusable risk semantics required across the bounded claims and is supported by cross-source evidence/design rationale. Frequency in Jira, Pharma, Health or a database schema is insufficient.

## Module model
- `Core`: reusable risk semantics.
- `Enterprise`: register/workflow/operational application semantics.
- `Architecture`: mapping package to externally owned objective/capability/process semantics.
- `Method`: method/scales/threshold refinements.
- `Governance`: appetite/tolerance/criteria/governance refinements.
- `Pharma`: bounded Paper-1 case/profile, federated with CM-PharmE v1.0.0.
- `Health`: deferred broad profile; not part of Paper-1 completion.
- `ExternalMappings`: COVER/ROSE/PROV-O/CM-PharmE mappings.
- `DataProjection`: later RDB/application projection; never source of ontology truth.
- `RiskIntelligence`: deferred future application.

## Dependency direction
`Core` is inward/stable. Profiles depend on Core. Mapping packages may depend on Core/profile plus pinned external owners. Application/data projections depend on approved semantic modules. Reverse dependencies into Core are prohibited.

## External ownership
- COVER/ROSE: reference/alignment dependencies; no bulk import/equivalence at G2.
- CM-PharmE v1.0.0: canonical owner of selected Pharma ecosystem concepts used by the case.
- PROV-O: preferred provenance owner for later exact predicate reuse.
- Objective/Capability/Process taxonomies: externally owned; SemRisk owns only risk-linkage semantics.
- API/INN/product terminology: currently unmapped external-owner gap; explicitly not CM-PharmE v1.0.0.

## Paper-1 boundary
Paper 1 includes Core + Enterprise/Architecture support + bounded Pharma profile/mappings. Broad Health, Newsium, Commentium, dynamic forecasting and Risk Intelligence are excluded from completion claims.

## Canonical source rule
CSV/YAML/MD registries and decisions are canonical research artifacts. Diagrams are generated/projection views and cannot introduce new semantic entities.

## Conditional-PASS condition
G2 architecture ownership/module boundaries are accepted, so #25 foundational analysis may proceed. However, **stable formalization in #26 is blocked** until #25 resolves or explicitly bounds the HIGH foundational questions for Risk/COVER Risk, Assessment activity/result vs COVER/ROSE RiskAssessment, Likelihood result vs COVER Likelihood, RiskEvent type/occurrence, ControlMechanism vs ROSE SecurityMechanism, Vulnerability/PredisposingCondition and Risk State.

## Claim consequence
Until #25 clears the condition, SemRisk may describe a governed conceptual architecture but may not claim finalized foundational categories, well-founded formalization or stable equivalence/import mappings.