# Candidate Figure 1 and evidence table — SemRisk rc.4

This is a current-version **reviewable publication input**, not final Figure 1 approval, complete OntoUML conformance or a scholarly release. It preserves the historical 2026-icae assets and the complete 15-view rc.4 companion.

## Figure caption

**Figure 1. Selected conceptual distinctions in SemRisk 0.2.0-rc.4.** The source-derived projection includes nine of 47 conceptual entries and eight of 40 registered relation decisions. A scenario is a second-order type, an event an occurrence, and an assessment result an issued information artifact. Register entry, workflow value and risk state remain distinct. Ordinary associations do not indicate causal arrows; `0..*` imposes no global bound. `hasWorkflowState` is the unqualified snapshot relation, not the temporal assignment query. Risk remains an explicitly labeled pattern boundary. The full companion preserves all 47 concepts, 40 relation decisions and qualified-profile constraints; the 38 concepts and 32 relation decisions absent here are omitted only from this selected paper projection.

Caption claim IDs: **SR-CL01**, with source-verification boundary **SR-CL08**. Interpret under `docs/execution/2026-10-04/scientific-contract.md`; no novelty, exclusive differentiation or expert-validation claim.

## Files and reproduction

- `figure1-selected-rc4.svg`: editable vector projection, with source IDs embedded in each concept/relation group.
- `figure1-selected-rc4.pdf`: normalized vector PDF of the same figure; 170 mm wide and 141.11 mm high. Minimum text size is eight points at that physical width.
- `manifest.json`: exact source hashes, baseline commit, selected/omitted denominators and explicit remaining gates.
- `evidence-table.csv` / `.md`: six source-bound rows with target/version, unit, observed result, claim IDs and limitations. Historical CQs/parity remain historical; no SQL work is performed.

Run `python tools/build_publication_assets_rc4.py --check --pdf` and `python tools/check_publication_assets_rc4.py`. Pins are in `requirements.txt`. The SVG's 482-point coordinate width corresponds to the 170 mm print width; font sizes are measured in these points, not inferred from a zoomed raster. Do not scale this figure below 148.75 mm without recalculating the seven-point minimum. The official venue template and final page budget still need manuscript QA.

## Visual review and unresolved gates

The rendered PDF was inspected at publication proportions. The first draft's multiplicity-label overlaps were corrected before publication; no cropped node, changed source relationship or hidden concept substitution was accepted. This review is figure-layout QA, not native-editor round-trip or expert semantic validation. The figure's compactness does not convert the complete atlas's existing `FAIL_READABILITY` at 170 mm into a pass.

Still open under #33/P08: full scoped pattern/antipattern evidence, actual native-editor round-trip, complete article representation and final manuscript integration/author review, #53 claim calibration and #55 publication release binding. This candidate alone closes none of those gates. The source-bound table is an input for #32/#34, not evidence that their page/layout requirements have passed.
