# ICAEA 2026 — SemRisk Paper 1

**Status:** manuscript planning baseline  
**Target format:** IEEE conference format  
**Target venue:** ICAEA 2026  
**Submission deadline:** 2026-09-25

## Working title

**SemRisk: An Ontology-Grounded Enterprise Risk Register for Architecture-Driven Risk Governance and Resilience**

Alternative short title:

**SemRisk-RR: Ontology-Grounded Risk Registers for Architecture-Driven Resilience**

## Paper role in the SemRisk research programme

This paper is the **first bounded publication** of the SemRisk programme. It must not attempt to publish the entire comprehensive ontology network in six pages.

The paper should introduce and evaluate the subset needed to demonstrate:

1. semantic separation of risk phenomena, scenarios, records, assessments, assessment results, treatments and workflow states;
2. Enterprise Architecture linkage to objectives, capabilities, processes, controls and accountable actors;
3. executable mapping of an operational Jira-style Risk Register;
4. a bounded Health/Pharma scenario connected to CM-PharmE;
5. an initial reproducible evaluation package.

## Research questions

### RQ1
How can conventional enterprise Risk Register constructs be ontologically disambiguated to separate risk phenomena, scenario descriptions, register records, assessment activities, assessment results, treatments and workflow states?

### RQ2
How can ontology-grounded risk knowledge be connected to Enterprise Architecture elements so that risk governance can trace potential impacts to objectives, capabilities, processes and controls?

### RQ3
To what extent can the proposed SemRisk profile represent and validate a real Jira-style Risk Register schema and a bounded Health/Pharma risk scenario using executable semantic artifacts?

## Candidate contribution statements

### C1 — Operational semantic disambiguation
A well-founded pattern for distinguishing the managed risk phenomenon from information artifacts and management activities used to describe, assess and track it.

### C2 — Architecture binding
A semantic linkage pattern connecting risk knowledge to enterprise objectives, capabilities, processes, controls and accountable actors.

### C3 — Executable demonstration
A mapping from a real operational Risk Register to SemRisk, evaluated using ontology validation, SHACL, competency questions and a bounded Health/Pharma case.

## CM-PharmE relationship

The paper should explicitly cite **CM-PharmE ver.1: Towards a Conceptual Model for Pharmaceutical Ecosystem with a Business-Architecture Perspective** as prior work providing the pharmaceutical ecosystem conceptual foundation.

The new contribution is not a replacement for CM-PharmE. SemRisk provides a reusable risk semantic layer that can be connected to CM-PharmE entities while preserving their ontological categories.

The case should preferably use a risk scenario that crosses enterprise architecture, pharmaceutical ecosystem structure and health consequences.

### Preferred case candidate

**Medicine availability disruption caused by pharmaceutical supply-capacity or supplier disruption**

Candidate chain:

```text
External / supplier condition
    -> disruption event
    -> reduced pharmaceutical supply capacity
    -> medicine shortage / availability impact
    -> healthcare delivery impact
    -> patient-related consequence
```

This case is attractive because it can connect:

- enterprise objective and capability impact;
- CM-PharmE ecosystem actors / supply relationships / processes;
- Health consequences;
- risk treatment and controls;
- inherent vs residual assessment;
- future Newsium external-signal integration without making Newsium part of Paper 1 implementation.

## Section plan and page discipline

| Section | Purpose | Indicative space |
|---|---|---:|
| I. Introduction | problem, gap, contributions | 0.7 page |
| II. Background / Related Work | COVER, ROSE, ISO/COSO, EA, risk-register/KG work | 0.8 page |
| III. Method | evidence, conceptualization, OGCM-RF-derived engineering | 0.6 page |
| IV. SemRisk Model | semantic distinctions + architecture links | 1.3 pages |
| V. Operational Mapping / Case | Jira mapping + Health/Pharma scenario | 1.0 page |
| VI. Evaluation | logic, SHACL, CQs, mapping coverage | 0.8 page |
| VII. Discussion / Conclusion | limitations, comprehensive SemRisk direction, Risk Intelligence future | 0.5 page |

The exact page budget must be rechecked against the conference template and references.

## Required visual artifacts

1. **Figure A — Semantic separation pattern**
   - risk phenomenon / scenario / record / assessment / result / treatment / workflow state.

2. **Figure B — Architecture-linked risk knowledge**
   - objective / capability / process / control / accountable actor.

3. **Table A — Closest-work comparison**
   - COVER/ROSE, ISO/COSO, Risk Register KG, health-specific ontology example, SemRisk.

4. **Table B — Jira mapping or evaluation summary**
   - chosen according to page pressure.

## Evaluation minimum

- RDF/Turtle syntax validity;
- logical consistency check;
- structural inventory;
- mapping coverage for the Jira schema;
- SHACL validation;
- executable competency questions;
- bounded application/query demonstration;
- reproducible release binding.

## Explicit limitations

Paper 1 does not claim:

- complete coverage of all risk domains;
- a complete Health ontology;
- completed Newsium/Commentium integration;
- real-time autonomous risk prediction;
- full validation of every future SemRisk module.

## Immediate dependencies

- Issue #1 — contribution freeze
- Issue #2 — Jira mapping
- Issue #3 — SemRisk Core inventory
- Issue #4 — Health evidence baseline
- Issue #5 — CM-PharmE bridge
- Issue #7 — competency questions / evaluation

## Manuscript freeze checks

Before submission:

- rerun closest-work search;
- verify novelty wording;
- cite the exact CM-PharmE publication and release used;
- bind manuscript to SemRisk ontology/evaluation artifact version;
- verify IEEE formatting and page limit;
- record the conference-required generative-AI disclosure as applicable.
