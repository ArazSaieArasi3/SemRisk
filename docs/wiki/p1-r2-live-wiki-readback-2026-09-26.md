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

**Navigation/render checks:** Home lists all seven published pages and the Wiki sidebar lists eight pages. Home → Scope opened. All seven subpage return links target Wiki Home. The Semantic Architecture atlas link at exact commit `2786302451c948106ec0df413d771ef0dff712f2` opened GitHub's SVG preview. The seven Home URLs and seven return URLs were inspected in the rendered UI. These checks do not claim a full external-link crawl, independent accessibility review or unauthenticated public access.

**Rollback/read-back:** Home history at `https://github.com/ArazSaieArasi3/SemRisk/wiki/Home/_history` shows latest `d23cb7807bcb2aaa8585ffeaaf8aec5e7501e823`, previous curated `99aa2c66b25178d8c0abc135be7169aa1a724d87`, and original placeholder `12bc844a1e40716b8c15908405f802e81c173d7c`. The original was preserved in history. This records a recovery route; no rollback was executed.

**Automated source checks:** Wiki manifest run `36240700066`, Wiki formal parity run `36240700096`, and offline Pages reference run `36240700105` succeeded at `84b2a7f3`. They validate their scoped source artifacts, not the live Wiki or deployed Pages.

**Access/release boundary:** The Wiki belongs to a private repository. Its signed-in view was verified; public Pages is not deployed. The Wiki's candidate banners retain #51/#31/#53/#54/#55/#56 limitations. A future source edit, Wiki edit, semantic candidate change, Pages deployment, access change or release binding requires a fresh source hash, rendered link and history read-back. Generated reference/WebVOWL remains a Pages concern under OGCM-RF; no WebVOWL view is claimed here.
