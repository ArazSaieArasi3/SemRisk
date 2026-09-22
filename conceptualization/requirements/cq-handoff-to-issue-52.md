# #7 → #52 Conceptual CQ Handoff Contract

**Frozen:** 2026-09-22

## Authority
`conceptualization/requirements/conceptual-cq-registry.csv` is the authoritative semantic-intent baseline for #52.

## Rules for #52
1. Preserve CQ ID, natural-language intent and expected capability/answer.
2. Allowed runtime states are those owned by #52: `conceptual_only`, `executable`, `partially_executable`, `deferred`, `not_applicable`, `failed`.
3. A query executing successfully is not by itself semantic PASS.
4. A failing CQ creates a finding; it is not deleted or rewritten after result inspection without a governed #7/#24 requirement decision.
5. Negative/edge CQs remain in the applicable denominator when claim-relevant.
6. Every executable test must bind exact ontology/mapping/data release identifiers.
7. Where ontology and relational projections both apply, #52 cross-references #49 parity evidence.
8. Expected answers are frozen before executable query authoring.

## Required trace chain
`Requirement → CQ → Concept/Relation/Event/State → Formal/Mapping Artifact → Query/Test → Result → Claim`.

## Change control
A semantic change that materially alters a CQ's intended answer requires a dated requirements decision and downstream regression impact analysis. Wording-only clarification may preserve the same CQ ID if semantic intent is unchanged.

## Non-equivalence
Conceptual CQ adequacy, query answerability, query executability and semantic/domain validation are separate evaluation dimensions.