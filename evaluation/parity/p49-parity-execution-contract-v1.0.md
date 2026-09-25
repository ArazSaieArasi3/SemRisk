# SQL↔SPARQL Parity Execution Contract v1.0

Issue: #49

The eight paired tasks in `p49-paired-query-registry-v1.0.csv` are frozen before paired execution.

Rules:
- Compare stable semantic IRIs/IDs whenever both projections retain them.
- Normalize only where the registry declares a representation difference before execution.
- SQL closed-world/NULL behavior is never interpreted as OWL entailment.
- A relational FK/CHECK PASS is not OWL proof.
- RDF graph absence is not universal negation.
- Any mismatch remains a finding and is classified as `partial`, `projection_loss`, `implementation_bug`, `ontology_gap` or `data_gap`; expected output must not be rewritten merely to obtain parity.
- Snapshot: P1-DATA-0.1.0-rc.2 + E2E scenario v1.1 (same frozen eight-task denominator; R7 domain-boundary correction only).
- Ontology candidate: P1-R2 / 0.1.0-rc.1.
- DB projection: 0.1.0-rc.1 plus additive V005/V006 hardening; data snapshot rc.2.


## R7 note
The R7 Pharma correction does not alter the frozen P49 task set. It removes an overtyped DS-003 transparency response from the constructed-case treatment strategy projection and preserves the E2E scenario on pooled procurement. P49 therefore remains an eight-task application-parity evaluation, not a Pharma-validity metric.
