# SRC-PA-013 Deep Technical Profile — Unified Architecture for Risk Reasoning

**Source ID:** SRC-PA-013  
**Publication:** Stefano M. Nicoletti, *A Unified Architecture for Risk Reasoning: Bridging Ontologies, Theorem Proving, and Model Checking*, SAFECOMP 2026 Workshops (SENSEI), pp. 654–661, DOI `10.1007/978-3-032-35506-5_47`.  
**Mining date:** 2026-09-21  
**Status:** DEEP-PROFILED v0.1 — published bibliographic identity verified; accessible author/preprint text inspected.

## 1. Contribution

The paper proposes a high-level architecture for unifying heterogeneous safety/security risk-analysis formalisms through three coordinated layers:
1. ontology-grounded shared semantics;
2. deductive verification in an interactive theorem prover using a risk DSL;
3. automated model checking for suitable quantitative/algorithmic proof obligations.

The described prototype architecture uses Lean for deductive reasoning and Storm as an external model-checking engine/trusted oracle.

## 2. Semantic consequence for SemRisk

This establishes current prior art for the **architectural idea** of combining ontology-grounded risk semantics with theorem proving and model checking. SemRisk must not imply that combining ontologies with formal verification/automated analysis is itself novel.

However, the source is primarily a high-level risk-verification architecture, not an operational risk-register ontology. It does not displace SemRisk's candidate focus on information-artifact identity, assessment-result provenance, risk-state/workflow-state separation, governed source-to-claim traceability or ontology↔RDB projection fidelity.

## 3. Method consequence

For #23, this is a serious alternative method family. SemRisk must justify why its Paper-1 stack uses OWL/reasoning + SHACL + CQ regression + RDB parity for its bounded claims instead of claiming generic superiority over theorem proving/model checking.

## 4. Evaluation strength/boundary

The paper presents an architectural framework and integration direction. It should not be treated as evidence that every proposed interoperability/verification property has been empirically validated at operational scale unless a separate implementation/evaluation artifact is located.

## 5. Novelty impact

- SR-C1: no direct invalidation of the operational semantic-chain contribution.
- SR-C2: reinforces that formal/semantic integration with architecture models is prior art territory.
- Formal reasoning novelty: generic ontology + theorem-prover + model-checker integration is unavailable as a SemRisk novelty claim.
- Paper 1: comparator/method evidence, not a required SemRisk implementation target.

## 6. Downstream routing

- #14 closest work;
- #23 method selection;
- #26 formalization policy;
- #31 E10 comparison;
- #53 claim calibration.
## 7. Source-to-artifact binding and reproducibility — 2026-09-28

- The publisher landing page for DOI `10.1007/978-3-032-35506-5_47` describes the contribution as a **vision paper**, lists first online publication on 2026-09-03, and links the author's `lean-ufo` repository in a note: https://link.springer.com/chapter/10.1007/978-3-032-35506-5_47 . Its book citation uses 2027 while the associated SAFECOMP workshop is 2026; preserve both dates instead of silently normalizing the bibliography.
- Linked source artifact: https://github.com/smnicoletti/lean-ufo/tree/0f818fcfd54d53892041e74008556337ecd7bdb5 (immutable main snapshot, committed 2026-09-25). Repository license is AGPL-3.0. Its README and `docs/status.md` describe a Lean 4 UFO axiomatization, finite `ufo_model ... certify` DSL, generated Lean certificates, regression tests, and explicit trust/coverage limits. They report a 2026-09-17 local Lean/mathlib 4.34.0 test pass. This is author-linked **foundational/DSL artifact evidence**, not a verified end-to-end realization of the proposed risk architecture.
- The inspected recursive tree at that commit has 322 entries and no path named for Storm, risk, probabilistic reasoning, or model checking. This narrow observation does **not** prove such integration is absent in every branch, separate repository, private prototype, or future version. Exact risk-DSL bridge, Storm invocation, exchange format, run recipe, evaluated case set, and end-to-end result remain `UNKNOWN/NOT_REPORTED` in inspected sources.
- Version relation: published paper DOI ↔ author-linked evolving `lean-ufo` repository at the immutable commit above. No paper-specific release/tag or commit attribution was evidenced. Do not equate the later repository snapshot with the version used to produce the paper.
- Reuse implication: reference/compare only at present. AGPL-3.0 and the changing research version require a separate legal/dependency review before importing code. No semantic equivalence mapping follows from a shared UFO label.

**Qualification:** high confidence in publication identity and linked Lean UFO artifact; low/unknown confidence in an executable ontology→Lean→Storm risk pipeline or comparative operational evaluation. Keep #14 open for other comparator bindings and closest-work saturation.
