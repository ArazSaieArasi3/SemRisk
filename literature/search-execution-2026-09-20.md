# SemRisk W1 Search Execution — Run 2026-09-20

**Research:** R-022 / SemRisk  
**Issue:** #40  
**Run status:** PARTIAL EXECUTION — academic + targeted web/formal-artifact lanes started; saturation not yet reached.

## 1. Purpose

This run begins the reproducible Paper-1 search execution after W0 research-contract freeze. It records exact search families, channels, observed noise, material discoveries and downstream routing. Search completeness is not claimed from this run alone.

## 2. Channels executed

1. **OpenAlex-based academic discovery** via structured scholarly search.
2. **Google Scholar-based targeted academic search** using exact-title and phrase queries.
3. **Targeted web search** for publication pages, ontology repositories and recent 2025–2026 work.
4. **Formal artifact/repository verification** for known ontology projects when surfaced.

## 3. Search execution log

| Search ID | Channel | Exact query / family | Date | Screening result |
|---|---|---|---|---|
| SRCH-20260920-001 | OpenAlex | risk ontology | 2026-09-20 | HIGH NOISE; generic term risk produced many unrelated biomedical/statistical records; not suitable alone |
| SRCH-20260920-002 | OpenAlex | risk management ontology | 2026-09-20 | HIGH NOISE; broad query insufficiently precise |
| SRCH-20260920-003 | OpenAlex | enterprise risk ontology | 2026-09-20 | HIGH NOISE; requires phrase/field refinement |
| SRCH-20260920-004 | OpenAlex | risk register ontology | 2026-09-20 | LOW PRECISION; no strong direct closest-work result in first page |
| SRCH-20260920-005 | OpenAlex | dynamic risk management ontology | 2026-09-20 | MIXED; targeted verification needed |
| SRCH-20260920-006 | OpenAlex | risk knowledge graph enterprise | 2026-09-20 | HIGH NOISE |
| SRCH-20260920-007 | OpenAlex | pharmaceutical risk ontology | 2026-09-20 | HIGH NOISE; biology term risk dominates |
| SRCH-20260920-008 | OpenAlex | risk ontology evaluation methodology | 2026-09-20 | HIGH NOISE |
| SRCH-20260920-009 | Google Scholar | "The Common Ontology of Value and Risk" | 2026-09-20 | MATERIAL known comparator confirmed; also yielded 2025 risk-propagation lead |
| SRCH-20260920-010 | Google Scholar | "An Ontology of Security from a Risk Treatment Perspective" | 2026-09-20 | Known comparator; Scholar recall weak, repository verification preferred |
| SRCH-20260920-011 | Google Scholar | "AIRO" ontology risk | 2026-09-20 | Noisy; exact repository/publication verification preferred |
| SRCH-20260920-012 | Google Scholar | "Riskman" ontology shapes risk management | 2026-09-20 | Weak Scholar precision; web/publisher verification succeeded separately |
| SRCH-20260920-013 | Google Scholar | "Ontology-Based System for Dynamic Risk Management in Administrative Domains" | 2026-09-20 | Scholar recall weak; publisher/web verification succeeded separately |
| SRCH-20260920-014 | Google Scholar | "Toward an ontology-based modeling for risk management" | 2026-09-20 | Scholar returned none; targeted web found authoritative university record |
| SRCH-20260920-015 | Google Scholar | "risk register" ontology risk management | 2026-09-20 | No direct material ontology in first result set; topic remains unsaturated |
| SRCH-20260920-016 | Google Scholar | "enterprise risk knowledge graph" | 2026-09-20 | No direct result in this exact query; alternative terminology required |
| SRCH-20260920-017 | targeted web | "risk management" ontology risk ontology semantic web | 2026-09-20 | Dynamic risk ontology paper + Open Risk ontology family + known comparators found |
| SRCH-20260920-018 | targeted web | exact COVER / ROSE / AIRO / RISKMAN titles and repositories | 2026-09-20 | Formal artifact loci verified |
| SRCH-20260920-019 | targeted web current-work refresh | "risk ontology" / "risk management ontology" 2025–2026 | 2026-09-20 | Material 2025 comparator candidates found |
| SRCH-20260920-020 | targeted web | "risk register ontology" 2025 semantic | 2026-09-20 | No direct close ontology found in this run; not evidence of absence |

## 4. Search-method finding

Broad keyword search is **not adequate** for this topic because risk, ontology, and enterprise are highly polysemous and produce unrelated biomedical, statistical, information-retrieval and organizational results. The protocol therefore changes from broad-keyword-only execution to a layered strategy:

1. exact-title / seed comparator verification;
2. phrase-constrained risk-ontology searches;
3. domain-specific synonym families;
4. author/citation snowballing from COVER/ROSE and 2025 risk-ontology work;
5. formal-artifact/repository retrieval separately from publication discovery.

This is a search-strategy refinement, not a change to the W0 research design.

## 5. Material comparator/source delta

### NEW-MATERIAL-001 — Toward an ontology-based modeling for risk management
- Year: 2025
- Authors: Ítalo Oliveira, Stefano M. Nicoletti, Mattia Fumagalli, Gal Engelberg, Giancarlo Guizzardi
- Venue: VMBO / CEUR Workshop Proceedings, Vol. 4129
- Why material: explicitly proposes a risk-management ontology network integrating value, risk, incident, security, monitoring, trust and resilience, motivated by semantic ambiguity/interoperability in risk-management techniques.
- Impact: high on SemRisk novelty boundary and #14/#22/#23; must be deeply mined before G1.
- Initial role: comparative + discovery/design evidence, not independent validation.

### NEW-MATERIAL-002 — Beyond Risk Propagation: A Unified Approach
- Year: 2025
- Authors include Alessandro Mosca, Mattia Fumagalli, Gal Engelberg, Victor D. Corvalan, Dan Klein, Pnina Soffer, Diego Calvanese, Giancarlo Guizzardi
- Venue: JOWO 2025 / CEUR
- Why material: well-founded ontology-driven account of risk propagation involving objects, assets, agents and objectives with implementation/testing.
- Impact: high for event/causal/propagation semantics and for nonclaims around dynamic propagation; must inform #14/#20/#22.
- Initial role: comparative + design lead; Paper 1 should not claim novelty for generic risk propagation.

### NEW-CANDIDATE-003 — Open Risk ontology family
- Formal repository includes BMRO, NPLO, DOAM, CRO, RFO.
- Why relevant: demonstrates multiple operational/domain risk ontologies in Semantic Web form; likely medium-to-high relevance depending exact semantic overlap.
- Routing: #14 comparator inventory; individual ontology qualification before inclusion in closest-work matrix.

### NEW-CANDIDATE-004 — Ontology-Based Approach to Supplier Risk Management Using Large Language Models
- Year: 2025
- Domain: supplier/supply-chain risk
- Relevance: potentially useful Pharma/supply-chain domain comparator and ontology-engineering-method comparator; not yet classified as closest work.
- Routing: #15 Pharma/supply-chain and #23 method comparison.

### NEW-CANDIDATE-005 — Rule Inferring for Engineering Quality Risk Management Based on Ontology
- Year: 2025
- Domain: construction/engineering quality risk
- Relevance: application ontology + SWRL + case validation; useful for transferability/application-evaluation comparison, probably not foundational closest work.
- Routing: #14/#31 if retained.

## 6. Known formal artifacts reverified

- COVER — formal GitHub repository; OntoUML + OWL; Apache-2.0 repository license.
- ROSE — formal GitHub repository; reference ontology for security engineering; corrected artifact differs from paper erratum; exact release/ref still needs pinning.
- AIRO — formal GitHub repository; persistent w3id namespace; ontology serializations and release history.
- RISKMAN — current peer-reviewed 2025 publication plus ontology/shapes locus; 2024 preprint is lineage-related and must not be double-counted.
- Dynamic Administrative Risk Ontology/System — 2019 peer-reviewed system remains relevant as dynamic/runtime comparator.

## 7. Lineage/dedup controls already identified

- RISKMAN 2024 preprint -> 2025 SEMANTiCS peer-reviewed paper: one research lineage, multiple versions.
- COVER paper -> repository artifact: publication/artifact pair, not two independent comparators.
- ROSE papers -> repository/corrected model: lineage-linked.
- AIRO publication -> repository/release: lineage-linked.

## 8. Saturation state by search family

| Search family | State after this run |
|---|---|
| foundational/well-founded risk ontology | PARTIAL; good seed set but forward/backward snowballing still required |
| generic risk-management ontology | PARTIAL; new 2025 ontology-network proposal materially changes landscape |
| risk-register semantics | UNSATURATED |
| enterprise/architecture risk ontology | UNSATURATED |
| dynamic risk / risk propagation | PARTIAL; several material works identified |
| Health/medical-device risk ontology | PARTIAL; RISKMAN strong anchor |
| Pharma/supply-chain risk ontology | UNSATURATED |
| ontology engineering/evaluation methods | UNSATURATED |
| formal artifact/repository landscape | PARTIAL |

## 9. Required next search actions

1. Forward/backward snowball COVER, ROSE, 2025 Toward an ontology-based modeling for risk management, and Beyond Risk Propagation.
2. Search author clusters: Oliveira / Fumagalli / Engelberg / Guizzardi / Sales / Gorczyca.
3. Separate risk register, risk record, risk assessment ontology, GRC ontology, enterprise architecture risk, business architecture risk.
4. Search Pharma-specific terms: quality risk management ontology, drug shortage ontology, pharmaceutical supply chain ontology risk, pharmacovigilance ontology risk.
5. Search formal ontology portals/repositories and exact GitHub artifact loci.
6. Build deduplicated screening registry and update source-register only after source identity is sufficiently qualified.

## 10. Current decision

**Issue #40 remains OPEN.**

This run establishes that execution has started and records material deltas, but it does not yet satisfy saturation, complete snowballing, screening/dedup or unresolved-source queue acceptance criteria.
