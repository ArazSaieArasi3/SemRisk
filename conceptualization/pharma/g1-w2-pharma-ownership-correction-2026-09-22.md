# G1/W2 Pharma Ownership Correction Addendum — 2026-09-22

During #5 exact review of the frozen CM-PharmE v1.0.0 catalog, SemRisk found that the earlier G1/W2 working assumption `Active Pharmaceutical Ingredient → CM-PharmE owner` was false.

## Evidence
- CM-PharmE v1.0.0 frozen catalog contains exactly 39 canonical concepts.
- No `Active Pharmaceutical Ingredient`, `API`, `INN`, medicine/product kind, dosage form or product strength concept is present.

## Correction
- Historical G1 extraction remains evidence of the source term and of the earlier reconciliation routing decision.
- Current W2 ownership is `UNMAPPED_EXTERNAL_OWNER_TBD`, explicitly **not** CM-PharmE v1.0.0.
- SemRisk does not mint an ad-hoc Core class to repair the gap.
- DS-004/API-level future mapping must select a governed external terminology owner or preserve unmapped status.

## Impact
The bounded Pharma federation remains viable because Paper-1 federation uses actual v1.0.0 concepts such as Pharmaceutical Enterprise, Enterprise Capability, Pharmaceutical Business Process, Ecosystem Supply Capacity, Supply Chain Relationship, Organizational Stakeholder/Ecosystem Actor and Risk Management Activity.

No G1 search/reconciliation result is invalidated; this is a W2 owner-resolution correction discovered by exact external-catalog inspection.