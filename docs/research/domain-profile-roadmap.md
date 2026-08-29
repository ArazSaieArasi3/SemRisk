# SemRisk Domain Profile Roadmap

**Status:** planning baseline  
**Date:** 2026-08-29

## 1. Principle

SemRisk should pursue **real comprehensiveness through a small well-founded core plus explicit domain profiles**, not through one oversized undifferentiated ontology.

The core must remain reusable. Domain profiles may introduce domain-specific kinds, roles, relators, modes, events, situations, information entities, constraints and mappings only when the domain evidence justifies them.

A domain profile is not allowed to become a list of generic `Object` subclasses. Each candidate class must have an explicit modeling rationale and, where applicable, a UFO/OntoUML stereotype or foundational alignment.

---

## 2. Priority profile portfolio

| Priority | Profile | Purpose | Main external evidence | Main internal integration | Publication role |
|---|---|---|---|---|---|
| `P0` | **Core** | Domain-neutral semantics of risk, value, scenario, assessment, evidence, treatment, control, observation and responsibility | COVER, ROSE, ISO 31000, ISO 31073, IEC 31010 | OGCM-RF | Foundation of all papers |
| `P0` | **Enterprise** | Operational enterprise risk knowledge, risk-register semantics, ownership, assessment lifecycle | ISO 31000, COSO ERM, OCEG GRC | Jira risk attributes | **Primary Paper 1** |
| `P0` | **Architecture** | Connect risk to objectives, capabilities, processes, applications, data, technology and change initiatives | TOGAF/ArchiMate literature, ontology-based security modeling in ArchiMate | CM-PharmE business-architecture lineage | **Primary Paper 1** |
| `P1` | **Health** | Broad reusable risk profile across clinical, patient-safety, digital-health, public-health and care-delivery contexts | ReMINE, ARK, ISO 14971 where applicable, healthcare safety literature | SemRPM, SemCRS, PHR and future health ontologies | Highest-priority domain expansion |
| `P1` | **Pharma** | Pharmaceutical quality, pharmacovigilance, ecosystem, regulatory, supply and post-market risk | ICH Q9, PV-SDO, pharmacovigilance literature | **CM-PharmE** | Bounded Paper 1 case; major Paper 2 profile |
| `P2` | **Governance** | Appetite, tolerance, policy, compliance, audit, issue, control accountability | COSO ERM, OCEG GRC | CM-PharmE governance concepts | Paper 2 |
| `P2` | **News** | External event/claim/source/narrative signals for risk identification and reassessment | news-risk KG research, event forecasting, external-risk sensing literature | **Newsium**, **Commentium** | Paper 2 / Risk Intelligence |
| `P2` | **Security** | Threat, vulnerability, prevention, security mechanisms, cyber-risk monitoring | ROSE, Open FAIR, STIX-oriented literature | Digital systems across portfolio | Paper 2 or specialized paper |
| `P2` | **Finance** | Credit, liquidity, market, operational, counterparty, fraud, settlement and systemic risk | financial risk standards + KG literature | SCF, Loan, Ledger, BNPL, Reconciliation, Trading | Later domain paper / product |
| `P2` | **SupplyChain** | Supplier, dependency, disruption, logistics, resilience and propagation risk | supply-chain risk literature | SemSCF, CM-PharmE | Later domain/profile paper |
| `P3` | **AI** | AI-system risk, impact, compliance, model/data risk | AIRO, AI regulation, ISO AI risk standards | AI-enabled product components | Later profile |
| `P3` | **Environment** | Environmental, exposure, cumulative and public-health risk | EPA-style risk assessment, cumulative-risk literature | Health profile | Later research wave |

Domain names intentionally avoid `and` / `&`.

---

## 3. Health-first architecture

Health is the preferred broad domain profile. Pharma should **not** be treated as the whole Health domain, and it should not be modeled as a simple subclass hierarchy beneath Health.

Recommended structure:

```text
SemRisk-Core
   ├── SemRisk-Enterprise
   ├── SemRisk-Architecture
   ├── SemRisk-Governance
   ├── SemRisk-Health
   │      ├── clinical risk patterns
   │      ├── patient-safety patterns
   │      ├── digital-health risk patterns
   │      └── public-health risk patterns
   └── SemRisk-Pharma
          ├── quality risk
          ├── pharmacovigilance risk
          ├── manufacturing risk
          ├── regulatory risk
          ├── supply risk
          └── post-market risk
```

`SemRisk-Pharma` intersects Health, Enterprise, Governance and SupplyChain. It is therefore a profile composition, not merely a child taxonomy.

---

## 4. CM-PharmE bridge design

CM-PharmE already contains ontologically typed concepts that SemRisk should respect rather than flatten.

### High-value CM-PharmE bridge candidates

| CM-PharmE concept | Existing stereotype | Candidate SemRisk use |
|---|---|---|
| Pharmaceutical Enterprise | kind | risk subject / accountable enterprise context |
| Organizational Stakeholder | role | risk owner, assessor, affected stakeholder candidate |
| Enterprise Capability | mode | capability exposed to or affected by risk |
| Ecosystem Actor | role | external risk source / affected actor context |
| Ecosystem Demand Signal | mode | possible observation/evidence input; requires ontological review before signal mapping |
| Ecosystem Supply Capacity | mode | exposure/resilience-relevant capability state |
| Pharmaceutical Business Process | perdurant | process exposed to risk or producing risk-relevant events |
| Individual Patient | role | affected stakeholder / patient-safety subject |
| Adverse Event Reporting Procedure | perdurant | evidence-generation / monitoring process |
| Regulatory Authority Entity | kind | governance actor |
| Regulatory Authority Role | role | oversight/accountability role |
| Governance Policy Framework | mode | governance constraint context |
| Compliance Requirement | mode | compliance-risk context |
| Risk Management Activity | perdurant | direct alignment candidate to SemRisk assessment/treatment lifecycle |
| Digital Health Platform Component | kind | digital asset at risk |
| AI-Enabled Clinical Decision Support System | kind | AI/Health risk subject |
| Blockchain-Based Supply Chain Ledger | kind | digital/supply asset at risk |
| Patient Record Quality | mode | quality/value condition linked to information risk |
| Pharmacovigilance Requirement | mode | Pharma governance constraint |
| Post-Market Surveillance Activity | perdurant | risk observation / evidence-generation activity |
| Real-World Evidence Platform | kind | evidence infrastructure |

### Bridge rule

SemRisk should prefer relations such as:

- `isRiskSubjectIn`
- `isAssetAtRiskIn`
- `isAffectedByRiskScenario`
- `isPotentialSourceIn`
- `providesEvidenceForAssessment`
- `participatesInRiskManagementActivity`
- `isGovernedByRiskRequirement`
- `isProtectedByControl`

Exact relation names and ontological commitments remain to be validated against COVER, UFO and the CM-PharmE relation registry before implementation.

---

## 5. Newsium bridge design

Newsium is not a Risk ontology and SemRisk should not absorb its core.

The intended integration pattern is:

```text
Newsium
NewsItem / Event / Claim / Source / Actor / Narrative / Topic / Time
                  ↓ contextual bridge
SemRisk
Evidence / Observation / RiskSignalRole / TriggerEvidence / AssessmentContext
                  ↓
RiskIdentification / RiskAssessment / Reassessment / Alert
```

### Key semantic rule

A news article is **not intrinsically a risk**. A claim is **not intrinsically a risk**. A real-world event is **not automatically a risk event** merely because it is reported in news.

Risk relevance should be context-dependent and traceable. Candidate approach:

- Newsium keeps identity and semantics of NewsItem, Claim, Source, Event and Narrative;
- SemRisk represents the assessment context in which an item/event/claim plays a risk-relevant evidential or signaling role;
- provenance must preserve which source and claim informed which assessment;
- confidence/trust should be modeled separately from the underlying event itself.

This bridge is central to the future **Risk Intelligence Platform**.

---

## 6. Commentium bridge design

Commentium models a Comment as a **context-embedded communicative event**, with separate CommentMessage, Interpretation, InterpretedMeaning, Agent roles, Situation, Stance and AssertedRelation structures.

SemRisk should reuse those distinctions.

Potential flow:

```text
Commentium Comment
   -> CommentMessage
   -> Interpretation
   -> InterpretedMeaning / AssertedRelation
             ↓ evidence bridge
SemRisk EvidenceItem / ObservationResult
             ↓
RiskSignalRole
             ↓
Risk Assessment / Reassessment
```

Example future applications include:

- reputational risk;
- product safety signal detection;
- healthcare experience risk;
- pharmacovigilance-supporting consumer evidence;
- policy/social response risk;
- emerging issue detection.

Analytical outputs such as sentiment or stance must not be silently treated as observed facts; provenance should distinguish observed, contextual and analytically derived layers.

---

## 7. Risk Intelligence Platform direction

The product direction should be built on SemRisk rather than define SemRisk from software requirements.

### Candidate bounded contexts

These are **product/DDD candidates**, not ontology domains:

- Risk Registry
- Risk Assessment
- Evidence Hub
- Signal Ingestion
- Monitoring
- Alerting
- Architecture Mapping
- Control Management
- Domain Profiles
- Semantic Query
- Knowledge Graph
- Reporting

### Future product flow

```text
Internal systems / Risk Register / CM-PharmE data / Health data
Newsium / Commentium / external feeds
                  ↓
           ingestion + provenance
                  ↓
      semantic mapping to SemRisk
                  ↓
 observation / signal / evidence layer
                  ↓
 risk identification / reassessment
                  ↓
 controls / treatment / owner / objective impact
                  ↓
 dashboards / alerts / KG / API / explainable query
```

### Paper 1 boundary

Paper 1 should only implement enough product capability to validate the ontology:

- load a bounded Risk Register sample;
- show semantic mapping;
- query risk-to-architecture links;
- distinguish inherent/residual assessments;
- show a bounded Health/Pharma case;
- execute competency questions and validation.

Real-time signal ingestion and Newsium integration should be represented in architecture, but not claimed as completed Paper 1 functionality unless it is actually implemented and evaluated.

---

## 8. Ontological category checklist for every domain profile

Every profile must explicitly inspect whether evidence supports candidates in each category:

| Category | Typical examples |
|---|---|
| **Kind / Subkind** | organization, system, device, platform, product, dataset-bearing artifact |
| **Role** | risk owner, patient, regulator, assessor, supplier, affected stakeholder |
| **Relator** | responsibility assignment, oversight, contractual exposure, control assignment |
| **Mode / Disposition / Quality** | vulnerability, capability, appetite, tolerance, quality condition, resilience-related disposition |
| **Event / Perdurant** | risk event, adverse event, assessment activity, treatment activity, monitoring activity, disruption |
| **Situation** | exposure situation, noncompliance situation, control state, risk context |
| **Information Entity** | risk scenario description, register entry, assessment report, evidence item, claim, policy document |
| **Observation Entity** | observation event, observation result, indicator reading, threshold evaluation |

No profile passes conceptual review if it merely adds named domain objects without examining these categories and their relations.

---

## 9. Research wave sequence

### Wave C0 — ICAEA conference foundation

1. freeze Paper 1 contribution boundary;
2. map Jira risk attributes to candidate ontology constructs;
3. establish Core + Enterprise + Architecture minimum model;
4. add minimum Health bridge;
5. add bounded Pharma/CM-PharmE scenario;
6. implement OWL/Turtle + SHACL + competency questions;
7. perform OGCM-RF-style initial evaluation;
8. write the IEEE-format ICAEA manuscript in parallel with artifact development.

### Wave J1 — Comprehensive ontology expansion

1. deepen COVER / ROSE grounding;
2. build Health profile systematically;
3. expand Pharma profile;
4. add Governance, Security, Finance and SupplyChain profiles;
5. formalize temporal assessment, uncertainty, evidence and observation;
6. build cross-profile mapping and coverage evaluation;
7. expand datasets and expert validation.

### Wave J2 — Risk intelligence

1. formalize News bridge;
2. formalize Commentium bridge;
3. build external-signal provenance model;
4. implement trigger / KRI / threshold / reassessment semantics;
5. evaluate explainable risk-signal chains;
6. validate Risk Intelligence Platform capabilities.

### Wave X — Specialized research papers

Potential later papers may focus on Health risk ontology, Pharma risk ontology/profile, News Risk Intelligence, Financial Risk Intelligence, SupplyChain propagation, Security risk integration or AI risk alignment. These should be opened only when evidence shows an independent contribution.

---

## 10. Immediate next executable tasks

1. Jira field-to-ontology semantic mapping.
2. SemRisk Core concept inventory v0.1.
3. Health evidence inventory.
4. CM-PharmE bridge subset selection.
5. Paper 1 competency-question registry.
6. Paper 1 figure architecture.
7. IEEE manuscript skeleton.

These tasks form the next working gate after the current alignment baseline.
