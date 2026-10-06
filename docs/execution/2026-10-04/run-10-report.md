# Run 10: current formal-reference synchronization

Baseline: `b2047f6eb72dc2253e7536644573cfd4929ad5fa`. Target candidate: **0.2.0-rc.4**. This batch does not change any ontology, SHACL, query, frozen release, relational schema or source dataset. #125 is explicitly deferred by the author; no SQL parity work is performed.

## Delivered scope

- Current `docs/formal/formal-ontology-description-rc4.md`: all FD-A–FD-J dimensions, actual selected commitments, readable Exposure example, explicit OWL/SHACL/query/SQL/governance separation, historical versus current evidence.
- Complete deterministic generated source projection: seven local modules plus vendored gUFO; **1,618 unique asserted triples**; **116 locally declared terms** (46 classes, 50 object properties, eight datatype properties, one annotation property, seven named individuals, four markers). Helpers and 47 conceptual / 40 relation rows have distinct denominators.
- Cumulative migration/consumer matrix. Unknown scale parents/content, scenario review, optional grounding and deployment limitations remain explicit.
- Source hashes, Git blob identities, full canonical graph and path-triggered reproduction/semantic CI. Historical P1-R2 reference/generator is preserved.

## Verification

Local pinned RDFLib 7.6.0 / PySHACL 0.40.1:

- Deterministic generation and all ten documented dimensions checked.
- **9/9 deliberate corruptions rejected**: inventory, missing FD section, unbound/escaping imports, missing module, changed axiom, removed metadata declaration, shape drift and CQ drift.
- Original P1-R2 local-reference and generated-closure checks pass unchanged (76 declarations / 1,409 asserted triples), separately from rc.4.
- rc.4 exposure-scale source manifest passes; bounded rc.4 behavioral suite **31/31**, including **17 negative cases**. Its embedded old-suite call executes the frozen rc.3 tests against rc.3; it is not 31 additional current-candidate guarantees.
- Exact-head reasoner and CI outcome must be read from the PR and subsequent readback evidence, not inferred from this report. The workflow executes four actual type entailments, two satisfiable countermodels and two expected category inconsistencies using the pinned ROBOT/HermiT toolchain.

The tests are synthetic verification. They are not independent domain validation, a full CQ/SQL equivalence rerun or full OntoUML conformance.

## Acceptance and downstream gates

#124/P07's formal-source/reference/migration work is implemented for review. Final acceptance requires the checked exact head, independent review and merged-main readback. Its stale residual list is replaced with precise current acceptance conditions; the already implemented rc.3 semantic choices are not reopened.

#115 remains open even after this internal bundle because its issue retains source→generated→Wiki/Pages parity (#117) and final scholarly-release binding (#55). No license, semantic, review, manuscript or submission gate is waived. P06's broader diagram conformance acceptance is separate and has not been silently marked complete.

Package baseline remains **3/19 accepted** and author requirement evidence **28/90** until a verified acceptance update. Documentation coverage is **10/10 dimensions**, not a scientific-quality or article-readiness score. Current batch reviewable deliverables: **5/5 implemented** (curated reference, generated projection, cumulative migration, verification tools, path-triggered workflow); publication/CI acceptance is separate.

Next eligible batch after verified integration: #33 publication diagrams and tables; preserve the full-atlas 170 mm readability failure until genuinely fixed. No arbitrary time stop and no external-review outreach.
