# R1–R8 remediation evidence ledger — audit checkpoint, 2026-09-25

**Owner:** #110. **Status:** IN PROGRESS / not closure evidence.  
**Machine-readable ledger:** `evaluation/integrity/r1-r8-remediation-evidence-ledger-v0.1.csv`.

## Inspected

- 41 closed corrective issues #69–#109, their eight role acceptance audits, and the role-specific audit sections.
- 44 unique primary paths extracted from those audits plus seven representative paths for entries without an explicit pathname; every selected current artifact path was fetched successfully. One representative primary artifact per issue is recorded with its current Git blob SHA. A primary artifact represents an entry point, not its complete implementation dependency closure.
- R1's four primary artifacts were compared with the exact recorded semantic CI commit `573eb36518454809bbc9d24c1396525cffe7736c`. All four blobs match the current branch.
- R6's six primary artifacts were compared with the exact substantive run commit `7d3915c7c211f9a7a7cc6b827a80ccd3d5bca047`. Four match; two changed later.
- The listed R6/R7/R8 workflow runs were queried for job conclusions; sampled jobs report `success`. Run job queries did not expose the underlying run head commit in this connector, so job success is not equated to an exact current-branch candidate binding.
- The R2 audit originally listed #73–#78 yet declared “all five”. Corrected with a dated note to **six**, preserving the historical 6+2 parity result and its later 8/8 amendment.

## Ledger statuses

| Status | Number | Interpretation |
|---|---:|---|
| PRIMARY_BLOB_MATCH_AT_TEST_REF | 8 | Representative primary artifact blob matches recorded R1/R6 tested commit; other dependencies still need exact release-level impact assessment |
| PRIMARY_BLOB_CHANGED_AFTER_TEST_REF | 2 | Representative R6 artifact changed later; see investigations below |
| RUN_TO_BLOB_BINDING_PENDING | 31 | Audit supplies run/marker but exact run commit was not recovered and compared in this checkpoint |
| Total | 41 | All reviewer-originated corrective issues indexed; **not 41/41 reverified against the current candidate** |

### Two changed artifacts

- **#97:** `evaluation/parity/p49-parity-results-v1.0.csv` at the R6 substantive test ref still reported P49-05 and P49-08 as `equivalent_after_declared_normalization`. The current file reports `equivalent_for_task` with preserved actor and CM-PharmE identity. Commit `b46ebbc75dc96130b6feec33fc2df2f8cade0fd4` later synchronized the 8/8 register; #97 and the R6 audit cite final synchronization run `36124075870` as SUCCESS. **Recheck:** bind that run's head and exact fixture/harness/result state before treating the CSV itself as directly validated at the earlier `7d3915...` ref. The earlier ref cannot substantiate the later CSV.
- **#101:** `evaluation/data/r6-evidence-role-compatibility-v1.0.csv` changed the ER6-008 description from generic future E11 holdout to *cross-domain stress/transfer candidate*. This is consistent with R7's DS-002 role correction (#107), whose acceptance audit cites relational run `36145811696` as SUCCESS. **Recheck:** confirm exact later ref and guard coverage; a R6 run from before R7 cannot attest to the later role wording. DS-002 remains unopened.

## Completion condition for #110

1. Recover exact tested commit/head and relevant artifact bundle for the 31 run-bound rows; compare role-critical paths, not only the one representative primary artifact.
2. Confirm subsequent #97/#101 runs at the exact later refs and the relevant guard outputs, or label the result `UNVERIFIED_PENDING_RECHECK`; run a current candidate validation only where this comparison leaves material uncertainty.
3. Record each role's surviving limitation, including #13, #14, #31 E11, #51, #53/#54/#56. Hand the resulting exact candidate ledger to #111 and #54.
4. Retain the R2 count correction and historical-versus-current parity timeline. Do not close #110 solely because all 41 Issues have a CSV row.

**Interpretation:** documentation trace coverage now exists for 41/41, but current-candidate verification coverage is still conditional. The closed historical remediation issues remain closed as historical bounded decisions; this ledger audits their use in a later publication claim.


## Follow-up: exact CI checkout recovered — 2026-09-25

The prior 8/2/31 count above records the *initial* checkpoint and is retained as audit history. Subsequently, `git log -1 --format=%H` lines were extracted from the successful GitHub Actions job logs for each role. The CSV ledger was refreshed without rewriting that earlier observation:

| Role | Successful run | Exact checkout commit |
|---|---:|---|
| R1 | 36003691215 | `573eb36518454809bbc9d24c1396525cffe7736c` |
| R2 | 36017187020 | `2c72a0fc4c501d27112f652cc5c2380a821e2b34` |
| R3 | 36113296441 | `6b6e401d1b4b34f0e9691f00508b2309e6d2a815` |
| R4 | 36116720075 | `06bff3804062ecae9c018f84b2eaed93dd0c57c3` |
| R5 | 36120388638 | `e78ed06f1469a9f4f692edd327a01690d3bffa08` |
| R6 | 36124075870 | `2259cbfce023c063366e0c27ca1b8b76cd97ff70` |
| R7 | 36145965757 | `6e18964c3267a36fa4bef80ac8ed7e0419d32f37` |
| R8 | 36156336036 | `3c2bd8dd1dc24758221435f4673c2a5431cd5029` |

Primary artifact SHA comparison at each role's listed run: **34/41 match**; **7/41 changed later**. All seven current primary blobs matched a later successful tested checkout: #76 and #85/#87/#88/#90 at R6 run 36124075870; #77 and #101 at R7 semantic run 36145965757 (and R7 relational run 36145811696 also contains them). This confirms version inclusion, **not automatically that every affected assertion had a relevant test in that run**. Inspect changed-file semantics and guard coverage before release binding.

#97's historical mismatch at the earlier R6 run `36123602513` is resolved at the **final** R6 run `36124075870`: its current parity-result blob matches that later exact checkout. The second R6 primary artifact change (#101) is resolved at R7's tested checkout, where DS-002 was reclassified as a cross-domain candidate. Current headline parity remains eight direct equivalents for eight frozen tasks.

**Remaining #110 condition:** assess full dependency closure and changed-file test relevance, including R2 workflow path expansion, R4→R5/6 standards edits and R6→R7 evidence-role changes, then bind the final candidate for #54. A match of one representative blob per issue is not a full reproducibility bundle and does not by itself close #110.
