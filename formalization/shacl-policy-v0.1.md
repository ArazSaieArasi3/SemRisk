# SHACL Policy v0.1

- Use SHACL Core by default; SHACL-SPARQL only when necessary and explicitly registered.
- Shapes are named by module/profile and version; no anonymous release-critical shapes.
- Core shapes validate structural invariants only when conceptually justified.
- Enterprise/Method/Pharma/Application shapes may enforce stronger closed-world completeness.
- Controlled vocabularies and status values belong to profile shapes, not Core class taxonomies by convenience.
- Claim-critical violations cannot be downgraded from `Violation` to `Warning` after results are observed.
- Shapes must carry stable semantic requirement/CQ/source references once #43 IDs/IRIs are fixed.
- Shape changes that alter evaluated denominator/result require regression and release-impact review.