-- SemRisk R5 architecture federation projection extension
-- Issues #92 #94 | additive to Paper-1 relational twin
-- Core ontology remains semantic authority; these are qualified application/profile structures.

BEGIN;

CREATE TABLE IF NOT EXISTS ref.external_entity_mapping (
  external_mapping_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  source_external_entity_id uuid NOT NULL REFERENCES ref.external_entity(external_entity_id) ON DELETE CASCADE,
  target_external_entity_id uuid NOT NULL REFERENCES ref.external_entity(external_entity_id) ON DELETE CASCADE,
  mapping_relation text NOT NULL CHECK (mapping_relation IN (
    'exactMatch','closeMatch','relatedMatch','broadMatch','narrowMatch'
  )),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  mapping_note text,
  CONSTRAINT ck_external_mapping_not_self
    CHECK (source_external_entity_id <> target_external_entity_id),
  UNIQUE(source_external_entity_id,target_external_entity_id,mapping_relation)
);

CREATE TABLE IF NOT EXISTS enterprise.architecture_context_link (
  architecture_context_link_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  relation_semantic_id text NOT NULL DEFAULT 'SR-REL-010'
    CHECK (relation_semantic_id='SR-REL-010'),
  source_instance_id uuid NOT NULL REFERENCES meta.semantic_instance(instance_id) ON DELETE CASCADE,
  external_entity_id uuid NOT NULL REFERENCES ref.external_entity(external_entity_id) ON DELETE CASCADE,
  target_family text NOT NULL CHECK (target_family IN (
    'objective','capability','business_process','other_external'
  )),
  effect_mode text NOT NULL CHECK (effect_mode IN (
    'anticipated','realized','contextual','unknown'
  )),
  source_artifact_id uuid REFERENCES meta.source_artifact(source_artifact_id),
  confidence_code text,
  qualification_note text
);

CREATE INDEX IF NOT EXISTS ix_external_entity_mapping_source
  ON ref.external_entity_mapping(source_external_entity_id,mapping_relation);
CREATE INDEX IF NOT EXISTS ix_external_entity_mapping_target
  ON ref.external_entity_mapping(target_external_entity_id,mapping_relation);
CREATE INDEX IF NOT EXISTS ix_architecture_context_source
  ON enterprise.architecture_context_link(source_instance_id,target_family,effect_mode);
CREATE INDEX IF NOT EXISTS ix_architecture_context_external
  ON enterprise.architecture_context_link(external_entity_id);

COMMIT;
