# SemRisk PostgreSQL relational twin

Issue: #46  
Projection version: `0.1.0-rc.1`  
Target: PostgreSQL 16+

## Clean build
Run in order:

1. `V001__paper1_projection.sql`
2. `V001__views.sql`
3. `V001__reference_data.sql`
4. `tests/V001__integrity_tests.sql`

For a clean local/test reset run `reset.sql` first.

Example:

```bash
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/reset.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__paper1_projection.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__views.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/V001__reference_data.sql
psql -v ON_ERROR_STOP=1 "$DATABASE_URL" -f relational/sql/tests/V001__integrity_tests.sql
```

The ontology and governed semantic registries remain authoritative. The database is a bounded application projection. Historical migrations must not be edited after an evaluated release; use a new migration.

#47 owns staging/load/transformation/data-snapshot behavior.
