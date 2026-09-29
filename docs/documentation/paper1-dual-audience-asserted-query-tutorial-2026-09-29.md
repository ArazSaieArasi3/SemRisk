# Reader exercise: Scenario, Event and `realizedAs` in the P1-R2 source

**Issue:** #122; **state:** executable source-level exercise checked locally, private-Wiki reader task **NOT_EXECUTED**. **Semantic input:** P1-R2 / 0.1.0-rc.1 candidate, six local modules plus pinned gUFO import. The [asserted-closure manifest](../ontology/generated/p1-r2-closure-manifest.json) fixes seven source Git blobs and graph SHA-256 `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`; the Core blob is `cf20fe78687a4db4dcffc21e75297f6801cc5cb4`. This exercise reads those exact bytes, even if the checkout's documentation commit changes. Python standard library suffices for this lookup.

## Choose a route

| Reader | Starting route in the eight-page private Wiki | Question to answer before running code |
| --- | --- | --- |
| Academic/domain reviewer | Home → Scope and Contributions → Semantic Architecture → Formal Reference → Evidence and VVEAA | What is the claimed Scenario/Event distinction, and which evidence supports only the formal source assertion rather than domain-semantic validity? |
| Ontology/data engineer | Home → Semantic Architecture → Formal Reference → Relational Projection → Reproduce and Release | Which canonical IDs/IRIs, Core file and asserted `realizedAs` signature should an implementation trace? Why is OWL domain/range different from SQL FK completeness? |

The route names are [source-controlled pages](../wiki/pages/Home.md) with an earlier [8/8 private-Wiki read-back](../wiki/p1-r2-live-wiki-readback-2026-09-26.md). This exercise has **not** been navigated from a live signed-in Wiki session or observed with a target reader. The [diagram README](../ontology/diagrams/README.md) describes the zoomable atlas and relation map as source-derived views; a graph edge or label alone is not an axiom, OntoUML stereotype, cardinality or realized event.

## Exact-source task

From a checkout containing the [closure manifest](../ontology/generated/p1-r2-closure-manifest.json), [N-Triples graph](../ontology/generated/p1-r2-asserted-closure.nt), [formal inventory](../ontology/p1-r2-formal-source-entity-reference-v0.1.csv) and six local ontology modules, run:

```bash
python tools/paper1_reader_asserted_query.py
```

The [script](../../tools/paper1_reader_asserted_query.py) first checks the Core Git blob, graph SHA-256, 1,409 unique asserted triples, and inventory source binding. It then checks that `SR-CPT-006` Risk Scenario and `SR-CPT-007` Risk Event are locally declared Core OWL classes with an explicit `owl:disjointWith` assertion, and that `SR-REL-003` `realizedAs` is an object property with asserted Scenario domain and Event range. Expected terminal summary:

```text
SEM_RISK_READER_ASSERTED_QUERY_PASS | P1-R2/0.1.0-rc.1; 7 files; 1,409 asserted triples
SR-CPT-006 Risk Scenario and SR-CPT-007 Risk Event: local Core OWL classes; explicit disjointWith
SR-REL-003 realizedAs: asserted domain Scenario, range Event; source ontology/core/semrisk-core-v0.1.0-rc.1.ttl
BOUNDARY: asserted source lookup only; no inferred closure, domain validation, cardinality or occurrence claim
```

**Observed preflight, 2026-09-29:** Python 3.12.14 in a local shell, against a checkout whose four exercise inputs have the exact manifest/inventory/Core/graph blobs above: command returned those four lines with exit code 0. A controlled appended Core comment was rejected with `Core source blob drift`. This checks a source query and integrity guard. It neither reruns OWL reasoning nor proves the distinction is useful or correct to independent readers.

## Reader observation record still needed

At the exact private Wiki revision, record participant role and prior SemRisk familiarity, entry URL, browser/device and viewport, keyboard or assistive mode, each destination opened, whether the source and formal link were found without prompting, the command and result, explanation of asserted versus inferred semantics, confusion, prompts, errors, and `PASS/PARTIAL/FAIL`. Repeat the route on desktop and a phone-sized viewport; a keyboard-only observation is separate from a named/versioned screen-reader observation. No such reader or assistive-technology result is reported here.

**Escalation:** a missing live route or stale status belongs to #121/#122 Wiki source/publication parity; diagram interpretation to #122; WebVOWL-specific readability and T1–T4 to #119; Pages visibility and cross-surface deployment to #117/#55/#56; semantic-definition changes through Core governance, never by editing the tutorial alone.
