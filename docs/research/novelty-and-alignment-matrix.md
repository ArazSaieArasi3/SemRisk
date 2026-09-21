# SemRisk Novelty and Alignment Matrix

**Status:** Gate S0 baseline  
**Date:** 2026-08-29  
**Purpose:** prevent novelty overclaiming, make reuse decisions explicit, and establish a traceable boundary between SemRisk, existing reference ontologies, standards, risk-management frameworks, domain ontologies and adjacent semantic systems.

## 1. Research position

SemRisk is **not** intended to introduce another isolated definition of risk. The research program aims to build a **comprehensive, modular, well-founded and executable ontology network for risk knowledge** that can be specialized through domain profiles.

The current candidate differentiator is the integration of six concerns that are often treated separately:

1. well-founded risk semantics;
2. operational enterprise risk-register semantics;
3. explicit separation of risk phenomena, scenario descriptions, records, assessments, results and workflow states;
4. temporal, evidence-aware reassessment;
5. enterprise-architecture and governance linkage;
6. reusable domain profiles, beginning with Health and Pharma and later extending to additional domains.

The strongest novelty claim must be established by **combination, integration quality, execution and evaluation**, not by claiming that the individual ideas are unprecedented.

---

## 2. External alignment matrix

| Source / artifact | Type | Primary scope | Foundational grounding | What overlaps with SemRisk | What SemRisk should reuse or align | Gap relevant to SemRisk | Current decision |
|---|---|---|---|---|---|---|---|
| **COVER — Common Ontology of Value and Risk** (Sales et al., ER 2018) | Well-founded reference ontology | Value, goals, risk experience, risk events, threat/loss, vulnerability | UFO / OntoUML | Core semantics of value, goals, threats, losses and risk events | Reuse or formally align foundational risk constructs; avoid redefining them without evidence | Does not by itself provide the complete operational enterprise risk-register, governance, domain-profile, evidence-history and application architecture targeted by SemRisk | **FOUNDATION / REUSE** |
| **ROSE — Reference Ontology for Security Engineering** (Oliveira et al., ER 2022) | Well-founded reference ontology | Security from a risk-treatment perspective | UFO + COVER + prevention ontology | Treatment, prevention, security mechanism, risk events | Reuse for Security profile and treatment semantics where applicable | Security-focused; not a complete cross-domain enterprise risk knowledge model | **PROFILE REUSE** |
| **Oliveira et al. 2025 — Toward an ontology-based modeling for risk management** | Research programme / ontology-network proposal | Integrated risk-management ontology network, semantic interoperability, DSL/services | UFO + COVER + ROSE + ROT + ResiliOnt | Very close to SemRisk Core/method ambition; explicitly distinguishes risk scenarios as possible events from incidents as past occurrences | Mandatory closest-program comparator; track follow-up artifacts and method lineage | SemRisk must differentiate through the narrower operational phenomenon/record/assessment-result/risk-state/workflow-state/evidence pattern, governed traceability, executable projection and bounded CM-PharmE federation | **MANDATORY CLOSEST PROGRAM** |
| **ISO 31000:2018**; Edition 3 under development in 2026 | International standard | Generic organizational risk management | Standard, not foundational ontology | Principles, identification, analysis, evaluation, treatment, monitoring, communication | Align process vocabulary and management lifecycle; version mappings because ISO/CD 31000 is under development | Not a formal ontology and not a machine-executable semantic integration model | **STANDARD ALIGNMENT** |
| **ISO 31073:2022** | Vocabulary standard | Risk-management terminology | Standard vocabulary | Terminology | Use as terminology/evidence source; do not equate vocabulary entries automatically with ontology classes | Terminological, not a foundational ontological account | **TERMINOLOGY ALIGNMENT** |
| **IEC 31010:2019** | Assessment-technique standard | Risk-assessment techniques | Standard | Assessment methods | Model assessment techniques as method/profile entities rather than hard-code one method into the core | Technique catalogue does not solve semantic integration among risk records, evidence, architecture and domains | **METHOD PROFILE** |
| **COSO ERM — Integrating with Strategy and Performance** | Enterprise risk-management framework | Strategy, performance, governance, ERM | Management framework | Objectives, governance, performance, risk responses | Align enterprise governance / objective / performance concerns | Not a formal ontology; operational semantics and machine-readable traceability remain external | **FRAMEWORK ALIGNMENT** |
| **OCEG GRC Capability Model** | GRC capability model | Governance, risk, compliance, audit, policy, issue management | Capability framework | Policies, controls, issues, audit, monitoring, governance | Reuse as competency and coverage benchmark for Governance profile | Does not provide the well-founded and executable risk ontology targeted by SemRisk | **COVERAGE BENCHMARK** |
| **Open FAIR O-RT / O-RA** | Risk taxonomy + quantitative analysis standard | Quantitative information/cyber risk | Risk-factor taxonomy | Loss events, frequency, magnitude, quantitative assessment | Treat as an Assessment Method / Security profile; align without making SemRisk dependent on FAIR | Primarily quantitative information-risk analysis rather than general cross-domain semantics | **METHOD PROFILE** |
| **CORAS** | Model-driven risk analysis language | Threat/scenario analysis | Modeling method | Scenarios, threats, treatment | Candidate mapping target for Scenario profile | A risk-analysis language, not the complete cross-domain ontology network | **FUTURE MAPPING** |
| **Integrated GRC Conceptual Model** (Vicente & da Silva, 2011) | Conceptual model | Integrated governance-risk-compliance | Ad-hoc conceptual language | Risk, process, control, policy, objective, KRI, issue, audit, monitoring | Use as historical GRC benchmark and concept source | Reported evaluation was partial; no well-founded ontology, executable OWL/SHACL/CQ stack or modern traceability architecture | **BENCHMARK / EVIDENCE** |
| **Risk Knowledge Graph / Risk Register KG approaches** | Knowledge-graph applications | Risk-register integration, queries, dashboards | Varies | Graph-based risk representation | Reuse implementation patterns only where evidence supports them | KG construction alone is not novelty; SemRisk must semantically repair/register distinctions and ground them ontologically | **IMPLEMENTATION BENCHMARK** |
| **Enterprise dynamic risk KG** (Yang & Liao, 2021) | Dynamic knowledge graph | Multi-source enterprise risk, temporal evolution, reasoning | Bottom-up KG / ontology construction | Time, evolving risk events, reasoning | Benchmark Dynamic profile and future product architecture | Dynamic KG is prior art; SemRisk novelty cannot be merely “dynamic risk KG” | **DYNAMIC BENCHMARK** |
| **Ontology-based dynamic risk system** (Vega-Barbas et al., 2019) | Ontology-based platform | Dynamic risk, real-time context, trust of sources | Semantic-web ontology architecture | Continuous sensing, risk context, source trust | Benchmark Risk Intelligence Platform | Dynamic risk monitoring and CTI-style enrichment already exist | **PLATFORM BENCHMARK** |
| **AIRO** (Golpayegani et al., 2022) | Domain risk ontology | AI risk, regulation, ISO-aligned documentation | Ontology + regulatory alignment | Risk documentation, assessment, regulation | Candidate AI profile alignment | Domain-specific; not a generic enterprise/health risk core | **DOMAIN PROFILE BENCHMARK** |
| **Riskman Ontology & Shapes** (2024) | Domain ontology + SHACL | Medical-device risk management | ISO 14971 / SHACL | Hazard, harm, risk-control documentation, conformity validation | Important benchmark for Health profile; potentially reuse mappings to ISO 14971 | Medical-device specific; SemRisk Health must be broader and avoid duplicating Riskman where reuse is justified | **HEALTH BENCHMARK** |
| **ISO 14971:2019** | Medical-device risk-management standard | Medical devices through lifecycle | Standard | Hazard identification, risk estimation/evaluation, controls, post-production monitoring | Major Health profile standard; current edition confirmed in 2025 | Device-specific rather than general health risk | **HEALTH STANDARD ALIGNMENT** |
| **ReMINE** (2009) | Ontology-based healthcare risk platform | Patient-safety risk prediction/detection/monitoring | Ontology-enabled platform | Early warning, mitigation, hospital process correlation | Benchmark Health profile and Risk Intelligence product | Older platform; not a general comprehensive ontology network and not aligned to SemRisk’s planned inter-ontology architecture | **HEALTH PLATFORM BENCHMARK** |
| **ARK Platform** (2020) | Semantic-web clinical-risk platform | Socio-technical clinical safety risk | Linked Data + clinical safety taxonomy | Operational data + qualitative risk integration, continuous/adaptive management | Benchmark Health profile, Evidence and Observation modules | Clinical safety focused and not intended as a general enterprise risk ontology | **HEALTH PLATFORM BENCHMARK** |
| **PV-SDO** (2014) | Pharmacovigilance ontology | Drug-safety signal detection | Semantic integration ontology | Signals, heterogeneous data, methods, provenance | Important for Pharma profile and News/Signal bridge | Pharmacovigilance signal detection only; not full pharmaceutical ecosystem risk | **PHARMA BENCHMARK / POSSIBLE REUSE** |
| **ICH Q9(R1)** | Pharmaceutical quality-risk guideline | Pharmaceutical quality across development, manufacturing, distribution, inspection and lifecycle | Industry guideline | Hazard, harm, risk assessment, quality-risk management methods | Primary Pharma profile alignment | Quality-risk management does not cover the full enterprise/ecosystem risk space | **PHARMA STANDARD ALIGNMENT** |
| **Institutional risk identification using automated news profiling** (Mahfouz et al., 2021) | News-to-risk system | Global news monitoring, risk matching, triggers, impacted operations | KG + embeddings | External signals, triggers, risk proximity, affected operations | Important benchmark for News profile and Risk Intelligence Platform | News-to-risk mapping already exists; SemRisk must contribute ontology-grounded, explainable cross-ontology signal semantics rather than simple news matching | **NEWS-RISK BENCHMARK** |
| **Knowledge-based news event analysis / forecasting** (2025) | Event KG / neurosymbolic framework | News events, causal analysis, forecasting | Knowledge graph | Event extraction, causal knowledge, forecasting | Benchmark Newsium–SemRisk integration | Not a comprehensive risk ontology | **NEWS BENCHMARK** |

---

## 3. Internal ontology integration matrix

| Internal asset | Existing semantic strengths | SemRisk relationship | Modeling rule | Conference relevance |
|---|---|---|---|---|
| **OGCM-RF** | Layered conceptual/formal/data/mapping/evaluation/research/application architecture; release-specific evaluation | SemRisk should be an implementation profile / adopting repository | Reuse repository architecture, stable IDs, traceability, release discipline and E1–E9 evaluation logic | **High** — enables reproducible ontology paper artifacts |
| **CM-PharmE** | 39 canonical concepts spanning pharmaceutical enterprise, stakeholders, capabilities, ecosystem relations, processes, governance, pharmacovigilance, post-market surveillance, digital health and supply-chain constructs; UFO/OntoUML grounding | Main Pharma integration target and immediate Health-related reuse source | Do not collapse CM-PharmE entities into generic `Object`. Preserve/reuse correct stereotypes: kinds, roles, relators, modes, perdurants. Introduce bridge relations from SemRisk risk subjects/events/assessments to CM-PharmE entities | **High** — bounded Pharma case and explicit citation path |
| **Newsium** | Research-first news ontology locus; planned separation of news, event, source, claim, actor, document, publishing semantics; target News Intelligence capability | External signal / evidence source for Risk Intelligence; bridge through Event, Claim, Source and temporal constructs | News items remain Newsium information artifacts; real-world events remain events; SemRisk should type their *risk relevance* contextually rather than redefine Newsium core concepts | **Architectural only in Paper 1**; major later contribution |
| **Commentium** | Comment as context-embedded communicative event; explicit separation of Comment event, CommentMessage, Interpretation, InterpretedMeaning, roles, norms and Situation; UFO grounding | Social/public/consumer signal source for reputation, safety, product, policy or ecosystem risks | Prefer mapping interpreted content / asserted relations / contextual evidence into SemRisk Evidence or Signal roles; do not turn Comment into a generic risk object | **Not central in Paper 1**; important Risk Intelligence extension |
| **SemRPM / SemCRS / broader health ontologies** | Domain-specific health semantic models and datasets | Candidate Health profile integration cases after SemRisk Core stabilizes | Build Health bridge patterns that can be reused across health ontologies; avoid one-off Pharma-only semantics | **Future / optional evidence** |

---

## 4. Candidate ontological distinctions to preserve

SemRisk should explicitly test and document the following distinctions before formal implementation:

| Operational term | Candidate ontological treatment | Why it matters |
|---|---|---|
| `Risk Event` | Reuse/align COVER event semantics | Avoid inventing a competing foundational event model |
| `Risk Scenario` | Structured information object describing possible event chains / situations | A scenario description is not the event itself |
| `Risk Register Entry` | Information artifact / record | A database/Jira row is not the risk phenomenon |
| `Risk Assessment` | Deliberate assessment activity / process | The act of assessing is distinct from its output |
| `Risk Assessment Result` | Information content / result | Likelihood, impact and risk level are contextual outputs, not timeless properties of the risk |
| `Risk State` | Time-indexed assessment or situation characterization | Enables reassessment without creating a new “risk” for every score change |
| `Workflow State` | State of the management record/process | `Closed` record does not entail that the risk ceases to exist |
| `Evidence Item` | Information content with provenance | Supports traceable decisions and later automated sensing |
| `Observation` | Observation event/result pair, to be refined | Required for KRI and continuous risk intelligence |
| `Risk Signal` | Context-dependent analytical/epistemic role played by an observation, claim or information item | Prevents treating every news article/comment as an intrinsic risk object |
| `Risk Owner` | Role played by an agent/organizational actor | Preserves UFO role semantics |
| `Risk Ownership Assignment` | Candidate relator / responsibility relation | Avoids reducing accountability to a string field |
| `Vulnerability` | Reuse/align COVER/ROSE disposition semantics where applicable | Prevents vague “weakness” classes |
| `Control` / `Treatment` | Reuse/align ROSE and management standards as appropriate | Distinguish preventive mechanisms, treatment plans and executed treatment activities |

These are **candidate design commitments**, not yet final axioms.

---

## 5. Candidate contribution register

| ID | Candidate contribution | Paper 1 status | Paper 2 status | Evidence burden |
|---|---|---|---|---|
| `SEM-C01` | Ontological separation of risk phenomenon/scenario/record/assessment/result/workflow state | **Primary** | Retained / expanded | Closest-work comparison + formal model + data mapping |
| `SEM-C02` | Architecture-linked risk knowledge connecting risk to objectives, capabilities, processes and controls | **Primary** | Expanded | EA benchmark + competency questions + case |
| `SEM-C03` | Executable mapping of a real operational Risk Register into ontology-grounded semantics | **Primary** | Expanded to multiple schemas | Jira spreadsheet mapping + SHACL/CQ validation |
| `SEM-C04` | Health-first domain profile architecture with Pharma specialization and CM-PharmE bridge | **Bounded case** | **Primary expansion** | Health/pharma literature, standards, ontology mappings |
| `SEM-C05` | Temporal and evidence-aware risk reassessment | Minimal semantic hooks | **Primary** | Temporal model + provenance + longitudinal data |
| `SEM-C06` | Newsium / Commentium bridges for risk-signal semantics | Architecture note only | **Primary extension** | News-risk literature + external-signal datasets + cross-ontology CQ |
| `SEM-C07` | Risk Intelligence Platform based on SemRisk | Prototype boundary only | Application validation | Product architecture + data ingestion + explainability + evaluation |
| `SEM-C08` | Comprehensive cross-domain risk ontology network | **Do not claim in Paper 1** | Long-term research claim, only after coverage evaluation | Systematic evidence registry + domain coverage + external expert evaluation |

---

## 6. Paper 1 novelty boundary — ICAE 2026

### Title status

**TBD.** The old ICAEA-era working title is superseded. Final title is controlled by the ICAE 2026 research contract and #32 after evidence/evaluation maturation.

### Primary contributions to claim

1. **Semantic disambiguation:** a well-founded operational pattern separating the managed risk phenomenon from its scenario description, register record, assessment activity, assessment result, treatment and workflow state.
2. **Enterprise Architecture binding:** explicit links from risk knowledge to objectives, capabilities, processes, controls and accountable actors.
3. **Executable industrial demonstration:** mapping a real Jira-style Risk Register schema to SemRisk with machine-readable ontology artifacts, SHACL/competency-query validation and a bounded Health/Pharma scenario referencing CM-PharmE.

### Claims to avoid in Paper 1

- “the first comprehensive risk ontology”;
- “the first dynamic risk knowledge graph”;
- “the first news-based risk intelligence platform”;
- “complete coverage of all risk-management standards”;
- “validated applicability to all domains”.

---


## 6A. Evidence-driven novelty refinement — 2026-09-21

Deep mining of SRC-PA-005 and current-work refresh materially narrow the SemRisk novelty boundary.

### Closest research-program lineage

The 2025 Oliveira et al. proposal is no longer treated as an isolated proposal-only citation. Current evidence shows a continuing programme with concrete outputs, including:

- **An Ontological Lens on Attack Trees: Toward Adequacy and Interoperability** (FOIS 2025) — executes COVER-grounded ontological analysis of a major risk technique.
- **WATCHDOG** (CAiSE 2025) — operationalizes COVER notions in an ontology-aware formal risk-assessment framework with disruption graphs, logic and query language.
- **A Unified Architecture for Risk Reasoning: Bridging Ontologies, Theorem Proving, and Model Checking** (SAFECOMP Workshops 2026) — extends the programme toward integrated ontology-grounded formal verification.
- **News-Informed Probabilistic Models for AI Risk Analysis** (CAiSE 2026) — relevant primarily to future Risk Intelligence/Newsium claims and demonstrates current news-informed quantitative risk-analysis prior art.

### Resulting Paper-1 novelty controls

1. **Generic risk-management ontology network** is not a SemRisk novelty claim.
2. **UFO/OntoUML/gUFO grounding** is not a novelty claim.
3. **Scenario-as-possible-event vs incident-as-realized-occurrence** is prior art.
4. **Ontology + formal risk reasoning / propagation / probabilistic analysis** is not a safe standalone novelty claim.
5. **Ontology-driven semantic interoperability among risk techniques/data sources** is explicit prior work.
6. SemRisk's strongest remaining candidate differentiator is the integrated operational semantic separation of:
   **risk phenomenon/event/scenario → information artifact/register entry → assessment activity → assessment result → risk state → workflow state → evidence/provenance → treatment/responsibility**, tied to governed source traceability and bounded executable projections.
7. SR-C2 and SR-C3 remain supporting contributions but are narrower: generic EA-risk linkage and generic Pharma QRM ontology are both prior art.
8. Final differentiation must compare **implemented/evaluated SemRisk evidence** against both prior proposals and their concrete follow-up artifacts, not compare SemRisk implementation against an older proposal alone.

## 7. Paper 2 novelty direction

The journal extension should move from an enterprise-risk-register contribution to a broader **SemRisk ontology network** with:

- deeper COVER / ROSE grounding;
- Health profile as the first broad domain profile;
- Pharma profile as an intersecting specialization using CM-PharmE, ICH Q9, pharmacovigilance and supply-risk evidence;
- Governance, Architecture, Security, Finance and SupplyChain profiles;
- Observation, evidence, uncertainty and temporal reassessment;
- Newsium / Commentium semantic bridges;
- Risk Intelligence Platform validation;
- multi-dataset mapping;
- full OGCM-RF E1–E9 evaluation.

The eventual comprehensive claim should be treated as an **evaluated coverage objective**, not a rhetorical adjective.

---

## 8. Evidence quality policy

| Tier | Evidence type | Use |
|---|---|---|
| `A` | International standards, official ontology specifications, peer-reviewed high-quality research | Primary design / claim evidence |
| `B` | Peer-reviewed applied systems, reputable proceedings, official framework documentation | Benchmark / implementation evidence |
| `C` | Preprints, technical reports, patents, repositories | Discovery leads and supplementary evidence |
| `D` | Vendor/product pages or informal material | Product benchmark only; never sufficient for academic novelty claims |

Every future comparator should record source URL/DOI, publication year, evidence tier, extracted concepts, overlap, gap, reuse decision and affected SemRisk module.

---

## 9. Initial verified sources

- Sales, T. P. et al. **The Common Ontology of Value and Risk**. ER 2018. DOI: `10.1007/978-3-030-00847-5_11`. Repository: https://github.com/unibz-core/value-and-risk-ontology
- Oliveira, Í. et al. **An Ontology of Security from a Risk Treatment Perspective**. ER 2022. DOI: `10.1007/978-3-031-17995-2_26`.
- Oliveira, Í. et al. **Toward an ontology-based modeling for risk management**. VMBO 2025 / CEUR 4129.
- ISO 31000:2018, current published edition; ISO/CD 31000 Edition 3 under development in 2026: https://www.iso.org/standard/65694.html and https://www.iso.org/standard/88574.html
- ISO 31073:2022 Risk management — Vocabulary.
- IEC 31010:2019 Risk management — Risk assessment techniques.
- COSO **Enterprise Risk Management — Integrating with Strategy and Performance**: https://www.coso.org/enterprise-risk-management
- The Open Group **Open FAIR** O-RA 2.0.1 / O-RT 3.0.1: https://www.opengroup.org/open-fair
- ISO 14971:2019 Medical devices — Application of risk management to medical devices: https://www.iso.org/standard/72704.html
- ICH Q9(R1) Quality Risk Management: https://www.ema.europa.eu/en/ich-q9-quality-risk-management-scientific-guideline
- Yang, B.; Liao, Y. **Research on enterprise risk knowledge graph based on multi-source data fusion**. Neural Computing and Applications, 2021. DOI: `10.1007/s00521-021-05985-w`.
- Vega-Barbas, M. et al. **Ontology-Based System for Dynamic Risk Management in Administrative Domains**. Applied Sciences, 2019. DOI: `10.3390/app9214547`.
- Golpayegani, D.; Pandit, H. J.; Lewis, D. **AIRO: An Ontology for Representing AI Risks Based on the Proposed EU AI Act and ISO Risk Management Standards**. 2022. DOI: `10.3233/SSW220008`.
- Gorczyca, P. et al. **Risk Management for Medical Devices via the Riskman Ontology & Shapes**. 2024 preprint. DOI: `10.48550/arXiv.2405.09875`.
- Crotti, A. et al. **The ARK Platform: Enabling Risk Management Through Semantic Web Technologies**. ICBO 2020 workshop.
- Carenini, M. **ReMINE: an ontology-based risk management platform**. Studies in Health Technology and Informatics, 2009.
- Koutkias, V.; Jaulent, M.-C. **PharmacoVigilance Signal Detectors Ontology (PV-SDO)**. SWAT4LS 2014.
- Mahfouz, M.; Nourbakhsh, A.; Shah, S. **A Framework for Institutional Risk Identification using Knowledge Graphs and Automated News Profiling**. 2021 preprint.

---

## 10. Gate S0 completion criteria

This baseline is sufficient to start concept extraction, but Gate S0 is not fully closed until:

- each comparator is represented in a machine-readable evidence registry;
- the Jira risk-attribute spreadsheet is mapped field-by-field into candidate SemRisk constructs;
- Health and Pharma profile boundaries are frozen for Paper 1;
- the CM-PharmE bridge subset is selected;
- candidate competency questions are registered;
- the contribution statements are rechecked against a second closest-work search immediately before manuscript freeze.
