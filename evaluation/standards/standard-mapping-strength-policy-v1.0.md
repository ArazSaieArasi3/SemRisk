# Standard-to-SemRisk Mapping Strength Policy v1.0

**Owner:** Issue #86

Permitted mapping strengths:

- **EXACT** — source meaning and SemRisk meaning are materially coextensive for the stated scope; requires inspected authoritative definition/locator and explicit rationale.
- **CLOSE** — meanings substantially overlap but differ in scope, category, lifecycle or context.
- **BROADER** — source construct is broader than the SemRisk construct.
- **NARROWER** — source construct is narrower than the SemRisk construct.
- **RELATED** — meaningful conceptual/terminological relationship without subsumption/equivalence.
- **OPERATIONALIZES** — the source provides an operational record/process/schema realization related to a SemRisk semantic construct.
- **PROFILE_SUPPORT** — source informs a Method/Governance/Enterprise/Domain profile rather than Core identity.
- **COVERAGE_BENCHMARK** — framework used to assess scope/coverage; no semantic equivalence implied.

Rules:
1. lexical identity never implies EXACT;
2. EXACT never authorizes `owl:equivalentClass` automatically;
3. inaccessible/paywalled definition text cannot silently be reconstructed from secondary sources;
4. framework process terms remain activities/profile semantics unless independently foundationalized;
5. field/status/control labels from operational standards are mappings, not ontology classes by default.
