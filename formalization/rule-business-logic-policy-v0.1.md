# Rule and Business-Logic Policy v0.1

Rules are used only for semantics that are **derived, procedural, temporal, method-specific or application-specific** and are not universal OWL truths.

Each executable rule must declare: rule ID, owning module/profile, inputs, completeness assumptions, method/workflow version, deterministic output, error behavior, provenance, expected positive/negative tests and affected CQs/claims.

Initial rule families:
- derived `hasRiskOwner` from Risk Responsibility assignment;
- method-specific risk-score formula;
- threshold-based classification;
- workflow-transition legality;
- current-state selection from history;
- optional projection/materialization rules.

No rule engine or language is canonically selected in #26. #27/#44 may choose the smallest deterministic technology needed by actual Paper-1 claims.