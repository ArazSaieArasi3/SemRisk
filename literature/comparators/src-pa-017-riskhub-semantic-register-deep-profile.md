# SRC-PA-017 Technical Deep Profile — RiskHub Semantic-Aware Risk Register

**Source ID:** SRC-PA-017  
**Citation:** Aghazadeh Ardebili et al. (2026), *Data-Driven Decision Support via Semantic-Aware Risk Data Modeling: Operational Intelligence Platform for Smart Transport*, Operations Research Forum 7:79, DOI 10.1007/s43069-026-00666-7  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — open article inspected through conceptual/logical/physical/evaluation sections; supplementary high-resolution artifacts still need exact binding.

## 1. Why this is a very close comparator

The study explicitly redesigns an operational spreadsheet/database risk-management process into an ontology-informed conceptual, logical and physical risk-register model and implements a decision-support platform. This overlaps strongly with SemRisk SR-C2 and planned #45–#49.

## 2. Knowledge/design inputs

The model is grounded in a knowledge synthesis using:
- COSO;
- ISO/IEC 27005;
- an Operational Risk Management ontology;
- Risk Data Open Standard (RDOS);
- requirements analysis and operational company data.

## 3. As-Is / To-Be methodology

The study analyzes the existing operational process and data, builds As-Is and To-Be conceptual models, and uses ontology-informed entities/relationships to re-engineer the risk register.

Important represented concerns include:
- risk scenario;
- business function;
- risk owner;
- high/low-level risk categories;
- frequency/likelihood;
- impact;
- status;
- mitigation tools;
- residual-risk-relevant control information.

Mitigation is specialized into operational, contractual and insurance controls.

## 4. Relational projection

The conceptual model is mapped to a relational logical model with 12 tables, including a table introduced for a many-to-many relation. Referential integrity and specialization mapping are explicitly discussed. MySQL is used for the physical implementation.

## 5. Operational prototype

RiskHub provides a Risk Register interface/dashboard integrating scenario, business function, owner, frequency, impact, status and mitigation information.

## 6. Evaluation

The study reports exploratory expert elicitation with 12 professionals/academics in risk management, security/safety and data management. Evaluation dimensions include completeness, accuracy, adaptability and extensibility. The authors explicitly caution about exploratory scope.

## 7. Direct SemRisk novelty impact

Already prior art:
- ontology-informed risk-register redesign;
- spreadsheet→structured relational database transition;
- conceptual→logical→physical risk data modeling;
- owner/function/status/scenario/mitigation modeling;
- operational dashboard;
- expert evaluation of the risk data model.

Thus SemRisk cannot present PostgreSQL/RDB implementation or ontology-guided database design as novelty by themselves.

## 8. Remaining candidate differentiation

SemRisk must demonstrate additional semantic commitments rather than more tables:
1. Risk phenomenon is not the register row/information artifact.
2. Scenario Description is not the possible/real event itself.
3. Assessment Activity is not Assessment Result.
4. Risk State is not Workflow State.
5. Inherent/residual values are contextual assessment results, not timeless risk properties.
6. Evidence/provenance and reassessment are explicit and traceable.
7. RDB is a governed projection whose semantic loss/parity is tested against ontology queries.
8. External ontologies such as CM-PharmE retain semantic ownership.

## 9. Method implication

RiskHub is a strong alternative engineering path for #23: bottom-up requirements/process re-engineering + ontology synthesis + ER modeling + relational implementation + expert evaluation. SemRisk's OGCM-RF/evidence-first approach must be justified against this, not presumed superior.

## 10. Downstream use

- mandatory SR-C2/E10 comparator;
- key prior art for #45–#49;
- source for #23 method comparison;
- input to #53 claim calibration.
## 11. Publisher supplement and cited predecessor artifact — 2026-09-28

- Publisher article/version of record: https://link.springer.com/article/10.1007/s43069-026-00666-7 (published 2026-06-22). Its Supplementary Information section links one `Supplementary file 1`, a JPG image reported as 95 KB: https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs43069-026-00666-7/MediaObjects/43069_2026_666_MOESM1_ESM.jpg . This binds the publicly listed supplemental artifact identity, but does not establish a machine-readable ontology/ER schema or executable implementation.
- The paper's reference 17 cites Flores (2021) and links https://github.com/sydalabnavid/Risk-Hub , which redirects to https://github.com/NaviDATA-Repos/Risk-Hub/tree/f0664c1dbdbdf40f59361751b9f55807ff6dddaf . At that immutable 2024-03-08 snapshot, the top level contains `CITATION.cff`, `README.md`, and `RiskHub.pdf`; GitHub does not report a repository license. The README describes a thesis risk-assessment database/dashboard prototype. Treat it as a **cited predecessor**, not as source code or a release of the 2026 paper's RiskHub implementation.
- Exact 2026 data model/code version, executable build, dataset and reproduction commands remain `UNKNOWN/NOT_REPORTED` in these inspected public artifacts. No code or ontology reuse is approved by this binding. The 2026 article's conceptual/relational and exploratory expert prior-art comparisons remain valid at the publication evidence level.

**Status:** publication supplement and predecessor identity bound; implementation reproducibility remains open. Do not conflate a publisher image, a cited thesis PDF, and the evaluated platform.
