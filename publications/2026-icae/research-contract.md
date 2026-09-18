# SemRisk Paper 1 Research Contract — ICAE 2026

**Research:** R-022 / SemRisk  
**Venue locus:** ICAE 2026, Track 2 / Cluster B — Informatics & AI  
**Frozen:** 2026-09-19  
**Status:** PASS — bounded contribution/RQ/nonclaim contract for Paper 1.

## 1. Problem and bounded gap

Risk-management practice and semantic artifacts frequently conflate a real-world risk phenomenon with its possible event/scenario descriptions, operational register records, assessment activities, assessment results, management workflow states, evidence and treatments. Existing risk ontologies and standards provide important partial/foundational semantics, but Paper 1 investigates whether a source-complete, well-founded and operationally executable semantic architecture can preserve these distinctions while remaining reusable across an enterprise risk context and one bounded pharmaceutical federation case.

The paper does **not** attempt to prove a universal or complete ontology of all risk domains.

## 2. Research questions

### SR-RQ1 — Core semantic disambiguation
How can an evidence-grounded, well-founded SemRisk Core represent risk knowledge while preserving the distinctions among risk phenomenon, event, scenario, scenario description, register record, assessment activity, assessment result, risk state, workflow state, evidence, treatment/control and responsibility?

**Primary units:** U03–U08.  
**Evaluation path:** G1 reconciliation; conceptual CQs; UFO/gUFO/OntoUML analysis; OWL/SHACL formalization; E1–E7; negative controls.

### SR-RQ2 — Enterprise operationalization
To what extent can the SemRisk Core be operationalized for enterprise/architecture-driven risk management by linking risks to objectives, capabilities, processes, controls and accountable actors while mapping a real Jira-style risk-register schema without treating the schema itself as ontology truth?

**Primary units:** U09, U10, U12, U13.  
**Evaluation path:** source/standard mapping; operational-schema mapping; bounded relational projection; CQ/query tests; SQL↔SPARQL parity; E6/E8/E9.

### SR-RQ3 — Bounded Pharma federation and transfer
To what extent can the same Core semantic pattern be specialized/federated for a bounded pharmaceutical ecosystem risk case using CM-PharmE, ICH Q9 and qualified Pharma evidence/data while preserving external semantic ownership and explicitly identifying unmapped or context-dependent semantics?

**Primary units:** U09–U12, U14.  
**Evaluation path:** CM-PharmE bridge review; Pharma case/data mapping; case CQs; expert/semantic review where feasible; E6/E8/E11 with bounded conclusions.

## 3. Contributions

### SR-C1 — Dominant contribution: well-founded operational risk semantic pattern
An evidence-grounded SemRisk Core pattern that formally distinguishes the managed risk phenomenon from event/scenario semantics, scenario descriptions, risk-register records, assessment activities/results, risk/workflow states, evidence, responsibility and treatment/control.

This is the dominant scientific contribution. It must be supported by closest-work comparison, source reconciliation, foundational analysis, formal implementation and claim-appropriate evaluation.

### SR-C2 — Supporting contribution: enterprise operationalization and executable projection
A governed Enterprise/Architecture application of the Core that connects risk knowledge to objectives, capabilities, processes, controls and accountable roles, and demonstrates how a real operational risk-register schema and bounded relational projection can implement these semantics without becoming their canonical owner.

The RDB is an evaluation/application projection, not a separate ontology contribution.

### SR-C3 — Supporting contribution: bounded Pharma federation case
A versioned SemRisk↔CM-PharmE federation pattern and evidence-backed pharmaceutical risk case showing how domain specialization can preserve canonical ownership and reveal reusable Core semantics versus Pharma-specific extensions.

This is a bounded case contribution, not evidence of universal Health or cross-domain validity.

## 4. Supporting method/evaluation contribution status

The governed source-mining, OGCM-RF gates, negative controls, E1–E11 evaluation, claim calibration and reproducibility package are **methodological support for credibility**. Paper 1 must not inflate them into a fourth independent novelty claim unless W1/W4 evidence later establishes a truly distinct method contribution and #1 is formally reopened.

## 5. Candidate claim register

| Claim ID | Candidate wording | Required evidence | Current status |
|---|---|---|---|
| SR-CL01 | SemRisk provides an evidence-grounded semantic architecture separating risk phenomena from operational information/assessment/workflow artifacts. | G1, CQs, foundational model, formal artifacts, closest-work comparison | PLANNED / bounded |
| SR-CL02 | The pattern can represent the governed Jira-style operational schema without class-per-column translation. | field/code mapping, mapping correctness, CQ/application evidence | PLANNED / bounded |
| SR-CL03 | Enterprise objectives/capabilities/processes/controls/responsibility can be linked to risk semantics without redefining them as risk entities. | conceptual model, mappings, CQs, scenario | PLANNED |
| SR-CL04 | A relational projection can preserve claim-critical SemRisk meanings for selected tasks. | ontology↔RDB mappings, SQL↔SPARQL parity, loss analysis | PLANNED; task-bounded |
| SR-CL05 | The SemRisk Core can be federated with CM-PharmE for one bounded Pharma risk case while preserving semantic ownership. | exact CM-PharmE ref, bridge mappings, case/evaluation evidence | PLANNED |
| SR-CL06 | Selected Core semantics show bounded transfer across operational and Pharma contexts. | E11 heterogeneous evidence + failures/limitations | CONDITIONAL; may be removed |
| SR-CL07 | SemRisk differs from closest prior work in the integrated combination actually implemented/evaluated. | current closest-work search, common criteria, E10 | CONDITIONAL; descriptive only |
| SR-CL08 | The evaluated candidate is formally consistent for the tested axioms/profile. | exact-ref reasoning + negative controls | PLANNED; formal only |
| SR-CL09 | Paper-1 artifacts/results are reproducible to the extent allowed by licenses/private evidence. | exact release/tool/data refs and rerun evidence | PLANNED |

## 6. Explicit nonclaims

Paper 1 does **not** claim:

- the first or universally comprehensive risk ontology;
- complete coverage of all risk-management standards or risk domains;
- universal Health, Pharma or cross-domain validity;
- overall superiority over all prior ontologies/models;
- a completed or validated Risk Intelligence Platform;
- dynamic risk forecasting/propagation as an evaluated contribution;
- Newsium/Commentium runtime integration;
- certification/conformance to ISO/COSO/OCEG merely from semantic alignment;
- that formal logical consistency equals semantic/domain validity;
- that a high mapping percentage equals ontology correctness;
- that operational Jira evidence is independent validation of semantics it helped shape;
- guaranteed IEEE Xplore/Scopus publication.

## 7. Paper-1 artifact boundary

In scope when required by the claims:
- governed source/search/reconciliation evidence;
- UL and conceptual CQ registry;
- Core concept/relation/event/state registries;
- selected COVER/ROSE reuse/alignment decisions;
- UFO/gUFO/OntoUML model;
- modular OWL/RDF/Turtle and SHACL/rule separation;
- Enterprise/Architecture application mapping;
- Jira-style operational mapping;
- CM-PharmE bridge and bounded Pharma case;
- bounded PostgreSQL projection and parity evidence if retained;
- E1–E11 claim-dependent evidence;
- claim calibration, threats/limitations, reproducibility bundle.

Out of scope:
- full Health profile;
- full Risk Intelligence platform;
- production ingestion/streaming;
- Newsium/Commentium runtime federation;
- universal profile catalogue.

## 8. Information budget under the 8-total-page contract

The manuscript should reserve approximately:
- Introduction/problem/contributions: 0.6–0.8 page
- Closest work/gap: 0.7–0.9
- Method/evidence engineering: 0.7–0.9
- Core semantic architecture: 1.4–1.6
- Enterprise/operational application: 0.7–0.9
- Pharma federation/case: 0.7–0.9
- Evaluation/results: 1.1–1.4
- Discussion/limitations/conclusion: 0.4–0.6
- References: within the same 8-page cap

If content pressure occurs, claims/scope must be narrowed rather than deleting claim-critical method/evaluation evidence.

## 9. Preferred visual information budget

1. Core semantic distinctions / Core-profile architecture figure.
2. Enterprise→operational→Pharma bounded semantic/application chain.
3. Closest-work comparison table.
4. Compact E1–E11 results table.
5. Traceability/mapping summary only if space remains.

## 10. Change-control rule

W1/W4 evidence may narrow, qualify or remove claims without reopening this gate. Any change that adds a new primary RQ, changes the dominant contribution, upgrades a bounded case into a general validity claim, or introduces Risk Intelligence/Newsium/Commentium as a completed Paper-1 contribution requires #1 and #8 to be reopened with downstream impact analysis.

## 11. Gate decision

**PASS**

This gate freezes the scientific boundary and intended claims, not their truth. Final claim wording remains controlled by #53 after evaluation.
