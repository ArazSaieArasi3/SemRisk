-- SemRisk Paper-1 PostgreSQL relational twin
-- Issue #46 | projection version 0.1.0-rc.1
-- Target: PostgreSQL 16+
-- Semantic authority remains the SemRisk ontology; this DDL is a bounded application projection.

BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE SCHEMA IF NOT EXISTS meta;
CREATE SCHEMA IF NOT EXISTS ref;
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS assessment;
CREATE SCHEMA IF NOT EXISTS treatment;
CREATE SCHEMA IF NOT EXISTS enterprise;
CREATE SCHEMA IF NOT EXISTS governance;
CREATE SCHEMA IF NOT EXISTS pharma;
CREATE SCHEMA IF NOT EXISTS staging;

CREATE TABLE meta.source_artifact (
  source_artifact_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  source_kind text NOT NULL,
  locator text NOT NULL,
  version_ref text,
  sha256 text,
  license text,
  evidence_role text NOT NULL CHECK (evidence_role IN (
    'discovery','design','reconciliation','regression','comparative',
    'bounded_case','constructed_case','transferability_holdout',
    'independent_validation','synthetic_test','supplementary','provenance_only'
  )),
  accessed_at timestamptz
);

CREATE TABLE meta.semantic_instance (
  instance_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  instance_iri text NOT NULL UNIQUE,
  semantic_type_id text NOT NULL,
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  evidence_role text NOT NULL CHECK (evidence_role IN (
    'discovery','design','reconciliation','regression','comparative',
    'bounded_case','constructed_case','transferability_holdout',
    'independent_validation','synthetic_test','supplementary','provenance_only'
  )),
  synthetic_flag boolean NOT NULL DEFAULT false,
  created_at timestamptz NOT NULL DEFAULT transaction_timestamp(),
  CONSTRAINT ck_semantic_instance_synthetic_role
    CHECK (NOT synthetic_flag OR evidence_role <> 'independent_validation')
);

CREATE TABLE meta.instance_provenance (
  instance_provenance_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  source_artifact_id uuid NOT NULL REFERENCES meta.source_artifact(source_artifact_id),
  activity_iri text,
  agent_iri text,
  generated_at timestamptz,
  derivation_note text
);

CREATE TABLE meta.state_transition (
  transition_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  state_family text NOT NULL CHECK (state_family IN ('risk_state','workflow_state')),
  prior_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  next_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  observed_at timestamptz,
  CONSTRAINT ck_state_transition_not_self CHECK (prior_instance_id <> next_instance_id)
);

CREATE TABLE ref.external_entity (
  external_entity_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  instance_id uuid NOT NULL UNIQUE REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  owner_namespace text NOT NULL,
  owner_semantic_id text NOT NULL,
  version_ref text NOT NULL,
  label text,
  stereotype_code text,
  UNIQUE(owner_namespace, owner_semantic_id, version_ref)
);

CREATE TABLE core.risk (
  risk_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  title text,
  description text
);

CREATE TABLE core.risk_scenario (
  scenario_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  risk_id uuid REFERENCES core.risk(risk_id),
  description text
);

CREATE TABLE core.risk_event (
  event_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  realizes_scenario_id uuid REFERENCES core.risk_scenario(scenario_id),
  occurred_at timestamptz,
  valid_from timestamptz,
  valid_to timestamptz,
  description text,
  CONSTRAINT ck_risk_event_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE core.consequence (
  consequence_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  description text,
  valid_from timestamptz,
  valid_to timestamptz,
  CONSTRAINT ck_consequence_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE core.predisposing_condition (
  condition_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  description text,
  valid_from timestamptz,
  valid_to timestamptz,
  CONSTRAINT ck_predisposing_condition_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE core.trigger_event (
  trigger_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  occurred_at timestamptz,
  description text
);

CREATE TABLE core.vulnerability (
  vulnerability_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  bearer_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  description text
);

CREATE TABLE core.exposure (
  exposure_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  subject_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  source_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  valid_from timestamptz,
  valid_to timestamptz,
  CONSTRAINT ck_exposure_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE core.risk_source_link (
  risk_source_link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  risk_id uuid REFERENCES core.risk(risk_id),
  scenario_id uuid REFERENCES core.risk_scenario(scenario_id),
  source_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  relation_semantic_id text NOT NULL DEFAULT 'SR-REL-005' CHECK (relation_semantic_id='SR-REL-005'),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  CONSTRAINT ck_risk_source_exactly_one_target CHECK ((risk_id IS NOT NULL)::int + (scenario_id IS NOT NULL)::int = 1)
);

CREATE TABLE core.scenario_condition (
  scenario_id uuid NOT NULL REFERENCES core.risk_scenario(scenario_id) ON DELETE CASCADE,
  condition_id uuid NOT NULL REFERENCES core.predisposing_condition(condition_id) ON DELETE CASCADE,
  PRIMARY KEY (scenario_id, condition_id)
);

CREATE TABLE core.event_trigger (
  event_id uuid NOT NULL REFERENCES core.risk_event(event_id) ON DELETE CASCADE,
  trigger_id uuid NOT NULL REFERENCES core.trigger_event(trigger_id) ON DELETE CASCADE,
  PRIMARY KEY (event_id, trigger_id)
);

CREATE TABLE core.event_consequence (
  link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_id uuid REFERENCES core.risk_event(event_id),
  scenario_id uuid REFERENCES core.risk_scenario(scenario_id),
  consequence_id uuid NOT NULL REFERENCES core.consequence(consequence_id),
  CONSTRAINT ck_event_consequence_one_source CHECK ((event_id IS NOT NULL)::int + (scenario_id IS NOT NULL)::int = 1)
);

CREATE TABLE core.semantic_relation_assertion (
  assertion_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  relation_semantic_id text NOT NULL CHECK (relation_semantic_id IN ('SR-REL-008','SR-REL-009','SR-REL-010')),
  subject_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  object_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  confidence_code text
);

CREATE TABLE assessment.assessment_method (
  method_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  method_code text NOT NULL,
  version_ref text,
  external_ref text
);

CREATE TABLE assessment.assessment_activity (
  assessment_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  risk_id uuid NOT NULL REFERENCES core.risk(risk_id),
  method_id uuid REFERENCES assessment.assessment_method(method_id),
  prior_assessment_id uuid REFERENCES assessment.assessment_activity(assessment_id),
  started_at timestamptz,
  ended_at timestamptz,
  CONSTRAINT ck_assessment_activity_period CHECK (ended_at IS NULL OR started_at IS NULL OR ended_at >= started_at),
  CONSTRAINT ck_assessment_not_self_prior CHECK (prior_assessment_id IS NULL OR prior_assessment_id <> assessment_id)
);

CREATE TABLE assessment.assessment_result (
  result_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  assessment_id uuid NOT NULL REFERENCES assessment.assessment_activity(assessment_id),
  risk_id uuid NOT NULL REFERENCES core.risk(risk_id),
  result_kind text NOT NULL CHECK (result_kind IN ('generic','likelihood','impact','risk_level','inherent','residual')),
  supersedes_result_id uuid REFERENCES assessment.assessment_result(result_id),
  value_numeric numeric,
  value_text text,
  value_code text,
  CONSTRAINT ck_assessment_result_one_primary_value CHECK (
    (value_numeric IS NOT NULL)::int + (value_text IS NOT NULL)::int + (value_code IS NOT NULL)::int <= 1
  ),
  CONSTRAINT ck_assessment_result_not_self_supersede CHECK (supersedes_result_id IS NULL OR supersedes_result_id <> result_id)
);

CREATE TABLE assessment.assessment_confidence (
  confidence_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  result_id uuid NOT NULL REFERENCES assessment.assessment_result(result_id) ON DELETE CASCADE,
  confidence_code text,
  confidence_value numeric,
  method_ref text
);

CREATE TABLE assessment.evidence_item (
  evidence_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  content_locator text,
  source_artifact_id uuid NOT NULL REFERENCES meta.source_artifact(source_artifact_id),
  evidence_kind text
);

CREATE TABLE assessment.assessment_evidence (
  result_id uuid NOT NULL REFERENCES assessment.assessment_result(result_id) ON DELETE CASCADE,
  evidence_id uuid NOT NULL REFERENCES assessment.evidence_item(evidence_id) ON DELETE CASCADE,
  support_role text NOT NULL CHECK (support_role IN ('support','challenge','context')),
  PRIMARY KEY (result_id, evidence_id)
);

CREATE TABLE assessment.observation_activity (
  observation_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  started_at timestamptz,
  ended_at timestamptz,
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  CONSTRAINT ck_observation_activity_period CHECK (ended_at IS NULL OR started_at IS NULL OR ended_at >= started_at)
);

CREATE TABLE assessment.observation_result (
  observation_result_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  observation_id uuid NOT NULL REFERENCES assessment.observation_activity(observation_id),
  value_numeric numeric,
  value_text text,
  CONSTRAINT ck_observation_result_one_value CHECK (
    (value_numeric IS NOT NULL)::int + (value_text IS NOT NULL)::int <= 1
  )
);

CREATE TABLE treatment.strategy (
  strategy_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  title text,
  description text
);

CREATE TABLE treatment.plan (
  plan_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  strategy_id uuid REFERENCES treatment.strategy(strategy_id),
  title text,
  status_code text
);

CREATE TABLE treatment.activity (
  activity_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  plan_id uuid REFERENCES treatment.plan(plan_id),
  started_at timestamptz,
  ended_at timestamptz,
  CONSTRAINT ck_treatment_activity_period CHECK (ended_at IS NULL OR started_at IS NULL OR ended_at >= started_at)
);

CREATE TABLE treatment.control_mechanism (
  control_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  external_entity_id uuid REFERENCES ref.external_entity(external_entity_id),
  description text
);

CREATE TABLE treatment.activity_control (
  activity_id uuid NOT NULL REFERENCES treatment.activity(activity_id) ON DELETE CASCADE,
  control_id uuid NOT NULL REFERENCES treatment.control_mechanism(control_id) ON DELETE CASCADE,
  PRIMARY KEY (activity_id, control_id)
);

CREATE TABLE treatment.control_protection (
  link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  control_id uuid NOT NULL REFERENCES treatment.control_mechanism(control_id),
  protected_instance_id uuid REFERENCES meta.semantic_instance(instance_id),
  external_entity_id uuid REFERENCES ref.external_entity(external_entity_id),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  CONSTRAINT ck_control_protection_one_target CHECK (
    (protected_instance_id IS NOT NULL)::int + (external_entity_id IS NOT NULL)::int = 1
  )
);

CREATE TABLE enterprise.risk_register (
  register_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  name text NOT NULL,
  scope_ref text,
  version_label text
);

CREATE TABLE enterprise.risk_register_entry (
  entry_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  register_id uuid NOT NULL REFERENCES enterprise.risk_register(register_id),
  risk_id uuid NOT NULL REFERENCES core.risk(risk_id),
  title text,
  description text
);

CREATE TABLE enterprise.scenario_description (
  description_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  scenario_id uuid NOT NULL REFERENCES core.risk_scenario(scenario_id),
  entry_id uuid REFERENCES enterprise.risk_register_entry(entry_id),
  text_value text NOT NULL
);

CREATE TABLE enterprise.workflow_state_history (
  workflow_state_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  entry_id uuid NOT NULL REFERENCES enterprise.risk_register_entry(entry_id),
  state_code text NOT NULL,
  valid_from timestamptz,
  valid_to timestamptz,
  is_current boolean NOT NULL DEFAULT false,
  CONSTRAINT ck_workflow_state_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE UNIQUE INDEX uq_workflow_state_current
  ON enterprise.workflow_state_history(entry_id)
  WHERE is_current;

CREATE TABLE enterprise.risk_state_history (
  risk_state_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  risk_id uuid NOT NULL REFERENCES core.risk(risk_id),
  state_code text NOT NULL,
  valid_from timestamptz,
  valid_to timestamptz,
  evidence_result_id uuid REFERENCES assessment.assessment_result(result_id),
  CONSTRAINT ck_risk_state_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE enterprise.actor_ref (
  actor_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  external_entity_id uuid REFERENCES ref.external_entity(external_entity_id),
  actor_kind text,
  label text
);

CREATE TABLE enterprise.risk_responsibility (
  responsibility_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  actor_id uuid NOT NULL REFERENCES enterprise.actor_ref(actor_id),
  risk_id uuid REFERENCES core.risk(risk_id),
  entry_id uuid REFERENCES enterprise.risk_register_entry(entry_id),
  plan_id uuid REFERENCES treatment.plan(plan_id),
  valid_from timestamptz,
  valid_to timestamptz,
  CONSTRAINT ck_risk_responsibility_one_target CHECK (
    (risk_id IS NOT NULL)::int + (entry_id IS NOT NULL)::int + (plan_id IS NOT NULL)::int = 1
  ),
  CONSTRAINT ck_risk_responsibility_period CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to > valid_from)
);

CREATE TABLE treatment.risk_strategy_selection (
  selection_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  risk_id uuid NOT NULL REFERENCES core.risk(risk_id),
  register_entry_id uuid REFERENCES enterprise.risk_register_entry(entry_id),
  strategy_id uuid NOT NULL REFERENCES treatment.strategy(strategy_id),
  selected_at timestamptz
);

CREATE TABLE governance.indicator (
  indicator_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  name text NOT NULL,
  method_ref text
);

CREATE TABLE governance.threshold (
  threshold_id uuid PRIMARY KEY REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  indicator_id uuid REFERENCES governance.indicator(indicator_id),
  method_id uuid REFERENCES assessment.assessment_method(method_id),
  comparator text NOT NULL CHECK (comparator IN ('>','>=','=','<=','<','between','in')),
  value_numeric numeric,
  value_text text,
  unit text,
  CONSTRAINT ck_threshold_value CHECK ((value_numeric IS NOT NULL)::int + (value_text IS NOT NULL)::int = 1)
);

CREATE TABLE governance.risk_indicator (
  link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  risk_id uuid REFERENCES core.risk(risk_id),
  external_entity_id uuid REFERENCES ref.external_entity(external_entity_id),
  indicator_id uuid NOT NULL REFERENCES governance.indicator(indicator_id),
  CONSTRAINT ck_risk_indicator_one_context CHECK (
    (risk_id IS NOT NULL)::int + (external_entity_id IS NOT NULL)::int = 1
  )
);

CREATE TABLE pharma.context_link (
  context_link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  risk_id uuid REFERENCES core.risk(risk_id),
  scenario_id uuid REFERENCES core.risk_scenario(scenario_id),
  event_id uuid REFERENCES core.risk_event(event_id),
  consequence_id uuid REFERENCES core.consequence(consequence_id),
  external_entity_id uuid NOT NULL REFERENCES ref.external_entity(external_entity_id),
  bridge_relation_id text NOT NULL DEFAULT 'SR-REL-037' CHECK (bridge_relation_id='SR-REL-037'),
  CONSTRAINT ck_pharma_context_one_source CHECK (
    (risk_id IS NOT NULL)::int + (scenario_id IS NOT NULL)::int +
    (event_id IS NOT NULL)::int + (consequence_id IS NOT NULL)::int = 1
  )
);

CREATE OR REPLACE FUNCTION pharma.enforce_cm_pharme_target()
RETURNS trigger
LANGUAGE plpgsql
AS $semrisk$
DECLARE
  ns text;
  vr text;
BEGIN
  SELECT owner_namespace, version_ref INTO ns, vr
  FROM ref.external_entity
  WHERE external_entity_id = NEW.external_entity_id;

  IF ns IS DISTINCT FROM 'CM-PharmE' OR vr IS DISTINCT FROM 'v1.0.0' THEN
    RAISE EXCEPTION 'pharma.context_link requires CM-PharmE v1.0.0 target; got namespace=%, version=%', ns, vr
      USING ERRCODE = '23514';
  END IF;
  RETURN NEW;
END $semrisk$;

CREATE TRIGGER trg_pharma_context_cm_pharme_target
BEFORE INSERT OR UPDATE OF external_entity_id ON pharma.context_link
FOR EACH ROW EXECUTE FUNCTION pharma.enforce_cm_pharme_target();

CREATE INDEX ix_semantic_instance_type ON meta.semantic_instance(semantic_type_id);
CREATE INDEX ix_semantic_instance_source ON meta.semantic_instance(source_artifact_id);
CREATE INDEX ix_instance_provenance_instance ON meta.instance_provenance(instance_id);
CREATE INDEX ix_external_entity_owner ON ref.external_entity(owner_namespace, owner_semantic_id, version_ref);
CREATE INDEX ix_risk_scenario_risk ON core.risk_scenario(risk_id);
CREATE INDEX ix_risk_event_scenario ON core.risk_event(realizes_scenario_id);
CREATE INDEX ix_assessment_activity_risk ON assessment.assessment_activity(risk_id);
CREATE INDEX ix_assessment_result_risk ON assessment.assessment_result(risk_id, result_kind);
CREATE INDEX ix_assessment_evidence_evidence ON assessment.assessment_evidence(evidence_id);
CREATE INDEX ix_register_entry_risk ON enterprise.risk_register_entry(risk_id);
CREATE INDEX ix_risk_state_risk ON enterprise.risk_state_history(risk_id, valid_from);
CREATE INDEX ix_responsibility_risk ON enterprise.risk_responsibility(risk_id);
CREATE INDEX ix_pharma_context_external ON pharma.context_link(external_entity_id);

COMMIT;
