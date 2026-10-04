# SemRisk Paper 1 scientific contract — revision 2026-10-04

Owner: P02 / #53. Decision: **PASS_CONTRACT_ONLY**. This is a decision about scope, wording and evidence obligations; it does not approve the ontology, dataset or manuscript. Baseline: `f37cf41f6987d9887d9b96e913174a718f41439d`.

## Position and intended outcome

Working title: **SemRisk: An Extensible Core Ontology for Enterprise Risk Knowledge**.
The paper develops a reusable core for representing enterprise risk knowledge, with bounded pharmaceutical application and operational projection. Enterprise risk is the intended scope; complete coverage of strategic, financial, operational, compliance and all other risk categories is not claimed. Each evaluated scenario establishes only its stated coverage.

Risk knowledge denotes the connected representation of risk-relevant phenomena and scenarios, objectives and affected entities, documented risk records, assessment activities and time-qualified results, evidence and provenance, responsibility, and treatment. The ontology is distinguished from a particular populated knowledge graph, register, relational database or future intelligence platform.

The candidate differentiator is the **traceable integration** of semantic distinctions, time/context-qualified assessment, responsibility, provenance, a bounded CM-PharmE bridge and executable relational tasks. This remains a hypothesis until P03 comparison and P11 controlled tasks support it. OntoUML/UFO grounding, pharmaceutical risk ontologies and EA risk modeling already have prior art; none is claimed as a first.

## Questions, proposed contributions and acceptance evidence

Main question: How can a bounded, extensible enterprise-risk ontology preserve key semantic distinctions and support traceable assessment and use across conceptual, formal and relational representations?

| Stable ID | Question / contribution | Required evidence | Bound |
|---|---|---|---|
| SR-RQ1 / SR-C1 | Which core distinctions and commitments prevent conflating risk, record, assessment/result and workflow? Deliver a formalized core pattern. | P06 identity/state decisions; P08 OntoUML; P07 axioms; P11 entailment, non-entailment and pattern/anti-pattern results | Selected core, not a universal theory of risk |
| SR-RQ2 / SR-C2 | How can enterprise risk knowledge be operationalized without losing the semantics required by selected tasks? Deliver documented formal-to-relational mapping and executable tasks. | P10 typed/time-aware SQL/SPARQL tests, expected outputs, projection limitations; P11 feature-effect scenario | Task-specific fidelity, not lossless OWL conversion or performance superiority |
| SR-RQ3 / SR-C3 | How does the core organize a bounded literature-derived pharmaceutical case while preserving source provenance and extension boundaries? Deliver the CM-PharmE ver.1-linked case and curated dataset if release rights permit. | P09 source/locator/role lineage; P06 extension regression; P11 applicability results; P12 actual expert findings | Applicability unless genuinely independent evidence supports stronger transferability |

These IDs preserve the existing register identity. P15 must revise old operational-risk-only phrasing rather than creating competing claim IDs. Final wording may narrow as results require.

## Claim ledger and present permission

| Existing claim | Current permission | Evidence needed for strengthened wording |
|---|---|---|
| SR-CL01 semantic distinctions | Candidate core exists; distinctions require rechecking after revision | P06-P08 and targeted positive/negative tests |
| SR-CL02 operational mapping | Existing selected application evidence may be cited only at its tested ref | P10 updated mapping and load checks |
| SR-CL03 enterprise semantics | Intended ERM/EA use with bounded implemented links | Exact implemented objective/capability/responsibility mappings and scenarios |
| SR-CL04 relational projection | Existing eight-task parity is bounded to its comparator semantics | Typed literals, null/time/order/set/bag contract and new tasks |
| SR-CL05 federation | Bounded CM-PharmE v1.0.0 reference/bridge | Exact source ownership and category-preserving extension evidence |
| SR-CL06 transferability | Independent-transfer claim not permitted at this checkpoint | Preassigned unused source/record evidence and declared test protocol |
| SR-CL07 differentiation | Proposed integrated contribution, not proven superiority | Primary-source comparison plus fair controlled task/ablation |
| SR-CL08 formal correctness | Report only the actual tests at their exact candidate ref | Fresh formal checks on the revised candidate; no inference of domain truth |
| SR-CL09 reproducibility | Existing runners/artifacts exist; final package not yet released | Clean rebuild, pinned inputs/toolchain and publication manifest |

Real expert validation is **pending**, with zero responses at the reviewed baseline. Existing E1-E4 PASS records and green workflows are formal/engineering evidence, not substitutes for domain validation. The forty CQs retain their full denominator and status breakdown.

## Evidence-grounded and minimum viable ontology

Remove *evidence-grounded* from the working title. In methods, use the narrower **source-traceable design** description where a source-to-requirement-to-concept-to-constraint-to-test chain is demonstrated. Dataset inspection can ground a design decision; a case can test applicability. Neither automatically proves independent validation. Public corroboration must not rewrite the actual derivation history. See the [Persian rationale](evidence-grounded-fa.md).

Do not use *minimum viable ontology* as a certified maturity label. P06 decides whether the core supports a defined organization-use scenario, reasoning tasks and a nonbreaking domain extension. If those gates pass, the paper may describe a usable, extensible core and explicitly name its limits. Size alone is not viability.

## Standards and future boundaries

Distinguish source-informed design, explicit alignment, coverage and demonstrated conformance. Versioned clause-level mapping supports alignment; it does not certify compliance. P04 checks the intended standards/framework names instead of perpetuating speech-transcription errors.

Governance, Risk, Audit and Compliance (GRAC) describe a future integration direction. Current responsibility, provenance and governance references may support integration, but implemented compliance/audit ontologies, complete governance federation and demonstrated organizational resilience are not current results. Future reference-ontology breadth, broad Health profiles, Newsium/Commentium runtime integration, forecasting and intelligence services remain roadmap items. Full OQF adoption and CM-PharmE v2 are not prerequisites for this paper; P13 uses only explicitly selected reproducible metrics.

## Interaction and change control

Proceed autonomously with justified reversible decisions and verification. Present one consolidated author-review candidate. Ask only when a fundamental unresolved interpretation changes the contribution, actual expert participation is needed, or permanent publication/license/submission approval is missing. All source and semantic changes trigger an impact check against downstream requirements. Final evidence may narrow a claim; strengthening one requires a recorded test and assessment.

P02 is complete as a scope contract. Its linked scientific capabilities remain unverified until their implementation/evaluation packages close. The requirement register intentionally does not mark those capabilities complete here.
