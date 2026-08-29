# Source Analysis — Jira Risk Attributes

**Source ID:** `SRC-OP-001`  
**File:** `jira risk attributes.xlsx`  
**Source locus:** direct user-supplied ChatGPT attachment  
**SHA-256:** `6f40bb5dd670e884df205093b8048d62807f5371e502997279f03073b09e5c8f`  
**Scope:** `Sheet1!A1:C28`  
**Access date:** 2026-08-29  
**Evidence tier:** A — direct operational evidence

## Extraction summary

- Operational attributes: **27**
- Raw extraction records including controlled vocabulary values: **121**
- Attribute rows covered: **27/27**
- Core-only candidate records: **12**
- Core/Enterprise candidate records: **21**
- Enterprise-specific records: **88**

Disposition counts:

| Disposition | Count |
|---|---:|
| Candidate ontology constructs | 20 |
| Profile / mapping vocabulary | 70 |
| Assessment-method profile values | 17 |
| Data / product constructs | 9 |
| Data-only metadata | 5 |

## High-value semantic findings

### 1. The spreadsheet does not represent a single ontological layer

The schema mixes at least five different semantic layers:

1. **risk-domain semantics** — consequence, treatment, owner, assessment;
2. **assessment-method semantics** — ordinal impact/likelihood scales and score formulas;
3. **risk-record semantics** — title, description, labels, created/updated time;
4. **workflow/product semantics** — analyzed state, assignee, status;
5. **source-specific taxonomies** — strategic, financial, operational and detailed risk categories.

These layers must not be projected directly into one OWL class hierarchy.

### 2. Risk, Risk Record and Risk Assessment must be separated

`Inherent risk` and `Residual risk` are represented as derived values from impact × likelihood. This source therefore provides direct operational evidence that:

- the **risk phenomenon/scenario** is distinct from
- the **assessment activity/context**, which is distinct from
- the **assessment result/score**, which is distinct from
- the **Risk Register record** carrying those results.

The formula itself is a method/business rule and should not be asserted as a universal OWL truth.

### 3. Record workflow state is not Risk state

`Open → Analyzed → Treated → Closed` and `Completed/Reviewed/Ready` are management-process or record states. Closing a record does not entail that the underlying risk no longer exists.

### 4. Ownership requires role/relator semantics

`واحد مالک` and `Assignee` are semantically different:

- the owner field points toward a **Risk Owner role / accountability assignment**;
- the assignee field is a **workflow responsibility** and may be temporary or task-specific.

### 5. Identification provenance is heterogeneous

`کانال ورودی ریسک` contains actors, committees, activities, training, complaints, audits and compliance processes. It should therefore not become a single flat enumeration in the canonical ontology. It is evidence for a more general **Risk Identification Provenance** pattern whose sources can be agents, organizational bodies, activities, records or processes.

### 6. Threat and opportunity are modeled together

The source explicitly distinguishes `تهدید` and `فرصت` and mixes response strategies for both:

- threat-oriented: Accept, Avoid, Mitigate, Transfer;
- opportunity-oriented: Exploit, Enhance, Share.

This is a material design question for SemRisk and must be reconciled with ISO/COSO/COVER semantics before canonicalization.

### 7. The risk taxonomy is source-specific but valuable

The secondary taxonomy includes strategic-external, strategic-internal, financial and operational families with detailed concepts such as:

- sanctions risk;
- competition risk;
- commodity-pricing risk;
- environmental risk;
- technology-change risk;
- regulatory-change risk;
- supplier/value-chain risk;
- interest-rate risk;
- FX risk;
- liquidity/funding risk;
- credit risk;
- information-systems/technology risk;
- accounting-control risk;
- human-resource risk;
- legal risk;
- process-design risk;
- reputational risk;
- compliance risk;
- external-event risk including fraud and natural hazards.

These terms should be preserved in a **source taxonomy mapping package** and used in cross-source reconciliation. They should not automatically become SemRisk Core subclasses.

## Candidate anti-patterns detected

1. `table/field = ontology class`
2. `controlled vocabulary value = subclass` without ontological evidence
3. `workflow state = risk state`
4. `risk score = risk`
5. `record creation date = risk identification time`
6. `assignee = risk owner`
7. `text describing consequence = consequence event/state`
8. `risk response strategy = executed treatment activity`
9. `impact × likelihood = universal risk semantics`
10. `all identification channels = same ontological category`

## Immediate reconciliation questions

1. Should SemRisk represent an upper concept broader than downside risk so that opportunity is first-class?
2. How should inherent/residual assessment context align to COVER and ISO 31000?
3. Which risk-category terms belong to generic profiles versus sector-specific taxonomies?
4. Should identification provenance be represented using a generic Evidence/Provenance pattern?
5. Which accountability relation should connect organizational units to Risk Owner roles?
6. What is the formal relationship between Risk Consequence, Impact and Objective/Value change?
7. Which spreadsheet constraints belong in SHACL and which remain application/business rules?

## Output artifacts

- `jira-risk-attributes-concepts.csv` — raw source mining and semantic disposition
- `jira-risk-attributes-coverage.csv` — row-level coverage evidence
- source record in `source-register.csv`

## Status

This is **source mining v0.1**, not canonical SemRisk. All ontology candidates remain subject to cross-source reconciliation at Gate G1/G2.
