# SemRisk

**SemRisk** is a research-first programme for developing a **comprehensive, modular and domain-extensible risk ontology** with a well-founded reusable Core and explicit application/domain profiles.

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

### Paper 1 — ICAEA 2026 conference-first

The first target is an IEEE-format ICAEA 2026 paper. The **title is deliberately not frozen**.

Paper 1 focuses on a bounded, evaluated SemRisk Core plus Enterprise/Architecture application and a pharmaceutical-ecosystem case/data evaluation. The operational Risk Register/Excel is a major source and validation artifact, but **not the identity of the paper or ontology**.

The planning envelope is **up to 8 content pages**, subject to final verification against the actual conference/template rule.

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

**W0 — Governance, evidence architecture and conference control**

The next gate is **Source Completeness and Conference Contribution Gate**. The immediate execution sequence is:

- evidence/source registry and review protocol;
- operational spreadsheet mining;
- standards/framework mining;
- closest-ontology/model mining;
- Pharma/Health literature and dataset mining;
- reconciliation and competitive-gap audit;
- SemRisk Core v0.1 conceptualization;
- foundational analysis and formalization;
- claim-dependent multilayer evaluation;
- manuscript/release binding.

## Start here

- [Novelty and Alignment Matrix](docs/research/novelty-and-alignment-matrix.md)
- [Domain Profile Roadmap](docs/research/domain-profile-roadmap.md)
- [ICAEA 2026 Paper Plan](publications/2026-icaea/README.md)
- [Portfolio Manifest](.research/manifest.yaml)
- [OGCM-RF Implementation Profile](.research/ogcm-rf-profile.yaml)

## Governing research infrastructure

SemRisk is Portfolio Research **R-022**, classified under **P1 / P1-L6 — Cross-Domain Foundational Semantics**, with P2/P3/P5 bridges. Generic Research identity and publication/product/artifact governance belong to `araz-research-portfolio`; ontology/conceptual-model engineering, source-complete semantic mining, formalization, traceability, evaluation and release discipline follow OGCM-RF.

SemRisk maintains explicit cross-Research reuse/bridge traceability to assets such as **CM-PharmE**, with Newsium and Commentium integration reserved for the later Risk Intelligence workstream.
