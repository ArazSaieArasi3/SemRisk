# OWL Profile and Serialization Policy v0.1

- **Target semantics:** OWL 2 DL.
- **Canonical source:** Turtle.
- **Generated distributions:** RDF/XML and JSON-LD may be generated deterministically.
- **No OWL Full:** metamodel use must remain within legal OWL 2 DL punning/annotation patterns.
- **No artificial EL/QL/RL promise:** #27 reports the actual used fragment after implementation.
- **Cardinality:** universal semantic cardinalities only when justified by #25; application completeness goes to SHACL.
- **Disjointness:** used only for foundationally incompatible categories where doing so does not conflict with external/profile semantics.
- **Property characteristics:** transitive/symmetric/functional/inverse-functional only with explicit rationale and tests.
- **External foundational terms:** gUFO exact dependency/version must be bound by #43 before any import/reference is release-bound.
- **Reasoning result:** consistency/entailment is verification evidence, never domain validation.