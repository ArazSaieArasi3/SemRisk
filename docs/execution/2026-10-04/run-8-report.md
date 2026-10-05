Verified CI checkpoint: **all 16 triggered job types passed**. Native Exposure projection: **11/11 tests**, **11 represented triples**, **2 synthetic episodes**. Actual HermiT results: **4 new type entailments**, **2 consistent countermodels**, **2 correctly rejected contradictions**; OWL 2 DL passed. [Exact CI evidence](../../../evaluation/exposure-scale/v0.2.0-rc.4/ci-evidence.json), [readback](run-8-readback.json), [PR #137](https://github.com/ArazSaieArasi3/SemRisk/pull/137). The two targeted decisions are **2/2 implemented and verified**. No broader manuscript/package acceptance is inferred.

# Run 8 — Exposure endpoints and NumericScale identity

Baseline `6d619c5bbcb3532d68e250e2c27a9a3232fd06f9`. New candidate **0.2.0-rc.4**, with seven modules and unchanged historical releases.

## Concrete changes

1. Exposure remains a situation. Two registered properties now link it to its Risk Subject and Risk Source. These correspond to already existing relational columns; they are not added solely to eliminate isolation. No automatic event, consequence, score or causal rule is introduced.
2. NumericScale is an issued scale-specification version, a justified subkind inheriting ArtifactVersion identity. Equal numeric intervals do not equate distinct issued versions. Strict data completeness composes the existing scale and artifact-version shapes; legacy missing parent/content data are not fabricated.
3. Full editable diagram rebuilt: **47/47 concepts, 40/40 registered relation decisions**, 11 helper classes, 15 SVG views and 15-page vector review atlas. All previous 38 relation decisions are retained. New properties and scale inheritance are visible. Minimum A3 review font: **8.52 pt**. The complete atlas remains unsuitable at 170 mm; the separately labeled scenario panel is not the entire ontology.
4. A bounded Exposure RDF/PostgreSQL adapter and native regression test now map existing endpoint and temporal fields without a schema migration. Scale/content/workflow relational parity remains #125; old temporal parity is not relabeled as full rc.4 coverage.

## Evidence and verification

[Acceptance contract](../../../evaluation/exposure-scale/v0.2.0-rc.4/acceptance-contract.md) was fixed before implementation. [Design decisions and sources](../../../foundational/exposure-scale-v0.2.0-rc.4/decisions.md), [behavioral results](../../../evaluation/exposure-scale/v0.2.0-rc.4/results.json), [diagram checks](../../../diagrams/ontouml/0.2.0-rc.4/validation-results.json), [source manifest](../../../ontology/releases/0.2.0-rc.4/manifest.json).

Local: **31/31 behavioral checks**, including **17 expected corrupt-data rejections** and a nested unchanged **31/31 rc.3 regression**; **16/16 diagram checks**, including six corruption controls. Fifteen rendered pages inspected. The two test suites have separate scopes; their counts are not a quality score or number of competency questions.

The workflow executes actual OWL 2 DL/HermiT with four new type entailments, two consistent countermodels and two contradictions that must be rejected. It also runs native PostgreSQL parity and an independent diagram rebuild. Their actual outcomes and exact tested commit are recorded in the Run 8 CI/readback checkpoint after execution; this report does not claim a planned run passed.

## Progress and boundaries

The two targeted semantic gaps are implemented and locally checked (**2/2**); formal/native publication evidence is a separate final gate. Complete packages remain **3/19 = 15.8%**, requirements **22/90 = 24.4%** at their bounded evidence scopes, with **90/90 routed**. Existing requirements gain stronger evidence; no percentage is raised merely by adding relations or splitting tasks.

No new real pharmaceutical case records, expert responses, final Word/PDF manuscript, native-editor round-trip or complete antipattern result were created. Full Figure 1/article integration remains open. The manuscript target is seven IEEE pages, absolute cap eight including references.

## Next concrete batch

Prioritize execution of the already prepared P09 literature-case extraction and source-to-record mapping. In the same bounded follow-up, synchronize the remaining rc.3/rc.4 helper SQL/formal reference requirements. Reuse the current diagram and decisions; do not restart broad ontology design or source searches. Keep native-editor/full pattern checks and final article layout as explicit downstream gates. The author is not needed for routine execution; genuine expert responses still require actual people and authorized contact.
