-- Refuse data-losing rollback. Export/migrate qualified data before retiring profile.
BEGIN;
DO $body$
BEGIN
 IF EXISTS(SELECT 1 FROM assessment.result_context)
 OR EXISTS(SELECT 1 FROM assessment.numeric_scale)
 OR EXISTS(SELECT 1 FROM enterprise.risk_responsibility WHERE invalidated_at IS NOT NULL) THEN
  RAISE EXCEPTION 'rollback refused: qualified profile data would be lost' USING ERRCODE='23514';
 END IF;
END $body$;
DROP VIEW assessment.v_qualified_result_context;
DROP FUNCTION enterprise.risk_owners_at(timestamptz);
DROP TRIGGER trg_qualified_result_history ON assessment.assessment_result;
DROP TRIGGER trg_qualified_activity_history ON assessment.assessment_activity;
DROP TRIGGER trg_qualified_method_history ON assessment.assessment_method;
DROP TRIGGER trg_qualified_scale_history ON assessment.numeric_scale;
DROP FUNCTION assessment.guard_qualified_history();
DROP TRIGGER trg_result_context_integrity ON assessment.result_context;
DROP FUNCTION assessment.enforce_result_context();
DROP FUNCTION assessment.parse_zoned_timestamp(text);
DROP TABLE assessment.result_context;
DROP TABLE assessment.numeric_scale;
ALTER TABLE enterprise.risk_responsibility DROP COLUMN invalidated_at;
COMMIT;
