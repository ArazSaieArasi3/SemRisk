> Current checkpoint: [Run 3](run-3-report.md), 3/19 bounded revision package contracts accepted. Use [status](status.md) for current progress; earlier reports are historical.

# SemRisk author-revision execution register

Snapshot: 2026-10-04. Master: [#8](https://github.com/ArazSaieArasi3/SemRisk/issues/8).
This controls the new 90-requirement revision cycle over the existing candidate, not a restart of the research.

- [Current status and next action](status.md)
- [90 requirement rows and individual acceptance tests](requirements.csv) / [JSON](requirements.json)
- [19 package contracts](work-packages.json) and [33-issue routing](issue-map.json)
- [Baseline](baseline.json), [legacy PR dispositions](legacy-pr-disposition.md), [additional findings](additional-findings.json)
- [Scientific contract](scientific-contract.md) and [Persian evidence-grounding rationale](evidence-grounded-fa.md)
- [Correct venue contract](../../../publications/2026-icaea-sbu/venue-contract.md)
- [Execution prompt](execution-prompt.md) and [19 package-specific prompts](prompts/)
- [33 rhetorical criteria](rhetorical-rubric.json), [artifact groups](artifact-register.json), [revision gates](gates.json)

## Progress accounting

Coverage = mapped requirements / 90; issue routing = mapped pre-existing open issues / 29. Neither is implementation progress.
Accepted package completion = packages with completed status and nonconditional acceptance / 19. Equal units are a transparent checklist measure, not an estimate of effort or scientific readiness. Reopening a package reduces the count and must be explained.
Each run also publishes its own checklist numerator/denominator. Scientific readiness requires all applicable publication gates; blockers cannot be averaged away.
Historical W/G and P1-R release labels are retained. Revision gates use **EG0-EG6** to avoid silently redefining historical gates.

## Fast execution order

1. P01/P02 control and bounded claims; proceed under explicit submission-only conditions.
2. P03/P04 closest-work and standards deltas; prepare P09 extraction protocol and P12 instrument early.
3. P05 actual method; P06 semantic closure; P07 formal sources and P08 true OntoUML.
4. P09 final source-derived case; P10 relational load/parity; P11 tests and P13 metrics; P12 real review; P14 synthesis.
5. P15 compact rewrite; P16 docs and P17 existing viewer; P19 rendered Word/PDF and rhetoric review.
6. P18 release/citation/license package after applicable gates. No dependency on full OQF completion or CM-PharmE v2.

P09/P12 preparation can start before final ontology freeze; their final outputs must use the reviewed candidate. The author receives one consolidated candidate rather than repeated small approval requests. Expert contact/signature and permanent publication decisions remain real external steps.
