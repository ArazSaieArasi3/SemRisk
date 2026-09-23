# W3 #43 Acceptance Audit — Semantic Identity, IRI and Versioning

**Date:** 2026-09-23
**Result:** PASS

## Deliverables completed
- semantic identity policy;
- stable-ID/IRI rules;
- 71 conceptual-ID→formal-IRI mappings;
- ontology/module IRI registry with reserved initial formal candidate version;
- version/release policy;
- semantic change/deprecation/lineage schema;
- central semantic-lineage registry;
- exact Paper-1 release binding policy;
- exact external-dependency binding registry;
- public-IRI hosting decision;
- 15 executable/governance policy tests, all PASS.

## Acceptance verification
- Entity identity is independent of English/Persian preferred labels.
- IDs are never reused for semantically different entities.
- Rename, owner correction, semantic correction, split/merge/deprecation/replacement rules preserve lineage.
- Ontology/version IRI, component version, Git commit and planning release are explicitly different identity layers.
- Evaluation evidence cannot silently transfer across breaking semantic/constraint changes.
- Paper-1 external semantic dependencies are either exact-version/ref bound or explicitly excluded/deferred.
- gUFO is pinned to v1.0.0 / commit `12b098158a9244179c5e0e2534cd85254a2d3b7e`.
- PROV-O is bound to the W3C Recommendation dated 2013-04-30.
- OWL-Time is deliberately bound to the W3C Recommendation dated 2017-10-19 for Paper 1; later drafts do not silently replace it.
- P1-R2 and later require immutable commit/checksum/component manifests.
- No public HTTPS SemRisk IRI is claimed without an operational resolver.
- Conceptual IDs map deterministically to repository-independent URN IRIs.

## Reserved initial candidate
`v0.1.0-rc.1` is reserved for the first #27/#44 formal candidate; it is **not yet a released ontology version**.

## Boundary
PASS authorizes #27 modular OWL/SHACL implementation. It does not claim that P1-R2 exists until #27 and #44 produce and validate the actual candidate artifacts.