# Run 7 — editable diagram and complete companion atlas

Baseline: `0417f1d7f0237904f8b57a65ddc5385aeab85fb0`; candidate ontology **0.2.0-rc.3** unchanged. Current outputs: [package](../../../diagrams/ontouml/0.2.0-rc.3/README.md), [checks](../../../diagrams/ontouml/0.2.0-rc.3/validation-results.json), [coverage](../../../diagrams/ontouml/0.2.0-rc.3/concept-coverage.csv).

## Executed result

Actual editable OntoUML schema JSON and draw.io source; 15 SVG views; complete tiled SVG; 15-page A3 vector review PDF; separately labeled 170 mm scenario panel; exact coverage, multiplicity evidence and source hashes. There are **47/47 concepts**, **38/38 registered relations**, 11 separately counted helper classes, seven controlled literals and all 19 distinct helper properties. Scoped projections and generalizations yield 98 diagram edges; the editable package contains 786 model/view/geometry elements. These larger counts are not additional domain vocabulary or quality scores.

**16/16 bounded checks**, including **six expected fault-injection rejections**, passed locally. Cardinalities were also compared independently with actual SHACL shapes: temporal attributes belong to qualified responsibility/workflow, not an invented mandatory assessment interval. Native-editor round-trip and complete UFO/OntoUML antipattern testing are unexecuted. Upstream schema JSON is byte-bound to Git blob `7608e50f9e020fbadc782fd86d6b0c66e3b85b65`. All 15 PDF pages and the paper-panel render were inspected; minimum review text is 8.52 pt, scoped panel 8.56 pt. Continuous integration and exact remote readback are recorded separately once observed.

## Open gates and ownership

| Gate | Owner | Next evidence |
|---|---|---|
| Exposure isolated in registered graph | #123 / #124 | Decide explicit bounded exclusion or justified association; if changed, successor release and impacted tests |
| NumericScale category; external RoleMixin realization | #123 | Source-backed classification/bridge boundary; no fictitious stereotype |
| Full antipattern and editor round-trip | #33 / #113 | Actual detector/import results, or explicit supported-tool limitation |
| Complete figure at IEEE width | #33 / #34 | Readable article panel arrangement with complete companion route; retain seven-page target and eight-page cap |
| Formal description and data parity | #115 / #125 | Bring new helpers into formal reference and SQL/CQ scope without recycling old parity numbers |

Risk/Risk Source pattern boundaries are explicit design choices, not falsely completed single categories. Exposure is deliberately visible rather than hidden by dropping a node. No empirical case records, expert responses or final revised Word/PDF article were created in this diagram batch. The companion PDF is not the manuscript.

## Progress and handoff

- Run artifact checklist: source, complete views, vector PDFs, coverage, executable validation, rendered inspection, control/issue updates, publication/readback. Final completion of the last two items is established by the remote readback checkpoint, not by this draft claim.
- Bounded packages accepted: **3/19 = 15.8%**, unchanged; P08 remains conditional.
- Author requirements evidenced: **22/90 = 24.4%**, previously 18/90. New bounded evidence covers 5.2, 5.4, 5.5, 5.6 for the companion artifacts; manuscript integration remains separate. **90/90 routed** remains unchanged.
- Next smallest batch: resolve Exposure/NumericScale and diagram semantic gates with explicit decisions, then synchronize formal reference and new-helper SQL parity. The prepared P09 literature-case extraction remains dependency-ready and must not wait for indefinite diagram polish. Reuse CM-PharmE v1 and the existing extraction protocol; no new broad replanning.

Seven continuation prompts (P06/P07/P08/P09/P10/P13/P15) now begin with current inputs, unresolved checks and stopping boundaries. Issue #33 carries the diagram gate; related issues retain specialist ownership. No issue is closed merely for coverage or green CI.
