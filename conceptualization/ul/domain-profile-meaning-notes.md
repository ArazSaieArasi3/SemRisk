# SemRisk Ubiquitous Language — Domain and Profile Meaning Notes

**Status:** W2 candidate vocabulary; noncanonical until #24 G2.

## Scope rules

1. **Core** terms express cross-domain semantic patterns only when G1 evidence supports a reusable distinction.
2. **Enterprise** terms cover registers, workflows, governance and architecture context; they do not redefine external business/process ontologies.
3. **Pharma** terms are profile mappings/federation targets; CM-PharmE remains semantic owner of pharmaceutical ecosystem entities.
4. **Health** terms such as Hazard/Harm may use safety/medical-device meanings and are not silently generalized to all domains.
5. **Governance** terms such as Risk Appetite, Risk Tolerance, Risk Criteria and Policy retain framework-specific definitions when materially different.
6. **Method** terms own scales, thresholds, formulas and assessment techniques; method values are not promoted to Core classes.
7. **Data/Product** terms own fields, dropdown values, workflow statuses, dashboards and serialization/UI artifacts.

## Meaning notes by high-risk term

### Threat
In security profiles a Threat may be an actor/action/source of adverse effects. In generic ERM sources, threat may simply denote negative risk framing. SemRisk therefore does not equate Threat with Risk; exact foundational category remains open for #3/#25.

### Hazard
In medical-device/safety usage, Hazard is a potential source of Harm and participates in hazardous situations. This usage is preserved in Health/Safety profile semantics and is not imposed on finance, enterprise or Pharma supply-chain contexts.

### Vulnerability
Security sources emphasize weakness/susceptibility; supply-chain sources emphasize structural susceptibility; health sources may use predisposing conditions. The preferred Core/Profile candidate is deliberately broad, with domain refinements required.

### Exposure
Financial exposure, physical exposure, vulnerability exposure and an exposure rating are different meanings. No single label-equivalence is asserted. Assessment scores remain Method; real-world exposure relations/qualities remain profile candidates.

### Risk Appetite / Risk Tolerance / Risk Criteria
These are Governance/Method concepts. They remain separate because standards/frameworks use them with different decision and threshold semantics. They are not intrinsic properties of a Risk phenomenon.

### Signal
Detailed pharmacovigilance Signal semantics remain Pharma/profile-owned and must align with OpenPVSignal/PV sources. Signal is not synonymous with Evidence, Event or Risk.

### Issue / Incident
`Issue` is a Governance/Enterprise problem concept; `Incident` is a realized occurrence. Their Jira/ticket representations are product information artifacts and are treated separately.

## Naming convention

SemRisk module/domain labels must not contain `and` or `&`. Current governed scope labels are single semantic names such as `Core`, `Enterprise`, `Governance`, `Pharma`, `Health`, `Method`, `Data`, `Architecture`, `SupplyChain` and `Environment`.

## Canonicalization rule

Preferred UL labels reduce communication ambiguity only. They do not establish OWL classes, UFO stereotypes, identity criteria, subclassing or equivalence. Those decisions belong to #3/#20/#21/#25 and G2.