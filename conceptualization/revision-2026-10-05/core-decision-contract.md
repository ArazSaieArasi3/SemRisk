> **Run 4 update:** the selected Trigger definition and numeric temporal/ownership contract are implemented in candidate 0.2.0-rc.1 with native V007, SHACL and SQL/SPARQL tests. The Run 3 prototype/history below remains unchanged. Minimum viable ontology remains rejected as an unqualified organization-ready claim: real case validation, foundational completion and independent review are still pending. See [current formal contract](../../formalization/qualified-context-contract-v0.2.0-rc.1.md).

# Run 3 core decisions and remaining acceptance boundary

Baseline: `b8a321baaff2534d6594d80d23402c6e8046e94a`. This decision/audit layer does not rename the evaluated `0.1.0-rc.1` release or silently replace its Turtle.

## Stable decisions
Risk remains a governed domain pattern with explicit identity continuity; no forced UFO primitive, global key, or automatic sameAs. A changing score, owner, description or workflow does not create a new risk identity. Scenario is a possible-pattern construct; Risk Event is an occurrence. Responsibility is a normative assignment about the risk, with actor/endurant participation, rather than a database key masquerading as mediation. Treatment specification, execution and control bearer remain distinct.

Risk State describes a situation; Workflow State describes processing of a record. Assessment Result is information about a risk under a method, time and control baseline. A separate generic RiskAssessmentState class from legacy PR #61 is not adopted: existing result/context distinctions and the qualified temporal profile address its required questions without an extra ungrounded identity. Inherent/residual remain result contexts; projected-after-control and observed-after-control must be distinguished explicitly.

## Complete inventory accounting
All 47 concept rows have a disposition: 35 current OWL classes, four SKOS reference/pattern markers and eight without a local declaration. The latter are not eight accidental omissions: API is an unresolved external reference; Hazard/Harm, Signal, Criteria/Appetite/Tolerance and Risk Nature are bounded/deferred profile work. They remain visible and do not count as implemented local classes. The 12-scope research portfolio, ten architecture responsibilities and six formal modules are different denominators. `domain-membership.csv` reports overlapping conceptual assignments, with Method shown separately; no domain name uses an ampersand.

## Corrections and residual gaps
The current state-lifecycle table is corrected to remove administrative escalation from situational Risk State and to stop treating gross as an automatic inherent synonym. These align it with already frozen contracts. Additional definition refinements—event-only Core Trigger, confidence as an information qualification, indicator specification versus observation value—must be synchronized with OWL comments, registry definitions and the full diagram in P07/P08. The current 33-row foundational category registry is not a complete stereotype assignment for every one of the 47 descriptive rows.

The temporal companion is executable and separately namespaced. It adds no production import or native database column in this run. The existing SQL `result_kind` is a single discriminator, so it cannot by itself preserve both a result dimension (impact/likelihood) and a control baseline (inherent/residual). This is a concrete P07/P10 synchronization gap, not covered up by the 27-field disposition count. Future-dated ownership also requires the qualified at-time rule, not just absence of an invalidation marker.

## Minimum viable claim decision
Use **bounded executable core candidate**, not an unqualified organization-ready minimum viable ontology. Existing and new synthetic tests show selected behaviors; real reviewer input, populated literature-case tests, complete OntoUML and native temporal projection remain outstanding. Extensibility is supported only by the tested additive pharmaceutical specialization and baseline-query regression, not a formal conservative-extension theorem or arbitrary-profile guarantee.

P06 remains IN_PROGRESS until the temporal/context and definition choices are synchronized into the canonical candidate with downstream tests and an explicit promotion decision. No critical uncertainty is disguised as completed merely because each row has an owner.
