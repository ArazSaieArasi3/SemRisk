# Run 11 — selected publication figure and version-explicit evidence table

Baseline main: `3bbe7e8e3a51d609bf09d9e92462e8d444a5f49b`. Scope: dependency-ready #33 assets. No ontology, shape, SQL, full atlas or empirical source data is changed. #125 remains deferred.

## Delivered inputs

1. A source-derived four-panel Figure 1 **candidate**, explicitly selecting 9/47 concepts and 8/40 relation decisions. Labels, stereotypes, association names and unconstrained endpoints come from the existing rc.4 view specification; Risk remains a pattern boundary.
2. Editable SVG and equivalent vector PDF at **170 × 141.111 mm**, with actual **8-point minimum text** in both SVG physical scaling and PDF effective text transformations. Seven negative controls reject missing elements, altered stereotypes/cardinalities, invented arrows, stale source binding, too-small print scaling and miswired endpoints.
3. Six-row evidence table with target/version, unit, result, calibrated claim ID, source and limit. Current rc.4 inventory/verification and six-source/24-statement applicability pilot remain separate from historical 40-CQ classification and eight frozen SQL/SPARQL tasks.
4. Source manifest, complete caption/limitations, pinned export dependencies and path-triggered reproduction/print QA workflow.

Files are under `publications/2026-icaea-sbu/visuals-rc4/`. The old `publications/2026-icae/` artifacts and the complete 47/40 companion atlas remain unchanged. This batch does not silently promote the old 90 mm figure (whose minimum physical font is below seven points) or the unreadable complete 170 mm atlas to a publication pass.

## Review and evidence boundary

Local deterministic source checks and vector-PDF text/geometry checks pass; final selected SVG and PDF were rendered and visually inspected. Multiplicity overlaps and one obscured box border in the first layout were corrected before publication. Exact remote head, independent review, CI and main readback are recorded on this batch's pull request; this report alone is not merge evidence.

This is a figure-layout/source-correspondence result, not native-editor round-trip, full OntoUML/UFO conformance, independent domain-expert review, final article page-fit or publication-release acceptance.

## Acceptance disposition

#33/P08 remains open. The complete atlas still fails readability at 170 mm; the selected figure does not replace that fact. Full scoped pattern/antipattern analysis, native-editor import/export, final article integration/author review and #55 release binding remain unmet. Candidate caption feeds #53, and the evidence table feeds #32/#34. No gate is waived.

Reviewable deliverables: **4/4 implemented**. Selected-figure scope: **9/47 concepts, 8/40 relation decisions**; omitted from this panel only: **38 concepts, 32 decisions**. Negative controls: **7/7 rejected**. Accepted package denominator stays **3/19** and bounded requirement evidence **28/90**; these are not scientific-quality or paper-readiness scores.

Next authorized batch after verified integration: #126's SQL-independent bounded metrics, reusing existing pilots and declaring formulas/denominators before calculation. No external review outreach or runtime/orchestrator work.
