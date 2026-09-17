# SemRisk W0 Contract Validation — 2026-09-17

## Scope

This record validates the repository-level governance contract for **R-022 / SemRisk** against the current Portfolio and OGCM-RF bootstrap expectations. It does **not** claim ontology completeness, scientific validity, formal OGCM-RF conformance or publication readiness.

## Authoritative references checked

- `ArazSaieArasi3/araz-research-portfolio/portfolio-state/research-state.yaml` — R-022 is `SemRisk`, repository `ArazSaieArasi3/SemRisk`, lifecycle `Active`, priority `A`, current wave `W1 — Exhaustive Source Mining`, current gate `G1 — Source Completeness and Cross-Source Reconciliation`.
- `ArazSaieArasi3/OGCM-RF` main commit `4f2615dd76c302e080e69058f6237c0f82d56c4c`.
- `OGCM-RF/framework/ontology-repository-bootstrap.md`.
- `OGCM-RF/specification/implementation-profile.schema.json`, profile schema `1.0`.
- `OGCM-RF/specification/semantic-dependencies.schema.json`, dependency schema `1.0`.

## Validation method

The contracts were reviewed field-by-field against the current Portfolio template and OGCM-RF JSON schemas/bootstrap contract. No dedicated SemRisk-side automated schema-validation workflow is currently installed for these YAML contracts, and no dedicated OGCM-RF repository validator for `semantic-dependencies.yaml` was located during this gate. That automation gap is recorded rather than being treated as a hidden PASS condition; future CI may automate the same checks when SemRisk's semantic CI is activated.

## Contract checks

| Check | Result | Evidence / decision |
|---|---|---|
| Portfolio Research identity | PASS | `R-022`, `SemRisk`, P1/P1-L6 and repository identity agree with the current Portfolio projection. |
| Portfolio repository synchronization | PASS | Historical Portfolio synchronization debt via Portfolio Issue #141 is completed and removed from active SemRisk coherence debt. |
| Portfolio Manifest Contract 1.1 structure | PASS | `.research/manifest.yaml` remains schema/version `1.1` / template `1.1.0` and preserves the canonical Research identity. |
| OGCM-RF framework pin | PASS | SemRisk now pins current reviewed OGCM-RF main commit `4f2615dd76c302e080e69058f6237c0f82d56c4c` instead of the older August commit. |
| OGCM-RF implementation profile | PASS for repository contract | `.research/ogcm-rf-profile.yaml` remains profile schema `1.0` and records the current framework ref. Formal conformance deliberately remains `not_assessed`. |
| Semantic dependency contract | PASS with recorded validator limitation | `semantic-dependencies.yaml` now declares SemRisk canonical scope and required schema fields for explicit external ownership/dependency records. Automated YAML→JSON-Schema validation is not yet wired into SemRisk CI; this limitation is explicit. |
| Root README identity and owner boundary | PASS | README now states Portfolio, OGCM-RF, SemRisk and external-owner responsibilities and links the machine-readable dependency contract. |
| Semantic source-of-truth policy | PASS | README/profile explicitly distinguish W0/W1 evidence from future canonical SemRisk semantic registries/ontology source. |
| Core/Profile/external-owner boundary | PASS for W0 | Domain-general Core intent, first profiles, CM-PharmE external ownership and deferred dependencies are explicit. Final canonical architecture remains gated by G1/G2. |
| Migration/handover plan | N-A | No canonical SemRisk ontology is currently being migrated from another repository. Any later handover must use OGCM-RF migration controls. |
| Initial evidence baseline | PASS | Governed source register exists; operational Jira source is already SHA-bound/mined; standards/ontology/Pharma/dataset evidence remains W1 work. |
| Evidence-first next wave and gate | PASS | W1 evidence mining and hard G1 reconciliation remain authoritative; canonical conceptual/formal commitments remain blocked before the applicable gate. |
| Formal OGCM-RF conformance | NOT_ASSESSED | Contract presence is not treated as conformance. A future requirement-by-requirement assessment is required before changing this state. |
| Publication venue contract | OUTSIDE THIS GATE / OPEN | Stale venue assumptions were removed from README authority. Issue #38 must establish the current authoritative venue/deadline/template/page-limit contract. |

## Dependency policy decisions

1. **COVER** is a required reference/alignment dependency for Paper-1 Core reuse/novelty decisions, but its immutable release/commit and reuse/license status must be pinned under #14/#21 before release-bound claims.
2. **ROSE** is a conditional reference/alignment dependency where Security/treatment/prevention semantics overlap SemRisk; immutable ref remains unresolved until reuse adjudication.
3. **CM-PharmE** is a required federation dependency for the bounded Pharma case, but exact release/commit and bridge semantics remain work of #5.
4. **Newsium**, **Commentium**, **Business Ontology** and **Ontology Quality Framework** remain planned/deferred and do not block Paper 1 unless scope is formally reopened.

## Residual coherence debt

- Issue #38 must verify the actual Paper-1 venue contract from authoritative current sources.
- External ontology dependency refs/licenses must become immutable/release-bound before final mappings/releases.
- Formal OGCM-RF conformance remains `not_assessed`.
- Automated schema validation for the YAML contracts is not yet active in SemRisk CI; the current gate used direct schema/contract review.
- Canonical Core, UL, module architecture and formal ontology remain prohibited until G1/G2 allow them.
- Dataset/license/version qualification remains active W1 work.

## Gate decision

**W0 repository contract gate: PASS**

This PASS means only that Research identity, repository ownership, method binding, semantic dependency ownership and evidence-first gate sequencing are coherent enough to proceed. It does **not** imply scientific validity, ontology completeness, formal conformance, publication readiness or success of any later evaluation layer.

## Next mandatory sequence

`#38 Venue contract -> #39 Study design/evidence roles -> #1 RQs/contributions/nonclaims -> #40 reproducible search -> W1 evidence mining -> #18 G1`
