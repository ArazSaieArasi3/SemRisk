# Exposure projection, rc.4

| Source | Existing relational field | RDF meaning |
|---|---|---|
| Exposure IRI | meta.semantic_instance.instance_iri / core.exposure.exposure_id | SR-CPT-010 instance identity |
| Exposed subject | core.exposure.subject_instance_id | SR-REL-039 |
| Exposure source | core.exposure.source_instance_id | SR-REL-040 |
| Start/end | core.exposure.valid_from / valid_to | ac:validFrom / ac:validTo |

No DDL migration is needed for these existing fields. The synthetic adapter validates endpoint completeness and types before insert, preserves exposure identity and periods, rejects conflicting history, and returns only the represented graph projection. A timeless `exposes` pair is not reconstructed as an episode. Explicit differentFrom/provenance triples outside these columns are not claimed to round-trip. The test fixture's scale/version/content statements are outside this adapter; full new-helper projection remains #125. The exporter is for the adapter's validated synthetic namespace and must not be used to assert types for unaudited legacy rows.
