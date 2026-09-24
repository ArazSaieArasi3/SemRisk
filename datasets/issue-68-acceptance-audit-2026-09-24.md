# W3A #68 Acceptance Audit — Master Dataset–SemRisk Mapping Matrix

**Date:** 2026-09-24
**Result:** PASS_WITH_GOVERNED_BLOCKERS

## Completed
- Master cross-dataset semantic mapping matrix: **58 rows**.
- Governed source coverage:
  - SRC-OP-001: **27/27** operational attributes represented.
  - DS-003: **18/18** governed elements represented.
  - DS-004: **9 study-documented family-level mappings**; exact file-column claims intentionally prohibited.
  - DS-002: **2 protected family-level dispositions**; no record inspection.
  - DS-001: supplementary artifact disposition.
  - SYNTH-P1-TBD: planned deterministic regression mapping family.
- Dataset-level readiness summary.
- Explicit mapping-status vocabulary and cross-dataset semantic-hub policy.
- Six-item blocker/limitation register with owners and downstream consequences.
- DS-003 coverage inconsistency corrected to **7 direct/context + 10 partial + 1 unobserved = 18/18 dispositions**.

## Acceptance checks
- Every governed Paper-1 dataset/source family has a master disposition.
- Every mapped row carries source identity/locator, target semantic ID(s) where defensible, mapping status/relation, confidence, evidence role, execution readiness and source-specific artifact reference.
- Source-native semantics remain recoverable; the master matrix is an index, not a replacement truth source.
- Dataset-to-dataset comparison is mediated by SemRisk semantic IDs plus mapping status/provenance, never lexical equivalence.
- DS-004 exact fields are not invented; file-level evaluated use remains blocked.
- DS-002 record-level holdout protection is preserved.
- SRC-OP-001 workflow/record semantics are kept distinct from Core risk semantics.
- Unobserved/blocked/protected items remain explicit.
- #41/#42 evidence-role restrictions are preserved.
- #47 load readiness and #49 parity prerequisites are explicit.

## Governed blockers
- DS-004 exact file/version/license/checksum/schema: HIGH, blocks evaluated structured load/parity.
- DS-002 exact release + predeclared E11 protocol: HIGH, protected holdout.
- DS-001 primary identity/schema/license: MEDIUM, supplementary only.
- Synthetic generator/seed/version/checksum: MEDIUM, planned.
- SRC-OP-001 lacks empirical record corpus: bounded limitation, not a schema-design blocker.
- DS-003 raw-file checksum enumeration: LOW/nonblocking for the bounded constructed case.

## Artifacts
- `datasets/master-dataset-semantic-mapping-v1.0.csv`
- `datasets/master-dataset-semantic-mapping-summary-v1.0.csv`
- `datasets/master-dataset-semantic-mapping-blockers-v1.0.csv`
- `datasets/master-dataset-semantic-mapping-policy-v1.0.md`
- corrected `case/pharma/pharma-case-mapping-coverage-v1.0.csv`

## Consequence
#68 is complete as a governance/mapping-index task. It does not assert that blocked datasets are now executable. #46/#47 may use the matrix to implement the relational twin and select permitted load inputs; #49 must retain the declared blocked/protected states and mapping-loss caveats.
