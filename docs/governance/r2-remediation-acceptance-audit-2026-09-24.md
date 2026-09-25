# R2 Semantic Web / KR Review Remediation Acceptance Audit — 2026-09-24

**Issues:** #73, #74, #75, #76, #77, #78  
**Origin:** specialist-style simulated Semantic Web / OWL 2 DL / SHACL / Knowledge Representation review (R2), used as an adversarial review aid. This is **not independent human expert validation**.

## Decision
**PASS / CLOSED for all five remediation issues.**

The remediations were deliberately minimal:
- no broad new domain ontology was introduced;
- no global closed-world OWL semantics were added;
- no lossless ontology↔RDB claim was introduced;
- qualified fixture metadata was used where a fixture-level representation gap was the actual problem.

## #73 — unintended concernsRisk domain inference
Implemented:
- removed global `rdfs:domain SR-CPT-033` from `SR-REL-001 concernsRisk`;
- retained the justified Risk range;
- preserved Register Entry completeness as SHACL/profile validation;
- added `tools/r2_formal_semantics_guard_check.py`.

Semantic CI run **36014986794**:
- `PASS: concernsRisk has no global OWL domain and retains Risk range`
- marker `SEM_RISK_R2_FORMAL_GUARDRAILS_PASS`.

## #74 — Risk vs Assessment Result disjointness
Implemented:
- `SR-CPT-001 Risk owl:disjointWith SR-CPT-013 Risk Assessment Result`;
- subclasses such as inherent/residual results inherit this protection;
- added `testdata/negative/reasoner-inconsistent-result-risk.ttl`;
- HermiT negative-control step added to Semantic CI.

Semantic CI run **36014986794**:
- main candidate remains OWL 2 DL and consistent;
- HermiT rejected the deliberate Risk/Assessment Result conflation.

## #75 — historical owner leakage
Implemented:
- owner CONSTRUCT rule now excludes responsibility assignments explicitly invalidated with `prov:invalidatedAtTime`;
- no global current-owner OWL axiom was added;
- the rule explicitly documents its governed application-graph / OWA limitation;
- added `testdata/negative/rule-historical-owner.ttl`;
- added `tools/r2_owner_rule_temporal_check.py`.

Semantic CI run **36014986794**:
- active responsibility derives owner;
- explicitly invalidated historical responsibility does not derive owner;
- marker `SEM_RISK_R2_OWNER_TEMPORAL_RULE_PASS`.

## #76 — qualified assessment evidence support role
Implemented:
- base `supportedByEvidence` relation retained;
- E2E RDF fixture now carries a qualified RDF statement for support role `context`;
- this role remains case/evaluation metadata and is not promoted into a universal Core taxonomy;
- P49-07 now compares result + evidence + support role against PostgreSQL.

First Relational CI run **36015074346** failed during RDF parsing because the new fixture used `rdf:Statement` without declaring the `rdf:` prefix. The failure was retained as genuine test evidence and corrected.

Final Relational CI run **36015300327**: **SUCCESS**.
- RDF scenario: 609 triples; 10/10 predeclared answer families.
- P49-07: `equivalent_for_task`, RDF rows=2, SQL rows=2.
- overall parity after remediation:
  - 6/8 equivalent_for_task
  - 2/8 equivalent_after_declared_normalization
  - 0/8 partial
- negative controls and CQ regression remain green.

Downstream manuscript/evaluation/claim artifacts were refreshed so the old 5+2+1 parity counts are not retained as current results.

## #77 — Relational CI trigger coverage
Finding during remediation: the Relational CI consumed case/RDF/parity/CQ files but originally auto-triggered only on `relational/**`.

Implemented trigger coverage for:
- `case/pharma/**`;
- `ontology/core/**`;
- `ontology/enterprise/**`;
- parity/CQ registries;
- E2E/parity/CQ/negative-control scripts;
- relational sources and the workflow itself.

The workflow-file change automatically triggered run **36015074346**, and the subsequent case-file correction automatically triggered run **36015300327**, demonstrating that the trigger blind spot is closed.

## #78 — Predisposing Condition definition↔axiom alignment
Implemented:
- narrowed the canonical definition from "state or disposition" to a contextual state-of-affairs / situational condition;
- retained `gufo:Situation` formalization and explicit disjointness from Vulnerability;
- aligned conceptual/foundational registries;
- extended the R2 formal guard to prevent prose/axiom drift.

Semantic CI run **36017187020**: **SUCCESS**.
Relational/E2E regression run **36017167764**: **SUCCESS**.
Guard output confirms the Predisposing Condition prose/formalization is situational and disjoint from Vulnerability.

## Residual R2 review observations mapped to existing governance
- mutation-coverage limitations remain governed by #50 and the growing negative-control suite; coverage is representative, not exhaustive;
- the Provenance umbrella risk remains controlled by the #72 PROV-O guard and the Core scope note that qualified PROV-O is normative;
- SKOS mapping predicates remain alignment metadata, not OWL equivalence; no substitutability claim is authorized;
- CM-PharmE license governance remains an explicit release/availability dependency for #55/#56 and is not falsely marked resolved.

## Claim boundary
The R2 remediations strengthen formal and task-level application fidelity. They do not establish independent human semantic validation, universal correctness, complete SHACL coverage, or global lossless ontology↔database equivalence.


## Superseding R6 parity note — 2026-09-25

The R2 6/8 direct + 2/8 normalized result above remains the historical R2 outcome. Subsequent R6 data-architecture remediation preserved stable actor identity and exact CM-PharmE target IRIs in the relational projection. Final validated run **36123602513** therefore reports **8/8 `equivalent_for_task`**, with no identity-erasing normalization. This remains an eight-task, task-bounded result rather than global ontology↔RDB equivalence.
