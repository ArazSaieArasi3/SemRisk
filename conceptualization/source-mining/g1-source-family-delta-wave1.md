# G1 Source-Family Delta Summary — Wave 1

**Date:** 2026-09-22

| Source family | Unique contribution to reconciliation | Core impact | Profile/method impact |
|---|---|---|---|
| SRC-OP-001 Jira operational schema | record/workflow fields, inherent/residual values, owner/identifying units, response/treatment fields, operational taxonomies | exposes Risk vs Record, Assessment vs Result, Risk State vs Workflow State | Enterprise taxonomy/method/data mappings |
| SRC-PA-001 Integrated GRC | Risk, control, objective, monitoring, process linkage, evidence | provides governance/control/objective relation candidates | Governance/Enterprise profile |
| SRC-PH-001 Pharma supply-risk review | broad Pharma supply/finance/market/organizational risk factors and affected process/capability | supports generic context/exposure patterns but not Core classes by frequency | Pharma/SupplyChain/Enterprise profile |
| SRC-PH-004 PESTELI expert evidence | context drivers, management strategies, expert evidence, provenance | supports Evidence/Context/Treatment patterns | Pharma/Health/Governance profile and method |
| SRC-PH-005 cross-national shortage study | shortage phenomenon vs records, jurisdictions, recurrence, evidence bias, causal/generalizability constraints, provenance | strengthens phenomenon/record/evidence/provenance and causation-vs-association distinctions | Pharma/Health profile + dataset/method semantics |

## Cross-family conclusion
No single source family is sufficient to define the Core. Operational data contributes workflow/record semantics; foundational/comparator evidence constrains ontology identity; GRC contributes governance relations; Pharma sources supply domain stress tests and evidence/provenance distinctions. This supports a federated Core/profile architecture rather than a source-dominant ontology.