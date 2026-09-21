# DS-004 Qualification — Cross-National Antibiotic Shortage Primary Data

**Dataset ID:** DS-004
**Linked publication:** Chirac et al. (2026), *Structural Patterns of Antibiotic Shortages: A Cross-National Analysis of Systemic Antibacterials*, Antibiotics 15(6):571, DOI `10.3390/antibiotics15060571`.
**Qualification date:** 2026-09-21
**Status:** `PRIMARY_DATA_CONFIRMED / AUTHORITATIVE_SHARE_LOCATOR_BOUND / FILE_MANIFEST_AND_DATASET_LICENSE_UNRESOLVED`.

## 1. Identity and authoritative linkage

The peer-reviewed article's Data Availability Statement explicitly identifies `https://figshare.com/s/a0bca1308da751f465b6` as the **primary data used within the paper**. This establishes primary-artifact lineage even though the share artifact does not expose a dataset DOI/version through the currently accessible metadata channels.

Article identity:
- published 2026-06-03;
- DOI `10.3390/antibiotics15060571`;
- study data derived from official shortage registers in Belgium, France, Germany, Romania, Spain, the United States/FDA and Saudi Arabia.

## 2. Study-level data structure that is safe to assert

The article documents two distinct grains:

### Raw/harmonization grain
- 350 product-level shortage records collected across seven jurisdictions;
- records selected for systemic antibacterials in ATC J01;
- source records required harmonization of active-substance names, route-of-administration descriptions and ATC classification levels.

### Analytical master-dataset grain
- 64 unique active substances / INNs;
- one analytical record per INN reported in at least one jurisdiction;
- country/jurisdiction shortage occurrence per INN;
- ATC level-3 therapeutic subclass;
- number of jurisdictions reporting shortage;
- derived multinational-recurrence indicator(s), including the main >=3-jurisdiction threshold and sensitivity thresholds;
- EMA critical-medicine status;
- route-of-administration grouping including injectable vs other.

These are **study-documented analytical variables**, not asserted as exact Figshare file column names.

## 3. Quality information available before file inspection

Strengths:
- primary-data lineage explicitly confirmed by peer-reviewed publication;
- underlying sources are official national shortage registers;
- explicit harmonization process and INN-based analytical unit;
- raw count (350) and analytical-unit count (64) are reported;
- seven-jurisdiction coverage is explicit;
- sensitivity analysis around jurisdiction thresholds is reported.

Known limitations:
- national registers differ in reporting rules and temporal fields;
- onset/resolution dates are missing or heterogeneous across jurisdictions;
- duration/time-evolution analyses were therefore not feasible;
- cross-jurisdiction selection/reporting heterogeneity limits representativeness;
- manual cleaning/harmonization introduces transformation decisions that must be inspectable before SemRisk quantitative use.

## 4. What remains unresolved

- exact Figshare article/item ID behind the share token;
- dataset DOI/PID, if one exists;
- dataset-specific version/revision;
- dataset-specific license (article/preprint CC BY does **not** automatically establish the share-data license);
- exact file names, file count, sizes and checksums;
- exact column names/datatypes;
- file-level missingness, duplicate counts and invalid-value metrics;
- transformation script/workbook provenance.

## 5. SemRisk fitness decision

**Current decision:** `APPROVED_WITH_LIMITS_FOR_DESIGN_AND_RECONCILIATION / BLOCKED_FOR_EVALUATED_FILE_LEVEL_MAPPING`.

Allowed now:
- use linked-study semantics for W1 reconciliation;
- use documented raw/master grains, INN/jurisdiction/ATC/criticality/route/recurrence constructs as source-backed candidates;
- use published limitations as evidence about data heterogeneity and temporal incompleteness.

Not allowed yet:
- claim exact dataset schema;
- compute SemRisk mapping coverage denominators from the Figshare files;
- report dataset-level missingness/duplicate/validity metrics;
- use the dataset in release-bound SQL/SPARQL parity or quantitative evaluation.

## 6. G1 consequence

DS-004 no longer represents an **unknown primary-data identity**: its authoritative primary-data locator, source lineage, study grains and documented analytical variables are now established. The remaining gap is file-level qualification needed for later evaluated use. G1 may treat the dataset artifact as `PARTIAL/BLOCKED_FILE_LEVEL` with explicit consequences rather than as an undiscovered source.