# V007 migration and evidence boundary

Apply `V007__qualified_assessment_context.sql` after the six historical ordered schema/companion scripts ending at V006. It creates two tables (five scale columns and nine result-context columns), one qualified result view, temporal owner retrieval and validation/history functions, and adds one optional invalidation column to responsibility. The 15 new columns are documented in `qualified-context-field-map-v0.2.0-rc.1.csv`.

Existing rows retain their values and remain **unqualified** until actual context is available. No date, method, scale, score or projected/observed status is inferred during migration. The old `result_kind` and its convenience views remain for compatibility; qualified consumers use `v_qualified_result_context` and filter the separate axes. The old latest-by-kind view is not a cross-context comparison operation.

`U007__qualified_assessment_context.sql` permits rollback only while the added profile holds no data. It refuses rollback when qualified results, scales or invalidation values would be lost. Migration/rollback is tested on a disposable populated PostgreSQL database, never on a production database in this run. Historical V001/V002/V005/V006 scripts are not edited.

Qualified results are append-only, including their referenced method, activity and scale. Use a new result/method/scale identity for a new version; keep supersession and assessment-predecessor links. Validity is `[start,end)`; invalidation is a separate exclusion bound. SQL timestamps store instants; timezone presence is enforced at the supported input boundary.

Tests verify row-content preservation across migration, safe empty rollback, exact represented-field RDF round-trip, ownership parity at six instants, orthogonal result-context grouping and 17 named SQL rejection controls. These do not prove behavior under arbitrary concurrent workloads; no such assurance claim is made.
