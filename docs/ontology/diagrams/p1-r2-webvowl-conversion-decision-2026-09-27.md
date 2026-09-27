# P1-R2 WebVOWL conversion decision and offline gate

**State:** offline conversion JSON and static WebVOWL viewer bundle produced; narrow desktop/mobile browser smoke passed, while graph readability and deployment remain open. Owner: #119. This is a derived view, not formal ontology authority or public Pages deployment. See [browser QA](p1-r2-webvowl-browser-qa-2026-09-27.md).

## Pinned upstream source choices

| Component | Release/tag | Immutable source commit | License evidence | Use |
| --- | --- | --- | --- | --- |
| OWL2VOWL | `0.3.7` (tag has **no** `v` prefix) | `VisualDataWeb/OWL2VOWL@2833ead00122ca252a0fd0e18c5e5b696d711d2c` | `LICENSE.txt` Git blob `b04cd03ac00b1570f1f56e0e80320abce747ed58` (MIT) | Local OWL → WebVOWL JSON conversion |
| WebVOWL | `v1.1.7` | `VisualDataWeb/WebVOWL@28e7dd9540622e8cb723dc000824b5eef5ae775f` | `license.txt` Git blob `6df36dbfe044376b68e8c9348cfcae0472623665` (MIT); `package.json` version 1.1.7 | Local static viewer candidate |

Upstream source and release tags were cross-checked at those commits. The locally built standalone JAR used in this check has SHA-256 `f61a49c9bfee60e0a3e02c23f780f3d07d7edaad5b1dd63ced2d4c4c292dc4a9` (Java 17 with `--add-opens java.base/java.lang=ALL-UNNAMED`, Maven 3.9.9, `package -P standalone-release -DskipTests`). It is **not** committed to SemRisk; a viewer distribution and its dependency/license inventory remain pending. No `master-SNAPSHOT`, floating CDN, online ontology upload or remote conversion service is a reproducible substitute.

## Exact SemRisk input boundary

- Candidate `P1-R2/0.1.0-rc.1`; six local Turtle modules plus vendored gUFO v1.0.0, resolved by `ontology/catalog-v001.xml` and enumerated in `docs/ontology/generated/p1-r2-closure-manifest.json`.
- Semantic source commit `c17cc111f02309270a60474623259cefcf907c6f`; generated asserted graph has 1,409 unique triples, SHA-256 `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`. This is an asserted union, **not** OWL inference.
- Local declaration denominator: 35 OWL classes, 37 object properties, four separate SKOS markers in `docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv`. Imported gUFO declarations have a separate denominator and should be filterable, not silently counted as local SemRisk classes.
- SHACL shapes, SPARQL rules, synthetic test individuals, SQL schemas and external-owner COVER/ROSE/CM-PharmE semantics are outside this WebVOWL input. The viewer must not invent them.

## Conversion result and compatibility finding

The exact `-file Core -dependencies gUFO` smoke run emitted **zero** SemRisk local classes/properties despite successful CLI exit; it showed vendor terms only. An isolated diagnostic using HTTP-shaped surrogate IRIs exposed the 26 Core classes and 29 Core object properties. In the generated-only adapter, seven catalog-bound asserted graphs are combined locally, `owl:imports` and original ontology-type triples are omitted from the derived conversion input, one derived view identity is inserted, and local `urn:` IRIs are temporarily mapped to `https://semrisk.invalid/` IRIs. After OWL2VOWL, those aliases are restored to canonical URNs throughout JSON. The seven original Turtle files are unchanged. This is a visualization bridge, **not** an alternate canonical OWL serialization or entailment closure.

`python tools/build_webvowl_candidate.py --jar <locally-built-shaded-jar>` generated `docs/ontology/generated/webvowl-candidate-v0.1/combined.json` and its `manifest.json`. A second `--check` reproduced the bytes exactly. The manifest records source/ref/blobs, conversion-input and output digests, 35/35 local class IRIs and 37/37 local object-property IRIs, and the private browser-smoke run. The four SKOS markers are outside the WebVOWL class/property denominator. The 1,394 conversion-input triples differ from the 1,409 asserted-source triples because import triples and original ontology-type declarations were removed and two derived view triples were added; the source graph itself remains unchanged.

## Remaining sequence and acceptance

1. The pinned WebVOWL source was built locally with Node 24.19.0/npm 11.9.0 and `NODE_OPTIONS=--openssl-legacy-provider grunt release`. A reduced static bundle at `docs/ontology/generated/webvowl-viewer-candidate-v0.1/` loads the exact JSON by default, includes upstream MIT license, source/formal links and a candidate notice. Its manifest records asset hashes and a passing private Chromium smoke with partial readability. A lockfile/transitive dependency license review remains for release-bound reproducibility.
2. Assess combined graph readability (108 class nodes and 212 property nodes in raw JSON, including imported/structural terms). Add module-scoped/filterable views if needed; clearly separate locally declared SemRisk nodes from referenced/imported gUFO nodes and generated structural stubs.
3. The private Chromium smoke now checks local JSON fetch, initially visible nodes, search entry, zoom transform, desktop/mobile canvas, JavaScript errors and outbound requests. Initial Google Fonts requests were removed from the bundled CSS. Continue with unsupported constructs, label/legend and target-reader usability, full privacy/license review, and exact 35/37 local IRI reconciliation after rendering rather than relying on raw JSON alone.
4. Move only a verified bundle to a new versioned candidate route, separate from frozen `site/ontology/0.1.0-rc.1/index.html`. #117/#55/#56 govern actual publication and public read-back.

**Current gate:** converter JSON and a locally servable static bundle exist in the private repository; narrow browser rendering passes, but combined/mobile readability, transitive licensing/privacy and deployment remain open. There is no public WebVOWL link yet. The existing source-derived SVG atlas and relation map remain available in the private repository.
