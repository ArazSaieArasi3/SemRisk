# Multi-Ontology External Identity and Collision Policy v1.0

**Owner:** Issue #94

## Source identity key
The governed source identity of an external entity is:
`(owner_namespace, owner_semantic_id, version_ref)`.

A label is display metadata and is never an identity key.

## Multiple ontology references
Two records with the same label but different owner namespace, semantic ID or version remain distinct external references.

## Correspondence
Cross-ontology correspondence is represented explicitly with one of:
- `exactMatch`
- `closeMatch`
- `relatedMatch`
- `broadMatch`
- `narrowMatch`

These mapping relations do not imply `owl:sameAs`, `owl:equivalentClass` or database row identity.

## Version change
A new external version remains a distinct source identity reference unless an explicit migration/correspondence assertion records continuity. Labels alone never authorize migration.

## Collision rule
If two external sources appear to denote the same real-world bearer, SemRisk may link them by an explicit mapping assertion while preserving both source identities and provenance.
