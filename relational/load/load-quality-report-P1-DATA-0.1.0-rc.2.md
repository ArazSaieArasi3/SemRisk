# SemRisk Governed Data Load — R7 Quality Amendment

**Snapshot:** `P1-DATA-0.1.0-rc.2`  
**Purpose:** preserve the prior rc.1 evidence while correcting the R7 Pharma-domain interpretation of response typing and DS-002 role.

## Changes from rc.1
- the prior evaluated rc.1 snapshot is not overwritten;
- pooled procurement remains a source-grounded **proposed Risk Treatment Strategy**;
- PCI-005 supply-chain transparency is no longer materialized in `treatment.strategy`;
- PCI-005 is retained as `PROFILE-PHARMA-RESPONSE-CANDIDATE` with `partial` disposition because contextual typing is unresolved;
- DS-004 remains file-level blocked;
- DS-002 remains record-level protected and is described as a future **cross-domain Pharma stress candidate**, not a shortage-validation holdout;
- no DS-002 record is loaded or inspected.

## Case composition
The constructed DS-003 package continues to provide:
- one bounded Risk context;
- two source-grounded Predisposing Conditions;
- one constructed possible Risk Scenario;
- one source-grounded proposed treatment strategy (pooled procurement);
- one context-sensitive response candidate (supply-chain transparency);
- evidence/assessment/state support artifacts;
- exact CM-PharmE v1.0.0 external references.

The E2E extension remains separately synthetic and does not provide empirical evidence for shortage occurrence, treatment effectiveness, causal magnitude or prediction.

## Claim boundary
This snapshot is suitable for deterministic application/regression evaluation. It does not establish Pharma-wide validity, structured-shortage robustness, independent transferability, prevalence, or treatment effectiveness.
