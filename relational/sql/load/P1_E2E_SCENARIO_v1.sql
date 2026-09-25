-- SemRisk #48 executable end-to-end scenario extension
-- Builds on P1-DATA-0.1.0-rc.1 from #47.
BEGIN;

-- Synthetic semantic instances for the executable path.
INSERT INTO meta.semantic_instance
(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
VALUES
('48000000-0000-0000-0001-000000000001','urn:semrisk:scenario:p1:e2e:trigger','SR-CPT-005','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000002','urn:semrisk:scenario:p1:e2e:event','SR-CPT-007','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000003','urn:semrisk:scenario:p1:e2e:consequence','SR-CPT-008','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000004','urn:semrisk:scenario:p1:e2e:register','SR-CPT-032','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000005','urn:semrisk:scenario:p1:e2e:entry','SR-CPT-033','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000006','urn:semrisk:scenario:p1:e2e:description','SR-CPT-034','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000007','urn:semrisk:scenario:p1:e2e:responsibility','SR-CPT-031','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000008','urn:semrisk:scenario:p1:e2e:plan','SR-CPT-027','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000009','urn:semrisk:scenario:p1:e2e:treatment-activity','SR-CPT-028','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000010','urn:semrisk:scenario:p1:e2e:control','SR-CPT-029','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000011','urn:semrisk:scenario:p1:e2e:assessment-pre','SR-CPT-011','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000012','urn:semrisk:scenario:p1:e2e:result-inherent','SR-CPT-017','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000013','urn:semrisk:scenario:p1:e2e:assessment-post','SR-CPT-011','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000014','urn:semrisk:scenario:p1:e2e:result-residual','SR-CPT-018','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000015','urn:semrisk:scenario:p1:e2e:risk-state-pre','SR-CPT-035','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000016','urn:semrisk:scenario:p1:e2e:risk-state-post','SR-CPT-035','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000017','urn:semrisk:scenario:p1:e2e:workflow-open','SR-CPT-036','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('48000000-0000-0000-0001-000000000018','urn:semrisk:scenario:p1:e2e:workflow-treated','SR-CPT-036','47000000-0000-0000-0000-000000000199','synthetic_test',true)
ON CONFLICT (instance_id) DO NOTHING;

INSERT INTO core.trigger_event(trigger_id,occurred_at,description)
VALUES('48000000-0000-0000-0001-000000000001','2026-01-15T09:00:00Z','Synthetic supply-disruption trigger for model execution only.')
ON CONFLICT DO NOTHING;

INSERT INTO core.risk_event(event_id,realizes_scenario_id,occurred_at,description)
VALUES('48000000-0000-0000-0001-000000000002','47000000-0000-0000-0001-000000000004','2026-01-15T10:00:00Z','Synthetic realized disruption event; not DS-003 empirical occurrence.')
ON CONFLICT DO NOTHING;

INSERT INTO core.event_trigger(event_id,trigger_id)
VALUES('48000000-0000-0000-0001-000000000002','48000000-0000-0000-0001-000000000001')
ON CONFLICT DO NOTHING;

INSERT INTO core.consequence(consequence_id,description,valid_from)
VALUES('48000000-0000-0000-0001-000000000003','Synthetic operational consequence used to exercise consequence/impact separation.','2026-01-15T10:00:00Z')
ON CONFLICT DO NOTHING;

INSERT INTO core.event_consequence(event_id,consequence_id)
VALUES('48000000-0000-0000-0001-000000000002','48000000-0000-0000-0001-000000000003')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_register(register_id,name,version_label)
VALUES('48000000-0000-0000-0001-000000000004','Paper-1 executable Pharma scenario register','E2E-v1.0')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_register_entry(entry_id,register_id,risk_id,title,description)
VALUES('48000000-0000-0000-0001-000000000005','48000000-0000-0000-0001-000000000004',
'47000000-0000-0000-0001-000000000001','Antibiotic supply disruption management',
'Synthetic management record concerning the bounded constructed Risk.')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.scenario_description(description_id,scenario_id,entry_id,text_value)
VALUES('48000000-0000-0000-0001-000000000006','47000000-0000-0000-0001-000000000004',
'48000000-0000-0000-0001-000000000005',
'Information artifact describing the bounded supply-disruption scenario; not the scenario or event itself.')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.actor_ref(actor_id,actor_iri,actor_kind,label)
VALUES('48000000-0000-0000-0002-000000000001','urn:semrisk:scenario:p1:e2e:actor','synthetic_external_actor','Synthetic Supply Risk Manager')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_responsibility(responsibility_id,actor_id,risk_id,valid_from)
VALUES('48000000-0000-0000-0001-000000000007','48000000-0000-0000-0002-000000000001',
'47000000-0000-0000-0001-000000000001','2026-01-15T08:00:00Z')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.plan(plan_id,strategy_id,title,status_code)
VALUES('48000000-0000-0000-0001-000000000008','47000000-0000-0000-0001-000000000005',
'Synthetic pooled-procurement execution plan','executed_fixture')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.activity(activity_id,plan_id,started_at,ended_at)
VALUES('48000000-0000-0000-0001-000000000009','48000000-0000-0000-0001-000000000008',
'2026-01-16T08:00:00Z','2026-01-20T17:00:00Z')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.control_mechanism(control_id,description)
VALUES('48000000-0000-0000-0001-000000000010','Synthetic procurement coordination control used only for application-path testing.')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.activity_control(activity_id,control_id)
VALUES('48000000-0000-0000-0001-000000000009','48000000-0000-0000-0001-000000000010')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.control_protection(control_id,protected_instance_id,source_artifact_id)
VALUES('48000000-0000-0000-0001-000000000010','47000000-0000-0000-0001-000000000001','47000000-0000-0000-0000-000000000199');

INSERT INTO treatment.risk_strategy_selection(risk_id,register_entry_id,strategy_id,selected_at)
VALUES('47000000-0000-0000-0001-000000000001','48000000-0000-0000-0001-000000000005',
'47000000-0000-0000-0001-000000000005','2026-01-15T12:00:00Z');

INSERT INTO assessment.assessment_activity(assessment_id,risk_id,started_at,ended_at)
VALUES('48000000-0000-0000-0001-000000000011','47000000-0000-0000-0001-000000000001',
'2026-01-15T11:00:00Z','2026-01-15T11:30:00Z')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,value_text)
VALUES('48000000-0000-0000-0001-000000000012','48000000-0000-0000-0001-000000000011',
'47000000-0000-0000-0001-000000000001','inherent','Synthetic inherent-context qualitative result; no numeric score.')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_evidence(result_id,evidence_id,support_role)
VALUES('48000000-0000-0000-0001-000000000012','47000000-0000-0000-0001-000000000007','context')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_activity(assessment_id,risk_id,prior_assessment_id,started_at,ended_at)
VALUES('48000000-0000-0000-0001-000000000013','47000000-0000-0000-0001-000000000001',
'48000000-0000-0000-0001-000000000011','2026-01-21T09:00:00Z','2026-01-21T09:30:00Z')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,supersedes_result_id,value_text)
VALUES('48000000-0000-0000-0001-000000000014','48000000-0000-0000-0001-000000000013',
'47000000-0000-0000-0001-000000000001','residual','48000000-0000-0000-0001-000000000012',
'Synthetic residual-context qualitative result; no effectiveness or improvement magnitude asserted.')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_evidence(result_id,evidence_id,support_role)
VALUES('48000000-0000-0000-0001-000000000014','47000000-0000-0000-0001-000000000007','context')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_state_history(risk_state_id,risk_id,state_code,valid_from,valid_to,evidence_result_id)
VALUES
('48000000-0000-0000-0001-000000000015','47000000-0000-0000-0001-000000000001','supply_disruption_context_realized','2026-01-15T11:30:00Z','2026-01-21T09:30:00Z','48000000-0000-0000-0001-000000000012'),
('48000000-0000-0000-0001-000000000016','47000000-0000-0000-0001-000000000001','supply_disruption_context_persists_after_treatment_activity','2026-01-21T09:30:00Z',NULL,'48000000-0000-0000-0001-000000000014')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.workflow_state_history(workflow_state_id,entry_id,state_code,valid_from,valid_to,is_current)
VALUES
('48000000-0000-0000-0001-000000000017','48000000-0000-0000-0001-000000000005','open','2026-01-15T08:00:00Z','2026-01-20T17:00:00Z',false),
('48000000-0000-0000-0001-000000000018','48000000-0000-0000-0001-000000000005','treated','2026-01-20T17:00:00Z',NULL,true)
ON CONFLICT DO NOTHING;

INSERT INTO meta.state_transition(transition_id,state_family,prior_instance_id,next_instance_id,observed_at)
VALUES
('48000000-0000-0000-0003-000000000001','risk_state','48000000-0000-0000-0001-000000000015','48000000-0000-0000-0001-000000000016','2026-01-21T09:30:00Z'),
('48000000-0000-0000-0003-000000000002','workflow_state','48000000-0000-0000-0001-000000000017','48000000-0000-0000-0001-000000000018','2026-01-20T17:00:00Z')
ON CONFLICT DO NOTHING;

-- Deterministic provenance for all synthetic E2E semantic instances.
INSERT INTO meta.instance_provenance(instance_provenance_id,instance_id,source_artifact_id,activity_iri,agent_iri,generated_at,derivation_note)
SELECT
  ('48000000-0000-0000-0004-' || lpad(row_number() OVER (ORDER BY instance_id)::text,12,'0'))::uuid,
  instance_id,
  '47000000-0000-0000-0000-000000000199',
  'urn:semrisk:scenario-generator:E2E-v1.0',
  'urn:semrisk:agent:deterministic-scenario-generator',
  NULL,
  'Synthetic E2E scenario extension; execution/application test only; not empirical domain evidence.'
FROM meta.semantic_instance si
WHERE si.instance_iri LIKE 'urn:semrisk:scenario:p1:e2e:%'
  AND NOT EXISTS (
    SELECT 1 FROM meta.instance_provenance p
    WHERE p.instance_id=si.instance_id AND p.activity_iri='urn:semrisk:scenario-generator:E2E-v1.0'
  );

COMMIT;
