# Public repository and Pages artifact exposure audit — 2026-10-02

**Issue:** #56, stage 1. **Baseline:** `62005cc01dd33bb575c7150c541a33d10496bc40` on `main`; full reachable Git history (886 HEAD commits, 1081 distinct blobs). This is a public-exposure inventory and bounded technical scan. It does not authorize a license, prove the absence of sensitive content, certify legal rights, or constitute the #55 scholarly release.

## Observed inventory

| Surface | Finding | Consequence |
| --- | --- | --- |
| Repository and Wiki | Repository public, Wiki enabled and eight pages source-matched at the 2026-09-30 read-back. Repository metadata has no root license and GitHub Pages is disabled. | Public read access already exists. A root reuse license and Pages publication are separate decisions. |
| Full reachable Git history | `python tools/public_history_exposure_scan.py` scanned 1081 blobs for six common credential shapes and 532 historical file paths for named secret/private file formats: zero matches. The original Jira spreadsheet filename and its bytes were not found in tracked paths/blobs by this method. | Bounded, reproducible negative result only. Renamed, encoded, unusually formatted, untracked, Wiki-only, remote-hosted or semantically sensitive contents may evade it; public history cannot be undone by deleting a working-tree file. |
| Derived operational data | Six public `conceptualization/source-mining/SRC-OP-001-*` files identify a private source workbook by SHA-256 and range, expose 27 source-field rows (also repeated in a coverage table), and contain 94 controlled-term rows across three CSVs. The analysis file discusses the derivation. | The workbook itself is not shipped, but extracted field labels and controlled vocabulary values are already public. The owner must explicitly confirm that this derived publication is permitted. Do not reproduce its values in status reports. |
| Offline WebVOWL candidate | `docs/ontology/generated/webvowl-viewer-candidate-v0.1/` has a 15-file pinned runtime manifest. WebVOWL MIT, D3 BSD-3-Clause and Lodash MIT notices are included; the exact combined JSON and five module projections pass static integrity checks (35 local classes / 37 local object properties). | This repository path is publicly readable, but it is not a Pages URL or a released scholarly artifact. Build-only dependency closure is not frozen. |
| Imported ontology attribution | The combined JSON contains imported gUFO terms; the repository has `ontology/vendor/GUFO-LICENSE` (CC BY 4.0). Neither candidate viewer landing page nor frozen formal reference page provides a clear source and license attribution/link next to the view. | Add explicit gUFO attribution and license/source links to a new, reviewed deployable artifact before Pages; preserve the immutable `site/ontology/0.1.0-rc.1/` candidate. |
| Viewer behavior | Existing private desktop/mobile Chromium smoke recorded zero outbound requests. The UI hides converter/upload controls, yet bundled `js/webvowl.app.js` retains `XMLHttpRequest`/`FormData` upload paths. | Review and disable/remove dormant upload paths in a release candidate, then repeat browser network and usability checks on the exact deployable bytes. A previous smoke run is not a proof of all possible interactions. |

## Reproduce and limits

From a **full** clone, run `python tools/public_history_exposure_scan.py`, `python tools/check_webvowl_viewer_bundle.py`, and `python tools/check_webvowl_inputs.py`. The first script rejects shallow history and reports category counts and object prefixes only; it never prints matched contents. The WebVOWL script checks exact manifest hashes, bundled notices, local HTML assets, source JSON equality and module coverage. It does not inspect remote navigation links, every JavaScript network path, terms of use, or phone comprehension. The earlier private browser run is recorded in the viewer README and is not a public URL read-back.

## Decisions and follow-through

1. **Owner decision for #56:** confirm whether publishing the extracted 27 field labels and 94 controlled-term rows from the private Jira workbook was authorized. If not, plan containment with the understanding that current files and Git history were already public; assess Wiki, forks/caches and downstream copies before claiming removal.
2. **Owner decision for #56:** choose an explicit repository-wide reuse license, or consciously retain no root license. Confirm any rights for the SemRisk ontology, code, generated JSON and private-source-derived vocabulary separately from upstream runtime notices. Do not infer permission from public visibility.
3. **Engineering in #119/#117:** prepare a new versioned viewer/formal route with visible gUFO attribution, preserved WebVOWL/D3/Lodash notices, and closed upload/network paths; repeat exact-byte browser, mobile, accessibility and public access QA before enabling Pages and adding Wiki links.
4. **Release in #55/#56:** after the actual expert response and assurance gates, bind the final artifact, citation and availability statement to an immutable ref. Keep #56 open until owner decisions and release read-back are complete.

No root `LICENSE` was added and Pages was not enabled by this audit.

## Owner follow-up, 2026-10-02

After this audit, the owner authorized publication of the extracted vocabulary and requested its reference locations before directing further handling. Decision 1 above is therefore resolved for the extracted vocabulary; original workbook redistribution and the root reuse license are not included. See [the recorded decision and reference inventory](src-op-001-publication-decision-2026-10-02.md). The original audit findings remain as the pre-decision snapshot.
