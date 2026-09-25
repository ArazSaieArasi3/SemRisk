# SemRisk PostgreSQL relational twin

Issue: #46  
Projection version: `0.1.0-rc.1`  
Target: PostgreSQL 16+

## Clean build
Run governed migrations/companions in order:

1. `V001__paper1_projection.sql`
2. `V001__views.sql`
3. `V001__reference_data.sql`
4. `V002__data_load_support.sql`
5. `V005__r5_architecture_federation.sql`
6. `V006__r6_projection_integrity.sql`
7. integrity/regression tests and governed data loads.

The machine-readable order and immutable Git blob checksums are frozen in `relational/design/migration-manifest-v1.0.csv`.

For a clean local/test reset run `reset.sql` first.

Example:

```bash
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/reset.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__paper1_projection.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__views.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__reference_data.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V002__data_load_support.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V005__r5_architecture_federation.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V006__r6_projection_integrity.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/tests/V001__integrity_tests.sql
```

The ontology and governed semantic registries remain authoritative. The database is a bounded application projection. Historical migrations must not be edited after an evaluated release; use a new migration.

#47 owns staging/load/transformation/data-snapshot behavior.
