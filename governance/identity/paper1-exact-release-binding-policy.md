# Paper-1 Exact Release Binding Policy

## Required manifest fields
Every P1-R2 or later release bundle must contain:
- planning release ID and bundle ordinal;
- release timestamp;
- exact repository commit SHA;
- conceptual package version;
- ontology module versions and ontology/version IRIs;
- SHACL/rule/mapping versions;
- external dependency exact refs and licenses/status;
- RDB schema/migration version when applicable;
- dataset file IDs/versions/checksums/license/role when applicable;
- CQ/test package version and result artifact checksums;
- evaluation/assurance package version;
- claim-register revision;
- tool versions/container lock or environment lock;
- `change_class` and compatibility/evaluation-reuse decision;
- predecessor bundle ID and lineage.

## Manuscript rule
Every claim/result table or figure that depends on implementation/evaluation must be reconstructable from the P1-R5 manifest. `main`, a screenshot, a branch, or 'latest' cannot substitute for the manifest.

## Release identity
Bundle IRI: `urn:semrisk:release:<bundle-id>`. Example form: `urn:semrisk:release:P1-R5-1`. The bundle IRI identifies the manifest-bound scholarly state, not the ontology itself.

## Rebinding
If a manuscript changes only prose with no artifact/claim dependency change, P1-R5 may remain unchanged. Any changed semantic artifact, mapping, data input, test result or calibrated claim requires impact review and, when material, a successor bundle and rerun.