# SemRisk P1-R2 WebVOWL Explorer Candidate

Status: **OFFLINE CANDIDATE / NOT PUBLICLY DEPLOYED**

This record implements the offline portion of issue #119. WebVOWL is a derived
interactive exploration surface. It is not the semantic authority, not an
OntoUML model, and not evidence of formal completeness.

## Source binding

- Candidate: P1-R2 / 0.1.0-rc.1
- Canonical source commit: `dfdd7ca68c7fae460f5764afc8d9965aa00c20ae`
- Asserted import-closure SHA-256:
  `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`
- Asserted closure: 1,409 triples
- Local inventory: 35 OWL classes, 37 OWL object properties, 4 SKOS concepts,
  76 total local semantic IDs
- Full asserted import scope: 93 OWL class declarations and 77 object-property
  declarations, including vendored gUFO
- Canonical sources remain the six SemRisk Turtle modules and their governed
  external dependency binding. Generated VOWL JSON is never canonical.

## Pinned visualization toolchain

| Component | Pin | License | Role |
|---|---|---|---|
| WebVOWL | v1.1.7 / `28e7dd9540622e8cb723dc000824b5eef5ae775f` | MIT | Interactive viewer |
| OWL2VOWL | `c6331c4c79b0034b8537a11cccd1a6587cedb0b9` | MIT | Local OWL/RDF to VOWL JSON conversion |
| RDFLib | 7.6.0 | BSD-3-Clause | Deterministic input scoping and graph checks |

The build clones the exact OWL2VOWL commit inside the GitHub runner and posts
ontology files only to `127.0.0.1`. No SemRisk ontology is uploaded to a
third-party conversion service.

## Two explicit scopes

### Local SemRisk scope

The preferred reading view retains statements whose subjects are one of the 76
local SemRisk IDs, recursively preserves reachable blank-node expressions, and
adds labels only for explicitly referenced external boundary IRIs. It omits
`owl:imports` so imported declarations do not swamp the SemRisk graph.

Expected reconciliation after conversion:

- 35 local class IRIs with `SR-CPT-` identity
- 37 local object-property IRIs with `SR-REL-` identity
- 4 SKOS markers remain concept markers and are not reclassified as OWL classes

### Asserted import-closure scope

A second candidate preserves the complete 1,409-triple asserted import closure,
including gUFO. This is useful for foundational context but is intentionally not
the default SemRisk reading view.

Neither scope is an entailment closure.

## Reproducible build

The workflow `.github/workflows/paper1-webvowl-offline.yml`:

1. verifies the pinned asserted graph and inventory counts;
2. creates local-scope and import-scope Turtle inputs;
3. builds OWL2VOWL from the exact pinned commit;
4. converts both inputs through a localhost-only endpoint;
5. reconciles the produced VOWL JSON against 35 local classes and 37 local
   object properties;
6. builds WebVOWL v1.1.7 and smoke-tests the viewer;
7. freezes SHA-256 values for inputs, generated JSON, and manifest;
8. uploads an offline artifact named
   `semrisk-p1-r2-webvowl-offline-candidate`.

## Viewer capabilities and reading policy

WebVOWL supplies interactive zoom, search, labels, graph exploration and its
standard legend. The preferred local scope is designed to keep those features
usable without representing imported gUFO declarations as SemRisk-owned
semantics.

For source interpretation, use the curated FD-A–FD-J formal description and
the generated formal reference. For a static complete local inventory, use the
76-ID ontology atlas and the 37-property relation map.

## Candidate documentation route

Reserved route:

`/ontology-explorer/0.1.0-rc.1/`

This route is separate from the frozen
`/ontology/0.1.0-rc.1/` formal-reference route. No existing frozen page is
modified.

## Privacy, release and deployment boundary

The current candidate is offline-only. Public Pages deployment remains blocked
until #117, #55 and #56 settle access, licensing, release identity and
availability claims. A source-controlled site directory is not evidence that a
public Pages URL exists.

## Remaining acceptance work

- rendered desktop browser QA using the generated VOWL JSON;
- rendered mobile/readability QA and any required module-focused fallback;
- final public/private Pages access decision;
- publication-bound deployment and exact live URL read-back.

Until those checks pass, issue #119 must remain open and the explorer must be
described as an offline candidate.
