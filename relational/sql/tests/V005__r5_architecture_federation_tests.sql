-- R5 architecture federation regression | Issues #92 #94 #95
BEGIN;

DO $semrisk$
DECLARE
  src uuid;
  risk_i uuid;
  ext1_i uuid; ext2_i uuid;
  ext1 uuid; ext2 uuid;
  same_label_count int;
  link_count int;
BEGIN
  SELECT source_artifact_id INTO src
  FROM meta.source_artifact
  WHERE source_artifact_id='00000000-0000-0000-0000-000000000001';

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:r5:risk','SR-CPT-001',src,'synthetic_test',true)
  RETURNING instance_id INTO risk_i;
  INSERT INTO core.risk(risk_id,title) VALUES(risk_i,'R5 architecture federation risk');

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:r5:ea-a','EXT-EA',src,'synthetic_test',true)
  RETURNING instance_id INTO ext1_i;
  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:r5:ea-b','EXT-EA',src,'synthetic_test',true)
  RETURNING instance_id INTO ext2_i;

  INSERT INTO ref.external_entity(instance_id,owner_namespace,owner_semantic_id,version_ref,label)
  VALUES(ext1_i,'EA-A','CAP-001','v1','Shared Capability Label')
  RETURNING external_entity_id INTO ext1;

  INSERT INTO ref.external_entity(instance_id,owner_namespace,owner_semantic_id,version_ref,label)
  VALUES(ext2_i,'EA-B','CAP-900','2026','Shared Capability Label')
  RETURNING external_entity_id INTO ext2;

  SELECT count(*) INTO same_label_count
  FROM ref.external_entity
  WHERE label='Shared Capability Label'
    AND external_entity_id IN (ext1,ext2);
  IF same_label_count <> 2 THEN
    RAISE EXCEPTION 'R5 collision regression: same-label external entities were not preserved separately';
  END IF;

  INSERT INTO ref.external_entity_mapping(
    source_external_entity_id,target_external_entity_id,mapping_relation,source_artifact_id,mapping_note
  ) VALUES(ext1,ext2,'closeMatch',src,'Explicit correspondence; not identity merge');

  INSERT INTO enterprise.architecture_context_link(
    source_instance_id,external_entity_id,target_family,effect_mode,source_artifact_id,qualification_note
  ) VALUES
    (risk_i,ext1,'capability','anticipated',src,'Potential future impact'),
    (risk_i,ext1,'capability','realized',src,'Observed/realized impact assertion fixture');

  SELECT count(*) INTO link_count
  FROM enterprise.architecture_context_link
  WHERE source_instance_id=risk_i AND external_entity_id=ext1;
  IF link_count <> 2 THEN
    RAISE EXCEPTION 'R5 qualification regression: expected anticipated and realized links to coexist, got %', link_count;
  END IF;

  IF EXISTS (
    SELECT 1
    FROM ref.external_entity_mapping m
    JOIN ref.external_entity s ON s.external_entity_id=m.source_external_entity_id
    JOIN ref.external_entity t ON t.external_entity_id=m.target_external_entity_id
    WHERE s.label=t.label
      AND s.owner_namespace<>t.owner_namespace
      AND m.mapping_relation='exactMatch'
  ) THEN
    RAISE EXCEPTION 'R5 collision regression: same label across owners was promoted to exactMatch';
  END IF;
END $semrisk$;

SELECT 'SEM_RISK_R5_MULTI_ONTOLOGY_IDENTITY_PASS' AS test_result,
       count(*) AS qualified_link_count
FROM enterprise.architecture_context_link
WHERE qualification_note IN ('Potential future impact','Observed/realized impact assertion fixture');

ROLLBACK;
