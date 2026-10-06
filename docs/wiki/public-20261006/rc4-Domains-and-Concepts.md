# All 47 concepts and domain assignments

> Ontology documentation candidate 0.2.0-rc.4. Source snapshot `67247f13ba5d0c7d32163f2b3e848af15067d92e`. Not a scholarly release or independent domain validation. No manuscript is included.

Concept definitions below are copied from the governed concept registry. Module/profile assignments are not OWL subclass assertions. Planned domain scopes are available in the [domain portfolio](https://arazsaiearasi3.github.io/SemRisk/ontology/0.2.0-rc.4/docs-20261006/catalog.html#domains); planning priority does not mean implementation.

## SR-CPT-001 — Risk

A context-dependent risk phenomenon or pattern concerning possible effects on value/objectives; distinct from records, descriptions, scores and workflow artifacts.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Foundational category intentionally remains a derived pattern. Identity continuity follows the #69 contract; mutable record/assessment/state/ownership/treatment fields do not automatically define or replace Risk identity.

## SR-CPT-002 — Risk Subject

An entity, value-bearing object or externally owned item about which risk relevance is asserted.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Should remain minimal to avoid generic Object inflation; exact relation to Value/Objectives handled in #20/#25.

## SR-CPT-003 — Risk Source

A risk-relevant origin, source or contextual contributor that may participate in a scenario or event; causal status is not implied by the label alone.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Must not collapse Cause, Trigger, Threat and Predisposing Condition.

## SR-CPT-004 — Predisposing Condition

A contextual state-of-affairs or situational condition that increases susceptibility to a risk-relevant event/effect without necessarily directly causing it.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Boundary with Vulnerability is foundationally frozen: Predisposing Condition is situational; intrinsic disposition-like susceptibility maps to Vulnerability or an explicit profile refinement.

## SR-CPT-005 — Trigger

An occurrence acting as the initiating event for a risk-relevant event or process transition; an enabling condition is represented separately as a Predisposing Condition.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: May be event, threshold condition or role depending context; #20 must model relation semantics carefully. Run 4: event-only definition clarified; successor formal bundle 0.2.0-rc.1 carries the matching annotation; frozen 0.1.0-rc.1 retained.

Current disposition: Trigger is event-only; enabling conditions are modeled separately. The older alternatives are superseded by the current definition.

## SR-CPT-006 — Risk Scenario

A risk-relevant situation type specifying a possible configuration, whether or not instantiated; separate from the managed descriptions that express it and from realized events.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-007 — Risk Event

A realized occurrence relevant to a risk context, distinct from a possible scenario and information artifacts describing it.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Incident may be a profile refinement; event type vs occurrence requires #25.

## SR-CPT-008 — Consequence

A risk-relevant outcome or effect of an event/scenario; its magnitude/severity may be assessed separately.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Must remain distinct from Impact Assessment Result.

## SR-CPT-009 — Vulnerability

A disposition or condition that increases susceptibility to a risk-relevant event/effect.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Cross-domain polysemy remains; profile refinements required.

## SR-CPT-010 — Exposure

A context-dependent condition or relation indicating how a subject/value is exposed to a risk-relevant source/event; assessment scores remain separate.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Financial amount, physical exposure and exposure rating must not be unified without explicit mapping.

## SR-CPT-011 — Risk Assessment Activity

An activity applying a method, context and evidence to produce one or more risk assessment results.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Must never merge with result.

## SR-CPT-012 — Risk Assessment Method

A method or technique governing how assessment evidence/context is transformed into one or more assessment results.

Scope: Method. Status: CORE_SUPPORT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-013 — Risk Assessment Result

A contextual, time-bound information/measurement result produced by a Risk Assessment Activity concerning a risk subject/context.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-014 — Likelihood Assessment Result

An assessment result concerning estimated likelihood/probability/frequency under a specified method and context.

Scope: Core. Status: CORE_REFINEMENT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-015 — Impact Assessment Result

An assessment result concerning magnitude/severity of effects under a specified assessment method/context.

Scope: Core. Status: CORE_REFINEMENT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-016 — Risk Level Assessment Result

A method-dependent overall risk rating/level produced from assessment evidence/results.

Scope: Method. Status: CORE_SUPPORT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-017 — Inherent Risk Assessment Result

A risk assessment result representing a pre-treatment/pre-control assessment context.

Scope: Core. Status: CORE_REFINEMENT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-018 — Residual Risk Assessment Result

A risk assessment result representing a post-treatment/control assessment context.

Scope: Core. Status: CORE_REFINEMENT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-019 — Assessment Confidence

An information qualification stating confidence or uncertainty in a specified assessment result under a stated basis; it is distinct from estimated likelihood and from an intrinsic quality of the risk.

Scope: Method. Status: CORE_SUPPORT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-020 — Evidence Item

An information artifact used in context to support, challenge or contextualize a risk-related assertion, assessment or decision.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-021 — Provenance

Information about origin, derivation, version, agent, time and transformation history of an artifact/assertion/result.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Prefer reuse/alignment to PROV-O over local reinvention.

## SR-CPT-022 — Observation Activity

An activity that observes/measures risk-relevant phenomena and may produce observation results.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Monitoring may include broader process semantics; exact alignment pending.

## SR-CPT-023 — Observation Result

An information/measurement result produced by an observation/monitoring activity and potentially used as evidence.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-024 — Indicator

A versioned specification of what is observed or computed to monitor a risk-relevant condition; each observation value or result is distinct from this specification.

Scope: Method/Governance. Status: CORE_SUPPORT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-025 — Threshold

A versioned decision-boundary specification used with an indicator or assessment method; its comparison operator, scale, unit and applicability belong to the selected application profile, not to a universal risk formula.

Scope: Method/Governance. Status: METHOD_PROFILE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-026 — Risk Treatment Strategy

A decision/information artifact specifying a high-level selected approach for addressing a risk.

Scope: Core/Governance. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-027 — Risk Treatment Plan

An information artifact specifying planned treatment activities, responsibilities, timing or resources.

Scope: Core/Enterprise. Status: CORE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-028 — Risk Treatment Activity

An activity performed to modify risk-relevant conditions, likelihood, consequences or preparedness.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Activity must not be collapsed into persistent Control Mechanism.

## SR-CPT-029 — Control Mechanism

A persistent mechanism, capability or implemented measure used in prevention, detection, protection or risk treatment.

Scope: Core/Governance. Status: CORE_V0_1.

Inherited registry note: Exact ROSE reuse vs local superpattern owned by #21; do not declare novel yet.

## SR-CPT-030 — Risk Owner

A context-dependent role classification of persons, organizations or other eligible external actors bearing specified risk-management responsibilities; bearer identity is supplied by the external actor kinds, not by ownership.

Scope: Core/Enterprise. Status: CORE_V0_1.

Inherited registry note: Broad ownership is anti-rigid and cross-kind; narrower roles need their external identity provider. No local Person/Organization kind is introduced.

## SR-CPT-031 — Risk Responsibility

A concrete responsibility/accountability assignment context that depends on an Actor/role bearer and any modeled governance participants, and is about the Risk, artifact, plan or obligation it concerns.

Scope: Core/Governance. Status: CORE_V0_1.

Inherited registry note: Mediation applies to endurant participants; Risk is an aboutness/assignment target under the #71 grounding contract. Responsibility vs accountability may require later subpattern.

## SR-CPT-032 — Risk Register

A governed information artifact organizing risk register entries for a defined scope; its managed identity persists as entries are added or removed.

Scope: Enterprise. Status: ENTERPRISE_PROFILE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-033 — Risk Register Entry

A governed information artifact in a risk register recording risk-related description, assessments, ownership, treatment and workflow information.

Scope: Core/Enterprise. Status: CORE_INFORMATION_ARTIFACT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-034 — Scenario Description

An information artifact describing a Risk Scenario, event chain, assumptions or consequences.

Scope: Core/Enterprise. Status: CORE_INFORMATION_ARTIFACT_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-035 — Risk State

A time- and context-bound state-of-affairs concerning the governed Risk context, distinct from assessment results, record/workflow progression and management/monitoring classifications.

Scope: Core. Status: CORE_V0_1.

Inherited registry note: Core Risk State is reserved for situational state-of-affairs. Workflow, management-attention, escalation and monitoring labels remain outside Core unless a later profile introduces them explicitly.

## SR-CPT-036 — Workflow State

A reusable nominal workflow-status value interpreted within an explicit scheme version; distinct from each record-specific temporal status attribution and from the underlying Risk State.

Scope: Enterprise. Status: ENTERPRISE_PROFILE_V0_1.

Inherited registry note: Identity decision implemented in 0.2.0-rc.3; editable OntoUML and expanded SQL projection remain separate gates. See foundational/semantic-identity-v0.2.0-rc.3/decisions.md.

## SR-CPT-037 — Objective

An externally owned enterprise/governance objective that may be affected by or provide context for risk.

Scope: Enterprise. Status: EXTERNAL_OWNER_REFERENCE.

Inherited registry note: Not SemRisk Core-owned.

## SR-CPT-038 — Capability

An externally owned enterprise capability that may be exposed to/affected by risk.

Scope: Enterprise/Architecture. Status: EXTERNAL_OWNER_REFERENCE.

Inherited registry note: Not SemRisk Core-owned.

## SR-CPT-039 — Business Process

An externally owned process/business activity context that may generate, encounter or be affected by risk.

Scope: Enterprise/Architecture. Status: EXTERNAL_OWNER_REFERENCE.

Inherited registry note: Risk Assessment/Treatment Activities remain SemRisk activities; business process taxonomy does not.

## SR-CPT-040 — Active Pharmaceutical Ingredient

A pharmaceutical ingredient/entity referenced in Pharma shortage evidence; the frozen CM-PharmE v1.0.0 catalog does not contain an API/INN concept.

Scope: Pharma. Status: EXTERNAL_OWNER_REFERENCE_UNMAPPED.

Inherited registry note: Do not mint duplicate SemRisk Core class; do not attribute API ownership to CM-PharmE v1.0.0.

## SR-CPT-041 — Hazard

A potential source of harm under safety/medical-device semantics.

Scope: Health. Status: PROFILE_DEFERRED.

Inherited registry note: Full Health profile outside Paper 1.

## SR-CPT-042 — Harm

A negative consequence affecting an entity/value under safety/medical-device semantics.

Scope: Health. Status: PROFILE_DEFERRED.

Inherited registry note: Narrower than generic Consequence; full Health profile deferred.

## SR-CPT-043 — Signal

An information-level indication suggesting a potentially important risk-relevant pattern requiring assessment; detailed semantics are domain-specific.

Scope: Pharma. Status: PROFILE_OPTIONAL.

Inherited registry note: Not synonym of Risk/Event/Evidence; detailed PV runtime outside Paper 1.

## SR-CPT-044 — Risk Criteria

Information/decision criteria used to evaluate significance, acceptability or treatment choices in a specified governance/method context.

Scope: Governance/Method. Status: PROFILE_SUPPORT.

Inherited registry note: Threshold values/scales remain method-specific.

## SR-CPT-045 — Risk Appetite

A governance-level expression of the type/amount of risk an organization is prepared to pursue or retain, under a specified framework.

Scope: Governance. Status: PROFILE_SUPPORT.

Inherited registry note: Framework-specific definitions; not intrinsic Risk property.

## SR-CPT-046 — Risk Tolerance

A governance/method expression of permitted variation/bounds around objectives or risk criteria in a specified framework.

Scope: Governance. Status: PROFILE_SUPPORT.

Inherited registry note: Do not merge with appetite.

## SR-CPT-047 — Risk Nature

A polarity/classification construct expressing threat/opportunity framing without asserting separate universal Risk identities.

Scope: Method/Governance. Status: UNRESOLVED_CANDIDATE.

Inherited registry note: Threat/opportunity identity remains open; Critical only if manuscript claims it.

[Governed concept registry](https://github.com/ArazSaieArasi3/SemRisk/blob/67247f13ba5d0c7d32163f2b3e848af15067d92e/conceptualization/core/core-concept-registry-v0.1.csv).

## Navigation

[Overview](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Overview) · [Domains and Concepts](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Domains-and-Concepts) · [Relations](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Relations) · [Formal Reference](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Formal-Reference) · [Diagrams and Explorer](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Diagrams-and-Explorer) · [Tutorial](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Tutorial) · [Sources and Limits](https://github.com/ArazSaieArasi3/SemRisk/wiki/rc4-Sources-and-Limits)

[Home](https://github.com/ArazSaieArasi3/SemRisk/wiki/Home) · [Versioned Pages](https://arazsaiearasi3.github.io/SemRisk/ontology/0.2.0-rc.4/docs-20261006/index.html) · [Canonical repository](https://github.com/ArazSaieArasi3/SemRisk/blob/67247f13ba5d0c7d32163f2b3e848af15067d92e/ontology/releases/0.2.0-rc.4/README.md)
