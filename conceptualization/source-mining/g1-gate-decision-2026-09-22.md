# G1 Gate Decision — P1-R0 Evidence Baseline

**Date:** 2026-09-22
**Issue:** #18
**Decision:** `CONDITIONAL_PASS`

## Gate scope

This decision applies only to the bounded ICAE 2026 Paper-1 claim boundary frozen under #1. It authorizes W2 conceptual synthesis; it does not canonize any concept, relation, module, OWL artifact or publication claim.

## Evidence baseline

- Governed source register: **50 sources**.
- Broad search execution: #40 **PASS / CLOSED**.
- Raw concept-bearing extraction baseline: **274 rows** across five deeply mined source families.
- Row-level dispositions: **274/274 assigned**.
- Consolidated provisional candidates: **191 unique normalized candidates**.
- Relation/event/state/activity provisional candidates: **175 rows**.
- Cross-source reconciliation: 15 backbone clusters.
- Semantic conflict register: 13 major conflicts, all given explicit noncanonical G1 resolutions.
- Source coverage snapshot: 27 `ADEQUATE_FOR_G1`, 11 `BOUNDED_PENDING`, 10 `BOUNDED_OR_DEFERRED`, 1 `BOUNDED_ACCESS_GAP`, 1 `SUPPLEMENTARY_ONLY`.
- Dataset roles/fitness: #16/#41/#42 closed with explicit independence and fitness controls.

## Why CONDITIONAL_PASS rather than PASS

Eleven governed sources still have residual deep-mining/locator/schema debt. These gaps are known, have owner issues and claim restrictions, but full source-complete closure has not been achieved. The gaps do not currently justify blocking the bounded Core conceptual work because broad novelty/search families are stopped and the unresolved items are routed as profile/method/locator/application debt.

## Conditions

### C1 — bounded pending sources
`BOUNDED_PENDING` sources may not support detailed feature/coverage/superiority claims beyond their actually mined evidence. Owners: #12/#13/#14/#15/#17. Recheck trigger: before #24 G2 and again before #53 claim calibration.

### C2 — no premature canonicalization
All G1 candidate/disposition files remain `PROVISIONAL_NONCANONICAL`. W2 must explicitly decide identity, foundational category, reuse/alignment and scope before anything enters a canonical Core/profile registry.

### C3 — Core identity invariants
W2 must preserve or explicitly overturn with evidence the following G1 distinctions:
- Risk phenomenon vs Risk Register Entry/information artifact;
- scenario description vs possible/realized event;
- Assessment Activity vs Assessment Result;
- inherent/residual as contextual assessment-result semantics by default;
- Risk State vs Workflow State;
- Risk Owner as role/responsibility;
- strategy vs plan vs activity vs control/mechanism;
- evidence vs observation/result vs provenance/source;
- causation vs association/dependency;
- method scales and source taxonomies outside Core by default;
- external ownership/federation for Pharma concepts via CM-PharmE.

### C4 — dataset/file debt
DS-004 exact file schema/license/checksum debt is not a W2 Core blocker, but it remains a hard prerequisite for any later evaluated file-level mapping/application claim. DS-002 remains at most a record-level holdout candidate after protocol/version freeze.

### C5 — scope triggers
Broad Health, pharmacovigilance signal and future Risk Intelligence semantics remain outside the Paper-1 Core claim boundary unless their owner issues explicitly expand scope and trigger G1 regression.

### C6 — new evidence regression
A materially closer ontology/model/source, a contradiction discovered during W2, or expansion of Paper-1 claims automatically reopens the affected G1 coverage/reconciliation decision.

## Prohibited claims after G1

- no claim of a validated/canonical SemRisk ontology yet;
- no universal/comprehensive all-domain claim;
- no first risk ontology / first Pharma ontology / first risk-register KG/RDB / first ontology+formal-verification claim;
- no claim that bounded pending sources were fully mined;
- no independent-validation claim from design-influencing datasets;
- no claim that reasoner/SHACL/application success proves semantic validity.

## Gate artifacts

- `conceptualization/source-mining/g1-raw-disposition-registry.csv`
- `conceptualization/source-mining/g1-consolidated-candidate-set.csv`
- `conceptualization/source-mining/g1-relation-event-state-candidates.csv`
- `conceptualization/source-mining/g1-cross-source-reconciliation-wave1.csv`
- `conceptualization/source-mining/g1-conflict-register.csv`
- `conceptualization/source-mining/g1-source-family-delta-wave1.md`
- `conceptualization/source-mining/g1-source-coverage-snapshot.csv`
- `conceptualization/source-mining/g1-raw-disposition-completeness-wave1.md`
- `literature/search-final-stopping-decision-2026-09-22.md`

## Reconstructability anchor

Pre-decision repository head after all reconciliation artifacts: `73ee794a168414cfdde267987246a7b65831aadb`.

## Authorization

`P1-R0 → CONDITIONAL_PASS`.

W2 may begin with #19 and #7, subject to the conditions above. No canonical freeze is authorized until W2/G2 criteria are satisfied.