# SemRisk P1-R2: bounded OQuaRE structural pilot

**Status:** executed, raw structural subset only. Exact SemRisk semantic source ref `c17cc111f02309270a60474623259cefcf907c6f`; candidate `0.1.0-rc.1`. The input is the seven-file catalog-resolved **asserted** closure in `docs/ontology/generated/p1-r2-asserted-closure.nt`, SHA-256 `7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a`. The generator verifies this digest and all seven Git blob IDs against `docs/ontology/generated/p1-r2-closure-manifest.json` before measurement. It selects the 35 locally declared SemRisk OWL classes; gUFO contributes to the graph but is excluded from the class denominator. No inferred hierarchy is measured.

## Method and exact tools

- **OQuaRE framework:** structural metrics TMOnto and ANOnto, with definitions/bands read from `tecnomod-um/oquare@3c870b504c799bfb7598912d1b29cab7f44d12ac`, `oquare_docs/quality_metrics.md`. This is the scoring framework, not the SemRisk ontology.
- **Local tool:** `tools/pilot_oquare_structural.py` using RDFLib `7.6.0`. It implements the two declared formulas independently; the upstream `tecnomod-um/oquare-metrics` Java/GitHub Action at tag `v3.0` (`89627d32e41deafc69945f7062dbd5131defec70`) was **not executed**. Its documented GitHub Action mode writes into the repository and is not an offline local engine. No QASAR service or external ontology upload was used.
- **OQUO representation:** `tecnomod-um/oquo@a43fe72aabe2bbff0b2d10cebd67e89c8049c9ff` example `oquo-qasar/examples/go_oquare_eval_with_scales.ttl` supplies the Measurement, Observation, Evaluation, QualityValue, metric and scale terms. The local `.nt` adapter contains two **raw** baseline measurements. This RDF vocabulary represents results; it is neither a metric implementation nor SemRisk's semantic source. We parse the generated RDF locally; full OQUO SHACL conformance and QASAR ingestion remain untested.

Reproduce from the repository root with Python and `rdflib==7.6.0`:

```sh
python tools/pilot_oquare_structural.py --check
```

To regenerate intentionally, omit `--check`. The command compares both committed generated files byte for byte. Input source blobs, closure digest, local class count and fixture restoration are asserted by the script.

| Condition | Local classes | Multiple named direct parents | TMOnto raw = count / (35 − 1) | Published TMOnto band | ANOnto raw = label/comment assertions / 35 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Exact asserted baseline | 35 | 0 | 0 | 5 | 70/35 = 2 |
| Safe in-memory annotation: add one explanatory `rdfs:comment` | 35 | 0 | 0 | 5 | 71/35 ≈ 2.02857 |
| Deliberate in-memory tangle: add a second named direct parent | 35 | 1 | 1/34 ≈ 0.02941 | 5 | 70/35 = 2 |

Both mutations are removed before exit; the graph returns to 1,409 asserted triples. The extra parent is an **adverse structural diagnostic**, not a demonstrated logical inconsistency: multiple inheritance can be justified. The raw TMOnto measure detects one extra parent while its 1–5 band stays at 5. A score of 5 is therefore no validation of risk semantics. The published ANOnto percentage band does not map cleanly to the observed mean of two label/comment assertions per class; its scale is left **NOT_ASSESSED**, with no fabricated score. The other OQuaRE metrics and their applicability are **NOT_ASSESSED** in this two-metric pilot.

## Added value and boundary

The existing semantic CI tests RDF syntax, OWL 2 DL/HermiT reasoning, SHACL fixtures and traceability; this pilot adds a version-bound hierarchy/annotation measurement and a concrete example of score insensitivity. It does not repeat or replace formal verification, and neither the raw counts nor an OQuaRE band establish ontology quality, domain validity or comparative superiority. The structured results are `p1-r2-structural-pilot-v0.1.json` and `p1-r2-structural-pilot-v0.1.nt`. #33/#34 may cite only the bounded raw experiment after their own release-bound review.
