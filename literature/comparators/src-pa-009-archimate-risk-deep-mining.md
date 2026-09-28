# SRC-PA-009 Deep Mining — Ontological Analysis and Redesign of Risk Modeling in ArchiMate

Source ID: SRC-PA-009
Citation: Sales et al. (2018), Ontological Analysis and Redesign of Risk Modeling in ArchiMate, IEEE EDOC 2018, DOI 10.1109/EDOC.2018.00028
Mining date: 2026-09-20
Status: DEEP-MINED v0.1 — full text inspected; final locator normalization remains.

## Why this source is material

This is a direct closest-work comparator for SR-RQ2 / SR-C2 because it applies ontological analysis to risk modeling in an Enterprise Architecture language and proposes a redesign of ArchiMate risk-related concepts using well-founded ontological distinctions.

SemRisk therefore must not claim novelty merely for connecting risk to Enterprise Architecture, grounding EA risk constructs in foundational ontology, or distinguishing risk-related modeling constructs through ontological analysis.

## Material semantic findings

1. Risk semantics require ontological clarification rather than direct reuse of a generic EA modeling primitive.
2. Event, situation and disposition-like distinctions are material to risk modeling.
3. Assets, value and objectives are central to risk semantics.
4. Threat and vulnerability have prior ontological treatments and cannot be treated as simple labels.
5. EA notation can hide ontological overload; this supports SemRisk anti-pattern checks for Risk vs Risk Record, Risk Event vs Scenario Description, Risk Assessment vs Assessment Result, and Risk State vs Workflow State.

## Comparator strengths relative to SemRisk

The source is stronger or already established in explicit Enterprise Architecture context, formal ontological analysis of an established EA language, redesign of risk-related EA constructs, and connection between ontological analysis and modeling-language improvement. These strengths must remain visible in E10 and novelty calibration.

## SemRisk differentiation that remains plausible

Candidate differentiators still requiring evidence are: operational risk-register information artifacts and workflow semantics; Assessment Activity vs Assessment Result; Risk State vs Workflow State; governed source-to-canonical traceability; relational projection with SQL/SPARQL parity; bounded Pharma/CM-PharmE federation; and release-bound claim calibration.

## Claim impact

- SR-CL03 Enterprise semantics: NARROWED. Ontologically grounded EA-risk linking is prior art.
- SR-CL07 Differentiation: HIGHER EVIDENCE BURDEN. This source must be included explicitly in E10.
- SR-C2: RETAINED BUT REFRAMED around the combined operationalization from well-founded Core to EA context to operational register/assessment/workflow semantics to executable projection.

## Candidate mappings for W2

- Risk Event: prior event semantics; align/reuse.
- Threat: compare COVER/ROSE/ArchiMate redesign.
- Vulnerability: align disposition semantics.
- Asset/Object at Risk: compare ownership with Business/Architecture ontologies.
- Objective/Value linkage: treat as reused/aligned context, not novelty.
- Risk Register Entry, Assessment Result, Workflow State: remain candidate differentiation points requiring direct comparison.

## Remaining extraction debt

Before G1: normalize exact page/figure/table locators; reconcile terminology against COVER/ROSE; record exact ArchiMate constructs and redesign relations in comparator registry; check newer ArchiMate-risk work for supersession/extensions.

## Exact primary-source locator and novelty recalibration — 2026-09-28

**Primary author-hosted full text:** https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/ontological_analysis_and_redesign_of_risk_modeling_in_archimate_2018.pdf (10 PDF pages; corresponding IEEE EDOC 2018 pp. 154–163; DOI above). Page references below use printed conference pagination: PDF page index + 154.

| Claim-critical evidence | Exact locator | SemRisk consequence |
| --- | --- | --- |
| Risk and Security Overlay (RSO) terms and original ArchiMate mapping | Table 1, p. 155; Fig. 1, pp. 155–156 | Original RSO Risk and Vulnerability mapped to ArchiMate Assessment; do not equate original RSO with authors' redesign. |
| Ontology distinguishes experiential event, assessor-linked relation and quantifiable quality | §3, Figs. 5–6, pp. 157–158 | A risk experience comprises threat/loss events; an objectified Risk Assessment relates assessor to event/object; Risk quality inheres in assessment. Generic experience/assessment/value separation is established prior art. |
| Original RSO deficiencies L1–L8 | §4, Table 2, p. 161 | L1 conflates vulnerability and its assessment; L8 collapses risk experience, asset-level risk and a judgment about action. These exact critique categories precede SemRisk. |
| Redesign of threat/object/goal roles | §5, Figs. 7–8, pp. 161–162 | Threat enabler vs asset at risk, hazardous-situation assessment, affected subject's goal and loss-event damage are explicit; generic EA goal/asset/risk semantics are prior art. |
| Three risk perspectives, final scheme and exact ArchiMate representation | §5, Figs. 9–10 and Table 3, p. 162 | Risk Experience→Grouping; Risk→Driver; Risk Assessment→Assessment; Risk Assessor→Stakeholder. The authors explicitly allow different stakeholder judgments to coexist. |

**Corrected novelty boundary:** SemRisk must not claim novelty for risk-event/experience vs risk-assessment vs risk-value separation, assessor perspective, EA goal/asset links, or an ontologically grounded ArchiMate risk redesign. Candidate contribution is the *joint, formally specified and evaluated operational chain* that also identifies the register entry as an information artifact, connects activity/result/evidence and record workflow to temporal state, and tests a governed relational projection. The 2018 paper does not, on these inspected pages, establish that entire chain or its SQL↔SPARQL parity; this is an evidence-bound comparison, not a claim of capability absence. PA-006 further narrows assessor/result/provenance novelty.

**Formal artifact boundary:** the inspected article supplies conceptual diagrams, an ontological analysis and an ArchiMate mapping table. No exact downloadable OWL/OntoUML repository, semantic release, license for code/model import or executable reproduction ref is established by these pages. The author-hosted PDF is the publication artifact; do not call it a machine-readable ontology. Source-code/semantic-artifact status stays `UNKNOWN/NOT_REPORTED` pending a targeted author-repository check if reuse is proposed.
