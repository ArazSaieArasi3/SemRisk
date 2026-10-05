# SemRisk operational candidate 0.2.0-rc.1

This is the successor **implementation candidate** for the author revision. It is not a stable or publication-bound release. [Manifest](manifest.json) binds the exact component files; test and CI evidence lives in `evaluation/temporal/v0.2.0-rc.1/`.

Six existing semantic modules retain their logical assertions. Version/date metadata changes and the Core Trigger comment is corrected to match its already-existing `gufo:Event` axiom. Enabling conditions stay under Predisposing Condition. A seventh, **operational assessment-context profile**, adds five helper classes, seven controlled individuals and thirteen properties. This does not add a seventh enterprise domain or redefine the 47 conceptual inventory rows. Historical `0.1.0-rc.1` files and evaluation remain frozen and addressable.

The profile separates numeric assessment dimension, control baseline and evidence basis. Each qualified result records assessment time, reference time, a versioned scale and method, its producing assessment and risk identity. New SHACL constraints apply to explicitly qualified input; old incomplete records are not silently backfilled or treated as complete. Responsibility queries require an explicit instant and retain co-owners.

An observation-informed likelihood estimate and a projected likelihood estimate remain different results. Their numeric difference alone is not a treatment effect. An immutable scale IRI denotes one scale version; changed bounds require a new IRI/version. Qualified historical results, their activities, methods and scales cannot be overwritten through the projection. Corrections create successor results.

This profile is deliberately bounded to numeric scales and one reference instant. Ordinal scales, prediction windows, uncertainty distributions, arbitrary score comparability and concurrent enterprise workload assurance need separate profiles/tests. The full OntoUML model, real literature case, real expert validation and final seven-page manuscript remain downstream.

Reproduce:
```bash
python -m pip install -r tools/requirements-qualified-context.txt
python tools/build_qualified_context_manifest.py --check --assemble
python tools/check_qualified_context.py
```
The `paper1-qualified-context.yml` workflow additionally performs PostgreSQL migration/round-trip/negative tests and OWL 2 DL/HermiT checks. Its actual status is authoritative; parsing Turtle alone is not a formal PASS.
