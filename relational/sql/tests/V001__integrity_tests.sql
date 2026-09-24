-- SemRisk #46 integrity tests.
-- Run after V001__paper1_projection.sql and V001__views.sql.
-- This script must terminate successfully; expected failures are isolated in PL/pgSQL blocks.

DO $$
DECLARE src uuid; i1 uuid; i2 uuid;
BEGIN
  SELECT source_artifact_id INTO src FROM meta.source_artifact
    WHERE source_artifact_id='00000000-0000-0000-0000-000000000001';

  -- RC-014 synthetic data cannot claim independent validation.
  BEGIN
    INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
    VALUES ('urn:semrisk:test:invalid-synthetic','SR-CPT-001',src,'independent_validation',true);
    RAISE EXCEPTION 'TEST FAILED: synthetic independent_validation insert unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- Create two generic helper instances for relation/state tests.
  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role)
  VALUES ('urn:semrisk:test:i1','SR-CPT-020',src,'synthetic_test') RETURNING instance_id INTO i1;
  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role)
  VALUES ('urn:semrisk:test:i2','SR-CPT-020',src,'synthetic_test') RETURNING instance_id INTO i2;

  -- RC-004 semantic relation whitelist.
  BEGIN
    INSERT INTO core.semantic_relation_assertion(relation_semantic_id,subject_instance_id,object_instance_id,source_artifact_id)
    VALUES ('SR-REL-999',i1,i2,src);
    RAISE EXCEPTION 'TEST FAILED: non-whitelisted semantic relation unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- RC-020 state family whitelist.
  BEGIN
    INSERT INTO meta.state_transition(state_family,prior_instance_id,next_instance_id)
    VALUES ('mixed_state',i1,i2);
    RAISE EXCEPTION 'TEST FAILED: invalid state family unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  DELETE FROM meta.semantic_instance WHERE instance_id IN (i1,i2);
END $$;

DO $$
DECLARE
 src uuid; risk_i uuid; reg_i uuid; entry_i uuid; actor uuid;
 resp_i uuid; wf1 uuid; wf2 uuid; plan_i uuid;
BEGIN
  SELECT source_artifact_id INTO src FROM meta.source_artifact
  WHERE source_artifact_id='00000000-0000-0000-0000-000000000001';

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:risk','SR-CPT-001',src,'synthetic_test',true) RETURNING instance_id INTO risk_i;
  INSERT INTO core.risk(risk_id,title) VALUES(risk_i,'test risk');

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:register','SR-CPT-032',src,'synthetic_test',true) RETURNING instance_id INTO reg_i;
  INSERT INTO enterprise.risk_register(register_id,name) VALUES(reg_i,'test register');

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:entry','SR-CPT-033',src,'synthetic_test',true) RETURNING instance_id INTO entry_i;
  INSERT INTO enterprise.risk_register_entry(entry_id,register_id,risk_id,title)
  VALUES(entry_i,reg_i,risk_i,'test entry');

  INSERT INTO enterprise.actor_ref(label,actor_kind) VALUES('test actor','synthetic') RETURNING actor_id INTO actor;

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:responsibility','SR-CPT-031',src,'synthetic_test',true) RETURNING instance_id INTO resp_i;

  -- RC-009 exactly one responsibility target.
  BEGIN
    INSERT INTO enterprise.risk_responsibility(responsibility_id,actor_id,risk_id,entry_id)
    VALUES(resp_i,actor,risk_i,entry_i);
    RAISE EXCEPTION 'TEST FAILED: multi-target responsibility unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  INSERT INTO enterprise.risk_responsibility(responsibility_id,actor_id,risk_id)
  VALUES(resp_i,actor,risk_i);

  IF NOT EXISTS (SELECT 1 FROM enterprise.v_risk_owner WHERE risk_id=risk_i AND actor_id=actor) THEN
    RAISE EXCEPTION 'TEST FAILED: derived risk-owner view did not resolve responsibility';
  END IF;

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:wf1','SR-CPT-036',src,'synthetic_test',true) RETURNING instance_id INTO wf1;
  INSERT INTO enterprise.workflow_state_history(workflow_state_id,entry_id,state_code,is_current)
  VALUES(wf1,entry_i,'open',true);

  INSERT INTO meta.semantic_instance(instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES ('urn:semrisk:test:wf2','SR-CPT-036',src,'synthetic_test',true) RETURNING instance_id INTO wf2;

  -- RC-007 unique current workflow state.
  BEGIN
    INSERT INTO enterprise.workflow_state_history(workflow_state_id,entry_id,state_code,is_current)
    VALUES(wf2,entry_i,'closed',true);
    RAISE EXCEPTION 'TEST FAILED: duplicate current workflow state unexpectedly succeeded';
  EXCEPTION WHEN unique_violation THEN NULL;
  END;

  -- Verify no primitive owner_id was added to core.risk.
  IF EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_schema='core' AND table_name='risk' AND column_name='owner_id'
  ) THEN
    RAISE EXCEPTION 'TEST FAILED: primitive owner_id exists on core.risk';
  END IF;

  -- Cleanup cascades through semantic subtype tables.
  DELETE FROM meta.semantic_instance WHERE instance_id IN (wf2,wf1,resp_i,entry_i,reg_i,risk_i);
  DELETE FROM enterprise.actor_ref WHERE actor_id=actor;
END $$;

SELECT 'SEM_RISK_ISSUE_46_INTEGRITY_TESTS_PASS' AS test_result;
