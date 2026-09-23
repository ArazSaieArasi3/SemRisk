# #27 → #44 Deterministic Build Handoff

**Candidate:** P1-R2 `0.1.0-rc.1` implementation  
**State:** `IMPLEMENTED_NOT_BUILD_VALIDATED`

## Canonical inputs
- Core: `ontology/core/semrisk-core-v0.1.0-rc.1.ttl`
- Enterprise: `ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl`
- Method: `ontology/method/semrisk-method-v0.1.0-rc.1.ttl`
- Governance: `ontology/governance/semrisk-governance-v0.1.0-rc.1.ttl`
- Pharma: `ontology/pharma/semrisk-pharma-v0.1.0-rc.1.ttl`
- Mappings: `ontology/mappings/semrisk-mappings-v0.1.0-rc.1.ttl`
- SHACL: `shapes/semrisk-paper1-shapes-v0.1.0-rc.1.ttl`
- Rule: `rules/enterprise/derive-has-risk-owner-v0.1.0-rc.1.rq`
- Synthetic positive fixture: `testdata/p1-r2-positive-smoke-v0.1.ttl`
- Candidate manifest: `ontology/p1-r2-candidate-manifest.yaml`

## Required #44 first-pass checks
1. Parse every canonical Turtle file separately and as resolved import closure.
2. Validate OWL 2 DL profile and record unsupported constructs separately.
3. Resolve gUFO v1.0.0 through an exact pinned catalog/cache, never mutable master.
4. Confirm PROV-O references and mapping IRIs without replacing exact #43 bindings.
5. Verify 71/71 release-critical IDs against `formal-entity-inventory-v0.1.csv`.
6. Run expected entailment and non-entailment requirements from #26.
7. Run SHACL on positive fixture and create known-negative fixtures for every release-critical shape family.
8. Run SR-RULE-001 and assert exactly the expected derived owner triple.
9. Fail on any unregistered `owl:equivalentClass/property`, mutable dependency ref or `urn:semrisk:test:` occurrence inside ontology TBox paths.
10. Emit checksums/tool versions/result states bound to exact commit.

## Status discipline
Until #44 executes, parser/reasoner/SHACL/CQ statuses are `NOT_RUN`, not PASS. #27 implementation success is not ontology validation.