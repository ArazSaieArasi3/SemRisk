# Issue #50 — Negative-control baseline and gap register v0.1

Status: CHECKPOINT — not Issue completion
Target baseline: `bae1480138ed713bfc0af6161a5ae2ed2d8a6024`
Work item: #50

## Purpose

Establish the controlled starting inventory for Paper-1 negative controls before extending mutation coverage. This register distinguishes controls already executable in the deterministic #44 pipeline from defect families still requiring fixtures. Existing green CI is verification evidence only; it is not ontology/domain validity evidence.

## Existing executable controls observed on the target baseline

| ID | Fixture/artifact | Defect family | Expected detector | Current evidence |
|---|---|---|---|---|
| NC-SHACL-01 | `testdata/negative/entry-missing-risk.ttl` | required risk link missing | PySHACL / declared shapes | executable in `tools/semrisk_semantic_ci.py` |
| NC-SHACL-02 | `testdata/negative/workflow-two-current.ttl` | invalid workflow-current cardinality/state | PySHACL / declared shapes | executable in semantic CI |
| NC-SHACL-03 | `testdata/negative/responsibility-missing-assignee.ttl` | responsibility assignment incomplete | PySHACL / declared shapes | executable in semantic CI |
| NC-SHACL-04 | `testdata/negative/assessment-result-missing-trace.ttl` | assessment result lacks trace | PySHACL / declared shapes | executable in semantic CI |
| NC-SHACL-05 | `testdata/negative/pharma-wrong-target.ttl` | invalid Pharma target/profile binding | PySHACL / declared shapes | executable in semantic CI |
| NC-TRACE-01 | `testdata/negative/trace-mismatch.csv` | conceptual↔formal trace mismatch | `TRACE-NEG-001` | executable in semantic CI; expected two fake IDs absent |
| NC-REASON-01 | #44 reasoner inconsistency fixture | logical inconsistency | ROBOT/HermiT path | #44 acceptance/build evidence reports detection |

The five SHACL fixtures and trace mismatch are explicitly enumerated by the current CI source. The #44 acceptance/build evidence additionally reports one reasoner inconsistency fixture. This checkpoint does not strengthen that observation into a broader coverage claim.

## Required Issue #50 coverage gap matrix

| Defect family required by #50 | Existing evidence | Gap disposition |
|---|---|---|
| RDF/Turtle syntax corruption | parser positive path exists; dedicated negative fixture not established here | ADD |
| OWL profile violation | profile validator exists; dedicated negative fixture not established here | ADD if technically stable |
| inconsistent axioms / unsatisfiable class | reasoner inconsistency negative exists | RETAIN + bind exact fixture metadata |
| unintended/missing entailment | entailment/non-entailment positive expectations exist | ADD mutation fixture(s) |
| wrong role/type modeling | no dedicated controlled mutation established here | ADD |
| event vs information-object confusion | no dedicated controlled mutation established here | ADD |
| risk record vs risk phenomenon conflation | no dedicated controlled mutation established here | ADD |
| workflow state vs risk state conflation | SHACL workflow control is partial, not semantic-conflation proof | ADD semantic mutation |
| unsupported mapping equivalence | `MAP-001` rejects unapproved equivalence in canonical graph; no mutation fixture established | ADD |
| SHACL cardinality/datatype/value-set violation | five negative fixtures cover selected shape families | RETAIN; classify exact mutation per fixture |
| broken import/IRI/reference | dependency checks exist; no dedicated mutation fixture established here | ADD |
| stale ontology↔RDB mapping | RDB projection dependency not yet evidenced for this checkpoint | DEFER to relevant projection baseline, do not mark PASS |
| CQ expected-answer mismatch | CQ infrastructure exists; dedicated mutation fixture not established here | ADD with #52 contract |
| provenance/evidence loss | no dedicated mutation fixture established here | ADD |
| scenario mutation changing risk/reassessment output | bounded Pharma case exists; controlled mutation not established here | ADD after exact expected semantics are fixed |

## Metadata contract for every new fixture

Every fixture added under #50 MUST record: stable fixture ID; exact baseline ref; mutation class; exact changed artifact/diff; intended defect; independent rationale for expected result where possible; expected detector/method/result; evaluation layer; limitations; remediation/retest expectation; and exact execution evidence. `FAIL`, `ERROR`, `UNSUPPORTED`, and `NOT_RUN` remain distinct.

## Scientific safeguards

1. A fixture is synthetic test evidence, never external domain-validation evidence.
2. A failing fixture is retained; it is not weakened to preserve green CI.
3. Expected results are specified before execution whenever possible.
4. Existing controls are not counted as covering a conceptual distinction unless the mutation actually exercises that distinction.
5. Tool timeout/error is not defect detection.
6. Coverage claims use declared defect-family denominators and preserve untested families as gaps.
7. Exact-version binding is mandatory for baseline, mutation and result.

## Next atomic batch

Create the highest-value missing semantic mutation fixtures first: (a) risk-record/risk-phenomenon conflation, (b) workflow-state/risk-state conflation, (c) unsupported equivalence mapping, and (d) expected-entailment mutation. Predeclare expected detector/results, then integrate them into the deterministic #44 runner without weakening existing checks. Follow with parser/profile/import/provenance/CQ/scenario families and finally reassess the Issue #50 acceptance denominator.
