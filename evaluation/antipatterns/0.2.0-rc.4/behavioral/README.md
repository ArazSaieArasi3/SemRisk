# Selected current behavioral and category-preservation probes

This companion executes previously unassessed portions of FAP-006, FAP-012, FAP-013 and FAP-014. It does not replace the [asserted-source subset](../README.md) or establish full OntoUML/UFO conformance. **All 15 full-antipattern verdicts remain NOT_ESTABLISHED.**

The [protocol](protocol.json) was committed as `829c94b9f080347539ce06f5d2e97d327539f72c` before execution. Its frozen checkpoint status is historical. Protocol SHA256: `4b053d8107d62a1952a5aaddff5603a001171151032b58a5a4cd25b016882fa5`.

## Actual selected results

[Results](results.json): **50 passing checks, including 25 rejection controls**, plus one separately recorded adverse observation. Nine worlds passed OWL 2 DL validation before actual HermiT reasoning: four consistent countermodels and five genuine inconsistent controls. These totals measure this test suite, not detector sensitivity, ontology quality or domain truth.

- **FAP-006:** the exact ownership query preserves expected temporal/co-owner pairs, ignores primitive owner assertions and mediation counterparts, and rejects missing assignment evidence through the expected answer oracle. Duplicate paths do not duplicate answers. Only the ownership subgraph is used; historical scale fixtures are not silently treated as rc.4 compliant.
- **FAP-012:** a zero-endpoint Exposure world and a two-distinct-subject world are OWL-consistent. Their strict profile data fail only the predeclared focus/path/component constraints (two MinCount violations and one MaxCount violation respectively). Injected global existence/functionality produces actual inconsistency. This demonstrates the selected endpoint boundary, not every cardinality policy.
- **FAP-013:** distinct associated Risks and distinct same-Risk states connected by `precedesState` remain consistent with explicit negative `causes` assertions. Injected causal subproperties and a direct causal assertion produce inconsistency. These are actual selected non-entailment countermodels, not an absence-of-triples shortcut or a universal causal-independence claim.
- **FAP-014:** all 12 category-audit rows, 16 bridge decisions and five external marker references match the frozen CM-PharmE v1.0.0 catalog/manifest at commit `5099888668d35f798e4759e3534e707ed906db24`. C0025's relator/mode conflict, unmapped API/product/Objective gaps and reference-only ownership remain explicit. Semantic mutations are tested after input verification; source hash failure is not substituted for a category oracle.

## Adverse assignee observation

The current explicit-data Responsibility shape requires an IRI assignee, not a validated actor category. Replacing an assignee with the known Risk Owner class IRI still conforms, and the query returns that IRI. The raw data, actual answer pairs and shape report are retained by the runner. This is recorded separately as **OBSERVED_LIMITATION**, not as a successful rejection or a universal safety guarantee. The optional grounding profile is a separate contract; these probes do not silently activate it or change the frozen profile.

## Reproduce and inspect

Use Python 3.12, RDFLib 7.6.0, PySHACL 0.40.1, PyYAML 6.0.2 and the repository's pinned ROBOT 1.9.10 / HermiT 1.4.5.456. Supply the two exact external files identified by commit, Git blob and SHA256 in the protocol. Keep them outside the output directory.

```
python tools/check_current_antipattern_behavior.py --robot /path/to/robot.jar --external-inputs /temporary/cmpe-inputs
```

The workflow is configured to fetch those public immutable references into runner-temporary storage and upload only SemRisk proof outputs. It does not vendor or redistribute the external catalog/manifest. The runner retains reasoner worlds/logs/profile reports, focused SHACL reports, ownership observations and runtime versions. Actual exact-head CI artifact verification is required before merged acceptance.

No canonical ontology, shape, query, historical fixture, SQL adapter or manuscript is changed. Native-editor preservation, complete 170 mm readability, full pattern applicability and scholarly release/rights gates remain open. No author requirement or whole issue is accepted merely because this selected suite passes.
