# SRC-PH-003 — MedSupplyKG source-level deep profile

Date: 2026-09-28. Source: Eberhardt et al., *Leveraging knowledge graphs in pharmaceutical supply chains: insights into key drivers of drug shortages*, *International Journal of Production Research* 63(19), 7129–7152 (2025), DOI 10.1080/00207543.2025.2496671. Author-institution hosted 25-page publisher PDF: https://publikationen.bibliothek.kit.edu/1000181579/159785046 ; KITopen record DOI 10.5445/IR/1000181579. Article license CC BY 4.0 on PDF p. 2. **Source-level full text inspected; formal ontology file/code/reproducible dataset not bound.** PDF indexes here begin with cover P0; printed article pagination is in the paper.

## Coverage and exact locators

| Scope | Disposition | Claim-relevant evidence |
| --- | --- | --- |
| Abstract, §1 and RQ/contribution, PDF pp. 1–2 | MINED | RQ1 heterogeneous KG integration/critical nodes; RQ2 disruption drivers and economic significance. Ontology-based KG method plus network analysis and decision support are explicit prior art. |
| §2 related work, PDF pp. 3–6, Table 1 p. 4 | MINED_FOR_COMPARATOR | KG/network and pharmaceutical shortage background; Table 1 distinguishes KG objectives, method, application and data. Not counted as independent evidence that all cited methods are implemented here. |
| §3.1 and Fig. 2, PDF pp. 6–7 | MINED | Ontology/schema precedes data→graph; four steps: collection/processing, extraction/linking, storage/visualisation, analysis/application. Formal ontological commitments beyond the published schema are not proven. |
| §3.2 and Fig. 3, PDF pp. 6–8 | MINED | German BfArM report snapshot on 2024-06-01, enrichments from market/product/API/ATC sources; 5,466 initial package-level notifications → 5,414 cleaned records dated Jan 2017–Jun 2024. PZN/ATC missingness repair and exclusions are explicit; exact released data file/schema remains unavailable. |
| §3.3–3.5, Tables 2–3, Fig. 4, PDF pp. 8–10 | MINED | MedSupplyKG six node families and nine directed edge labels; Neo4j via Python and Cypher/degree centrality. Table 2 gives fields; Fig. 4 graph schema is visual evidence, not an OWL file. |
| §4 results, PDF pp. 11–17, Figs. 5–12, Table 4 | MINED_FOR_CLAIMS | 10,351 nodes, 24,820 edges, 5,414 reports, 3,869 drugs, 251 authorisation holders, 687 APIs, 90 pharmacological groups, 32 shortage reasons in eight reason types; graph-driven drivers/priority analyses. These are authors' reported results, not independently reproduced. |
| §5–6, PDF pp. 17–20; data availability p. 20 | MINED | Severity/economic factor and four-quadrant priority matrix; limited public data, static graph, source quality and manual-construction limitations. Supporting study data are available on reasonable request, not a publicly qualified SemRisk dataset. |
| References, PDF pp. 21–24 | CONTEXT_ONLY | Bibliographic snowball leads require independent screening, not automatic inclusion or fact transfer. |

## Semantic inventory and comparison

The graph separates `Report` from `Shortage` as distinct node types. A report has ID, notification type/date, start and expected end, and is transmitted by an authorisation holder. A shortage node carries reason type/characteristic/comment and influences a drug. This **directly falsifies any SemRisk novelty claim that merely distinguishing a report/notification from a shortage event or condition is new**. Table 2 (PDF p. 9), Table 3 and Fig. 4 (PDF p. 10) are the exact locators. The paper's `Report` is a domain shortage notification, not automatically equivalent to SemRisk's broader Risk Register Entry; nor does a `Shortage` label alone decide event vs situation vs type semantics. No exact equivalence is asserted.

Other nodes: authorisation holder, drug, active pharmaceutical ingredient (API), and pharmacological group (PHG). Eight Table-3 edges are `TRANSMITS`, `HAS_AUTHORIZATION`, `HAS_INFORMATION`, `INCLUDES` (Shortage→Shortage subtype/reason), `INFLUENCES`, `HAS_ALTERNATIVE`, `CONTAINS`, `CLASSIFIED_BY` and `CATEGORIZES`. Each label is a graph relation at the paper's application level, not a certified OWL object-property IRI or foundational relation.

The model links product PZN/ENR, ATC classification, API supply relevance/criticality, paediatric/hospital status, alternative drugs, package prices, prescription volumes and costs. It joins heterogeneous public and market information for Germany. This establishes prior art for Pharma shortage notification graphs, source integration, product/entity linkage, graph-based criticality, temporal notification fields and decision support. SemRisk SR-C3 must focus on demonstrated Core↔CM-PharmE semantic federation/ownership and assessment/evidence/workflow distinctions with exact case tasks, rather than “first Pharma risk KG”, graph queries, or report-vs-shortage separation.

## Methods, results and limits

The paper describes an ontology as entity/relationship types, builds the graph in Neo4j through Python, uses Cypher and degree centrality, and reports shortage cause categories including production, market, process, quality, legal, logistics and data issues. It combines severity and economic-cost factors in a four-quadrant prioritisation view (§4.5, Fig. 12); this is a domain analytics result, not an evaluation of SemRisk's OWL reasoning or SQL↔SPARQL parity. The paper's own §5.3 says important supplier/location/transport/inventory data are missing, the graph is static, data quality matters and construction is manual. These limitations do not imply the published graph lacks other unreported capabilities.

The article says supporting data are available on reasonable request (§Data availability, PDF p. 20). An exact ontology serialization/repository/version/license, Python code snapshot, Neo4j dump, file-level dataset and independent rerun are **UNKNOWN/NOT_ASSESSED**. The article CC BY 4.0 does not by itself license any unseen software/data artifact. E10 can compare publication-level graph semantics and reported results now; reproducibility comparisons require a separately bound artifact and permission.

## Downstream disposition

- #14: add as direct Pharma KG/report-vs-shortage comparator; append to E10 shortlist and claim calibration (#53). No lexical exact mapping of `Report` to Risk Register Entry or `Shortage` to Risk Event.
- #15: source-level material sections covered for this paper; the paper's data/source schema is a lead for #17, not a qualified reusable dataset. Source-complete data extraction is separate.
- #31/#113: compare recorded unit/denominator: six node families, Table-3 edge rows, 5,414 record snapshot and selected tasks at the exact paper locator, against SemRisk's release-bound semantic and task outputs. Authors' reported numbers are not independent verification.
