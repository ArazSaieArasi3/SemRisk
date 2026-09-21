# SRC-PH-009 Deep Mining — Domain Ontology for Risks Management in Pharmaceutical Supply Chain

**Source ID:** SRC-PH-009  
**Citation:** Touria Benazzouz, *Domain Ontology for Risks Management in Pharmaceutical Supply Chain*, JOMODS Vol.1 Issue 1, pp.13–18, DOI 10.34874/IMIST.PRSM/jomods-v1i1.29052  
**Mining date:** 2026-09-21  
**Status:** DEEP-MINED v0.1 — full public text inspected; publication-year metadata is inconsistent across sources and exact ontology artifact is unresolved.

## 1. Bibliographic quality note

The public PDF header states **2020, Volume 1, Issue 1**, while DOI/profile/indexing records surfaced in this search describe the publication as **2021**. SemRisk must preserve this discrepancy rather than silently normalize it. DOI is treated as the stable scholarly identity; year requires final bibliographic verification.

## 2. Scientific scope

The paper proposes a domain ontology/decision-support system for risk management in the pharmaceutical/medicines supply chain, especially public hospitals in Morocco.

The motivation is semantic interoperability and risk-information sharing across supply-chain partners and information systems.

## 3. Risk taxonomy extracted

The paper organizes risks into six broad categories:
- Process Risks;
- Demand-related Risks;
- Supply-related Risks;
- Environmental Risks;
- Market Risks;
- Financial Risks.

Examples include inventory/stockout, worker skills, information flow and traceability, production/acquisition, transport, planning/control, outsourcing, strategy, human resources, customer needs, supplier partnership, delivery reliability, information systems, raw-material availability/quality, manufacturing complexity/nonconformance, disasters/terrorism, political issues, waste management, market-price risk and budget/financial constraints.

## 4. Ontology engineering method

The paper describes an ontology lifecycle including:
- needs identification and evaluation;
- domain/objective/user definition;
- conceptualization from expert interviews and/or document analysis;
- informal conceptual model;
- semi-formal representation;
- formal ontology construction;
- use and later re-evaluation/reconstruction.

The ontology is conceived first as a UML model. The authors explicitly note that UML alone does not support automatic semantic reasoning, and cite OWLGred as the mechanism for transforming UML-class-diagram conceptualization into OWL-based formal ontology.

## 5. Claimed ontology functions

The proposed domain ontology provides three main functions:
1. identification of risks in the medicines/pharmaceutical supply chain at public hospitals;
2. semantic description/classification of each risk category/subcategory;
3. risk management/information sharing among multiple supply-chain partners.

Risks are also classified across strategic, tactical and operational management levels.

## 6. Partner and ecosystem semantics

The ontology includes medicines-supply-chain partner concepts and interactions, supporting the idea that risk cannot be represented in isolation from supply-chain actors/processes.

This is important prior art for SR-C3 because Pharma risk semantics were already modeled in relation to supply-chain partners, not merely as a flat risk vocabulary.

## 7. Evaluation state

The paper concludes that the proposed domain ontology/decision-support system still needs validation in a broader context with final users.

Therefore:
- it is material prior art for design/scope/semantic coverage;
- it is weaker evidence for completed empirical/semantic validation.

## 8. Direct impact on SemRisk

### SR-C3
**RETAINED / NARROWED FURTHER.**

Not novel by itself:
- a pharmaceutical/medicines supply-chain risk ontology;
- ontology-based risk identification/classification in public-hospital medicines supply;
- sharing risk knowledge among Pharma supply-chain partners;
- UML→OWL ontology engineering for Pharma risk;
- classifying Pharma supply risk at strategic/tactical/operational levels.

SemRisk must differentiate through a reusable, externally federated Risk Core; CM-PharmE ownership; explicit phenomenon/record/assessment/result/state/workflow/evidence distinctions; exact provenance; and bounded release/evaluation controls.

## 9. Critical lineage finding

This 2020/2021 paper is **not the beginning of the line**. It explicitly builds on earlier work by the same research group, including:
- *Ontology for Risks in Medicines Supply Chain: Case of Public Hospitals in Morocco* — MATEC Web of Conferences 105 (2017), DOI 10.1051/matecconf/201710500012;
- *A new approach for the conception of an information system related to the medicines supply chain in Morocco* — published online 2017, DOI 10.1080/20479700.2017.1337836;
- earlier risk-analysis studies/registers in Moroccan medicines supply.

These outputs must be treated as one evolving Pharma supply-risk ontology/modeling lineage rather than independent novelty votes.

## 10. SemRisk comparison boundaries

Prior-work strengths:
- domain-specific Pharma/medicines supply semantics;
- explicit partner/system interoperability objective;
- risk taxonomy with operational/tactical/strategic scope;
- UML/OWL formalization path;
- supply-chain information-system orientation.

Candidate SemRisk differences still requiring evidence:
- foundational/well-founded semantics;
- explicit information-artifact identity for Risk Register Entry;
- Assessment Activity vs Assessment Result;
- Risk State vs Workflow State;
- evidence/provenance/reassessment lifecycle;
- controlled external federation with CM-PharmE instead of locally owning all Pharma entities;
- ontology↔RDB fidelity/parity evaluation;
- release-bound claim/evaluation governance.

## 11. Downstream routing

- #15 Pharma corpus;
- #14 closest-work registry;
- #18 G1 reconciliation;
- #5 CM-PharmE bridge;
- #22 differentiation;
- #23 method comparison;
- #28 Pharma case;
- #31 E10;
- #53 claim calibration.