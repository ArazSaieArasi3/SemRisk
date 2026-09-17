# SemRisk Paper 1 Study Design

**Research:** R-022 / SemRisk  
**Paper locus:** `publications/2026-icae/`  
**Frozen for study design:** 2026-09-17  
**Status:** PASS — suitable to feed Issue #1 contribution/RQ freeze; later evidence may narrow claims but cannot silently change this design.

## 1. Study type

Paper 1 is an **ontology-engineering design research study with evidence-synthesis, bounded case/application, and claim-dependent evaluation components**.

It is not described generically as a “mixed-methods study” unless the manuscript later names the exact methods and their roles. The scientific design consists of five coordinated components:

1. **Evidence discovery and synthesis** — systematic-mapping/scoping-style search plus structured comparative review, source-complete mining and cross-source reconciliation. A systematic-review claim is made only for any component that actually satisfies the executed protocol.
2. **Ontology engineering** — evidence-grounded requirements/CQs, conceptualization, reuse/alignment, foundational analysis, modular formalization and controlled release under OGCM-RF.
3. **Bounded application/case study** — Enterprise/Architecture application plus a pharmaceutical ecosystem case connected to CM-PharmE and qualified operational/public data.
4. **Executable projection/application evidence** — governed ontology instance data, relational projection, representative risk scenario and SQL↔SPARQL semantic-parity tests where retained in Paper 1.
5. **Claim-dependent evaluation and assurance** — formal/foundational verification, semantic/expert/data/standard validation, CQ regression, application utility, reproducibility, closest-work comparison and bounded transferability.

## 2. Research objects and units of analysis

A percentage, coverage result or evaluation conclusion is invalid unless its unit and denominator match one of the governed units below.

| Unit ID | Unit of analysis | Meaning / examples | Typical denominator |
|---|---|---|---|
| U01 | Material source | Paper, standard, ontology, dataset, operational artifact | All material sources in the declared Paper-1 source boundary |
| U02 | Source locus | Section/page/table/figure/clause/sheet/field/artifact path | All concept-bearing loci applicable to the source |
| U03 | Raw evidence item | Native term, definition, relation, field, code, finding | All extracted material items in the source boundary |
| U04 | Normalized semantic candidate | Reconciled pre-canonical candidate concept/relation/event/state | All candidates entering G1/W2 reconciliation |
| U05 | Canonical semantic entity | Approved concept/relation/event/state in Core/profile | All applicable release-critical semantic entities |
| U06 | Semantic requirement | Evidence-grounded requirement before implementation | All Paper-1-required requirements |
| U07 | Competency Question | Conceptual or executable CQ with expected capability | All applicable Paper-1 CQs, separated by conceptual/executable status |
| U08 | Formal commitment | OWL axiom/entity, SHACL shape/constraint, rule or formal mapping | All release-critical applicable formal commitments in the evaluated ref |
| U09 | External mapping | SemRisk↔standard/ontology/data mapping assertion | All applicable mapping targets in the declared source/profile boundary |
| U10 | Dataset element | Table/file/field/code/value-set/record subset | Exact qualified applicable elements; blocked/out-of-scope kept separate |
| U11 | Expert review item | Definition/relation/profile/case item presented for review | All reviewer-applicable items in the bound review instrument |
| U12 | Scenario/task/query | Risk scenario step, decision task, SPARQL/SQL query | All predeclared applicable tasks/queries for the evaluated scenario |
| U13 | Relational projection element | Table/column/join/constraint/mapping pattern | All Paper-1 projection elements in the exact schema version |
| U14 | Evaluated release | Exact ontology/model/mapping/data/tool state | One exact immutable/reconstructable candidate per evaluation run |
| U15 | Manuscript claim | Stable claim ID in abstract/body/conclusion | All central Paper-1 claims, including unsupported/removed claims |

## 3. Evidence-role policy

Machine-readable policy: `evaluation/evidence-role-policy.yaml`.

Allowed roles are:

- `discovery`
- `design`
- `reconciliation`
- `illustrative`
- `regression`
- `independent_validation`
- `holdout`
- `comparative`
- `future_only`

The key invariant is:

> **Evidence that materially shaped the tested design is not independent validation of that same design unless a predeclared untouched partition or genuinely independent evidence source exists.**

Role assignment is artifact/version/subset specific and must be visible in every evaluation that depends on independence.

## 4. Current evidence-role baseline

This table is an initial study-design classification. Issue #41 owns the complete artifact-by-artifact registry and may refine roles without violating the rules above.

| Evidence family | Baseline role(s) | Independence consequence |
|---|---|---|
| `jira risk attributes.xlsx` / SRC-OP-001 | discovery, design, reconciliation, regression/application mapping | Cannot independently validate semantic commitments it helped create; useful for operational mapping and regression with explicit dual-role limitation |
| Risk literature / conceptual models | discovery, design, reconciliation, comparative | Included sources cannot independently validate claims they directly shaped unless a separate untouched source/corpus is reserved |
| ISO/IEC/ICH/COSO/OCEG/Open FAIR evidence | design, reconciliation, comparative; bounded validation for alignment claims | Alignment validation is standard-specific; terminology overlap alone is not independent semantic validation |
| COVER/ROSE/other ontologies | discovery, design/reuse, comparative | Can support closest-work comparison/reuse decisions; not independent validation of a SemRisk construct copied/derived directly from them |
| CM-PharmE | design/federation, comparative, illustrative/application | Cannot independently validate Pharma bridge semantics it directly determines; external ownership must remain explicit |
| Pharma literature used to construct case/profile | discovery, design, reconciliation | Not independent validation of that same profile/case unless separate holdout evidence exists |
| Qualified Pharma datasets | role not assumed; #41/#42 decide by exact dataset/subset | May become mapping/design, regression, or independent validation only after provenance/fitness/leakage review |
| Synthetic fixtures/data | illustrative, regression, application testing | Never independent real-world/domain validation |
| Expert review | potentially independent_validation | Only if reviewer eligibility, independence/project involvement and instrument are declared before interpretation |
| Negative controls/mutations | regression/verification | Demonstrate defect detection, not domain validity |
| Closest-work current refresh | comparative | Supports bounded difference/novelty claims, never an overall superiority verdict |

## 5. Claim type → required evidence design

| Claim family | Minimum supporting evidence | Evidence that is insufficient alone |
|---|---|---|
| Evidence-grounded conceptual semantics | G1 source reconciliation + UL/CQs + concept/relation rationale | frequency of terms, one operational schema, one standard |
| Foundational/ontological soundness | UFO/gUFO/OntoUML analysis + explicit category rationale + anti-pattern review | use of OntoUML notation by itself |
| Formal correctness | syntax/profile checks + reasoning/expected entailments + negative controls | files parse; reasoner returns green once |
| Standards alignment | exact edition/clause/term mappings + mapping correctness review | matching labels or generic standards citations |
| Operational mapping | field/code mapping with denominator + provenance + conflicts/unmapped items | high mapping percentage alone |
| Pharma case adequacy | bounded evidence-backed case + CM-PharmE bridge + qualified data + CQ/task results | one synthetic scenario or one case mapped successfully |
| Relational projection fidelity | ontology↔RDB mapping + SQL/SPARQL parity + explicit loss/OWA-CWA analysis | table/row count similarity |
| Semantic validity | independent/bounded expert or evidence validation + disagreement/findings | author judgment; design evidence only; formal reasoner PASS |
| Application/query utility | predeclared decision/task intent + scenario/query outcomes + failures/limitations | query executes or visualization looks correct |
| Reproducibility | exact release/data/mapping/tool refs + reconstruction/rerun evidence | repository/code merely exists |
| Novelty/differentiation | current closest-work search + common comparison criteria + source-backed differences | absence of a feature in one paper; concept-count advantage |
| Transferability | heterogeneous contexts not all used to design the same commitments + bounded failure analysis | one Jira schema plus one Pharma example used during design |
| Overall Paper-1 assurance | claim-level integration of all applicable evidence, counterevidence and threats | arithmetic average/one global ontology-quality score |

## 6. Independence and holdout rules

1. **Freeze-before-test rule:** expected result/CQ/task and artifact role are recorded before evaluation result inspection.
2. **Design-evidence rule:** if a source materially changes a class/relation/CQ/mapping under test, that source is design evidence for that commitment.
3. **Partition rule:** a dataset can provide both design and holdout evidence only when partitioning is predeclared, provenance/checksums are exact and the holdout has not influenced the tested decision.
4. **Schema leakage rule:** holding out rows does not create independence for schema-level ontology validation if the complete schema/data dictionary already shaped the ontology.
5. **Expert independence rule:** author/co-author/project-team judgment is not labeled independent expert validation; reviewer involvement is reported.
6. **Synthetic rule:** synthetic data may test executability, constraints and regression but cannot support prevalence, empirical causality or external representativeness.
7. **Comparator rule:** comparator selection criteria are fixed before comparison results are used for novelty wording.
8. **Publication rule:** no result from a later semantic/data state is backfilled into an earlier release-bound manuscript without re-evaluation/impact review.

## 7. Primary case/application design

Paper 1 uses two complementary evidence/application contexts without claiming universal cross-domain validation:

### 7.1 Operational risk-register context
Purpose: test whether SemRisk can represent operational risk-management data while preserving the distinction between the real-world risk phenomenon and its register/assessment/workflow artifacts.

Primary role: design/reconciliation plus later mapping/regression/application evidence.

### 7.2 Pharmaceutical ecosystem context
Working scenario direction, subject to #28 evidence qualification:

`pharmaceutical supply disruption → affected capability/process/value/objective → risk event/scenario/consequence → assessment/evidence → treatment/control → residual/reassessment state → responsible actor → risk-record workflow`

Purpose: test a domain specialization/federation with CM-PharmE and qualified Pharma evidence/data.

This is a bounded case. It cannot establish all-Health or all-domain validity.

## 8. Evaluation design

Paper 1 keeps the OGCM-RF E1–E11 structure as a **claim-dependent evaluation matrix**, not a checklist that must all be green.

- E1 — syntax/profile
- E2 — logical consistency / expected reasoning
- E3 — structural/traceability integrity
- E4 — foundational/ontological review
- E5 — bounded semantic/expert validation
- E6 — standards/operational/dataset mapping validation
- E7 — competency-question regression
- E8 — application/query/mapping utility
- E9 — reproducibility/release binding
- E10 — closest-work comparative evaluation
- E11 — bounded transferability/robustness

Negative controls/mutations must precede final formal evaluation for applicable automated layers. Verification, validation, evaluation result, assessment and assurance remain separate concepts in reporting.

## 9. Circularity / leakage risk register

| Risk ID | Risk | Consequence | Control |
|---|---|---|---|
| SD-R01 | Jira spreadsheet used for design and later called independent validation | inflated validity claim | classify as design/reconciliation; report mapping utility separately |
| SD-R02 | Pharma dataset schema mined before holdout assignment | schema-level leakage | distinguish schema/design role from record-level holdout; document partition timing |
| SD-R03 | CQs written after ontology implementation | post-hoc test bias | #7 conceptual CQs must precede implementation; #52 only executes/regresses them |
| SD-R04 | Expected query results derived from actual output | tautological PASS | expected semantic answer frozen before execution |
| SD-R05 | Comparator set selected after seeing favorable differences | novelty bias | #14/#22 criteria and comparator shortlist precede final novelty calibration |
| SD-R06 | Expert instrument changes after responses | confirmation bias | instrument/reviewer criteria frozen before interpretation; changes create new round/version |
| SD-R07 | Failed mappings/CQs removed from denominator | inflated coverage | applicable denominator and failed/partial/conflict states preserved |
| SD-R08 | Synthetic scenario presented as empirical evidence | invalid real-world inference | explicit synthetic provenance and prohibited claim classes |
| SD-R09 | RDB constraints treated as ontology truths | semantic overcommitment | #26 formalization policy and #49 OWA/CWA parity analysis |
| SD-R10 | Formal PASS presented as domain validity | category error | claim-type matrix + #53/#54 calibration/assurance |
| SD-R11 | Later ontology version used with earlier evaluation | release drift | exact semantic IDs/refs, #43/#55 binding and impact-triggered re-evaluation |
| SD-R12 | Pharma case generalized to Health/all domains | external-validity overclaim | explicit bounded population/context and E11 claim limits |

## 10. Threats introduced by the study design

The study design explicitly creates or inherits the following threats, which must be maintained in #56:

- source/database access limitations and publication bias;
- analyst judgment during semantic extraction/reconciliation;
- dependence on foundational modeling assumptions;
- limited number/independence of domain experts;
- operational-source confidentiality and representativeness;
- bounded Pharma evidence and geography/time coverage;
- incomplete independence between construction and evaluation evidence;
- ontology/RDB open-world vs closed-world differences;
- venue page pressure potentially reducing reportable method detail;
- private/licensed evidence reducing third-party reproducibility.

These threats may narrow claims; they are not a manuscript-only appendix.

## 11. Explicit study-design nonclaims

Unless later evidence independently justifies stronger wording, Paper 1 does **not** claim:

- a universally complete ontology of all risk domains;
- universal Health/Pharma transferability;
- predictive risk intelligence or dynamic propagation;
- a validated Risk Intelligence Platform;
- certification against ISO/COSO/OCEG or any external standard;
- superiority over all risk ontologies/models;
- that formal consistency equals semantic/domain validity;
- that high mapping coverage equals ontology correctness;
- that public/DOI datasets are automatically independent or representative.

## 12. Change-control rule

This design is frozen as the Paper-1 study baseline. A later change to:

- study type;
- unit of analysis/denominator;
- evidence independence rule;
- primary case;
- evaluation class;
- holdout definition;
- or claim-support logic

requires a decision record plus downstream impact review of #1, #7, #18, #28–#31, #41–#42, #51–#56 and manuscript artifacts as applicable.

## 13. Handoff to Issue #1

Issue #1 should now freeze RQs/contributions/nonclaims using the following constraints:

1. The dominant contribution must be semantic/ontology-engineering, not merely repository construction or Risk Register digitization.
2. Each primary RQ must map to one or more units of analysis and at least one plausible evaluation route above.
3. Claims requiring independent validation must identify where that independence can actually come from; otherwise wording must be bounded.
4. Enterprise/Architecture and Pharma are application/case contexts around a reusable Core, not separate claims of universal validation.
5. The contribution must fit the verified ICAE 2026 conservative 8-total-page contract without removing method/evaluation detail required to make the claim defensible.
