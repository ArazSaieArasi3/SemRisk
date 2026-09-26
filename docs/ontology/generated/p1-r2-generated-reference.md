# P1-R2 generated asserted import-closure reference

> Candidate `0.1.0-rc.1`; generated offline from six local modules and the catalog-bound gUFO v1.0.0 file. This is an **asserted graph**, not OWL entailment closure, independent validation or the #55 release.

The complete canonicalized graph is [`p1-r2-asserted-closure.nt`](p1-r2-asserted-closure.nt) (1409 unique triples; SHA-256 `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`). It includes anonymous OWL expressions and the vendored import. Local entity summaries below list direct URI-subject assertions from *all* seven files. Blank-node targets are represented in the canonical graph, while this readable index records their count rather than assigning unstable source-local identifiers.

## Resolved source files

| File | Git blob SHA | Asserted triples | Imports |
| --- | --- | ---: | --- |
| `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` | `cf20fe78687a4db4dcffc21e75297f6801cc5cb4` | 420 | `http://purl.org/nemo/gufo#/1.0.0` |
| `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` | `b3c559b520442423a175db72e32f8fd7384d02cb` | 62 | `urn:semrisk:ontology:core:0.1.0-rc.1` |
| `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl` | `3e6e1ec0824f266052e7c8dbcfc402b2ecdcac93` | 23 | `urn:semrisk:ontology:core:0.1.0-rc.1`, `urn:semrisk:ontology:method:0.1.0-rc.1` |
| `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` | `459145e4a1d7d1f20377b4eb2ed89b3d43e3420e` | 69 | `urn:semrisk:ontology:core:0.1.0-rc.1`, `urn:semrisk:ontology:enterprise:0.1.0-rc.1`, `urn:semrisk:ontology:pharma:0.1.0-rc.1` |
| `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` | `a265e500ee210ec3bb4bbb065524a875a8402c9b` | 54 | `urn:semrisk:ontology:core:0.1.0-rc.1` |
| `ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl` | `0fddc6e7be7db52ab75f18389a8ce7ad937cf410` | 15 | `urn:semrisk:ontology:core:0.1.0-rc.1`, `urn:semrisk:ontology:enterprise:0.1.0-rc.1` |
| `ontology/vendor/gufo-v1.0.0.ttl` | `db1dc7feb6eba2de628e3274671e0e3cfd99f09e` | 766 | none |

## Locally declared entities and cross-file assertions

### `SR-CPT-001` — Risk

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-002` — Risk Subject

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://purl.org/nemo/gufo#RoleMixin>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-003` — Risk Source

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-004` — Predisposing Condition

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 9. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Situation>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-009>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-005` — Trigger

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Event>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-006` — Risk Scenario

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://purl.org/nemo/gufo#SituationType>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-007>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-007` — Risk Event

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Event>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-008` — Consequence

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Situation>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-015>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-009` — Vulnerability

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#IntrinsicMode>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-010` — Exposure

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Situation>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-011` — Risk Assessment Activity

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Event>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-012` — Risk Assessment Method

Declared as `owl:Class` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-CPT-013` — Risk Assessment Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-014` — Likelihood Assessment Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-015` — Impact Assessment Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-016` — Risk Level Assessment Result

Declared as `owl:Class` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-CPT-017` — Inherent Risk Assessment Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-018` — Residual Risk Assessment Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-019` — Assessment Confidence

Declared as `owl:Class` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-CPT-020` — Evidence Item

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-021` — Provenance

Declared as `skos:Concept` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2004/02/skos/core#Concept>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-022` — Observation Activity

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Event>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-023` — Observation Result

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-024` — Indicator

Declared as `owl:Class` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-CPT-025` — Threshold

Declared as `owl:Class` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-CPT-026` — Risk Treatment Strategy

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-027` — Risk Treatment Plan

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-028` — Risk Treatment Activity

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Event>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-029` — Control Mechanism

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://purl.org/nemo/gufo#RoleMixin>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-030` — Risk Owner

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://purl.org/nemo/gufo#Role>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-031` — Risk Responsibility

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Relator>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-032` — Risk Register

Declared as `owl:Class` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-CPT-033` — Risk Register Entry

Declared as `owl:Class` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-001>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-CPT-034` — Scenario Description

Declared as `owl:Class` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-006>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-007>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-CPT-035` — Risk State

Declared as `owl:Class` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#subClassOf` → `<http://purl.org/nemo/gufo#Situation>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-CPT-036` — Workflow State

Declared as `owl:Class` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#Class>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2002/07/owl#disjointWith` → `<urn:semrisk:entity:SR-CPT-035>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-CPT-037` — Objective

Declared as `skos:Concept` in `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2004/02/skos/core#Concept>` (`ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`)

### `SR-CPT-038` — Capability

Declared as `skos:Concept` in `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2004/02/skos/core#Concept>` (`ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`)

### `SR-CPT-039` — Business Process

Declared as `skos:Concept` in `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2004/02/skos/core#Concept>` (`ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`)

### `SR-REL-001` — concernsRisk

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 1. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-001>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-REL-002` — describesScenario

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6, `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-034>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-006>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-REL-003` — realizedAs

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-006>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-007>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-004` — hasConsequence

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-008>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-005` — hasRiskSource

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-003>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-006` — predisposedBy

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-004>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-007` — triggeredBy

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-007>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-005>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-008` — causes

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 3. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-009` — associatedWith

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-010` — affects

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-011` — exposes

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-012` — hasVulnerability

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-009>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-013` — performedAssessmentOf

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-011>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-001>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-014` — usesAssessmentMethod

Declared as `owl:ObjectProperty` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-011>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-012>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-REL-015` — producesAssessmentResult

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-011>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-016` — assessmentResultConcerns

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-001>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-017` — supportedByEvidence

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-020>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-018` — generatedByObservation

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-023>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-022>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-019` — hasProvenance

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-020` — qualifiedByConfidence

Declared as `owl:ObjectProperty` in `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-019>` (`ontology/method/semrisk-method-v0.1.0-rc.1.ttl`)

### `SR-REL-021` — selectsTreatmentStrategy

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-026>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-022` — planImplementsStrategy

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-027>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-026>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-023` — activityExecutesPlan

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-028>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-027>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-024` — activityUsesControl

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-028>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-029>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-025` — controlProtects

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7, `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl` 2. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-029>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-026` — hasRiskOwner

Declared as `owl:ObjectProperty` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-REL-027` — assignsResponsibilityFor

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-031>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-028` — responsibilityAssignedTo

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-031>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-029` — registerContainsEntry

Declared as `owl:ObjectProperty` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-032>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-033>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-REL-030` — hasWorkflowState

Declared as `owl:ObjectProperty` in `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-033>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-036>` (`ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`)

### `SR-REL-031` — hasRiskState

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-001>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-035>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-032` — precedesState

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-033` — supersedesAssessmentResult

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#domain` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-013>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-034` — basedOnPriorAssessment

Declared as `owl:ObjectProperty` in `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl` 6. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/core/semrisk-core-v0.1.0-rc.1.ttl`)

### `SR-REL-035` — hasIndicator

Declared as `owl:ObjectProperty` in `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-024>` (`ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`)

### `SR-REL-036` — hasThreshold

Declared as `owl:ObjectProperty` in `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl` 8. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`)
- `http://www.w3.org/2000/01/rdf-schema#range` → `<urn:semrisk:entity:SR-CPT-025>` (`ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`)

### `SR-REL-037` — pharmaEntityInRiskContext

Declared as `owl:ObjectProperty` in `ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl`. Direct assertion counts by source: `ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl` 7. Anonymous-expression targets: 0.

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type` → `<http://www.w3.org/2002/07/owl#ObjectProperty>` (`ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl`)

## Interpretation boundary

The `.nt` file contains every *asserted* triple in the catalog-resolved files. Duplicate triples across files collapse in the union. The Markdown index is a convenience projection and does not replace the Turtle sources or list every vendor term. No OWL inference, SHACL result, SQL constraint or live Wiki/Pages publication is implied.
