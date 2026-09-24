# SemRisk Paper-1 Data Snapshot Manifest

**Snapshot ID:** `P1-DATA-0.1.0-rc.1`  
**Load pipeline:** `relational/sql/load/P1_DATA_0_1_0_rc1.sql`  
**Staging migration:** `relational/sql/V002__data_load_support.sql`  
**Load tests:** `relational/sql/tests/V002__data_load_tests.sql`  
**Transformation policy:** `relational/load/data-load-spec-v0.1.md`  
**Repository commit validated by CI:** `da6ac1ea7a1597cd1fdd098167b5316af5449f64`  
**GitHub Actions run:** `35988814931`

## Input bindings
- SRC-OP-001: SHA-256 `6f40bb5dd670e884df205093b8048d62807f5371e502997279f03073b09e5c8f`; schema/mapping context only.
- DS-003: DOI `10.25375/uct.29178665.v4`, version v4, CC BY 4.0; bounded constructed case.
- Constructed input repository blob: `case/pharma/constructed-case-input-v1.0.csv` blob `ef8ec9a9d79e9aed8f58249d89576380e550b607`.
- DS-004: authoritative share locator only; blocked from evaluated load.
- DS-002: DOI `10.7910/DVN/G9SHDA`; protected holdout; records not opened.
- Synthetic fixture: generator `SYNTH-P1-0.1.0`, seed `4701`.

## Snapshot counts verified in PostgreSQL 16 CI
- governed source/staging records: 8
- constructed semantic instances: 13
- synthetic semantic instances: 5
- rejected records: 0

Reconstruction is repository-controlled: reset → V001 schema → V001 views/reference data → V002 staging → governed load → V002 reconciliation tests.
