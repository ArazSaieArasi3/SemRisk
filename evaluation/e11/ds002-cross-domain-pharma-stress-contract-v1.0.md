# DS-002 Cross-Domain Pharma Stress Contract v1.0

**Owner:** Issue #107  
**State:** PROTECTED — RECORDS UNOPENED

DS-002 is a FAERS-derived adverse-event dataset family. FDA describes FAERS as a post-marketing safety-surveillance database containing adverse-event, medication-error and related safety reports. It is therefore **not a drug-shortage dataset**.

## Permitted future role
DS-002 may be activated only as a **cross-domain pharmaceutical stress candidate** for selected generic SemRisk Core semantics, for example:
- Risk Event / event occurrence;
- Evidence Item / provenance;
- Signal/profile semantics;
- external drug/product references;
- observation/reporting artifacts.

## Prohibited interpretation
- It must not be described as direct validation of antibiotic-shortage semantics.
- It must not establish shortage-specific transferability.
- Publicly exposed schema details must not be reused as independent design validation.
- Record files remain unopened until exact release/license/checksums and predeclared E11 tasks are frozen.

A future E11 activation must specify the exact semantic questions whose portability across **shortage management → pharmacovigilance** is being tested.
