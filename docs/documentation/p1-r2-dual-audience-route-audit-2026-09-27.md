# P1-R2 dual-audience route audit

**Status:** bounded desktop/source route inspection; not a human usability study or final RO-30 pass.  
**Profile:** OGCM-RF `4822b1a1b7978e94e66bd6a283024bac78b6a0b8`, `templates/documentation/dual-audience-home.md`.  
**Candidate:** SemRisk 0.1.0-rc.1; private Wiki source in `docs/wiki/pages/`. Prior live Wiki read-back is recorded in `docs/wiki/p1-r2-live-wiki-readback-2026-09-26.md`.

## Reader tasks and observed routes

| Task | Entry and destination | Source-level observation | Disposition |
| --- | --- | --- | --- |
| Researcher identifies candidate scope and contribution ceiling | Home → Scope and Contributions | Named research shortcut exists; destination states selected distinctions, 27/27 and 8/8 denominators, unsupported independent transferability and open gates. | BOUNDED |
| Researcher finds formalization and evaluation | Home → Semantic Architecture / Pharma Case → Evidence and VVEAA | All named destinations exist among the eight Wiki sources; the research shortcut explicitly reaches evidence and reproducibility. | BOUNDED |
| Researcher finds final citation and limitations | Home → Reproduce and Release | Destination states citation/DOI pending #55/#56 and release limitations. It does not supply a final verified bibliography; manuscript v0.3 also says references await verification. | PARTIAL (#53/#55) |
| Engineer locates semantic authority | Home → Semantic Architecture → Formal Reference | Engineering shortcut points to formal reference. That page links exact Turtle, inventory and asserted closure, and distinguishes them from OWL entailment. | BOUNDED |
| Engineer evaluates SQL mapping and caveats | Home → Relational Projection → Reproduce and Release | Destination states task-specific 8/8 and representation losses and links mapping/parity evidence. | BOUNDED |
| Practitioner explores and integrates a versioned ontology visually | Formal Reference → Pages/WebVOWL | No published Pages or WebVOWL route; SVG atlas and relation map are source-derived candidate views only. | PENDING (#117/#119/#55/#56) |

## Checks against the OGCM-RF Home pattern

- Both applicable audience shortcuts appear in Home. A product/business route is absent because that profile is declared N/A for this candidate; no invented shortcut is offered.
- Every named Wiki destination in the Home shortcuts resolves to one of the eight source-controlled pages (nine link occurrences; seven distinct destinations). The Wiki publication guard checks source links and hashes; the prior live read-back checks the published eight-page state separately.
- Research shortcut reaches evaluation and limitations; engineering shortcut reaches semantic authority and caveats. Candidate maturity is visible on Home and each destination, and the pages point back to ontology/evidence authority.
- The route is not a measured usability outcome. There is no task observation with academic/industrial participants, mobile accessibility assessment, time/error data or public Pages read-back. The complete citation route and interactive explorer are unavailable.

## Next acceptance checks

1. After #53/#55, render page-local references from the governed REF corpus and verify a researcher's claim → source → exact version path.
2. After #117/#119 and #56, inspect desktop/mobile rendered routes, search/legend and version compatibility using actual target readers and record task success, errors and unresolved ambiguity.
3. Rerun source hash, published read-back and link checks on the exact documentation baseline; reassess RO-30 and QN/QL then.

**Result:** RO-30 is `partial` for route existence and bounded task inspection. This audit is not evidence of satisfactory dual-audience usability or OGCM-RF conformance.
