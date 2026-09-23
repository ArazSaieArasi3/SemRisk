# Pharma case handoff to #45–#49 and #30/#31

## Frozen package
- primary dataset binding: DS-003 v4 / DOI 10.25375/uct.29178665.v4 / CC BY 4.0;
- structured extension DS-004 excluded until file-level qualification;
- 18-element governed source→semantic mapping;
- explicit denominator coverage report;
- conflict/unmapped register;
- constructed case input and Turtle instance package;
- 8 executable case CQs/expected answers.

## #45 relational design
Create tables that preserve:
- source dataset/version/provenance;
- Evidence Item vs Assessment Result;
- Scenario vs Event;
- external CM-PharmE target identity;
- treatment strategy vs activity;
- mapping disposition/confidence;
- historical provenance.

## #46 PostgreSQL twin
Load the constructed case package as **synthetic/constructed application fixture**, not as DS-003 raw empirical rows.

## #47 data load
DS-003 raw-file ingestion is optional and requires an explicit file acquisition/checksum step. DS-004 ingestion is blocked until exact file manifest/version/license/checksum/schema is frozen.

## #48 end-to-end scenario
Use the constructed case to exercise create/query/assessment/evidence/treatment/responsibility paths. Do not compute a universal risk score.

## #49 SQL↔SPARQL parity
Use PH-CQ-001/002/003/005/006/008 as initial parity candidates and document OWA/CWA differences.

## #30/#31 evaluation
The case supports bounded application/mapping evidence, not independent semantic validation. Expert/holdout/comparative evidence must remain separately classified.
