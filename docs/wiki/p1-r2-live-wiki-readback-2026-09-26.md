# SemRisk P1-R2 Wiki live read-back — 2026-09-26

**Scope:** private, signed-in GitHub Wiki candidate, eight pages. **Repository source:** commit `84b2a7f3b237f6a2cd6509e7f4bee14b57aefd38`, manifest `docs/wiki/p1-r2-wiki-publish-manifest-v0.1.json`. This is documentation publication, not the #55 scholarly release, #54 assurance or #56 public-access decision.

## Source ↔ live Wiki content

The live Wiki editor's Markdown body was read back for each page in a signed-in browser session. A single trailing newline was restored after the accessibility representation, and SHA-256 was computed over UTF-8. Each digest equals the source manifest's byte digest. Navigation was reconciled in source to the actual published absolute Wiki page URLs; no other source-page text changed in that reconciliation commit.

| Page | Source and live SHA-256 | Result |
|---|---|---|
| Home | `db3dde4b4f96d9e40f50d7542d920622e9ad154624f5776ef4c9cc0e9e6f5bfa` | MATCH |
| Scope-and-Contributions | `1eb9f802b82ab55a1bb555c2edd2b854e7a6cf3af848918595e2b5621e24fd6b` | MATCH |
| Semantic-Architecture | `91fc4063e66fed0b6471e1db44b33423b59264a7ce9c40192d7e8309f68726b7` | MATCH |
| Formal-Reference | `b29afd5a34783146859ba8b560a527078d4b712eeb8b03dcfd89815d267d3121` | MATCH |
| Evidence-and-VVEAA | `8b9c968ad7f2edafb81c738356938d0f691ed9405fa47b716d5f78697c99311e` | MATCH |
| Relational-Projection | `492ff0a53b211b7eb2e1be71e3e29d3b71586b02318c7b38694820ec03918feb` | MATCH |
| Pharma-Case | `55b9fa2f2dc4c52bb35cbf72e6aeed4d377f440135ba0502779603c28c0c359a` | MATCH |
| Reproduce-and-Release | `16417efefff77860216c6638a1b3e984c1e4d3493d16d9aaeac8ba301132ac09` | MATCH |

**Navigation/render checks:** Home lists all seven published pages and the Wiki sidebar lists eight pages. Home → Scope opened. All seven subpage return links target Wiki Home. The Semantic Architecture atlas link at exact commit `2786302451c948106ec0df413d771ef0dff712f2` opened GitHub's SVG preview; the 37-property relation map also opened GitHub's SVG preview. The seven Home URLs and seven return URLs were inspected in the rendered UI. All 30 distinct exact-commit repository file targets used by the eight pages were fetched successfully through the connected GitHub repository API (35 link occurrences). This checks target existence at pinned refs, not every browser rendering mode. Independent accessibility review and unauthenticated public access are not claimed.

**Rollback/read-back:** Home history at `https://github.com/ArazSaieArasi3/SemRisk/wiki/Home/_history` shows latest `d23cb7807bcb2aaa8585ffeaaf8aec5e7501e823`, previous curated `99aa2c66b25178d8c0abc135be7169aa1a724d87`, and original placeholder `12bc844a1e40716b8c15908405f802e81c173d7c`. The original was preserved in history. The previous curated revision was opened and read back with its original relative links. This demonstrates readable historical content and a recovery route; no rollback was executed.

**Automated source checks:** Wiki manifest run `36240700066`, Wiki formal parity run `36240700096`, and offline Pages reference run `36240700105` succeeded at `84b2a7f3`. They validate their scoped source artifacts, not the live Wiki or deployed Pages.

**Access/release boundary:** The Wiki belongs to a private repository. Its signed-in view was verified; public Pages is not deployed. The Wiki's candidate banners retain #51/#31/#53/#54/#55/#56 limitations. A future source edit, Wiki edit, semantic candidate change, Pages deployment, access change or release binding requires a fresh source hash, rendered link and history read-back. Generated reference/WebVOWL remains a Pages concern under OGCM-RF; no WebVOWL view is claimed here.

## Audience-route refresh — 2026-09-26

Source-controlled Home and its publication manifest were updated atomically at [commit 8f71a75](https://github.com/ArazSaieArasi3/SemRisk/commit/8f71a75d9aa4fbe013c78f5a1122d7277ed47a1d). Home source SHA-256 is `63e921e4c950a7d95252b8aeaa4f2462265208056c118c05446265324a4adba6`. The signed-in Wiki Home editor displayed the exact source body (terminal newline included) after save; rendered Home showed distinct research/review and ontology/data-engineering routes, their existing seven Wiki page destinations, the candidate/nonclaim banner and eight-page sidebar. History shows new revision `9827a5211d864bc1b6a2eda587ca5741a2f64f0f` and retains `d23cb7807bcb2aaa8585ffeaaf8aec5e7501e823` as the immediately previous Home revision. No rollback was performed.

The source manifest, formal parity guard and offline Pages builder passed locally on this change. This check is for the private signed-in Wiki Home and source parity; no public or mobile usability claim, independent editorial QN/QL score, or Pages deployment is inferred. Next publication baseline requires a fresh read-back.

## Research-journey refresh — 2026-09-26

Source-controlled Scope-and-Contributions, Wiki manifest and navigation guard changed atomically at [commit 84bc224](https://github.com/ArazSaieArasi3/SemRisk/commit/84bc2241ebc3b29daedd30742867853010b8e1b4). Source SHA-256 is `b1501356ceb0a1e6e53a94965e38079dbefcd6b3485677fdc68b840a6bce37cc`. The signed-in editor body matched the source Markdown including terminal newline. The rendered page displayed four evidence→boundary→model→check→claim steps, the limits and the return link; the eight-page sidebar remained intact. History revision `f9e6b60c2d2b990df7cf040e0fc6a6aee0d13cc9` retains prior `d8df8b05afd87ae1611dfba55a82ad391f66ab5c`. The two new exact-commit file links (candidate manifest and release train) were fetched at their pinned ref; the four issue links and VVEAA Wiki route were observed in the rendered page.

Local Wiki source, formal parity and offline Pages checks passed after the guard permitted a same-Wiki cross-link while continuing to require every subpage's Home return link and only known Wiki destinations. This is a bounded research route, not an entity-level version lineage or completed editorial/semantic review.
