# SemRisk P1-R2 offline WebVOWL viewer candidate

**Status:** locally built static bundle; JavaScript, assets and JSON identity checked. Private Chromium desktop/mobile rendering, local JSON fetch, search/zoom smoke and no-outbound-request check passed at [run 36312545968](https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312545968). Graph readability, target-reader usability, full privacy/license review and public Pages deployment remain open. This is an exploratory derived view, not ontology authority, evaluation evidence or the #55 scholarly release.

The initial private Chromium smoke run found an upstream Google Fonts CSS import. It was removed from the bundled stylesheet; system font fallbacks remain. The viewer loads 45 initially displayed class nodes after its automatic collapsing filter. The phone details rail now starts collapsed. [Screenshot review](../../diagrams/p1-r2-webvowl-browser-qa-2026-09-27.md) finds labels small on a phone, so a focused module view remains necessary. The underlying JSON still contains all 35 local classes and 37 local object properties; the initially displayed node count is a different measure.

The bundled `index.html` loads `data/semrisk.json` by default. The JSON is byte-identical to `../webvowl-candidate-v0.1/combined.json`; that file's manifest checks 35/35 SemRisk OWL classes and 37/37 object properties against the exact source inventory. The displayed graph also contains vendored gUFO and structural/reference nodes; the raw WebVOWL JSON has 108 class nodes and 212 property nodes. These are visualizer nodes, not 108/212 SemRisk declarations. Four SKOS markers are outside the class/property denominator. A combined view may be too dense; module-scoped filtering remains #119 work.

The Ontology menu offers five smaller **source-only** projections from Core, Enterprise, Method, Governance and Pharma. Each is generated from one exact Turtle module and does not carry imported gUFO or cross-module definitions; referenced terms are context stubs. The [module manifest](../webvowl-module-v0.1/manifest.json) records source blobs and local IRI coverage. Mappings has only three SKOS markers and no local OWL class/object property, so it is documented outside the WebVOWL module menu. The combined view remains the seven-file asserted union. Module browser/readability QA is tracked separately and is not implied by the combined-view smoke.

## Local preview

From this directory, serve files over a local HTTP server (a `file://` open may block JSON loading):

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/` and check search, zoom, labels, filter controls and side panel. The converter/upload controls are visually hidden in this static candidate; no ontology needs to be sent to an online converter. A formal browser QA record is still required before the candidate can be called usable.

## Build provenance

- Upstream viewer: `VisualDataWeb/WebVOWL@28e7dd9540622e8cb723dc000824b5eef5ae775f`, `v1.1.7`, MIT (`license.txt` preserved).
- In a disposable checkout, install with `npm install --ignore-scripts --legacy-peer-deps --no-audit --no-fund`; set `NODE_OPTIONS=--openssl-legacy-provider` and run `./node_modules/.bin/grunt release` (observed Node 24.19.0/npm 11.9.0). Install/build is a reproducibility recipe, not a claim that future transitive resolution is immutable; pin a lockfile/dependency digest for a release-bound build.
- Before build, change `src/app/js/loadingModule.js` default JSON name from `foaf` to `semrisk`; copy the exact combined JSON to `src/app/data/semrisk.json`; replace the demo ontology menu in `src/index.html` with SemRisk, add the candidate/source notice and hide the remote converter control. After build, omit demo data, hide direct input, and remove the absent favicon link. File SHA-256 values and sizes are in `manifest.json`.
- The source-bound converter method, the temporary IRI bridge and its limitations are documented in `../../diagrams/p1-r2-webvowl-conversion-decision-2026-09-27.md` and `tools/build_webvowl_candidate.py`.

## Release boundary

The repository remains private. This path is under `docs/ontology/generated/`, **not** the frozen `site/ontology/0.1.0-rc.1/` route. It is not deployed or publicly reachable as Pages. #119 owns rendered usability/omission QA and a separate route; #117 owns Pages QA/deployment; #55/#56 own release identity, licensing/privacy and public access. Preserve WebVOWL, D3 and bundled dependency notices during packaging.
