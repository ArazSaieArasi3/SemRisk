-- Additive operational profile 0.2.0-rc.1. Apply after V006.
-- Existing results remain explicitly unqualified; no inferred/backfilled scores.
BEGIN;
CREATE TABLE assessment.numeric_scale (
  scale_iri text PRIMARY KEY,
  version_ref text NOT NULL CHECK (btrim(version_ref) <> ''),
  dimension text NOT NULL CHECK (dimension IN ('Likelihood','Impact','RiskLevel')),
  minimum numeric NOT NULL,
  maximum numeric NOT NULL,
  CHECK (minimum <= maximum AND minimum > '-Infinity'::numeric AND maximum < 'Infinity'::numeric)
);
CREATE TABLE assessment.result_context (
  result_id uuid PRIMARY KEY REFERENCES assessment.assessment_result(result_id),
  dimension text NOT NULL CHECK (dimension IN ('Likelihood','Impact','RiskLevel')),
  control_baseline text NOT NULL CHECK (control_baseline IN ('BeforeControl','AfterControl')),
  evaluation_basis text NOT NULL CHECK (evaluation_basis IN ('Observed','Projected')),
  scale_iri text NOT NULL REFERENCES assessment.numeric_scale(scale_iri),
  method_id uuid NOT NULL REFERENCES assessment.assessment_method(method_id),
  method_version text NOT NULL CHECK (btrim(method_version) <> ''),
  assessed_at timestamptz NOT NULL CHECK (isfinite(assessed_at)),
  reference_time timestamptz NOT NULL CHECK (isfinite(reference_time))
);
ALTER TABLE enterprise.risk_responsibility ADD COLUMN invalidated_at timestamptz;
COMMENT ON COLUMN enterprise.risk_responsibility.invalidated_at IS
 'PROV invalidation instant, independent of validity end; a known invalidation excludes the assignment at and after that instant.';

CREATE FUNCTION assessment.parse_zoned_timestamp(input_text text)
RETURNS timestamptz LANGUAGE plpgsql STABLE STRICT AS $body$
BEGIN
 IF input_text !~ '(Z|[+-][0-9]{2}:[0-9]{2})$' THEN
   RAISE EXCEPTION 'explicit timestamp timezone required' USING ERRCODE='23514';
 END IF;
 RETURN input_text::timestamptz;
END $body$;

CREATE FUNCTION assessment.enforce_result_context()
RETURNS trigger LANGUAGE plpgsql AS $body$
DECLARE
 result_row assessment.assessment_result%ROWTYPE;
 activity_row assessment.assessment_activity%ROWTYPE;
 method_row assessment.assessment_method%ROWTYPE;
 scale_row assessment.numeric_scale%ROWTYPE;
 prior_time timestamptz;
BEGIN
 IF TG_OP <> 'INSERT' THEN
   RAISE EXCEPTION 'qualified context is append-only; create a successor result' USING ERRCODE='23514';
 END IF;
 SELECT * INTO STRICT result_row FROM assessment.assessment_result WHERE result_id=NEW.result_id FOR SHARE;
 SELECT * INTO STRICT activity_row FROM assessment.assessment_activity WHERE assessment_id=result_row.assessment_id FOR SHARE;
 SELECT * INTO STRICT method_row FROM assessment.assessment_method WHERE method_id=NEW.method_id FOR SHARE;
 SELECT * INTO STRICT scale_row FROM assessment.numeric_scale WHERE scale_iri=NEW.scale_iri FOR SHARE;
 IF result_row.risk_id <> activity_row.risk_id OR activity_row.method_id IS DISTINCT FROM NEW.method_id
    OR method_row.version_ref IS DISTINCT FROM NEW.method_version THEN
   RAISE EXCEPTION 'context activity/risk/method/version mismatch' USING ERRCODE='23514';
 END IF;
 IF NEW.dimension <> scale_row.dimension OR result_row.value_numeric IS NULL
    OR NOT (result_row.value_numeric BETWEEN scale_row.minimum AND scale_row.maximum) THEN
   RAISE EXCEPTION 'context numeric value/dimension incompatible with scale' USING ERRCODE='23514';
 END IF;
 -- Legacy result_kind is a compatibility discriminator, not the full context.
 IF (result_row.result_kind='likelihood' AND NEW.dimension<>'Likelihood')
 OR (result_row.result_kind='impact' AND NEW.dimension<>'Impact')
 OR (result_row.result_kind='risk_level' AND NEW.dimension<>'RiskLevel')
 OR (result_row.result_kind='inherent' AND NEW.control_baseline<>'BeforeControl')
 OR (result_row.result_kind='residual' AND NEW.control_baseline<>'AfterControl') THEN
   RAISE EXCEPTION 'qualified context contradicts legacy result kind' USING ERRCODE='23514';
 END IF;
 IF result_row.supersedes_result_id IS NOT NULL THEN
   PERFORM 1 FROM assessment.assessment_result WHERE result_id=result_row.supersedes_result_id FOR SHARE;
   SELECT assessed_at INTO prior_time FROM assessment.result_context WHERE result_id=result_row.supersedes_result_id;
   IF prior_time IS NOT NULL AND NEW.assessed_at < prior_time THEN
     RAISE EXCEPTION 'successor assessment time precedes predecessor' USING ERRCODE='23514';
   END IF;
 END IF;
 RETURN NEW;
END $body$;
CREATE TRIGGER trg_result_context_integrity BEFORE INSERT OR UPDATE OR DELETE
 ON assessment.result_context FOR EACH ROW EXECUTE FUNCTION assessment.enforce_result_context();

CREATE FUNCTION assessment.guard_qualified_history()
RETURNS trigger LANGUAGE plpgsql AS $body$
DECLARE used boolean := false;
BEGIN
 IF TG_TABLE_NAME='assessment_result' THEN
   SELECT EXISTS(SELECT 1 FROM assessment.result_context q WHERE q.result_id=OLD.result_id)
    OR EXISTS(SELECT 1 FROM assessment.assessment_result r JOIN assessment.result_context q USING(result_id)
              WHERE r.supersedes_result_id=OLD.result_id) INTO used;
 ELSIF TG_TABLE_NAME='assessment_activity' THEN
   SELECT EXISTS(SELECT 1 FROM assessment.assessment_result r JOIN assessment.result_context q USING(result_id)
                 WHERE r.assessment_id=OLD.assessment_id) INTO used;
 ELSIF TG_TABLE_NAME='assessment_method' THEN
   SELECT EXISTS(SELECT 1 FROM assessment.result_context WHERE method_id=OLD.method_id) INTO used;
 ELSIF TG_TABLE_NAME='numeric_scale' THEN
   SELECT EXISTS(SELECT 1 FROM assessment.result_context WHERE scale_iri=OLD.scale_iri) INTO used;
 END IF;
 IF used AND (TG_OP='DELETE' OR NEW IS DISTINCT FROM OLD) THEN
   RAISE EXCEPTION 'referenced qualified history is immutable; create a new version/result' USING ERRCODE='23514';
 END IF;
 IF TG_OP='DELETE' THEN RETURN OLD; END IF;
 RETURN NEW;
END $body$;
CREATE TRIGGER trg_qualified_result_history BEFORE UPDATE OR DELETE ON assessment.assessment_result
 FOR EACH ROW EXECUTE FUNCTION assessment.guard_qualified_history();
CREATE TRIGGER trg_qualified_activity_history BEFORE UPDATE OR DELETE ON assessment.assessment_activity
 FOR EACH ROW EXECUTE FUNCTION assessment.guard_qualified_history();
CREATE TRIGGER trg_qualified_method_history BEFORE UPDATE OR DELETE ON assessment.assessment_method
 FOR EACH ROW EXECUTE FUNCTION assessment.guard_qualified_history();
CREATE TRIGGER trg_qualified_scale_history BEFORE UPDATE OR DELETE ON assessment.numeric_scale
 FOR EACH ROW EXECUTE FUNCTION assessment.guard_qualified_history();

CREATE VIEW assessment.v_qualified_result_context AS
 SELECT si.instance_iri AS result_iri, ri.instance_iri AS risk_iri,
 ai.instance_iri AS assessment_iri, mi.instance_iri AS method_iri,
 q.dimension, q.control_baseline, q.evaluation_basis, q.scale_iri, s.version_ref AS scale_version,
 s.minimum, s.maximum, q.method_version, q.assessed_at, q.reference_time, r.value_numeric,
 pi.instance_iri AS supersedes_iri
 FROM assessment.result_context q
 JOIN assessment.assessment_result r USING(result_id)
 JOIN assessment.numeric_scale s USING(scale_iri)
 JOIN meta.semantic_instance si ON si.instance_id=r.result_id
 JOIN meta.semantic_instance ri ON ri.instance_id=r.risk_id
 JOIN meta.semantic_instance ai ON ai.instance_id=r.assessment_id
 JOIN meta.semantic_instance mi ON mi.instance_id=q.method_id
 LEFT JOIN meta.semantic_instance pi ON pi.instance_id=r.supersedes_result_id;

CREATE FUNCTION enterprise.risk_owners_at(as_of_time timestamptz)
RETURNS TABLE(risk_iri text,actor_iri text) LANGUAGE sql STABLE STRICT AS $body$
 SELECT DISTINCT si.instance_iri, a.actor_iri
 FROM enterprise.risk_responsibility rr
 JOIN meta.semantic_instance si ON si.instance_id=rr.risk_id
 JOIN enterprise.actor_ref a USING(actor_id)
 WHERE rr.valid_from IS NOT NULL AND rr.valid_from <= as_of_time
   AND (rr.valid_to IS NULL OR as_of_time < rr.valid_to)
   AND (rr.invalidated_at IS NULL OR as_of_time < rr.invalidated_at)
   AND a.actor_iri IS NOT NULL
$body$;
COMMENT ON FUNCTION enterprise.risk_owners_at(timestamptz) IS
 'Qualified risk-scoped ownership at explicit time; unknown starts excluded; co-owners retained; does not infer entry/plan responsibility as risk ownership.';
COMMIT;
