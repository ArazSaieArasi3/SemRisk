# All 40 relation decisions

> Ontology documentation candidate 0.2.0-rc.4. Source snapshot `67247f13ba5d0c7d32163f2b3e848af15067d92e`. Not a scholarly release or independent domain validation. No manuscript is included.

The 40 current relation decisions are separate from 50 OWL object-property declarations. Conceptual endpoints and multiplicity proposals must not be mistaken for global OWL constraints.

## SR-REL-001 — concernsRisk

Conceptual endpoints: SR-CPT-033 or SR-CPT-034 → SR-CPT-001.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-001.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Exact multiplicity depends on register policy; do not make functional globally.

## SR-REL-002 — describesScenario

Conceptual endpoints: SR-CPT-034 → SR-CPT-006.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-034. Asserted range: urn:semrisk:entity:SR-CPT-006.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Do not infer description = scenario.

## SR-REL-003 — realizedAs

Conceptual endpoints: SR-CPT-006 → SR-CPT-007.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-006. Asserted range: urn:semrisk:entity:SR-CPT-007.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Exact modal semantics require #25.

## SR-REL-004 — hasConsequence

Conceptual endpoints: SR-CPT-007 or SR-CPT-006 → SR-CPT-008.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-008.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Must not imply causal certainty from mere association.

## SR-REL-005 — hasRiskSource

Conceptual endpoints: SR-CPT-001 or SR-CPT-006 → SR-CPT-003.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-003.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Source relation is weaker than causal relation by default.

## SR-REL-006 — predisposedBy

Conceptual endpoints: SR-CPT-006 or SR-CPT-007 → SR-CPT-004.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-004.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Not equivalent to cause.

## SR-REL-007 — triggeredBy

Conceptual endpoints: SR-CPT-007 → SR-CPT-005.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-007. Asserted range: urn:semrisk:entity:SR-CPT-005.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Do not infer trigger = cause universally.

## SR-REL-008 — causes

Conceptual endpoints: risk-chain entity → risk-chain entity.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Never inferred merely from sequence/dependency.

## SR-REL-009 — associatedWith

Conceptual endpoints: risk-chain entity → risk-chain entity.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Symmetry only for generic association, not directed dependency; formal split may be needed.

## SR-REL-010 — affects

Conceptual endpoints: SR-CPT-001/007/008 → SR-CPT-002/037/038/039.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Potential vs realized effect semantics require care.

## SR-REL-011 — exposes

Conceptual endpoints: SR-CPT-003/004 → SR-CPT-002.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Financial/physical exposure refinements remain profile-level.

## SR-REL-012 — hasVulnerability

Conceptual endpoints: SR-CPT-002 → SR-CPT-009.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-009.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Exact bearer/category requires #25.

## SR-REL-013 — performedAssessmentOf

Conceptual endpoints: SR-CPT-011 → SR-CPT-001.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-011. Asserted range: urn:semrisk:entity:SR-CPT-001.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: Exact min cardinality belongs to #26/SHACL.

## SR-REL-014 — usesAssessmentMethod

Conceptual endpoints: SR-CPT-011 → SR-CPT-012.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-011. Asserted range: urn:semrisk:entity:SR-CPT-012.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: Multi-method assessments possible; do not make functional globally.

## SR-REL-015 — producesAssessmentResult

Conceptual endpoints: SR-CPT-011 → SR-CPT-013.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-011. Asserted range: urn:semrisk:entity:SR-CPT-013.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: No process/result collapse.

## SR-REL-016 — assessmentResultConcerns

Conceptual endpoints: SR-CPT-013 → SR-CPT-001.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-013. Asserted range: urn:semrisk:entity:SR-CPT-001.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: One result may concern a compound context; exact semantics later.

## SR-REL-017 — supportedByEvidence

Conceptual endpoints: SR-CPT-011/013/020 → SR-CPT-020.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-020.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Evidence role is contextual, not intrinsic class identity.

## SR-REL-018 — generatedByObservation

Conceptual endpoints: SR-CPT-023 → SR-CPT-022.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-023. Asserted range: urn:semrisk:entity:SR-CPT-022.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Functionality only local hypothesis.

## SR-REL-019 — hasProvenance

Conceptual endpoints: information/result artifact → SR-CPT-021.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Exact PROV-O predicates chosen in #21/#26.

## SR-REL-020 — qualifiedByConfidence

Conceptual endpoints: SR-CPT-013/020 → SR-CPT-019.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-013. Asserted range: urn:semrisk:entity:SR-CPT-019.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Confidence/uncertainty exact representation unresolved.

## SR-REL-021 — selectsTreatmentStrategy

Conceptual endpoints: SR-CPT-001/033 → SR-CPT-026.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-026.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Decision event concept may need explicit representation in #25.

## SR-REL-022 — planImplementsStrategy

Conceptual endpoints: SR-CPT-027 → SR-CPT-026.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-027. Asserted range: urn:semrisk:entity:SR-CPT-026.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: No global cardinality.

## SR-REL-023 — activityExecutesPlan

Conceptual endpoints: SR-CPT-028 → SR-CPT-027.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-028. Asserted range: urn:semrisk:entity:SR-CPT-027.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Plan can exist without execution.

## SR-REL-024 — activityUsesControl

Conceptual endpoints: SR-CPT-028 → SR-CPT-029.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-028. Asserted range: urn:semrisk:entity:SR-CPT-029.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Control may preexist the activity; no identity collapse.

## SR-REL-025 — controlProtects

Conceptual endpoints: SR-CPT-029 → SR-CPT-002/037/039.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-029. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Do not equate presence of control with effectiveness.

## SR-REL-026 — hasRiskOwner

Conceptual endpoints: SR-CPT-001/033 → external Actor.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Replaces prior `bearsRiskOwnerRole` shorthand because Risk Owner is a role type, not a role individual.

## SR-REL-027 — assignsResponsibilityFor

Conceptual endpoints: SR-CPT-031 → SR-CPT-001/033/027.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-031. Asserted range: not asserted.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: Risk is not forced to be a mediated endurant; exact accountability vs responsibility specialization remains future work.

## SR-REL-028 — responsibilityAssignedTo

Conceptual endpoints: SR-CPT-031 → external Actor or SR-CPT-030.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-031. Asserted range: not asserted.

Multiplicity status: LOCAL_PROFILE_CONSTRAINT_SEPARATE. Inherited registry note: Mediation applies to endurant participants; exact actor ontology remains external.

## SR-REL-029 — registerContainsEntry

Conceptual endpoints: SR-CPT-032 → SR-CPT-033.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-032. Asserted range: urn:semrisk:entity:SR-CPT-033.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: No inference that register contains actual Risk phenomena.

## SR-REL-030 — hasWorkflowState

Conceptual endpoints: SR-CPT-033 → SR-CPT-036.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-033. Asserted range: urn:semrisk:entity:SR-CPT-036.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Closed must not imply Risk State cessation.

## SR-REL-031 — hasRiskState

Conceptual endpoints: SR-CPT-001 → SR-CPT-035.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-001. Asserted range: urn:semrisk:entity:SR-CPT-035.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Risk State boundary frozen by #70; no management/workflow labels in Core fixture.

## SR-REL-032 — precedesState

Conceptual endpoints: SR-CPT-035 or SR-CPT-036 → same state family.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Never use across Risk State vs Workflow State indiscriminately.

## SR-REL-033 — supersedesAssessmentResult

Conceptual endpoints: SR-CPT-013 → SR-CPT-013.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-013. Asserted range: urn:semrisk:entity:SR-CPT-013.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Do not delete/replace old result semantically.

## SR-REL-034 — basedOnPriorAssessment

Conceptual endpoints: SR-CPT-011 → SR-CPT-011/013.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Not every assessment is reassessment.

## SR-REL-035 — hasIndicator

Conceptual endpoints: SR-CPT-001/039 → SR-CPT-024.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-024.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: No claim that indicator is observation result itself.

## SR-REL-036 — hasThreshold

Conceptual endpoints: SR-CPT-024/012/044 → SR-CPT-025.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: urn:semrisk:entity:SR-CPT-025.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Not Core by default.

## SR-REL-037 — pharmaEntityInRiskContext

Conceptual endpoints: SR-CPT-001/006/007/008 → SR-CPT-040 or other CM-PharmE external entity.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: Exact bridge predicates finalized in #5/#21.

## SR-REL-038 — profileExtendsCoreConcept

Conceptual endpoints: profile concept → Core concept.

Formal status: PATTERN_OR_METADATA. Asserted domain: not asserted. Asserted range: not asserted.

Multiplicity status: NO_GLOBAL_OWL_MULTIPLICITY. Inherited registry note: May remain registry/mapping relation, not ontology property.

Current formal disposition: SR-REL-038 is an OWL annotation property, not an object-property edge; the earlier alternative remains historical.

## SR-REL-039 — hasExposedSubject

Conceptual endpoints: SR-CPT-010 → SR-CPT-002.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-010. Asserted range: urn:semrisk:entity:SR-CPT-002.

Multiplicity status: QUALIFIED_PROFILE_ONLY. Inherited registry note: No global functionality, causality or risk-score interpretation.

## SR-REL-040 — hasExposureSource

Conceptual endpoints: SR-CPT-010 → SR-CPT-003.

Formal status: OWL_OBJECT_PROPERTY. Asserted domain: urn:semrisk:entity:SR-CPT-010. Asserted range: urn:semrisk:entity:SR-CPT-003.

Multiplicity status: QUALIFIED_PROFILE_ONLY. Inherited registry note: No global functionality, causality or risk-score interpretation.

[Current relation audit](https://github.com/ArazSaieArasi3/SemRisk/blob/67247f13ba5d0c7d32163f2b3e848af15067d92e/foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv).

## Navigation

[Overview](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Overview) · [Domains and Concepts](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Domains-and-Concepts) · [Relations](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Relations) · [Formal Reference](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Formal-Reference) · [Diagrams and Explorer](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Diagrams-and-Explorer) · [Tutorial](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Tutorial) · [Sources and Limits](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Sources-and-Limits)

[Home](https://github.com/ArazSaieArasi3/SemRisk/wiki/Home) · [Versioned Pages](https://arazsaiearasi3.github.io/SemRisk/ontology/0.2.0-rc.4/docs-20261006/index.html) · [Canonical repository](https://github.com/ArazSaieArasi3/SemRisk/blob/67247f13ba5d0c7d32163f2b3e848af15067d92e/ontology/releases/0.2.0-rc.4/README.md)
