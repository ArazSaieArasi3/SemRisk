# Run 9 — traceable pharmaceutical literature pilot

Date: 2026-10-05. Baseline: `231a82cde3a43ccbafc06afa744ea9df35af7c26`. Ontology: `0.2.0-rc.4` unchanged. CM-PharmE semantic bridge: v1.0.0, not a guessed conference citation.

## Delivered scope

The prepared extraction protocol is now executed for six accessible primary studies and 24 source-local paraphrased enterprise-risk statements. JSON/CSV records, separate analyst mappings, dedup decisions, source roles, exact passage locators, search/screening audit, DS-001–004 dispositions, codebook, bibliography and manifest live in [the dataset package](../../../case/pharma/literature-pilot-v0.1.0/README.md). A two-sheet [review workbook](../../../outputs/semrisk-run9/pharma-literature-pilot-v0.1.0.xlsx) covers all statements and sources.

Twelve mappings support a possible situation type; eleven retain ambiguous factors/criteria; one remains unmapped. No occurred event, concrete firm, calibrated probability or domain assessment result is invented. The RDF information graph has 978 triples. Three reused sources contribute 15 statements; three newly located sources contribute nine, with newness measured only against the frozen repository source register. All evidence is applicability only; zero independent validation and zero expert responses.

## Verification and boundaries

Local checks: 27/27, including 12 negative controls; exact CSV round-trip, deterministic RDF, source/mapping query counts and artifact/version/content SHACL constraints. The workbook has zero spreadsheet error cells and is visually reviewed. Native PostgreSQL results and publication readback are separate observed checkpoints; consult `ci-evidence.json` and `run-9-readback.json` once published.

The new adapter loads full source/statement/mapping payloads into existing governed information staging. It preserves actual research-artifact provenance and differentiates these from synthetic domain fixtures. It does not claim normalized rc.4 domain-helper or temporal parity. Existing ontology/diagram/formal releases remain byte-identical.

Five of six selected studies concern Iran; publications span 2012–2022. Counts are not incidents, participant totals, globally unique risks, prevalence or systematic-review coverage. One source has conflicting sample sizes, retained as a limitation. One precise reuse license and the exact CM-PharmE ver.1 conference reference list remain unresolved. Stop at the bounded accessible corpus; the original 30–50-row estimate is not a quota. No scholarly dataset DOI/license, final Word/PDF or full-paper readiness claim.

## Coverage and next work

All 90 requirements remain routed. A bookkeeping inconsistency was corrected: Run 7/8 reports counted 22 accepted requirement rows, but the machine register still contained 18. Companion-only rows 5.2/5.4/5.5/5.6 were rechecked against unchanged rc.4 evidence and synchronized. These are four historical reconciliations, not four new scientific results. Six P09 requirements now pass at bounded scope: 4.12, 6.1, 6.3, 6.5, 6.6, 6.12. Four remain partial: 3.9, 6.2, 6.4, 6.7. Overall: 28/90 = 31.1% requirements evidenced; 3/19 = 15.8% package contracts accepted (P02/P03/P05), unchanged. P09 is 6/10 = 60% by its requirement checklist; this is not 60% scientific quality or final-paper readiness.

Next: P10 remaining normalized artifact/content/scale/workflow SQL synchronization and bounded parity. Carry the actual pilot into P12 review and P14/P15 evaluation/manuscript; do not repeat broad planning/search. Seven continuation prompts were updated: P09/P10/P12/P13/P14/P15/P18.

## Batch acceptance checklist

1. Frozen baseline and pre-extraction acceptance contract.
2. Six inspected sources and search/screening/source-role records.
3. Twenty-four traceable statements, mappings and complete dedup audit.
4. Deterministic data exports, 27 integrity/negative checks and readback.
5. Native PostgreSQL load/idempotence/round-trip/rejection checks.
6. Two-sheet reviewed workbook and complete codebook/bibliography/manifest.
7. Requirements, continuation prompts and issue evidence synchronized.
8. Exact repository readback, successful CI and verified PR merge.

Items 5, 7 and 8 require observed remote evidence; artifact creation alone does not satisfy them. Final state is recorded in the publication checkpoint.
