# Issue #47 governed data-load specification v0.1

## Allowed inputs for this snapshot
- SRC-OP-001: schema/mapping provenance only; no empirical record corpus exists.
- DS-003 v4: bounded constructed Pharma case derived from frozen study-level thematic summaries.
- SYNTH-P1: deterministic synthetic operational fixture, seed 4701.
- DS-004: explicitly BLOCKED at file level.
- DS-002: explicitly PROTECTED as record-level holdout.
- DS-001: supplementary; not loaded as primary evidence.

## Pipeline
source registry → staging.load_batch/source_record → semantic_instance + typed projection tables → provenance/reconciliation tests.

No source data are overwritten. Staging records preserve disposition even when a source is blocked/protected/partial.

## Semantic transformation rules
DS-003 follows `case/pharma/pharma-case-transformation-spec-v1.0.md`. Constructed data use `constructed_case` evidence role and `synthetic_flag=true` because they are generated abstractions, not raw empirical rows. No dated Risk Event, prevalence, causal strength or treatment effectiveness is fabricated.

SRC-OP-001 contributes schema/mapping context only. A deterministic synthetic operational register fixture is generated from seed 4701 to exercise register/workflow/responsibility paths without pretending the private spreadsheet supplied record data.

## Quarantine policy
Invalid or unmapped future source rows must be inserted into `staging.reject_record` with retained original value and reason. Silent coercion/deletion is prohibited.

## Reproducibility
Snapshot identifier: `P1-DATA-0.1.0-rc.1`.
Synthetic generator identity: `SYNTH-P1-0.1.0-seed-4701`.
All primary IDs in the fixture are deterministic constants. CI rebuilds the DB from zero and reruns reconciliation tests.
