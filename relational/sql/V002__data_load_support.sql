-- SemRisk governed data-load support | Issue #47
-- Migration V002: staging/quarantine/batch lineage. No semantic ownership is introduced here.
BEGIN;

CREATE TABLE staging.load_batch (
  load_batch_id uuid PRIMARY KEY,
  batch_code text NOT NULL UNIQUE,
  pipeline_version text NOT NULL,
  started_at timestamptz NOT NULL DEFAULT transaction_timestamp(),
  completed_at timestamptz,
  status text NOT NULL CHECK (status IN ('started','completed','failed','partial')),
  source_scope text NOT NULL,
  repository_commit text,
  notes text
);

CREATE TABLE staging.source_record (
  source_record_id uuid PRIMARY KEY,
  load_batch_id uuid NOT NULL REFERENCES staging.load_batch(load_batch_id),
  source_artifact_id uuid NOT NULL REFERENCES meta.source_artifact(source_artifact_id),
  source_record_key text NOT NULL,
  source_locator text NOT NULL,
  raw_semantic_summary text,
  transform_rule_id text,
  target_instance_iri text,
  disposition text NOT NULL CHECK (disposition IN (
    'loaded','context_only','partial','external_owner','unobserved','blocked','protected','rejected'
  )),
  UNIQUE(load_batch_id, source_artifact_id, source_record_key)
);

CREATE TABLE staging.reject_record (
  reject_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  load_batch_id uuid NOT NULL REFERENCES staging.load_batch(load_batch_id),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  source_record_key text,
  source_locator text,
  reason_code text NOT NULL,
  reason_detail text,
  retained_value text,
  created_at timestamptz NOT NULL DEFAULT transaction_timestamp()
);

CREATE INDEX ix_source_record_batch ON staging.source_record(load_batch_id);
CREATE INDEX ix_source_record_target ON staging.source_record(target_instance_iri);
CREATE INDEX ix_reject_record_batch ON staging.reject_record(load_batch_id);

COMMIT;
