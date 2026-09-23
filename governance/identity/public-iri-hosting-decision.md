# SemRisk Public IRI Hosting Decision

**Decision:** no public HTTPS namespace is claimed at #43.

SemRisk requires durable identifiers before #27, but a persistent resolver/redirect is not yet configured and tested. Therefore Paper-1 implementation uses repository-independent `urn:semrisk:*` IRIs.

A future HTTPS namespace may use a persistence service such as w3id or another institutionally controlled resolver only after:
1. ownership/control of redirect configuration is confirmed;
2. ontology and documentation targets exist;
3. content negotiation/resolution is tested;
4. repository relocation behavior is documented;
5. old URN→HTTPS lineage/alias policy is published;
6. #43 change-control tests are rerun.

Until those conditions pass, no `https://...semrisk...` string is described as the canonical/public ontology IRI.