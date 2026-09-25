# Pharma case transformation specification v1.1

## Purpose
Transform a governed, source-locatable **case abstraction** into SemRisk instance data without pretending that the abstraction is a raw DS-003 row export.

## Inputs
1. DS-003 exact identity: DOI 10.25375/uct.29178665.v4 / v4 / CC BY 4.0.
2. `pharma-case-field-mapping-v1.1.csv`.
3. `constructed-case-input-v1.1.csv`, containing study-level thematic summaries, never copied participant quotes.
4. CM-PharmE v1.1.0 bridge registry.

## Transformation rules
1. Create one bounded `Risk` context for antibiotic-shortage management.
2. Create `PredisposingCondition` individuals only for source-supported thematic conditions; retain source locator and mark them `CONSTRUCTED_FROM_SOURCE_SUMMARY`.
3. Do not create a `RiskEvent` from a generic theme unless the evidence denotes an occurrence; the current package therefore uses a scenario/context representation and does not fabricate dated shortage events.
4. Type proposed responses from their source context. Pooled procurement is retained as a proposed `RiskTreatmentStrategy` because the source frames it as a possible mitigation strategy. Supply-chain transparency remains a Pharma response candidate requiring contextual typing because the source frames it as a management need; do not auto-promote it to Strategy/Activity/Control.
5. Preserve CM-PharmE entities as external targets referenced through `SR-REL-037 pharmaEntityInRiskContext`; never recast them as SemRisk-owned classes.
6. Evidence objects identify the source dataset/study locator and provenance role. They do not encode participant identity beyond released pseudonymous context.
7. API/INN/product identity remains unmapped/external until a governed terminology owner is selected.
8. No prevalence, frequency, causal-strength or generalizability property is generated.
9. Every generated instance must carry the case package version and source dataset ID.

## Output
- `constructed-pharma-case-v1.1.ttl` for semantic/RDB projection tests.
- The output is **constructed/illustrative application data**, not an empirical row-level reproduction of DS-003.

## Reproducibility boundary
The transformation is reproducible from the versioned DOI, frozen mapping registry and constructed input table. Exact raw-file reconstruction is not claimed because the connected access path did not expose individual DS-003 file checksums.
