# SRC-PH-011 Technical Deep Profile — Ontology for Risks in Medicines Supply Chain: Case of Public Hospitals in Morocco

**Source ID:** SRC-PH-011  
**Citation:** Benazzouz, Echchtabi & Charkaoui (2017), MATEC Web of Conferences 105, 00012, DOI 10.1051/matecconf/201710500012  
**License:** CC BY 4.0  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — public full text inspected; exact ontology file/repository is unresolved.

## 1. Core contribution

The paper develops a domain ontology for risk management in the medicines supply chain of Moroccan public hospitals. The ontology is generated with OWLGred from a UML model and is intended to improve common understanding, semantic information exchange, risk identification and decision support among supply-chain partners.

## 2. Scope and modeled context

The modeled context includes the medicines supply process and partner interactions across procurement, storage, distribution and hospital use. The paper explicitly treats risk management as embedded in a multi-actor supply-chain information system rather than as an isolated risk vocabulary.

## 3. Ontology purpose

The ontology is designed to:
1. identify supply-chain risks;
2. classify/semantically describe risks;
3. support risk management and information/knowledge sharing among partners.

Risk categories are tied to management levels and supply-chain actors/processes.

## 4. Engineering approach

- corpus/knowledge elicitation from risk literature and medicines-supply context;
- UML conceptual model;
- OWLGred transformation/formalization toward OWL;
- ontology used as an integration/interoperability layer.

## 5. SemRisk impact

Not novel for SemRisk:
- ontology-based medicines/pharmaceutical supply-risk identification;
- multi-partner risk-information interoperability;
- UML→OWL ontology development for Pharma supply risk;
- ontology as decision support for hospital medicines supply.

Candidate SemRisk differentiation still requires evidence for foundational semantics, external CM-PharmE federation, risk-phenomenon vs register-record identity, assessment/result and state/workflow distinctions, provenance/reassessment, and governed executable projections.

## 6. Lineage relation

This source is a direct predecessor of SRC-PH-009. SRC-PH-012 is an adjacent UML/information-system modeling publication by the same research group. These outputs should be compared as one evolving Moroccan medicines-supply ontology/modeling programme rather than counted as independent novelty votes.

## 7. Evaluation limitation

The paper proposes broader future validation with final users. This means it is strong prior art for scope/design and weaker evidence for completed user/domain validation.

## 8. Downstream routing

- #15 Pharma corpus;
- #14 closest-work registry;
- #18 G1;
- #22 differentiation;
- #23 method comparison;
- #5/#28 Pharma federation/case;
- #31 E10;
- #53 claim calibration.
## 9. Same-group IEOM 2017 sibling and register evidence — 2026-09-28

The separate official [IEOM 2017 conference paper](https://ieomsociety.org/ieom2017/papers/90.pdf), *Using Ontology as a Decision Support System for Manage Risks in Medicines Supply Chain: Case of Public Hospitals in Morocco* (Benazzouz, Echchtabi & Charkaoui, pp. 281–292), belongs to the same Moroccan research lineage. It is the precise [22] cited by PH-008, although PH-008's bibliography misdates it as 2013. The IEOM paper's **Table 3** explicitly calls its categories/subcategories/descriptions a medicines-supply `Risk Register`; **Figures 2–4** show OWLGred views of supply-chain partners, risk management and the domain ontology. The MATEC PH-011 DOI identifies a distinct publication in the lineage; avoid treating these titles as identical or as independent novelty votes.

This limits SemRisk's wording: a Pharma supply-risk register/taxonomy and OWLGred ontology diagrams already existed in 2017. A narrower claim about governed *register-entry information-artifact identity*, integrated assessment/result/state/workflow/evidence and tested federation remains a hypothesis requiring direct comparison. Exact downloadable OWL for either publication is still not bound.
