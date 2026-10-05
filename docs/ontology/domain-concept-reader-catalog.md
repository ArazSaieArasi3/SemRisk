# SemRisk domains, concepts and diagrams

This reader view is generated from the governed registries. It distinguishes the planned domain portfolio, conceptual assignments and the frozen formal candidate `0.1.0-rc.1`. It does not adopt new concepts or change an ontology definition.

The current tested successor is [0.2.0-rc.1](../../ontology/releases/0.2.0-rc.1/README.md), selected by [current-candidate.json](../../ontology/current-candidate.json). Its additional context terms are listed separately in the [profile IRI registry](../../ontology/releases/0.2.0-rc.1/profile-iri-registry.csv); the formal-count join below remains explicitly historical. The current concept registry includes the successor Trigger definition.

Start with [domain definitions](#domain-definitions), [domains and their concepts](#domains-and-their-concepts), [concept definitions](#concept-definitions), or [diagrams](#diagrams).

## Domain definitions

The following scope descriptions are copied from the [domain profile roadmap](../research/domain-profile-roadmap.md#2-priority-profile-portfolio). Priority is a planning priority, not implementation status. Core is the shared foundation; other rows are planned profiles. Method is a supporting module listed below, not a new application domain.

| Domain / profile | Scope definition from roadmap | Priority |
| --- | --- | --- |
| Core | Domain-neutral semantics of risk, value, scenario, assessment, evidence, treatment, control, observation and responsibility | `P0` |
| Enterprise | Operational enterprise risk knowledge, risk-register semantics, ownership, assessment lifecycle | `P0` |
| Architecture | Connect risk to objectives, capabilities, processes, applications, data, technology and change initiatives | `P0` |
| Health | Broad reusable risk profile across clinical, patient-safety, digital-health, public-health and care-delivery contexts | `P1` |
| Pharma | Pharmaceutical quality, pharmacovigilance, ecosystem, regulatory, supply and post-market risk | `P1` |
| Governance | Appetite, tolerance, policy, compliance, audit, issue, control accountability | `P2` |
| News | External event/claim/source/narrative signals for risk identification and reassessment | `P2` |
| Security | Threat, vulnerability, prevention, security mechanisms, cyber-risk monitoring | `P2` |
| Finance | Credit, liquidity, market, operational, counterparty, fraud, settlement and systemic risk | `P2` |
| SupplyChain | Supplier, dependency, disruption, logistics, resilience and propagation risk | `P2` |
| AI | AI-system risk, impact, compliance, model/data risk | `P3` |
| Environment | Environmental, exposure, cumulative and public-health risk | `P3` |

## Governed modules and implementation boundary

The [module registry](../../architecture/g2/module-profile-registry-v0.1.csv) also includes mapping and application packages. These ten architectural responsibilities are not ten implemented OWL domain ontologies. The six formal source modules are Core, Enterprise, Method, Governance, Pharma and Mappings; Architecture uses external references and Health has no standalone formal module in this candidate.

| Module | Type | Responsibility | Paper-1 status |
| --- | --- | --- | --- |
| Core | core | Domain-neutral risk/scenario/event/assessment/evidence/treatment/responsibility semantics. | REQUIRED |
| Enterprise | profile | Risk-register, workflow, ownership and operational enterprise application semantics. | REQUIRED |
| Architecture | mapping_package | Mappings from risk semantics to externally owned objective/capability/process architecture entities. | REQUIRED_SUPPORT |
| Method | profile | Assessment methods, scales, thresholds and method-specific values/constraints. | SUPPORT |
| Governance | profile | Appetite, tolerance, criteria, responsibility and governance-specific refinements. | SUPPORT |
| Pharma | profile | Bounded Pharma case/federation; risk-specific semantics remain SemRisk, pharma ecosystem entities remain CM-PharmE/external. | REQUIRED_CASE |
| Health | profile | Broad Health profile reserved for later source-backed expansion. | DEFERRED_PAPER2 |
| ExternalMappings | mapping_package | Machine-readable mappings/references to COVER, ROSE, PROV-O, CM-PharmE and future owners. | REQUIRED_SUPPORT |
| DataProjection | application_projection | RDB/schema mappings, SQL projection, data constraints and case fixtures. | POST_G2_EXECUTION |
| RiskIntelligence | future_application | News/Comment/Risk Intelligence runtime and dynamic forecasting. | DEFERRED_PAPER2 |

## Domains and their concepts

Membership below splits the exact `module_profile` field of the [concept registry](../../conceptualization/core/core-concept-registry-v0.1.csv) on `/`. Shared concepts therefore appear in more than one row. These are conceptual assignments, not OWL declaration ownership, subclass assertions, or additive counts. A blank portfolio area has no concept assigned in this registry; it is not proof that no research or source vocabulary exists for it.

| Domain / scope | Concepts currently assigned in registry |
| --- | --- |
| Core | SR-CPT-001 — Risk; SR-CPT-002 — Risk Subject; SR-CPT-003 — Risk Source; SR-CPT-004 — Predisposing Condition; SR-CPT-005 — Trigger; SR-CPT-006 — Risk Scenario; SR-CPT-007 — Risk Event; SR-CPT-008 — Consequence; SR-CPT-009 — Vulnerability; SR-CPT-010 — Exposure; SR-CPT-011 — Risk Assessment Activity; SR-CPT-013 — Risk Assessment Result; SR-CPT-014 — Likelihood Assessment Result; SR-CPT-015 — Impact Assessment Result; SR-CPT-017 — Inherent Risk Assessment Result; SR-CPT-018 — Residual Risk Assessment Result; SR-CPT-020 — Evidence Item; SR-CPT-021 — Provenance; SR-CPT-022 — Observation Activity; SR-CPT-023 — Observation Result; SR-CPT-026 — Risk Treatment Strategy; SR-CPT-027 — Risk Treatment Plan; SR-CPT-028 — Risk Treatment Activity; SR-CPT-029 — Control Mechanism; SR-CPT-030 — Risk Owner; SR-CPT-031 — Risk Responsibility; SR-CPT-033 — Risk Register Entry; SR-CPT-034 — Scenario Description; SR-CPT-035 — Risk State |
| Enterprise | SR-CPT-027 — Risk Treatment Plan; SR-CPT-030 — Risk Owner; SR-CPT-032 — Risk Register; SR-CPT-033 — Risk Register Entry; SR-CPT-034 — Scenario Description; SR-CPT-036 — Workflow State; SR-CPT-037 — Objective; SR-CPT-038 — Capability; SR-CPT-039 — Business Process |
| Architecture | SR-CPT-038 — Capability; SR-CPT-039 — Business Process |
| Health | SR-CPT-041 — Hazard; SR-CPT-042 — Harm |
| Pharma | SR-CPT-040 — Active Pharmaceutical Ingredient; SR-CPT-043 — Signal |
| Governance | SR-CPT-024 — Indicator; SR-CPT-025 — Threshold; SR-CPT-026 — Risk Treatment Strategy; SR-CPT-029 — Control Mechanism; SR-CPT-031 — Risk Responsibility; SR-CPT-044 — Risk Criteria; SR-CPT-045 — Risk Appetite; SR-CPT-046 — Risk Tolerance; SR-CPT-047 — Risk Nature |
| News | No assigned entries in this registry; planned portfolio scope. |
| Security | No assigned entries in this registry; planned portfolio scope. |
| Finance | No assigned entries in this registry; planned portfolio scope. |
| SupplyChain | No assigned entries in this registry; planned portfolio scope. |
| AI | No assigned entries in this registry; planned portfolio scope. |
| Environment | No assigned entries in this registry; planned portfolio scope. |
| Method | SR-CPT-012 — Risk Assessment Method; SR-CPT-016 — Risk Level Assessment Result; SR-CPT-019 — Assessment Confidence; SR-CPT-024 — Indicator; SR-CPT-025 — Threshold; SR-CPT-044 — Risk Criteria; SR-CPT-047 — Risk Nature |

## Concept definitions

All 47 definitions below are copied exactly from the concept registry. Formal status is joined by stable semantic ID to the [source-derived entity inventory](p1-r2-formal-source-entity-reference-v0.1.csv). Of these concepts, 35 are declared OWL classes and 4 are SKOS markers in the frozen candidate. The remaining concepts have no local declaration there; their conceptual status remains visible. A SKOS marker is not an OWL class.

| ID | Concept | Definition | Conceptual status | Formal declaration / module |
| --- | --- | --- | --- | --- |
| SR-CPT-001 | Risk | A context-dependent risk phenomenon or pattern concerning possible effects on value/objectives; distinct from records, descriptions, scores and workflow artifacts. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-002 | Risk Subject | An entity, value-bearing object or externally owned item about which risk relevance is asserted. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-003 | Risk Source | A risk-relevant origin, source or contextual contributor that may participate in a scenario or event; causal status is not implied by the label alone. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-004 | Predisposing Condition | A contextual state-of-affairs or situational condition that increases susceptibility to a risk-relevant event/effect without necessarily directly causing it. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-005 | Trigger | An occurrence acting as the initiating event for a risk-relevant event or process transition; an enabling condition is represented separately as a Predisposing Condition. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-006 | Risk Scenario | A possible or hypothesized risk-relevant configuration or event pattern used for analysis, distinct from descriptions and realized events. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-007 | Risk Event | A realized occurrence relevant to a risk context, distinct from a possible scenario and information artifacts describing it. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-008 | Consequence | A risk-relevant outcome or effect of an event/scenario; its magnitude/severity may be assessed separately. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-009 | Vulnerability | A disposition or condition that increases susceptibility to a risk-relevant event/effect. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-010 | Exposure | A context-dependent condition or relation indicating how a subject/value is exposed to a risk-relevant source/event; assessment scores remain separate. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-011 | Risk Assessment Activity | An activity applying a method, context and evidence to produce one or more risk assessment results. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-012 | Risk Assessment Method | A method or technique governing how assessment evidence/context is transformed into one or more assessment results. | CORE_SUPPORT_V0_1 | owl:Class / Method |
| SR-CPT-013 | Risk Assessment Result | A contextual, time-bound information/measurement result produced by a Risk Assessment Activity concerning a risk subject/context. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-014 | Likelihood Assessment Result | An assessment result concerning estimated likelihood/probability/frequency under a specified method and context. | CORE_REFINEMENT_V0_1 | owl:Class / Core |
| SR-CPT-015 | Impact Assessment Result | An assessment result concerning magnitude/severity of effects under a specified assessment method/context. | CORE_REFINEMENT_V0_1 | owl:Class / Core |
| SR-CPT-016 | Risk Level Assessment Result | A method-dependent overall risk rating/level produced from assessment evidence/results. | CORE_SUPPORT_V0_1 | owl:Class / Method |
| SR-CPT-017 | Inherent Risk Assessment Result | A risk assessment result representing a pre-treatment/pre-control assessment context. | CORE_REFINEMENT_V0_1 | owl:Class / Core |
| SR-CPT-018 | Residual Risk Assessment Result | A risk assessment result representing a post-treatment/control assessment context. | CORE_REFINEMENT_V0_1 | owl:Class / Core |
| SR-CPT-019 | Assessment Confidence | An information qualification stating confidence or uncertainty in a specified assessment result under a stated basis; it is distinct from estimated likelihood and from an intrinsic quality of the risk. | CORE_SUPPORT_V0_1 | owl:Class / Method |
| SR-CPT-020 | Evidence Item | An information artifact used in context to support, challenge or contextualize a risk-related assertion, assessment or decision. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-021 | Provenance | Information about origin, derivation, version, agent, time and transformation history of an artifact/assertion/result. | CORE_V0_1 | skos:Concept / Core |
| SR-CPT-022 | Observation Activity | An activity that observes/measures risk-relevant phenomena and may produce observation results. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-023 | Observation Result | An information/measurement result produced by an observation/monitoring activity and potentially used as evidence. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-024 | Indicator | A versioned specification of what is observed or computed to monitor a risk-relevant condition; each observation value or result is distinct from this specification. | CORE_SUPPORT_V0_1 | owl:Class / Method |
| SR-CPT-025 | Threshold | A versioned decision-boundary specification used with an indicator or assessment method; its comparison operator, scale, unit and applicability belong to the selected application profile, not to a universal risk formula. | METHOD_PROFILE_V0_1 | owl:Class / Method |
| SR-CPT-026 | Risk Treatment Strategy | A decision/information artifact specifying a high-level selected approach for addressing a risk. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-027 | Risk Treatment Plan | An information artifact specifying planned treatment activities, responsibilities, timing or resources. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-028 | Risk Treatment Activity | An activity performed to modify risk-relevant conditions, likelihood, consequences or preparedness. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-029 | Control Mechanism | A persistent mechanism, capability or implemented measure used in prevention, detection, protection or risk treatment. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-030 | Risk Owner | A context-dependent role classification of persons, organizations or other eligible external actors bearing specified risk-management responsibilities; bearer identity is supplied by the external actor kinds, not by ownership. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-031 | Risk Responsibility | A concrete responsibility/accountability assignment context that depends on an Actor/role bearer and any modeled governance participants, and is about the Risk, artifact, plan or obligation it concerns. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-032 | Risk Register | A managed repository/collection of Risk Register Entries for a defined organizational or analytical scope. | ENTERPRISE_PROFILE_V0_1 | owl:Class / Enterprise |
| SR-CPT-033 | Risk Register Entry | A governed information artifact in a risk register recording risk-related description, assessments, ownership, treatment and workflow information. | CORE_INFORMATION_ARTIFACT_V0_1 | owl:Class / Enterprise |
| SR-CPT-034 | Scenario Description | An information artifact describing a Risk Scenario, event chain, assumptions or consequences. | CORE_INFORMATION_ARTIFACT_V0_1 | owl:Class / Enterprise |
| SR-CPT-035 | Risk State | A time- and context-bound state-of-affairs concerning the governed Risk context, distinct from assessment results, record/workflow progression and management/monitoring classifications. | CORE_V0_1 | owl:Class / Core |
| SR-CPT-036 | Workflow State | A state of a management record/process indicating processing/progression, independent from the existence/state of the underlying risk. | ENTERPRISE_PROFILE_V0_1 | owl:Class / Enterprise |
| SR-CPT-037 | Objective | An externally owned enterprise/governance objective that may be affected by or provide context for risk. | EXTERNAL_OWNER_REFERENCE | skos:Concept / Mappings |
| SR-CPT-038 | Capability | An externally owned enterprise capability that may be exposed to/affected by risk. | EXTERNAL_OWNER_REFERENCE | skos:Concept / Mappings |
| SR-CPT-039 | Business Process | An externally owned process/business activity context that may generate, encounter or be affected by risk. | EXTERNAL_OWNER_REFERENCE | skos:Concept / Mappings |
| SR-CPT-040 | Active Pharmaceutical Ingredient | A pharmaceutical ingredient/entity referenced in Pharma shortage evidence; the frozen CM-PharmE v1.0.0 catalog does not contain an API/INN concept. | EXTERNAL_OWNER_REFERENCE_UNMAPPED | Not declared in frozen candidate |
| SR-CPT-041 | Hazard | A potential source of harm under safety/medical-device semantics. | PROFILE_DEFERRED | Not declared in frozen candidate |
| SR-CPT-042 | Harm | A negative consequence affecting an entity/value under safety/medical-device semantics. | PROFILE_DEFERRED | Not declared in frozen candidate |
| SR-CPT-043 | Signal | An information-level indication suggesting a potentially important risk-relevant pattern requiring assessment; detailed semantics are domain-specific. | PROFILE_OPTIONAL | Not declared in frozen candidate |
| SR-CPT-044 | Risk Criteria | Information/decision criteria used to evaluate significance, acceptability or treatment choices in a specified governance/method context. | PROFILE_SUPPORT | Not declared in frozen candidate |
| SR-CPT-045 | Risk Appetite | A governance-level expression of the type/amount of risk an organization is prepared to pursue or retain, under a specified framework. | PROFILE_SUPPORT | Not declared in frozen candidate |
| SR-CPT-046 | Risk Tolerance | A governance/method expression of permitted variation/bounds around objectives or risk criteria in a specified framework. | PROFILE_SUPPORT | Not declared in frozen candidate |
| SR-CPT-047 | Risk Nature | A polarity/classification construct expressing threat/opportunity framing without asserting separate universal Risk identities. | UNRESOLVED_CANDIDATE | Not declared in frozen candidate |

## Diagrams

| View | Link | Boundary |
| --- | --- | --- |
| Ontology atlas | [Open SVG](diagrams/p1-r2-local-ontology-atlas-v0.1.svg) | All 76 local IDs: 35 OWL classes, 37 object properties and 4 SKOS markers, grouped by formal module. |
| Relation diagram | [Open SVG](diagrams/p1-r2-local-relations-v0.1.svg) | Asserted signatures of all 37 object properties; no inferred causal interpretation or cardinality. |
| Formal reference | [Read definitions and assertions](generated/p1-r2-generated-reference.md) | Generated from the exact formal source; external imports are distinguished from local entities. |
| WebVOWL | [Bundle and local viewing instructions](generated/webvowl-viewer-candidate-v0.1/README.md) | Candidate files exist. GitHub displays their source; this link is not a hosted interactive viewer. |

At the 2026-10-02 repository metadata check, GitHub Pages was disabled. Public WebVOWL availability still requires the #56 license disposition, a new versioned candidate with visible gUFO attribution and disabled dormant upload paths, and #119/#117 browser/accessibility/public-access QA. The old `site/ontology/0.1.0-rc.1/` route remains frozen. No public viewer URL or calendar delivery date is claimed here.

## Rebuild and authority

Run `python tools/build_ontology_reader_catalog.py` to regenerate or add `--check` to detect drift. The concept registry owns conceptual definitions, the module/ownership registries own architecture decisions, and Turtle owns formal assertions. The roadmap describes future scope. This page is a reading aid, not a fourth authority.
