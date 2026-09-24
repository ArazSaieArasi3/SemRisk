-- SemRisk #48 end-to-end scenario acceptance tests

DO $semrisk$
DECLARE
  risk_id uuid := '47000000-0000-0000-0001-000000000001';
  scenario_id uuid := '47000000-0000-0000-0001-000000000004';
  event_id uuid := '48000000-0000-0000-0001-000000000002';
  owner_count int;
  risk_state_count int;
  workflow_state_count int;
BEGIN
  -- Q01 scenario/event distinction.
  IF scenario_id = event_id THEN RAISE EXCEPTION 'Scenario and event identity conflated'; END IF;
  IF NOT EXISTS (SELECT 1 FROM core.risk_event WHERE event_id=event_id AND realizes_scenario_id=scenario_id)
    THEN RAISE EXCEPTION 'Scenario realization path missing'; END IF;

  -- Q02 trigger/event/consequence executable chain.
  IF NOT EXISTS (
    SELECT 1 FROM core.risk_event e
    JOIN core.event_trigger et ON et.event_id=e.event_id
    JOIN core.event_consequence ec ON ec.event_id=e.event_id
    WHERE e.event_id=event_id
  ) THEN RAISE EXCEPTION 'Trigger-event-consequence chain missing'; END IF;

  -- Q03/Q07 reassessment lineage and same Risk identity.
  IF NOT EXISTS (
    SELECT 1
    FROM assessment.assessment_activity post
    JOIN assessment.assessment_result residual ON residual.assessment_id=post.assessment_id
    JOIN assessment.assessment_result inherent ON inherent.result_id=residual.supersedes_result_id
    WHERE post.assessment_id='48000000-0000-0000-0001-000000000013'
      AND post.prior_assessment_id='48000000-0000-0000-0001-000000000011'
      AND residual.result_kind='residual'
      AND inherent.result_kind='inherent'
      AND residual.risk_id=risk_id AND inherent.risk_id=risk_id
  ) THEN RAISE EXCEPTION 'Reassessment/supersession/same-risk path missing'; END IF;

  -- Q04 strategy/plan/activity/control are four distinct nodes.
  IF NOT EXISTS (
    SELECT 1 FROM treatment.plan p
    JOIN treatment.activity a ON a.plan_id=p.plan_id
    JOIN treatment.activity_control ac ON ac.activity_id=a.activity_id
    JOIN treatment.control_mechanism c ON c.control_id=ac.control_id
    WHERE p.plan_id='48000000-0000-0000-0001-000000000008'
      AND p.strategy_id='47000000-0000-0000-0001-000000000005'
      AND a.activity_id <> p.plan_id
      AND c.control_id <> a.activity_id
  ) THEN RAISE EXCEPTION 'Treatment distinction chain missing'; END IF;

  -- Q05 derived owner through responsibility.
  SELECT count(*) INTO owner_count FROM enterprise.v_risk_owner WHERE risk_id=risk_id;
  IF owner_count <> 1 THEN RAISE EXCEPTION 'Expected exactly one derived synthetic owner, got %',owner_count; END IF;
  IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='core' AND table_name='risk' AND column_name='owner_id')
    THEN RAISE EXCEPTION 'Primitive owner_id found'; END IF;

  -- Q06 separate state families.
  SELECT count(*) INTO risk_state_count FROM enterprise.risk_state_history
    WHERE risk_id=risk_id AND risk_state_id IN ('48000000-0000-0000-0001-000000000015','48000000-0000-0000-0001-000000000016');
  SELECT count(*) INTO workflow_state_count FROM enterprise.workflow_state_history
    WHERE entry_id='48000000-0000-0000-0001-000000000005';
  IF risk_state_count <> 2 OR workflow_state_count <> 2 THEN
    RAISE EXCEPTION 'Expected two risk states and two workflow states; got % / %',risk_state_count,workflow_state_count;
  END IF;
  IF EXISTS (
    SELECT 1 FROM meta.state_transition
    WHERE transition_id IN ('48000000-0000-0000-0003-000000000001','48000000-0000-0000-0003-000000000002')
    GROUP BY transition_id
    HAVING min(state_family) NOT IN ('risk_state','workflow_state')
  ) THEN RAISE EXCEPTION 'Invalid state family transition'; END IF;

  -- Q08 explicit evidence roles; no synthetic leakage.
  IF EXISTS (
    SELECT 1 FROM meta.semantic_instance
    WHERE instance_iri LIKE 'urn:semrisk:scenario:p1:e2e:%'
      AND (synthetic_flag=false OR evidence_role<>'synthetic_test')
  ) THEN RAISE EXCEPTION 'Scenario synthetic provenance leakage'; END IF;

  -- Q09 CM-PharmE external ownership remains.
  IF NOT EXISTS (
    SELECT 1 FROM pharma.context_link pc
    JOIN ref.external_entity ee ON ee.external_entity_id=pc.external_entity_id
    WHERE (pc.risk_id=risk_id OR pc.scenario_id=scenario_id)
      AND ee.owner_namespace='CM-PharmE' AND ee.version_ref='v1.0.0'
  ) THEN RAISE EXCEPTION 'CM-PharmE bridge missing'; END IF;
END $semrisk$;

-- Negative/edge: workflow state is not stored as risk state.
DO $semrisk$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM enterprise.workflow_state_history w
    JOIN enterprise.risk_state_history r ON r.risk_state_id=w.workflow_state_id
    WHERE w.entry_id='48000000-0000-0000-0001-000000000005'
  ) THEN RAISE EXCEPTION 'Workflow/Risk State identity conflation detected'; END IF;
END $semrisk$;

SELECT
  'SEM_RISK_ISSUE_48_E2E_SCENARIO_PASS' AS test_result,
  (SELECT count(*) FROM core.risk_event WHERE realizes_scenario_id='47000000-0000-0000-0001-000000000004') AS realized_events,
  (SELECT count(*) FROM assessment.assessment_result WHERE risk_id='47000000-0000-0000-0001-000000000001' AND result_kind IN ('inherent','residual')) AS temporal_results,
  (SELECT count(*) FROM enterprise.v_risk_owner WHERE risk_id='47000000-0000-0000-0001-000000000001') AS derived_owners;
