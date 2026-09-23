# W3A #28 Acceptance Audit — Bounded Pharma Case and Dataset Package

**Date:** 2026-09-23
**Result:** PASS_BOUNDED_QUALITATIVE_CASE

## Primary case decision
DS-003 v4 is the primary Paper-1 bounded Pharma case dataset. DS-004 is a structured extension explicitly deferred from evaluated/file-level denominator until exact PID/version/license/files/checksums/schema are frozen.

## Deliverables completed
- frozen case protocol and bounded population/context;
- exact DS-003 DOI/version/license/source binding;
- evidence-role and independence declaration before interpretation;
- #42 fitness limitations carried into the case contract;
- 18 governed source-field/code/content-element mapping rows;
- explicit coverage denominator and mapped/partial/unobserved states;
- unmapped/conflict register;
- source-grounded constructed case input;
- transformation specification;
- provenance-rich constructed Turtle case graph;
- 8 case-specific CQ expected-answer rows;
- handoff to #45–#49 and #30/#31.

## Coverage
- Governed source elements: 18/18 dispositioned.
- Direct/context mapped: 7/18 (38.9%).
- Partial/context-dependent: 10/18 (55.6%).
- Unobserved: 1/18 (5.6%; Ecological PESTELI theme).
- Hidden/unclassified: 0.

Coverage is an application mapping diagnostic, not ontology correctness.

## Acceptance verification
- DS-003 is not described as independent validation.
- No prevalence/population-frequency/general causal claim is made from the purposive n=16 sample.
- PESTELI codes remain method/profile vocabulary; they are not promoted to Core classes.
- Participant sector/actor context does not automatically create Risk Owner identity.
- Treatment Strategy vs Activity vs Control distinctions are preserved.
- CM-PharmE external ownership is preserved.
- API/INN/product terminology remains an explicit external-owner gap.
- Constructed values/instances are labeled illustrative and cannot support empirical prevalence/causality claims.
- DS-004 unresolved file state remains visible and does not inflate mapping denominator.

## Reproducibility boundary
The DS-003 case is reconstructable by versioned DOI v4 + frozen mapping/transformation/case package. Individual raw-file checksums were not exposed through the current connected access path, so raw-row/file-checksum completeness is not claimed. If raw files are later ingested, #47 must bind their filenames/checksums as a new execution input.

## Consequence
#28 is complete as a bounded qualitative Pharma application case. DS-004 file-level structured execution remains downstream debt and does not reopen #28 unless Paper-1 claims are expanded to depend on it.