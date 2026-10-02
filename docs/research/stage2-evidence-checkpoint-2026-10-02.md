# Stage 2 evidence checkpoint — 2026-10-02

Baseline `db3cc89ade7efa213b68c235844da640ffcf9424`. **Current stage: 2, IN_PROGRESS.** Stage 1 technical audit is complete; the owner now approves extracted SRC-OP-001 vocabulary publication. Root license and final release decisions remain #56.

| Issue | Completed in this wave | Remaining acceptance work | State |
| --- | --- | --- | --- |
| #4 | Bounded Health evidence/ownership/exclusion document; ReMINE and ARK identities registered | Broader Health families, internal bridge identities and source-specific stopping check | OPEN |
| #12 | SRC-PA-002 text section profile with conflicts/limitations; ARK text and ReMINE abstract profiles | Figures, remaining seeded papers, source-complete coverage | OPEN |
| #13 | Exact ICH Corr.2 locators; 40 coverage units and 11 selected non-equivalence mappings | Remaining guideline detail and other standards/framework locators/access | OPEN |
| #15 | PH-010 DOI/year/abstract and pharmacovigilance boundary; DS-003 source inventory | Remaining Pharma full texts/figures and final corpus stopping decision | OPEN |
| #17 | DS-003 v4 six-file manifest and hash verification; six-column schema; 251 code rows | Code reconciliation; transcript/PDF semantics; DS-004 access/file debt; underlying DS-001 primary data unavailable | OPEN |

## Exact outputs and tests

- `datasets/ds003-v4-file-manifest-2026-10-02.json`: 6/6 downloaded files match publisher byte counts and MD5; SHA-256 recorded; 2,031,599 total bytes.
- `datasets/ds003-v4-codebook-schema-2026-10-02.csv` and `...-codes-2026-10-02.csv`: one sheet, six columns, 251 source rows, 152 distinct labels; 250 missing descriptions explicitly retained. Participant quotation text is not republished.
- `literature/standards/ich-q9-r1-*2026-10-02*`: section inventory and selected evidence mappings; detailed unmined units remain visible.
- `literature/comparators/src-pa-002-*` and `src-pa-018-019-*`; `literature/pharma/src-ph-010-*`; `profiles/health/paper1-health-evidence-boundary-2026-10-02.md`.
- `evaluation/integrity/src-op-001-publication-decision-2026-10-02.md` and reference inventory: owner decision and where the source is mentioned, without changing its terms.

DS-001 supplement inspection also resolved its file ambiguity: it is a 17,237-byte historical register-link appendix, not the primary dataset. DS-004 returned HTTP 403 and remains access-blocked. Ten PA-002/ARK figures received visual boundary review with source hashes; exhaustive graphical extraction remains unclaimed.

No issue is closed by this wave: the broader acceptance criteria remain unsatisfied. Source inventory completeness, schema extraction, semantic reconciliation and independent evaluation are distinct denominators. The frozen ontology, #28 case denominator and DS-002 record-level holdout remain unchanged.

## Next execution

Continue **stage 2** on `gpt-6-astra high`: reconcile DS-003 code labels and finish remaining file coverage; complete detailed PA-002/ARK extraction; advance NIST clause/schema locators and remaining Pharma sources. Route any proposed semantic change through #18 and an impact review rather than silently editing the frozen release. Stage 3 should begin only after the stage-2 readiness audit or an explicit bounded handoff.
