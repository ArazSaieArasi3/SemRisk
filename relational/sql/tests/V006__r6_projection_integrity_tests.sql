-- R6 projection-integrity regression tests | Issues #97 #98 #99 #101
BEGIN;

DO $semrisk$
DECLARE
  src uuid := '00000000-0000-0000-0000-000000000001';
  risk2 uuid := '4a000000-0000-0000-0000-000000000001';
  a_old uuid := '4a000000-0000-0000-0000-0000000000ff';
  a_new uuid := '4a000000-0000-0000-0000-000000000002';
  r_old uuid := '4b000000-0000-0000-0000-0000000000ff';
  r_new uuid := '4b000000-0000-0000-0000-000000000002';
  latest uuid;
BEGIN
  -- #97 duplicate stable actor IRI must fail.
  BEGIN
    INSERT INTO enterprise.actor_ref(actor_iri,actor_kind,label)
    VALUES('urn:semrisk:scenario:p1:e2e:actor','synthetic','duplicate actor IRI');
    RAISE EXCEPTION 'R6 FAILED: duplicate actor_iri unexpectedly succeeded';
  EXCEPTION WHEN unique_violation THEN NULL;
  END;

  -- Create a second Risk with deliberately non-time-ordered UUIDs.
  INSERT INTO meta.semantic_instance(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
  VALUES
    (risk2,'urn:semrisk:test:r6:risk2','SR-CPT-001',src,'synthetic_test',true),
    (a_old,'urn:semrisk:test:r6:assessment-old','SR-CPT-011',src,'synthetic_test',true),
    (a_new,'urn:semrisk:test:r6:assessment-new','SR-CPT-011',src,'synthetic_test',true),
    (r_old,'urn:semrisk:test:r6:result-old','SR-CPT-013',src,'synthetic_test',true),
    (r_new,'urn:semrisk:test:r6:result-new','SR-CPT-013',src,'synthetic_test',true);

  INSERT INTO core.risk(risk_id,title) VALUES(risk2,'R6 temporal lineage test risk');

  INSERT INTO assessment.assessment_activity(assessment_id,risk_id,started_at,ended_at)
  VALUES
    (a_old,risk2,'2026-01-01T10:00:00Z','2026-01-01T11:00:00Z'),
    (a_new,risk2,'2026-02-01T10:00:00Z','2026-02-01T11:00:00Z');

  INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,value_text)
  VALUES
    (r_old,a_old,risk2,'generic','older result with lexicographically larger UUID'),
    (r_new,a_new,risk2,'generic','newer result with lexicographically smaller UUID');

  SELECT result_id INTO latest
  FROM assessment.v_latest_result_by_kind
  WHERE risk_id=risk2 AND result_kind='generic';

  IF latest <> r_new THEN
    RAISE EXCEPTION 'R6 FAILED: latest-result view is not temporal; got %, expected %', latest, r_new;
  END IF;

  -- #99 cross-risk prior assessment must fail.
  BEGIN
    UPDATE assessment.assessment_activity
    SET prior_assessment_id=a_new
    WHERE assessment_id='48000000-0000-0000-0001-000000000013';
    RAISE EXCEPTION 'R6 FAILED: cross-risk prior assessment unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #99 two-node assessment cycle must fail.
  BEGIN
    UPDATE assessment.assessment_activity
    SET prior_assessment_id='48000000-0000-0000-0001-000000000013'
    WHERE assessment_id='48000000-0000-0000-0001-000000000011';
    RAISE EXCEPTION 'R6 FAILED: assessment lineage cycle unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #99 cross-risk result supersession must fail.
  BEGIN
    UPDATE assessment.assessment_result
    SET supersedes_result_id=r_new
    WHERE result_id='48000000-0000-0000-0001-000000000014';
    RAISE EXCEPTION 'R6 FAILED: cross-risk result supersession unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #99 two-node result supersession cycle must fail.
  BEGIN
    UPDATE assessment.assessment_result
    SET supersedes_result_id='48000000-0000-0000-0001-000000000014'
    WHERE result_id='48000000-0000-0000-0001-000000000012';
    RAISE EXCEPTION 'R6 FAILED: result supersession cycle unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #98 cross-Risk state transition must fail.
  BEGIN
    INSERT INTO meta.state_transition(transition_id,state_family,prior_instance_id,next_instance_id)
    VALUES('4c000000-0000-0000-0000-000000000001','risk_state',
      '48000000-0000-0000-0001-000000000015',
      '47000000-0000-0000-0001-000000000010');
    RAISE EXCEPTION 'R6 FAILED: cross-Risk state transition unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #98 wrong endpoint family must fail.
  BEGIN
    INSERT INTO meta.state_transition(transition_id,state_family,prior_instance_id,next_instance_id)
    VALUES('4c000000-0000-0000-0000-000000000002','risk_state',
      '48000000-0000-0000-0001-000000000017',
      '48000000-0000-0000-0001-000000000018');
    RAISE EXCEPTION 'R6 FAILED: workflow endpoints accepted as risk_state transition';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #98 cross-Entry workflow transition must fail.
  BEGIN
    INSERT INTO meta.state_transition(transition_id,state_family,prior_instance_id,next_instance_id)
    VALUES('4c000000-0000-0000-0000-000000000003','workflow_state',
      '48000000-0000-0000-0001-000000000017',
      '47000000-0000-0000-0010-000000000004');
    RAISE EXCEPTION 'R6 FAILED: cross-Entry workflow transition unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;

  -- #98 known temporal reversal must fail.
  BEGIN
    INSERT INTO meta.state_transition(transition_id,state_family,prior_instance_id,next_instance_id)
    VALUES('4c000000-0000-0000-0000-000000000004','risk_state',
      '48000000-0000-0000-0001-000000000016',
      '48000000-0000-0000-0001-000000000015');
    RAISE EXCEPTION 'R6 FAILED: temporally reversed transition unexpectedly succeeded';
  EXCEPTION WHEN check_violation THEN NULL;
  END;
END
$semrisk$;

-- #101 Frozen snapshot lineage must reconcile.
DO $semrisk$
DECLARE
  bad int;
BEGIN
  SELECT count(*) INTO bad
  FROM staging.v_lineage_reconciliation
  WHERE lineage_status <> 'OK';

  IF bad <> 0 THEN
    RAISE EXCEPTION 'R6 FAILED: governed snapshot contains % unresolved lineage rows', bad;
  END IF;

  -- Protected holdout must not materialize record-level semantic instances.
  IF EXISTS (
    SELECT 1
    FROM meta.semantic_instance si
    WHERE si.source_artifact_id='47000000-0000-0000-0000-000000000102'
  ) THEN
    RAISE EXCEPTION 'R6 FAILED: protected DS-002 holdout leaked into semantic instances';
  END IF;

  IF EXISTS (
    SELECT 1 FROM meta.semantic_instance
    WHERE synthetic_flag=true AND evidence_role='independent_validation'
  ) THEN
    RAISE EXCEPTION 'R6 FAILED: synthetic evidence carries independent_validation role';
  END IF;
END
$semrisk$;

-- Inject unresolved lineage and prove the reconciliation detector catches it.
INSERT INTO staging.source_record(
  source_record_id,load_batch_id,source_artifact_id,source_record_key,source_locator,
  raw_semantic_summary,transform_rule_id,target_instance_iri,disposition
) VALUES(
  '4d000000-0000-0000-0000-000000000001',
  '47000000-0000-0000-0000-000000000001',
  '47000000-0000-0000-0000-000000000103',
  'R6-NEG-UNRESOLVED','synthetic negative fixture',
  'Deliberately unresolved target for detector test','R6-NEG',
  'urn:semrisk:test:r6:missing-target','loaded'
);

DO $semrisk$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM staging.v_lineage_reconciliation
    WHERE source_record_id='4d000000-0000-0000-0000-000000000001'
      AND lineage_status='UNRESOLVED_TARGET'
  ) THEN
    RAISE EXCEPTION 'R6 FAILED: unresolved target lineage mutation was not detected';
  END IF;
END
$semrisk$;

SELECT 'SEM_RISK_R6_PROJECTION_INTEGRITY_PASS' AS test_result;

ROLLBACK;
