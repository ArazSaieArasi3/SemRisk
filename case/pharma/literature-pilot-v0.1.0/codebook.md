# Data dictionary and coding decisions

Parent field definitions: `../literature-dataset-data-dictionary-v1.0.csv`. This candidate separates source statements from analyst mappings instead of mixing them in one canonical row. Stable join key: `statement_id` (`PRS-0001` onward); source foreign key: `source_id` (`PLS-001` onward). Each JSON array has one object per record; generated CSV uses the same field names. Lists/objects/booleans in CSV are JSON-encoded, not delimiter-split strings.

| Field or group | Meaning and rule |
|---|---|
| source_locator | Human-retrievable section, table or paragraph anchor in the exact cited publication; runtime search line numbers are not canonical locators. |
| statement_paraphrase | Short source-local proposition, with authors' hypotheses and model dependence preserved. No long quotation. |
| enterprise_context | Analyst category for browsing; not a native ontology class or a complete taxonomy. |
| subject_actor | Source-described generic group; not an identified firm/person and not automatic `RiskSubject` instantiation. |
| potential_event, consequence | Source-supported possibility/association; absence is `NOT_REPORTED`. Neither field asserts realization. |
| likelihood_reported, impact_reported | Source-local reported category if present. Only two rows contain qualitative quadrant labels. None supplies a calibrated case probability or severity. |
| other_quantity_reported | Ranking/closeness/category with method/context. SAW and TOPSIS measures cannot populate a probability field. |
| temporal_qualifier | Reported time-horizon dependence of a claim, never a fabricated timestamp or event interval. |
| control_reported | Textual mitigation proposal, not evidence that a control was implemented/effective. |
| evidence_kind | `author_analysis` for this pilot: published expert rankings, author interpretations, qualitative models or regression estimates. No record is a directly verified operational incident. |
| occurrence_status | `NOT_ASSERTED` for every row. |
| source_role | `design_reused` or repository-relative `evaluation_new`, assigned before mapping; both used only for applicability. |
| review_status, extraction_method | `unreviewed` by independent human coder; AI-assisted inspected-source extraction. No invented agreement score or expert review. |
| rights_status | `paraphrase_with_citation`; detailed source terms remain in `sources.json`. |
| mapping_status | `partial`: useful scenario pattern with gaps; `ambiguous`: insufficient adverse-event/outcome semantics; `unmapped`: no defensible scenario mapping. No `exact` mappings in this pilot. |
| semrisk_ids | Existing frozen conceptual IDs used by the mapping; `SR-CPT-021` is a provenance registry marker, never instantiated as an OWL class. |
| scenario_type_created | If true, create `RiskScenario` as a situation type and a distinct `ScenarioDescription` artifact version. No witness individual is created. |
| external_ids | Empty here: no named CM-PharmE identity can be justified from generic participant labels. |
| duplicate_group | Analyst topic grouping for review only. Rows sharing a topic are not merged across contexts or studies. |

`NOT_REPORTED` means not established for this extracted statement, not proven absent from all of the source paper. Unknown validity, disagreement and intentional non-assertion are explained in mapping/source notes rather than encoded as a false zero. The PLS-006 26-versus-30 sample inconsistency is a source limitation; no chosen value is silently substituted. PLS-001 table-caption offsets are handled with the narrative paragraph locator.

Grey literature policy: no blog/community/news statements are included. Any later grey supplement requires author/organization, date/version, direct experience/evidence basis, conflict-of-interest note, retrievable locator and separate role/analysis. It cannot silently contribute to this primary-source denominator.
