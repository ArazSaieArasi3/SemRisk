# SemRisk Conceptual→Formal Translation Contract v0.1

**Date:** 2026-09-23  
**Issue:** #26  
**Status:** FROZEN POLICY — implementation starts only after #43 identity/version policy.

## Canonical authoring
- Canonical ontology authoring serialization: **Turtle (.ttl)**.
- Canonical SHACL serialization: **Turtle (.ttl)** in separate shape graphs.
- RDF/XML and JSON-LD may be generated distributions; they are never hand-edited sources of truth.
- Deterministic generation/validation belongs to #44.

## OWL target
SemRisk targets **OWL 2 DL**. The model may require disjointness, inverses, conservative existential restrictions and legal metamodel/punning patterns. #27 must report the actual used fragment and remain as conservative as possible.
OWL represents **open-world semantic commitments**, not application completeness.

## SHACL target
Use **SHACL Core first**. SHACL-SPARQL is allowed only for claim-required constraints not adequately expressible in Core, and each such constraint must be separately identified and tested.
Shape severity: `Violation` = release/application requirement failure; `Warning` = quality/recommended completeness; `Info` = advisory. Severity cannot downgrade a claim-critical failure.

## Rules and calculations
Risk-score formulas, thresholds, derived classifications, workflow transitions, temporal current-state selection and similar business/method logic are versioned rule/application-profile semantics, not timeless OWL definitions.
No rule language is mandated until #27/#44 demonstrates a Paper-1 need. Every executable rule needs stable ID, assumptions, method/profile version, deterministic expected output, provenance and regression test.

## RDB
PostgreSQL constraints implement projection integrity. PK/FK/UNIQUE/NOT NULL/CHECK/trigger choices do not become ontology truths unless independently justified by the semantic contract. #49 owns OWA/CWA and semantic-loss analysis.

## Provenance
Prefer qualified **PROV-O** generation, derivation, attribution and revision patterns after #43 binds an exact dependency. SemRisk metadata adds semantic IDs, evidence role, mapping decision, release/build and CQ/claim links.

## Imports and mappings
- COVER/ROSE: reference/alignment, no bulk import.
- CM-PharmE: external-owner bridge; no redistribution/import assumption before license resolution.
- gUFO/PROV-O/OWL-Time: exact release/IRI/import strategy must be bound in #43.
- No `owl:equivalentClass` or `owl:equivalentProperty` from lexical similarity.
- Prefer governed SKOS/annotation mappings until equivalence burden is met.

## Identity
`SR-CPT-*` / `SR-REL-*` remain stable conceptual IDs. #26 does not invent public IRIs. #43 defines conceptual-ID→IRI and version/hosting policy.

## Semantic-change rule
If formal implementation requires collapsing/changing a #25 distinction, implementation stops and the semantic decision is reopened. Syntax convenience is never sufficient reason.