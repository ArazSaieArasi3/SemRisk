# ADR: Ontology requirements engineering policy — 2026-10-08

- Decision ID: SEMRISK-ADR-20261008-ORE
- Status: ACCEPTED_BY_AUTHOR
- Authority: explicit author approval in the Risk Ontology conversation on 2026-10-08 (Asia/Tehran).
- Effective date: 2026-10-08, for prospective requirements-engineering work.
- Scope: SemRisk Paper 1 and subsequent ontology requirements revisions; local application projections remain separately governed.

## Approved directive

Adopt SABiO (Falbo, 2014) as the primary ontology-engineering method for continuing work. Use an Ontology Requirements Specification Document (ORSD), drawing on NeOn's requirements guidelines, to organize the requirements. Record each content requirement with a semantic statement, competency question(s), provenance and acceptance/rejection criteria. Analyze and formalize domain constraints using UFO-grounded OntoUML and an appropriate formal notation. Use EARS only as an optional writing aid. Establish bidirectional traceability from requirements to the model and tests, then evaluate relational mappings as application-specific implementations of their declared coverage.

This is a project-specific composition of existing methods and not a newly established, independently validated methodology.

## Relation to the existing method contract

The historical process described in `paper1-engineering-method-v1.1.md` was organized through OGCM-RF and mapped to SABiO. This decision changes the prospective method-selection policy. It does not rewrite the history as if SABiO had been adopted at project inception, establish completed execution of SABiO activities, or reopen/close scientific gates by itself.

OGCM-RF continues to govern source completeness, evidence, traceability, configuration and release gates. VVEAA continues to organize evaluation evidence and its interpretation. UFO provides foundational commitments; OntoUML provides the conceptual modeling notation. None of these roles is interchangeable.

## Requirements record

For every requirement, maintain:
1. Stable ID, type, version and status.
2. Exact source and locator; source role and evidence strength.
3. Semantic statement and rationale.
4. Scope: reusable Core, contextual profile, or application-specific policy.
5. Linked motivating scenario / stakeholder objective where available.
6. Relevant CQ IDs and expected answer type or representational capability.
7. Required concepts, relations, cardinalities and formal constraints.
8. Acceptance criteria and negative acceptance criteria.
9. Model/axiom links and test links with predeclared expected outcomes.
10. Operational encoding and relational mapping links when applicable.
11. Review decision, author/expert role and unresolved assumptions.

Not every non-functional requirement must become a CQ; use an appropriate quality/process check. A content requirement may require multiple CQs, and a CQ may cover multiple requirements. Additional fields are a SemRisk policy, not a claim that every field is mandated by SABiO or NeOn.

## Mandatory separation

Keep distinct, cross-linked registries or types for:
- Product/stakeholder goals.
- Ontology content and ontology quality requirements.
- Domain constraints / conceptual commitments.
- Software behavioral requirements.
- Data/schema and mapping requirements.

A software action is not an ontology axiom. A database field is design evidence, not automatic proof of a universal domain concept. A relational foreign key, OWL axiom and SHACL shape have different semantics.

## EARS policy

EARS is optional for controlled textual statements, especially software responses, and may aid ontology content requirements in a ubiquitous-statement form. Do not force all domain facts into event-response wording. EARS does not determine UFO categories, identity, dependence, modality or cardinality and does not replace CQs or formalization. If EARS wording is used, link it to the same stable requirement; do not count it as a duplicate requirement.

## Formalization and testing

Separate:
- Representational adequacy and foundational analysis.
- Formal consistency and permitted/prohibited model instances.
- Query answerability given a stated ontology version, dataset and reasoning regime.
- Local data completeness and validation.
- Relational projection conformance and round-trip preservation within declared coverage.

Declare open-world vs closed-world assumptions. A missing explicitly asserted OWL value is not automatically an existential-constraint violation. Use SHACL or SQL/application checks when explicit data completeness is required. Record expected answers, forbidden inferences and relevant counterexamples. Bounded formal checking is not proof of complete domain validity.

## Existing assets and migration boundary

Preserve the original requirement/CQ IDs and historical execution classes:
- `conceptualization/requirements/semantic-requirements-registry.csv`
- `conceptualization/requirements/conceptual-cq-registry.csv`
- `method/sabio-executed-process-crosswalk-v1.1.csv`

This decision does not migrate, refreeze or mark these registries accepted/tested. Extend them through a versioned crosswalk or controlled revision, retaining all historical IDs. Application-derived and explainably inferred requirements must retain their individual provenance and review status; their counts must not silently be merged with the frozen conceptual baseline.

## Next implementation sequence

1. Audit existing requirements and CQs against this policy without changing semantic IDs.
2. Produce a versioned ORSD and explicit requirements-type separation.
3. Link semantic requirements to grouped CQs, informal constraints and formal commitments.
4. Complete bidirectional model/test traceability and identify uncovered or unsupported links.
5. Run bounded positive/negative checks and report coverage separately from validity.
6. Evaluate the relational projection's declared mapping and round-trip behavior.
7. Update manuscript methods to distinguish historical execution from this dated adaptation.

For requirements claiming complete scoped coverage, require every approved in-scope content requirement to have a justified model link and an appropriate assessed check, or an explicit unresolved disposition. Do not infer academic readiness from assignment coverage or issue closure.

## Acceptance of this recording task

- The approved decision is saved in the repository with an effective date.
- Its relation to the earlier method contract is explicit.
- SABiO, ORSD, CQs, optional EARS, UFO/OntoUML and mapping roles are all stated.
- Historical evidence, counts, artifacts and scientific gate status are preserved.
- Recording this decision is not reported as completion of the migration or ontology acceptance.

Rejection conditions: retroactive history rewriting; renumbering baseline requirements/CQs; marking unexecuted checks passed; claiming global methodological superiority or full ontology/database equivalence; disclosure of raw restricted organizational records.

## Primary references

1. R. de Almeida Falbo. SABiO: Systematic Approach for Building Ontologies. ONTO.COM/ODISE, CEUR-WS 1301, 2014. https://ceur-ws.org/Vol-1301/ontocomodise2014_2.pdf
2. M. C. Suárez-Figueroa, A. Gómez-Pérez, B. Villazón-Terrazas. How to Write and Use the Ontology Requirements Specification Document. OTM/ODBASE 2009. https://oa.upm.es/5474/1/INVE_MEM_2009_64393.pdf
3. P. C. B. Fernandes, R. S. S. Guizzardi, G. Guizzardi. Using Goal Modeling to Capture Competency Questions in Ontology-based Systems. JIDM 2(3), 2011. https://periodicos.ufmg.br/index.php/jidm/article/view/124
4. A. Mavin, P. Wilkinson, A. Harwood, M. Novak. Easy Approach to Requirements Syntax (EARS). IEEE RE 2009, pp. 317–322. https://doi.org/10.1109/RE.2009.9
5. W3C. OWL 2 Web Ontology Language Primer (Second Edition). https://www.w3.org/TR/owl2-primer/
6. W3C. Shapes Constraint Language (SHACL). https://www.w3.org/TR/shacl/
