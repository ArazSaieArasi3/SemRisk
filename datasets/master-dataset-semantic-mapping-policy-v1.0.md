# Master Dataset–SemRisk Mapping Policy v1.0

Issue: #68

## Purpose
This package is the cross-dataset semantic index for SemRisk Paper 1. It does not replace source-specific mappings, ontology registries, dataset registries, or relational mappings.

## Canonical rule
Datasets do not become semantically equivalent to each other by sharing labels or columns. Each source element is first mapped, partially mapped, externally owned, blocked, protected, or left unmapped relative to governed SemRisk semantic IDs. Cross-dataset comparison is then performed through those semantic IDs plus mapping status and provenance.

## Status semantics
- DIRECT — source element supports a governed SemRisk semantic construct with sufficiently specific semantics for the declared use.
- CONTEXT — source element supplies record/evidence/provenance context but is not identity-equivalent to the target concept.
- PARTIAL — overlap exists but context, role, subtype, method or interpretation is required.
- PROFILE_MAPPING — source taxonomy/workflow/product semantics remain profile/source mappings rather than Core ontology classes.
- EXTERNAL_OWNER — semantics belong to an external vocabulary/domain owner; SemRisk links rather than recreates.
- UNMAPPED — no defensible current target.
- UNOBSERVED — a source framework/category exists but no observation/instance is supported.
- BLOCKED_FILE_SCHEMA — study/package semantics are known but exact file-level columns/version/checksums/license are not frozen.
- PROTECTED_HOLDOUT — mapping/record inspection is intentionally restricted to preserve a predeclared evaluation role.
- PLANNED_SYNTHETIC — future deterministic test data only.

## Evidence-role safeguards
Mapping coverage is not ontology correctness. SRC-OP-001 and DS-003 already influenced design and are not independent semantic validation. DS-004 linked-study semantics influenced design and file-level use remains blocked. DS-002 is protected only as a possible record-level transferability holdout. Synthetic data can support regression/negative controls/application execution, never empirical prevalence or causal claims.

## Downstream contract
#47 must read load readiness from the master summary/blocker registry before ingesting any source.
#49 must bind paired SQL/SPARQL tasks to stable SemRisk IDs and preserve OWA/CWA, null, external-owner and projection-loss caveats.
Any new dataset, exact file version, field mapping, mapping-status change or evidence-role change must update this package and preserve prior provenance.
