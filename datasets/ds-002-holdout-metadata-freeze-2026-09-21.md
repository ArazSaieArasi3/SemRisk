# DS-002 Holdout-Safe Metadata Qualification — Patient Safety / FAERS

**Dataset ID:** DS-002
**Dataset DOI:** `10.7910/DVN/G9SHDA`
**Linked publication:** Zhang, Sumathipala & Zitnik (2021), Nature Computational Science.
**Qualification date:** 2026-09-21
**Status:** `METADATA_AND_PUBLIC_DOCUMENTATION_QUALIFIED / RECORDS_UNINSPECTED`.

## 1. Provenance

The peer-reviewed publication and project site identify Harvard Dataverse DOI `10.7910/DVN/G9SHDA` as the public data resource supporting the study. The source data originate from FDA FAERS.

Public documentation states the study examined 10,443,476 FAERS reports from 2013-01 through 2020-09 before population-specific filtering. The project provides processed patient-safety data, drug/adverse-event mappings and ATC mappings, with raw-data download and preprocessing code documented separately.

## 2. Reproducibility-code binding

Supporting code repository: `mims-harvard/patient-safety`.
- immutable observed repository commit: `d3a62d01f980320048f97d34bd8c1cd7ee464f8f`;
- repository/software license: MIT.

**Important:** the GitHub software license is not substituted for the Harvard Dataverse dataset license.

## 3. Holdout-integrity change

During metadata qualification, public project documentation exposed structural details of the processed dataset. Therefore DS-002 can no longer be represented as a **schema-blind independent holdout**.

No Dataverse records/files were downloaded or inspected in this execution. Consequently, a narrower role remains possible:

`RECORD_LEVEL_TRANSFERABILITY_HOLDOUT_CANDIDATE`

provided the exact dataset release and evaluation protocol are frozen before any record-level inspection.

## 4. Allowed and prohibited use

Allowed:
- provenance and methodology comparison;
- predeclared E11 record-level transferability testing after exact release freeze;
- external pharmacovigilance application context.

Prohibited:
- independent validation of schema/Core semantics;
- using exposed project schema details to justify new SemRisk classes/properties;
- calling the dataset independent if the actual records later influence mappings/rules before test freeze.

## 5. Remaining qualification debt

- exact Harvard Dataverse version;
- dataset-specific license;
- file manifest/checksums;
- predeclared record-level test protocol and expected outcomes.

Schema/content mining is intentionally deferred to the evaluation phase if the record-level holdout role is retained.