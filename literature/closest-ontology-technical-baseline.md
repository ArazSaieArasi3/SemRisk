# SemRisk Closest Ontology / Semantic Model Technical Baseline

**Status:** W1 technical baseline. Deep source-complete extraction remains open under Issue #14.  
**Date:** 2026-08-29

This file records verified technical evidence from papers and released semantic artifacts. It separates paper claims from repository artifact evidence.

## Comparator matrix — baseline

| Comparator | Scope | Foundation / modeling | Formal artifacts | Constraints / executable support | Evaluation / use evidence | SemRisk decision |
|---|---|---|---|---|---|---|
| **COVER** | common ontology of value and risk | well-founded; OntoUML; gUFO-based OWL implementation | public `cover.ttl`; PURL namespace | OWL axioms; no SemRisk assumption about SHACL until verified | foundational/reference paper | **Primary foundation / reuse-alignment** |
| **ROSE** | security engineering from risk-treatment / prevention perspective | well-founded; OntoUML; builds on value/risk/prevention; gUFO OWL | public OntoUML + OWL; PURL | OWL; repository documents correction/erratum | reference ontology paper; maintained artifact | **Security/treatment reuse-alignment** |
| **AIRO** | AI risk, EU AI Act and ISO-aligned risk documentation | domain ontology; regulatory/standards alignment | TTL, OWL, RDF, JSON-LD, examples, w3id | repository contains SHACL/SPARQL/N3 rule assets | modeled real-world AI-risk use cases; maintained repo | **AI profile benchmark / standards-integration comparator** |
| **RISKMAN** | medical-device risk-management documentation and conformity | ontology engineered from ISO 14971/VDE Spec; LOT/NeOn lineage; domain-expert input | ontology + SHACL shapes, w3id | SHACL validation; reasoning | HermiT/OOPS/FAIR checks reported; semi-structured documentation converted/validated | **Health comparator; strong method/evaluation benchmark** |
| **Operational Risk Ontology (2011)** | cross-unit operational risk information sharing/inference | ontology approach to ORM | paper evidence; artifact status to verify | computational inference claimed | organizational interoperability motivation | **Enterprise ORM prior art** |
| **Brownsword risk ontology/framework (2010)** | formalized pragmatic risk-management framework/ontology | systems-engineering / conceptual approach | artifact status to verify | to verify | cross-domain case validation reported | **Cross-domain prior art; inspect for comprehensiveness claims** |
| **Oliveira et al. risk-management ontology programme (2025)** | integrated ontology-based risk-management modeling/services/ontology network | builds on well-founded risk/security work | programme/work artifacts to inspect | planned/integrated semantic services | closest current research-program overlap | **Primary novelty threat / continuous watch** |

---

## 1. COVER — Common Ontology of Value and Risk

### Verified source / artifact evidence

- Paper: Sales et al., **The Common Ontology of Value and Risk**, ER 2018, DOI `10.1007/978-3-030-00847-5_11`.
- Repository: `unibz-core/value-and-risk-ontology`.
- Repository README explicitly describes COVER as a **well-founded ontology** that makes connections between value and risk explicit, grounded in multiple theories and specified in **OntoUML**.
- Repository has `/ontouml` and `/owl`; the OWL implementation is described as **gUFO-based**.
- Current public OWL source: `owl/cover.ttl` under namespace `https://purl.org/krdb-core/cover#`, importing gUFO.

### Material class evidence observed in released OWL

The public TTL includes, among others:

- `RiskSubject`
- `RiskExperience`
- `RiskEvent`
- `RiskEnabler`
- `ObjectAtRisk`
- `ThreatObject`
- `ThreatAgent`
- `ThreatCapability`
- `Vulnerability`
- `HazardousSituation`
- `ThreatEvent`
- `LossEvent`
- `LossSituation`
- `ImpactEvent`
- `TriggerEvent`
- `GainEvent`
- `OpportunityEvent`
- `RootCauseEvent`
- `Likelihood`
- `Risk`
- `RiskAssessment`
- `RiskAssessor`
- value-related constructs such as `Value`, `ValueExperience`, `ValueEvent`, `ValueAscription`, `GainAscription`, `LossAscription`.

Foundational categories are encoded using gUFO stereotypes/types such as `RoleMixin`, `EventType`, `SituationType`, `Kind`, `SubKind`, `Category`.

### Immediate implication for SemRisk

Several constructs that might otherwise be advertised as SemRisk inventions clearly have well-founded prior art in COVER. SemRisk should therefore not claim novelty for generic `RiskEvent`, `RiskSubject`, `Vulnerability`, `OpportunityEvent`, `RiskAssessment`, etc. without demonstrating a materially different/extended commitment.

The likely SemRisk contribution is instead in the **operational/enterprise/domain bridge and evidence architecture** around such foundations: records, assessment contexts/results, governance, standards, architecture, empirical schemas, domain profiles and traceable evaluation.

### Open technical questions

- exact COVER definitions/relations relevant to `Risk`, `RiskAssessment`, likelihood and ex-ante/ex-post value ascriptions;
- whether and how `Risk` as a quality/value construct aligns with ISO's effect-of-uncertainty wording;
- treatment/control coverage versus ROSE;
- exact reuse architecture: OWL import vs reference/mapping/bridge.

These are deferred to Issue #21 after source-complete profiling.

---

## 2. ROSE — Reference Ontology for Security Engineering

### Verified source / artifact evidence

- Paper: Oliveira et al., **An Ontology of Security from a Risk Treatment Perspective**, ER 2022, DOI `10.1007/978-3-031-17995-2_26`.
- Repository: `unibz-core/security-ontology`.
- Repository README describes ROSE as a well-founded reference ontology in **OntoUML**, explaining security mechanisms in relation to **value, risk and prevention**.
- Public PURL: `https://purl.org/security-ontology`.
- Repository contains OntoUML and gUFO-based OWL sources.
- Repository explicitly records an **erratum/correction** to a characterization cardinality between `Intention` and subject roles, demonstrating that the living artifact can supersede a paper-level modeling detail.

### SemRisk implication

Security mechanisms, prevention and treatment semantics should be reused/aligned where applicable rather than recreated in a generic SemRisk security module. The recorded erratum also reinforces SemRisk's own rule that manuscript claims must bind to a precise semantic release rather than assuming the paper PDF is the latest formal truth.

---

## 3. AIRO — AI Risk Ontology

### Verified source / artifact evidence

- Paper DOI: `10.3233/SSW220008`.
- Repository: `DelaramGlp/airo`.
- Persistent namespace: `https://w3id.org/airo`.
- License shown in README: **CC BY 4.0**.
- Repository contains multiple serializations (`airo.ttl`, `.owl`, `.rdf`, `.jsonld`), examples and documentation.
- Repository root also includes directories for **SHACL**, **SPARQL** and N3/rule-oriented assets for high-risk/prohibited classification tasks.

### SemRisk implication

AIRO is strong prior art for:

- domain-specific risk ontology construction;
- explicit alignment to regulation/ISO risk-management terminology;
- executable compliance/high-risk determination;
- persistent IRI and public artifact packaging.

It does **not** eliminate a domain-general SemRisk contribution, but it prevents claims that standards-aligned executable domain risk ontologies are unprecedented.

---

## 4. RISKMAN — Medical Device Risk Management Ontology and Shapes

### Verified scholarly evidence

- Preprint: `10.48550/arXiv.2405.09875`.
- Peer-reviewed 2025 publication: **Supporting Risk Management for Medical Devices via the RISKMAN Ontology and Shapes**, DOI `10.3233/ssw250023`.
- Public persistent locus stated in the paper: `https://w3id.org/riskman`.

### Method/evaluation signals from the scholarly work

RISKMAN is especially important for SemRisk method comparison because the work reports:

- development around actual medical-device risk-management documentation and relevant standards;
- ontology-engineering method lineage based on **Linked Open Terms (LOT)** / NeOn-oriented practices;
- domain-expert involvement;
- OWL ontology plus **SHACL** conformity/completeness constraints;
- reasoning / ontology-quality tooling (including HermiT and ontology-quality checks as reported in the work);
- a pipeline that uses semantics and shapes to validate risk-management information.

### SemRisk implication

SemRisk cannot claim that `OWL + SHACL + standard alignment + medical/Health risk documentation` is novel. Its potential advantage must be demonstrated through a broader reusable Core, foundational alignment, multi-source provenance, cross-domain/domain-profile transfer, enterprise/architecture integration and stronger comparative/reproducibility evidence.

---

## 5. Other material prior art identified

### Ontology-based Operational Risk Management — 2011

DOI `10.1109/CEC.2011.18`. Motivates a unified ontology for operational risk information sharing across organizational units and computational inference over heterogeneous ORM applications.

**Novelty consequence:** enterprise-wide semantic integration of operational risk is longstanding prior art.

### A Formalised Approach to the Management of Risk — 2010

DOI `10.4018/JKSS.2010100101`. Reports a conceptual framework and ontology with case validation across multiple sectors including IT, defence, rail, education, health/safety, business/project contexts.

**Novelty consequence:** cross-domain applicability/comprehensiveness must be empirically and comparatively demonstrated, not asserted by SemRisk as a first.

### Oliveira et al. — ontology-based modeling for risk management — 2025

This line of work is currently treated as the **closest research-program-level novelty threat** because it explicitly pushes well-founded ontology networks and modeling/services for risk management, building on COVER/ROSE-related work.

**Required action:** source-complete technical extraction and a fresh citation/author-work search at Gate G5.

### Recent watch item: SECUMAN (2026 preprint)

A very recent medical-device/cybersecurity risk ontology direction surfaced in August 2026 and should be tracked under the Health/Security landscape. It is not yet treated as peer-reviewed evidence unless publication status is verified.

---

## Current non-novelty findings

The following cannot safely be marketed as novel on their own:

1. use of an ontology for enterprise/operational risk information sharing;
2. a well-founded ontology of value/risk;
3. a reference ontology for risk treatment/security;
4. domain-specific ISO/regulation-aligned risk ontologies;
5. OWL + SHACL validation of risk documentation;
6. application of risk ontologies to Health/medical-device settings;
7. a generic claim of cross-domain risk ontology applicability;
8. knowledge graphs for enterprise or pharmaceutical risk information.

## Candidate defensible SemRisk differentiators to test, not yet claim

- source-complete, exact-locator concept/relation extraction across operational evidence, standards, papers, ontologies and datasets;
- explicit reconciliation from raw evidence to canonical Core with no silent concept dropping;
- deep separation of risk phenomenon/value/event from scenario/record/assessment/activity/result/workflow-state semantics;
- formal bridging of a well-founded risk Core into enterprise architecture/governance semantics;
- domain-extensible profile composition with Health broad-profile and Pharma/CM-PharmE specialization;
- standard/framework mappings plus public empirical dataset mappings in the same release;
- evaluation breadth tied to claim strength, including comparative E10 and transferability E11;
- SHA/release-bound manuscript, source and evaluation reproducibility.

These differentiators require implementation/evaluation before they may be described as advantages.

## Remaining Issue #14 work

- extract exact class/property/axiom inventories from material comparators;
- inspect licenses/version/release histories;
- identify CQs and explicit development/evaluation methods;
- populate machine-readable comparator profiles and mappings;
- add any closer work discovered through citation chaining;
- produce the E10 shortlist for Paper 1.
