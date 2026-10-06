# Interpretation of SQL-independent rc.4 metrics

These measurements supplement formal/source verification. They do not establish domain validation, overall scientific quality, universal completeness, comparative superiority or release assurance.

The protocol was committed at `7a7f50bd699985faf5e2136b9daf2d35dabe1e7b` before the new candidate calculations. Prior P1-R2 results and inventory counts were already known. Domain classes and helper classes are separate populations; imported gUFO classes, conceptual markers and undeclared concept slots are excluded by explicit registry rules.

## Findings and adverse evidence

- Domain classes: 35/35 have a nonempty local label and 35/35 a nonempty local comment. This establishes presence only. The synthetic nonsense-comment control leaves the metrics unchanged.
- Helpers: 5/11 have a nonempty local label and 6/11 a nonempty local comment. The complete missing-IRI lists are retained in `evaluation/oquare/rc4-bounded/results.json`. No missing annotation was invented, and no frozen ontology file was changed to improve a score.
- Raw assertion density is 70/35 = 2 for domain classes and 11/11 = 1 for helpers. Additional or empty annotations can inflate density without improving semantics; it is not a percentage or quality grade.
- The asserted multiple-parent diagnostic is 5/34 for domain classes and 0/10 for helpers. These are explicitly scoped OQuaRE-style values using the historical N−1 convention. Named multiple inheritance can be justified; neither value proves a defect, and a third parent on an already counted class is invisible to this metric.

The changed domain multiple-parent value must not be described as deterioration against the historical pilot: the asserted semantic pattern and helper generalizations changed, while the original pilot remains version-bound. Cross-version numerical comparison alone is not a controlled quality comparison.

## Reporting contract

Use the integer fractions, population, candidate version and precise metric names. Do not pool domain and helper coverage to hide missing documentation. Do not call comments validated definitions, raw density completeness, or four metrics full OQuaRE/OQF adoption. Two metrics reuse OQuaRE families through explicit local operationalization; two are local presence diagnostics. The official Java engine was not executed. No one-to-five band or aggregate score is supplied.

Original CQ statuses and the eight historical paired tasks remain separate. #125 is deferred; no SQL queries, schemas or parity implementation are added by this batch. The six-source/24-statement pilot has its own information-level provenance and limitations, not a denominator for these ontology measurements.

#126/P13's broader P07/P09 dependencies remain governed by their own acceptance conditions. A reproducible raw result is usable even while the issue and assurance gates remain open; it does not waive them.
