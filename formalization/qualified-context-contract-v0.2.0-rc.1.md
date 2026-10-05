# Qualified context: conceptual, formal and operational contract

## Knowledge boundary
Risk knowledge spans the risk phenomenon and scenario, the records describing them, contextual assessments, their evidence and provenance, and responsibility assignments. These are linked representations with different identities. A score, document update or ownership change does not create a new Risk. Numerical context is one operational view of that knowledge, not the ontology's whole domain.

## Formal commitments and local constraints
`QualifiedAssessmentResult ⊑ RiskAssessmentResult` is an OWL axiom. Controlled dimension/baseline/basis values have explicit OWL enumerations and distinct names within each enumeration. SHACL then requires a single dimension, baseline, basis, numeric value, scale, method/version, assessment time and reference instant **for this qualified data profile**. These cardinalities are not universal closed-world assertions about all enterprise risks.

For result `x` concerning `r`, the producing activity must concern the same `r` and use the recorded method/version. The value must belong to the declared numeric interval and dimension. Result supersession is acyclic, concerns the same risk and cannot go backwards in known assessment time. A supersession link records history; it does not establish causal effectiveness or numerical comparability when other context changes.

For time `t`, a risk-scoped assignment contributes its `(risk, actor)` pair iff its start is known, `start ≤ t`, any end satisfies `t < end`, and any invalidation satisfies `t < invalidation`. Missing start is unknown and excluded. Missing end is an open upper bound under this application policy. Multiple active assignments/co-owners are allowed. Entry/plan assignments are not silently reinterpreted as risk-scoped ownership. `asOf` is an explicit input, never the ambient current clock.

## RDF/SQL comparison contract
Answers use **set semantics**: duplicate assignment paths to the same pair collapse. Row ordering is only deterministic display/test order. RDF missing values map to SQL NULL for optional ownership bounds; neither becomes zero or an invented date. Numeric values use decimals. Zoned instants compare as absolute instants, including equivalent UTC and `+03:30` representations. The supported importer and timestamp parser reject zone-less input. A direct PostgreSQL `timestamptz` column cannot recover whether the caller originally omitted a timezone; no lexical enforcement claim is made for arbitrary direct SQL writes.

The round-trip checks all represented fixture assertions after decimal/timezone normalization, excluding only the explicit fixture-package annotation. It is not a lossless exporter for arbitrary RDF annotations or every SemRisk module. The included loader is explicitly synthetic and flags every instance accordingly. A real literature-case loader must separately supply source/locator and evidence-role provenance; changing the synthetic flag alone is insufficient.

## Concise manuscript paragraphs for P15
**Operationalization.** A relational projection makes selected ontology distinctions available to conventional enterprise applications. Qualified assessment results retain separate dimensions, control baselines, evidence bases, times and versioned methods and scales; responsibility is retrieved at an explicit instant. Versioned migration and RDF–SQL round-trip tests check preservation of these selected meanings. The database remains an application projection of the ontology, and the reported execution evidence is bounded to the stated synthetic fixtures.

**Formal example.** A qualified assessment result specializes Risk Assessment Result, while its completeness is checked by a local shape. A successor result must concern the same risk and preserve the predecessor as history. Ownership at time `t` is derived from qualified assignments whose validity includes `t`, with unknown starts excluded and co-owners retained. These rules distinguish a changed estimate or responsibility from a changed underlying risk situation.

Final numbered citations and manuscript tense will be bound to the accepted evidence snapshot. These paragraphs do not claim measured risk reduction or independent validation.

## Method references used in implementation
- W3C, *Shapes Constraint Language*, Recommendation, 2017: Sections 4 and 5 distinguish core constraints and SPARQL constraints. https://www.w3.org/TR/shacl/
- PostgreSQL 16 manual, Section 5.4: row checks do not by themselves guarantee cross-table invariants; this implementation uses foreign keys and explicit triggers. https://www.postgresql.org/docs/16/ddl-constraints.html
- PostgreSQL 16, `CREATE TRIGGER`: https://www.postgresql.org/docs/16/sql-createtrigger.html

These references support implementation choices, not claims of domain validity. SHACL-SPARQL is an explicit addition in this operational profile; the historical SHACL-Core-only package is unchanged.
