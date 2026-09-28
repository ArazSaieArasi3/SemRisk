# SemRisk: An Evidence-Grounded and Well-Founded Semantic Architecture for Operational Risk Knowledge

**Working manuscript draft v0.3 — 2026-09-25**  
**Target:** ICAE 2026, Track 2 / Cluster B — Informatics & AI.  
**Status:** AUTHOR-REVIEW DRAFT v0.3 — VVEAA/formal-documentation checkpoint; final citations, figures, claim assurance and release binding pending. The present results support bounded formal and application claims. Human semantic validation (#51/#30), an independent shortage-domain E11 test (#31), final comparator/standards locators (#14/#13), claim calibration (#53), assurance (#54), release binding (#55) and the submission audit (#35) remain pending.

## Abstract — provisional

Operational risk-management artifacts commonly mix several semantically different things: the underlying risk being managed, possible scenarios, realized events, narrative descriptions, register records, assessment activities and results, workflow states, evidence, responsibilities, treatments, and controls. Such conflation complicates interoperability, reasoning, traceability, and faithful implementation across semantic and relational representations. This paper presents SemRisk, an evidence-grounded and well-founded semantic architecture for operational risk knowledge. SemRisk was developed through governed evidence synthesis and semantic reconciliation, explicit reuse and external-ownership decisions, UFO/gUFO-informed foundational analysis, modular OWL/SHACL formalization, and bounded enterprise and pharmaceutical applications. The current Paper-1 candidate is implemented as a modular ontology with a PostgreSQL projection and a bounded end-to-end pharmaceutical scenario. Formal and structural evaluation reports successful parsing, OWL 2 DL profile validation, HermiT consistency and named-class satisfiability, release-critical traceability, negative-control sensitivity, and governed constraint checks. In application evaluation, all 40 original competency questions are retained; 26 are executable, seven partially executable, six conceptual-only, and one explicitly deferred. Eight predeclared SQL↔SPARQL tasks show direct equivalence for the specified tasks in all eight pairs, covering 17 directly represented competency questions; this does not establish global ontology–database equivalence. These results support bounded formal and executable claims. Independent human semantic validation, an independent shortage-domain transfer test, and final claim/release assurance remain pending. SemRisk therefore provides a controlled basis for separating risk phenomena from operational artifacts and for evaluating how those semantics survive enterprise, database, and domain-specific projections without claiming universal risk-domain validity.

**Keywords:** risk ontology; ontology engineering; enterprise risk management; semantic interoperability; knowledge representation; OntoUML; OWL; risk register

## I. Introduction

Risk management is routinely implemented through registers, spreadsheets, workflow systems, reports, dashboards, and assessment methods. These artifacts are operationally useful, but they often encourage a schema-centered view in which columns such as “risk”, “scenario”, “event”, “owner”, “status”, “likelihood”, “impact”, “residual risk”, and “treatment” are treated as if they belonged to one semantic layer. This creates a recurring modeling problem: a real-world risk phenomenon can become conflated with the record used to document it; a possible scenario with a realized event; an assessment activity with the assessment result it produces; a workflow status with the modeled state of the risk; or a responsible actor with the role or responsibility assignment through which accountability is established.

For semantic interoperability, these distinctions matter. A register entry can be opened or closed without logically creating or eliminating the underlying risk. A scenario description is an information artifact, not the scenario or event itself. Inherent and residual risk are often better interpreted as contextual assessment results about the same underlying risk rather than as timeless subclasses of Risk. Likewise, a treatment strategy, a plan, an executed activity, and a persistent control mechanism may be operationally related but should not be collapsed into a single concept when their identities and lifecycles differ.

SemRisk addresses this problem through a bounded ontology-engineering study. The work does not attempt to define a universal ontology for every risk domain. Instead, it investigates whether an evidence-grounded, well-founded, formally implemented semantic pattern can preserve claim-critical distinctions while remaining operationally usable in an enterprise risk-register context and in one bounded pharmaceutical federation case.

The study is organized around three research questions. **SR-RQ1** asks how a SemRisk Core can preserve the distinctions among risk phenomenon, event, scenario, scenario description, register record, assessment activity/result, risk state, workflow state, evidence, treatment/control, and responsibility. **SR-RQ2** asks to what extent those semantics can be operationalized for enterprise risk management and a real Jira-style register schema without treating the database or spreadsheet schema as ontology truth. **SR-RQ3** asks to what extent the same Core pattern can be federated with CM-PharmE for a bounded pharmaceutical case while preserving external semantic ownership and making context-dependent or unmapped semantics visible.

The corresponding contributions are: **SR-C1**, a well-founded operational risk semantic pattern; **SR-C2**, an enterprise operationalization with an executable relational projection; and **SR-C3**, a bounded pharmaceutical federation case. The database projection, negative-control pipeline, and evaluation framework are supporting credibility mechanisms rather than separate novelty claims.

## II. Related Work and Semantic Gap

SemRisk is positioned relative to existing risk ontologies, conceptual models, standards, enterprise-risk frameworks, and operational risk-register representations. The historical #22 comparison snapshot has 12 rows—11 external works or lineages plus SemRisk—across 17 dimensions, producing 204 evidence cells. That snapshot predates the implemented P1-R2 candidate. MedSupplyKG is a subsequent targeted Pharma prior-art check outside that fixed denominator; final E10 requires release-bound source-locator review. The purpose of this comparison is not to produce a league table or an overall winner, but to determine which semantic capabilities are already established, where SemRisk reuses or aligns with prior work, and which integrated distinctions require explicit treatment in the present architecture.

Existing work contributes important pieces of the problem. Foundational risk ontologies such as COVER and related security/risk models provide semantics for risk-related entities and relations. Risk-register and GRC-oriented approaches contribute operational structures, register concepts, governance context, or relational implementations. Standards and frameworks including the ISO 31000 family, NIST IR 8286, COSO ERM, OCEG, Risk IT, IEC 31010, and ICH Q9 provide authoritative terminology, processes, roles, and method contexts. Domain ontologies such as CM-PharmE provide externally owned semantics for pharmaceutical entities that should not be silently duplicated by a risk ontology.

Two enterprise-facing sources further constrain the comparison. The PA-009 ontological analysis and redesign of risk modeling in ArchiMate examines risk, assessment, vulnerability and enterprise links (SRC-PA-009, §3, Figs. 5–6; §4, Table 2; §5, Figs. 7–10 and Table 3). PA-006's risk-propagation model explicitly includes a business-process/model object, intended goal, capability, assessor and control context (SRC-PA-006, §3, Fig. 2, PDF pp. 3–4), and reports ProbLog rules and example queries (§§4–5.1, PDF pp. 7–10). These are prior art for selected enterprise/goal/process links and risk reasoning. The historical CELL-059 `not_in_scope` classification for PA-006 D08 was incorrect. Neither publication, by itself, establishes an exact mapping to the selected SemRisk external-owner path or a comparable SQL↔SPARQL task result; those comparisons remain to be evaluated in E10.

RiskHub (SRC-PA-017, 2026) is a direct operational register comparator. Its published To-Be model connects risk scenarios to business functions, risk owners and mitigation (§5.1, Figs. 7–9), maps the model to 12 relational tables and MySQL (§§5.2–5.3, Figs. 10–11), and reports dashboard queries (§7.1) and exploratory feedback from 12 academic respondents (§6.1). Thus, ontology-informed register redesign, a relational database and human model feedback are established prior art. The inspected publisher supplement is a diagram, and the cited earlier thesis repository is not the 2026 executable release; exact code/data and a shared SQL↔SPARQL parity benchmark remain unbound. SemRisk's tested projection concerns its eight predeclared task pairs, not a claim of general superiority over RiskHub.

RISKMAN (SRC-ON-004, 2025) is medical-device risk-documentation prior art. Its model distinguishes analyzed and controlled risk with initial and residual risk levels and links safe-design arguments to implementation evidence (Table 1 and Fig. 1); its versioned OWL EL ontology and SHACL shapes constrain risk reports (§4.4, Fig. 4). The paper explicitly limits these checks to documented structure rather than the adequacy of mitigation. Those results preclude novelty claims for risk OWL+SHACL or evidence-linked medical-device assurance alone. RISKMAN's device-safety context is separate from the bounded antibiotic-shortage federation evaluated here.

MedSupplyKG, a pharmaceutical supply-chain knowledge graph by Eberhardt et al. (2025), is direct prior art for integrating drug-shortage reports, product and ingredient information and graph analysis. Its published schema explicitly distinguishes a `Report` notification node from a `Shortage` node (SRC-PH-003, Table 2, Table 3 and Fig. 4; DOI 10.1080/00207543.2025.2496671). The `Report` is a shortage notification and is not thereby identical to a SemRisk Risk Register Entry; the paper's `Shortage` label alone does not establish exact event or situation identity in SemRisk. This source rules out claiming that report-versus-shortage separation, a pharmaceutical risk knowledge graph or graph-based shortage prioritization is first introduced here. An exact released ontology, code snapshot, graph dump and independent rerun have not been established from the publication; their absence from the inspected source is not evidence that the capabilities do not exist.

The bounded gap addressed by SemRisk is therefore not “the absence of a risk ontology”. Rather, it is the need for an explicitly governed semantic architecture that integrates several distinctions simultaneously: risk phenomenon versus information artifact; scenario versus realized event versus scenario description; assessment activity versus result; risk state versus workflow state; contextual inherent/residual assessment results; responsibility-derived ownership; treatment strategy versus plan/activity/control; evidence/provenance; external semantic ownership; and executable projection into operational data structures.

This gap statement remains deliberately descriptive. Current evidence supports bounded differentiation hypotheses, but final comparative wording is reserved for E10 and claim calibration because missing documentation in a comparator cannot be treated as evidence of absence.

## III. Research and Ontology-Engineering Method

### A. Study Design and Evidence Roles

Paper 1 is an ontology-engineering design research study with evidence-synthesis, bounded case/application, executable projection, and claim-dependent evaluation components. Evidence is governed by explicit roles: discovery, design, reconciliation, illustrative, regression, independent validation, holdout, comparative, and future-only. A central control rule is that an artifact that materially shaped a semantic commitment cannot later be described as independent validation of that same commitment unless an untouched partition or genuinely independent source exists.

This rule is important for the operational Jira schema and the pharmaceutical evidence. The Jira artifact shaped design and reconciliation and is therefore valid for operational mapping and regression, but not for independent semantic validation. DS-003, the bounded pharmaceutical source used for the case, likewise contributed to case semantics and is treated as design/reconciliation/illustrative evidence. Synthetic data are regression and application fixtures only. DS-002 remains protected and unopened; because its FAERS content concerns a different pharmaceutical safety context, it is a prospective cross-domain stress candidate for selected generic Core distinctions, not an independent antibiotic-shortage holdout.

### B. Evidence Acquisition and Semantic Reconciliation

Source mining and reconciliation were executed before formalization. The process produced a governed raw-to-canonical semantic pipeline rather than promoting each observed field or label directly into an ontology class. Cross-source reconciliation classified 274 raw rows and retained 191 canonical or unique concept candidates plus 175 relation/event/state/activity candidates, while preserving bounded-pending sources rather than forcing premature closure.

A ubiquitous-language stage then stabilized 43 preferred terms, recorded 20 terminology conflicts or false friends, 22 anti-concepts, 29 mappings, and 15 rename/migration lineage decisions. These controls are important because common risk labels can hide different ontological categories. For example, “owner” may refer to an actor, a role, or a responsibility assignment; “residual risk” may refer to a contextual result rather than a second Risk entity; and “status” may refer to workflow rather than risk state.

The requirements stage froze 20 semantic requirements and 40 competency questions. The original questions were retained through later execution rather than rewritten after implementation to improve apparent coverage.

### C. Reuse, Architecture, and External Ownership

SemRisk uses an explicit reuse/reference policy. COVER and ROSE are referenced and aligned by default; import or equivalence requires stronger evidence and additional gates. No `owl:equivalentClass` or `owl:equivalentProperty` relationship is inferred from lexical similarity. CM-PharmE entities remain externally owned in the pharmaceutical bridge. Generic Objective, Capability, and Business Process families are likewise not redefined as local SemRisk classes: Paper 1 treats TOGAF 10 and ArchiMate 3.2 as reference/alignment sources while leaving the generic canonical semantic owner unbound. The Core is kept independent of profiles and application projections, while Enterprise, Method, Governance, and Pharma modules depend on or specialize the Core.

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

SemRisk is modularized into Core, Enterprise, Method, Governance, and Pharma concerns. External enterprise or domain semantics are referenced rather than absorbed into the Core when their identity belongs elsewhere. Architecture-facing `affects` assertions are interpreted as bounded links whose target family, effect mode and provenance may be qualified in the Enterprise/DataProjection layer; a bare link does not imply objective failure, capability degradation, process disruption or causal propagation. In the Pharma case, CM-PharmE v1.0.0 remains the semantic owner of pharmaceutical entities. SemRisk contributes risk-specific participation or contextual relations around those external entities.

### C. Temporal Assessment and Responsibility

Reassessment is modeled as a new assessment activity linked to a prior assessment, producing a new result that may supersede an earlier result while preserving the identity of the underlying Risk. This supports historical inherent/residual or pre/post-treatment interpretations without minting a second Risk by default.

Responsibility is modeled through an actor–responsibility–risk pattern. The owner view is derived from the responsibility structure, providing an explicit semantic truthmaker and avoiding schema-driven primitive ownership.

## V. Operationalization and Bounded Pharmaceutical Case

### A. Operational Risk-Register Mapping

The operational source is a Jira-style risk-register schema with 27 governed attributes. All 27 fields have semantic dispositions in the master mapping rather than a class-per-column transformation. The denominator is precisely the selected SRC-OP-001 schema, not all risk-register products or enterprise risk management. A field may map to a concept, relation, result, workflow value, profile term, metadata artifact, or an explicitly partial/deferred status.

This mapping provides evidence that the Core can be operationalized without making the spreadsheet schema the canonical semantic model. Because the complete schema influenced conceptualization, its 27/27 coverage is an operational mapping result, not an independent correctness percentage and not evidence of complete enterprise-risk-management or generic risk-register functionality. Common capabilities such as delegation/RACI, control assurance/effectiveness, due-date/escalation governance, portfolio aggregation and emerging/systemic-risk management remain outside the demonstrated Paper-1 operational scope.

### B. Relational Projection

A PostgreSQL relational twin implements the Paper-1 projection. The projection preserves stable semantic identities for the eight evaluated task families, separates Core, assessment, treatment, enterprise, provenance, reference, Pharma, and governance structures, and exposes selected derived views such as risk ownership. The governed data snapshot P1-DATA-0.1.0-rc.2 includes a source-grounded constructed DS-003 case and separately identified synthetic execution fixtures; it does not include DS-002 or file-level DS-004 rows.

Relational constraints are interpreted as application-level closed-world controls, not as OWL entailments. Conversely, absence of an RDF triple is not interpreted as universal negation. This open-world/closed-world distinction is made explicit in the parity evaluation.

### C. Bounded Pharma Federation

The bounded Pharma case uses DS-003 as a qualified qualitative source and CM-PharmE v1.0.0 as an external semantic owner. ICH Q9(R1) provides bounded pharmaceutical quality-risk context, including assessment, treatment/review and product-availability concerns; however, its Hazard/Harm semantics are not claimed as Paper-1 Core coverage because those SemRisk profile concepts remain deferred. DS-003 contributes source-supported conditions, actor/context evidence, and pooled procurement as a proposed treatment strategy. Supply-chain transparency is retained more conservatively as a Pharma response candidate requiring contextual typing because the source frames it as a management need rather than unambiguously as a strategy, activity, control, policy, requirement, or capability. The purposive expert source does not support prevalence, treatment-effectiveness, or universal causal generalization.

The mapping package contains 18 governed DS-003 elements: seven direct/context mappings, ten partial mappings, and one unobserved item. These are disposition counts, not a Pharma-validity score. DS-004 remains blocked for file-level evaluated mapping and structured-shortage robustness until exact files, version, license, checksums, columns, quality metrics, transformation lineage, and predeclared evaluation tasks are frozen. DS-002 remains unopened at record level, but R7 classifies its FAERS content as a protected cross-domain Pharma stress candidate for selected generic Core semantics rather than as direct validation of shortage semantics.

### D. Executable End-to-End Scenario

A predeclared end-to-end scenario connects the source-grounded Pharma semantics to explicitly synthetic execution artifacts. The scenario contains DS-003-supported predisposing conditions and a proposed treatment strategy, then adds synthetic trigger, realized event, consequence, register entry, owner responsibility, plan, treatment activity, control, pre-treatment assessment, post-treatment reassessment, risk-state history, and workflow-state history.

Ten expected-answer families were frozen before execution. The PostgreSQL run returns one realized synthetic event, two temporal assessment results, and one derived owner. The RDF graph contains the corresponding semantic path. The synthetic extension exists only to exercise the model and is not evidence of an observed DS-003 shortage event, real treatment effectiveness, causal strength, prevalence, or prediction. Trigger, realized Event, synthetic Consequence, plan, activity, control, reassessment, and operational state transitions therefore remain application/regression fixtures rather than domain evidence.

## VI. Evaluation

### A. E1–E4 Formal, Logical, Structural, and Foundational Evaluation

The E1–E4 package contains 21 declared evaluation records, all of which pass for their bounded criteria. Fourteen governed Turtle inputs parse successfully. The candidate passes OWL 2 DL profile validation under the declared toolchain. HermiT classification reports consistency for the governed closure, expected entailments are present, and an explicit post-reasoning satisfiability check finds no named SemRisk class classified as `owl:Nothing`.

Structural checks report 71/71 release-critical semantic IDs present, unique canonical IDs and IRIs, zero unapproved OWL equivalence mappings, and controlled dependency/test isolation. The positive SHACL fixture conforms, while five of five known-negative SHACL fixtures fail as expected. The owner-derivation rule constructs the expected `hasRiskOwner` triple.

E4 reuses the frozen foundational review: 33/33 release-critical concepts and 38/38 release-critical relations have foundational dispositions or rationales, and all seven high-risk foundational conditions identified at G2 were resolved for the Paper-1 subset.

These results establish formal, structural, and foundational verification evidence only. They do not establish domain correctness or universal ontology quality.

### B. E5–E6 Semantic, Expert, Standards, Operational, and Dataset Validation

E6 has been assembled as a bounded evidence-validation package. The standards/framework crosswalk contains 11 governed rows with version/status and mapping-strength controls. ISO 31000:2018 remains the current published edition while its Edition-3 committee draft is tracked separately; draft and published editions are not mixed. The strongest operational standards evidence concerns the current NIST IR 8286 family, but NIST register fields are treated as operational/profile evidence rather than ontology identities. ISO 31000/31073, IEC 31010, COSO ERM 2017, OCEG GRC Capability Model 3.5, Risk IT 2nd Edition and ICH Q9(R1) are used only for bounded RELATED, PROFILE_SUPPORT, OPERATIONALIZES or COVERAGE_BENCHMARK mappings as applicable, not as conformance certifications.

Operational mapping reports 27/27 Jira fields dispositioned. DS-003 reports 18/18 governed elements dispositioned. These denominators describe mapping governance, not semantic correctness percentages.

E5 human semantic validation remains pending. The expert-review protocol, reviewer eligibility matrix, 20-item review instrument, response template, and adjudication rules are frozen before any reviewer response. The protocol preserves `NOT_ASSESSED`, reviewer disagreement, independence information, and Critical/High findings rather than averaging them away. No expert response is fabricated in the present draft.

### C. E8 Application, Query, and Projection Evaluation

Application evidence combines the end-to-end scenario, SQL↔SPARQL parity, and competency-question regression.

For the eight predeclared SQL↔SPARQL tasks, all eight are directly equivalent for the declared task under the frozen comparison rules. R6 removed the two former identity normalizations by preserving the synthetic actor IRI explicitly in the relational projection and comparing the exact CM-PharmE external target IRI through the versioned external-entity reference. The assessment-evidence task also compares the qualified support role (`context`) explicitly in both RDF and PostgreSQL. The denominator remains the eight frozen tasks, which directly cover 17 of the 40 competency questions; these results are task-bounded and do not establish lossless global ontology-to-database equivalence.

The CQ registry contains 40 original questions. CQ-039 is explicitly deferred, leaving 39 Paper-1-applicable CQs. Twenty-six are executable, seven partially executable, six conceptual-only, and one deferred; none is failed. These categories describe execution status, not a quality score.

### D. Negative Controls and Detector Sensitivity

The evaluation pipeline is tested not only on the candidate that is expected to pass but also on deliberately faulty fixtures. Negative controls cover malformed RDF, SHACL cardinality and trace failures, unsupported semantic equivalence, missing entailment, reasoner inconsistency, unresolved imports, stale ontology↔RDB mapping, altered expected CQ behavior, reassessment mutation, and workflow/risk-state conflation.

The declared fixtures are representative rather than exhaustive. The selected mutations were detected by the declared guards, but those selected mutation families do not support a general detector-sensitivity or defect-detection-rate estimate.

### E. E9–E11 Reproducibility, Comparison, and Transferability

E9 is currently supported in a bounded form. The semantic candidate, relational projection, data snapshot, scenario, parity harness, and regression tests rebuild in clean CI from exact repository-controlled artifacts and pinned tools. Public and synthetic evaluation artifacts are reproducible from governed paths. The private Jira source is represented by governed provenance and extracted schema evidence rather than redistributed bytes. Exact publication-bound release identity and a final availability statement remain work for #55/#56.

E10 has a historical 12-row × 17-dimension snapshot (11 external rows plus SemRisk) and a targeted MedSupplyKG source comparison, but final comparative wording awaits current per-cell locators, remaining source/artifact work and claim calibration. No overall ranking is produced.

E11 remains partial. Shared Core distinctions are exercised across an operational register schema and a Pharma case, but both are design-influencing evidence. The current evidence therefore supports bounded cross-context applicability, not independent transferability. DS-002 remains protected for possible later **cross-domain** record-level stress testing of generic Core semantics in a pharmacovigilance context; it is not a shortage-domain holdout. DS-004 is more shortage-aligned but remains file-level blocked. Consequently, no clean independent shortage-domain holdout has yet been executed.

### F. Claim-Dependent VVEAA Synthesis

The evaluation is organized as a case-specific Verification, Validation, Evaluation, Assessment, and Assurance (VVEAA) profile over the predeclared E1–E11 methods. Verification examines syntactic, logical and structural obligations; validation examines whether the bounded meanings and source mappings are appropriate; evaluation examines declared query/application, comparative, reproducibility and robustness tasks; assessment judges each claim against favorable and adverse evidence; assurance asks whether the resulting argument supports a release decision. This profile is documented in `evaluation/vveaa/paper1-vveaa-execution-profile-v0.1.md`; it is not described as an adopted or completed Ontology Quality Framework release.

| Function | Current Paper-1 evidence | Decision boundary |
| --- | --- | --- |
| Verification | E1–E4: 21/21 bounded records report PASS; 71/71 release-critical semantic IDs present; five negative SHACL fixtures detected. | Formal/foundational checks do not establish domain truth. |
| Validation | E6: 27/27 selected operational fields and 18/18 DS-003 elements dispositioned; E5 review instrument frozen. | Mappings are non-independent where they shaped the design; real expert judgments remain absent. |
| Evaluation | 40 CQs retained (26 executable, seven partial, six conceptual-only, one deferred); 8/8 frozen SQL↔SPARQL tasks directly equivalent; E9 bounded reconstruction. | E10 remains provisional and no clean independent E11 shortage holdout has been executed. |
| Assessment | Nine headline claims crosswalked to methods, denominators, supporting and challenging evidence. | Independent transferability is unsupported; final #53 judgment is pending. |
| Assurance | #54 release-bound argument, assumptions, blockers and decision are specified as the next gate. | Integrated assurance has not been assessed; no global quality score or certification is reported. |

The table's full evidence and caveats are maintained in `publications/2026-icae/paper1-vveaa-results-table-v0.1.md` and `evaluation/vveaa/paper1-vveaa-claim-method-evidence-v0.1.csv`. The corresponding formal description `docs/ontology/formal-ontology-description-p1-r2-v0.2.md` separates the six source modules, OWL axioms, five SHACL shapes, one implemented rule, and SQL/application constraints. Its source-derived 35 class, 37 object-property and four SKOS-marker declarations are a different counting unit from the 71 release-critical conceptual IDs. The exact publication release and complete FD-A–FD-J documentation audit remain pending.

## VII. Discussion

The current evidence indicates that SemRisk can maintain several distinctions that are easily lost in operational implementations and can project those distinctions into an executable relational environment for selected tasks. The strongest current support concerns formal integrity, traceability, bounded application behavior, and preservation of specific semantic separations such as Risk versus Register Entry, Scenario versus Event versus Description, Assessment Activity versus Result, Risk State versus Workflow State, and responsibility-derived ownership.

The projection evaluation also shows why a binary “ontology equals database” claim would be inappropriate. After the R6 identity remediation, all eight frozen paired tasks preserve their declared comparison identities directly, but those eight tasks cover only a bounded, predeclared subset of the competency-question space. Semantic-loss findings such as open-world/closed-world asymmetry, foundational role projection, bounded provenance and external-taxonomy non-reconstruction therefore remain relevant even when the selected queries are task-equivalent.

Several limitations directly constrain the claims. First, the operational Jira schema and DS-003 Pharma evidence materially influenced the design and therefore cannot be reused as independent validation of the same semantics. Second, DS-003 is a bounded qualitative source and does not support prevalence, treatment-effectiveness, or general cross-domain claims. The current Pharma case also does not exercise explicit Risk Source, Vulnerability, Exposure, a populated Assessment Method, Indicator/Threshold semantics, or control-effectiveness/assurance semantics. MedSupplyKG already separates shortage notifications and shortages and performs graph-based Pharma analysis; the distinctiveness of SemRisk's broader integrated chain remains a provisional E10 comparison question, not a claim that this separation or application domain is new. Third, some standards evidence remains access- or locator-bounded, so terminology/process alignment must not be described as complete standards conformance. Fourth, expert semantic validation is not yet executed. Fifth, independent E11 holdout transferability is not yet demonstrated. Sixth, the end-to-end execution contains synthetic artifacts that test application semantics rather than real-world treatment effectiveness or prediction.

These limitations do not invalidate the formal and application results already obtained; they determine the level at which those results may be described. Final claims are therefore deferred to the claim-calibration and assurance gates rather than inferred from the existence of an ontology, successful CI, or high mapping coverage alone.

## VIII. Conclusion — provisional

SemRisk provides an evidence-grounded, foundationally analyzed, formally implemented, and operationally executable semantic architecture for separating key operational risk concepts that are commonly conflated in registers and software systems. The current Paper-1 candidate passes its declared formal/structural checks, preserves all original competency questions, supports a bounded executable scenario, and demonstrates task-specific relational projection fidelity with explicit representation losses. The work also establishes controlled, bounded enterprise and pharmaceutical federation patterns while preserving external source identity and versioning. It does not claim complete enterprise-architecture risk integration, architecture dependency propagation, objective-performance causality, capability degradation reasoning, or TOGAF/ArchiMate conformance.

The present results should be interpreted within their evaluated scope. Expert semantic validation, final comparative and transferability evaluation, threats-to-validity synthesis, claim calibration, and publication-bound release are still required before final manuscript wording is frozen. Accordingly, this draft supports bounded formal and application claims and does not claim universal risk-domain validity, overall superiority, complete standards conformance, or general cross-domain transferability.

## References and source verification — review-stage register

This author-review version intentionally carries a source-verification checklist rather than invented bibliographic entries. Before submission, material in-text claims must receive numbered, verified references from the governed source register. Required families:
- closest risk ontologies and conceptual models from #14/#22;
- ISO 31000 and ISO 31073;
- IEC 31010;
- NIST IR 8286 family;
- COSO ERM, OCEG GRC, and Risk IT as used;
- UFO/gUFO/OntoUML foundational sources;
- OWL, SHACL, PROV-O, and gUFO specifications/releases used in implementation;
- CM-PharmE v1.0.0;
- DS-003 exact DOI/version and linked study;
- selected closest Enterprise/Pharma comparators, including Eberhardt et al. (2025), MedSupplyKG, DOI 10.1080/00207543.2025.2496671 (SRC-PH-003, Tables 2–3 and Fig. 4; formal artifact/reproduction status unresolved).

A publishable manuscript still requires verified in-text citations, bibliography, exact figure/table binding, IEEE typesetting, human review and final assurance. The present version is intended for scientific and editorial review of the argument and its bounded results.


## Author review notes for the next revision

1. **Validate the narrative:** assess the descriptive difference against COVER, ROSE, risk-register, GRC and MedSupplyKG comparators; record missing or conflicting sources under #14/#13, not as absent competitor capabilities.
2. **Review semantic commitments:** focus on Risk identity, scenario/event separation, responsibility and state semantics. The R1–R8 simulated critiques are engineering aids and do not replace independent #51 judgments.
3. **Inspect claim ceilings:** 27/27 applies only to the selected Jira schema; 8/8 applies only to eight frozen paired tasks; constructed Pharma context and synthetic scenario are not observed treatment effects; DS-002/DS-004 have not furnished an independent shortage holdout.
4. **Next production pass:** insert verified numbered citations, one compact source-derived core figure and one bounded E1–E11 table, then typeset to the venue contract. Record the manuscript commit and any semantic/data change impact before #54/#55.
