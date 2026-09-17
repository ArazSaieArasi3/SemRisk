# SemRisk Paper 1 — ICAE 2026 Venue Contract

**Verified:** 2026-09-17  
**Contract status:** CONDITIONAL PASS — venue is current/feasible, but official submission timezone is not stated, selected policy details are not explicitly published on the checked pages, and IEEE Xplore inclusion remains pending final approval/quality review.

## Canonical venue identity

- **Conference:** 9th International Conference on Applied Engineering
- **Acronym:** ICAE 2026
- **Organizer/host:** Politeknik Negeri Batam (Polibatam), Indonesia
- **Conference dates:** 19–20 November 2026
- **Official site:** https://icae.polibatam.ac.id/
- **Official author-guidelines/registration page:** https://icae.polibatam.ac.id/registration
- **Submission system:** EDAS, https://edas.info/N35485

## Target track for SemRisk

**Track 2 — IEEE Proceeding / Cluster B — Informatics & AI.**

The official ICAE 2026 site places Software Engineering, AI, IoT and Cybersecurity inside the Informatics & AI cluster. SemRisk should be framed as an ontology-engineering / software-engineering / semantic risk-management contribution, not as an auditing paper and not as a mechanical-engineering submission.

## Important dates

| Milestone | Verified date/status |
|---|---|
| Full paper submission | **30 September 2026** |
| Notification | **26 October 2026** |
| Camera-ready + payment | **6 November 2026** |
| Conference | **19–20 November 2026** |

### Deadline timezone control

The official ICAE pages currently state the submission **date** but do not state an explicit deadline timezone/time-of-day. Therefore the official deadline is recorded as `2026-09-30 (timezone/time not stated)` rather than inventing a conference deadline time.

For internal execution only, SemRisk uses a conservative safety cutoff of **2026-09-29T12:00:00Z** and requires the EDAS deadline display to be rechecked immediately before submission. This internal cutoff is not represented as an official ICAE deadline.

## Format and page contract

- Official IEEE conference template / two-column format.
- Initial proceeding-paper submission: PDF via EDAS according to the current proceeding requirements.
- **Hard planning cap: 8 total pages including figures, tables and references.**
- The author-guidelines page also uses `6–8 pages` wording and elsewhere mentions typical 4–6 pages plus references/extra-page charges. Because the pages are internally inconsistent, SemRisk will use the stricter safe interpretation: **never exceed 8 total manuscript pages unless ICAE explicitly clarifies otherwise in writing.**
- Similarity index must not exceed 20%.
- Initial submission must be anonymized for double-blind review.
- At least one author/designated substitute must present; no-show papers are not submitted for publication/indexing.

## Policies not explicitly resolved on the checked official pages

- **Submission timezone/time-of-day:** not stated.
- **Generative-AI assisted writing disclosure:** no explicit ICAE-specific rule was found on the checked official pages; final submission must follow any rule exposed by EDAS/IEEE/organizer at submission time and must not infer that silence means unrestricted use.
- **Supplementary-material policy:** not explicitly stated on the checked official pages; supplementary artifacts should remain repository-hosted/release-bound unless ICAE/EDAS exposes an approved channel.

These are controlled as `NOT_STATED / RECHECK_REQUIRED`, not as PASS.

## Publication / indexing status

The official site states that ICAE 2026 is technically co-sponsored by **IEEE Indonesia Section** and that accepted papers within IEEE's scope are intended to be submitted for consideration to **IEEE Xplore**, subject to final approval, sponsorship agreement and IEEE quality/scope review.

Therefore the repository must use wording such as:

> `intended for IEEE Xplore consideration, pending final approval and IEEE quality/scope review`

and must **not** state that IEEE Xplore or Scopus indexing is guaranteed.

## Superseded venue assumption

The previous repository target `ICAEA 2026 — International Conference on Computer Auditing` is not a feasible current submission target:

- official conference dates: 31 May–2 June 2026;
- official submission deadline: 28 February 2026;
- venue/topic: Computer Auditing / accounting and audit analytics;
- submission style: APA rather than the SemRisk repository's assumed IEEE contract.

Official source checked: https://www.icaea.net/ICAEA2026/CFP.php

The previous `publications/2026-icaea/` material is therefore historical planning evidence and must not remain the canonical active Paper-1 venue contract.

## SemRisk publication controls

1. Paper 1 must fit **8 total pages including references** under the conservative contract.
2. The manuscript should target Cluster B / Software Engineering / Informatics scope explicitly in title, abstract, keywords and contribution framing where scientifically accurate.
3. Ontology/RDB/Risk Intelligence breadth may not be added merely because a venue accepts up to 8 pages.
4. Abstract/conclusion may not claim guaranteed IEEE Xplore/Scopus indexing.
5. The exact EDAS deadline/timezone must be rechecked before final submission; if a materially different deadline is shown, Issue #38 and this contract must be amended.
6. Any conference-site change to page/template/publication status triggers an impact review of #1/#32/#34/#35.
7. AI-disclosure and supplementary-material handling remain recheck items until the organizer/EDAS publishes an explicit rule.

## Gate decision

**CONDITIONAL PASS**

The venue is current and the known contract is sufficiently precise to proceed with Paper-1 study-design and contribution freeze. Conditions are:

- recheck EDAS deadline time/timezone before submission;
- keep IEEE Xplore/indexing wording explicitly conditional;
- use the conservative 8-total-page cap until the organizer clarifies any internal wording inconsistency;
- recheck AI-disclosure and supplementary-material rules at the final submission gate.
