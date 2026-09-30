# P1-R2 public Wiki access and source parity — 2026-09-30

**Trigger:** SemRisk repository visibility changed to `public` after the earlier private-Wiki baseline. **Candidate:** P1-R2 / `0.1.0-rc.1`. This is a documentation access and status correction, not #54 assurance or the #55 publication-bound release.

## Access and publication

- GitHub repository metadata reported `private=false`, `visibility=public`, `has_wiki=true`, `has_pages=false`, `license=null` on 2026-09-30. An unauthenticated Git read of `SemRisk.wiki.git` returned the Wiki head; public Git access was verified independently of the signed-in Wiki editor.
- All eight status banners now say repository and Wiki are publicly readable, while final scholarly release, artifact availability and citation remain pending #55/#56. The Scope page removes closed #14 from its pending list and retains #31's separate comparator impact review.
- Wiki publication used GitHub's signed-in page editor and preserved each page's history. The rendered Home and Scope routes, status text and Scope gate wording were read back; the remaining six rendered pages were checked for the new status text after save. Wiki `master` read-back revision: `f548d865885f74b39b20bbf055280af9f08eb136`.

## Exact page parity

The public Wiki Git revision above was fetched after the eight saves. Each UTF-8 page body SHA-256 equals both the source file and `docs/wiki/p1-r2-wiki-publish-manifest-v0.1.json` in this documentation change.

| Page | SHA-256 | Result |
| --- | --- | --- |
| Home | `fc5b5ab48dca8b1e47568571dc1a913ac5cd5a91f4da40417c41a1d5bd3f8282` | MATCH |
| Scope-and-Contributions | `6bd5d029a2fb08f1dc7046ec7b2dd0a19f1dd589d513355fda04670d956d3202` | MATCH |
| Semantic-Architecture | `a18e4690b66cb5d66b74492cd6a91a5f30789191e92113891f6b75e2e46f1fd0` | MATCH |
| Formal-Reference | `3b920a622cf57f8e1fa6ad34e5a5d90726f08bb3f2b3b15cf3e0cfc6a4f66deb` | MATCH |
| Evidence-and-VVEAA | `562ad89d5089cf3e5ee23f2ccdeb26b13b7a69de9261b981ca600bf3c1902882` | MATCH |
| Relational-Projection | `196d1db477fedaa753e94777d0d1a1731bfcb4346852b67309964597eb47aae4` | MATCH |
| Pharma-Case | `718d46c1f2368a8b2297c1388b9393cb17d52f7cef865a2365e0ada56b402996` | MATCH |
| Reproduce-and-Release | `c00c70f74d3fa8ace90889e8e6602e6481d7ebbd7a43607dde4436f6e5b56231` | MATCH |

The source guard verifies page set, exact source hashes, allowed navigation and candidate/nonclaim banners. This read-back does not establish independent user accessibility or all outbound links at the new public baseline. A browser reader exercise remains #122; citation/source and human-dependent editorial review remain #121.

## Pages and release boundary

Public repository visibility does not enable GitHub Pages. The versioned formal reference and WebVOWL remain offline candidates under #117/#119, with no verified public diagram URL. #56 must review already public repository/history and the exact deployable artifact's privacy and third-party license notices; #55 still owns release/citation binding. The absence of a repository-level license cannot be interpreted as a reuse grant. The next deployment step is to resolve these gates, enable Pages for an explicitly selected source and verify the rendered versioned URL before adding Wiki backlinks.
