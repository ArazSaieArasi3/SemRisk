# SRC-ON-005 Qualification — Open Risk Ontology Family

**Source ID:** SRC-ON-005  
**Repository:** `open-risk/risk_management_ontology`  
**W1 bound repository commit:** `e01228b03a13e43827945f1c6f6dc6db98392252`  
**Status:** FAMILY QUALIFIED / NON-CORE BLOCKER

## 1. Member-level qualification

| Member | Bound/version evidence | Primary scope | SemRisk relevance |
|---|---|---|---|
| BMRO | `bmro/bmro.0.1.owl`; versionIRI `/bmro/0.1` | business-model sensitivity to risk | adjacent Enterprise/Profile evidence |
| NPLO | `nplo.0.2/nplo.0.2.ttl`; version 0.2 repository family | non-performing-loan portfolio datasets | financial-risk data/profile evidence |
| DOAM | `doam.0.4/*`; versionIRI `/doam/0.4`; active 0.4.x line | description of risk/predictive models and lifecycle | method/model-documentation comparator |
| CRO | `cro/cro.0.1.xml`; versionIRI `/cro/0.1` | credit ratings production concepts | financial/credit profile evidence |
| RFO | `rfo/rfo.0.1.xml`; public spec revision 0.1 | risk-management roles/functions/skills/reporting context | responsibility/governance adjacent evidence |

## 2. Core-comparator decision

The family is not one general well-founded ontology of the risk phenomenon. Its members specialize business models, NPL data, model descriptions, credit ratings and risk functions. They are relevant to profile/data/governance semantics but do not replace COVER/ROSE or the closest UFO-based risk programme as Core comparators.

## 3. License status

The currently inspected family documentation/repository does not provide a single sufficiently clear family-wide license binding for all member artifacts. License remains `UNRESOLVED_FOR_REUSE` and must be checked member-by-member before import/redistribution.

## 4. W1 consequence

The Open Risk family no longer represents an unqualified hidden novelty threat. Member identities/scopes are known and can be routed selectively. License uncertainty is a reuse-governance issue, not a reason to keep Core-literature search open.

## 5. Routing

- BMRO/RFO → Enterprise/Governance profile evidence;
- NPLO/CRO → financial/credit profile future work;
- DOAM → model/method provenance comparison;
- none enter SemRisk Core automatically.