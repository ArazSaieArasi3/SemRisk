# R5 Enterprise Architecture / Business Architecture / Business Ontology Review Remediation Acceptance Audit — 2026-09-25

**Issues:** #91, #92, #93, #94, #95, #96  
**Origin:** specialist-style simulated Enterprise Architecture / Business Architecture / Business Ontology review (R5), used as an adversarial review aid. This is **not independent human expert validation**.

## Decision
**PASS / CLOSED for the six R5 remediations, with bounded federation scope.**

The remediation strengthens external ownership, architecture-link qualification, current reference binding, multi-ontology identity governance and dependency-direction regression without turning TOGAF/ArchiMate into canonical ontology owners or adding unsupported Core semantics.

## #91 — external enterprise ownership
Implemented:
- `evaluation/architecture/external-enterprise-ownership-state-v1.0.csv`
- SR-CPT-037/038/039 remain `UNBOUND_EXTERNAL_FAMILY` at generic Paper-1 level;
- ArchiMate 3.2 / TOGAF 10 are reference/alignment sources, not canonical semantic owners;
- CM-PharmE v1.0.0 remains profile-specific owner where exact Capability/Business Process concepts exist;
- mappings ontology scope notes updated; no local OWL classes introduced.

## #92 — qualified architecture linkage
Implemented:
- `evaluation/architecture/architecture-link-qualification-policy-v1.0.md`
- additive RDB extension `enterprise.architecture_context_link`;
- architecture-facing SR-REL-010 assertions can carry target family, effect mode, provenance and confidence;
- anticipated/realized/contextual/unknown are explicit projection qualifications;
- bare `affects` does not entail objective failure, capability degradation, process disruption or causality.

## #93 — TOGAF / ArchiMate reference binding
Implemented:
- `evaluation/architecture/ea-reference-binding-v1.0.csv`
- TOGAF Standard 10th Edition / current Technical Corrigendum 1 product family bound;
- ArchiMate Specification 3.2 bound as current reference specification;
- standards version/evidence registers and crosswalk updated;
- #13 updated but remains open for section/element-level locator depth.

## #94 — multi-ontology identity/collision
Implemented:
- `evaluation/architecture/multi-ontology-identity-collision-policy-v1.0.md`
- source identity remains `(owner_namespace, owner_semantic_id, version_ref)`;
- new `ref.external_entity_mapping` stores explicit exact/close/related/broad/narrow correspondence;
- labels never merge identity;
- no automatic `owl:sameAs` / equivalence.

Relational regression demonstrates two external entities with the same label but different owners coexist and are linked explicitly.

## #95 — dependency-direction CI guard
Implemented:
- `tools/r5_architecture_governance_check.py`
- fails if Objective/Capability/Business Process become local OWL classes;
- checks generic owner remains unbound while profile ownership stays version-bound;
- checks Core/Profile/DataProjection direction;
- checks Core does not import downstream Enterprise/Pharma/Mapping/Data modules;
- checks the RDB still declares ontology semantic authority;
- checks TOGAF/ArchiMate reference binding and EA nonclaims.

An initial Semantic CI run **36120285197** failed in the new guard because the assertion checked an exact sentence ("must not depend") while the registry used semantically equivalent wording ("cannot depend"). The invariant itself was present. The guard was corrected to test the semantic content rather than an exact phrase.

Final Semantic CI run **36120388638**: **SUCCESS**.

## #96 — bounded EA capability/nonclaim boundary
Implemented:
- `evaluation/architecture/ea-capability-nonclaim-matrix-v1.0.csv`
- direct external Objective/Capability/Business Process linkage and versioned references are DEMONSTRATED_BOUNDED;
- objective-performance causality, capability degradation, architecture dependency propagation, portfolio reasoning, architecture-change propagation, EA assurance and TOGAF/ArchiMate conformance remain NOT_DEMONSTRATED;
- manuscript/prohibited-wording controls updated.

## Relational validation
Final Relational CI run **36120289624**: **SUCCESS**.

R5 regression marker:
- `SEM_RISK_R5_MULTI_ONTOLOGY_IDENTITY_PASS`
- qualified architecture links observed: **2** (anticipated + realized for one preserved external identity).

The same run retained:
- SQL↔SPARQL parity PASS;
- cross-layer negative controls PASS;
- CQ regression PASS;
- R3 co-ownership PASS.

## Semantic validation
Final Semantic CI run **36120388638** retained:
- R1 foundational guard PASS;
- R2 formal guard PASS;
- R4 standards guard PASS;
- R5 architecture guard PASS;
- OWL 2 DL PASS;
- HermiT consistency/classification PASS;
- negative reasoner controls PASS.

Marker:
`SEM_RISK_R5_ARCHITECTURE_GOVERNANCE_PASS`.

## Residual boundary
R5 does not resolve a universal canonical Business/Enterprise ontology owner for Objective, Capability or Business Process. That remains deliberately unbound at generic Paper-1 level. Section/element-level TOGAF/ArchiMate mapping depth remains #13 debt. Advanced EA reasoning is deferred beyond Paper 1.
