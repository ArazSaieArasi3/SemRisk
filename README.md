# SemRisk

**SemRisk** is a research-first programme for developing a **comprehensive, modular and domain-extensible risk ontology** with a well-founded reusable Core and explicit application/domain profiles.

Read the [domain definitions, domain-to-concept tables, concept definitions and diagrams](docs/ontology/domain-concept-reader-catalog.md). The catalog distinguishes planned profiles from implemented ontology declarations and links to the available SVG diagrams and WebVOWL candidate.

## Research identity and canonical ownership

- Portfolio Research ID: **R-022**.
- Primary programme/line: **P1 / P1-L6 — Cross-Domain Foundational Semantics**.
- `araz-research-portfolio` owns Research identity, lifecycle, priority and cross-repository governance.
- `OGCM-RF` owns the reusable ontology-engineering, repository-federation, validation and release method adopted by this repository.
- **SemRisk** owns risk-domain evidence, governed semantic decisions, canonical SemRisk concept/relation/module registries, SemRisk ontology artifacts, mappings, data projections, evaluation evidence and SemRisk releases.
- External ontologies remain canonical at their owning repositories; SemRisk consumes them only through explicit imports, references, mappings or federation contracts.

The machine-readable external semantic ownership/dependency contract is [`semantic-dependencies.yaml`](semantic-dependencies.yaml). Presence of Portfolio/OGCM-RF contracts does **not** by itself establish scientific validity or formal OGCM-RF conformance; `conformance_level` remains `not_assessed` until an explicit conformance assessment is executed.

## Semantic source of truth

During W0/W1, literature, standards, ontology baselines, operational schemas and datasets are **evidence**, not canonical SemRisk semantics. Canonical semantic authority will move only to governed SemRisk concept/relation/module registries and their formal ontology source after the applicable G1/G2 gates pass. Generated diagrams, relational schemas, catalogs, dashboards and publication figures remain projections/consumers and cannot silently become semantic source of truth.

## Current research intent

SemRisk aims to provide:

- a domain-general **Risk Core** grounded in UFO/gUFO and aligned/reused against COVER and other justified reference ontologies rather than redefining foundational semantics without evidence;
- deep, source-complete concept and relation extraction from literature, standards, frameworks, ontologies, operational schemas and public datasets;
- exact provenance from raw source term/field/statement to normalized candidate, canonical semantic entity, relation, profile, formal axiom, competency question and evaluation evidence;
- explicit separation of risk phenomena, events, scenarios, records, assessments, assessment results, controls, treatments, observations, evidence, responsibility and workflow states;
- standards/framework mappings to ISO 31000/31073, IEC 31010, COSO ERM, OCEG GRC, Open FAIR and domain standards;
- reusable profiles, with **Enterprise** and **Architecture** as the first application emphasis, **Health** as the highest-priority broad domain, and **Pharma** as the first bounded specialization/case connected to CM-PharmE;
- later semantic bridges to Newsium and Commentium and an eventual Risk Intelligence Platform.

## Publication strategy

### Paper 1 — conference-first

The first paper is a bounded conference contribution. The exact venue, deadline, page limit, template and publication contract are deliberately treated as **unverified until Issue #38 is completed**; stale venue assumptions must not control the research design.

The **title is deliberately not frozen**. Paper 1 focuses on a bounded, evaluated SemRisk Core plus Enterprise/Architecture application and a pharmaceutical-ecosystem case/data evaluation. The operational Risk Register/Excel is a major source and evaluation artifact, but **not the identity of the paper or ontology**.

Knowledge-graph construction, dynamic Risk Intelligence and Newsium/Commentium runtime integration are deferred from the Paper 1 contribution.

### Paper 2 — comprehensive extension

A later paper will expand SemRisk toward broader Core/profile coverage, temporal/evidence-aware assessment, stronger transferability evaluation and Risk Intelligence/product validation.

## Priority profile names

Domain/profile names intentionally avoid `and` / `&`.

- `Core`
- `Enterprise`
- `Architecture`
- `Health`
- `Pharma`
- `Governance`
- `Security`
- `Finance`
- `SupplyChain`
- `News`
- `AI`
- `Environment`

These are semantic research profiles, not predefined DDD bounded contexts, services, tables or APIs.

## Research method gate

SemRisk adopts **OGCM-RF Exhaustive Source Mining** as a hard pre-formalization rule:

1. register material sources;
2. mine each source before normalization;
3. preserve exact locators and evidence strength;
4. maintain source coverage registers;
5. disposition every material extracted item;
6. reconcile only after individual-source completeness;
7. regress earlier modeling decisions;
8. freeze the canonical Core / CQs / modules / foundational commitments only after the applicable Source Completeness Gate.

Formal OWL/SHACL implementation must not outrun evidence and conceptual reconciliation.

## Current execution state

The canonical execution order is governed by **Issue #8** rather than GitHub issue number order.

- W0 contract refresh is current.
- Immediate sequence: **#38 venue contract → #39 study design/evidence roles → #1 RQs/contributions/nonclaims**.
- W1 then resumes with reproducible search and source mining.
- The next scientific hard gate is **G1 — Source Completeness and Cross-Source Reconciliation (#18)**.
- Canonical Core/module/foundational/formal commitments remain blocked until the applicable evidence boundary passes.

## Start here

- [Novelty and Alignment Matrix](docs/research/novelty-and-alignment-matrix.md)
- [Domain Profile Roadmap](docs/research/domain-profile-roadmap.md)
- [Portfolio Manifest](.research/manifest.yaml)
- [OGCM-RF Implementation Profile](.research/ogcm-rf-profile.yaml)
- [Semantic Dependencies](semantic-dependencies.yaml)
- [Canonical Backlog / Critical Path — Issue #8](https://github.com/ArazSaieArasi3/SemRisk/issues/8)

## Governing research infrastructure

SemRisk is Portfolio Research **R-022**, classified under **P1 / P1-L6 — Cross-Domain Foundational Semantics**, with P2/P3/P5 bridges. Generic Research identity and publication/product/artifact governance belong to `araz-research-portfolio`; reusable ontology/conceptual-model engineering, source-complete semantic mining, formalization, traceability, evaluation and release discipline follow OGCM-RF.

SemRisk maintains explicit cross-Research reuse/bridge traceability to assets such as **CM-PharmE**, with Newsium and Commentium integration reserved for the later Risk Intelligence workstream.
