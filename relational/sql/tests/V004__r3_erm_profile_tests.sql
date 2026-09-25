-- R3 ERM/GRC profile regression tests | Issues #80 #83
BEGIN;

-- Demonstrate that Paper-1 does not impose unique ownership.
INSERT INTO meta.semantic_instance(
  instance_id,instance_iri,semantic_type_id,evidence_role,synthetic_flag
) VALUES (
  '49000000-0000-0000-0001-000000000001',
  'urn:semrisk:test:r3:responsibility-coowner',
  'SR-CPT-031','synthetic_test',true
);

INSERT INTO enterprise.actor_ref(actor_id,actor_kind,label)
VALUES (
  '49000000-0000-0000-0001-000000000002',
  'synthetic_external_actor',
  'R3 synthetic co-owner'
);

INSERT INTO enterprise.risk_responsibility(
  responsibility_id,actor_id,risk_id,valid_from,valid_to
) VALUES (
  '49000000-0000-0000-0001-000000000001',
  '49000000-0000-0000-0001-000000000002',
  '47000000-0000-0000-0001-000000000001',
  transaction_timestamp() - interval '1 minute',
  NULL
);

DO $semrisk$
DECLARE
  owner_count int;
BEGIN
  SELECT count(*) INTO owner_count
  FROM enterprise.v_risk_owner
  WHERE risk_id='47000000-0000-0000-0001-000000000001';

  IF owner_count <> 2 THEN
    RAISE EXCEPTION 'R3 co-ownership regression: expected 2 concurrent derived owners, got %', owner_count;
  END IF;

  IF EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_schema='core' AND table_name='risk' AND column_name='owner_id'
  ) THEN
    RAISE EXCEPTION 'R3 regression: primitive owner_id found on core.risk';
  END IF;
END $semrisk$;

SELECT 'SEM_RISK_R3_COOWNERSHIP_PASS' AS test_result,
       count(*) AS current_owners
FROM enterprise.v_risk_owner
WHERE risk_id='47000000-0000-0000-0001-000000000001';

ROLLBACK;
