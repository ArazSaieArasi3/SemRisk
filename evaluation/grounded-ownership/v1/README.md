# Opt-in validation-first ownership entrypoint v1

This is a separately versioned application guard for the existing **GroundedRiskResponsibility** contract. It preserves every frozen rc.4 ontology/profile/query byte and does not require legacy records to become grounded.

It addresses the [observed permissive class-token case](../../antipatterns/0.2.0-rc.4/behavioral/README.md) within the stricter selected workflow. The old profile/query still retain their documented limitation. **Full FAP-006 remains NOT_ESTABLISHED**; no real-world actor identity or authority is certified.

## What is required

- Each selected assignment explicitly has both `ac:GroundedRiskResponsibility` and `sr:SR-CPT-031` types. No hidden subclass inference is assumed.
- The existing temporal and optional-grounding constraints are copied unchanged and targeted only at those opted assignment nodes. Unrelated profile targets are inactive.
- Assignees have Endurant evidence, are themselves mediated by the assignment, and have the existing explicitly distinct mediated counterpart evidence. Risk remains an aboutness target, not an invented participant.
- The complete supplied data graph, including non-opted records, must pass OWL 2 DL and actual HermiT consistency before any applicable validated result.
- Caller time is explicit and timezone-aware in the supported lexical form. Unknown assignment starts are reported and excluded from as-of answers.
- Data are read from a local Turtle file. Data-level `owl:imports` are rejected before reasoning; no user model is sent to an external verification service.

The new local constraint follows the already adopted participant-side meaning of SR-REL-028. No actor kind, external actor registry or new canonical ontology class is introduced. An `owl:Class` declaration alone is not blacklisted: OWL punning can be legitimate. The known RoleMixin falsely asserted as an Endurant instead fails the pinned gUFO Type/Individual consistency boundary.

## Use

Use Python 3.12, RDFLib 7.6.0, PySHACL 0.40.1 and pinned ROBOT 1.9.10 / HermiT 1.4.5.456.

```
python tools/query_grounded_owners_v1.py \
  --data evaluation/grounded-ownership/v1/positive.ttl \
  --as-of 2026-10-05T00:00:00Z \
  --robot /path/to/robot.jar
```

The ROBOT SHA256 must be `16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105`.

By default diagnostic files use a temporary directory that is cleaned after the command. To retain local diagnostics, supply an empty `--work-dir`. The standalone query file is an unchecked projection if executed directly; validated results require this entrypoint.

### Result contract

- `VALIDATED_QUERY_RESULT`: owner pairs are returned only after input, scoped SHACL, OWL-profile and consistency success. The response states opted/legacy counts and unknown-start assignments. Empty answers mean no qualifying explicit answer in this supplied graph at this instant, not universal absence of owners.
- `VALIDATION_FAILED`: explicit failure stage/code and **no owners field**. Shape, tool or consistency errors cannot become a misleading empty successful result.
- `NOT_APPLICABLE`: no opted assignments; consistency is explicitly **NOT_ASSESSED**, with no owners field. A legacy-only graph is never labeled grounded or consistent by this early response.

Non-opted records are excluded from grounding shape targets and ownership results. Application-level incompleteness in those records is not silently called valid; logically inconsistent non-opted data still blocks an applicable whole-graph result.

## Executed evidence and limits

The [protocol](protocol.json), exact new shape/query and synthetic fixture were committed at `233add41aa5776017842089d30f5899c0334bcce` before execution. Its frozen checkpoint status is historical. Protocol SHA256: `337459943ef5c1b12eb0cd4be106ef3336ea379e90fa2fda0ef377b7bcbde505`.

[Results](results.json): **39 checks, including 20 negative controls**. Three additional mocked tool failures are clearly separate software error-path controls, not formal verdicts. Actual reasoning covers eight consistent applicable cases and three genuine inconsistencies. Tests exercise complete risk/actor tuples, co-owners, temporal boundaries, benign punning, missing mediation/type/distinctness, class-token/event misuse, mixed legacy scope, input imports and actual CLI success/failure.

The isolated membership test shows the earlier optional shapes conform while the new participant-membership constraint rejects the deficient assignment. The bare known RoleMixin token is rejected by participant validation; falsely adding Endurant typing is rejected by actual reasoning. The ownership-query execution spy verifies no ownership SELECT runs on failure.

The workflow is configured to retain synthetic input worlds, shape/DL reports, tool logs and CLI responses after execution. Exact-head CI/artifact readback and independent review are required before merged integration. Generated reasoning headers are not canonical release/license metadata.

This does not establish actual personal/organizational identity, legitimate authority, an exhaustive actor taxonomy, universal ownership completeness or complete antipattern safety. Mandatory grounding for every legacy assignment or adoption of an authoritative actor registry remains a separate scientific/data decision.
