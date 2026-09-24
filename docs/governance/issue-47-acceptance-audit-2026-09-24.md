# W3A #47 Acceptance Audit — Governed Data Load

**Date:** 2026-09-24  
**Result:** PASS_WITH_GOVERNED_SOURCE_LIMITS / CLOSED

## Acceptance result
- Source/version/evidence roles registered.
- Raw/source disposition and transformed projection are separated through staging.
- Source→transformation→target lineage is explicit for the bounded DS-003 case.
- Partial/blocked/protected inputs are retained rather than silently coerced or deleted.
- Deterministic synthetic fixture is explicitly non-empirical and seed/version governed.
- Data roles from #41/#42/#68 are preserved.
- CI clean-build/load/reconciliation is reproducible.
- No DS-004 file-level load occurred.
- No DS-002 record access occurred.
- No operational record rows were fabricated from SRC-OP-001.

## Verified execution
CI run `35988814931` on PostgreSQL 16:
- static catalog/mapping: PASS
- clean build: PASS
- integrity tests: PASS
- governed staging migration: PASS
- Paper-1 governed load: PASS
- reconciliation tests: PASS

Observed reconciliation counts:
- **8** governed staging records
- **13** constructed-case semantic instances
- **5** deterministic synthetic instances
- **0** rejected records

Marker: `SEM_RISK_ISSUE_47_LOAD_TESTS_PASS`

## Boundary
PASS establishes a reproducible Paper-1 data state sufficient to proceed to #48 end-to-end scenario execution. It does not remove DS-004 or DS-002 blockers and does not claim independent empirical validation.
