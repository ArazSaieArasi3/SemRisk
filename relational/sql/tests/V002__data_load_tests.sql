-- Issue #47 governed data-load reconciliation checks
DO $semrisk$
DECLARE
  batch_status text;
  ds3_loaded int;
  blocked_count int;
  protected_count int;
  synthetic_count int;
  constructed_count int;
BEGIN
  SELECT status INTO batch_status FROM staging.load_batch
  WHERE load_batch_id='47000000-0000-0000-0000-000000000001';
  IF batch_status <> 'completed' THEN
    RAISE EXCEPTION 'Load batch not completed: %', batch_status;
  END IF;

  SELECT count(*) INTO ds3_loaded FROM staging.source_record
  WHERE source_artifact_id='47000000-0000-0000-0000-000000000103'
    AND source_record_key LIKE 'PCI-%';
  IF ds3_loaded <> 5 THEN
    RAISE EXCEPTION 'Expected 5 governed DS-003 constructed input rows, found %', ds3_loaded;
  END IF;

  SELECT count(*) INTO blocked_count FROM staging.source_record WHERE disposition='blocked';
  IF blocked_count < 1 THEN RAISE EXCEPTION 'Expected explicit blocked source record'; END IF;

  SELECT count(*) INTO protected_count FROM staging.source_record WHERE disposition='protected';
  IF protected_count < 1 THEN RAISE EXCEPTION 'Expected explicit protected holdout record'; END IF;

  SELECT count(*) INTO synthetic_count FROM meta.semantic_instance
  WHERE evidence_role='synthetic_test' AND synthetic_flag=true;
  IF synthetic_count < 5 THEN RAISE EXCEPTION 'Synthetic fixture count too low: %', synthetic_count; END IF;

  SELECT count(*) INTO constructed_count FROM meta.semantic_instance
  WHERE evidence_role='constructed_case' AND synthetic_flag=true;
  IF constructed_count < 10 THEN RAISE EXCEPTION 'Constructed Pharma case count too low: %', constructed_count; END IF;

  IF EXISTS (
    SELECT 1 FROM meta.semantic_instance
    WHERE synthetic_flag=true AND evidence_role='independent_validation'
  ) THEN RAISE EXCEPTION 'Synthetic/constructed evidence-role leakage detected'; END IF;

  IF EXISTS (
    SELECT 1 FROM meta.source_artifact
    WHERE source_artifact_id='47000000-0000-0000-0000-000000000102'
      AND evidence_role <> 'transferability_holdout'
  ) THEN RAISE EXCEPTION 'DS-002 holdout role changed'; END IF;

  IF NOT EXISTS (
    SELECT 1 FROM enterprise.v_risk_owner
    WHERE risk_id='47000000-0000-0000-0010-000000000001'
  ) THEN RAISE EXCEPTION 'Synthetic operational responsibility did not derive Risk Owner'; END IF;
END $semrisk$;

SELECT
  (SELECT count(*) FROM staging.source_record) AS governed_source_records,
  (SELECT count(*) FROM meta.semantic_instance WHERE evidence_role='constructed_case') AS constructed_instances,
  (SELECT count(*) FROM meta.semantic_instance WHERE evidence_role='synthetic_test') AS synthetic_instances,
  (SELECT count(*) FROM staging.reject_record) AS rejected_records,
  'SEM_RISK_ISSUE_47_LOAD_TESTS_PASS' AS test_result;
