-- R7 Pharma case governance regression | Issues #103 #106 #107
BEGIN;

DO $semrisk$
DECLARE
  batch_code_v text;
  candidate_type text;
  candidate_iri text;
  pci005_disposition text;
  pci005_rule text;
  ds4_disposition text;
  ds2_disposition text;
BEGIN
  SELECT batch_code INTO batch_code_v
  FROM staging.load_batch
  WHERE load_batch_id='47000000-0000-0000-0000-000000000001';

  IF batch_code_v <> 'P1-DATA-0.1.0-rc.2' THEN
    RAISE EXCEPTION 'R7 FAILED: expected rc.2 governed snapshot, got %', batch_code_v;
  END IF;

  -- Pooled procurement remains the one source-grounded proposed strategy.
  IF NOT EXISTS (
    SELECT 1 FROM treatment.strategy
    WHERE strategy_id='47000000-0000-0000-0001-000000000005'
      AND title='Pooled procurement'
  ) THEN
    RAISE EXCEPTION 'R7 FAILED: pooled procurement proposed strategy missing';
  END IF;

  -- Transparency is no longer forced into treatment.strategy.
  IF EXISTS (
    SELECT 1 FROM treatment.strategy
    WHERE strategy_id='47000000-0000-0000-0001-000000000006'
  ) THEN
    RAISE EXCEPTION 'R7 FAILED: transparency response remains overtyped as Risk Treatment Strategy';
  END IF;

  SELECT semantic_type_id,instance_iri
    INTO candidate_type,candidate_iri
  FROM meta.semantic_instance
  WHERE instance_id='47000000-0000-0000-0001-000000000006';

  IF candidate_type <> 'PROFILE-PHARMA-RESPONSE-CANDIDATE'
     OR candidate_iri <> 'urn:semrisk:case:pharma:v1:transparency-response-candidate' THEN
    RAISE EXCEPTION 'R7 FAILED: transparency response candidate identity/type mismatch: % / %',
      candidate_type,candidate_iri;
  END IF;

  SELECT disposition,transform_rule_id
    INTO pci005_disposition,pci005_rule
  FROM staging.source_record
  WHERE source_record_key='PCI-005';

  IF pci005_disposition <> 'partial'
     OR pci005_rule NOT LIKE '%PROFILE-PHARMA-RESPONSE-CANDIDATE%' THEN
    RAISE EXCEPTION 'R7 FAILED: PCI-005 contextual typing is not preserved: % / %',
      pci005_disposition,pci005_rule;
  END IF;

  SELECT disposition INTO ds4_disposition
  FROM staging.source_record
  WHERE source_record_key='DS-004-FILE-LEVEL';
  IF ds4_disposition <> 'blocked' THEN
    RAISE EXCEPTION 'R7 FAILED: DS-004 file-level gate unexpectedly opened';
  END IF;

  SELECT disposition INTO ds2_disposition
  FROM staging.source_record
  WHERE source_record_key='DS-002-RECORD-LEVEL';
  IF ds2_disposition <> 'protected' THEN
    RAISE EXCEPTION 'R7 FAILED: DS-002 protected record-level state changed';
  END IF;

  IF EXISTS (
    SELECT 1 FROM meta.semantic_instance
    WHERE source_artifact_id='47000000-0000-0000-0000-000000000102'
  ) THEN
    RAISE EXCEPTION 'R7 FAILED: protected DS-002 record-level evidence leaked into projection';
  END IF;
END
$semrisk$;

SELECT 'SEM_RISK_R7_PHARMA_CASE_GOVERNANCE_PASS' AS test_result;

ROLLBACK;
