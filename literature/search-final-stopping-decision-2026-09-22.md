# SemRisk Search Execution — Final Stopping Decision for P1-R0

**Date:** 2026-09-22
**Owner:** Issue #40
**Release:** P1-R0 — Evidence Baseline
**Decision:** `PASS_FOR_SEARCH_EXECUTION / STOP_BROAD_DISCOVERY / ROUTE_RESIDUAL_DEBT`

## Decision rule

#40 closes when each claim-critical family has one of three governed outcomes:
1. `SATURATED_FOR_PAPER1_BOUNDED_SCOPE` — stopping test met;
2. `BOUNDED_FOR_G1` — residual inaccessible/artifact detail cannot change the bounded claim unless scope expands, and consequence is explicit;
3. `DEFERRED_OUTSIDE_PAPER1_CORE_SCOPE` — relevant to future/profile work but not a P1 Core novelty blocker.

Residual locator, implementation-artifact, reuse-license, clause-level, or file-schema work may remain in #12–#17/#4/#21/#23 without keeping broad discovery open.

## Final per-family disposition

| Family | Final #40 disposition | Why broad search stops now | Residual owner |
|---|---|---|---|
| Foundational / well-founded risk | SATURATED_FOR_PAPER1_BOUNDED_SCOPE | COVER/ROSE, closest UFO programme, EA comparator and propagation lineage cover the claim-critical semantic space; final refresh found no Core-changing comparator | #14/#21/#23 for artifact/reuse details |
| Generic risk-management ontology | BOUNDED_FOR_G1 | Historical generic ontologies are less claim-proximate than COVER/ROSE + active UFO programme; remaining artifact detail cannot support a broader 'first ontology' claim because that claim is already prohibited | #14 |
| Risk Register / GRC semantics | BOUNDED_FOR_G1 | NIST 8286 current schemas + RisKG + RiskHub + operational Jira establish authoritative/register→KG/register→RDB prior art; remaining OCEG/COSO/detail work affects crosswalk depth, not discovery of the central novelty threat | #13/#14/#22 |
| Enterprise / Architecture risk | SATURATED_FOR_PAPER1_BOUNDED_SCOPE | ArchiMate UFO redesign + current refresh + RiskHub/operational sources bound SR-C2; no newer claim-changing comparator found | #14 locator cleanup |
| Dynamic risk / propagation | BOUNDED_FOR_G1 | PA-015→PA-010→PA-006 plus WATCHDOG/PA-013 establishes semantic and executable/formal prior art; unresolved code refs are reproducibility debt, not discovery debt | #14/#23 |
| Health / medical-device risk | DEFERRED_OUTSIDE_PAPER1_CORE_SCOPE | RISKMAN v1.0.0 + ISO 14971 establishes mandatory Health comparator; broader Health profile boundary is explicitly owned by #4 and is not required to freeze P1 Core novelty | #4/#14 |
| Pharma QRM | SATURATED_FOR_PAPER1_BOUNDED_SCOPE_WITH_GAPS | PH-007 bounded + ICH Q9 + IOF exact module + current refresh establish prior art; detailed inaccessible PH-007 features are prohibited from claims | #15/#14 |
| Pharma supply-chain risk | BOUNDED_FOR_G1 | Multiple independent lineages (Morocco 2017+, ontology+FQFD 2020, literature/data cases) establish that generic Pharma supply-risk ontology is prior art; remaining seeded-paper/artifact details affect comparison depth only | #15/#14 |
| Pharmacovigilance signal | DEFERRED_PROFILE/FUTURE | OpenPVSignal + ADR/PV-SDO lineages establish signal/report/provenance prior art; not a Paper-1 Core novelty axis and DS-002 records remain protected | #15/#36 |
| Ontology engineering/evaluation method | BOUNDED_FOR_G1 | OGCM-RF + RISKMAN + WATCHDOG + PA-013 + RiskHub provide materially distinct method alternatives sufficient for #23 selection after G1 | #23/#14 |
| Formal artifact/repository landscape | BOUNDED_FOR_G1 | Main mandatory artifacts are exact-bound; remaining implementation repos/licenses are routed artifact debt and cannot hide a new closest ontology identity | #14/#21/#23 |
| Paper-1 dataset universe | GOVERNED_COMPLETE_FOR_W1 | Every current dataset has identity/role/fitness/disposition or explicit blocked state | #17/#28/#47-#49 for file-level execution |

## Search execution evidence

- Exact search log maintained through SRCH-20260921-037.
- Screening/dedup registry preserves publication/preprint/repository lineages.
- Source register contains 50 governed sources.
- Saturation/stopping registry records per-family stop logic.
- Unresolved-source queue preserves inaccessible/unfinished evidence and routes consequences.
- Formal-artifact search was performed separately from publication discovery.
- Current-work refresh covered 2025–2026 claim-critical domains.
- Backward/forward lineage work was performed for the closest risk-ontology, propagation and Pharma programmes.

## Explicit nonclaims that make bounded stopping defensible

Paper 1 does not claim:
- first risk ontology;
- first well-founded risk ontology;
- first dynamic/propagation ontology;
- first risk-register KG/RDB;
- first EA-risk integration;
- first Pharma/QRM ontology;
- first ontology+formal-verification architecture;
- universal Health/domain completeness.

Because those broad claims are prohibited, residual historical/profile sources cannot silently expand the novelty boundary.

## Reopen triggers

#40 broad search reopens only if:
- Paper-1 claim scope expands;
- #18 finds a contradiction requiring new evidence;
- a newly discovered source is materially closer than the governed comparator set;
- reviewers/venue require a new comparison family;
- a currently deferred Health/PV/future-Risk-Intelligence claim is moved into Paper 1.

## Final judgment

`PASS_FOR_SEARCH_EXECUTION`.

#40 may close. This does **not** mean #12–#17/#4 are complete; it means broad discovery/search execution is sufficient to enter #18 Source Completeness reconciliation with residual evidence debt explicitly routed.