# Run 16 — rc.4 offline formal-surface parity

Baseline: `bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6`. This implements a dependency-ready part of first-priority #115/#124 synchronization. It does not require a manuscript, SQL work, release decision or public deployment.

## Actual gap and implemented correction

The accepted rc.4 reference was not represented in the existing Wiki/Pages tooling: those scripts and the live Wiki still target P1-R2/rc.1. A new isolated rc.4 route now supplies all 116 local-term anchors, the full FD-A–FD-J interpretation, a separate Wiki draft and exact critical-source parity. Historical artifacts remain intact.

The projection checks 14 selected terms across risk/record, scenario/event, activity/result, treatment strategy/plan/activity/control, domain/workflow state, Exposure and NumericScale identity. It preserves source labels, explicit superclass/disjointness commitments and Exposure endpoints without inferring semantics from diagram appearance.

An independently checked baseline source lock fixes the bd7 Git blobs and SHA-256 values. This closes a review-discovered stale-commit gap: recomputing working hashes after a source change cannot continue claiming the old source commit. Deliberate source, ID, category, label, anchor, version-link, route and history corruptions are rejected. No aggregate scientific score follows.

## Verification and boundaries

The source guard and historical offline/Wiki checks run separately. CI must execute the real base-commit history checks with a sufficient checkout depth, not only an in-memory overwrite test. Desktop/mobile browser navigation and screenshot review are required before final visual acceptance. Exact-head results and main readback belong to the batch PR.

The live Wiki has not changed and Pages remains disabled. Thus live parity, deployment, release identity, full OntoUML/native-editor acceptance and target-reader usability are not established. #115/#124 stay open. Individual accepted requirement/package counts are not increased by this narrower documentation checkpoint: durable baseline remains 34/90 and 3/19. Local manuscript acceptance remains separate.
