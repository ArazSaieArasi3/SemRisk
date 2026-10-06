# Finite synthetic rc.4 pharmaceutical extension compatibility

Requirement: **1.9**, P06/#123 (a dependency of formal synchronization #124). This is a new current-candidate experiment; the historical six-module extension result is not promoted.

## Predeclared question and protocol

At an explicit time, which recorded synthetic pharmaceutical-supply exposure episode connects the enterprise subject to its designated supply-risk source?

The [protocol](protocol.json), two-class [test-only extension](pharma-extension.ttl), and [domain-filtered query](pharma-exposure-at.rq) were committed as `d05bbc70dfcef77cdecbac345606d9490794f53c` before execution. Protocol SHA256: `c56e87d36673b80581f94ea11c0aafe170fd37d0ad7a5a4540cf7433ecab885d`. Its PREDECLARED_NOT_EXECUTED field records that frozen checkpoint, not the later result status. The runner rejects protocol drift.

The extension introduces exactly two fresh test-namespace classes and their forward subclass axioms, without a new foundational stereotype, CM-PharmE equivalence or canonical vocabulary promotion. The complete current fixture receives exactly three additional type assertions; every baseline triple is retained. The question concerns hypothetical episodes, not an observed pharmaceutical shortage or treatment effect.

## Executed bounded result

[Results](results.json): **44/44 checks**, including **16 negative controls**. Actual HermiT evaluates five consistent worlds and one genuinely inconsistent instantiated specialization; all six worlds pass OWL 2 DL profile checks first. Strict current SHACL composition conforms for baseline and extended complete fixtures with inference=none and MetaSHACL enabled.

- Before, boundary, after and equivalent-timezone queries preserve exact full core tuples and answer the domain-filtered question. Unbound time returns no answers.
- Separate fresh subtype-only witnesses have no explicit parent types or endpoint domain/range backdoor. Actual inherited type assertions disappear when their respective subclass axiom is removed.
- A shape-valid interval mutation changes the expected answer; removing domain-source typing loses the domain-specific answer.
- Exact extension allowlisting rejects Core redefinition, reverse subclassing, equivalence in either direction, keys, functionality and property chains.
- An instantiated PharmaceuticalExposure additionally constrained as gUFO QualityValue passes syntax/profile checks but produces actual HermiT inconsistency.
- Four inherited core types and **35 finite baseline-individual/current-class assertion pairs** are preserved. Extension classes and witnesses are excluded from that fixed projection.
- All eight ontology closure files remain byte-identical. The canonical inventory stays **47 concepts / 40 relations / 116 declarations**; the two test classes are counted separately.

The runner retains raw reasoning worlds, profile reports, logs, exact before/after projection pairs and actual runtime versions locally. The workflow is configured to upload those files after execution; an actual CI artifact readback is required before acceptance. The checked-in results bind the protocol and finite projection hashes. Exact-head CI and independent review must match this record before merged-main acceptance.

## Reproduce

Use Python 3.12, RDFLib 7.6.0 and PySHACL 0.40.1. Use ROBOT 1.9.10 with SHA256 `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105` (embedded HermiT 1.4.5.456).

```
python tools/check_rc4_extension.py --robot /path/to/robot.jar
```

The runner writes raw files under `build/extension-rc4/` and compares deterministic results with the committed result. It does not edit canonical ontology, shape, query or historical fixture bytes. `--write` is reserved for an explicitly reviewed result update.

## Acceptance ceiling

A synthetic pharmaceutical extension preserved the declared finite rc.4 invariants and supported the stated as-of scenario under the tested profile.

This is not empirical organizational usability, a general conservative-extension theorem, pharmaceutical domain adequacy, independent transfer, expert validation, full SQL parity or full OntoUML/native-editor acceptance. P06 and dependent whole issues retain their other gates. No manuscript or runtime automation is included.
