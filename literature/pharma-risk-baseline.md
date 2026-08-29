# Pharmaceutical Risk Evidence Baseline

**Status:** W1 active baseline; not a completed review.  
**Date:** 2026-08-29

## Why Pharma is useful for Paper 1

The pharmaceutical ecosystem is a strong specialization/evaluation domain because it forces a generic risk Core to cross multiple semantic boundaries simultaneously:

- enterprise objectives and capabilities;
- suppliers and ecosystem actors;
- manufacturing/process dependencies;
- regulation and quality constraints;
- medicine availability;
- healthcare-delivery consequences;
- patient-related consequences;
- financial/market/political exposures;
- monitoring, pharmacovigilance and post-market evidence.

This makes Pharma a better **transfer/extension test** than a decorative example.

## Anchor 1 — Jaberidoost et al. 2013

**Citation:** Mona Jaberidoost, Shekoufeh Nikfar, Akbar Abdollahiasl, Rassoul Dinarvand, “Pharmaceutical supply chain risks: a systematic review,” *DARU Journal of Pharmaceutical Sciences*, 21:69, 2013. DOI `10.1186/2008-2231-21-69`.

### Review method

The paper reports searching Scopus, PubMed, Web of Science and Google Scholar using six groups of keywords. After deduplication/screening, 94 full texts were reviewed and 9 studies were included for risk extraction.

### Extracted scope

The authors report **50 risks in 7 categories**:

1. supply / supplier;
2. organization / strategy;
3. financial;
4. logistic;
5. political;
6. market;
7. regulatory.

Reported distribution includes 20/50 supply-supplier risks, 14/50 organization-strategy, 7/50 financial, 3/50 market, 3/50 political, 2/50 logistic and 1/50 regulatory.

### High-value risk candidates directly described in the article

Supply / supplier:

- partnership with supplier;
- ordering cycle time;
- raw-material quality;
- supplier flexibility;
- contract/agreement issues;
- supplier customization;
- supplier GMP certificate;
- supply-chain fragmentation;
- delivery reliability;
- environmental assessment;
- supplier technology level;
- information systems;
- goodwill;
- technology development;
- delivery flexibility;
- quantity flexibility;
- product-variety flexibility;
- timely delivery;
- supplier quality-management system;
- customer-service disruption.

Organization / strategy:

- inventory management;
- planning issues;
- operation issues;
- worker skill;
- research/development;
- company strategy;
- information flow;
- stock visibility;
- organization/process issues;
- waste management;
- production cost;
- merger/acquisition;
- time to market.

Financial:

- currency / exchange-rate fluctuation;
- financial issues;
- tax change;
- supply-related cost;
- interest-rate change;
- tariff-policy change;
- cash flow.

Logistic:

- counterfeit;
- transportation risk.

Market:

- market risk/issues;
- consumer taste;
- demand.

The discussion additionally identifies high-priority/empirical examples from the reviewed literature, including supplier failure, regulatory risk, inventory risk, insufficient capacity to meet demand, inappropriate customer forecasting, lack of visibility/stock availability, uncertainty in demand, new-drug pipeline uncertainty, process development, capacity planning, network design and plant design.

### Important gap useful for SemRisk

The paper explicitly notes that impacts of supply/supplier risks on the whole business and other functions were not adequately described and calls for investigation of risk impacts on business processes/functions and mitigation strategies. This is directly relevant to SemRisk's planned **risk ↔ objective/capability/process** architecture linkage.

### Important boundary / limitation

The review was deliberately from the **production-company perspective**. Consumer safety, environmental risk-management, health-policy and third-party perspectives were excluded from the outcome-of-interest boundary. SemRisk must therefore not use this source as if it represented the whole pharmaceutical or Health risk domain.

---

## Anchor 2 — Recent pharmaceutical supply-chain risk review

**Work:** “Pharmaceutical Supply Chain Risk Assessment: A Systematic Literature Review,” IISE Annual Conference & Expo 2024. DOI `10.21872/2024iise_7761`.

### Current evidence status

DOI/citation is resolved. The paper is a recent review focused on identifying/evaluating pharmaceutical supply-chain risks and resilience across commercial/military contexts. Deep full-text extraction remains pending.

### SemRisk role

- update/extend the 2013 taxonomy;
- identify newer disruption/resilience constructs;
- compare assessment techniques;
- identify public/empirical dataset leads.

---

## Anchor 3 — Pharmaceutical shortage knowledge graph, 2025

**Work:** Katharina Eberhardt et al., “Leveraging knowledge graphs in pharmaceutical supply chains: insights into key drivers of drug shortages,” *International Journal of Production Research*, 63(19), 7129–7152, 2025. DOI `10.1080/00207543.2025.2496671`.

### Current evidence

The paper reports systematic collection/fusion of heterogeneous medical data into a comprehensive knowledge graph for pharmaceutical shortages. Reported shortage drivers are multifaceted, particularly production, market and process issues; the work also quantifies shortage severity and economic impact and supports mitigation/prioritization.

### SemRisk significance

- strong evidence for the Pharma case and future dataset landscape;
- direct prior art for Paper 2: **knowledge graph for pharmaceutical shortage/risk is not by itself novel**;
- useful comparator for data integration, shortage-driver semantics and decision support.

---

## Anchor 4 — Public shortage-register study and data

**Work:** Reko Ravela, Alan Lyles, Marja Airaksinen, “National and transnational drug shortages: a quantitative descriptive study of public registers in Europe and the USA,” *BMC Health Services Research*, 22, 2022. DOI `10.1186/s12913-022-08309-3`.

### Dataset evidence

The study uses openly accessible national drug-shortage notifications from national authorities. Comparable registers from Finland, Sweden, Norway, Spain and the USA were analyzed for January–September 2020, totaling **5,132 shortage reports**.

Supplementary files have persistent Figshare DOIs, including `10.6084/m9.figshare.20363552.v1` (plus associated additional-file records).

### SemRisk role

This is currently the strongest **Paper-1 primary dataset direction** for the preferred case because it links:

`medicine/product → shortage report → country/authority → therapeutic/formulation context → medicine availability`.

It can test SemRisk's Pharma/Health bridge without requiring a knowledge-graph contribution.

Exact file schema, version and license still require qualification before final selection.

---

## Anchor 5 — Pharmacovigilance transferability dataset

**Dataset:** Zhang, Sumathipala, Zitnik, “Population-scale patient safety dataset from 2013 to 2020 (Sep.),” Harvard Dataverse DOI `10.7910/DVN/G9SHDA`.

### Peer-reviewed linkage

Associated peer-reviewed work uses FAERS-based drug/adverse-event reports and reports a processed dataset of 1,425,371 reports in the final analysis, involving 2,821 drugs and 7,761 adverse events, with source data spanning January 2013–September 2020. The published data-availability statement points directly to the Harvard Dataverse DOI.

### SemRisk role

This is a promising **secondary E11 transferability** dataset because it moves from supply/availability risk to pharmacovigilance/patient-safety evidence. It should be optional for Paper 1 and only used if it adds distinct evaluation evidence without crowding the eight-page paper.

---

## Emerging Pharma risk conceptual families

These are **evidence-backed candidate families**, not yet canonical SemRisk modules/classes:

| Family | Candidate concerns |
|---|---|
| Supply | supplier failure, sourcing, capacity, delivery reliability, raw materials, flexibility |
| Availability | shortage, stock visibility, demand/capacity mismatch, forecasting, inventory |
| Manufacturing | process development, plant/network design, production cost, quality system, GMP |
| Quality | material quality, quality system, pharmaceutical QRM, hazard/harm |
| Logistics | transportation, counterfeit, distribution continuity |
| Financial | FX, interest, cash flow, tariff, supply cost |
| Market | demand, consumer/market change, price/economic effects |
| Regulatory | regulatory change, compliance, approval/oversight constraints |
| Strategic | strategy, M&A, R&D pipeline, organization/process, technology |
| Political | political/geopolitical instability, sanctions/external disruption |
| Health consequence | medicine access, care-delivery impact, patient safety/harm |
| Evidence / monitoring | shortage registers, inspections, adverse events, post-market evidence |

## Preferred Paper-1 case remains provisional

**Supply/production disruption → medicine availability/shortage → healthcare delivery impact → patient consequence**

This case remains preferred because it supports Enterprise/Architecture + Pharma + Health semantics and has promising public empirical evidence. It must change if dataset qualification shows a materially stronger evidence-backed case.

## Next Pharma extraction priorities

1. source-complete Jaberidoost table/risk extraction with exact source locators;
2. 2024 review full extraction;
3. current drug-shortage cause/model reviews;
4. ICH Q9(R1) concept/method extraction;
5. Eberhardt 2025 data/model extraction;
6. shortage-register schema qualification;
7. map Pharma risk candidates to CM-PharmE concepts;
8. identify which terms are Core, Pharma profile, SupplyChain profile, Health bridge or method-only.
