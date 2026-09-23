# SemRisk Version and Release Policy v1.0

**Frozen:** 2026-09-23

## 1. Independent versioned artifact families
SemRisk versions the following independently:
- `conceptual` — UL/concepts/relations/foundational decisions;
- `ontology` — OWL/RDF modules;
- `shapes` — SHACL package;
- `mappings` — external/data mapping package;
- `rules` — executable method/application rules;
- `projection` — relational schema/migrations;
- `dataset-binding` — exact dataset/file/schema/checksum package;
- `evaluation` — tests/results/assurance package;
- `release-bundle` — manifest binding all components for a planning release;
- `submission` — manuscript delivery package.

## 2. Semantic versioning
Machine semantic artifacts use SemVer syntax. Before a stable 1.0 declaration, formal candidates begin at `0.1.0-rc.1`.
- `PATCH`: editorial/metadata/build correction with no intended semantic entailment/constraint change.
- `MINOR`: additive compatible semantic capability or a pre-1.0 breaking semantic change. The manifest must always state `change_class` explicitly.
- `MAJOR`: breaking semantic change after a stable 1.x release.
- prerelease identifiers (`-rc.N`, `-dev.N`) distinguish candidates from stable releases.

Because SemVer is less informative before 1.0, every release manifest also declares one of: `NON_SEMANTIC`, `EVIDENCE_ONLY`, `ADDITIVE_COMPATIBLE`, `DEPRECATION_COMPATIBLE`, `BREAKING_SEMANTIC`, `CONSTRAINT_CHANGE`, `PROJECTION_ONLY`, `EVALUATION_ONLY`.

## 3. Planning release vs component versions
`P1-R0`…`P1-R5` remain research planning/gate identifiers. They are never substituted for ontology versions.
- P1-R0: evidence baseline; no ontology version.
- P1-R1: conceptual baseline; conceptual package v0.1.0.
- P1-R2: first formal candidate; ontology/shapes/mappings start at v0.1.0-rc.1 unless an earlier governed formal version exists.
- P1-R3: executable bundle; ontology may remain unchanged while projection/dataset components gain their own versions.
- P1-R4: evaluated release candidate; binds exact evaluated component versions.
- P1-R5: publication-bound scholarly bundle; may cite ontology 0.x or 1.x. Publication does **not** automatically promote ontology to 1.0.

## 4. Git tags
Tags are immutable distribution refs, not semantic identity. Naming:
- component tag: `<component>-v<semver>` (example `ontology-v0.1.0-rc.1`);
- release-bundle tag: `p1-r<stage>-<ordinal>` (example `p1-r5-1`).
A moved/reused tag invalidates its release binding and must never be silently repaired.

## 5. Repository commit binding
Every candidate/evaluated/publication release records a full 40-character Git commit SHA and artifact checksums. Commit SHA is provenance/build identity, not ontology IRI.

## 6. Evaluation reuse
- `NON_SEMANTIC` / `EVIDENCE_ONLY`: prior formal test evidence may transfer if inputs are unaffected and manifest records the reuse rationale.
- `ADDITIVE_COMPATIBLE`: rerun impacted tests; unaffected evidence may transfer only by impact analysis.
- `DEPRECATION_COMPATIBLE`: rerun identifier/mapping/CQ tests involving deprecated entities.
- `BREAKING_SEMANTIC` / `CONSTRAINT_CHANGE`: affected formal/CQ/application/evaluation evidence does not transfer automatically.
- `PROJECTION_ONLY`: ontology evidence may transfer, but parity/RDB/application evidence must rerun.

## 7. Publication binding
P1-R5 is one immutable manifest, not a branch. Any post-evaluation semantic change creates a successor release and reopens impacted assurance before manuscript rebinding.