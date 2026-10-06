# Run 12 — SQL-independent bounded metrics

Source baseline: `da148b2508f1eb820a37099cc135a794a290063b`. Protocol was committed before new calculation as `7a7f50bd699985faf5e2136b9daf2d35dabe1e7b`; the historical pilot and inventory were already known, so no blinded-selection claim is made.

## Delivered scope

- Four preselected diagnostics, applied separately to 35 domain classes and 11 helpers: raw TMOnto-style multiple-parent ratio, raw ANOnto-style assertion density, local nonempty label coverage and local nonempty comment coverage.
- Exact formulas, zero-denominator policy, population/member hashes, complete class-level parents/annotation ledger, source/protocol/script hashes, pinned RDFLib and deterministic recomputation.
- Twenty protocol-derived synthetic/sensitivity checks (nineteen original plus imported-file boundary hardening) and one generated-result-drift rejection; missing registry class, unexpected local class, source drift and unbound imports reject. Third-parent and nonsense-comment tests explicitly expose insensitivity.
- Bounded interpretation report and path-triggered CI. Historical P1-R2 pilot JSON/NT/Markdown and ontology source bytes remain unchanged.

## Raw results

| Population | TMOnto-style | ANOnto-style assertions/class | Label presence | Comment presence |
| --- | ---: | ---: | ---: | ---: |
| Domain | 5/34 | 70/35 | 35/35 | 35/35 |
| Helpers | 0/10 | 11/11 | 5/11 | 6/11 |

Helper annotation gaps are retained as adverse descriptive findings. There is no one-to-five scale, overall score, semantic-correctness inference, full framework adoption or official-engine equivalence claim. Comments are not automatically adequate definitions; multiple inheritance is not automatically wrong. These results do not prove better/worse quality than the historical semantic candidate.

## Acceptance disposition

All eight raw result rows are locally recomputable from the frozen protocol and source; exact-head independent review/CI/main readback belong to the batch PR. Requirement 4.11 is evidenced at bounded diagnostic scope, moving the requirement denominator from 28/90 to **29/90**. This is not overall project or paper readiness.

#126 remains open for its declared broader P07/P09 dependency acceptance. Accepted whole packages remain **3/19**. #125 is deferred and this batch performs no SQL work, rebrands no historical CQ result, collects no expert response and waives no semantic/release gate.

Next authorized batch after verified integration: #53/#111/#56 current claim, evidence and limitation synchronization; then #32 and dependency-ready #34 manuscript integration using the preserved latest author-review input.
