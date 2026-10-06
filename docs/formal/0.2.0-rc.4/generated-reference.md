# rc.4 generated asserted reference

This is a read-only source projection. The [curated FD-A–FD-J reference](../formal-ontology-description-rc4.md) explains scope and interpretation.

- Seven modules and one pinned local gUFO file
- 1618 unique asserted triples; 116 declared local entities
- 47 conceptual rows and 40 registered relation rows; helpers have separate identity
- The [complete canonical graph](asserted-closure.nt) includes anonymous expressions and imported statements.
- The [entity inventory](entity-inventory.csv) includes all local declarations and URI-target structural assertions from all local modules. It is not an entailment inventory.

## Source-bound modules

| Module | Ontology/version IRIs | Direct imports |
| --- | --- | --- |
| core | urn:semrisk:ontology:core, urn:semrisk:ontology:core:0.2.0-rc.4 | http://purl.org/nemo/gufo#/1.0.0 |
| enterprise | urn:semrisk:ontology:enterprise, urn:semrisk:ontology:enterprise:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4 |
| method | urn:semrisk:ontology:method, urn:semrisk:ontology:method:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4 |
| governance | urn:semrisk:ontology:governance, urn:semrisk:ontology:governance:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4, urn:semrisk:ontology:method:0.2.0-rc.4 |
| pharma | urn:semrisk:ontology:pharma, urn:semrisk:ontology:pharma:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4, urn:semrisk:ontology:enterprise:0.2.0-rc.4 |
| mappings | urn:semrisk:ontology:mappings, urn:semrisk:ontology:mappings:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4, urn:semrisk:ontology:enterprise:0.2.0-rc.4, urn:semrisk:ontology:pharma:0.2.0-rc.4 |
| assessment-context | urn:semrisk:ontology:assessment-context, urn:semrisk:ontology:assessment-context:0.2.0-rc.4 | urn:semrisk:ontology:core:0.2.0-rc.4, urn:semrisk:ontology:method:0.2.0-rc.4 |

## Complete local entity index

### `urn:semrisk:entity:SR-CPT-001`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-013`

### `urn:semrisk:entity:SR-CPT-002`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#RoleMixin`, `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:entity:SR-CPT-003`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:entity:SR-CPT-004`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Situation`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-009`

### `urn:semrisk:entity:SR-CPT-005`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Event`

### `urn:semrisk:entity:SR-CPT-006`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#SituationType`
- `http://www.w3.org/2002/07/owl#disjointWith`: `http://purl.org/nemo/gufo#Individual`, `urn:semrisk:entity:SR-CPT-007`

### `urn:semrisk:entity:SR-CPT-007`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Event`

### `urn:semrisk:entity:SR-CPT-008`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Situation`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-015`

### `urn:semrisk:entity:SR-CPT-009`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#IntrinsicMode`

### `urn:semrisk:entity:SR-CPT-010`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Situation`

### `urn:semrisk:entity:SR-CPT-011`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Event`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-013`

### `urn:semrisk:entity:SR-CPT-012`

class in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-013`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-014`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`, `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-015`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`, `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-016`

class in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`, `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-017`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`, `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-018`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`, `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-019`

class in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-020`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#Role`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ManagedInformationArtifact`

### `urn:semrisk:entity:SR-CPT-021`

marker in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2004/02/skos/core#Concept`

### `urn:semrisk:entity:SR-CPT-022`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Event`

### `urn:semrisk:entity:SR-CPT-023`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-024`

class in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-025`

class in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-026`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-027`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:entity:SR-CPT-028`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Event`

### `urn:semrisk:entity:SR-CPT-029`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#RoleMixin`, `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:entity:SR-CPT-030`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#RoleMixin`, `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:entity:SR-CPT-031`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Relator`

### `urn:semrisk:entity:SR-CPT-032`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ManagedInformationArtifact`

### `urn:semrisk:entity:SR-CPT-033`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ManagedInformationArtifact`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-001`

### `urn:semrisk:entity:SR-CPT-034`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-006`, `urn:semrisk:entity:SR-CPT-007`

### `urn:semrisk:entity:SR-CPT-035`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Situation`

### `urn:semrisk:entity:SR-CPT-036`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#AbstractIndividualType`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#QualityValue`
- `http://www.w3.org/2002/07/owl#disjointWith`: `urn:semrisk:entity:SR-CPT-035`

### `urn:semrisk:entity:SR-CPT-037`

marker in `ontology/releases/0.2.0-rc.4/mappings.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2004/02/skos/core#Concept`

### `urn:semrisk:entity:SR-CPT-038`

marker in `ontology/releases/0.2.0-rc.4/mappings.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2004/02/skos/core#Concept`

### `urn:semrisk:entity:SR-CPT-039`

marker in `ontology/releases/0.2.0-rc.4/mappings.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2004/02/skos/core#Concept`

### `urn:semrisk:entity:SR-REL-001`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-001`

### `urn:semrisk:entity:SR-REL-002`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-034`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-006`

### `urn:semrisk:entity:SR-REL-003`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-006`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-007`

### `urn:semrisk:entity:SR-REL-004`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-008`

### `urn:semrisk:entity:SR-REL-005`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-003`

### `urn:semrisk:entity:SR-REL-006`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-004`

### `urn:semrisk:entity:SR-REL-007`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-007`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-005`

### `urn:semrisk:entity:SR-REL-008`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-009`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-010`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-011`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-012`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-009`

### `urn:semrisk:entity:SR-REL-013`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-011`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-001`

### `urn:semrisk:entity:SR-REL-014`

object_property in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-011`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-012`

### `urn:semrisk:entity:SR-REL-015`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-011`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-013`

### `urn:semrisk:entity:SR-REL-016`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-013`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-001`

### `urn:semrisk:entity:SR-REL-017`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-020`

### `urn:semrisk:entity:SR-REL-018`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-023`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-022`

### `urn:semrisk:entity:SR-REL-019`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-020`

object_property in `ontology/releases/0.2.0-rc.4/method.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-013`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-019`

### `urn:semrisk:entity:SR-REL-021`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-026`

### `urn:semrisk:entity:SR-REL-022`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-027`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-026`

### `urn:semrisk:entity:SR-REL-023`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-028`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-027`

### `urn:semrisk:entity:SR-REL-024`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-028`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-029`

### `urn:semrisk:entity:SR-REL-025`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-029`

### `urn:semrisk:entity:SR-REL-026`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-027`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-031`

### `urn:semrisk:entity:SR-REL-028`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-031`

### `urn:semrisk:entity:SR-REL-029`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-032`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-033`

### `urn:semrisk:entity:SR-REL-030`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-033`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-036`

### `urn:semrisk:entity:SR-REL-031`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-001`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-035`

### `urn:semrisk:entity:SR-REL-032`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-033`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-013`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-013`

### `urn:semrisk:entity:SR-REL-034`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-035`

object_property in `ontology/releases/0.2.0-rc.4/governance.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-024`

### `urn:semrisk:entity:SR-REL-036`

object_property in `ontology/releases/0.2.0-rc.4/governance.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-025`

### `urn:semrisk:entity:SR-REL-037`

object_property in `ontology/releases/0.2.0-rc.4/pharma.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`

### `urn:semrisk:entity:SR-REL-038`

annotation_property in `ontology/releases/0.2.0-rc.4/mappings.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#AnnotationProperty`

### `urn:semrisk:entity:SR-REL-039`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-010`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-002`

### `urn:semrisk:entity:SR-REL-040`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-010`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-003`

### `urn:semrisk:profile:assessment-context:AfterControl`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:ControlBaseline`

### `urn:semrisk:profile:assessment-context:BeforeControl`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:ControlBaseline`

### `urn:semrisk:profile:assessment-context:ControlBaseline`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:profile:assessment-context:Dimension`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:profile:assessment-context:EvaluationBasis`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`

### `urn:semrisk:profile:assessment-context:GroundedRiskResponsibility`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-031`

### `urn:semrisk:profile:assessment-context:Impact`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:Dimension`

### `urn:semrisk:profile:assessment-context:Likelihood`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:Dimension`

### `urn:semrisk:profile:assessment-context:NumericScale`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:profile:assessment-context:Observed`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:EvaluationBasis`

### `urn:semrisk:profile:assessment-context:Projected`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:EvaluationBasis`

### `urn:semrisk:profile:assessment-context:QualifiedAssessmentResult`

class in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:entity:SR-CPT-013`

### `urn:semrisk:profile:assessment-context:RiskLevel`

named_individual in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#NamedIndividual`, `urn:semrisk:profile:assessment-context:Dimension`

### `urn:semrisk:profile:assessment-context:assessedAt`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#dateTime`

### `urn:semrisk:profile:assessment-context:controlBaseline`

object_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:assessment-context:ControlBaseline`

### `urn:semrisk:profile:assessment-context:dimension`

object_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:assessment-context:Dimension`

### `urn:semrisk:profile:assessment-context:evaluationBasis`

object_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:assessment-context:EvaluationBasis`

### `urn:semrisk:profile:assessment-context:maximum`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#decimal`

### `urn:semrisk:profile:assessment-context:method`

object_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-012`

### `urn:semrisk:profile:assessment-context:methodVersion`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#string`

### `urn:semrisk:profile:assessment-context:minimum`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#decimal`

### `urn:semrisk:profile:assessment-context:numericValue`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#decimal`

### `urn:semrisk:profile:assessment-context:referenceTime`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#dateTime`

### `urn:semrisk:profile:assessment-context:scale`

object_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:assessment-context:NumericScale`

### `urn:semrisk:profile:assessment-context:validFrom`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#dateTime`

### `urn:semrisk:profile:assessment-context:validTo`

datatype_property in `ontology/releases/0.2.0-rc.4/assessment-context.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#DatatypeProperty`
- `http://www.w3.org/2000/01/rdf-schema#range`: `http://www.w3.org/2001/XMLSchema#dateTime`

### `urn:semrisk:profile:information-state:ArtifactVersion`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ManagedInformationArtifact`

### `urn:semrisk:profile:information-state:InformationContent`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#AbstractIndividualType`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#AbstractIndividual`

### `urn:semrisk:profile:information-state:ManagedInformationArtifact`

class in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#Kind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#FunctionalComplex`

### `urn:semrisk:profile:information-state:WorkflowAssignment`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SituationType`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `http://purl.org/nemo/gufo#Situation`

### `urn:semrisk:profile:information-state:WorkflowSchemeVersion`

class in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://purl.org/nemo/gufo#SubKind`, `http://www.w3.org/2002/07/owl#Class`
- `http://www.w3.org/2000/01/rdf-schema#subClassOf`: `urn:semrisk:profile:information-state:ArtifactVersion`

### `urn:semrisk:profile:information-state:expressesContent`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:profile:information-state:ArtifactVersion`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:information-state:InformationContent`

### `urn:semrisk:profile:information-state:inScheme`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:entity:SR-CPT-036`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:information-state:WorkflowSchemeVersion`

### `urn:semrisk:profile:information-state:record`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:profile:information-state:WorkflowAssignment`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-033`

### `urn:semrisk:profile:information-state:scheme`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:profile:information-state:WorkflowAssignment`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:information-state:WorkflowSchemeVersion`

### `urn:semrisk:profile:information-state:value`

object_property in `ontology/releases/0.2.0-rc.4/enterprise.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:profile:information-state:WorkflowAssignment`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:entity:SR-CPT-036`

### `urn:semrisk:profile:information-state:versionOf`

object_property in `ontology/releases/0.2.0-rc.4/core.ttl`

- `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`: `http://www.w3.org/2002/07/owl#ObjectProperty`
- `http://www.w3.org/2000/01/rdf-schema#domain`: `urn:semrisk:profile:information-state:ArtifactVersion`
- `http://www.w3.org/2000/01/rdf-schema#range`: `urn:semrisk:profile:information-state:ManagedInformationArtifact`
