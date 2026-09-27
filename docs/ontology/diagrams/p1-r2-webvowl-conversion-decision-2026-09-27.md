# P1-R2 WebVOWL conversion decision and offline gate

**State:** source and tool versions selected; converter executable, generated JSON and rendered viewer not yet obtained/tested. Owner: #119. This is a candidate derived view, not the formal ontology authority or a public Pages deployment.

## Pinned upstream source choices

| Component | Release/tag | Immutable source commit | License evidence | Use |
| --- | --- | --- | --- | --- |
| OWL2VOWL | `0.3.7` (tag has **no** `v` prefix) | `VisualDataWeb/OWL2VOWL@2833ead00122ca252a0fd0e18c5e5b696d711d2c` | `LICENSE.txt` Git blob `b04cd03ac00b1570f1f56e0e80320abce747ed58` (MIT) | Local OWL → WebVOWL JSON conversion |
| WebVOWL | `v1.1.7` | `VisualDataWeb/WebVOWL@28e7dd9540622e8cb723dc000824b5eef5ae775f` | `license.txt` Git blob `6df36dbfe044376b68e8c9348cfcae0472623665` (MIT); `package.json` version 1.1.7 | Local static viewer candidate |

Upstream source and release tags were cross-checked at those commits. A built JAR or distributable viewer bundle is a **different artifact**: its SHA-256, dependency tree and included license text must be recorded before use. No `master-SNAPSHOT`, floating CDN, online ontology upload or remote conversion service is a reproducible substitute.

## Exact SemRisk input boundary

- Candidate `P1-R2/0.1.0-rc.1`; six local Turtle modules plus vendored gUFO v1.0.0, resolved by `ontology/catalog-v001.xml` and enumerated in `docs/ontology/generated/p1-r2-closure-manifest.json`.
- Semantic source commit `c17cc111f02309270a60474623259cefcf907c6f`; generated asserted graph has 1,409 unique triples, SHA-256 `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`. This is an asserted union, **not** OWL inference.
- Local declaration denominator: 35 OWL classes, 37 object properties, four separate SKOS markers in `docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv`. Imported gUFO declarations have a separate denominator and should be filterable, not silently counted as local SemRisk classes.
- SHACL shapes, SPARQL rules, synthetic test individuals, SQL schemas and external-owner COVER/ROSE/CM-PharmE semantics are outside this WebVOWL input. The viewer must not invent them.

## Conversion sequence and acceptance

1. Acquire the pinned OWL2VOWL executable and viewer bundle; record SHA-256, dependencies, source/asset licenses and exact build commands. Keep the private ontology local.
2. In a network-isolated process, try the official `java -jar <pinned-jar> -file <local-module.ttl> -dependencies <other-local-modules-and-gufo.ttl>` form, starting with Core. The upstream README documents `-file` and `-dependencies`; the actual import resolution for this catalog is **unproven**. Record errors and do not silently fall back to remote IRIs.
3. Convert each of the six modules with local dependencies if Core succeeds; choose separate module views when a combined gUFO graph is unreadable. Preserve a deterministic input list, command, tool hashes, JSON hashes and omission register. Check all 35 class and 37 property IRIs against source inventory; treat missing or unsupported constructs as findings.
4. Build a new candidate route, separate from frozen `site/ontology/0.1.0-rc.1/index.html`. Test search, zoom, labels, legend, desktop/mobile use, static links, privacy and rendering. Link canonical OWL, FD-A…FD-J, version registry and limitations. #117/#55/#56 govern publication and public read-back.

**Current gate:** steps 1–4 remain open. The source pin resolves a version-selection ambiguity, but neither a JSON output nor a WebVOWL link exists yet. The existing source-derived SVG atlas and relation map remain available in the private repository.
