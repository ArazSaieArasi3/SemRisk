# SemRisk #47 Governed Data Load — Quality Report

**Date:** 2026-09-24  
**Snapshot:** `P1-DATA-0.1.0-rc.1`  
**CI run:** `35988814931`  
**Validated commit:** `da6ac1ea7a1597cd1fdd098167b5316af5449f64`  
**Result:** PASS

## Loaded and governed state
- governed staging/source records: **8**
- constructed-case semantic instances: **13**
- deterministic synthetic semantic instances: **5**
- rejected records: **0**
- explicit blocked sources retained: **DS-004**
- explicit protected holdout retained: **DS-002**
- SRC-OP-001: schema/mapping context only; no empirical operational record corpus fabricated.

## DS-003 bounded case
Five governed constructed input summaries (PCI-001..PCI-005) were reconciled into the relational projection with source locators and transformation rules. No raw participant quote, prevalence estimate, dated event, treatment effectiveness or numeric risk score was invented.

The relational load contains:
- bounded Risk context;
- two Predisposing Conditions;
- Risk Scenario;
- two proposed Treatment Strategies;
- Evidence Item;
- constructed Assessment Activity + qualitative Assessment Result;
- contextual constructed Risk State;
- exact CM-PharmE v1.0.0 external references/bridges.

## Synthetic operational fixture
Seed: `4701`  
Generator identity: `SYNTH-P1-0.1.0-seed-4701`

The fixture contains:
- Risk;
- Risk Register;
- Risk Register Entry;
- Workflow State;
- Risk Responsibility;
- derived Risk Owner.

All synthetic instances carry `synthetic_flag=true` and evidence role `synthetic_test`; CI asserts that none can be labeled independent validation.

## Reconciliation
GitHub Actions PostgreSQL CI passed:
- clean schema build;
- #46 integrity tests;
- staging/load support;
- governed Paper-1 data load;
- #47 reconciliation tests;
- catalog snapshot.

Result marker:
`SEM_RISK_ISSUE_47_LOAD_TESTS_PASS`

## Limitations preserved
- DS-004 remains file-level blocked until exact version/license/files/checksums/columns are frozen.
- DS-002 remains protected; no record-level inspection/load occurred.
- DS-001 remains supplementary and is not used as primary evidence.
- SRC-OP-001 provides operational schema semantics but no empirical row corpus.

These limitations are not treated as failed rows and remain visible in staging governance.
