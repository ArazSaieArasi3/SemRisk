# Run 5 foundational decisions and complete inventory audit

Baseline main: `9fb392b2b592caf1e9fbf0f108daab9a73461320`. Successor: `0.2.0-rc.2`. This is a bounded correction and an honest readiness audit, not a claim that the full model is already OntoUML-valid. The earlier 33-row foundational register is retained as historical evidence. The [47-row current audit](concept-category-audit.csv) and [38-row relation audit](relation-formal-audit.csv) are the complete handoff inventories.

## Implemented decisions

| Decision | Rationale and action | Rejection condition |
|---|---|---|
| Risk Owner across external actor kinds | Persons and organizations need not share an identity principle. The broad class is now typed `gufo:RoleMixin`; narrower role classes may inherit their external kind later. Existing individual IRIs and co-ownership rules remain unchanged. | A universal sortal Role inferred merely from the word Actor; ownership becomes an identity provider. |
| Assessment Confidence | An information qualification of an assessment under a basis. Definition is synchronized in registry and Method module. | Confidence becomes estimated likelihood or an intrinsic quality of Risk; unimplemented confidence arithmetic is claimed. |
| Indicator | A versioned monitoring specification, separate from each observed/computed result. | Indicator specification and Observation Result are identified because both have a numeric value. |
| Threshold | A versioned decision-boundary specification. Operator, scale, unit and applicability are application commitments. | One universal threshold/formula is asserted or a threshold is confused with a Trigger occurrence. |
| Responsibility grounding | Relator commitments concern distinct endurant participants. An opt-in helper plus actual SHACL requires named, explicitly distinct witnesses. Risk remains an aboutness target. | The second participant is invented from Risk identity; an anonymous open-world witness is reported as complete data; an authority is silently inferred as an owner. |

These are design decisions informed by the primary semantics below; no primary source is claimed to provide SemRisk's particular confidence/indicator/threshold definitions verbatim. No new human validation was performed.

## Exact conceptual coverage

35 of 47 rows are local conceptual OWL classes, four are external/pattern SKOS markers and eight are undeclared profile/external candidates. The operational profile has 26 terms (six helper classes, seven controlled individuals, thirteen properties), counted separately. One new helper is not a new enterprise domain or a new row in the 47-concept domain inventory. All 38 conceptual relation rows are accounted for: 37 local OWL object properties and one architectural metadata relation. Definition and relation audits preserve both the conceptual proposals and actual OWL declarations; they do not equate them.

### SR-CPT-016
Risk Level Assessment Result inherits assessment-result identity; its aggregate rating is method-dependent. No universal multiplication rule is adopted.
### SR-CPT-019
Assessment Confidence qualifies information. A confidence value, method or uncertainty distribution would require a separately declared operational representation; this run clarifies the concept without pretending that such arithmetic exists.
### SR-CPT-022
Observation Activity is an event. Observation purpose does not make an observation result an event.
### SR-CPT-023
Observation Result is information produced by observation, potentially used as evidence; it is not the reusable monitoring specification.
### SR-CPT-024
Indicator denotes the definition of what to observe/compute. Version identity and observation identity remain distinct.
### SR-CPT-025
Threshold denotes a decision specification tied to a method/context, not a domain-neutral number. Executable comparisons remain future method-profile work.
### SR-CPT-040
API/INN has no matching class in the frozen CM-PharmE v1 bridge. Keep it external/unmapped; no invented CM-PharmE equivalence.
### SR-CPT-041
Hazard remains a safety-specific profile candidate.
### SR-CPT-042
Harm remains a safety-specific consequence candidate.
### SR-CPT-043
Signal remains a domain-specific information candidate pending adoption.
### SR-CPT-044
Risk Criteria remains a governance/method specification candidate.
### SR-CPT-045
Risk Appetite remains a governance expression; it is not a timeless Risk attribute.
### SR-CPT-046
Risk Tolerance remains a governance boundary; it is not equivalent to residual or desired risk.
### SR-CPT-047
Risk Nature remains objective/context-dependent polarity; no extra Risk identity is introduced.

## Remaining diagram-critical decisions: execute in this order

1. **Scenario level.** Existing `SR-CPT-006 rdf:type gufo:SituationType` class metadata must not be mistaken for `SR-CPT-006 rdfs:subClassOf gufo:SituationType`. The current possible-pattern wording and instance usage need an explicit type/instance-level contract, positive entailment and non-entailment probes before promotion. No silent metamodel conversion is made here.
2. **Information identity pattern.** Seventeen rows use information/result/collection categories. Select the common artifact-versus-content identity pattern and register any required helpers, then justify kind/subkind/role/collective choices individually. `information object` is not a standard OntoUML stereotype.
3. **Workflow value versus quality.** A reusable status value such as Open is distinct from a particular status quality of one record. Select an explicit scheme/value and qualified-history representation; do not draw the same shared value as one quality characterizing multiple bearers.
4. **Pattern-view boundary and full rendering.** Risk and Risk Source remain deliberately broader governed patterns. Represent their explanatory pattern view separately from the strictly stereotyped OntoUML view; do not invent `derived pattern` as a standard stereotype. Likewise, the derived Risk-to-Actor query is not automatically an OntoUML material association between endurants. Complete the editable model, explicit relation ends and cardinality evidence before claiming Figure 1 is complete.

Items 1–3 are the next dependency-ready semantic batch. Reuse these inventories; no new broad literature sweep or repeat temporal implementation is needed. P06/P07/P08 remain open. The user need not reapprove a routine defensible choice; escalate only if evidence leaves materially different unresolved research commitments.

## Primary method anchors

- OntoUML, **RoleMixin**, Definition and constraints: a heterogeneous, anti-rigid non-sortal classification; primary documentation accessed 2026-10-05. https://ontouml.readthedocs.io/en/latest/classes/nonsortals/rolemixin/index.html
- OntoUML, **Mediation**, Definition: the relator pattern needs distinct participants; this motivates explicit evidence checks without treating RDF names alone as proof of distinctness. https://ontouml.readthedocs.io/en/latest/relationships/mediation/index.html
- gUFO **1.0.0**, taxonomy of types and `Relator`/`mediates`: distinguishes class metadata from instance classification and supplies the imported minimum-participant restriction. https://nemo-ufes.github.io/gufo/
- OntoUML Vocabulary **1.1.1**, ClassStereotype and model/view separation: use the standard vocabulary and keep serialization validity separate from semantic adequacy. https://dev.ontouml.org/ontouml-vocabulary/

The separate formal protocol cites tools and describes actual execution. This bounded custom checker is not an exhaustive implementation of the OntoUML antipattern catalog.
