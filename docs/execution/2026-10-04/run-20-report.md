# Run 20 — current finite extension compatibility

Baseline: `577f4921b348fd69e9378bc7a0a767b03276dff3`. [Experiment and limits](../../../evaluation/extension/0.2.0-rc.4/README.md).

The protocol and exact two-class synthetic extension/query were committed before execution at `d05bbc70dfcef77cdecbac345606d9490794f53c`. Independent protocol review fixed the inference oracle to use relation-free subtype witnesses, a fixed finite projection and actual indirect ClassAssertions. The complete current fixture is separately checked under strict SHACL.

The actual local experiment passes 44 checks, including 16 negatives, five consistent reasoner worlds and one actual inconsistent specialization. All six worlds pass OWL 2 DL profile validation. Core as-of answers and the finite 35-pair class-assertion projection remain unchanged. Eight canonical ontology files and the 47/40/116 governed inventories are preserved; two test-only classes are separate.

## Acceptance delta

Requirement **1.9** gains bounded current-candidate evidence: a synthetic pharmaceutical extension preserves the declared finite invariants and answers the predeclared scenario. This is not a universal conservative-extension result or empirical usability claim. Individual requirements become **40/90**; whole packages remain **3/19**. No whole issue closes.

Broader P06/full OntoUML/native-editor/readability, private manuscript and final release/rights gates remain open. #125 and #51 remain deferred. No canonical model, SQL, public manuscript or published-site payload is changed.

Independent exact-head review, CI artifact readback and merged-main verification are required on the batch PR. The final CI receipt must distinguish actual results from this earlier local checkpoint.
