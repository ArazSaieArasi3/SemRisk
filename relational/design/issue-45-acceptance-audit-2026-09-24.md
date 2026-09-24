# W3A #45 Acceptance Audit — Ontology-Grounded Relational Projection Design

**Date:** 2026-09-24
**Result:** PASS

## Deliverables completed
- relational design specification;
- PostgreSQL target and schema/subject-area architecture;
- 45-table/view catalog;
- 210-field field-level catalog with semantic/helper/provenance/data classification;
- 20 explicit PK/FK/check/uniqueness/temporal/provenance constraints;
- 71/71 release-critical SemRisk concept/relation mappings;
- Master ERD plus Core/Assessment and Enterprise/Treatment/Pharma subject-area ERDs;
- 14 explicit semantic-loss/mismatch findings;
- DDL/migration implementation plan for #46;
- 12 predeclared query/parity test intentions for #48/#49.

## Coverage verification
- Release-critical semantic IDs in formal inventory: **71**.
- Unique IDs represented in ontology↔RDB mapping registry: **71**.
- Missing release-critical IDs: **0**.
- All 38 release-critical relations have a relational representation or intentional metadata/non-runtime disposition.

## Acceptance findings
- Risk, Risk Scenario, Risk Event, Risk Register Entry, Scenario Description, Assessment Activity, Assessment Result, Risk State and Workflow State remain structurally distinct.
- Inherent/residual are assessment-result kinds over the same Risk identity.
- Risk Owner is not a primitive actor subtype or primitive owner column; it is derived from Risk Responsibility.
- CM-PharmE/Enterprise external entities retain external ownership through ref.external_entity.
- Provenance/source/version/evidence role are first-class projection metadata.
- Cross-category relation storage is whitelisted and cannot become a generic EAV/graph escape hatch.
- Database constraints are explicitly labeled profile/projection integrity and are not ontology axioms.
- OWA/CWA/null differences are carried into the #49 query plan.
- Expected lossy mappings are explicit rather than hidden.

## Negative checks
- no one-table-per-class mechanical export;
- no generic EAV attribute model;
- no conflated Risk State/Workflow State;
- no duplicate inherent/residual Risk rows;
- no primitive owner field as semantic truth;
- no future Risk Intelligence scope in the Paper-1 RDB design.

## Boundary
PASS freezes the design only. #46 must implement the PostgreSQL schema from controlled migrations and prove catalog/DDL consistency; #47–#49 own data load, end-to-end execution and SQL↔SPARQL parity.