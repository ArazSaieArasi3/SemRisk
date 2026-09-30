# Paper-1 citation corpus coverage — 2026-09-29

**Issue:** #121 / #112. **Frozen comparison input:** working manuscript `publications/2026-icae/manuscript-working-draft-v0.3.md` at `6e0de461b4f045cb30de1d49ec4fefec0abe22a2`. A second manuscript scan extended the named-mention worklist from 30 to **33 targets**. This is a worklist denominator, not an approved bibliography count.

## Source identity passes

| Pass | Named targets with candidate REF | Candidate records | Remaining identity gaps |
| --- | ---: | ---: | ---: |
| Initial audit | 7/30 | 7 seed records | 23 in that pass |
| Priority comparator/case binding | 21/30 | 22 | 9 in that pass |
| Framework/foundation/specification binding | 30/30 | 31 | 0 in that pass |
| Manuscript rescan and omitted-source binding | 33/33 | 34 | 0 identity gaps in the revised 33-target worklist |
| Claim-local author-review token pass | 33/33 | 34 used at least once | 0 unbound `@REF` tokens in the mutable v0.3 working draft |

The extra record is deliberate: `REF-0021` identifies the DS-003 dataset v4 (DOI `10.25375/uct.29178665.v4`) and `REF-0022` the linked study version 2 (DOI `10.12688/wellcomeopenres.24292.2`). Seven original seeds remain candidate and their prior DOI resolver status is preserved. The nine framework/foundation/specification targets map to COSO 2017, OCEG 3.5, Risk IT 2nd edition, the UFO research article, pinned gUFO v1.0.0, a pinned OntoUML metamodel snapshot, and the date-specific W3C OWL 2 structural specification, SHACL Recommendation and PROV-O Recommendation. The rescan found three distinct manuscript sources omitted from the first worklist: the IEOM 2017 sibling of PH-011 (`REF-0032`, publisher PDF Table 3), TOGAF Standard 10th Edition (`REF-0033`, owner catalog C220), and ArchiMate Specification 3.2 (`REF-0034`, owner download page). The gUFO release tag and current OntoUML metamodel snapshot are bibliography candidates, not proof that every modeling decision used their exact historical files.

## Outstanding quality and citation work

- `PUB-0001` is a **local candidate manuscript identity**. All 34 memberships are `candidate`; the mutable v0.3 working manuscript now has claim-local `[@REF-####]` authoring markers for all 34 distinct records. These are *candidate source identities* rather than numbered IEEE references; no rendered bibliography or author approval exists. No corpus record is marked `cited`.
- Source status and metadata remain partial. Several DOI resolvers and publisher pages were unrendered or access restricted; full COSO/OCEG/ISACA/TOGAF/ArchiMate clauses cannot be asserted. Eleven foundational/framework/specification and newly discovered targets lack IDs in the frozen 50-row G1 register. The [separate governance record](paper1-ref-source-governance-2026-09-29.md) explains each role and trigger without silently rewriting that evidence-mining baseline; IEOM substantive comparator evidence requires #14/#31 impact review.
- The current manuscript may contain unnamed or implicit sources beyond these 33 named mentions. Claim-local citation placement must check *all* factual/source-dependent passages, not just each name once. Exact PDF section/table locators and external artifact versions remain governed by literature profiles; a publisher page alone does not show head-to-head comparator behavior.
- The official ZivaHub page dates DS-003 v4 to 2025-07-02 and v1 to 2025-06-02. It currently displays Download all (1.94 MB), conflicting with SemRisk's historical 18.01 MB. Byte-level package size remains unverified pending exact v4 file manifest/checksum reconciliation.

## Next

1. Check every claim-local candidate marker against the underlying exact source and its scholarly role; generate and proofread a draft IEEE list only after metadata verification. Resolve the candidate publication ID with #55 at release, not by inference.
2. Verify each entry's remaining author/edition/DOI/link metadata and role; apply the eleven-row REF/source-governance decisions, including IEOM #14/#31 impact review, before final claim and IEEE binding.
3. After any page edit, refresh source-controlled Wiki routes and check the live Wiki. The 2026-09-30 public-access/status refresh and 8/8 source/live hash read-back are recorded separately; claim/citation validation and the QN/QL human-dependent review still keep #121 open.

**Ceiling:** reference *identity coverage* for 33 named targets only; no final citation completeness, public release or conformance pass.
