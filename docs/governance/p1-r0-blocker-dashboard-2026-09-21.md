# SemRisk P1-R0 Blocker Dashboard — 2026-09-21

**Release:** P1-R0 — Evidence Baseline  
**Exit gate:** #18 G1  
**Current judgment:** IN PROGRESS / G1 NOT READY

| Blocker family | Current state | Consequence / next action |
|---|---|---|
| COVER exact identity/license | **RESOLVED** | Immutable commit/path/blob + Apache-2.0 pinned; formal anomaly deferred to #21/#29 |
| ROSE exact identity/license/erratum | **RESOLVED** | Corrected commit + MIT + PURL pinned |
| IOF Biopharma identity/version | **RESOLVED** | Suite 202603 / module versionIRI 202602 bound; reuse still conditional because Provisional |
| CM-PharmE semantic baseline | **RESOLVED** | Frozen v1.0.0 selected; license governance remains external |
| PH-007 full-text access | **BOUNDED** | Narrow prior-art claims allowed; detailed class/axiom claims prohibited |
| #16 dataset universe | **CLOSED / DONE** | shortlist, lineage, accepted/conditional/supplementary/future-only states governed |
| #41 evidence roles | **CLOSED / PASS** | DS-002 amendment governed; no circular validation labeling |
| #42 W1 dataset fitness | **CLOSED / PASS** | every dataset has allowed/prohibited use; blocked datasets remain blocked |
| DS-004 exact file artifact | **OPEN / high** | authoritative primary-data locator + study grains known; exact license/files/checksums/columns needed before evaluated mapping |
| DS-002 holdout | **OPEN / optional future** | schema-level independence revoked; record-level E11 holdout requires exact release + protocol freeze before record access |
| #17 schema coverage | **OPEN / bounded tail** | exact DS-004 file schema and DS-001 supplement file details unresolved |
| Pharma supply/QRM search | **PARTIAL_NEAR_SATURATION** | final stopping refresh and residual artifact cleanup |
| Risk Register/GRC search | **PARTIAL_MATERIAL_BASELINE** | final stopping/artifact checks remain |
| #40 search stopping | **CLOSED / PASS** | final stopping decision frozen; residual debt routed to owner issues |
| residual #12/#13/#14/#15 evidence debt | **OPEN** | resolve claim-critical locators/comparators or explicitly bound them |
| #18 cross-source reconciliation | **CLOSED / CONDITIONAL_PASS** | 274/274 raw rows dispositioned; 191 candidates consolidated; W2 authorized under gate conditions |

## Critical path now

1. Finish/formally bound claim-critical #12/#13/#14/#15/#17 residual debt.
2. Finish or formally bound claim-critical #12/#13/#14/#15 and #17 residual evidence debt.
3. Execute #18 cross-source reconciliation and issue `PASS | CONDITIONAL_PASS | FAIL`.

## No longer P1-R0 blockers

- generic dataset discovery;
- dataset role ambiguity;
- W1 dataset fitness decisions;
- COVER/ROSE/IOF identity;
- CM-PharmE semantic baseline;
- generic Pharma-ontology novelty discovery.