# #14/#31 comparison-cell locator and denominator audit

Date: 2026-09-28. Scope: `conceptualization/comparison/comparison-cell-evidence-index.csv` as the frozen #22 comparison snapshot, checked against `literature/closest-work-comparison-matrix.csv` and the current Paper-1 manuscript. Decision: **historical orientation only; not final E10 evidence**.

## Recomputed counts

Parsing the CSV as quoted fields yields **204 data rows** in **12 `comparator_id` groups**, with **17 dimension rows per group**. One group is `CMP-012` SemRisk; therefore the external comparison denominator is **11**, not 12. The broader living closest-work matrix has 19 rows including SemRisk and MedSupplyKG and is a different inventory; it is not the source of the 204-cell denominator.

All 204 cells have a nonempty `evidence_locator`, but each of the 12 groups repeats **one identical generic locator across all 17 dimensions** (12 distinct locator strings in total). Examples are `SRC-PA-016 profile`, `deep-mining artifact`, and `ER 2018 DOI; exact repository binding; #21 COVER mapping`. These are useful source-family leads, **not exact page/figure/IRI/axiom locators for each feature judgment**. The `status` column mixes controlled-looking states such as `not_reported` with descriptive prose such as `covered in concrete follow-ups`; it is not a single validated ordinal scale. The `CMP-012` self-row includes pre-implementation statements such as “formal OWL/SHACL not yet implemented”, which are historically meaningful but stale for current P1-R2.

## Claim and workflow consequence

- Manuscript, SR-CL07 calibration/crosswalk, #31 readiness and VVEAA denominators must state **12 historical rows = 11 external + SemRisk**, not “12 comparators”. Those files are corrected at this checkpoint.
- The 204-cell snapshot must not be cited as a current, source-complete, cell-level E10 execution or evidence of absent comparator features. The MedSupplyKG targeted comparison is an additional result, not a 13th row in the old matrix.
- #14 remains OPEN. Convert the claim-critical selected dimensions of the 11 external groups into exact locator/source-artifact paths; replace mixed statuses with explicit coverage/unknown and preserve prior strengths. Re-evaluate the current SemRisk P1-R2 row against its release-bound sources. #31 E10 remains PROVISIONAL until this trace and final shortlist/claim synthesis are done.
- This correction does not alter the historical index itself. A replacement version should have its own versioned path and a mapping from every old cell ID, preserving the audit trail. No score, ranking or overall superiority result is inferred.

Method: parsed 204 rows with a quoted-field CSV reader, counted group IDs and unique `evidence_locator` values within each group, inspected the `CMP-012` statuses and compared the living matrix row count. The result is a completeness/traceability audit, not source mining of all underlying publications.
