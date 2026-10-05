# Pharmaceutical enterprise-risk literature pilot v0.1.0

**Research candidate, bound to SemRisk 0.2.0-rc.4.** This package contains 24 paraphrased, source-local statements from six primary research papers. It is an applicability dataset, not a register of 24 observed incidents, an independent validation set, a systematic review or a representative pharmaceutical-risk taxonomy.

## What the records establish

Twelve statements support a cautiously described possible situation type. Eleven contain risk factors or selection criteria whose event/outcome meaning is insufficiently specified. One merger/acquisition label is unmapped at the scenario level. All 24 retain their provenance as information artifacts. `partial` means useful representation with unresolved domain/identity detail, not exact semantic equivalence. `ambiguous` and `unmapped` are findings, not pipeline errors. No domain Risk Event, measured probability, severity, implemented control or named company is invented.

The dataset spans analyst-coded financial, regulatory, strategic, governance, information, environmental, quality, logistics, operational, market and availability concerns. These labels are an extraction codebook, not 11 new ontology domains or evidence of complete enterprise-risk coverage. Five of six studies concern Iran and the papers date from 2012–2022. This access- and lineage-shaped pilot must not be presented as current worldwide prevalence evidence. No new expert responses were collected. All extraction remains unreviewed by an independent human coder.

## Files and regeneration

- `statements.json`: curated source paraphrases and explicit missingness; canonical data.
- `sources.json`: citations, inspected versions, roles, rights and study limitations.
- `mappings.json`: separate analyst mappings and field dispositions, including uncertainty.
- `statements.csv`, `sources.csv`, `mappings.csv`: generated UTF-8 views with LF line endings.
- `statements.ttl`: deterministic RDF information graph using rc.4 artifact/version/content and scenario-type semantics. Application metadata uses its own namespace and adds no SemRisk core class.
- `dedup-decisions.json`: every retained record has a source-local retention decision; shared topic groups never imply the same risk or independent corroboration.
- `source-freeze.json`, `search-screening.json`, `acceptance-contract.md`, `codebook.md`, `bibliography.md`: methodological controls and complete extraction bibliography.
- `metrics.json`, `validation-results.json`, `manifest.json`: generated counts, bounded tests and exact bytes.
- `postgres-results.json` and `ci-evidence.json`, when present: actual native CI execution, separately commit-bound.

Run `python tools/build_pharma_literature_pilot.py`, `python tools/check_pharma_literature_pilot.py`, then the builder again to bind the validation result. The dedicated GitHub workflow also initializes V001/V002 in PostgreSQL and runs `tools/check_literature_postgres.py`. No article PDFs or underlying study record files are redistributed.

## Evidence roles and CM-PharmE

Three reused source lineages contribute 15 statements. Three sources absent from the frozen repository register contribute nine statements and carry `evaluation_new`. That label means new relative to the inspected repository register, not proven blind across all past conversations. All six are restricted to **applicability only**. No design changes were made from this corpus; rc.4 remains byte-frozen.

Discovery began from CM-PharmE v1's enterprise/ecosystem scope and SemRisk's existing pharmaceutical baseline. PLS-001 cites the Jaberidoost review seed; PLS-002 is PLS-001 reference 6; PLS-006 is PLS-003 reference 22. PLS-005 was a publisher recommendation, not a citation edge. The IEEE record was unavailable through the retrieval route and the precise conference-paper reference list was not recovered. Direct CM-PharmE-paper citation snowballing remains **open**; later journal revisions and v2 artifacts were not substituted. The frozen CM-PharmE bridge is v1.0.0. General actor/process language is retained as context, with no invented instance IDs or equivalences. Medicine/API identity and Objective are known external gaps.

## Relational boundary

The new adapter loads actual evidence payloads into existing `meta` and `staging` tables. Complete JSON source/statement/mapping payloads support exact reconstruction of the RDF graph. This is **information-level staging fidelity**, not normalized domain-column parity for all rc.4 scale, artifact-content, workflow, responsibility or temporal semantics. Those remain P10. Source publication time and extraction time are never used as the date of a risk event.

## Publication placement and rights

Treat this pilot as supplementary application evidence for the ontology contribution until independent semantic review and release governance are complete. The seven-page manuscript should cite CM-PharmE v1 and whichever primary papers it directly discusses; the full six-item bibliography and every locator belong here. It must report the 12/11/1 mapping outcome and the regional/source-age limitations, rather than claim universal coverage. A paragraph on financial scenarios should cite PLS-003 and PLS-006; a supply/availability example should cite PLS-004; do not hide these behind a generic repository link. Integration into the final manuscript remains P15.

Only short attributed paraphrases and authored mappings are stored. Exact source licenses are recorded when inspected. An article license is not inherited by an unseen underlying dataset. The candidate has no new blanket dataset license or DOI; permanent release and DOI decisions remain P18. The bounded quotation/paraphrase policy permits this reviewable research checkpoint without redistributing full texts. Bibliographic and rights checks do not certify source methodological quality.

## Residual work and stopping decision

The six-source budget was reached. Twenty-four distinct source-local propositions were retained; no rows were manufactured to reach the earlier 30–50 estimate. The batch stops because the information-level dataset, mappings and checks are usable and its gaps are explicit, not because thematic saturation or scenario completeness was established. P09 remains conditional: recover the CM-PharmE v1 reference list, resolve exact PLS-001 reuse terms before scholarly release, review ambiguous mappings with real expertise in P12, and bind claim-critical citations in P15. More corpus growth is justified only by a specific gap, such as newer non-Iranian strategic/regulatory evidence, not a target row count.

DS-001 is an inspected appendix rather than primary shortage rows; DS-002 records remain unopened and are not schema-blind; DS-003 v4 already informed design and is not a holdout; DS-004 exact files/version/license remain blocked. This pilot reuses none of those raw records and changes none of those access dispositions. See `datasets/dataset-registry.csv` and `datasets/ds001-ds004-access-disposition-2026-10-02.md` at the frozen baseline.
