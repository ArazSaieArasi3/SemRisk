-- SemRisk R6 projection-integrity hardening
-- Issues #97 #98 #99 #101 | additive migration after V002 and V005
-- Semantic authority remains the SemRisk ontology; constraints below are bounded projection integrity.

BEGIN;

-- #97 Stable actor projection identity. Nullable for migration compatibility;
-- evaluated Paper-1 fixtures are required by CI to populate it.
ALTER TABLE enterprise.actor_ref
  ADD COLUMN IF NOT EXISTS actor_iri text;

CREATE UNIQUE INDEX IF NOT EXISTS uq_actor_ref_actor_iri
  ON enterprise.actor_ref(actor_iri)
  WHERE actor_iri IS NOT NULL;

COMMENT ON COLUMN enterprise.actor_ref.actor_iri IS
  'Stable projection/reference IRI for actor identity; not a local ontology ownership assertion.';

-- #98 State-transition scope integrity.
CREATE OR REPLACE FUNCTION meta.enforce_state_transition_scope()
RETURNS trigger
LANGUAGE plpgsql
AS $semrisk$
DECLARE
  prior_target uuid;
  next_target uuid;
  prior_from timestamptz;
  next_from timestamptz;
BEGIN
  IF NEW.prior_instance_id = NEW.next_instance_id THEN
    RAISE EXCEPTION 'state transition cannot self-loop'
      USING ERRCODE = '23514';
  END IF;

  IF NEW.state_family = 'risk_state' THEN
    SELECT risk_id, valid_from INTO prior_target, prior_from
    FROM enterprise.risk_state_history
    WHERE risk_state_id = NEW.prior_instance_id;

    SELECT risk_id, valid_from INTO next_target, next_from
    FROM enterprise.risk_state_history
    WHERE risk_state_id = NEW.next_instance_id;

    IF prior_target IS NULL OR next_target IS NULL THEN
      RAISE EXCEPTION 'risk_state transition endpoints must both be Risk State rows'
        USING ERRCODE = '23514';
    END IF;

    IF prior_target <> next_target THEN
      RAISE EXCEPTION 'risk_state transition endpoints must concern the same Risk'
        USING ERRCODE = '23514';
    END IF;

  ELSIF NEW.state_family = 'workflow_state' THEN
    SELECT entry_id, valid_from INTO prior_target, prior_from
    FROM enterprise.workflow_state_history
    WHERE workflow_state_id = NEW.prior_instance_id;

    SELECT entry_id, valid_from INTO next_target, next_from
    FROM enterprise.workflow_state_history
    WHERE workflow_state_id = NEW.next_instance_id;

    IF prior_target IS NULL OR next_target IS NULL THEN
      RAISE EXCEPTION 'workflow_state transition endpoints must both be Workflow State rows'
        USING ERRCODE = '23514';
    END IF;

    IF prior_target <> next_target THEN
      RAISE EXCEPTION 'workflow_state transition endpoints must concern the same Register Entry'
        USING ERRCODE = '23514';
    END IF;
  END IF;

  IF prior_from IS NOT NULL AND next_from IS NOT NULL AND next_from < prior_from THEN
    RAISE EXCEPTION 'state transition temporal order contradicts known valid_from values'
      USING ERRCODE = '23514';
  END IF;

  RETURN NEW;
END
$semrisk$;

DROP TRIGGER IF EXISTS trg_state_transition_scope ON meta.state_transition;
CREATE TRIGGER trg_state_transition_scope
BEFORE INSERT OR UPDATE OF state_family, prior_instance_id, next_instance_id
ON meta.state_transition
FOR EACH ROW EXECUTE FUNCTION meta.enforce_state_transition_scope();

-- #99 Reassessment lineage integrity: same Risk, acyclic predecessor chain.
CREATE OR REPLACE FUNCTION assessment.enforce_prior_assessment_lineage()
RETURNS trigger
LANGUAGE plpgsql
AS $semrisk$
DECLARE
  prior_risk uuid;
  cycle_found boolean;
BEGIN
  IF NEW.prior_assessment_id IS NULL THEN
    RETURN NEW;
  END IF;

  SELECT risk_id INTO prior_risk
  FROM assessment.assessment_activity
  WHERE assessment_id = NEW.prior_assessment_id;

  IF prior_risk IS NULL THEN
    RAISE EXCEPTION 'prior assessment must exist'
      USING ERRCODE = '23503';
  END IF;

  IF prior_risk <> NEW.risk_id THEN
    RAISE EXCEPTION 'prior assessment must concern the same Risk'
      USING ERRCODE = '23514';
  END IF;

  WITH RECURSIVE chain(assessment_id, prior_assessment_id, path) AS (
    SELECT a.assessment_id, a.prior_assessment_id, ARRAY[a.assessment_id]::uuid[]
    FROM assessment.assessment_activity a
    WHERE a.assessment_id = NEW.prior_assessment_id
    UNION ALL
    SELECT a.assessment_id, a.prior_assessment_id, c.path || a.assessment_id
    FROM assessment.assessment_activity a
    JOIN chain c ON a.assessment_id = c.prior_assessment_id
    WHERE NOT a.assessment_id = ANY(c.path)
  )
  SELECT EXISTS (
    SELECT 1 FROM chain
    WHERE assessment_id = NEW.assessment_id
       OR prior_assessment_id = NEW.assessment_id
  ) INTO cycle_found;

  IF cycle_found THEN
    RAISE EXCEPTION 'assessment predecessor lineage would create a cycle'
      USING ERRCODE = '23514';
  END IF;

  RETURN NEW;
END
$semrisk$;

DROP TRIGGER IF EXISTS trg_assessment_prior_lineage ON assessment.assessment_activity;
CREATE TRIGGER trg_assessment_prior_lineage
BEFORE INSERT OR UPDATE OF prior_assessment_id, risk_id
ON assessment.assessment_activity
FOR EACH ROW EXECUTE FUNCTION assessment.enforce_prior_assessment_lineage();

-- #99 Result supersession: same Risk, acyclic chain.
CREATE OR REPLACE FUNCTION assessment.enforce_result_supersession_lineage()
RETURNS trigger
LANGUAGE plpgsql
AS $semrisk$
DECLARE
  prior_risk uuid;
  cycle_found boolean;
BEGIN
  IF NEW.supersedes_result_id IS NULL THEN
    RETURN NEW;
  END IF;

  SELECT risk_id INTO prior_risk
  FROM assessment.assessment_result
  WHERE result_id = NEW.supersedes_result_id;

  IF prior_risk IS NULL THEN
    RAISE EXCEPTION 'superseded result must exist'
      USING ERRCODE = '23503';
  END IF;

  IF prior_risk <> NEW.risk_id THEN
    RAISE EXCEPTION 'superseded result must concern the same Risk'
      USING ERRCODE = '23514';
  END IF;

  WITH RECURSIVE chain(result_id, supersedes_result_id, path) AS (
    SELECT r.result_id, r.supersedes_result_id, ARRAY[r.result_id]::uuid[]
    FROM assessment.assessment_result r
    WHERE r.result_id = NEW.supersedes_result_id
    UNION ALL
    SELECT r.result_id, r.supersedes_result_id, c.path || r.result_id
    FROM assessment.assessment_result r
    JOIN chain c ON r.result_id = c.supersedes_result_id
    WHERE NOT r.result_id = ANY(c.path)
  )
  SELECT EXISTS (
    SELECT 1 FROM chain
    WHERE result_id = NEW.result_id
       OR supersedes_result_id = NEW.result_id
  ) INTO cycle_found;

  IF cycle_found THEN
    RAISE EXCEPTION 'result supersession lineage would create a cycle'
      USING ERRCODE = '23514';
  END IF;

  RETURN NEW;
END
$semrisk$;

DROP TRIGGER IF EXISTS trg_result_supersession_lineage ON assessment.assessment_result;
CREATE TRIGGER trg_result_supersession_lineage
BEFORE INSERT OR UPDATE OF supersedes_result_id, risk_id
ON assessment.assessment_result
FOR EACH ROW EXECUTE FUNCTION assessment.enforce_result_supersession_lineage();

-- #99 "Latest" is assessment/projection-time grounded, never UUID-order grounded.
CREATE OR REPLACE VIEW assessment.v_latest_result_by_kind AS
SELECT DISTINCT ON (r.risk_id, r.result_kind)
  r.result_id, r.assessment_id, r.risk_id, r.result_kind, r.supersedes_result_id,
  r.value_numeric, r.value_text, r.value_code
FROM assessment.assessment_result r
JOIN assessment.assessment_activity a ON a.assessment_id = r.assessment_id
JOIN meta.semantic_instance si ON si.instance_id = r.result_id
ORDER BY
  r.risk_id,
  r.result_kind,
  COALESCE(a.ended_at, a.started_at, si.created_at) DESC,
  si.created_at DESC,
  r.result_id DESC;

COMMENT ON VIEW assessment.v_latest_result_by_kind IS
  'Application convenience: latest by assessment end/start time with projection created_at fallback; UUID is tie-breaker only.';

-- #101 Post-load lineage reconciliation. This remains a view rather than an
-- insert-time FK so staging can precede target creation.
CREATE OR REPLACE VIEW staging.v_lineage_reconciliation AS
SELECT
  sr.source_record_id,
  sr.load_batch_id,
  sr.source_artifact_id,
  sr.source_record_key,
  sr.transform_rule_id,
  sr.target_instance_iri,
  sr.disposition,
  si.instance_id AS resolved_instance_id,
  CASE
    WHEN sr.disposition IN ('loaded','external_owner')
         AND sr.target_instance_iri IS NULL
      THEN 'MISSING_TARGET_IRI'
    WHEN sr.target_instance_iri IS NOT NULL
         AND si.instance_id IS NULL
      THEN 'UNRESOLVED_TARGET'
    WHEN sr.target_instance_iri IS NOT NULL
         AND (sr.transform_rule_id IS NULL OR btrim(sr.transform_rule_id)='')
      THEN 'MISSING_TRANSFORM_RULE'
    WHEN sr.disposition IN ('blocked','protected','rejected')
         AND sr.target_instance_iri IS NOT NULL
      THEN 'FORBIDDEN_TARGET_FOR_NONLOAD'
    ELSE 'OK'
  END AS lineage_status
FROM staging.source_record sr
LEFT JOIN meta.semantic_instance si
  ON si.instance_iri = sr.target_instance_iri;

COMMIT;
