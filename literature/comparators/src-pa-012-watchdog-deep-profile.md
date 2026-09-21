# SRC-PA-012 Technical Deep Profile — WATCHDOG

**Source ID:** SRC-PA-012  
**Title:** WATCHDOG: An ontology-aWare risk AssessmenT approaCH via object-oriented DisruptiOn Graphs  
**Venue:** CAiSE 2025, LNCS 15702, pp. 314–331  
**DOI:** 10.1007/978-3-031-94571-7_18  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — public full-text content inspected; exact code/artifact/release binding remains.

## 1. Core contribution

WATCHDOG operationalizes COVER notions inside a formal risk-assessment framework that combines:
- Object-Oriented Disruption Graphs (DOGs);
- attack trees;
- fault trees;
- an object graph;
- a disruption knowledge base;
- DOGLog formal logic;
- DOGLang query DSL.

## 2. Semantic/formal integration

WATCHDOG makes objects at risk explicit and connects their properties, parthood and participation in events/actions to disruption propagation, likelihood and risk-level reasoning.

This directly demonstrates that ontology + formal methods + object-aware risk reasoning is implemented prior art.

## 3. Query capabilities

The framework supports queries about:
- disruption propagation;
- disruption probability thresholds;
- minimal risk scenarios;
- most risky action/event for an object;
- maximum/minimum aggregated risk for an object;
- what-if evidence/configuration changes.

## 4. SemRisk novelty impact

Not available as standalone SemRisk novelty:
- ontology-aware formal risk assessment;
- object-oriented risk reasoning;
- integration of ontology with fault/attack-tree formalisms;
- logic/query DSL for risk;
- what-if scenario evaluation;
- object-level aggregated risk queries.

SemRisk remains differentiated only if it shows a distinct, governed operational ontology architecture around records, assessments/results, states, workflow, evidence provenance, responsibilities, enterprise ownership and cross-domain federation.

## 5. Method implication

WATCHDOG is a strong comparator for #23 because it integrates formal ontology with mature formal-method artifacts rather than relying on OWL reasoning alone. SemRisk's OWL/SHACL/RDB/CQ stack must therefore be justified by its target claims and operational semantics, not presented as generally stronger than theorem/logic-based approaches.

## 6. Current decision

Mandatory method/application comparator for E10. Security/safety-specific DOG/DOGLog/DOGLang constructs should not enter SemRisk Core unless separately justified.