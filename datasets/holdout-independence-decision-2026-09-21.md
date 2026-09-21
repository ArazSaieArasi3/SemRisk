# Paper 1 Holdout / Independence Decision — 2026-09-21

**Decision status:** FROZEN BASELINE pending exact dataset-version qualification.

## 1. Current conclusion

SemRisk currently has **no dataset that may honestly be described as independent validation evidence for semantic commitments already shaped by W1 sources**.

This is intentional evidence-governance, not a failure condition by itself. Independent claims must either use genuinely untouched evidence later or remain bounded.

## 2. Artifact decisions

| Artifact | Decision | Reason |
|---|---|---|
| SRC-OP-001 Jira spreadsheet | NOT independent | Complete operational schema has already shaped risk-register/workflow/assessment candidates. |
| DS-001 Ravela supplement | NOT eligible | Supplementary artifact not verified as complete primary dataset. |
| DS-003 PESTELI expert dataset | NOT independent | Already used for concept discovery and Pharma case semantics. |
| DS-004 cross-national shortage data | NOT independent for schema/Core semantics | Linked study has already shaped shortage/jurisdiction/recurrence/evidence-bias concepts; dataset identity/schema still unresolved. A future exact untouched record subset may test application robustness only, not schema-level semantic independence. |
| DS-002 FAERS/Harvard Dataverse | **PROTECTED CONDITIONAL HOLDOUT CANDIDATE** | It has not been used to shape Core/Profile semantics in the governed extraction baseline. Preserve it untouched if E11 independent transferability is retained. |
| Future expert review | Potential independent validation | Only after reviewer eligibility/independence and the instrument are frozen before responses are interpreted. |
| Synthetic fixtures | NEVER independent real-world validation | Regression/executability only. |

## 3. DS-002 protection rule

Until an explicit change decision:
1. do not mine DS-002 schema/records into canonical Core/Profile design;
2. metadata-level qualification for identity/license/access is allowed;
3. freeze exact Dataverse version/files/checksums before evaluation;
4. predeclare the transferability CQs/tasks and expected semantic outcomes before inspecting record-level results;
5. if DS-002 is later used for design, immediately revoke holdout/independence eligibility and preserve this original decision historically.

## 4. DS-004 partition rule

If DS-004 becomes the primary executable Pharma dataset, its schema and mappings may be used for design/application/regression. A record-level holdout can only test bounded application robustness when:
- the exact dataset version is frozen;
- partition rule is declared before record/result inspection;
- held-out records do not influence mappings/rules;
- the manuscript explicitly states that schema-level independence does not exist.

## 5. Claim consequence

Until independent evidence exists, SemRisk may report:
- operational mapping utility;
- case/application adequacy;
- regression behavior;
- standards/comparator alignment;
- bounded transferability only where untouched evidence actually supports it.

It must not report a general 'independent dataset validation' result from Jira, DS-003 or DS-004.

## 6. Change control

Any role change requires a dated decision record. The original role is never overwritten silently.
---

## 7. Controlled amendment — DS-002 schema-exposure regression — 2026-09-21

During holdout-safe metadata qualification, the public Zitnik Lab/project documentation surfaced processed-dataset structural details. No Dataverse records were downloaded or inspected, but the original **schema-blind** assumption is no longer true.

### Revised DS-002 role
Previous: `PROTECTED CONDITIONAL HOLDOUT CANDIDATE`.

Current: `RECORD_LEVEL_TRANSFERABILITY_HOLDOUT_CANDIDATE / SCHEMA-LEVEL INDEPENDENCE REVOKED`.

### Consequences
1. DS-002 cannot independently validate SemRisk Core/Profile schema semantics.
2. Publicly exposed DS-002 structural details must not be used to add/justify SemRisk canonical concepts before G1/G2.
3. Record-level transferability remains potentially independent because actual Harvard Dataverse records/files have not been opened in this execution.
4. Before any record access, freeze exact Dataverse version/files/checksums, E11 tasks/CQs, expected outcomes and pass/fail interpretation.
5. If record-level observations are used to revise mappings/rules before evaluation is completed, independent/holdout eligibility is revoked entirely.

This amendment preserves the original decision historically rather than silently rewriting it.