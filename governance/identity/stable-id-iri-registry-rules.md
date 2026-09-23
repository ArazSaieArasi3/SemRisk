# Stable-ID and IRI Registry Rules

1. IDs are centrally allocated; never hand-reused after deletion/deprecation.
2. ID syntax encodes artifact family, not English meaning.
3. Concept IDs use `SR-CPT-NNN`; relation IDs use `SR-REL-NNN`. New IDs increment monotonically within family.
4. Formal URN is deterministically derived from the stable ID, not label: `urn:semrisk:entity:<ID>`.
5. Label changes do not change ID/URN.
6. If the identity criterion changes, allocate a new ID unless a documented correction preserves the same entity identity.
7. Split/merge operations never erase predecessor records.
8. Public HTTPS IRIs, when later introduced, are aliases/resolution identifiers governed by an explicit migration registry; they are not generated merely because a GitHub Pages URL exists.
9. Ontology/version IRIs use module + semantic version, independent of branch/commit.
10. The ID→IRI registry is a release artifact and must be regression-tested for uniqueness, one-to-one mapping and forbidden reuse.