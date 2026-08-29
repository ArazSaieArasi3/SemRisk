# ICAEA Paper 1 — Pharmaceutical Dataset Selection Decision

**Status:** provisional selection baseline; final primary dataset is frozen only after file/schema inspection.  
**Date:** 2026-08-29

## Decision principle

Paper 1 should not force all empirical validation into one dataset if two independent evidence types test different claims more cleanly. The preferred design is therefore a **small evidence bundle** with explicit roles:

1. one source for **causes, actors, consequences and mitigations**;
2. one source for **structured shortage/availability records**;
3. one optional source for **cross-subdomain transferability**.

This produces stronger E6/E11 evidence than treating one convenient dataset as proof of all SemRisk capabilities.

## Candidate ranking

| Rank / role | Dataset | Strength | Main SemRisk test | Current blocker |
|---|---|---|---|---|
| **A1 — causal/domain evidence** | `DS-003` UCT PESTELI antibiotic-shortage dataset, DOI `10.25375/uct.29178665.v4` | public DOI; CC BY 4.0; expert data; explicit cause/consequence/response framing | Pharma concepts, actors, risk sources, consequences, mitigations, evidence provenance | file-level schema/transcript/table extraction |
| **A2 — structured shortage evidence** | `DS-004` Chirac et al. 2026 primary Figshare data | very recent peer-reviewed study; cross-national; public primary-data link | shortage event/record semantics, product/medicine context, jurisdictional variation, transferability | Figshare DOI/version/license unresolved; schema inspection pending |
| **B — transferability optional** | `DS-002` Harvard Dataverse patient-safety/FAERS dataset, DOI `10.7910/DVN/G9SHDA` | DOI-backed; linked peer-reviewed Nature Computational Science work; rich drug–adverse-event structure | test whether Core evidence/event/assessment patterns transfer from supply/availability to pharmacovigilance | exact Dataverse version/license and Paper-1 space/time budget |
| **C — supplementary only** | `DS-001` Ravela et al. Figshare supplementary file | DOI-backed supplement linked to strong public-register study | supplementary context / source-schema lead | not verified as primary 5,132-report dataset; linked article says analyzed datasets available on request |

## Recommended Paper-1 empirical design

### Primary package

Use **DS-003 + DS-004**, if DS-004 qualification succeeds.

```text
DS-003 qualitative expert evidence
  -> drivers / causes / actors / consequences / mitigations

DS-004 structured cross-national shortage evidence
  -> medicine / shortage record / jurisdiction / recurrence / structural factors

Both
  -> SemRisk Pharma mapping
  -> CM-PharmE bridge
  -> competency questions
  -> E6 coverage/conflict analysis
```

This gives the case both **semantic depth** and **structured empirical grounding**.

### Fallback package

If DS-004 cannot be DOI/license/schema-qualified in time:

1. keep DS-003 as the DOI-backed public dataset;
2. use official national shortage registers or Ravela's peer-reviewed study as independent external validation evidence where legal/access conditions allow;
3. do not misrepresent the Ravela Figshare supplementary artifact as the complete research dataset.

### Optional E11 package

Use DS-002 only if the Core is sufficiently stable and Paper-1 evaluation can demonstrate a genuinely distinct transferability result. Otherwise retain it for Paper 2 / Health-profile evaluation.

## Case refinement

The empirical evidence supports retaining the current case direction:

**upstream/supply/manufacturing/regulatory conditions → pharmaceutical shortage / medicine-availability disruption → healthcare delivery / patient consequence → mitigation / governance response**.

However, the case should not assert a specific causal edge unless supported by a selected source. Qualitative/expert statements, regulatory observations and structured shortage associations must remain distinguishable in provenance.

## Evaluation metrics to derive from datasets

For selected structured/qualitative sources:

- source fields/items mapped;
- fully mapped / partially mapped / unmapped / conflict counts;
- ontology category distribution;
- Core vs Pharma/Health/Enterprise profile distribution;
- relation/event/state coverage;
- ambiguity and mapping-confidence distribution;
- concepts unique to dataset versus literature/standard sources;
- negative cases that expose SemRisk limitations;
- query/CQ coverage;
- provenance completeness.

No single mapping percentage will be reported as ontology correctness.

## Final freeze criteria

A dataset enters the Paper-1 release only if all are true:

- exact PID/URL is stable;
- version is known or immutably identifiable;
- public-access and license/reuse status are documented;
- schema/data dictionary or file semantics can be inspected;
- transformation/mapping is reproducible;
- selected fields materially test a Paper-1 claim;
- privacy/sensitivity constraints are acceptable;
- manuscript can cite the linked scholarly source accurately.
