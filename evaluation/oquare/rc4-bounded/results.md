# rc.4 bounded metric results

Protocol commit: `7a7f50bd699985faf5e2136b9daf2d35dabe1e7b`; source commit: `da148b2508f1eb820a37099cc135a794a290063b`. The protocol was recorded before the new calculation, with historical pilot and inventory counts already known.

| Population | Diagnostic | Numerator | Denominator | Raw value |
| --- | --- | ---: | ---: | ---: |
| domain | TMOnto_asserted_scoped | 5 | 34 | 0.14705882352941177 |
| domain | ANOnto_assertion_density_scoped | 70 | 35 | 2.0 |
| domain | Local_nonempty_label_coverage | 35 | 35 | 1.0 |
| domain | Local_nonempty_comment_coverage | 35 | 35 | 1.0 |
| helpers | TMOnto_asserted_scoped | 0 | 10 | 0.0 |
| helpers | ANOnto_assertion_density_scoped | 11 | 11 | 1.0 |
| helpers | Local_nonempty_label_coverage | 5 | 11 | 0.45454545454545453 |
| helpers | Local_nonempty_comment_coverage | 6 | 11 | 0.5454545454545454 |

All results are descriptive and scope-bound. Domain and helper rows are not pooled. Zero coverage, if observed, means missing nonempty annotations under the declared local rule, not absence of semantics or a command to fabricate documentation. The class ledger exposes missing values and all counted assertions.

20 protocol-derived synthetic/sensitivity checks passed before each candidate calculation (including added source-boundary hardening). The third-parent and nonsense-comment tests deliberately demonstrate insensitivity. No one-to-five bands or aggregate score is produced.

Reproduce: `python tools/measure_rc4_bounded_metrics.py --check`. Existing P1-R2 pilot bytes are unchanged. Full CQ/SQL reevaluation, broader P07/P09 acceptance and scholarly publication remain separate.
