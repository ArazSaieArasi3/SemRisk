# SRC-PH-008 Deep Mining — Operational Risk Management in the Pharmaceutical Supply Chain Using Ontologies and Fuzzy QFD

**Source ID:** SRC-PH-008  
**Citation:** Osorio Gómez & Torres España, *Operational Risk Management in the Pharmaceutical Supply Chain Using Ontologies and Fuzzy QFD*, Procedia Manufacturing 51 (2020), 1673–1679, DOI 10.1016/j.promfg.2020.10.233  
**Mining date:** 2026-09-21  
**Status:** DEEP-MINED v0.1 — full open article content inspected; reused ontology artifact/reference lineage still requires exact binding.

## 1. Why this source is material

This is direct prior art for ontology-supported operational risk management in a pharmaceutical supply chain. It goes beyond vocabulary modeling: ontology is used for risk identification, Fuzzy QFD for prioritization, and cause-effect analysis for mitigation/action definition in a real pharmaceutical company case.

## 2. Method pipeline extracted

The paper uses a three-stage operational-risk workflow:
1. **risk identification** using an ontology;
2. **risk prioritization** using Fuzzy Quality Function Deployment (FQFD);
3. **risk management/mitigation** using cause-effect analysis and defined managerial actions.

The study explicitly excludes monitoring from its implemented scope although it cites a four-stage risk-management process that would include monitoring.

## 3. Ontology commitments

The reused operational-risk ontology contains the following top-level classes:
- Risk;
- Occurrence Probability;
- Source;
- Process;
- Impact;
- Managerial Strategy.

`Process` includes transportation and warehousing subclasses in the applied context.

Occurrence probability and impact are represented with linguistic values and are queried to identify candidate critical risks.

## 4. Decision-support logic

Ontology queries identify operational risks by combinations of occurrence probability and impact. FQFD then prioritizes the selected risks by relating them to organizational/process objectives. Mitigation/elimination actions derived from cause analysis are added back to the ontology under Managerial Strategy for future reuse.

SemRisk implication: ontology-supported risk identification + prioritization + treatment feedback is established prior art.

## 5. Applied Pharma case

The method is applied to a pharmaceutical manufacturer in Cali, Colombia, focused on transport and storage of finished products for export.

The paper identifies operational risks including:
- storage temperature outside acceptable limits;
- improper handling of finished-product pallets;
- poor packaging;
- pest-control failures;
- cross-contamination;
- product contamination;
- primary packaging material failures;
- bad road conditions;
- product defects;
- vehicle breakdown;
- cold-chain disruption;
- crime/theft/terrorist acts;
- improper fleet;
- invasive regulatory inspections;
- pressure-change damage during transport.

The most critical risks in the reported case were improper fleet and primary-packaging material failures.

## 6. Evidence and evaluation strength

Strengths:
- real pharmaceutical-company application;
- explicit ontology queries;
- integration of risk identification, prioritization and mitigation;
- real expert/company-history inputs;
- concrete mitigation outputs.

Limitations for ontology comparison:
- ontology itself is reused from prior work rather than introduced as a newly evaluated foundational ontology;
- no well-founded/foundational analysis comparable to UFO/COVER is reported;
- no explicit Risk Record vs Risk phenomenon distinction;
- no Assessment Activity vs Assessment Result modeling distinction;
- no Risk State vs Workflow State distinction;
- ontology artifact/version/IRI is not bound in the article;
- evaluation is application/decision-support oriented, not formal semantic validation.

## 7. Direct impact on SemRisk

### SR-C3
**RETAINED / NARROWED FURTHER.**

Not available as novelty:
- using ontology for pharmaceutical supply-chain risk identification;
- querying probability/impact combinations in an ontology;
- linking ontology-based risk identification to prioritization;
- using ontology to preserve mitigation/managerial strategies;
- applying ontology-supported operational risk management in a pharmaceutical company.

SemRisk's candidate contribution remains the governed federation of a reusable Risk Core with CM-PharmE plus explicit distinction among real-world risk phenomena, scenario descriptions, register records, assessment activities/results, states, workflow, evidence and responsibility.

### SR-C2
The source also narrows generic operational-risk workflow novelty: identification→prioritization→mitigation with reusable ontology knowledge is prior art.

## 8. Important lineage finding

The paper explicitly cites earlier pharmaceutical/medicines supply-chain ontology work in Morocco and reuses an ontology-based operational-risk identification approach from 3PL/transport literature. Therefore this paper is not an isolated first occurrence; it belongs to a broader operational-risk ontology lineage.

## 9. Downstream routing

- #15 Pharma corpus;
- #14 closest-work comparison;
- #20 assessment/treatment/lifecycle reconciliation;
- #22 differentiation matrix;
- #23 method comparison;
- #28 Pharma case;
- #31 E10 comparison;
- #53 claim calibration.

## 10. Remaining debt

- bind the exact reused ontology/reference [28] and its artifact, if public;
- bind the pharmaceutical ontology predecessor cited as [22];
- normalize exact table/figure/page locators in comparator registry;
- determine whether any machine-readable ontology file survives publicly.