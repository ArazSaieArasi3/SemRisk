> **Current-control notice — 2026-10-04:** the historical release identities and gate rules below remain useful, but their dated execution snapshot and ICAE destination are superseded by the [revision status](../execution/2026-10-04/status.md) and [ICAEA SBU venue contract](../../publications/2026-icaea-sbu/venue-contract.md). A new revision must revalidate affected evidence; historical closure is not automatic acceptance of the revised candidate.

# SemRisk Paper 1 Release Train

**Research:** R-022 / SemRisk
**Defined:** 2026-09-21
**Status:** ACTIVE PLANNING CONTRACT

## 1. Why this release train exists

SemRisk previously had waves/gates and release-policy issues, but no explicit ordered release train tying backlog completion to concrete reviewable deliverables. This document defines planning releases without prematurely assigning semantic-version numbers. Formal version/IRI semantics remain owned by Issue #43.

Planning IDs are stable backlog coordination identifiers. They are not yet ontology version IRIs or Git tags.

## 2. Release train

| Planning release | Exit gate / trigger | Primary content | What it authorizes | What it does NOT authorize |
|---|---|---|---|---|
| **P1-R0 — Evidence Baseline** | #18 G1 PASS/CONDITIONAL_PASS | governed source registry; search/screening/snowballing; standards/framework evidence; closest-work profiles; Pharma/Health evidence; dataset qualification/schema/role/quality records; reconciliation snapshot | start evidence-grounded W2 conceptual freeze work | no canonical Core/UL/formal ontology claim while affected evidence remains unresolved |
| **P1-R1 — Conceptual Baseline** | #24 G2 PASS | UL/conflict registry; semantic requirements/CQs; Core concepts; relations/events/states; reuse/alignment decisions; differentiation matrix; selected method profile; CM-PharmE bridge boundary; module/profile architecture | begin foundational/formal implementation against a frozen conceptual architecture | no claim that OWL/SHACL implementation or application projection is validated |
| **P1-R2 — Semantic Candidate** | W3 completion / #44 deterministic pipeline PASS for candidate | UFO/OntoUML analysis; formalization policy; stable IDs/IRI policy; modular OWL/RDF; SHACL/rules; deterministic build/reasoning/regression pipeline | create an exact formal candidate for executable application and later evaluation | no publication-validity or domain-validity claim |
| **P1-R3 — Executable Candidate** | #49 projection/parity evaluation complete for selected tasks | Pharma case package; ontology-grounded RDB design; PostgreSQL twin; governed data load; end-to-end scenario; SQL↔SPARQL parity/projection-loss evidence | start full W4 claim-dependent evaluation on an executable bounded candidate | no final assurance/publication binding |
| **P1-R4 — Evaluated Release Candidate** | #54 G4 PASS/CONDITIONAL_PASS with no publication-blocking Critical finding | negative-control results; E1–E11 evidence; expert/semantic validation; CQ regression; threats snapshot; claim calibration; integrated assessment/assurance | freeze the evaluated candidate eligible for publication binding | not yet the immutable scholarly release cited by the manuscript |
| **P1-R5 — Publication-Bound Scholarly Release** | #55 completed after #54 | exact semantic artifacts; mappings; RDB/data refs; CQ/tests; evaluation package; claims/nonclaims; checksums; tool versions; reproducibility manifest | bind Paper 1 figures/tables/manuscript/results to one reconstructable SemRisk state | does not itself authorize conference submission; #35 G5 does |

## 3. Submission package

**P1-S1 — Submission Package** is a publication delivery package, not a semantic release. It is authorized only by #35 G5 PASS and contains the exact manuscript revision, bibliography, figures/tables, declarations and P1-R5 release reference submitted to ICAE 2026.

## 4. Backlog mapping

### P1-R0
#40, #12, #13, #14, #15, #4, #16, #17, #41, #42, #18.

### P1-R1
#19, #7, #3, #20, #21, #22, #23, #5, #24.

### P1-R2
#25, #26, #43, #27, #44.

### P1-R3
#28, #45, #46, #47, #48, #49.

### P1-R4
#50, #29, #51, #30, #52, #31, pre-assurance #56, #53, #54.

### P1-R5
#55 plus final availability/integrity refresh under #56.

### P1-S1
#32, #33, #34, #35.

## 5. Release rules

1. A release planning ID cannot be marked complete merely because all mapped issues are closed; its exit gate must be satisfied.
2. A later release inherits earlier evidence only when no impacted invariant has changed or an explicit regression/reassessment confirms transfer.
3. Critical evidence gaps may result in CONDITIONAL_PASS only when the affected claim is explicitly prohibited/narrowed and the gate contract permits it.
4. P1-R0 and P1-R1 are research/conceptual baselines, not public semantic ontology releases.
5. P1-R2 and later must bind exact commit/build/artifact identities.
6. P1-R4 is an evaluated release candidate, not a publication-bound release.
7. P1-R5 is the only Paper-1 scholarly release intended to be cited as the exact evaluated SemRisk state.
8. Semantic version names, ontology/version IRIs, tags and deprecation rules are finalized by #43; this release train must not preempt them.
9. P1-S1 may be regenerated only from the same P1-R5 or from a formally re-bound successor after impact review.
10. Post-Paper1 Newsium/Commentium/Risk Intelligence/OQF work is outside this train unless a formal re-scope decision is made.

## 6. Current state

- P1-R0: **COMPLETE / CONDITIONAL_PASS** — #18 G1 closed with bounded source-mining debt.
- P1-R1: **COMPLETE / PASS_FOR_FORMALIZATION** — #24 G2 closed and its foundational condition was cleared by #25.
- P1-R2: **COMPLETE / REPRODUCIBLE_SEMANTIC_CANDIDATE** — #25/#26/#43/#27/#44 complete; application projection and independent evaluation remain later gates.
- P1-R3: **IN PROGRESS** — #28 bounded Pharma case complete; #45–#49 relational/application projection sequence remains.
- P1-R4: BLOCKED by executable candidate.
- P1-R5: BLOCKED by G4.
- P1-S1: BLOCKED by P1-R5 and G5 requirements.

## 7. GitHub milestone note

At definition time, the SemRisk issues inspected have no GitHub milestone assigned. The current connector exposes issue milestone assignment but does not expose milestone creation, so this document and MASTER #8 are the authoritative release-train mapping until milestones are created through GitHub UI or another supported action.
## 8. Formal identity/version integration — #43

- Planning release IDs remain gate/work-package identities, not ontology semantic versions.
- P1-R1 conceptual package is `conceptual v0.1.0`.
- First P1-R2 formal ontology/shapes/mapping candidate starts at `v0.1.0-rc.1` unless #27 documents a prior governed formal version.
- Component versions are independent: ontology, SHACL, mappings, rules, projection, datasets and evaluation can change separately.
- Internal formal IRIs use repository-independent `urn:semrisk:*` namespaces until a persistent HTTPS resolver is actually configured and tested.
- P1-R2 and later release bundles must bind exact component versions, Git SHAs, checksums and external refs.
- Publication does not automatically make the ontology `1.0.0`; P1-R5 binds the exact evaluated semantic version that actually exists.
