# SemRisk Risk Identity and Continuity Contract v0.1

**Owner:** Issue #69  
**Scope:** Paper-1 governed Risk identity  
**Status:** FROZEN_POLICY

## Purpose
SemRisk treats `Risk` as a governed domain pattern without forcing it into one UFO/gUFO primitive. This contract defines how a governed Risk instance retains or changes identity in the Paper-1 implementation.

## Identity principle
A Risk instance is identified by its **governed semantic identity** (stable semantic-instance identifier/IRI plus explicit provenance and lifecycle decisions), not by any mutable record field, score, state, owner, treatment, label or description.

The stable identifier is an identity-management mechanism, not a claim that identifier equality by itself proves metaphysical identity. Identity continuity remains an explicit governed semantic decision.

## Changes that do NOT automatically create a new Risk
The following changes preserve the existing Risk identity by default unless an explicit split/new-identity decision is made:
- Risk Register Entry creation, revision, migration or replacement;
- title, narrative or Scenario Description changes;
- Workflow State changes;
- new or superseding Assessment Results, including inherent/residual contexts;
- Risk State history changes;
- ownership/responsibility reassignment;
- treatment strategy, plan, activity or control changes;
- evidence/provenance additions or corrections;
- creation of additional scenarios/events/consequences concerning the same governed Risk context.

None of these mutable artifacts is an identity key for Risk.

## When a new Risk identity is required
A new Risk semantic identity is created only through an explicit governed identity decision, including:
1. deliberate split of one governed Risk into two or more independently managed risk identities;
2. deliberate creation of a new risk phenomenon/context judged not to preserve the prior identity;
3. source-governance decision that two previously conflated risks must be separated;
4. migration where semantic identity cannot be preserved and lineage must record replacement.

A material change in subject/scenario/context may **trigger review**, but SemRisk does not infer new identity automatically from content differences.

## Merge and split
- **Split:** allocate new stable IDs; retain lineage to the predecessor; never reuse the predecessor ID for both successors.
- **Merge:** allocate or select one governed surviving identity only through explicit governance; preserve predecessor lineage.
- Do not use `owl:sameAs` automatically to implement merge.
- Do not infer sameness from labels, titles or database keys imported from source systems.

## Counterexamples
### Same Risk
A register entry moves from `open` to `treated`, receives a residual assessment, changes owner, and gains a new treatment plan. The underlying governed Risk identity remains unchanged.

### Same Risk with changed scenario description
A causal narrative is revised after better evidence. The Scenario Description changes; the governed Risk is not automatically replaced.

### New Risk
A review determines that one record actually conflates two independently managed risk phenomena with different governed identity anchors. The record is split and two new Risk identities are created with lineage.

## Projection rule
A relational `risk_id` is a projection of the governed semantic identity. It must not be regenerated from mutable field values and must not be used as evidence that a database row defines the ontology identity.

## Formalization nonclaims
- No single gUFO stereotype is imposed on Risk by this policy.
- No global `owl:hasKey` is asserted for Risk.
- No `owl:sameAs` is inferred from shared fields, records or labels.
- The policy is a governed identity/continuity contract for Paper 1, not a universal metaphysical theory of risk identity.

## Regression consequence
The E2E pre/post assessment path MUST continue to use one stable Risk identity while assessment results, workflow and state histories change.
