# Issue #52 — Competency Question Regression Report

**Candidate:** SemRisk P1-R2 / ontology 0.1.0-rc.1  
**RDB:** 0.1.0-rc.1  
**Data:** P1-DATA-0.1.0-rc.1  
**Scenario:** E2E v1.0

## Denominator
The original registry contains **40** CQs. CQ-039 is explicitly deferred from Paper 1, leaving **39 Paper-1-applicable CQs**.

Current disposition:
- executable: **26/40** (65.0% total; 66.7% of applicable)
- partially executable: **7/40** (17.5% total; 17.9% of applicable)
- conceptual-only: **6/40** (15.0% total; 15.4% of applicable)
- deferred: **1/40** (2.5%)
- failed: **0**

These are executability states, not quality scores. Conceptual-only does not mean failed, and an executable query does not establish domain validity.

## Semantic evaluation
All 39 Paper-1-applicable CQs retain their original expected capability from #7 and have a current PASS, PASS_PARTIAL or PASS_CONCEPTUAL disposition. No CQ was deleted or rewritten after execution to improve the result.

The strongest executable evidence is concentrated in the Paper-1 distinctions exercised by #48–#50: risk/record identity, scenario/event/description, assessment activity/result, inherent/residual context, state-family separation, responsibility-derived ownership, treatment distinctions, provenance, external Pharma ownership and reassessment.

## Material partials
- CQ-006: method is not populated in the bounded executable assessment fixture.
- CQ-012: Risk Source and evidence-governed causal-vs-association assertion are not fully exercised end-to-end.
- CQ-013: external federation is executed for CM-PharmE, not the Objective/Capability/Process path.
- CQ-028: causal/association predicates are distinguished, but no empirical causal assertion is introduced.
- CQ-035: operational↔Pharma comparison is bounded mapping evidence, not independent transferability.
- CQ-037: trace reaches executable tests but final manuscript claim linkage awaits #53 and manuscript issues.
- CQ-038: multiple assessments are executable; multiple record versions are not fully instantiated.

## Conceptual-only items
CQ-002, CQ-004, CQ-017 and CQ-019 remain release-relevant conceptual tests whose semantics are represented but whose specific multiplicity/method fixtures are not currently executed. Optional CQ-030 and CQ-032 also remain conceptual-only.

## Regression governance
Semantic changes are covered by Semantic CI and #50 mutation controls. RDB/scenario/mapping changes are covered by the relational CI, #49 parity harness and #50 cross-layer mutation controls. The exact execution evidence is therefore version-bound and repeatable.

## Claim boundary
This result supports semantic requirement/CQ traceability and bounded executable answerability. It does not replace expert/domain validation (#51/#30), transferability evaluation (#31), or final claim calibration (#53).
