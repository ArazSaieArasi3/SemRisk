# SemRisk Pharma Ontology Prior-Art Lineages — Paper 1

**Updated:** 2026-09-21  
**Purpose:** prevent duplicate counting, novelty inflation and accidental reimplementation of pharmaceutical risk semantics.

## Lineage A — Moroccan medicines/pharmaceutical supply-risk ontology programme

### A1 — SRC-PH-011 (2017)
*Ontology for Risks in Medicines Supply Chain: Case of Public Hospitals in Morocco*.

Core contribution:
- medicines-supply risk ontology for Moroccan public hospitals;
- OWLGred from UML toward OWL;
- multi-partner semantic interoperability;
- risk identification/classification and decision support.

### A2 — SRC-PH-012 (published online 2017)
*A new approach for the conception of an information system related to the medicines supply chain in Morocco*.

Adjacent contribution:
- UML-based modeling of the medicines supply chain, partner interactions and associated risks;
- information-system design context around the same problem space.

### A3 — SRC-PH-009 (PDF 2020 / metadata 2021)
*Domain Ontology for Risks Management in Pharmaceutical Supply Chain*.

Follow-up contribution:
- six-category pharmaceutical supply-risk taxonomy;
- strategic/tactical/operational classification;
- ontology lifecycle and UML→OWL/OWLGred method;
- partner-oriented risk-management decision support.

**Counting rule:** one evolving research programme with distinct publications; cite distinct contributions when needed but do not count them as independent repetitions of the same novelty gap.

## Lineage B — Operational risk ontology + FQFD application

### B1 — reused operational-risk ontology / 3PL antecedent
Exact ontology publication/artifact to be bound from SRC-PH-008 reference [28].

### B2 — SRC-PH-008 (2020)
*Operational Risk Management in the Pharmaceutical Supply Chain Using Ontologies and Fuzzy QFD*.

Contribution:
- ontology-based operational-risk identification;
- probability/impact queries;
- FQFD prioritization;
- cause-effect mitigation;
- mitigation strategies fed back into ontology;
- real pharmaceutical-company transport/storage case.

**Counting rule:** application/method prior art distinct from Lineage A, but its reused ontology must be lineage-linked before exact novelty comparison.

## Lineage C — Pharmaceutical Quality Risk Management / QbD

### C1 — SRC-PH-007 (2012)
*A risk management ontology for Quality-by-Design based on a new development approach according GAMP 5.0*.

Verified from authoritative metadata/abstract:
- pharmaceutical Quality Risk Management ontology;
- QbD/GMP/GAMP 5.0 context;
- V-model process;
- requirements specification, conceptualization, formalization, implementation and validation approach.

**Evidence limitation:** full text remains access-blocked in current SemRisk execution, so class/axiom/evaluation details are not asserted.

## Lineage D — Current formal biopharma risk-management artifact

### D1 — SRC-ON-006 (IOF Biopharma Risk Management, release 202603)
Current formal biopharma Quality Risk Management module adapted from ICH Q9(R1). Exact dependency/release semantics still require qualification.

## Consequence for SemRisk SR-C3

Pharma ontology novelty cannot be based on existence of:
- Pharma/medicines risk ontology;
- supply-chain partner interoperability;
- risk identification/classification;
- UML→OWL transformation;
- QRM ontology engineering;
- ontology-supported prioritization/mitigation.

The surviving candidate contribution is the **federation of a reusable SemRisk Core with CM-PharmE**, while preserving external semantic ownership and explicit distinctions among risk phenomenon, scenario description, register information artifact, assessment activity/result, risk/workflow states, evidence/provenance and treatment/responsibility.

## Required remaining work before G1

1. resolve or formally bound SRC-PH-007 full-text limitation;
2. bind formal ontology artifacts for PH-011/PH-009 if they survive publicly;
3. bind PH-008 reused ontology lineage;
4. qualify IOF Biopharma exact release/dependencies;
5. complete source mining of remaining Pharma corpus and one final saturation refresh.