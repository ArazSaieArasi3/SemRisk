# SRC-PA-006 Deep Mining — Beyond Risk Propagation: A Unified Approach

**Source ID:** SRC-PA-006
**Title:** Beyond Risk Propagation: A Unified Approach — Takeaways From the Cybersecurity Domain
**Authors:** Alessandro Mosca, Mattia Fumagalli, Gal Engelberg, Victor D. Corvalan, Dan Klein, Pnina Soffer, Diego Calvanese, Giancarlo Guizzardi
**Venue lineage:** JOWO 2025 / CEUR-WS Vol. 4176; volume published 2026
**License:** CC BY 4.0
**Mining date:** 2026-09-21
**Status:** DEEP-MINED v0.2 — complete paper and a matching public prototype repository inspected at immutable commit; paper PURL-to-repository redirect still unverified; execution not assessed.

## 1. Why this source is material

This paper is a direct closest-work source for SemRisk SR-C1 and for any future propagation/reassessment claim. It does not treat risk propagation as the movement of one self-standing quantity. Instead it provides a well-founded, COVER-inspired account where risk assessment depends on event types, participating objects, goals, assessors, controls and multiple computed assessment values.

## 2. Research lineage

The paper explicitly builds on two important 2023 predecessors:
- On the Semantics of Risk Propagation — conceptual/ontological analysis of overloaded propagation semantics.
- An Ontology-Driven Approach for Process-Aware Risk Propagation — proof-of-concept process-aware ontology + propagation method validated in cybersecurity.

SRC-PA-006 extends this line with a richer model, assessment taxonomy, competency/query set, ProbLog implementation and cross-domain intent.

## 3. Core ontological commitments extracted

### 3.1 Risk is not a self-standing propagated thing
The paper explicitly argues that risk is a measure/ascription produced by assessment rather than a physical substance that propagates. Risk values are associated with scopes and event types through an assessor-dependent evaluation.

SemRisk implication: the Core must not model risk as a transferable object flowing through a network. Propagation should be represented through changing dependencies, event likelihoods, impact/vulnerability/mitigation assessments and resulting risk assessments.

### 3.2 Future risk concerns event types, not concrete future event individuals
The model follows COVER in treating likelihood as inhering in event types. Future-event risk assessment is therefore attached to event types/semi-saturated event types rather than unknowable future event individuals.

SemRisk implication: carefully separate Event Type / possible event pattern from realized event occurrence and from Scenario Description information artifacts.

### 3.3 Assessment is explicitly assessor- and scope-dependent
The model introduces an assessor and a scope combining:
- event type;
- participating object;
- intended goal/capability.

Different assessors can produce different values for the same event/object because they may select different goals, methods or input assessments.

### 3.4 Assessment taxonomy is prior art
The paper explicitly defines:
- LikelihoodAssessment;
- VulnerabilityAssessment;
- MitigationAssessment;
- ImpactAssessment;
- RiskAssessment;
with computed values and dependencies among these assessments.

This strongly narrows any SemRisk novelty claim based merely on separating assessment types or making risk values contextual.

### 3.5 Risk assessment combines other assessment results
The final RiskAssessment combines likelihood and impact values; impact itself can depend on vulnerability and mitigation assessments. Values may have been supplied by different assessors and re-used by a later assessor.

SemRisk implication: preserve provenance and derivation chains among Assessment Activity, Assessment Result, Assessor, Method, Evidence and reused prior results. A flat timeless risk score is semantically inadequate.

### 3.6 Goals/capabilities determine risk perspective
The same event/object can yield different risk assessments depending on the goal/capability being protected. This supports SemRisk's architecture-goal linkage but makes that contextual-goal idea non-novel.

### 3.7 Controls/mitigations are explicitly represented
Control mechanisms are implemented on objects and assessed for their mitigation effect relative to event type and intended goal.

SemRisk implication: generic Control/Treatment semantics must align with prior well-founded work/ROSE rather than be presented as novel.

## 4. Relation structure extracted

The model includes at least the following relation families:
- LeadsTo / DependsOn between event types;
- Participates / HasParticipant between objects and events;
- PartOf / HasPart for composite objects/events;
- IntendedGoal between assessor/object/goal;
- ImplementedOn between control mechanism and object;
- assessment-result dependencies across likelihood, vulnerability, mitigation, impact and risk.

These relations support graph navigation and automated reasoning.

## 5. Information needs / query contribution

The paper derives prototypical risk-propagation queries from literature, semi-automated extraction and domain-expert review. The query set covers:
- event probability and impact;
- objects participating in risky events;
- cascading event dependencies;
- effect of event likelihood on dependent-event riskiness;
- effect of observed vulnerability on impact;
- multi-perspective assessor/goal-based risk values;
- effect of vulnerability changes on risky-event classification.

SemRisk implication: several future CQs around risk assessment and propagation already have prior-art counterparts. Paper-1 CQs should focus on SemRisk's distinctive operational artifacts and lifecycle/state semantics.

## 6. Implementation/evaluation evidence

The paper implements the theory and running example in ProbLog and couples the ontology-grounded theory with external probability mechanisms such as Bayesian Networks. It demonstrates query resolution for the proposed information needs using a cybersecurity case.

This is stronger than a proposal-only comparator. SemRisk cannot claim novelty merely from executable ontology-grounded risk reasoning or query answering.

## 7. Direct novelty impact on SemRisk

### SR-C1 — dominant contribution
**RETAINED / FURTHER NARROWED.**

Not novel on their own:
- contextual/assessor-dependent risk assessment;
- explicit likelihood/impact/vulnerability/mitigation assessment types;
- goal/object/event-aware risk scopes;
- ontology-grounded propagation/reasoning;
- query-driven operational reasoning over risk assessments.

The strongest remaining candidate SR-C1 boundary is therefore the integrated separation of:
real-world risk-relevant phenomenon/event pattern → scenario description → risk register information artifact → assessment activity → assessment result/derivation provenance → risk state over time → workflow state of the management record → evidence/observation → treatment/responsibility.

### SR-C2 — enterprise operationalization
**RETAINED / NARROWED.**
Objects, goals, capabilities and controls are already explicit in PA-006. SemRisk's enterprise contribution must emphasize architecture-owned entities, register/workflow semantics, governance/accountability and executable projection rather than generic goal/object linkage.

### SR-C3 — Pharma federation
**UNCHANGED DIRECTLY.**
Cross-domain intent exists, but this paper demonstrates cybersecurity. It does not remove the specific SemRisk↔CM-PharmE federation contribution.

### Propagation / dynamic-risk claims
**REMOVE FROM PAPER-1 NOVELTY.**
Risk propagation semantics and executable ontology-grounded propagation are strong prior art and should remain future profile/reuse territory unless SemRisk contributes a demonstrably different mechanism.

## 8. Important methodological strength to preserve in comparison

PA-006 does not merely invent CQs. It reports a literature-derived query elicitation procedure, harmonization, automated extraction assistance, manual curation and domain-expert review. This is methodologically relevant to SemRisk #7/#23/#52 and must be represented fairly in E10.

## 9. Limitations / boundary of PA-006

- Demonstration is centered on cybersecurity.
- The paper's formal theory focuses risk assessment/propagation rather than risk-register information artifacts and record workflow.
- It does not appear to make Risk Register Entry a first-class information artifact.
- Risk State vs Workflow State is not the paper's central distinction.
- Publication-bound evidence governance and ontology↔RDB parity are not its primary contribution.

These are comparison boundaries, not proof that SemRisk is superior.

## 10. Reuse/alignment implications

- COVER-aligned risk/event/value semantics should be reused/aligned rather than recreated.
- Assessment taxonomy and assessor/goal context must be compared before SemRisk defines local equivalents.
- LeadsTo/DependsOn and event/object participation relations require semantic alignment review.
- Control/mitigation semantics should be reconciled with ROSE and PA-006.
- Propagation should be modeled as derived assessment/dependency behavior, not a moving Risk entity.

## 11. Required downstream actions

- Register On the Semantics of Risk Propagation as a distinct lineage source.
- Treat PA-010 and PA-006 as one evolving research lineage rather than independent novelty votes.
- Feed assessment distinctions into #19/#20, but do not canonize before G1.
- Feed PA-006 query methodology into #7/#23/#52.
- Make PA-006 mandatory in #22/#31 E10 and #53 claim calibration.
- Recheck implementation/artifact URI and exact version before #14 closes.

## 12. Gate consequence

PA-006 materially reduces novelty space but does not invalidate SemRisk Paper 1. It strengthens the need to anchor novelty in operational information-artifact, lifecycle/state, evidence/provenance and governed projection semantics rather than generic ontology-based risk assessment/propagation.
## 13. Implementation locator qualification — 2026-09-28

The canonical CEUR full text https://ceur-ws.org/Vol-4176/shields-2.pdf explicitly says in footnote 5 (printed p. 9 / PDF page 9) that the **complete implementation** is accessible at https://purl.archive.org/brp . The paper reports its ProbLog rules/assertions and queries in §5, plus a separate footnote 4 for query-elicitation material. This is a source-declared implementation locator, stronger than an inferred repository search match.

The PURL target was not retrievable through the available source inspection route on 2026-09-28. Its final destination, file inventory, version/commit, license, checksum, executable commands and independent outcomes therefore remain `UNKNOWN/NOT_ASSESSED`. Do not mark the implementation absent or equate the publisher's printed example with an audited software release. Resolve the PURL and pin artifact contents before making a reproducibility claim; the publication-level ProbLog proof of concept remains a valid prior-art comparison.

The SAC 2023 PA-010 predecessor is separately profiled in [the PA-010 technical profile](src-pa-010-process-aware-risk-propagation-profile.md); its OWL→Neo4j/Python DFS/max-per-aspect method is not the same formal implementation as the richer 2025 ProbLog model.

## 14. Public prototype repository inspected — 2026-09-28

A public repository with matching title and a paper coauthor's account is [gal-engelberg-acn/Beyond-Risk-Propagation-An-Ontology-based-Approach](https://github.com/gal-engelberg-acn/Beyond-Risk-Propagation-An-Ontology-based-Approach), pinned at commit `76cf94dabe00d525b6f0d61ceba128f9e0edbc61` (2024-05-12). The repository README describes the same ontology-driven paper/proof of concept and declares CC BY-NC-SA 4.0, with `LICENCE.md` blob `cbe5ad1670406e4402217edfb82d2c56af7e8631`. The article's CC BY 4.0 license and the repository's CC BY-NC-SA 4.0 license apply to **different artifacts**. Do not import or redistribute this code into SemRisk under an assumed article license.

| Repository artifact | Pinned blob | Observation |
| --- | --- | --- |
| `README.md` | `a31d1219ecbcff6a5387b6109f793aa81117084e` | Paper-like overview; contributor/acknowledgement fields anonymized. |
| `Prototype-Implementation/riskprop_a_v6.py` | `d0939180f80dc824b1d9c157cac087e3f7a266bf` | 15,185-byte **ProbLog-style declarative program despite .py extension**: probabilistic facts/rules, event/object/capability/assessor/control assertions, computed values, assessment relations and one active `query(mitigationAssessment(...))`. Many alternative queries are commented. Contains explicit `TO BE FIXED` / scale-update comments, so it is a prototype snapshot, not an audited release. |
| `Risk-Propagation-Query-Elicitation/Elicited-Queries.md` | `3d94d06cf3d33d13c40219eb9ccfa6bc83fc6483` | Elicited risk quantification, propagation, mission/value, and mitigation query candidates; this list is broader than the single active program query and is not evidence that all questions were executed. |
| `Risk-Propagation-Query-Elicitation/Query-processing.xlsx` | `4db81aa8ab907fb384eb2fedb0b294d458cb0ff0` | Binary elicitation workbook identity/size (25,913 bytes) observed; contents not inspected. |

The root listing contains no dependency lockfile, executable instructions or automated tests. The last commit message deletes a different `riskprop-POC.v00.py`; preserve the pinned snapshot identity. **Provenance strength:** a matching public author-associated prototype is bound, but the PURL `https://purl.archive.org/brp` could not be resolved to its target through the available route, so identity with the paper-declared destination remains unverified. The inspected repository can support a bounded implementation comparison; it does not establish paper-exact release correspondence, successful independent execution, or completeness of paper claims. If E10 needs a reproduced outcome, resolve that redirect and execute a clean, versioned ProbLog run with recorded queries/outputs; otherwise mark reproduction `NOT_ASSESSED`.
