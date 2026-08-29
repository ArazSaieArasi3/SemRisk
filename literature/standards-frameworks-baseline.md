# SemRisk Standards and Frameworks Baseline

**Status:** W1 evidence baseline — version/authority checked; deep clause-level mining remains open under Issue #13.  
**Date:** 2026-08-29

This file records the minimum authoritative standards/framework landscape for SemRisk Paper 1. It is not yet a clause-complete extraction. Standard terms do not automatically become ontology classes.

## 1. ISO 31000:2018 — Risk management — Guidelines

- **Authority:** ISO / ISO/TC 262
- **Edition:** 2 (2018-02)
- **Current status checked:** published; ISO states it was reviewed and confirmed in 2023 and remains current.
- **Official locator:** https://www.iso.org/standard/65694.html
- **SemRisk relevance:** generic organization-independent management context; identification, analysis, evaluation, treatment, monitoring and communication; governance/strategy integration; threats and opportunities.
- **Initial disposition:** `STANDARD_ALIGNMENT`
- **Important modeling implication:** process/lifecycle language should inform management/profile semantics; it is not itself a foundational ontology.

## 2. ISO 31073:2022 — Risk management — Vocabulary

- **Authority:** ISO / ISO/TC 262
- **Edition:** 1 (2022-02)
- **Official locator:** https://www.iso.org/standard/79637.html
- **SemRisk relevance:** generic risk-management terminology across organizations and functions.
- **Important scope note:** official ISO material explicitly acknowledges that application-specific or disciplinary terminology can supplement or displace the generic vocabulary and that the vocabulary includes both threats and opportunities.
- **Initial disposition:** `TERMINOLOGY_ALIGNMENT`
- **Modeling implication:** use as a terminology/evidence source; definition matching does not establish ontological equivalence.

## 3. IEC 31010:2019 — Risk management — Risk assessment techniques

- **Authority:** IEC / TC 56; double-logo ISO/IEC publication
- **Edition:** 2.0; publication date 2019-06-13
- **Official locator:** https://webstore.iec.ch/en/publication/59809
- **SemRisk relevance:** selection and application of risk-assessment techniques; decisions under uncertainty; planning/implementing/verifying/validating assessment techniques.
- **Initial disposition:** `ASSESSMENT_METHOD_PROFILE`
- **Modeling implication:** assessment techniques belong in method/profile semantics rather than being hard-coded into the Core. The operational Jira formula `impact × likelihood` is one method-specific pattern and must not be universalized.

## 4. COSO Enterprise Risk Management — Integrating with Strategy and Performance

- **Authority:** COSO
- **Official locus:** https://www.coso.org/enterprise-risk-management
- **SemRisk relevance:** strategy, objectives, performance, governance and risk integration.
- **Initial disposition:** `FRAMEWORK_ALIGNMENT`
- **Paper-1 role:** source for Enterprise Risk Governance profile and objective/performance linkage, not a formal ontology.

## 5. OCEG GRC Capability Model

- **Authority:** OCEG
- **Current research target:** GRC Capability Model 3.5 / Red Book materials
- **Official locus:** https://www.oceg.org/grc-capability-model-red-book/
- **SemRisk relevance:** integrated governance, risk, compliance, audit, policy, issue, monitoring and control capability coverage.
- **Initial disposition:** `COVERAGE_BENCHMARK`
- **Paper-1 role:** coverage and governance comparison; full GRC profile remains broader than Paper 1.

## 6. Open FAIR

- **Authority:** The Open Group
- **Current standards:** Open Risk Taxonomy (O-RT) and Open Risk Analysis (O-RA), current versions to be release-verified before manuscript freeze.
- **Official locus:** https://www.opengroup.org/open-fair
- **SemRisk relevance:** quantitative risk-analysis taxonomy/method, especially information/cyber risk.
- **Initial disposition:** `ASSESSMENT_METHOD_PROFILE`
- **Modeling implication:** SemRisk should be method-independent enough to represent FAIR-style assessments without becoming a FAIR ontology.

## 7. TOGAF / ArchiMate risk-security guidance

- **Authority:** The Open Group
- **SemRisk relevance:** Enterprise Architecture integration, architecture objectives/elements and risk/security governance.
- **Initial disposition:** `ARCHITECTURE_ALIGNMENT`
- **Paper-1 role:** supports the architecture-driven enterprise application framing. Deep concept extraction and exact guide/version binding remain pending.

## 8. ICH Q9(R1) — Quality Risk Management

- **Authority:** ICH; official EMA publication locus
- **Current effective version checked:** Q9(R1), effective 2023-07-26; current EMA page identifies Revision 2 / Corr.2 publication.
- **Official locator:** https://www.ema.europa.eu/en/ich-q9-quality-risk-management-scientific-guideline
- **Scope:** pharmaceutical quality risk management across development, manufacturing, distribution, inspection and submission/review throughout lifecycle of drug substances/products and biological/biotechnological products.
- **Official keyword signals:** risk assessment, quality risk management, risk, harm, hazard, FMEA.
- **Initial disposition:** `PHARMA_STANDARD_ALIGNMENT`
- **Paper-1 role:** principal pharmaceutical quality-risk standard alignment where the chosen case touches quality/manufacturing/supply consequences.

## 9. ISO 14971:2019 — Medical devices — Application of risk management to medical devices

- **Authority:** ISO
- **Edition:** 3 (2019); current edition to be rechecked at final freeze.
- **Official locator:** https://www.iso.org/standard/72704.html
- **SemRisk relevance:** Health/medical-device risk management; hazard, risk estimation/evaluation, controls and lifecycle/post-production monitoring.
- **Initial disposition:** `HEALTH_STANDARD_ALIGNMENT`
- **Paper-1 role:** comparative Health evidence; not central unless the selected case moves toward medical-device risk.

---

## Cross-standard modeling questions for reconciliation

1. How should SemRisk reconcile generic `risk` terminology across ISO 31000/31073 with COVER's value/risk model?
2. How should downside threat and upside opportunity be represented without forcing opportunity into a loss-only semantics?
3. Which constructs are Core versus management-framework/profile constructs (e.g., appetite, tolerance, policy, audit)?
4. Which assessment quantities are method-independent and which are method-specific (ordinal scale, probability, frequency, monetary loss, severity)?
5. How should treatment strategies and concrete controls/activities be distinguished?
6. How should standards' lifecycle/process requirements map to events/activities versus information artifacts and workflow states?
7. Which Enterprise Architecture concepts should be imported, referenced or bridged rather than redefined?

## Paper 1 minimum standard set

At minimum, the conference manuscript should maintain traceable alignment to:

- ISO 31000:2018
- ISO 31073:2022
- IEC 31010:2019
- one Enterprise/GRC framework source (COSO and/or OCEG)
- relevant EA guidance
- ICH Q9(R1) for the Pharma case

Open FAIR and ISO 14971 remain useful comparison/profile evidence if space and claim relevance justify inclusion.

## Remaining work under Issue #13

- clause/page-level extraction where access permits;
- exact source/version/license/access records;
- raw term/definition registry;
- cross-standard concept/relation conflict matrix;
- SemRisk disposition for each extracted construct;
- standard→CQ and standard→evaluation mapping;
- final version refresh at Gate G5.
