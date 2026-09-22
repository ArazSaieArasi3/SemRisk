# Paper-1 CQ Scope and Freeze Decision — 2026-09-22

## Frozen conceptual set
- Total semantic requirements: **20**.
- Total conceptual CQs: **40**.
- Paper-1 required CQs: **34**.
- Conditional CQs tied to SR-CL06 bounded transfer: **2**.
- Optional CQs: **3**.
- Explicitly deferred/Post-Paper1 CQs: **1**.

## Classification
- Positive CQs: **15**.
- Negative CQs: **16**.
- Edge CQs: **9**.

## Contribution coverage
- SR-C1 appears in **28** CQ links.
- SR-C2 appears in **16** CQ links.
- SR-C3 appears in **8** CQ links.

## Freeze rule
These CQs are implementation-independent semantic commitments. Later OWL/SQL/SPARQL/SHACL design may satisfy, partially satisfy, fail or defer them, but may not silently rewrite or delete them to improve results.

## Required Paper-1 focus
Required CQs cover the claimed Core distinctions, Enterprise/Jira mapping, ownership/responsibility, treatment/control semantics, evidence/provenance, causal-strength control, Pharma federation, traceability and principal anti-concepts.

## Conditional/optional/deferred rule
- `REQUIRED_IF_SR-CL06_RETAINED`: evaluated only if bounded transferability claim SR-CL06 remains in #53.
- `OPTIONAL`: useful for robustness/profile depth but not required to sustain the minimum Paper-1 claim set.
- `DEFERRED`: explicitly outside Paper 1 and cannot block G2/G4.