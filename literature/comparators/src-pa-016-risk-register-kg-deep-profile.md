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
## 8. Appendix-linked artifact binding — 2026-09-28

The author-uploaded full-text appendix for DOI `10.1007/s12205-023-2886-7` lists two GitHub links; their current default-branch heads were frozen for this comparison:

| Role | Immutable reference | Inspected top-level evidence |
| --- | --- | --- |
| RisKG data/model | https://github.com/Murry01/RisKG/tree/435b6b0ecebc49a4e82e62bdffbe9c4c2e2c4448 | `Data and results.xlsx`, `RisKG(Townsville ).cql`, `Townsvill-construction-risk-register.pdf`, ontology/overview/graph images and README. |
| ConRisk dashboard | https://github.com/Murry01/ConRisk_Dashboard/tree/9738b8e9a3c6a1b1bcee604452ce6f787688531f | `Home.py`, `neo4japp.py`, `pages/`, `requirements.txt`, CQL, query text, risk-assessment XLSX and MP4. |

Both snapshots date to March 2023; no repository license was exposed in the GitHub metadata/top-level files inspected. The appendix links and concrete files resolve the prior **artifact identity** gap. They do not establish an independently successful build, code/data licensing permission, a governed release tag, complete input provenance, or equality between the published 392-entity/391-relationship case and a rerun. No import of their source/data is proposed without a separate license decision. Reproduction remains `NOT_ASSESSED`.

**Status:** two implementation repositories COMMIT_BOUND; exact reproducibility and reuse permission still open. The publication's operational graph/dashboard prior art remains material to SR-C2.
