# SemRisk Paper 1 Dataset Shortlist and Disposition — 2026-09-21

**Governed by:** #16, #17, #41, #42
**Purpose:** separate dataset identity/fitness from narrative convenience and define what is actually on the P1-R0/P1-R3 path.

| Artifact | Paper-1 disposition | Current fitness | Independence | Immediate use | Deferred requirement |
|---|---|---|---|---|---|
| SRC-OP-001 Jira operational schema | REQUIRED operational evidence | approved_with_limits | not independent | register/workflow/assessment reconciliation; operational mapping/regression | no empirical generalization |
| DS-003 PESTELI v4 | REQUIRED bounded Pharma qualitative evidence | approved_with_limits | not independent | causes/actors/consequences/mitigations; case grounding | no prevalence/generalization; preserve quote context |
| DS-004 cross-national antibiotic-shortage primary data | PREFERRED structured Pharma case candidate | W1 design/reconciliation approved; file-level evaluation blocked | not independent for schema semantics | documented raw/master grains and analytical-variable semantics | exact dataset files/license/checksums/schema + quality metrics before evaluated mapping/W3A |
| DS-002 FAERS patient-safety | OPTIONAL E11 record-level transferability holdout | future_only | schema-level independence revoked; record-level potential remains | provenance only; no SemRisk design use | exact Dataverse release/license/files/checksums + frozen E11 protocol before record access |
| DS-001 Ravela supplement | SUPPLEMENTARY / FALLBACK CONTEXT ONLY | approved_with_limits as supplement | not independent | lineage/context/schema lead | cannot stand in for the complete 5,132-report corpus |
| SYNTH-P1-TBD | REQUIRED later executable regression fixture | planned | not real-world independent | none until generator freeze | deterministic seed/version/checksum and explicit synthetic labeling |

## Primary Paper-1 evidence composition

P1 does **not** require a single dataset to carry all evidentiary roles.

1. Operational semantic realism comes from `SRC-OP-001`.
2. Pharma causal/actor/mitigation grounding comes from `DS-003` plus Pharma literature/standards.
3. Structured cross-jurisdiction shortage mapping/application is expected to use `DS-004` if its exact share files can be frozen and qualified.
4. Independent transferability is not claimed from the above construction evidence.
5. `DS-002` may later support only record-level E11 transferability under a predeclared frozen protocol.
6. Synthetic data support executable regression/application completion but never external validity.

## G1 consequence

Dataset uncertainty no longer consists of an undefined universe. Every current candidate has an explicit disposition and claim boundary.

For G1:
- DS-003 is adequate bounded design/case evidence;
- DS-004 is adequate as a known/partially mined source with explicit file-level blocker; its exact file schema is not silently treated as complete;
- DS-002 is non-blocking for G1 because it is optional/future-only and its holdout role is explicitly deferred;
- DS-001 is non-blocking because it is explicitly supplementary rather than primary evidence.

Therefore the remaining data blocker for G1 is **not dataset discovery/role ambiguity**. It is completion of #17/#42 to the level required by the exact claims entering reconciliation, with DS-004 file-level evaluation debt carried forward explicitly if inaccessible.

## W3A consequence

DS-004 exact artifact acquisition/freeze becomes a hard prerequisite if #28/#47-#49 choose it for executable quantitative mapping. If that cannot be achieved, the case must use an explicitly governed alternative rather than inventing file-level metrics from the linked study.