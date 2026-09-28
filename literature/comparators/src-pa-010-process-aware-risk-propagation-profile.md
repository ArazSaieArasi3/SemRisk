# SRC-PA-010 Technical Profile — Process-Aware Risk Propagation

**Source:** Engelberg, Fumagalli, Kuboszek, Klein, Soffer, Guizzardi, *An Ontology-Driven Approach for Process-Aware Risk Propagation*, SAC 2023, pp. 1742–1745, DOI `10.1145/3555776.3577795`.
**Inspected primary copy:** https://ris.utwente.nl/ws/portalfiles/portal/359274644/3555776.3577795.pdf (four printed pages, consulted 2026-09-28).
**Lineage:** arXiv `2212.11763` predecessor → SAC 2023 paper → later PA-006 JOWO 2025/CEUR 4176. Distinct outputs in one research programme, not independent novelty votes.
**Status:** publication-level implementation/profile bound; source repository/version and independent reproduction `UNKNOWN/NOT_REPORTED`.

## Semantics and architecture

- The risk-process ontology has three scopes: generic task constructs `S2`, domain specialization `S1`, and case-specific types/instances `S0` (paper §2.1, printed p. 1743). Its lightweight `S2` central `ElementAtRisk` covers process types and objects; the authors explicitly leave their finer type distinctions implicit in this four-page work. Do not project later PA-006 assessment taxonomy backward into this version.
- Two propagation edge kinds are `Dependency` (e.g. process order/triggers) and `Abstraction` (object-to-higher process scope). The paper calls the corresponding calculated views `FollowedRisk`, `DirectedRisk`, and `TotalRisk`; `Importance` weights a relation by perspective (p. 1743, Fig. 2). Risk is quantified here with a simplified probability × severity vector; deeper ontological analysis is explicitly future work (§2).
- The analytics component queries the ontology to extract a labelled graph. Given leaf risk values as input, it traverses with depth-first search and uses `max_per_aspect` on vector components, multiplying incoming components by edge-importance weights (pp. 1743–1744, Fig. 3). This is a concrete worst-case propagation method, not an assertion that risk is a material entity moving through the graph.

## Reported implementation and case

- §3, printed pp. 1744–1745: ontology scopes encoded in OWL; Neo4j neosemantics imports OWL into a labelled property graph; a Python application with an ad hoc Neo4j client orchestrates extraction and propagation. The paper reports a cybersecurity demonstration for a vehicle-assembly process, with cyber assets, impacts, and process elements; relation examples include `CorrelatedTo`, `ComponentOf`, and `FollowedBy`.
- The case uses confidentiality, integrity, availability and safety perspectives. Figure 4 depicts the case subgraph; the paper gives example input/output vectors and points to an external demonstration video and predecessor [5] for more details. These are author-reported proof-of-concept results, not an independently reproduced benchmark or a multi-domain evaluation.
- The inspected four-page publication has no source repository, exact OWL artifact/ref, input dataset version, software dependency lock, or runnable command. This is an **unresolved artifact binding**; it is not evidence that no source exists elsewhere.

## Comparison and lineage consequence

PA-010 is strong prior art for an OWL-backed, process/object-aware risk model coupled to a graph database and an executable propagation method. SemRisk cannot claim novelty for an ontology→graph implementation, generic architecture/process links, risk vectors, or executable risk queries alone. This version does not establish first-class register-entry identity, assessment-activity/result provenance, risk-state vs management-workflow-state separation, or ontology↔relational projection parity; absence from a short paper is an evidence boundary rather than proof of incapability.

PA-006 later replaces the simple propagation emphasis with a COVER-inspired assessor/goal/event/object assessment account, richer assessment predicates and ProbLog theory. Do not assign PA-006's propositions to this SAC paper, and do not count both papers as two independent confirmations of SemRisk differentiation.

**Reuse:** comparison/reference only. Exact source license/version and code availability remain unknown. A new source or a broader claim triggers an artifact search and reassessment under #14/#23.
