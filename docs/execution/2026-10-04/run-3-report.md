# Run 3 — method, conceptual closure and temporal prototype

Baseline: `b8a321baaff2534d6594d80d23402c6e8046e94a`. Date: 2026-10-05.

## Delivered artifacts

| Work | Evidence | Result and limit |
|---|---|---|
| Actual design method | `method/paper1-engineering-method-v1.1.md`; SABiO and author-paper crosswalks | OGCM-RF retained; five development/five support mappings; real Commentium/CM4DI method/evaluation sections inspected; no transfer of their results |
| Concept/domain decisions | `conceptualization/revision-2026-10-05/` | 47 dispositions; twelve portfolio scopes plus Method; 12/10/6 counts distinguished |
| Restricted-input use audit | `evaluation/integrity/derived-field-use-audit-2026-10-05.*` | 27 dispositions tied to authorized derived vocabulary; no raw private record values released |
| State/time/extension prototype | `evaluation/core-contract/2026-10-05/` | 18/18 tests, including seven rejected invalid cases; separate prototype namespace and explicit promotion gates |
| Old foundational PR disposition | `foundational/legacy-pr-58-61-*2026-10-05.*` | 32+39 source rows individually routed; five retained state probes executed; PRs can be superseded without losing open obligations |
| Traceability audit | `tools/check_run3_traceability.py`; result JSON | 20 requirements/40 CQs/66 links valid; all method artifact references exist; not semantic-adequacy proof |
| Execution controls | requirements, package contracts, next-step prompts | 90 routed; nine individually reverified; three bounded package contracts accepted |
| Publication check | `run-3-readback.json` when present | Exact file/issue readback, current CI and actual PR states; no merge inferred from local files |

Reproduce from repository root:
```bash
python -m pip install rdflib==7.6.0
python tools/check_run3_core_contract.py
python tools/check_run3_traceability.py
python docs/execution/2026-10-04/validate_register.py
```

## Decisions that prevent overclaiming

The current risk-state registry contained an administrative escalation example; it is corrected to match the existing situation/workflow distinction. That correction does not redefine canonical OWL. Result context separates assessed time, reference time, dimension, control baseline, observation/projection basis, scale and method version in a tested companion. Owner-at-time retrieval uses a half-open interval and excludes unknown starts; it does not claim that the older absence-of-invalidation shortcut handled future assignments. The extension test shows preservation of four specific answers, not a general conservative-extension theorem.

The private source audit is an audit of 27 already-authorized extracted fields and current representation. It cannot establish complete use of a private original that was not reimported. The native single `result_kind` axis cannot fully preserve residual likelihood versus residual impact; this remains explicit P10 work.

## Unresolved findings and next batch

1. Synchronize Trigger's broad current definition with the event-role decision; review Confidence/Indicator/Threshold categories without forced stereotypes.
2. Promote the chosen time/context/scale design with qualified SHACL, native SQL migration and RDF/SQL parity. Preserve source version and history; do not retrofit synthetic scores into empirical claims.
3. Finish the category inventory (current foundational table has 33 rows) and genuine editable OntoUML coverage; current 47 dispositions are not 47 validated stereotypes.
4. Complete requirement 3.7's original-reference audit for all final UFO/OntoUML/tool claims and P04's publication clause/privacy scan.
5. Execute P09 literature extraction and obtain real P12 review only through authorized contact. Final manuscript, Wiki/Pages/viewer synchronization, Word/PDF and release gates remain downstream.

Run checklist has eight rows above; rows seven/eight require remote readback before reporting 8/8. Equal-package progress is 3/19 (15.8%), not a claim that this revision took 15.8% of its final effort. Seven readable IEEE pages and an absolute eight-page cap remain unchanged.
