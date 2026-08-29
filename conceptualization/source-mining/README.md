# SemRisk Exhaustive Source Mining Protocol

This directory implements the OGCM-RF review-to-ontology handoff for SemRisk. Its purpose is to prevent premature canonicalization and preserve exact evidence provenance from heterogeneous sources.

## Governing rule

**Source evidence is not ontology truth.** Every material source is mined independently before cross-source reconciliation. A raw term, spreadsheet field, dataset column, standard definition or external ontology class is never promoted directly to the canonical SemRisk Core.

## Trace chain

```text
Source
  -> exact locator
  -> raw term / field / statement / relation
  -> normalized candidate
  -> semantic disposition
  -> reconciled candidate
  -> canonical concept / relation / event / state
  -> foundational category
  -> module / profile
  -> formal artifact / axiom / SHACL rule
  -> mapping
  -> competency question
  -> evaluation result
  -> manuscript claim / table / figure
```

## Source families

- `OP` — operational spreadsheets, registers and enterprise artifacts;
- `PA` — peer-reviewed papers and conceptual models;
- `ST` — standards, official vocabularies and authoritative frameworks;
- `ON` — existing ontologies, semantic models and formal artifacts;
- `DS` — qualified datasets and data dictionaries;
- `PH` — pharmaceutical-risk literature and evidence;
- `HE` — broader Health risk literature and evidence;
- `IN` — internal governed ontology assets such as CM-PharmE.

## Pass A — source-complete extraction

Minimum fields:

- `source_concept_id`
- `raw_term`
- `raw_definition_or_context`
- `source_id`
- `source_locator`
- `source_type`
- `evidence_strength`
- `extraction_dimension`
- `fact_status`

Exact locators should use the strongest available addressing scheme:

- spreadsheet: workbook/sheet/cell or row/column;
- paper/PDF: page + section/table/figure where available;
- standard: edition/version + clause/section/page;
- ontology: exact version + IRI + module/file;
- dataset: DOI/PID + version + table/field/code/data-dictionary locator;
- repository: repository + commit/tag + path/line or semantic IRI.

## Pass B — semantic disposition

Minimum fields:

- `normalized_candidate`
- `candidate_scope`
- `disposition`
- `existing_target_id`
- `ontology_category_candidate`
- `ontology_product_data_relevance`
- `domain_relevance`
- `synonym_conflict_note`
- `follow_up_status`

Allowed dispositions include:

- `CANDIDATE`
- `PROFILE_OR_MAPPING`
- `METHOD_PROFILE`
- `DATA_ONLY`
- `DATA_OR_PRODUCT`
- `SYNONYM`
- `REFINEMENT`
- `CONFLICT`
- `ADJACENT`
- `ANTI_CONCEPT`
- `REJECTED`
- `BLOCKED`

## Evidence strength

Evidence strength and evidence type are separate dimensions. Suggested quality tiers:

- **A** — authoritative standard/official semantic artifact/direct operational artifact/high-quality peer-reviewed foundational work;
- **B** — peer-reviewed applied research/reputable framework or validated public dataset;
- **C** — preprint/technical report/repository evidence useful for discovery or implementation;
- **D** — vendor/informal material used only for product/market context.

`fact_status` must distinguish at least:

- `SOURCE_FACT`
- `INTERPRETATION`
- `DESIGN_PROPOSAL`
- `INFERENCE`

## Coverage requirement

Every material source requires a coverage artifact showing what parts were inspected. For Paper 1, Gate G1 passes only when all sources material to the actual claim boundary have either:

1. complete extraction and disposition;
2. an explicit scoped exclusion; or
3. an unresolved blocker that weakens/blocks the affected claim.

## Reconciliation

Reconciliation occurs only after independent source mining and must explicitly examine:

- synonymy;
- homonymy/polysemy;
- competing definitions;
- class vs role vs relator vs mode vs event vs situation vs information entity;
- Core vs profile-specific meaning;
- method-specific versus domain-independent semantics;
- data/product artifacts that are not ontology entities;
- conflicting standards/reference ontologies;
- concept and relation deltas unique to each source family.

## Current first material source

`SRC-OP-001` — `jira risk attributes.xlsx`, mined with SHA-bound provenance and 27/27 row coverage.

## Gate relationship

- W1 produces source-specific evidence only.
- G1 / Issue #18 reconciles sources and evaluates Source Completeness.
- W2 then produces canonical UL, concept and relation registries.
- W3 may formalize only the reconciled and governed subset.
