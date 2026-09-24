-- SemRisk relational twin governed reference/metadata seed | Issue #46
BEGIN;

COMMENT ON SCHEMA meta IS 'Projection identity, provenance and state-transition helpers. Not semantic authority.';
COMMENT ON SCHEMA ref IS 'References to externally owned semantic entities.';
COMMENT ON SCHEMA core IS 'Bounded SemRisk domain-neutral projection.';
COMMENT ON SCHEMA assessment IS 'Assessment activities, results, evidence and observations.';
COMMENT ON SCHEMA treatment IS 'Treatment strategy, plan, activity and controls.';
COMMENT ON SCHEMA enterprise IS 'Risk register, workflow, state and responsibility application profile.';
COMMENT ON SCHEMA governance IS 'Method/governance support projection.';
COMMENT ON SCHEMA pharma IS 'Bounded Pharma bridge projection; external entities remain externally owned.';
COMMENT ON SCHEMA staging IS 'Raw/normalized load staging reserved for #47; no semantic ownership.';

INSERT INTO meta.source_artifact
(source_artifact_id, source_kind, locator, version_ref, sha256, license, evidence_role, accessed_at)
VALUES
('00000000-0000-0000-0000-000000000001','repository-artifact','SemRisk relational twin schema','0.1.0-rc.1',NULL,NULL,'provenance_only',transaction_timestamp())
ON CONFLICT (source_artifact_id) DO NOTHING;

COMMIT;
