# DS-003 v4 file and codebook audit

**Owner:** #17. **Source:** [versioned publisher API](https://api.figshare.com/v2/articles/29178665/versions/4), DOI `10.25375/uct.29178665.v4`; CC BY 4.0. Downloaded 2026-10-02. Files remain at the publisher; this repository stores derived structure, code labels and hashes. Attribute the dataset creators through the DOI landing record when reusing the extraction.

## Verified package

Six files total **2,031,599 bytes** (1.9375 MiB). Actual byte lengths and MD5 values match the versioned API for 6/6 files; independent SHA-256 values are in `ds003-v4-file-manifest-2026-10-02.json`. This reconciles the approximately 1.94 MiB listing. The old 18.01 MB assertion is unsupported for these v4 files and is superseded.

## Exact codebook structure

One sheet, `Codebook`, range `A1:F252`: six columns and **251 data rows**, with **152 distinct Name strings** and six Folder values. Those denominators refer to export rows/labels, not concepts, participants, ontology coverage, or population prevalence. Only one Description cell is populated; 250 rows have no native definition. `Sources` and `References` are numeric coding metadata. Quotation strings in `Reference` are not copied into the extraction.

The schema table records all six columns, observed types, missingness and interpretation boundaries. The code table preserves all 251 source-row locators and native labels as unreconciled profile/value-set candidates. Spelling/case variants remain native evidence; no automated equivalence or new ontology classes are asserted. Row extraction completeness is 251/251 for the codebook export only. Transcript semantics and four PDF bodies remain unmined; entire-package semantic completeness is **PARTIAL**.

## Downstream use

This closes the file-manifest/size ambiguity and codebook column inventory debt. Semantic normalization, code-by-code reconciliation and remaining file coverage stay in #17/#18. The existing #28 qualitative case remains frozen; new rows do not increase its evaluated denominator or create independent validation. DS-004 file debt and unavailable DS-001 primary records and DS-002 record-level holdout controls remain separate.

## Extraction method

The XLS was read with `xlrd 2.0.1`: retain row 1 as the six native headers; enumerate rows 2–252 with exact cell addresses; copy A/B labels and D/E coding counts; record whether C is empty; omit F quotation text. Validate every exported row against the source workbook after verifying its SHA-256 against the file manifest.
