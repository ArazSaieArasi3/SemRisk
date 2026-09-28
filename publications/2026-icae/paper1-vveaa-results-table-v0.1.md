# Paper-1 Table Candidate: VVEAA claim-dependent evidence

**Issue:** #33, source #113/#115. **Status:** author-review candidate; final caption/venue layout and release binding pending #53–#55.  
**Table source:** `evaluation/vveaa/paper1-vveaa-claim-method-evidence-v0.1.csv` (9/9 claims). Exact semantic target P1-R2 / 0.1.0-rc.1 candidate.  
**Candidate caption:** *Layered evaluation of the SemRisk Paper-1 candidate. States apply to stated targets and denominators; pending evidence is not counted as success.*

| Function | Method and unit | Current evidence | Limit / pending |
| --- | --- | --- | --- |
| Verification | E1–E3 parse/profile/HermiT/SHACL, entailment and negative fixtures; E4 foundational review | 21/21 bounded E1–E4 records report PASS; 71/71 critical IDs structurally traced; five known-negative SHACL fixtures detected | Logical/structural coherence only; final release SHA and changed-source rerun required. |
| Validation | E5 actual reviewer instrument; E6 exact source/standard/data dispositions | E6: 27/27 selected Jira fields and 18/18 DS-003 elements dispositioned; 9/11 standards rows applicable | Design-influencing evidence is non-independent; E5 real reviewer responses absent; no standards conformance. |
| Evaluation | E7 CQ status; E8 scenario/parity; E9 reproducibility; E10 comparative; E11 heterogeneity | 26 executable / 7 partial / 6 conceptual-only / 1 deferred of 40 CQs; 8/8 *frozen tasks* directly SQL↔SPARQL-equivalent; public/synthetic CI reconstruction bounded | E10 seven-unit source-level result is bounded with no common-task head-to-head; no clean independent E11 shortage holdout; task results do not imply global ontology↔DB equivalence. |
| Assessment | #53 per-claim judgment from nine claim rows and #56 threats | 9/9 claims crosswalked; SR-CL06 blocked for independent transfer and SR-CL07 provisional | Judgment not finalized; no averaging across claims or hidden counterevidence. |
| Assurance | #54 argument/conditions/blockers; #55 immutable release; #35 audit | Integrated assurance **NOT ASSESSED** | No certification, all-green verdict or submission gate PASS asserted. |

**Source trace:** `evaluation/e1-e4/issue29-e1-e4-results-v1.0.csv`; `evaluation/e5-e6/e6-preliminary-validation-report-v0.1.md`; `evaluation/cq/issue52-cq-results-v1.0.csv`; `evaluation/parity/p49-parity-results-v1.0.csv`; `evaluation/e8-e11/issue31-readiness-report-v0.1.md`; `evaluation/integrity/pre-assurance-threat-snapshot-v1.0.md`. This table must be regenerated/rechecked when any numerator, denominator, evidence role or release ref changes. Footnotes in manuscript should distinguish 40 original versus 39 applicable CQs and note DS-003 constructed versus synthetic test additions.
