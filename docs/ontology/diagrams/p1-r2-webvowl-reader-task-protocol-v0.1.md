# P1-R2 WebVOWL reader task protocol — candidate v0.1

**State:** READY_TO_RUN, NOT_EXECUTED. This protocol checks whether a reader can use the offline exploratory view without mistaking it for semantic authority. It does not certify accessibility or OGCM-RF conformance. The tested bundle must be identified by Git commit and `docs/ontology/generated/webvowl-viewer-candidate-v0.1/manifest.json` SHA-256 values; record browser, viewport, assistive technology (if any), date and participant role. Do not use private operational data or upload the ontology.

## Participants and setup

Recruit at least one ontology/engineering reader and one academic/domain reader who did not build this candidate. Keep their roles and prior SemRisk familiarity, not names, in the result. Run the same tasks on desktop and a 390px-class phone or emulator; one keyboard-only pass on desktop. Serve the bundle on `127.0.0.1` as its README describes. Give the reader the viewer URL and no answer key. The facilitator may point out the View selector after the first unassisted attempt, recording that prompt.

## Tasks and observable outcomes

| ID | Reader request | Success evidence | Failure/limit to record |
| --- | --- | --- | --- |
| T1 | Find a focused view for the Enterprise module and identify whether `SR-CPT-006` is a local Enterprise class or a referenced external stub. | Reader selects Enterprise, sees `SR-CPT-006 (external)`, and states that source-only module views omit imported/cross-module definitions. | Treating the stub as a full local Enterprise definition; cannot operate selector on phone/keyboard. |
| T2 | Locate the distinction between Risk Scenario (`SR-CPT-006`) and Risk Event (`SR-CPT-007`) and find the formal source for the distinction. | Reader uses the viewer only as a locator, follows Semantic source/Formal explanation, and identifies the source-bound disjointness in the formal description. | Claiming graph position alone proves an axiom, or failing to reach the formal reference. |
| T3 | Explain whether the combined view shows all formal semantics and whether the seven-file 1,409-triple graph is an entailment closure. | Reader says the viewer is derived and exploratory, and the graph is an **asserted import closure**, not an OWL entailment closure. | Calling it a complete ontology diagram, independent validation or inferred closure. |
| T4 | On the phone, find a legible module view, zoom a node and return to the combined view. On desktop, repeat using keyboard alone for selector, zoom and details rail. | Record each successful action and whether labels can be read without facilitator interpretation; keyboard focus is visible. | Inability to read labels, reach a control, perceive focus, or recover from pan/zoom. |

## Result record and decision rule

For each participant/task/viewport, record `PASS`, `PARTIAL` or `FAIL`, time to completion, prompts, navigation path, misinterpretations and a screenshot or observation note. `PARTIAL` includes a correct answer only after a prompt or unreadable labels requiring another source. Record screen-reader name/version and observed graph semantics separately; a keyboard pass is not a screen-reader pass.

Do not mark #119 reader usability complete until both roles have performed T1–T4, the phone and keyboard paths are reviewed, any material misinterpretation is fixed or explicitly bounded, and the actual tested commit/assets are pinned. Public route/read-back and #55/#56 access/release decisions remain separate #117 gates. The [browser smoke record](p1-r2-webvowl-browser-qa-2026-09-27.md) is engineering preflight, not a participant result.
