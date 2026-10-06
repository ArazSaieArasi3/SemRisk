> **Current formal candidate reference:** [0.2.0-rc.4 FD-A–FD-J](docs/formal/formal-ontology-description-rc4.md), [complete asserted source projection](docs/formal/0.2.0-rc.4/generated-reference.md) and [migration boundaries](docs/formal/migration-to-rc4.md). These are candidate documentation, not a scholarly release or complete SQL-parity claim. [Run 10](docs/execution/2026-10-04/run-10-report.md) records checks and remaining gates.

> **Current Paper-1 revision — Run 9:** The [pharmaceutical literature pilot](case/pharma/literature-pilot-v0.1.0/README.md) contains 24 traceable source-local statements from six primary studies. See [Run 9 report](docs/execution/2026-10-04/run-9-report.md) and [current status](docs/execution/2026-10-04/status.md) for verification, limits and next work. This is applicability evidence, not independent or field validation.

> **Current Paper-1 revision — Run 8:** [0.2.0-rc.4](ontology/releases/0.2.0-rc.4/README.md) adds explicit Exposure endpoints and scale-specification identity. The [complete editable diagram](diagrams/ontouml/0.2.0-rc.4/README.md) covers all 47 concepts and 40 registered relation decisions. See [status](docs/execution/2026-10-04/status.md) and [Run 8 report](docs/execution/2026-10-04/run-8-report.md). Formal/native CI, case extraction and final article gates remain separately tracked.

> **Author revision — Run 16 (2026-10-06):** rc.4 offline formal reference and Wiki-draft parity. [Current status](docs/execution/2026-10-04/status.md) · [candidate documentation](docs/documentation/rc4/README.md). Accepted requirements remain 34/90; whole packages 3/19. Live deployment, full conformance, manuscript and release gates remain open.

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

Literature, standards, ontology baselines, operational schemas and datasets are **design evidence**. The existing candidate is governed by SemRisk concept/relation/module registries and their formal ontology sources, with historical G1/G2 decisions retained. New semantic revisions must reopen the affected evidence and conceptual checks. Generated diagrams, relational schemas, catalogs, dashboards and publication figures remain projections/consumers and cannot silently become semantic source of truth.

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

The first paper presents a bounded core for enterprise risk knowledge and a pharmaceutical application. The intended venue is the **10th Iranian Conference on Advances in Enterprise Architecture, Shahid Beheshti University**. The [corrected venue contract](publications/2026-icaea-sbu/venue-contract.md) supersedes the unrelated ICAE Applied Engineering assumptions. Target: **7 readable IEEE pages; absolute author cap 8**. Official deadline/extension and remaining submission conditions are not yet cleared.

Working title: **SemRisk: An Extensible Core Ontology for Enterprise Risk Knowledge**. It remains provisional until evaluation. Design-source influence, operational projection and independent validation are separately reported. The core does not claim comprehensive enterprise-risk coverage.

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

As of **2026-10-04**, the existing P1-R2 / 0.1.0-rc.1 semantic candidate, relational application evidence and v0.4 author-review manuscript are the revision baseline. They are not a final publication-bound release. Historical W0/W1 status statements no longer describe current implementation.

The active [90-requirement / 19-package revision register](docs/execution/2026-10-04/README.md) is governed by [Issue #8](https://github.com/ArazSaieArasi3/SemRisk/issues/8). Start with its [current status](docs/execution/2026-10-04/status.md), acceptance criteria and exact artifact references. Planning coverage and closed issue counts do not measure scientific readiness.

Next: bounded prior-art/standards deltas and early dataset/expert protocols, then semantic and OntoUML revision, evaluation, and the seven-page manuscript. Real expert responses, final release rights and submission conditions remain explicit gates.

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
