# SRC-ON-004 Deep Profile and Artifact Binding — RISKMAN

**Source ID:** SRC-ON-004  
**Canonical repository:** `cl-tud/riskman`  
**W1 bound commit:** `c046c5d1d5f13abc4241e6f7c0e48f0828df01df`  
**Ontology:** `ontology-1.0.0.ttl`, blob `aff89433467b60a78b7cf3f039b3fc2171629098`  
**SHACL:** `shapes-1.0.0.ttl`, blob `befee38dbd478f7a90d54b9f058d4129f2010218`  
**Version IRI:** `https://w3id.org/riskman/ontology/1.0.0`  
**License:** CC BY 4.0 (ontology annotation)  
**Peer-reviewed paper:** DOI `10.3233/SSW250023`, SEMANTiCS 2025.

## 1. Scope

RISKMAN represents and validates medical-device risk-management documentation grounded in ISO 14971 and VDE Spec 90025. Its central reusable artifact is the Safe Design Argument (SDA), which captures how a hazard associated with a device is mitigated under contextual information/assumptions.

## 2. Formal implementation

The public release includes both OWL/RDF ontology artifacts and SHACL shapes. The shapes enforce structural requirements such as cardinalities over analyzed risk, hazards, harms, device contexts, hazardous situations and risk levels.

## 3. SemRisk consequence

Already prior art:
- ontology-backed medical-device risk documentation;
- explicit risk-management information artifacts;
- ISO-14971-oriented semantic modeling;
- executable SHACL validation over risk-management records;
- reusable safety/design argument structures.

Therefore SemRisk's Health/medical-device contribution cannot be generic ontology+SHACL documentation validation.

## 4. Boundary

RISKMAN is medical-device/safety focused. It does not by itself establish the broader enterprise risk-register semantics, cross-domain reusable Core, Risk State vs Workflow State distinction, CM-PharmE federation, or SQL↔SPARQL projection-fidelity program planned by SemRisk.

## 5. W1 decision

`EXACT_ARTIFACT_BOUND / MANDATORY HEALTH+METHOD COMPARATOR`.

Artifact identity/version/license are sufficiently pinned for W1 comparison. Any detailed reuse/equivalence decision remains owned by #21/#24.

## 6. Downstream routing

- #4 Health evidence boundary;
- #14 closest work;
- #21 reuse/alignment;
- #23 method comparison;
- #26 SHACL policy;
- #30/#31 evaluation/comparison;
- #53 claim calibration.