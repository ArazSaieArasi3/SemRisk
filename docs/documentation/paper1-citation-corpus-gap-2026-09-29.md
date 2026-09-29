# Paper-1 citation corpus coverage checkpoint — 2026-09-29

**Owner:** #121, under #112. **Manuscript:** `publications/2026-icae/manuscript-working-draft-v0.3.md` at `6e0de461b4f045cb30de1d49ec4fefec0abe22a2`. **Corpus:** `docs/documentation/research-reference-corpus.yaml` at the same ref. This is a named-mention audit, not an approved bibliography or claim that the current manuscript has only 30 sources.

The companion CSV checks **30 distinct named citation targets** actually appearing in the working manuscript against the governed REF corpus and 50-source SemRisk source register. **Seven** have seed `REF-0001…0007` identities, but all seven still have empty manuscript membership and `active_unverified` source status. **Twenty-three** targets lack a stable REF entry (14 P0 claim-bearing or case/data targets; nine P1 framework/foundational/specification targets). Eight of the 23 also lack a corresponding identity in the 50-row source register as checked here; that means *registry binding pending*, not absence of an authoritative source. Several target names may resolve to one verified publication or multiple specification references; the 30 is a worklist denominator, not a final citation count.

## Method and boundaries

1. Match explicit source names/IDs in the current manuscript, including closest comparators, standards, foundational/formal dependencies, CM-PharmE and DS-003.
2. Compare with the seven REF seeds and `conceptualization/source-mining/source-register.csv`; preserve `REF_PENDING` rather than inventing IEEE numbers.
3. Prioritize named E10 closest-work sources, CM-PharmE artifact/publication identity and DS-003 DOI/version. Exact publication, DOI, edition, URL health, source role, manuscript membership and rendered citation remain verification work.
4. Treat URLs embedded in manuscript prose and internal source IDs as leads, not a finished bibliography. Paywalled and restricted sources retain their access ceilings.

The CSV includes an observed manuscript token, section/claim route, corpus state, source-register identity if found, priority and next verification step. The seven seed REF rows are **not** citation-ready simply because they have IDs. Current manuscript reference prose explicitly awaits a verified numbered list.

## Next actions

- P0: resolve the 14 pending claim-bearing/case/data targets using their governed source profiles, exact publication/artifact versions and primary DOI/landing pages, then add stable REF entries and manuscript membership.
- P1: resolve the nine foundational/framework/specification targets; especially COSO/OCEG and UFO/gUFO/OntoUML/OWL/SHACL/PROV-O provenance where no source-register identity was found in this check.
- Recheck the seven seed records' metadata, DOI/link health, evidence roles and memberships before IEEE rendering. Only after coverage and order are frozen should page-local IEEE numbers be generated.
- Update source-controlled Wiki evidence/citation routes and perform live private Wiki read-back if their bodies change. #55/#56 still own final scholarly release/citation and public access.

**State:** #121 remains open. This work exposes the exact citation debt and its priority; it does not pass RO-27, #53 final citation consistency or #35 submission audit.
