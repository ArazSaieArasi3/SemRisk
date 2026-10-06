# Run 21 — selected antipattern behavior and native-editor gate

Baseline: `5e3e1651794c4fc40b1a4cd36733c9f4a92148c1`. This batch adds actual selected probes and a source-level compatibility audit. It does not change the canonical model, shapes, production queries, SQL, manuscript or published site.

## Actual selected evidence

The [behavioral protocol](../../../evaluation/antipatterns/0.2.0-rc.4/behavioral/protocol.json) was committed as `829c94b9f080347539ce06f5d2e97d327539f72c` before execution. Independent review tightened exact SHACL result-node counts, bridge mapping decisions and object-position reference checks before the experiment.

The [results](../../../evaluation/antipatterns/0.2.0-rc.4/behavioral/results.json) contain **50 checks, including 25 rejection controls**. Nine worlds pass OWL 2 DL first; HermiT then confirms four consistent countermodels and five actual contradictions. This adds selected current evidence for FAP-006, FAP-012, FAP-013 and FAP-014. All 15 full-antipattern verdicts remain **NOT_ESTABLISHED**.

One adverse observation is separate from those successful checks: the current IRI-only assignee shape accepts the known Risk Owner class IRI, and the query returns it. This is not a successful class-target rejection. Any mitigation must preserve frozen source bytes and distinguish a new optional application guard from a decision to require grounding universally.

The external CM-PharmE catalog and manifest are checked at exact immutable commit/blob/SHA256 identities in temporary input storage. Their raw source files are not vendored or uploaded in the proof artifact. The original source conflict and unmapped API/product/Objective gaps remain explicit.

## Native-editor compatibility

The [source-level audit](../../documentation/native-editor/compatibility-20261006.md) identifies a concrete format and annotation-preservation gap in released Visual Paradigm plugin 0.5.3. Its source uses a different project/relation structure, lacks the needed note/anchor import-export path, and rewrites native IDs. Recasting SR-REL-038 as an association would change meaning. This is not an executed import failure or compiled-binary test.

No compatible native editor was available in the inspected environment. A supported annotation-preserving path, editor access/license eligibility and actual import/save/reopen/export remain necessary. No installation, terms acceptance or external model transmission was performed.

## Acceptance and next gates

Bounded author requirements remain **40/90**; whole packages **3/19**. No whole finding or issue closes from these selected probes. [Per-issue remaining acceptance](remaining-advanced-issues-20261006.md) separates completed evidence from implementation, private-integration and human/release gates. #125 and #51 remain deferred.

Independent local rerun has passed. Exact-head CI, artifact/source readback and merged-main verification are required on the batch PR before durable integration.
