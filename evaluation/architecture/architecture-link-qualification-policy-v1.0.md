# Architecture Link Qualification Policy v1.0

**Owner:** Issue #92

SR-REL-010 `affects` remains a generic SemRisk Core relation connecting Risk/Event/Consequence to an external Risk Subject or enterprise/architecture context.

For Enterprise/Architecture projection, every governed architecture-facing assertion SHOULD carry:
- target family: `objective | capability | business_process | other_external`;
- effect mode: `anticipated | realized | contextual | unknown`;
- external owner namespace + semantic ID + version;
- evidence/provenance source when available;
- optional confidence/qualification note.

Rules:
1. a bare `affects` assertion does not entail objective failure, capability degradation or process disruption;
2. `anticipated` and `realized` are not interchangeable;
3. no global transitivity is asserted;
4. the relation is not declared equivalent to any ArchiMate relationship;
5. target identity remains owned by the external source;
6. qualification belongs to Enterprise/Mapping/DataProjection, not a new universal Core taxonomy.
