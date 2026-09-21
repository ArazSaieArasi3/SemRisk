# SemRisk P1-R0 Blocker Dashboard — 2026-09-21

**Release:** P1-R0 — Evidence Baseline  
**Exit gate:** #18 G1  
**Current judgment:** IN PROGRESS / G1 NOT READY

| Blocker family | Earlier state | Current state | Consequence / next action |
|---|---|---|---|
| COVER exact identity/license | Critical unresolved | **RESOLVED** | Immutable commit/path/blob + Apache-2.0 pinned; formal source anomaly moves to #21/#29 |
| ROSE exact identity/license/erratum | High unresolved | **RESOLVED** | Corrected immutable repository commit + MIT + PURL pinned |
| IOF Biopharma exact release/module identity | High unresolved | **RESOLVED identity** | Suite 202603 + release commit + module versionIRI 202602 pinned; semantic reuse conditional because Provisional |
| CM-PharmE exact semantic owner/version | Critical unresolved | **RESOLVED semantic baseline** | Frozen v1.0.0 bound; license remains external governance gap for redistribution/import |
| PH-007 full-text access | Critical novelty blocker | **BOUNDED / medium** | Publisher evidence supports high-level prior-art/method claim; detailed structure forbidden; no longer blocks narrow SR-C3 |
| Pharma supply-risk ontology landscape | Unsaturated | **PARTIAL_NEAR_SATURATION** | Prior-art lineages established; final stopping refresh/artifact cleanup remains |
| Risk Register/GRC landscape | Unsaturated | **PARTIAL / material baseline established** | NIST + RisKG + RiskHub anchor set exists; final stopping/artifact checks remain |
| Propagation semantics | Partial | **NEAR-SATURATED foundational lineage** | PA-015→PA-010→PA-006 lineage governed; selected implementation refs remain |
| Search stopping evidence #40 | Incomplete | **OPEN / concentrated** | Complete final no-new-material-source refreshes and unresolved queue dispositions |
| Evidence-role leakage #41 | Open | **PASS / CLOSED** | 48-role baseline and holdout rules established; maintain on new sources |
| DS-002 holdout identity/version/license | Unresolved | **OPEN / protected** | Metadata-only qualification without design leakage; bind exact version/license/checksum |
| DS-004 dataset identity/schema/quality | Critical unresolved | **OPEN / Critical data blocker** | Resolve PID/version/license/files/schema and compute quality metrics |
| DS-003 qualitative file-level completeness | Partial | **OPEN / medium** | Complete released-file/sample/coding inspection if used in evaluated mapping |
| Standards clause/schema completeness | Partial | **OPEN** | Finish exact locator/schema mining, especially NIST/ISO/ICH claim-critical mappings |
| Comparator artifact/profile tail | Broad | **OPEN / smaller tail** | Open Risk members, PA-013, selected AIRO/RISKMAN/implementation refs |
| Cross-source semantic reconciliation | Not executed | **OPEN / final G1 blocker** | Build raw-item dispositions, conflicts, source deltas, Core/profile candidate classification and gate snapshot |

## Critical path from here

1. Finish #16/#17/#42 data qualification and fitness.
2. Finish #40 final stopping evidence and residual comparator/source dispositions.
3. Finish claim-critical #12/#13/#14/#15 locator/source-completeness debt.
4. Execute #18 cross-source reconciliation and issue PASS/CONDITIONAL_PASS/FAIL.

## What is no longer on the critical path

- generic Pharma ontology novelty discovery;
- COVER/ROSE artifact identity;
- IOF Biopharma artifact identity;
- CM-PharmE semantic baseline selection;
- evidence-role policy/holdout governance.

These items remain subject to downstream semantic/reuse decisions but no longer block P1-R0 because of unknown identity.