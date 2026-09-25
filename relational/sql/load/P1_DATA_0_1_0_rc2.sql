-- SemRisk Paper-1 governed data snapshot | Issue #47
-- Snapshot: P1-DATA-0.1.0-rc.2
-- This load uses only governed constructed/synthetic data and source metadata.
-- DS-004 is blocked from file-level load; DS-002 remains protected as a cross-domain Pharma stress candidate.

BEGIN;

-- Stable load-batch identity.
INSERT INTO staging.load_batch
(load_batch_id,batch_code,pipeline_version,status,source_scope,repository_commit,notes)
VALUES
('47000000-0000-0000-0000-000000000001','P1-DATA-0.1.0-rc.2','0.1.0-rc.2','started',
 'SRC-OP-001 schema metadata + DS-003 constructed bounded case + deterministic synthetic operational fixture',
 NULL,
 'DS-004 blocked; DS-002 protected cross-domain Pharma stress candidate; DS-001 supplementary not loaded as primary.')
ON CONFLICT (load_batch_id) DO NOTHING;

-- Governed source artifacts.
INSERT INTO meta.source_artifact
(source_artifact_id,source_kind,locator,version_ref,sha256,license,evidence_role,accessed_at)
VALUES
('47000000-0000-0000-0000-000000000101','operational-spreadsheet','jira risk attributes.xlsx | Sheet1!A1:C28',
 'sha256:6f40bb5dd670e884df205093b8048d62807f5371e502997279f03073b09e5c8f',
 '6f40bb5dd670e884df205093b8048d62807f5371e502997279f03073b09e5c8f',
 'private-do-not-redistribute','design',NULL),
('47000000-0000-0000-0000-000000000103','public-dataset','https://doi.org/10.25375/uct.29178665.v4',
 'v4',NULL,'CC BY 4.0','bounded_case',NULL),
('47000000-0000-0000-0000-000000000104','public-dataset','https://figshare.com/s/a0bca1308da751f465b6',
 'UNVERSIONED_SHARE_STATE',NULL,'TO_VERIFY','provenance_only',NULL),
('47000000-0000-0000-0000-000000000102','public-dataset','https://doi.org/10.7910/DVN/G9SHDA',
 'EXACT_RELEASE_TBD',NULL,'TO_VERIFY','transferability_holdout',NULL),
('47000000-0000-0000-0000-000000000199','synthetic-generator','SemRisk deterministic Paper-1 fixture generator',
 'SYNTH-P1-0.1.0-seed-4701',NULL,'N/A','synthetic_test',NULL)
ON CONFLICT (source_artifact_id) DO NOTHING;

-- Preserve blocked/protected inputs in staging rather than silently dropping them.
INSERT INTO staging.source_record
(source_record_id,load_batch_id,source_artifact_id,source_record_key,source_locator,raw_semantic_summary,transform_rule_id,target_instance_iri,disposition)
VALUES
('47000000-0000-0000-0000-000000010004','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000104',
 'DS-004-FILE-LEVEL','Chirac et al. 2026 + authoritative Figshare share locator',
 'Structured shortage data family; exact file/version/license/checksum/schema not frozen.','MDB-001',NULL,'blocked'),
('47000000-0000-0000-0000-000000010002','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000102',
 'DS-002-RECORD-LEVEL','Harvard Dataverse DOI 10.7910/DVN/G9SHDA',
 'FAERS-derived records intentionally not inspected; protected for future cross-domain Pharma Core stress testing, not shortage validation.','MDB-002',NULL,'protected')
ON CONFLICT (source_record_id) DO NOTHING;

-- SRC-OP-001: schema-level provenance only; no empirical records are fabricated.
INSERT INTO staging.source_record
(source_record_id,load_batch_id,source_artifact_id,source_record_key,source_locator,raw_semantic_summary,transform_rule_id,target_instance_iri,disposition)
VALUES
('47000000-0000-0000-0000-000000010001','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000101',
 'SRC-OP-001-SCHEMA','Sheet1!A1:C28',
 '27/27 operational attributes are governed mapping inputs; no record corpus was supplied.','MDM-001..027',NULL,'context_only')
ON CONFLICT (source_record_id) DO NOTHING;

-- DS-003 constructed bounded Pharma case semantic instances.
INSERT INTO meta.semantic_instance
(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
VALUES
('47000000-0000-0000-0001-000000000001','urn:semrisk:case:pharma:v1:risk-context','SR-CPT-001','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000002','urn:semrisk:case:pharma:v1:supply-concentration-condition','SR-CPT-004','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000003','urn:semrisk:case:pharma:v1:forecasting-condition','SR-CPT-004','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000004','urn:semrisk:case:pharma:v1:scenario','SR-CPT-006','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000005','urn:semrisk:case:pharma:v1:pooled-procurement-strategy','SR-CPT-026','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000006','urn:semrisk:case:pharma:v1:transparency-response-candidate','PROFILE-PHARMA-RESPONSE-CANDIDATE','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000007','urn:semrisk:case:pharma:v1:evidence-ds003','SR-CPT-020','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000008','urn:semrisk:case:pharma:v1:assessment-activity','SR-CPT-011','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000009','urn:semrisk:case:pharma:v1:assessment-result','SR-CPT-013','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000000010','urn:semrisk:case:pharma:v1:risk-state-contextual','SR-CPT-035','47000000-0000-0000-0000-000000000103','constructed_case',true)
ON CONFLICT (instance_id) DO NOTHING;

INSERT INTO core.risk(risk_id,title,description) VALUES
('47000000-0000-0000-0001-000000000001','Bounded antibiotic-shortage management risk','Constructed illustrative risk context grounded in DS-003 thematic evidence.')
ON CONFLICT DO NOTHING;

INSERT INTO core.predisposing_condition(condition_id,description) VALUES
('47000000-0000-0000-0001-000000000002','Study-supported thematic condition concerning concentration/limited suppliers in antibiotic/API supply.'),
('47000000-0000-0000-0001-000000000003','Study-supported thematic condition concerning forecasting/demand-estimation challenges.')
ON CONFLICT DO NOTHING;

INSERT INTO core.risk_scenario(scenario_id,risk_id,description) VALUES
('47000000-0000-0000-0001-000000000004','47000000-0000-0000-0001-000000000001',
 'Possible antibiotic supply disruption scenario constructed from bounded source themes.')
ON CONFLICT DO NOTHING;

INSERT INTO core.scenario_condition(scenario_id,condition_id) VALUES
('47000000-0000-0000-0001-000000000004','47000000-0000-0000-0001-000000000002'),
('47000000-0000-0000-0001-000000000004','47000000-0000-0000-0001-000000000003')
ON CONFLICT DO NOTHING;

INSERT INTO treatment.strategy(strategy_id,title,description) VALUES
('47000000-0000-0000-0001-000000000005','Pooled procurement','Proposed treatment strategy; no effectiveness claim.')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.evidence_item(evidence_id,content_locator,source_artifact_id,evidence_kind) VALUES
('47000000-0000-0000-0001-000000000007','DS-003 v4 / linked study thematic synthesis','47000000-0000-0000-0000-000000000103','constructed-source-summary-anchor')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_activity(assessment_id,risk_id,started_at,ended_at) VALUES
('47000000-0000-0000-0001-000000000008','47000000-0000-0000-0001-000000000001',NULL,NULL)
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_result(result_id,assessment_id,risk_id,result_kind,value_text) VALUES
('47000000-0000-0000-0001-000000000009','47000000-0000-0000-0001-000000000008',
 '47000000-0000-0000-0001-000000000001','generic',
 'Constructed qualitative assessment result; no numeric risk score asserted.')
ON CONFLICT DO NOTHING;

INSERT INTO assessment.assessment_evidence(result_id,evidence_id,support_role) VALUES
('47000000-0000-0000-0001-000000000009','47000000-0000-0000-0001-000000000007','support')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_state_history(risk_state_id,risk_id,state_code,evidence_result_id) VALUES
('47000000-0000-0000-0001-000000000010','47000000-0000-0000-0001-000000000001',
 'contextual_constructed','47000000-0000-0000-0001-000000000009')
ON CONFLICT DO NOTHING;

-- Exact external CM-PharmE v1.0.0 refs needed by constructed case.
INSERT INTO meta.semantic_instance
(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
VALUES
('47000000-0000-0000-0001-000000001011','urn:cm-pharme:v1.0.0:CMPE-C0011','EXT-CMPE-C0011','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000001032','urn:cm-pharme:v1.0.0:CMPE-C0032','EXT-CMPE-C0032','47000000-0000-0000-0000-000000000103','constructed_case',true),
('47000000-0000-0000-0001-000000001010','urn:cm-pharme:v1.0.0:CMPE-C0010','EXT-CMPE-C0010','47000000-0000-0000-0000-000000000103','constructed_case',true)
ON CONFLICT (instance_id) DO NOTHING;

INSERT INTO ref.external_entity
(external_entity_id,instance_id,owner_namespace,owner_semantic_id,version_ref,label)
VALUES
('47000000-0000-0000-0002-000000001011','47000000-0000-0000-0001-000000001011','CM-PharmE','CMPE-C0011','v1.0.0','Ecosystem Supply Capacity'),
('47000000-0000-0000-0002-000000001032','47000000-0000-0000-0001-000000001032','CM-PharmE','CMPE-C0032','v1.0.0','Supply Chain Relationship'),
('47000000-0000-0000-0002-000000001010','47000000-0000-0000-0001-000000001010','CM-PharmE','CMPE-C0010','v1.0.0','Ecosystem Demand Signal')
ON CONFLICT (external_entity_id) DO NOTHING;

INSERT INTO pharma.context_link(risk_id,external_entity_id) VALUES
('47000000-0000-0000-0001-000000000001','47000000-0000-0000-0002-000000001011'),
('47000000-0000-0000-0001-000000000001','47000000-0000-0000-0002-000000001032')
ON CONFLICT DO NOTHING;

INSERT INTO pharma.context_link(scenario_id,external_entity_id) VALUES
('47000000-0000-0000-0001-000000000004','47000000-0000-0000-0002-000000001011'),
('47000000-0000-0000-0001-000000000004','47000000-0000-0000-0002-000000001032')
ON CONFLICT DO NOTHING;

INSERT INTO pharma.context_link(risk_id,external_entity_id)
VALUES ('47000000-0000-0000-0001-000000000001','47000000-0000-0000-0002-000000001010')
ON CONFLICT DO NOTHING;

-- DS-003 source-row lineage for the five governed constructed inputs.
INSERT INTO staging.source_record
(source_record_id,load_batch_id,source_artifact_id,source_record_key,source_locator,raw_semantic_summary,transform_rule_id,target_instance_iri,disposition)
VALUES
('47000000-0000-0000-0003-000000000001','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000103','PCI-001','linked study Results / dataset v4 analysed data','Supply concentration and limited API suppliers are discussed as contributors to antibiotic shortage vulnerability.','PCI-001→SR-CPT-004','urn:semrisk:case:pharma:v1:supply-concentration-condition','loaded'),
('47000000-0000-0000-0003-000000000002','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000103','PCI-002','linked study Results / dataset v4 analysed data','Political engagement and government investment are discussed in relation to mitigation capability.','PCI-002 partial/context','urn:semrisk:case:pharma:v1:risk-context','partial'),
('47000000-0000-0000-0003-000000000003','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000103','PCI-003','linked study Results / dataset v4 analysed data','Forecasting and demand estimation challenges are discussed as management constraints.','PCI-003→SR-CPT-004','urn:semrisk:case:pharma:v1:forecasting-condition','loaded'),
('47000000-0000-0000-0003-000000000004','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000103','PCI-004','linked study Results / dataset v4 analysed data','Pooled procurement is discussed as a possible mitigation strategy.','PCI-004→SR-CPT-026','urn:semrisk:case:pharma:v1:pooled-procurement-strategy','loaded'),
('47000000-0000-0000-0003-000000000005','47000000-0000-0000-0000-000000000001','47000000-0000-0000-0000-000000000103','PCI-005','linked study Results / dataset v4 analysed data','Greater transparency in manufacturing and supply chains is discussed as a management need.','PCI-005→PROFILE-PHARMA-RESPONSE-CANDIDATE','urn:semrisk:case:pharma:v1:transparency-response-candidate','partial')
ON CONFLICT (source_record_id) DO NOTHING;

-- Deterministic synthetic operational fixture (seed 4701), explicitly non-empirical.
INSERT INTO meta.semantic_instance
(instance_id,instance_iri,semantic_type_id,source_artifact_id,evidence_role,synthetic_flag)
VALUES
('47000000-0000-0000-0010-000000000001','urn:semrisk:synthetic:p1:4701:risk','SR-CPT-001','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('47000000-0000-0000-0010-000000000002','urn:semrisk:synthetic:p1:4701:register','SR-CPT-032','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('47000000-0000-0000-0010-000000000003','urn:semrisk:synthetic:p1:4701:entry','SR-CPT-033','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('47000000-0000-0000-0010-000000000004','urn:semrisk:synthetic:p1:4701:workflow-state','SR-CPT-036','47000000-0000-0000-0000-000000000199','synthetic_test',true),
('47000000-0000-0000-0010-000000000005','urn:semrisk:synthetic:p1:4701:responsibility','SR-CPT-031','47000000-0000-0000-0000-000000000199','synthetic_test',true)
ON CONFLICT (instance_id) DO NOTHING;

INSERT INTO core.risk(risk_id,title,description)
VALUES('47000000-0000-0000-0010-000000000001','Synthetic operational risk','Deterministic non-empirical fixture for relational regression.')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_register(register_id,name,version_label)
VALUES('47000000-0000-0000-0010-000000000002','Synthetic Paper-1 Risk Register','SYNTH-P1-0.1.0')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_register_entry(entry_id,register_id,risk_id,title,description)
VALUES('47000000-0000-0000-0010-000000000003','47000000-0000-0000-0010-000000000002',
'47000000-0000-0000-0010-000000000001','Synthetic risk entry','Generated from seed 4701; not observed evidence.')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.workflow_state_history(workflow_state_id,entry_id,state_code,is_current)
VALUES('47000000-0000-0000-0010-000000000004','47000000-0000-0000-0010-000000000003','open',true)
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.actor_ref(actor_id,actor_iri,actor_kind,label)
VALUES('47000000-0000-0000-0011-000000000001','urn:semrisk:fixture:p1:synthetic:risk-manager','synthetic','Synthetic Risk Manager')
ON CONFLICT DO NOTHING;

INSERT INTO enterprise.risk_responsibility(responsibility_id,actor_id,risk_id)
VALUES('47000000-0000-0000-0010-000000000005','47000000-0000-0000-0011-000000000001',
'47000000-0000-0000-0010-000000000001')
ON CONFLICT DO NOTHING;

INSERT INTO meta.instance_provenance(instance_provenance_id,instance_id,source_artifact_id,activity_iri,agent_iri,generated_at,derivation_note)
VALUES
('47000000-0000-0000-0012-000000000001','47000000-0000-0000-0010-000000000001','47000000-0000-0000-0000-000000000199','urn:semrisk:generator:SYNTH-P1-0.1.0','urn:semrisk:agent:deterministic-generator',NULL,'seed=4701; deterministic synthetic fixture; not empirical evidence'),
('47000000-0000-0000-0012-000000000002','47000000-0000-0000-0010-000000000002','47000000-0000-0000-0000-000000000199','urn:semrisk:generator:SYNTH-P1-0.1.0','urn:semrisk:agent:deterministic-generator',NULL,'seed=4701; deterministic synthetic fixture; not empirical evidence'),
('47000000-0000-0000-0012-000000000003','47000000-0000-0000-0010-000000000003','47000000-0000-0000-0000-000000000199','urn:semrisk:generator:SYNTH-P1-0.1.0','urn:semrisk:agent:deterministic-generator',NULL,'seed=4701; deterministic synthetic fixture; not empirical evidence'),
('47000000-0000-0000-0012-000000000004','47000000-0000-0000-0010-000000000004','47000000-0000-0000-0000-000000000199','urn:semrisk:generator:SYNTH-P1-0.1.0','urn:semrisk:agent:deterministic-generator',NULL,'seed=4701; deterministic synthetic fixture; not empirical evidence'),
('47000000-0000-0000-0012-000000000005','47000000-0000-0000-0010-000000000005','47000000-0000-0000-0000-000000000199','urn:semrisk:generator:SYNTH-P1-0.1.0','urn:semrisk:agent:deterministic-generator',NULL,'seed=4701; deterministic synthetic fixture; not empirical evidence')
ON CONFLICT (instance_provenance_id) DO NOTHING;

-- Constructed Pharma transformation lineage; these are abstractions, not raw DS-003 rows.
INSERT INTO meta.instance_provenance(instance_provenance_id,instance_id,source_artifact_id,activity_iri,agent_iri,generated_at,derivation_note)
VALUES
('47000000-0000-0000-0013-000000000001','47000000-0000-0000-0001-000000000001','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'Constructed from DS-003 study-level thematic summary under case protocol v1.0.'),
('47000000-0000-0000-0013-000000000002','47000000-0000-0000-0001-000000000002','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'PCI-001 source-supported thematic condition.'),
('47000000-0000-0000-0013-000000000003','47000000-0000-0000-0001-000000000003','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'PCI-003 source-supported thematic condition.'),
('47000000-0000-0000-0013-000000000004','47000000-0000-0000-0001-000000000004','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'Constructed scenario; no realized event fabricated.'),
('47000000-0000-0000-0013-000000000005','47000000-0000-0000-0001-000000000005','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'PCI-004 proposed strategy; no effectiveness claim.'),
('47000000-0000-0000-0013-000000000006','47000000-0000-0000-0001-000000000006','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'PCI-005 management-need response candidate; contextual typing unresolved; no effectiveness claim.'),
('47000000-0000-0000-0013-000000000007','47000000-0000-0000-0001-000000000007','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'DS-003 evidence anchor.'),
('47000000-0000-0000-0013-000000000008','47000000-0000-0000-0001-000000000008','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'Projection-required constructed assessment activity; not an observed empirical activity.'),
('47000000-0000-0000-0013-000000000009','47000000-0000-0000-0001-000000000009','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'Constructed qualitative result; no numeric score.'),
('47000000-0000-0000-0013-000000000010','47000000-0000-0000-0001-000000000010','47000000-0000-0000-0000-000000000103','urn:semrisk:transformation:pharma-case-v1.1','urn:semrisk:agent:governed-transformation',NULL,'Constructed contextual state; not measured real-world state.')
ON CONFLICT (instance_provenance_id) DO NOTHING;

UPDATE staging.load_batch
SET status='completed', completed_at=transaction_timestamp()
WHERE load_batch_id='47000000-0000-0000-0000-000000000001';

COMMIT;
