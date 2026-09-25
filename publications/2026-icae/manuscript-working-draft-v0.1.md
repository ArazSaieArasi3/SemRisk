# SemRisk: An Evidence-Grounded and Well-Founded Semantic Architecture for Operational Risk Knowledge

**Working manuscript draft v0.1 — 2026-09-24**  
**Target:** ICAE 2026, Track 2 / Cluster B — Informatics & AI  
**Status:** PRELIMINARY EVIDENCE-BOUND DRAFT. Expert semantic validation (#51/#30), final E10/E11 evaluation (#31), threats/claim calibration (#56/#53), assurance (#54), publication-bound release (#55), and final venue audit (#35) remain pending.

## Abstract — provisional

Operational risk-management artifacts commonly mix several semantically different things: the underlying risk being managed, possible scenarios, realized events, narrative descriptions, register records, assessment activities and results, workflow states, evidence, responsibilities, treatments, and controls. Such conflation complicates interoperability, reasoning, traceability, and faithful implementation across semantic and relational representations. This paper presents SemRisk, an evidence-grounded and well-founded semantic architecture for operational risk knowledge. SemRisk was developed through governed evidence synthesis and semantic reconciliation, explicit reuse and external-ownership decisions, UFO/gUFO-informed foundational analysis, modular OWL/SHACL formalization, and bounded enterprise and pharmaceutical applications. The current Paper-1 candidate is implemented as a modular ontology with a PostgreSQL projection and a bounded end-to-end pharmaceutical scenario. Formal and structural evaluation reports successful parsing, OWL 2 DL profile validation, HermiT consistency and named-class satisfiability, release-critical traceability, negative-control sensitivity, and governed constraint checks. In application evaluation, all 40 original competency questions are retained; 26 are executable, seven partially executable, six conceptual-only, and one explicitly deferred. Eight predeclared SQL↔SPARQL tasks show five task-equivalent results, two equivalent after declared normalization, and one explicit partial representation. These results support bounded formal and executable claims, while expert semantic validation and final transferability/claim calibration remain pending. SemRisk therefore provides a controlled basis for separating risk phenomena from operational artifacts and for evaluating how those semantics survive enterprise, database, and domain-specific projections without claiming universal risk-domain validity.

**Keywords:** risk ontology; ontology engineering; enterprise risk management; semantic interoperability; knowledge representation; OntoUML; OWL; risk register

## I. Introduction

Risk management is routinely implemented through registers, spreadsheets, workflow systems, reports, dashboards, and assessment methods. These artifacts are operationally useful, but they often encourage a schema-centered view in which columns such as “risk”, “scenario”, “event”, “owner”, “status”, “likelihood”, “impact”, “residual risk”, and “treatment” are treated as if they belonged to one semantic layer. This creates a recurring modeling problem: a real-world risk phenomenon can become conflated with the record used to document it; a possible scenario with a realized event; an assessment activity with the assessment result it produces; a workflow status with the modeled state of the risk; or a responsible actor with the role or responsibility assignment through which accountability is established.

For semantic interoperability, these distinctions matter. A register entry can be opened or closed without logically creating or eliminating the underlying risk. A scenario description is an information artifact, not the scenario or event itself. Inherent and residual risk are often better interpreted as contextual assessment results about the same underlying risk rather than as timeless subclasses of Risk. Likewise, a treatment strategy, a plan, an executed activity, and a persistent control mechanism may be operationally related but should not be collapsed into a single concept when their identities and lifecycles differ.

SemRisk addresses this problem through a bounded ontology-engineering study. The work does not attempt to define a universal ontology for every risk domain. Instead, it investigates whether an evidence-grounded, well-founded, formally implemented semantic pattern can preserve claim-critical distinctions while remaining operationally usable in an enterprise risk-register context and in one bounded pharmaceutical federation case.

The study is organized around three research questions. **SR-RQ1** asks how a SemRisk Core can preserve the distinctions among risk phenomenon, event, scenario, scenario description, register record, assessment activity/result, risk state, workflow state, evidence, treatment/control, and responsibility. **SR-RQ2** asks to what extent those semantics can be operationalized for enterprise risk management and a real Jira-style register schema without treating the database or spreadsheet schema as ontology truth. **SR-RQ3** asks to what extent the same Core pattern can be federated with CM-PharmE for a bounded pharmaceutical case while preserving external semantic ownership and making context-dependent or unmapped semantics visible.

The corresponding contributions are: **SR-C1**, a well-founded operational risk semantic pattern; **SR-C2**, an enterprise operationalization with an executable relational projection; and **SR-C3**, a bounded pharmaceutical federation case. The database projection, negative-control pipeline, and evaluation framework are supporting credibility mechanisms rather than separate novelty claims.

## II. Related Work and Semantic Gap

SemRisk is positioned relative to existing risk ontologies, conceptual models, standards, enterprise-risk frameworks, and operational risk-register representations. The comparison baseline currently includes 12 closest or materially relevant comparators evaluated across 17 common dimensions, producing 204 evidence cells. The purpose of this comparison is not to produce a league table or an overall winner, but to determine which semantic capabilities are already established, where SemRisk reuses or aligns with prior work, and which integrated distinctions require explicit treatment in the present architecture.

Existing work contributes important pieces of the problem. Foundational risk ontologies such as COVER and related security/risk models provide semantics for risk-related entities and relations. Risk-register and GRC-oriented approaches contribute operational structures, register concepts, governance context, or relational implementations. Standards and frameworks including the ISO 31000 family, NIST IR 8286, COSO ERM, OCEG, Risk IT, IEC 31010, and ICH Q9 provide authoritative terminology, processes, roles, and method contexts. Domain ontologies such as CM-PharmE provide externally owned semantics for pharmaceutical entities that should not be silently duplicated by a risk ontology.

The bounded gap addressed by SemRisk is therefore not “the absence of a risk ontology”. Rather, it is the need for an explicitly governed semantic architecture that integrates several distinctions simultaneously: risk phenomenon versus information artifact; scenario versus realized event versus scenario description; assessment activity versus result; risk state versus workflow state; contextual inherent/residual assessment results; responsibility-derived ownership; treatment strategy versus plan/activity/control; evidence/provenance; external semantic ownership; and executable projection into operational data structures.

This gap statement remains deliberately descriptive. Current evidence supports bounded differentiation hypotheses, but final comparative wording is reserved for E10 and claim calibration because missing documentation in a comparator cannot be treated as evidence of absence.

## III. Research and Ontology-Engineering Method

### A. Study Design and Evidence Roles

Paper 1 is an ontology-engineering design research study with evidence-synthesis, bounded case/application, executable projection, and claim-dependent evaluation components. Evidence is governed by explicit roles: discovery, design, reconciliation, illustrative, regression, independent validation, holdout, comparative, and future-only. A central control rule is that an artifact that materially shaped a semantic commitment cannot later be described as independent validation of that same commitment unless an untouched partition or genuinely independent source exists.

This rule is important for the operational Jira schema and the pharmaceutical evidence. The Jira artifact shaped design and reconciliation and is therefore valid for operational mapping and regression, but not for independent semantic validation. DS-003, the bounded pharmaceutical source used for the case, likewise contributed to case semantics and is treated as design/reconciliation/illustrative evidence. Synthetic data are regression and application fixtures only. DS-002 is protected as a possible record-level holdout candidate for later bounded transferability evaluation.

### B. Evidence Acquisition and Semantic Reconciliation

Source mining and reconciliation were executed before formalization. The process produced a governed raw-to-canonical semantic pipeline rather than promoting each observed field or label directly into an ontology class. Cross-source reconciliation classified 274 raw rows and retained 191 canonical or unique concept candidates plus 175 relation/event/state/activity candidates, while preserving bounded-pending sources rather than forcing premature closure.

A ubiquitous-language stage then stabilized 43 preferred terms, recorded 20 terminology conflicts or false friends, 22 anti-concepts, 29 mappings, and 15 rename/migration lineage decisions. These controls are important because common risk labels can hide different ontological categories. For example, “owner” may refer to an actor, a role, or a responsibility assignment; “residual risk” may refer to a contextual result rather than a second Risk entity; and “status” may refer to workflow rather than risk state.

The requirements stage froze 20 semantic requirements and 40 competency questions. The original questions were retained through later execution rather than rewritten after implementation to improve apparent coverage.

### C. Reuse, Architecture, and External Ownership

SemRisk uses an explicit reuse/reference policy. COVER and ROSE are referenced and aligned by default; import or equivalence requires stronger evidence and additional gates. No `owl:equivalentClass` or `owl:equivalentProperty` relationship is inferred from lexical similarity. CM-PharmE entities remain externally owned in the pharmaceutical bridge. The Core is kept independent of profiles and application projections, while Enterprise, Method, Governance, and Pharma modules depend on or specialize the Core.

The Paper-1 architecture assigns each release-critical concept or relation to exactly one governed semantic owner or external owner. The publication subset is a governed view of that architecture, not a second ontology.

### D. Foundational Analysis and Formalization

Foundational analysis used UFO/gUFO/OntoUML to examine identity, dependence, roles, relators, qualities, dispositions, events, situations, information objects, participation, mediation, characterization, and material/formal relations. Thirty-three release-critical concepts and 38 release-critical relations were reviewed, seven high-risk foundational questions were resolved, 15 anti-pattern findings were retained, and seven alternative categorizations were preserved.

One material correction illustrates the value of the foundational step. The initial owner relation risked treating Risk Owner as if it were an individual role object. The corrected design interprets Risk Owner as a role type and Risk Responsibility as the assignment/relator that connects an actor to a risk. `hasRiskOwner` is therefore derived rather than stored as a primitive owner attribute.

Formalization then separated semantic axioms, SHACL constraints, rules, and implementation concerns. The Paper-1 candidate is modular OWL/RDF/Turtle with SHACL Core constraints and a governed SPARQL CONSTRUCT rule for derived ownership. The formal candidate is version-bound as P1-R2 / 0.1.0-rc.1 and is built through deterministic CI with pinned dependencies and external ontology bindings.

## IV. SemRisk Semantic Architecture

### A. Core Distinctions

The central design principle is to preserve identities that operational systems frequently collapse.

A **Risk** represents the underlying managed risk context or phenomenon. A **Risk Register Entry** is an information artifact that concerns a Risk. Multiple records may therefore refer to the same underlying Risk, and record lifecycle changes do not logically create or destroy that Risk.

A **Risk Scenario** represents a possible structured situation or course of events. A **Risk Event** is a realized occurrence. A **Scenario Description** is an information artifact that describes a scenario. These three are related but ontologically distinct.

A **Risk Assessment Activity** is the activity of assessing. A **Risk Assessment Result** is an outcome of that activity. Likelihood, impact, inherent, and residual interpretations are contextualized through assessment method, time, evidence, and treatment context rather than treated as timeless risk identities.

**Risk State** and **Workflow State** are likewise separated. A record may be administratively closed while the underlying modeled risk remains active, uncertain, treated, monitored, or otherwise not ceased. Workflow history belongs to the information/management process; risk-state history concerns the modeled risk context.

Treatment is represented as a sequence of distinct semantics: **Risk Treatment Strategy**, **Treatment Plan**, **Treatment Activity**, and **Control Mechanism**. This avoids treating a persistent control, a planned activity, and an abstract strategy as interchangeable. The existence or use of a Control Mechanism is not treated as evidence of control design adequacy, operating effectiveness, assurance success, or measured risk reduction.

Evidence and provenance remain explicit. Evidence items, observation or assessment results, source/version identifiers, derivation notes, and provenance activities are represented without reducing provenance to a source URL alone.

### B. Modules and Federation

SemRisk is modularized into Core, Enterprise, Method, Governance, and Pharma concerns. External enterprise or domain semantics are referenced rather than absorbed into the Core when their identity belongs elsewhere. In the Pharma case, CM-PharmE v1.0.0 remains the semantic owner of pharmaceutical entities. SemRisk contributes risk-specific participation or contextual relations around those external entities.

### C. Temporal Assessment and Responsibility

Reassessment is modeled as a new assessment activity linked to a prior assessment, producing a new result that may supersede an earlier result while preserving the identity of the underlying Risk. This supports historical inherent/residual or pre/post-treatment interpretations without minting a second Risk by default.

Responsibility is modeled through an actor–responsibility–risk pattern. The owner view is derived from the responsibility structure, providing an explicit semantic truthmaker and avoiding schema-driven primitive ownership.

## V. Operationalization and Bounded Pharmaceutical Case

### A. Operational Risk-Register Mapping

The operational source is a Jira-style risk-register schema with 27 governed attributes. All 27 fields have semantic dispositions in the master mapping rather than a class-per-column transformation. A field may map to a concept, relation, result, workflow value, profile term, metadata artifact, or an explicitly partial/deferred status.

This mapping provides evidence that the Core can be operationalized without making the spreadsheet schema the canonical semantic model. Because the complete schema influenced conceptualization, its 27/27 coverage is an operational mapping result, not an independent correctness percentage and not evidence of complete enterprise-risk-management or generic risk-register functionality. Common capabilities such as delegation/RACI, control assurance/effectiveness, due-date/escalation governance, portfolio aggregation and emerging/systemic-risk management remain outside the demonstrated Paper-1 operational scope.

### B. Relational Projection

A PostgreSQL relational twin implements the Paper-1 projection. The projection preserves stable semantic identities where possible, separates Core, assessment, treatment, enterprise, provenance, reference, Pharma, and governance structures, and exposes selected derived views such as risk ownership.

Relational constraints are interpreted as application-level closed-world controls, not as OWL entailments. Conversely, absence of an RDF triple is not interpreted as universal negation. This open-world/closed-world distinction is made explicit in the parity evaluation.

### C. Bounded Pharma Federation

The bounded Pharma case uses DS-003 as a qualified qualitative source and CM-PharmE v1.0.0 as an external semantic owner. DS-003 contributes source-supported conditions, actor/context evidence, and a proposed pooled-procurement treatment strategy. The source is a purposive expert study and is therefore not used to support prevalence or universal causal generalization.

The mapping package contains 18 governed DS-003 elements: seven direct/context mappings, ten partial mappings, and one unobserved item. DS-004 remains blocked for file-level evaluated mapping until exact files, version, license, checksums, columns, and quality metrics are frozen. DS-002 remains protected as a potential record-level holdout source and has not been opened for design use.

### D. Executable End-to-End Scenario

A predeclared end-to-end scenario connects the source-grounded Pharma semantics to explicitly synthetic execution artifacts. The scenario contains DS-003-supported predisposing conditions and a proposed treatment strategy, then adds synthetic trigger, realized event, consequence, register entry, owner responsibility, plan, treatment activity, control, pre-treatment assessment, post-treatment reassessment, risk-state history, and workflow-state history.

Ten expected-answer families were frozen before execution. The PostgreSQL run returns one realized synthetic event, two temporal assessment results, and one derived owner. The RDF graph contains the corresponding semantic path. The synthetic extension exists only to exercise the model and is not evidence of real treatment effectiveness, causal strength, prevalence, or prediction.

## VI. Evaluation

### A. E1–E4 Formal, Logical, Structural, and Foundational Evaluation

The E1–E4 package contains 21 declared evaluation records, all of which pass for their bounded criteria. Fourteen governed Turtle inputs parse successfully. The candidate passes OWL 2 DL profile validation under the declared toolchain. HermiT classification reports consistency for the governed closure, expected entailments are present, and an explicit post-reasoning satisfiability check finds no named SemRisk class classified as `owl:Nothing`.

Structural checks report 71/71 release-critical semantic IDs present, unique canonical IDs and IRIs, zero unapproved OWL equivalence mappings, and controlled dependency/test isolation. The positive SHACL fixture conforms, while five of five known-negative SHACL fixtures fail as expected. The owner-derivation rule constructs the expected `hasRiskOwner` triple.

E4 reuses the frozen foundational review: 33/33 release-critical concepts and 38/38 release-critical relations have foundational dispositions or rationales, and all seven high-risk foundational conditions identified at G2 were resolved for the Paper-1 subset.

These results establish formal, structural, and foundational verification evidence only. They do not establish domain correctness or universal ontology quality.

### B. E5–E6 Semantic, Expert, Standards, Operational, and Dataset Validation

E6 has been assembled as a bounded evidence-validation package. The standards/framework crosswalk currently contains 11 rows, of which nine are applicable to Paper-1 alignment discussion and two are explicitly out of scope. The strongest operational alignment evidence concerns the NIST IR 8286 family, while ISO 31000/31073, IEC 31010, COSO, OCEG, Risk IT, ICH Q9, and architecture guidance are interpreted as bounded terminology/process/profile alignments rather than conformance certifications.

Operational mapping reports 27/27 Jira fields dispositioned. DS-003 reports 18/18 governed elements dispositioned. These denominators describe mapping governance, not semantic correctness percentages.

E5 human semantic validation remains pending. The expert-review protocol, reviewer eligibility matrix, 20-item review instrument, response template, and adjudication rules are frozen before any reviewer response. The protocol preserves `NOT_ASSESSED`, reviewer disagreement, independence information, and Critical/High findings rather than averaging them away. No expert response is fabricated in the present draft.

### C. E8 Application, Query, and Projection Evaluation

Application evidence combines the end-to-end scenario, SQL↔SPARQL parity, and competency-question regression.

For the eight predeclared SQL↔SPARQL tasks, six are equivalent for the tested task and two are equivalent after a declared normalization. The two normalization cases concern representation differences such as external actor identity and CM-PharmE target representation. After the R2 remediation, the assessment-evidence task also compares the qualified support role (`context`) explicitly in both RDF and PostgreSQL. These results remain task-bounded and do not establish lossless global ontology-to-database equivalence.

The CQ registry contains 40 original questions. CQ-039 is explicitly deferred, leaving 39 Paper-1-applicable CQs. Twenty-six are executable, seven partially executable, six conceptual-only, and one deferred; none is failed. These categories describe execution status, not a quality score.

### D. Negative Controls and Detector Sensitivity

The evaluation pipeline is tested not only on the candidate that is expected to pass but also on deliberately faulty fixtures. Negative controls cover malformed RDF, SHACL cardinality and trace failures, unsupported semantic equivalence, missing entailment, reasoner inconsistency, unresolved imports, stale ontology↔RDB mapping, altered expected CQ behavior, reassessment mutation, and workflow/risk-state conflation.

The declared fixtures are representative rather than exhaustive. No false positive or false negative has been observed in the governed fixture set, but this is not interpreted as an external defect-detection rate.

### E. E9–E11 Reproducibility, Comparison, and Transferability

E9 is currently supported in a bounded form. The semantic candidate, relational projection, data snapshot, scenario, parity harness, and regression tests rebuild in clean CI from exact repository-controlled artifacts and pinned tools. Public and synthetic evaluation artifacts are reproducible from governed paths. The private Jira source is represented by exact hashes and extracted schema evidence rather than redistributed bytes.

E10 is provisionally ready from the 12-comparator × 17-dimension evidence matrix, but final comparative wording awaits the remaining source/artifact tail and claim calibration. No overall ranking is produced.

E11 remains partial. Shared Core distinctions are exercised across an operational register schema and a Pharma case, but both are design-influencing evidence. The current evidence therefore supports bounded cross-context applicability, not independent transferability. DS-002 remains a protected candidate for later record-level holdout testing.

## VII. Discussion

The current evidence indicates that SemRisk can maintain several distinctions that are easily lost in operational implementations and can project those distinctions into an executable relational environment for selected tasks. The strongest current support concerns formal integrity, traceability, bounded application behavior, and preservation of specific semantic separations such as Risk versus Register Entry, Scenario versus Event versus Description, Assessment Activity versus Result, Risk State versus Workflow State, and responsibility-derived ownership.

The projection evaluation also shows why a binary “ontology equals database” claim would be inappropriate. Some task-level meanings are preserved exactly, while others require declared normalization or remain partial because one representation records information that the other fixture does not. These differences are scientifically useful because they identify where implementation convenience can obscure semantic commitments.

Several limitations directly constrain the claims. First, the operational Jira schema and DS-003 Pharma evidence materially influenced the design and therefore cannot be reused as independent validation of the same semantics. Second, DS-003 is a bounded qualitative source and does not support prevalence or general cross-domain claims. Third, some standards evidence remains access- or locator-bounded, so terminology/process alignment must not be described as complete standards conformance. Fourth, expert semantic validation is not yet executed. Fifth, independent E11 holdout transferability is not yet demonstrated. Sixth, the end-to-end execution contains synthetic artifacts that test application semantics rather than real-world treatment effectiveness or prediction.

These limitations do not invalidate the formal and application results already obtained; they determine the level at which those results may be described. Final claims are therefore deferred to the claim-calibration and assurance gates rather than inferred from the existence of an ontology, successful CI, or high mapping coverage alone.

## VIII. Conclusion — provisional

SemRisk provides an evidence-grounded, foundationally analyzed, formally implemented, and operationally executable semantic architecture for separating key operational risk concepts that are commonly conflated in registers and software systems. The current Paper-1 candidate passes its declared formal/structural checks, preserves all original competency questions, supports a bounded executable scenario, and demonstrates task-specific relational projection fidelity with explicit representation losses. The work also establishes controlled enterprise and pharmaceutical federation patterns while preserving external semantic ownership.

The present results should be interpreted within their evaluated scope. Expert semantic validation, final comparative and transferability evaluation, threats-to-validity synthesis, claim calibration, and publication-bound release are still required before final manuscript wording is frozen. Accordingly, this draft supports bounded formal and application claims and does not claim universal risk-domain validity, overall superiority, complete standards conformance, or general cross-domain transferability.

## References — governed placeholders

Final bibliography will be generated from the governed source registry. The following source families are required and must be resolved to exact references before submission:
- closest risk ontologies and conceptual models from #14/#22;
- ISO 31000 and ISO 31073;
- IEC 31010;
- NIST IR 8286 family;
- COSO ERM, OCEG GRC, and Risk IT as used;
- UFO/gUFO/OntoUML foundational sources;
- OWL, SHACL, PROV-O, and gUFO specifications/releases used in implementation;
- CM-PharmE v1.0.0;
- DS-003 exact DOI/version and linked study;
- selected closest Enterprise/Pharma comparators.

No unresolved or unverified citation may remain in the final candidate.
