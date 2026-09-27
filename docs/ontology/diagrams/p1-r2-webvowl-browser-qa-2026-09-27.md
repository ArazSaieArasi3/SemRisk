# P1-R2 WebVOWL offline browser QA — 2026-09-27

**Scope:** private, source-controlled static candidate at `docs/ontology/generated/webvowl-viewer-candidate-v0.1/`. This record is not a Pages deployment, public-access check, comprehensive usability study or scholarly release. Semantic source remains `c17cc111f02309270a60474623259cefcf907c6f`.

## Executed checks

| Evidence | Observation | Limit |
| --- | --- | --- |
| [Static bundle CI](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312072266) | SHA-256 manifest, local assets, byte-identical source JSON, canonical view IRI and no remote CSS asset passed. | Does not render a page or audit all optional editor/export paths. |
| [First Chromium attempt](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36311964041) | Graph rendered, but the no-outbound-request assertion detected Google Fonts CSS/woff requests. | The upstream CSS import was removed from the bundled copy; source viewer remains pinned. |
| [Desktop/mobile smoke](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312069840) | Both viewports loaded the local JSON with HTTP 200, drew 45 initially displayed class nodes, accepted a search term, changed graph transform on zoom, logged no page errors and made zero outbound requests. | Initial count is after WebVOWL's collapsing filter, not the raw class/property inventory. Screenshot review found a narrow phone canvas. |
| [Responsive smoke](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312261370) | Phone details rail now starts collapsed; a 390px viewport supplies the full canvas width. Desktop and mobile smoke passed. | Graph labels remain small, and the initial filter hint occupies much of the phone view. |
| [Viewport/overflow smoke](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312455907) | Desktop and 390px mobile Chromium passed; mobile document scroll width was 390px, with menu items inside a deliberately scrollable horizontal toolbar. Private viewport screenshots were captured. | The captured filter hint was still animating closed; screenshot timing was adjusted for a later run. |
| [Final viewport capture](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312545968) | Desktop/mobile checks passed again. Private artifact contains 1440×900 and 390×844 viewport screenshots after dismissing the filter hint; mobile canvas uses the full width. | Labels remain very small on a phone and the graph is still an exploratory combined view. |
| [Module browser smoke after completed layout](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36319497749) | Combined view and all five module views loaded local JSON with HTTP 200 and zero outbound requests/page errors. Press-and-hold zoom changed the completed graph transform. | This verifies narrow interaction and display, not the semantic fidelity of every label or human task success. |

The JSON conversion [manifest](../generated/webvowl-candidate-v0.1/manifest.json) checks **35/35** local OWL classes and **37/37** local object properties from the exact seven-source asserted union. Four SKOS markers are outside that denominator. The browser's 45 visible class nodes include imported/structural content and are affected by its automatic collapsing filter; the two numbers measure different things. The source reference is asserted input, not OWL entailment.

## Focused module views

Each [module JSON](../generated/webvowl-module-v0.1/manifest.json) uses only the asserted triples in one exact SemRisk Turtle file. Imports are omitted in the derived conversion input; referenced gUFO and other-module IRIs appear as context stubs without their definitions. This is useful for exploration and must not be interpreted as the imported closure.

| Module | Local OWL classes | Local object properties | Visualizer class nodes after layout | Browser result |
| --- | ---: | ---: | ---: | --- |
| Core | 26 | 29 | 43 | Loaded |
| Enterprise | 4 | 3 | 10 | Loaded; labels are easier to separate, but external stubs/edge clipping remain |
| Method | 5 | 2 | 7 | Loaded |
| Governance | 0 | 2 | 4 | Loaded |
| Pharma | 0 | 1 | 1 | Loaded |

The totals are 35 local classes and 37 local object properties; a Core SKOS marker and three Mappings SKOS markers are separate. Mappings is omitted from the WebVOWL module menu because it has no local OWL class/object property. A prior browser test counted nodes before layout completion; [run 36319497749](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36319497749) waits for the loading indicator to disappear and holds the zoom button long enough to exercise its actual mousedown behavior.

## Visual observations and remaining acceptance

- Desktop renders a connected graph, search, zoom, filter menu and detail rail. Labels in dense areas are small; the combined view is not a complete readable diagram by inspection alone.
- Mobile renders and receives the full graph canvas after the details rail is collapsed, but combined-view labels are too small for reliable phone reading at the initial scale. Module views now exist; a target-reader mobile check and selection/default design remain #119 work.
- The runtime network assertion covered initial load and the exercised search/zoom path only. The hidden upstream converter/editor controls and bundled transitive license inventory need review before public publication. No ontology was uploaded during these runs.
- Target-reader tasks, keyboard/screen-reader review, cross-surface links, public URL, #55 release identity and #56 privacy/license/access decision remain open under #119/#117/#118/#55/#56.

**Disposition:** offline rendering and narrow interaction/network smoke pass; mobile and combined-graph readability remain partial. Do not use this as OGCM-RF RO-19/RO-30 conformance or a verified public WebVOWL link.
