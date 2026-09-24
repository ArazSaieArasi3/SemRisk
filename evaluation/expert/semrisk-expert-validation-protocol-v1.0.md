# SemRisk Paper-1 Expert Semantic Validation Protocol v1.0

Issue: #51  
Status: PROTOCOL_FROZEN_BEFORE_RESPONSES  
Candidate under review: P1-R2 / ontology 0.1.0-rc.1  
Executable companion: PostgreSQL projection 0.1.0-rc.1 + P1-DATA-0.1.0-rc.1

## Purpose
Obtain bounded human semantic-validation evidence for the Paper-1 subset. Expert review addresses whether the intended distinctions, definitions and relation patterns are understandable and defensible for the reviewed scope. It is not a vote on universal ontology truth and does not replace formal verification.

## Reviewer eligibility
The panel is selected to cover the following expertise dimensions collectively:
1. ontology/conceptual modeling or semantic-web engineering;
2. enterprise risk management / GRC / risk-register practice;
3. enterprise/software/data architecture;
4. pharmaceutical/health risk or pharmaceutical ecosystem knowledge for Pharma-specific items.

A reviewer must have demonstrable relevant professional or research experience in at least one dimension. Pharma-only items may be marked NOT_ASSESSED by reviewers lacking relevant domain expertise.

### Target and minimum interpretation rules
- Target completed panel: 5–8 reviewers if feasible.
- If fewer than 4 eligible completed reviewers are obtained, results are reported as qualitative expert feedback only; no aggregate agreement statistic is presented as stable evidence.
- Coverage of expertise dimensions matters more than raw count.
- Author/project contributors may participate only if their prior involvement is explicitly recorded; their responses are not described as independent validation.
- At least two completed reviewers should be independent of SemRisk design for any wording using “independent expert review”. Otherwise that wording is prohibited.

These thresholds are study-reporting rules, not claims of statistical representativeness.

## Review package
Each reviewer receives the same version-bound package:
- short scope/nonclaim sheet;
- glossary and selected definitions;
- relevant conceptual/OntoUML figure(s);
- item-specific classes/relations with stable semantic IDs;
- selected source/alignment rationale where needed;
- bounded Pharma scenario and CM-PharmE bridge excerpt for domain items;
- review instrument v1.0.

Reviewers must assess the semantic content, not merely labels or visual appearance.

## Response scale
Primary ordinal judgment:
- A — Accept as semantically adequate for reviewed scope
- B — Accept with minor clarification/revision
- C — Major semantic revision required
- D — Reject / semantically incorrect for reviewed scope
- NA — Not assessed / insufficient expertise or evidence

No arithmetic mean of A–D is a canonical result.

Each non-A response should include rationale. C/D responses require exact target identification if possible and are treated as findings rather than averaged away.

## Additional dimensions
For each item the reviewer may separately mark:
- clarity: clear / needs clarification / unclear / NA
- scope placement: Core correct / Profile correct / should move / NA
- relation direction/cardinality: appropriate / questionable / incorrect / NA, when applicable
- evidence sufficiency: sufficient for review / insufficient / NA

## Independence and provenance
For each reviewer record:
- pseudonymous reviewer ID;
- expertise dimensions;
- experience bracket;
- academic/practitioner context;
- prior SemRisk/CM-PharmE involvement;
- independence classification;
- conflict-of-interest note if any;
- review date and exact candidate/package version.

Names/contact information are not required in the public repository.

## Analysis
Report:
- item-level counts A/B/C/D/NA;
- proportion of assessed responses by category, with denominator;
- reviewer coverage by expertise dimension;
- disagreement distribution before adjudication;
- qualitative rationale themes;
- critical findings and remediation status;
- re-review status after material changes.

If at least four eligible reviewers complete the same ordinal items, an ordinal agreement statistic may be reported only if methodologically appropriate; raw item-level distributions remain primary.

## Finding severity
- Critical: category/identity/relation error that invalidates a central Paper-1 distinction or claim.
- High: material semantic error requiring ontology or major claim change.
- Medium: localized ambiguity/definition/profile-placement issue.
- Low: terminology/documentation clarification.

Any Critical/High finding remains open until remediated and re-reviewed by at least one suitable reviewer; an aggregate favorable majority cannot erase it.

## Adjudication
1. Preserve raw individual judgments.
2. Register disagreement.
3. Authors propose disposition with rationale.
4. Material semantic change triggers formal regression (#44/#29/#50/#52 as applicable).
5. Changed reviewed item is re-reviewed where Critical/High or claim-relevant.
6. Original and revised evidence remain linked.

## Claim rules
Expert evidence supports only:
- reviewed items;
- reviewed candidate version;
- represented expertise domains;
- explicitly assessed case/profile scope.

It cannot establish universal risk-domain validity, standards certification, universal Pharma transferability, predictive capability, or formal correctness.

## Ethics/data handling
Only reviewer-role metadata necessary for methodological reporting is retained. Public results should be pseudonymized. Any consent/privacy constraints on raw comments are recorded and respected.
