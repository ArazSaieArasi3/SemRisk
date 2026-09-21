# SRC-PA-005 Deep Mining — Toward an ontology-based modeling for risk management

**Source ID:** SRC-PA-005  
**Authors:** Ítalo Oliveira, Stefano M. Nicoletti, Mattia Fumagalli, Gal Engelberg, Giancarlo Guizzardi  
**Venue:** VMBO 2025 / CEUR Workshop Proceedings Vol. 4129  
**Length:** 7 pages  
**License:** CC BY 4.0  
**Mining date:** 2026-09-21  
**Status:** DEEP-MINED v0.1 — complete paper inspected; exact citation-lineage and downstream artifact tracking remain open.

## 1. Evidence role

- comparative
- discovery
- design/method lead
- not independent validation of SemRisk

This source is a **research proposal**, not evidence that the proposed full ontology network, modeling language and service ecosystem have already been completed and evaluated.

## 2. Problem formulation extracted

The authors argue that common risk-management techniques such as Attack Trees, Fault Trees, Risk Matrix, FMEA/FMECA, Bow-tie analysis and Bayesian Networks implicitly rely on domain conceptualizations but generally lack explicit ontological grounding.

They identify three main semantic problems:
1. ambiguous syntax/construct interpretation;
2. little or no modeling guidance;
3. poor semantic integration across techniques and data sources.

A central premise is that quantitative risk metrics are meaningful only through the conceptual model that defines the semantics of the measured entities and relationships.

## 3. Proposed research architecture

### 3.1 Risk Management Ontology Network
The proposed network explicitly includes COVER, ROSE, ROT and ResiliOnt, plus possible new/refined ontologies for missing topics such as monitoring and detection.

The intended formal stack is UFO as foundational ontology, OntoUML for conceptual representation, and OWL compatible with gUFO for formal implementation.

### 3.2 Ontological analysis of risk-management techniques
The proposal uses ontological analysis to diagnose ontological incompleteness/construct deficit, construct overload, construct redundancy and construct excess.

Target techniques include Attack Trees, Fault Trees, FMECA, Bayesian Networks, Risk Matrix and other risk-management techniques.

### 3.3 Domain-Specific Modeling Language and services
The planned language is intended to embody the ontology network, support types and individuals, distinguish risk scenarios as possible events from incidents as past concrete occurrences, integrate external datasets/knowledge bases, and support reasoning, simulation, risk propagation and root-cause analysis.

## 4. Closest-work implications for SemRisk

### 4.1 Generic ontology-network novelty is not available
SemRisk cannot claim novelty merely from integrating multiple well-founded risk-related ontologies, using UFO/OntoUML/gUFO, creating a risk-management ontology network, using ontological analysis to redesign risk techniques, pursuing semantic interoperability, or connecting ontology semantics to a domain-specific modeling language.

### 4.2 Scenario/incident distinction is prior art
The paper explicitly plans to distinguish risk scenarios as possible events from incidents as past concrete occurrences. SemRisk therefore cannot claim novelty merely from hypothetical-versus-realized event separation.

### 4.3 Data integration and executable services are also planned prior work
Automated reasoning, simulation, risk propagation, root-cause analysis and integration with external data/knowledge bases are part of the proposal. These are not safe standalone novelty claims for SemRisk.

## 5. SemRisk differentiation that remains plausible

The following combination is not explicitly specified in this 7-page proposal and remains a candidate SemRisk differentiation boundary, subject to broader closest-work checks:
1. real-world managed risk phenomenon vs Risk Register Entry as information artifact;
2. Assessment Activity vs Assessment Result;
3. Risk State vs management-record Workflow State;
4. evidence/provenance structures for assessment/reassessment;
5. operational Jira-style mapping without class-per-column shortcuts;
6. release-bound source→candidate→canonical→formal→evaluation→claim traceability;
7. ontology↔relational projection with SQL↔SPARQL parity/loss analysis;
8. bounded Pharma/CM-PharmE federation with explicit external semantic ownership.

## 6. Impact on frozen Paper-1 contract

### SR-C1 — dominant contribution
**RETAINED / NARROWED.** The defensible novelty target must emphasize the integrated operational pattern rather than generic semantic disambiguation or scenario-vs-incident separation.

### SR-C2 — enterprise operationalization
**RETAINED / HIGHER COMPARISON BURDEN.** SemRisk must demonstrate its enterprise contribution through operational architecture/register/assessment projection rather than general enterprise-risk modeling.

### SR-C3 — Pharma federation
**UNCHANGED DIRECTLY.** The generic ontology-network part cannot support novelty, but the bounded SemRisk↔CM-PharmE federation remains a distinct candidate contribution.

### SR-CL01
**NARROWED.** Wording must emphasize the full operational semantic separation, not generic risk concept clarification.

### SR-CL07
**MANDATORY COMPARATOR.** Any differentiation claim must compare SemRisk with this research program and distinguish proposed capabilities from implemented/evaluated results.

## 7. Methodological implication

This paper is especially relevant to Issue #23 because it provides a method profile: foundational ontology → reference ontology network → ontological analysis → mismatch diagnosis → modeling-language redesign → semantic services.

SemRisk should compare OGCM-RF's evidence-first/source-governed approach against this ontology-analysis-centric program without treating either method as automatically superior.

## 8. Comparator strength and limitation

Strengths: very close scientific problem statement, UFO lineage, ontology network, semantic interoperability objective, explicit modeling-language analysis method and executable/service vision.

Limitation: the paper itself is a research proposal. The full network, redesigned techniques, DSL and service ecosystem are future-oriented in the text. SemRisk must distinguish prior idea/proposal overlap from implemented and evaluated evidence.

## 9. Downstream routing

- #14 closest-work registry: mandatory comparator.
- #20 relation/event/state registry: scenario/incident semantics.
- #21 COVER/ROSE reuse decisions.
- #22 differentiation matrix.
- #23 method selection.
- #53 claim calibration.
- #35 final novelty refresh.

## 10. Remaining work

Before #14/G1 closure: trace post-2025 outputs from this research program; identify released ontology-network/DSL artifacts; bind exact referenced ontology versions; link CORAS/ArchiMate/Spyderisk lineages; normalize to the machine-readable comparator registry; check 2026 follow-up work for further novelty impact.