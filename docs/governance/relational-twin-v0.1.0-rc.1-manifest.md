# SemRisk relational twin implementation manifest

**Projection version:** `0.1.0-rc.1`  
**Issue:** #46  
**Validated commit:** `a469c961f67ed8ebb9557e28949f780fe1cca5fd`  
**CI workflow:** SemRisk relational twin CI  
**Successful run:** `35987903713`  
**PostgreSQL runtime:** 16.15 in CI service container

## Bound implementation blobs
- `relational/sql/V001__paper1_projection.sql` — `379d48c552e7e307bb002fece88667d0d89eb83c`
- `relational/sql/V001__views.sql` — `9328c44ea2579f6672afb51577f769e2b7e4e87d`
- `relational/sql/V001__reference_data.sql` — `eb1a7f3f348e6b74d89cb041ff31481625daa5ac`
- `relational/sql/tests/V001__integrity_tests.sql` — `a130dda306b892442ab9c3edb35510e2817fdc46`
- `relational/scripts/validate_relational_catalog.py` — `7e9c9ef4ab74c34490317920e9bb59939141db9b`
- `relational/sql/reset.sql` — `abc9fd242c05c3ce8454d094b9ed5eb7690de478`

## Validation result
- 45/45 frozen #45 catalog objects implemented.
- 210/210 frozen field-catalog fields statically accounted for.
- 71/71 ontology↔RDB mappings resolve to implemented objects or explicit intentional metadata dispositions.
- PostgreSQL clean create: PASS.
- Integrity/negative tests: PASS.
- Derived Risk Owner view: PASS.
- Pharma CM-PharmE v1.0.0 target restriction: enforced and negative-tested.
- No primitive `core.risk.owner_id`: verified.
- Risk State and Workflow State remain separate.
- Inherent/residual remain assessment-result semantics over the same Risk identity.

Two convenience views exist beyond the frozen #45 catalog:
- `enterprise.v_current_workflow_state`
- `assessment.v_latest_result_by_kind`

They add no new semantic ownership and are treated as query conveniences only.
