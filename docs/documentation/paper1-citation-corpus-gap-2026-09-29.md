# Paper-1 citation corpus coverage — 2026-09-29

**Issue:** #121 / #112. **Frozen comparison input:** working manuscript `publications/2026-icae/manuscript-working-draft-v0.3.md` at `6e0de461b4f045cb30de1d49ec4fefec0abe22a2`. The named-mention worklist has **30 targets**. This is a worklist denominator, not an approved bibliography count.

## Source identity passes

| Pass | Named targets with candidate REF | Candidate records | Remaining identity gaps |
| --- | ---: | ---: | ---: |
| Initial audit | 7/30 | 7 seed records | 23 |
| Priority comparator/case binding | 21/30 | 22 | 9 |
| Framework/foundation/specification binding | 30/30 | 31 | 0 within the 30-target worklist |

The extra record is deliberate: `REF-0021` identifies the DS-003 dataset v4 (DOI `10.25375/uct.29178665.v4`) and `REF-0022` the linked study version 2 (DOI `10.12688/wellcomeopenres.24292.2`). Seven original seeds remain candidate and their prior DOI resolver status is preserved. The nine final targets map to COSO 2017, OCEG 3.5, Risk IT 2nd edition, the UFO research article, pinned gUFO v1.0.0, a pinned OntoUML metamodel snapshot, and the date-specific W3C OWL 2 structural specification, SHACL Recommendation and PROV-O Recommendation. The gUFO release tag and current OntoUML metamodel snapshot are bibliography candidates, not proof that every modeling decision used their exact historical files.

## Outstanding quality and citation work

- `PUB-0001` is a **local candidate manuscript identity**. All 31 memberships are `candidate`; the working manuscript contains no stable `[@REF-####]` tokens or rendered IEEE list. No record is marked `cited`.
- Source status and metadata remain partial. Several DOI resolvers and publisher pages were unrendered or access restricted; full COSO/OCEG/ISACA clauses cannot be asserted. Eight foundational/framework/specification targets still lack binding in the 50-row legacy source register; the REF entries do not silently invent source IDs.
- The current manuscript may contain unnamed or implicit sources beyond these 30 named mentions. Claim-local citation placement must check *all* factual/source-dependent passages, not just each name once. Exact PDF section/table locators and external artifact versions remain governed by literature profiles; a publisher page alone does not show head-to-head comparator behavior.
- The official ZivaHub page dates DS-003 v4 to 2025-07-02 and v1 to 2025-06-02. It currently displays Download all (1.94 MB), conflicting with SemRisk's historical 18.01 MB. Byte-level package size remains unverified pending exact v4 file manifest/checksum reconciliation.

## Next

1. Add claim-local candidate REF tokens and a generated draft IEEE list to the manuscript; resolve the candidate publication ID with #55 at release, not by inference.
2. Verify each entry's remaining author/edition/DOI/link metadata and role; bind the eight missing legacy source-register identities or record why a framework/spec reference is separately governed.
3. Refresh source-controlled Wiki routes and check the live private Wiki after any page edit. Execute the research-journey and QN/QL documentation review; #121 remains open until those outputs are inspectable.

**Ceiling:** reference *identity coverage* for 30 named targets only; no final citation completeness, public release or conformance pass.
