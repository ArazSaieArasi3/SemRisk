# SemRisk Literature and Landscape Review Protocol

**Protocol status:** frozen v0.1 for W0/W1 execution  
**Date:** 2026-08-29  
**Research:** R-022 / SemRisk

## 1. Review purpose

The repository review is deliberately broader than the literature section that will appear in the ICAEA conference paper. It must support:

1. exhaustive concept/relation extraction for the Paper-1 claim boundary;
2. defensible reuse/alignment decisions;
3. state-of-the-art comparison and competitive-advantage claims;
4. comparison of ontology engineering and evaluation methods;
5. Health/Pharma domain specialization;
6. a reusable evidence base for later journal work.

The conference manuscript will report only the method/result subset required by its eight-page claim boundary.

## 2. Review design

Use three coordinated components.

### A. Systematic mapping / scoping component

Purpose: establish the broad landscape of risk ontologies, semantic risk models, enterprise/GRC/EA risk models, Health risk semantics and Pharma risk models.

### B. Structured closest-work comparison

Purpose: deeply profile the closest ontologies/formal models, including concept/relation inventories, foundational commitments, formal artifacts, engineering method, evaluation, datasets, releases and reuse constraints.

### C. Focused Health / Pharma evidence review

Purpose: extract risk categories, causal structures, assessment/treatment methods, domain entities, datasets and evaluation cases needed for the Health profile and pharmaceutical case.

Do not label any component a systematic review unless the executed search, screening and reporting satisfies that claim. PRISMA-style flow reporting may be used only for components actually run under a systematic protocol.

## 3. Review questions

### RQ-L1 — Landscape
What risk ontologies, conceptual models, semantic models and knowledge-representation frameworks currently exist, and what scopes do they cover?

### RQ-L2 — Semantics
Which concepts, relations, events, states, information entities and distinctions recur across authoritative sources, and where do definitions conflict?

### RQ-L3 — Engineering
How were the closest risk ontologies/models designed, grounded, formalized, implemented, maintained and versioned?

### RQ-L4 — Evaluation
How were they evaluated with reasoning, CQs, constraints, experts, datasets, applications, comparisons, robustness and reproducibility evidence?

### RQ-L5 — Enterprise / EA
How is risk linked to objectives, capabilities, processes, controls, governance, accountability and enterprise architecture?

### RQ-L6 — Health / Pharma
What risk concepts, taxonomies, causal models, standards, datasets and assessment techniques are most relevant to Health and the pharmaceutical ecosystem?

### RQ-L7 — Gap / advantage
Which material capabilities needed by the SemRisk claim boundary are absent, partial, ambiguous or differently modeled in the closest work?

## 4. Search families

Maintain exact executable search strings per database/source. Core query families include:

1. `risk ontology` OR `risk management ontology` OR `semantic risk model` OR `risk knowledge representation`;
2. `foundational ontology risk` OR UFO risk ontology OR value risk ontology;
3. enterprise risk ontology / GRC ontology / enterprise architecture risk ontology;
4. risk register ontology / risk register semantics / risk knowledge graph;
5. healthcare risk ontology / clinical risk ontology / patient safety ontology / medical device risk ontology;
6. pharmaceutical risk ontology / pharmaceutical quality risk / pharmaceutical supply chain risk / medicine shortage risk / drug shortage risk;
7. pharmacovigilance ontology / adverse event ontology / safety signal ontology;
8. ontology engineering method + risk ontology;
9. ontology evaluation + risk ontology;
10. formal ontology / OntoUML / UFO + risk / security / value.

## 5. Source channels

Use multiple evidence channels to reduce database bias:

- academic discovery/index services available to the project;
- publisher/DOI landing pages;
- backward and forward citation chaining;
- official standards/framework sites;
- ontology repositories / GitHub / persistent IRI endpoints;
- qualified public data repositories;
- user-supplied papers and datasets;
- internal governed ontology repositories where they are integration targets.

## 6. Search log fields

For each search execution record:

- search ID;
- exact query;
- source/database;
- date/time;
- filters;
- result count;
- export/result locator;
- dedup method;
- screening stage;
- deviations from protocol.

## 7. Screening

### Include when material to one or more review questions

- ontology/conceptual/semantic models explicitly representing risk, threat, vulnerability, hazard, consequence, assessment, treatment, control, governance or domain risk;
- standards/frameworks with authoritative risk terminology or lifecycle semantics;
- peer-reviewed Health/Pharma risk models and reviews;
- formal artifacts or repositories required to assess actual ontology scope/method;
- datasets with adequate metadata that can support semantic discovery/mapping/evaluation.

### Exclude or downgrade

- purely financial/statistical prediction papers with no semantic/conceptual contribution to the current questions;
- vendor pages used as if they were academic novelty evidence;
- inaccessible claims with no verifiable metadata;
- duplicated/superseded versions where the distinction is not historically material;
- knowledge graphs whose contribution is only graph storage and that provide no relevant semantic model, except as application benchmarks.

Every exclusion at full-text/technical-artifact stage gets an explicit reason.

## 8. Quality / credibility appraisal

Evidence is ranked by source authority and directness, not only citation count.

- Tier A: standards, official ontology artifacts, high-quality peer-reviewed foundational/reference work, direct operational evidence;
- Tier B: peer-reviewed applied research, official frameworks, validated datasets;
- Tier C: preprints, technical reports, repositories used as supplementary technical evidence;
- Tier D: market/vendor/informal context.

For ontology artifacts also record:

- persistent IRI/version;
- formal source availability;
- license;
- maintenance status;
- consistency between paper claims and released artifact;
- reproducibility/evaluation evidence.

## 9. Extraction schema

Material sources are handed to `conceptualization/source-mining/` with exact provenance. Extract, where applicable:

- definitions and aliases;
- actors/roles;
- value/objective/asset constructs;
- source/cause/condition/trigger;
- event/scenario/consequence/harm/loss/gain;
- vulnerability/exposure;
- assessment/method/result/likelihood/impact/risk level;
- uncertainty/confidence/evidence;
- treatment/control/response/plan;
- appetite/tolerance/policy/compliance/audit;
- observation/KRI/threshold/monitoring;
- record/report/document semantics;
- temporal/state/lifecycle semantics;
- relations and cardinality/constraint candidates;
- domain-specific constructs;
- explicitly absent/rejected concepts;
- dataset and evaluation use;
- development/evaluation method.

## 10. Saturation / stopping criteria

For the conference claim boundary, closest-work search may stop when all conditions hold:

1. repeated forward/backward chaining yields no materially closer comparator;
2. each candidate contribution has at least one direct closest-work challenge examined;
3. all authoritative standards/frameworks used in the paper are version-verified;
4. Pharma case/model searches reach thematic saturation for the chosen case;
5. dataset search has at least one qualified primary candidate and documented rejected alternatives;
6. a fresh search immediately before manuscript freeze reveals no unaddressed material publication.

The broader repository review remains living and may continue after Paper 1.

## 11. Review-to-ontology handoff

```text
Review source
   -> source register
   -> source-specific coverage
   -> raw semantic extraction
   -> disposition
   -> cross-source reconciliation
   -> canonical registry
   -> foundational/formal mapping
   -> CQ/evaluation trace
```

Review conclusions never directly overwrite canonical ontology entities.

## 12. Conference reporting policy

Paper 1 may report a compressed description such as a structured/scoping review and closest-work analysis only if that accurately reflects execution. Full search logs, extended comparison tables and extracted concepts stay in the repository and are referenced as reproducibility evidence where allowed.

## 13. Required refresh

A final closest-work and standards-version search is mandatory at Gate G5 immediately before manuscript freeze/submission.
