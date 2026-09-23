# SemRisk deterministic semantic build

This pipeline implements issue #44 for the P1-R2 candidate.

## Local execution

Requirements:
- Python 3.13
- `rdflib==7.6.0`
- `pyshacl==0.40.1`
- Java 17
- ROBOT 1.9.10 jar with SHA-256 `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`

Run the lightweight deterministic checks:

```bash
python -m pip install -r tools/requirements-semantic-ci.txt
python tools/semrisk_semantic_ci.py --stage pre
```

Then assemble/profile-check/reason using the exact commands in `.github/workflows/semantic-ci.yml`; finally:

```bash
python tools/semrisk_semantic_ci.py --stage post --reasoned build/semantic-ci/reasoned.owl
```

## Evidence semantics

Statuses are `PASS`, `FAIL`, `WARNING`, `ERROR`, `UNSUPPORTED`, `NOT_RUN`, or `N-A`. Missing execution is never converted to PASS.

A green run proves only the declared reproducible verification checks. It does **not** establish semantic/domain validity, expert agreement, transferability or overall ontology quality.

## Action-minutes discipline

Heavy semantic CI is path-filtered. Documentation-only changes outside governed semantic paths do not run this workflow. Any change to ontology, shapes, rules, formalization/foundational decisions, G2 architecture or semantic identity does run the full validation chain; validation depth is not reduced to save execution minutes.
