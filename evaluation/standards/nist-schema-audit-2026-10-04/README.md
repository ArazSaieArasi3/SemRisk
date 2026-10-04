# NIST register/detail source audit

The official IR 8286 Rev.1 final page, dated 18 December 2025, supplies RR schema v2 and RDR schema v3. The frozen JSON here is **normalized from the retrieved official web rendering** on 2026-10-04; formatting and line wrapping were normalized. Its hash is not a hash of the original server bytes. Source URLs are retained in the field inventory. No private workbook values are reproduced.

RR defines 11 fields, all listed as required. RDR defines 34 fields; its required array contains 33 names, including `currentRiskAnalysis`, which has no matching `properties` definition. `plannedRiskResponse` and `comments` are defined but not required. This does **not** make the source schema invalid: additional properties are permitted by default. It makes the required analysis field underspecified for mapping. Do not silently supply its type, rename it or delete it from the source record.

The inventory contains 46 dispositions: 45 defined properties plus one required-only name. Coverage means every source field/name has a disposition, **not** that SemRisk implements every source field. Types and requiredness remain source-schema facts; ontology cardinalities require a separate semantic decision. The planned/expected/actual result distinction, rating-versus-exposure ambiguity, and contact-versus-accountable-owner ambiguity are explicit P06/P10 handoffs.

These public sources corroborate design decisions independently of the restricted source's availability; they do not rewrite the actual design provenance or make design evidence an independent test set. Run `python tools/check_revision_source_audit.py` for inventory and protocol checks.
