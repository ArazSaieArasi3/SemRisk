# SemRisk G2 Dependency Diagram

```mermaid
flowchart TD
  CORE[Core]
  ENT[Enterprise]
  ARCH[Architecture Mapping]
  METHOD[Method Profile]
  GOV[Governance Profile]
  PHARMA[Pharma Profile]
  HEALTH[Health Profile - Deferred]
  MAP[External Mappings]
  DATA[Data Projection]
  RI[Risk Intelligence - Deferred]
  COVER[COVER / ROSE / PROV-O]
  CMPE[CM-PharmE v1.0.0]
  EA[External Enterprise / EA Semantics]

  ENT --> CORE
  ARCH --> CORE
  ARCH --> ENT
  METHOD --> CORE
  GOV --> CORE
  PHARMA --> CORE
  HEALTH --> CORE
  MAP --> CORE
  MAP --> COVER
  PHARMA --> CMPE
  ARCH --> EA
  DATA --> CORE
  DATA --> ENT
  DATA --> PHARMA
  RI --> CORE
  RI --> PHARMA
```

## Direction rule
Arrows mean `depends on / references`. No profile, external owner, database or application is allowed to define Core identity.

## Paper-1 active path
`Core → Enterprise/Architecture support → Pharma bounded profile → later DataProjection/evaluation`.

Health and RiskIntelligence are explicit deferred branches.