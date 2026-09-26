# SemRisk Paper-1 Wiki source map — P1-R2 v0.1

**Issue:** #116. **State:** source-controlled navigation draft; no claim that the GitHub Wiki has been populated or rendered. **Candidate:** P1-R2 / `0.1.0-rc.1`. The final publication identity is pending #55. This page is a curation map; OWL/SHACL/rules and governed evidence remain authoritative.

| Proposed Wiki page | Purpose | Canonical repository source | Publication rule |
| --- | --- | --- | --- |
| Home | Start Here, scope, current status | [README](../../README.md); [release train](../governance/paper1-release-train.md) | Mark author-review and release gates explicitly. |
| Scope-and-Contributions | Bounded claims and nonclaims | [claim calibration](../../publications/2026-icae/claim-calibration-preliminary-v0.1.csv); [manuscript v0.3](../../publications/2026-icae/manuscript-working-draft-v0.3.md) | Never imply final #53/#54 assurance. |
| Semantic-Architecture | Core versus profiles; external-owner boundaries | [formal description FD-B/C](../ontology/formal-ontology-description-p1-r2-v0.2.md); [figure candidate](../../publications/2026-icae/paper1-core-distinction-figure-v0.1.md) | Selected figure is not exhaustive. |
| Formal-Reference | FD-A…FD-J interpretation, limitations | [formal description](../ontology/formal-ontology-description-p1-r2-v0.2.md); [source entity inventory](../ontology/p1-r2-formal-source-entity-reference-v0.1.csv) | Link to semantic files; do not mirror mutable axioms as a second authority. |
| Evidence-and-VVEAA | Methods, observed results and pending gates | [execution profile](../../evaluation/vveaa/paper1-vveaa-execution-profile-v0.1.md); [results table](../../publications/2026-icae/paper1-vveaa-results-table-v0.1.md) | Keep human E5 and independent E11 as pending. |
| Relational-Projection | PostgreSQL projection and exact task scope | [relational manifest](../governance/relational-twin-v0.1.0-rc.1-manifest.md); [SQL README](../../relational/sql/README.md) | 8/8 is for eight declared tasks, not global equivalence. |
| Pharma-Case | DS-003 constructed context and synthetic fixtures | [transformation specification](../../case/pharma/pharma-case-transformation-spec-v1.1.md); [manuscript case section](../../publications/2026-icae/manuscript-working-draft-v0.3.md) | Do not publish protected rows; distinguish source from synthetic execution. |
| Reproduce-and-Release | Build, version, access and citation | [semantic build](../reproducibility/semantic-build.md); [release train](../governance/paper1-release-train.md) | Final public release URL and exact citation wait for #55/#56. |

The linked repository paths were inspected or created on 2026-09-26; this verifies source-path existence, **not** Wiki publication or rendered link behavior. Relative links are valid in this repository document; published Wiki pages must use version-specific canonical repository URLs because Wiki relative paths resolve differently.

## Proposed Home page copy

**SemRisk** is a modular semantic architecture for operational risk knowledge. Its Paper-1 candidate distinguishes risk phenomena from register records, possible scenarios from realized events, assessment activities from results, and modeled risk states from workflow states. The current P1-R2 candidate has bounded formal and application evidence; independent human semantic validation, an independent E11 shortage-domain holdout, final comparative calibration, assurance and publication release are pending. Start with the semantic architecture and formal description, then inspect the VVEAA result table, relational projection, Pharma case and release state through the source links in this map.

## Synchronization gate before Wiki publication

1. Inspect whether GitHub Wiki is enabled, private/public, empty or prepopulated; preserve existing pages and revisions.
2. Convert each source link to an exact canonical URL and record the P1-R2 commit/release ref per page.
3. Publish pages only from this map, then verify navigation, Mermaid/SVG rendering and link targets in a signed-in session.
4. Check critical IDs `SR-CPT-001`, `SR-CPT-006`, `SR-CPT-007`, `SR-CPT-033`, `SR-CPT-035`, `SR-CPT-036` against source and generated reference; log drift.
5. Retain a rollback revision and flag any change in semantics, evidence, private/public access or #55 release identity.

**Boundary:** the Wiki is a readable entry point, not the semantic source or scholarly release.

## Source-controlled page drafts — 2026-09-26

Eight curated drafts are now tracked under `docs/wiki/pages/`: [Home](pages/Home.md) · [Scope-and-Contributions](pages/Scope-and-Contributions.md) · [Semantic-Architecture](pages/Semantic-Architecture.md) · [Formal-Reference](pages/Formal-Reference.md) · [Evidence-and-VVEAA](pages/Evidence-and-VVEAA.md) · [Relational-Projection](pages/Relational-Projection.md) · [Pharma-Case](pages/Pharma-Case.md) · [Reproduce-and-Release](pages/Reproduce-and-Release.md). Their initial canonical source links pin `b9217100a4342fc61f0fedb19513126028f55370`; the Formal-Reference page additionally pins the generated asserted reference to `dfdd7ca68c7fae460f5764afc8d9965aa00c20ae`. All eight draft files, local navigation targets and pinned source paths were checked against the repository tree at that ref. The drafts contain no protected raw Jira rows; their status text retains the open human E5, independent E11, assurance and release gates.

**Publication checkpoint:** Wiki live content, access, page rendering, drift and rollback remain unverified. The repository metadata reports `has_wiki: true`, which establishes availability of the feature but not the state of any live Wiki pages. Do not mark #116 complete until the live state is inspected and the synchronization gate above is executed.
