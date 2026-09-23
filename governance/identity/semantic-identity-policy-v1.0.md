# SemRisk Semantic Identity Policy v1.0

**Frozen:** 2026-09-23  
**Issue:** #43

## 1. Identity layers
SemRisk distinguishes five identities that must never be conflated:
1. **Semantic entity identity** — stable `SR-*` identifier for a concept/relation/shape/rule/etc.
2. **Formal IRI identity** — machine identifier for that semantic entity.
3. **Artifact version identity** — version of ontology/shape/mapping/RDB/evaluation artifact.
4. **Repository state identity** — exact Git commit SHA.
5. **Planning/research release identity** — `P1-R0`…`P1-R5`, which coordinates gates but is not an ontology version.

## 2. Stable semantic IDs
- Existing `SR-CPT-*` and `SR-REL-*` IDs are permanent once released into a governed baseline.
- Future namespaces: `SR-SHP-*`, `SR-RULE-*`, `SR-MAP-*`, `SR-DATA-*`, `SR-EVAL-*`, `SR-TEST-*`.
- An ID is label-independent and repository-location-independent.
- IDs are never recycled, even after deprecation.
- Editorial rename with unchanged identity keeps the same ID.
- Semantic split creates new IDs for every successor; predecessor is deprecated with `splitInto` lineage.
- Semantic merge creates a new ID unless one predecessor is demonstrably identity-preserving; default is new ID.

## 3. Formal IRIs
Until a persistent HTTPS resolution service is actually configured and tested, SemRisk uses repository-independent **URN IRIs**:
- entity: `urn:semrisk:entity:<stable-id>`
- ontology: `urn:semrisk:ontology:<module>`
- ontology version: `urn:semrisk:ontology:<module>:<semantic-version>`
- shape: `urn:semrisk:shape:<stable-id>`
- rule: `urn:semrisk:rule:<stable-id>`
- release bundle: `urn:semrisk:release:<release-id>`

A future public HTTPS namespace is **reserved conceptually but unclaimed**. It may be introduced only after resolution/redirect ownership is operational and tested. Public aliasing/migration must preserve the URN lineage; it cannot silently replace semantic identity.

## 4. Repository relocation
Moving/renaming the GitHub repository does not change any semantic ID or URN. GitHub URLs are distribution locations and provenance refs, not semantic identity.

## 5. Labels
`rdfs:label`, Persian/English preferred terms, abbreviations and UI names are mutable annotations. No entity IRI is generated from a label.

## 6. Evaluation inheritance
Evaluation evidence attaches to an exact semantic release manifest + artifact versions + commit/checksums. It may transfer only across a declared non-semantic/evidence-only change or after explicit impact analysis/regression. Breaking semantic changes never inherit prior evaluation silently.

## 7. Scholarly binding
Manuscript claims/tables/figures must cite a publication-bound release manifest that records semantic artifact versions, exact Git commit(s), dependency refs, dataset refs/checksums, test/evaluation package versions and claim-register revision.

## 8. Mutable branches
`main`, `master`, `latest`, a working directory, or an unpinned URL is development location only. None is a scholarly semantic identity.