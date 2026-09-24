-- SemRisk derived views | Issue #46
BEGIN;

CREATE OR REPLACE VIEW enterprise.v_risk_owner AS
SELECT
  rr.risk_id,
  rr.entry_id,
  rr.actor_id,
  rr.responsibility_id
FROM enterprise.risk_responsibility rr
WHERE rr.valid_from IS NULL OR rr.valid_from <= transaction_timestamp()
  AND (rr.valid_to IS NULL OR rr.valid_to > transaction_timestamp())
  AND (rr.risk_id IS NOT NULL OR rr.entry_id IS NOT NULL);

CREATE OR REPLACE VIEW enterprise.v_current_workflow_state AS
SELECT workflow_state_id, entry_id, state_code, valid_from, valid_to
FROM enterprise.workflow_state_history
WHERE is_current;

CREATE OR REPLACE VIEW assessment.v_latest_result_by_kind AS
SELECT DISTINCT ON (risk_id, result_kind)
  result_id, assessment_id, risk_id, result_kind, supersedes_result_id,
  value_numeric, value_text, value_code
FROM assessment.assessment_result
ORDER BY risk_id, result_kind, result_id DESC;

COMMIT;
