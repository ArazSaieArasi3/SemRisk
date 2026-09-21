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