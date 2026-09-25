# SemRisk Paper-1 VVEAA execution profile — v0.1

**Date:** 2026-09-25 (Asia/Tehran)  
**Status:** PROVISIONAL CASE-SPECIFIC METHOD / NOT AN OQF RELEASE OR CONFORMANCE CLAIM  
**Issues:** #112/#113; feeds #33/#34/#53/#54/#56. Future independent OQF adoption: #57.  
**Evaluation target:** SemRisk Paper-1 P1-R2 / 0.1.0-rc.1 candidate; bind every run separately to its exact commit, imports, shape/rule/mapping/data refs and tool versions. This label alone is not an immutable full evidence bundle.

## Rationale and boundaries

Paper 1 already has the OGCM-RF E1–E11 claim-dependent evaluation design in `docs/research/paper1-study-design.md` and method decision `method/paper1-method-selection-decision-2026-09-22.md`. VVEAA is a *reporting and decision structure over those existing checks*, not a new replacement enumeration. The ongoing `ontology-quality-framework` research has a 200-source register and an OQUO closest-work delta, but its semantic/process gates are unfinished. Its eventual generic contracts are not retrospectively attributed to this paper. Commentium and CM4DI offer prior multi-layer evaluation practice; any precise method comparison requires verified full-text passages and exact citations before manuscript assertion.

| Function | Question answered | Immediately executable / existing evidence | Result/limit on 2026-09-25 |
| --- | --- | --- | --- |
| **Verification** | Does the exact artifact satisfy its declared syntax, logic and structural constraints? | E1–E3 parsing/OWL 2 DL/HermiT consistency and satisfiability, expected entailment and non-entailment, SHACL positive/negative fixtures, formal ID traceability; E7 executable CQ regression; E9 build binding as reproducibility control. | Formal tests reported PASS for prior tested candidate; exact-head recheck if changed. This does not establish semantic truth. |
| **Validation** | Do concepts/mappings represent the intended risk meaning in the bounded context? | E4 UFO/gUFO category/anti-pattern rationale; E6 standards/operational/DS-003 mapping with `mapped/partial/conflict/unknown` and denominators; E5 frozen #51 instrument when real independent answers arrive. | E6 preliminary and non-independent where design sources shaped commitments; E5 human responses PENDING; no standards conformance claim. |
| **Evaluation** | How useful and robust is the candidate for declared tasks and comparative contexts? | E7 40 original CQs by execution class; E8 predeclared application tasks and eight frozen SQL↔SPARQL pairs; E9 clean reconstruction; E10 closest-work common-criteria matrix; E11 context/holdout analysis. Optional OQuaRE structural metric pilot #114. | 26 executable, 7 partial, 6 conceptual-only, 1 deferred; 8/8 direct task equivalence for 17 directly represented CQs. E10 provisional; E11 no clean independent shortage-domain holdout. Metric pilot NOT YET EXECUTED. |
| **Assessment** | Which claim is justified *as worded*, on which evidence and against which threats? | Nine headline claim IDs `SR-CL01…09` in `publications/2026-icae/author-review-claim-evidence-v0.2.csv`; #53 claim register, #56 threat snapshot, #110 remediation ledger, #111 overclaim guard. | Per-claim assessment is in progress. Provisional manuscript is author-review only; do not turn missing evidence into PASS. |
| **Assurance** | Can an inspectable argument support the bounded release/publication decision? | #54 claim→evidence→counterevidence→assumption→blocker→decision package; #55 exact release, #35 submission audit. | NOT ASSESSED as an integrated gate. #51/E11 and other unresolved external dependencies stay visible. |

**Many-to-many crosswalk:** E1–E3 mainly verification; E4/E5/E6 mainly validation; E7 spans verification and task evaluation; E8/E9/E10/E11 mainly evaluation, with E9 also assurance provenance. Assessment and assurance integrate evidence from all applicable layers. A method belongs where its specific question and role justify it; its label does not confer a PASS in another function.

## Defense in depth and minimal next runs

1. **Exact candidate integrity:** capture ontology/SHACL/rules/mappings/database/data manifest, dependency versions and tested SHA; compare each manuscript number to that candidate. Run affected build/tests if changed. Method: existing SemRisk CI, not invented new run.
2. **Adversarial formal controls:** keep malformed ontology, unsatisfiable-class, negative entailment and failing shape fixtures; check that failures are detected. A passing reasoner is bounded to logical questions.
3. **Semantic counterchecks:** crosswalk material standards clauses, the 27 Jira fields and 18 DS-003 elements with separate mapping existence and correctness; preserve partial/conflict/unknown. Design inputs do not become independent validation.
4. **Predeclared task controls:** retain all 40 CQs and all eight frozen parity pairs, including failed/partial/deferred questions. SQL/OWL open-world–closed-world and projection loss are documented per task.
5. **Independent review/transfer:** collect real eligible reviewer responses under #51 and run genuinely independent E11 only when the data gate permits. Both remain pending for tonight's author draft.
6. **Optional quantitative metric pilot:** execute a *small, pinned* OQuaRE metric subset with raw counts, formula, import scope, scaling function and mutation sensitivity. Represent a few measurements using OQUO if feasible; evaluate QASAR separately. Keep score vectors as contextual measurements, not a single quality score or evidence of domain validity.
7. **Assurance synthesis:** for every claim include supportive and adverse evidence, applicability, uncertainty, owner, condition and recheck trigger. Critical failure is not averaged away.

## Candidate tools and selection

| Tool/family | Role here | Decision |
| --- | --- | --- |
| Existing OWL 2 DL parser/HermiT + SHACL + CQ/SQL/SPARQL regression | Deterministic version-bound formal/task controls | **Keep / rerun affected refs first.** |
| OQuaRE metric action (`tecnomod-um/oquare-metrics`) | Automated quantitative structural/maintainability perspective | **Pilot in #114** with raw metric and scale provenance; not yet executed. |
| OQUO (`tecnomod-um/oquo`) | Reusable model for quality characteristics, measurements, scales and evaluation outputs | **Consider output representation/crosswalk in #114;** it is an ontology, not itself a scoring engine. |
| QASAR / OQUO-QASAR | Aggregates framework outputs (OQuaRE, HURON, OntoEnrich; README also mentions Evaluome) | **Optional pilot only after setup/privacy/version check**; not required for tonight's paper. |
| OOPS! pitfall scanning | Complementary anomaly candidate detector | **Conditional later diagnostic**, findings require human/semantic confirmation; avoid redundant last-minute run without version binding. |
| Real expert protocol #51 | Semantic judgment and dissent | **Pending actual people.** Author or simulated review cannot substitute. |

OQUO's official README models metrics/evaluation; its QASAR README describes the integrated modules. The OQF local delta (source OQF-SRC-0178 pinned to external ref) found substantial overlap for measurement semantics and additional unresolved needs for assessment and assurance. We do not claim OQF novelty or adoption from this observation.

## Method reporting contract for the paper

Each reported result must have `claim_id; function; E-layer; exact target ref; method/tool/ref; unit/denominator; expected criterion; observed result; evidence role; counterevidence/limits; status; recheck trigger`. Allowed result states include `PASS_BOUNDED`, `CONDITIONAL`, `FAIL`, `NOT_ASSESSED`, `BLOCKED`, with a written rationale for N/A. A metric value is reported with raw and scaled values separately; weight/threshold and sensitivity must be declared if used. There is **no overall arithmetic quality score**, no certification, no general standards conformance and no independent semantic validity claim before the corresponding evidence exists.

## Dependencies / exact-source checklist

- SemRisk: `docs/research/paper1-study-design.md`; `evaluation/evidence-role-policy.yaml`; `publications/2026-icae/author-review-claim-evidence-v0.2.csv`; issue #30/#31/#51/#53/#54.
- OGCM-RF: `framework/documentation/formal-ontology-description-standard.md` (FD-A…FD-J) for companion formal page #115; E-layer taxonomy/profile exact ref to record in final manuscript.
- OQF: `synthesis/OQUO-OQF-SEMANTIC-DELTA-W2-R2.md` (research-stage comparison; not an adopted release).
- External: https://github.com/tecnomod-um/oquo and https://github.com/tecnomod-um/oquo/tree/main/oquo-qasar; https://github.com/tecnomod-um/oquare-metrics.
