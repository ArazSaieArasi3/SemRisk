# SRC-PA-016 Technical Deep Profile — RisKG Risk-Register Knowledge Graph

**Source ID:** SRC-PA-016  
**Citation:** Isah & Kim (2023), *Development of Knowledge Graph Based on Risk Register to Support Risk Management of Construction Projects*, KSCE Journal of Civil Engineering 27(7), 2733–2744, DOI 10.1007/s12205-023-2886-7  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — open full article content inspected; exact code/appendix artifact binding remains.

## 1. Purpose and architecture

The study converts a semi-structured construction project risk register into a risk knowledge graph (RisKG), stores it in Neo4j and exposes it through a dashboard for retrieval/reuse of risk knowledge.

## 2. Ontology/data model

The reported ontology/model defines six principal entity families:
- Project;
- Risk Source;
- Risk;
- Risk Rating;
- Risk Consequence;
- Risk Mitigation.

Reported relation families include:
- hasRiskSource;
- hasRisk;
- hasRiskRating;
- hasRiskConsequence;
- hasRiskMitigation.

Attributes include identifiers/descriptions and assessment-related values such as impact, probability and rating.

## 3. Extraction/implementation

Risk knowledge is manually extracted from the semi-structured register into the predefined graph model. The paper reports 392 entities and 391 relationships in the case graph. Neo4j/Cypher is used for graph storage/implementation.

## 4. Evaluation/application

The ConRisk dashboard is used for searching and retrieving risk-assessment details for the case project. Evaluation is application/task oriented rather than foundational ontological validation.

## 5. SemRisk implications

Prior art established:
- semi-structured Risk Register → ontology/graph schema;
- Risk Register → Neo4j KG;
- risk-source/rating/consequence/mitigation graph retrieval;
- risk dashboard over KG.

Therefore SR-C2 cannot rely on graphifying a register as novelty.

## 6. Candidate SemRisk distinction

RisKG appears primarily data/model driven. SemRisk's candidate distinction remains the ontological separation of risk phenomenon/scenario/record/assessment/result/state/workflow/evidence and explicit projection-loss/parity evaluation. This is a comparison hypothesis, not a superiority conclusion.

## 7. Downstream use

- mandatory SR-C2/E10 comparator;
- input to #45 ontology-grounded relational/KG projection design;
- anti-pattern evidence against class-per-column/entity-per-register-field modeling;
- input to #49 projection fidelity criteria.