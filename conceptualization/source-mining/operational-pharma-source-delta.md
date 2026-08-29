# Operational ↔ Pharma Source Delta — Preliminary Reconciliation View

**Status:** W1 analytical bridge only — **not** Gate G1 reconciliation and **not** a canonical SemRisk mapping.  
**Sources compared:** `SRC-OP-001` Jira operational risk schema; `SRC-PH-001` Jaberidoost pharmaceutical supply-chain review.  
**Date:** 2026-08-29

## Purpose

This view tests whether independent enterprise-operational and pharmaceutical evidence converges on reusable risk semantics while exposing domain-specific additions. It is deliberately created before canonicalization so we can distinguish:

- recurring cross-source concepts;
- source-specific taxonomies;
- Pharma-specific domain concepts;
- operational risk-management artifacts absent from the Pharma review;
- relation/event patterns that should be prioritized in later reconciliation.

## Cross-source convergence candidates

| Semantic area | Operational source evidence | Pharma source evidence | Preliminary interpretation |
|---|---|---|---|
| Supplier / value-chain exposure | `ریسک تامین کنندگان(زنجیره ارزش)` | supplier failure, supplier partnership, supplier flexibility, delivery reliability, GMP certificate, supplier QMS | Strong cross-source evidence for a reusable **dependency/exposure pattern** plus Pharma-specific supplier properties; not enough to define a Core `SupplierRisk` class |
| Regulatory exposure | `ریسک تغییر قوانین و مقررات`, `ریسک تطبیق`, legal/compliance classifications | regulatory risk, tariff-policy change, supplier GMP certification | Supports Governance/Profile semantics linking requirements/policies/status to risk scenarios; separate regulatory change events from compliance situations |
| Financial exposure | FX, interest rate, liquidity/funding, credit, asset-value and financial-ratio risk terms | currency fluctuation, interest rate, cash flow, tax change, tariffs, supply cost | Strong evidence that SemRisk Core should avoid hard-coding financial taxonomy while allowing Finance-profile exposure/impact patterns |
| Technology / information systems | technology change, information-system/technology risk | information systems, technology level/development | Supports Architecture-profile linkage to systems/capabilities/technology conditions |
| Process / operational conditions | inappropriate processes; operational taxonomy | planning issues, operation issues, organization/process, process development, plant/network design | Supports risk-to-process/capability/design linkage; material for Paper-1 EA contribution |
| Reputation / goodwill | reputational risk | supplier goodwill | Similar labels but different semantic roles/scopes; **do not merge without reconciliation** |
| Environmental context | environmental risk | environmental assessment, waste management | One is risk taxonomy, others are assessment/activity contexts; lexical overlap does not imply equivalent concepts |
| External event/disruption | external events including fraud/natural hazards | supplier failure, customer-service disruption, transportation risk | Supports generic event/disruption pattern but source semantics differ |
| Demand / market | competition/commodity/economic conditions | demand, demand uncertainty, market issues, consumer taste | Enterprise/Market profile candidates; Pharma exposes demand uncertainty and medicine-market specificity |
| Organizational responsibility | risk-identifying unit, risk owner | reviewed literature focuses manufacturing-company perspective and actors implicitly | Operational source is substantially richer for responsibility/record governance; Pharma sources needed for domain actor roles |

## Operational-source semantic contributions currently absent or weak in SRC-PH-001

These should not be interpreted as “SemRisk advantages”; they are **source deltas** requiring corroboration from standards/ontologies/other literature:

1. explicit Risk Register / record artifacts;
2. risk-record title/description/tags;
3. analysis workflow state;
4. management lifecycle `Open → Analyzed → Treated → Closed`;
5. risk owner / owner organizational unit;
6. risk-identifying organizational unit;
7. identification channel/provenance;
8. explicit threat vs opportunity polarity;
9. ordinal impact severity scale;
10. ordinal likelihood scale;
11. explicit `impact × likelihood` inherent/residual scoring method;
12. risk response strategy vocabulary;
13. treatment/response plan and contingency plan;
14. risk identification time versus record creation/update time;
15. inherent versus residual impact/likelihood/result distinction;
16. Assignee versus owner distinction.

These are especially important for the **Enterprise profile** and the paper’s operational validation.

## Pharma-source semantic contributions currently absent or weak in SRC-OP-001

1. medicine accessibility as a Health-system objective/value;
2. medicine quality as an objective/value condition;
3. medicine affordability as an objective/value;
4. raw-material quality;
5. GMP certification status;
6. supply-chain fragmentation;
7. supplier delivery reliability/flexibility;
8. inventory/stock visibility;
9. demand uncertainty;
10. new-drug pipeline uncertainty;
11. counterfeit medicine risk context;
12. capacity–demand mismatch;
13. supply network/plant design conditions;
14. explicit manufacturer-centered Pharma boundary;
15. research gap around risk impact on business processes/functions.

These are important for the **Pharma profile**, **Health bridge**, **SupplyChain profile** and the chosen case.

## High-value candidate bridge patterns emerging

### Pattern A — Dependency exposure

```text
Enterprise / Process / Capability
   depends on
Supplier / Resource / External Actor
   has condition / failure / disruption
→ potential Risk Event / Risk Scenario
→ impact on Objective / Capability / Availability
```

### Pattern B — Assessment context

The operational source provides explicit assessment values, while the Pharma source provides domain conditions/drivers. This reinforces the need to keep:

`Risk Scenario` ≠ `Risk Assessment` ≠ `Assessment Result`.

Domain conditions should be assessed under an explicit method/context rather than assigned timeless scores.

### Pattern C — Governance/control response

Operational evidence provides response strategies/plans and ownership; Pharma evidence provides regulatory/GMP/quality/supplier conditions. Later sources (ICH Q9, COSO/OCEG, ROSE) should determine the correct distinction among:

- policy/requirement;
- control/mechanism;
- treatment strategy;
- treatment plan;
- executed treatment activity;
- responsibility/accountability.

### Pattern D — Pharma availability chain

```text
supplier / production / logistics / regulatory condition
  → disruption / shortage event or situation
  → reduced medicine availability
  → healthcare-delivery impact
  → patient / health-system consequence
```

This is the current preferred Paper-1 case skeleton but causal edges must be source-qualified.

## Conflicts / questions requiring broader W1 evidence

1. `Risk` as threat/opportunity versus COVER's value/risk constructs;
2. risk category versus risk scenario versus risk source/driver;
3. consequence versus impact/harm/value change;
4. supplier failure as event versus vulnerability/condition;
5. shortage as event, state/situation, record, or multiple related entities;
6. regulatory risk as category versus regulatory change event/noncompliance situation;
7. inventory management as activity/capability versus “risk” label;
8. organizational/strategic labels as taxonomies versus ontology classes;
9. how to represent uncertainty independently from likelihood scoring;
10. how Pharma domain entities bridge CM-PharmE without reclassification.

## Gate status

This two-source comparison **does not pass Source Completeness**. Standards, closest ontologies, uploaded papers, qualified datasets, Health evidence and newer Pharma sources still need extraction before Issue #18 can reconcile the Paper-1 claim boundary.
