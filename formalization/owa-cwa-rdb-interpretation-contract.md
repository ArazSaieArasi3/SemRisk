# OWA / CWA / RDB Interpretation Contract

## OWL / OWA
- Missing triple means **unknown**, not false.
- Absence of an owner, assessment, consequence or provenance assertion does not by itself prove the entity lacks one.
- Universal semantic restrictions must be justified by #7/#25, not by form/database requirements.

## SHACL / scoped CWA
- SHACL validates a **named target graph/profile** under declared completeness assumptions.
- A SHACL violation means the data/package fails that profile requirement; it does not make the OWL ontology inconsistent.
- Shapes may be stricter than Core ontology because evaluated applications require complete fields.

## PostgreSQL / implementation CWA
- SQL tables operate with schema constraints and NULL semantics chosen for the projection.
- `NOT NULL`, FK, UNIQUE and CHECK constraints are implementation integrity controls unless independently elevated by semantic evidence.
- A SQL `NULL`, absent row and absent RDF triple are not automatically equivalent meanings.

## Required #49 parity notes
Every SQL↔SPARQL parity test must state: graph/table completeness assumptions, null-vs-absence handling, inferred-vs-asserted triples, duplicate/set semantics, current-vs-history snapshot rule, and any profile filtering.

## Paper-1 reporting rule
Do not describe OWL, SHACL and RDB PASS rates as one interchangeable correctness measure. Report them as separate verification/projection dimensions.