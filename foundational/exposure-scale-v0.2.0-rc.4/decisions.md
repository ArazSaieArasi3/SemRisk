# Exposure endpoints and numeric-scale identity

Baseline `6d619c5bbcb3532d68e250e2c27a9a3232fd06f9`; successor `0.2.0-rc.4`. These are explicit SemRisk design decisions. They are supported by existing definitions, database design and foundational constraints; they are not verbatim models prescribed by the cited standards.

## D4 — Exposure is a situation with explicit subject and source

Keep `SR-CPT-010` as a specialization of `gufo:Situation`. Introduce `SR-REL-039 hasExposedSubject` and `SR-REL-040 hasExposureSource`, both from Exposure to the corresponding existing concept. This repairs a missing semantic link: `core.exposure` already stores subject, source and optional interval, while the rc.3 ontology did not name the reified endpoints. The two properties are necessary to answer who is exposed, to what, and during which represented interval. They are not added to improve a graph statistic.

The domain definition remains unchanged to preserve existing stable vocabulary. Its operative interpretation here is a situation, not the extent/score of exposure. NIST's glossary lists context-dependent meanings: organizational/stakeholder exposure in SP 800-161r1-upd1 and an assessment-oriented likelihood/impact meaning in NISTIR 8286. These must not be collapsed into one number-valued phenomenon. No equivalence to either definition is asserted. A score remains an assessment result with method and scale.

Ordinary associations are used. Exposure does not establish that a risk event happened, that a consequence must occur, or that a source caused anything. The pre-existing `exposes` relation is retained without an unconditional property-chain rule: a timeless flattened pair cannot preserve the exposure episode's temporal identity. Neither new property is globally functional. The separately opted-in pair profile requires one named subject and one named source per exposure record, consistent with the existing relational row grain; broader multi-participant representations are not ruled out by OWL.

Intervals use the existing context properties with optional start/end. The as-of query requires an explicit start and supplied instant and interprets a known end as exclusive. A missing start is unknown, not silently converted into an active exposure. Two episodes with identical participants may remain distinct.

## D5 — NumericScale is an issued specification version

The pre-existing helper describes a **versioned** numeric interval and dimension, and `assessment.numeric_scale` already has `version_ref`. Retain its stable IRI, add `rdfs:subClassOf ist:ArtifactVersion` and `rdf:type gufo:SubKind`, and clarify the comment. The displayed name is “Numeric Scale Version.” It inherits the single local identity provider ManagedInformationArtifact through ArtifactVersion. This is a rigid specification category; neither assessment use nor equal bounds provides its identity.

The artifact has issuance/version identity. Its interval/dimension content is represented separately by InformationContent. Two issued scale versions can have identical bounds and share content while remaining explicitly different. This profile does not model all mathematical value spaces or classify the scale as a quality value. The existing Subkind constraints justify inherited identity; the choice of this particular information-artifact interpretation is a local design commitment.

The new strict profile composes `ac:ScaleShape` and `ist:VersionShape`. An old scale with only bounds and a version string is still parseable OWL but is incomplete for rc.4 strict validation until a governed artifact parent, content reference and explicit identity distinction are supplied. Do not invent these from a label, numeric equality or database key.

## Formal delta and consumer impact

| Consumer | Implemented delta | Bound |
|---|---|---|
| OWL | Two domain/range-defined properties; scale subclass/type | No automatic existence, equality, causal or consequence rule |
| SHACL | Explicit exposure pair and interval checks; composed scale-version completeness | Explicit-data, opt-in validation; not open-world inference |
| CQ | Exposure endpoint/as-of queries and scale identity examples | Synthetic, version-bound demonstrations |
| Native SQL | Map existing exposure row endpoints to the two properties and test parity | No schema migration required for Exposure; scale/content and rc.3 workflow parity still open |
| Editable diagram | Two named Exposure links and NumericScale-to-ArtifactVersion generalization | Full editor/antipattern and paper-fit gates remain separate |
| Vocabulary | 47 existing conceptual IDs; 40 registered relation decisions | Two genuinely new relations; helper counts unchanged |

Old rc.1–rc.3 source and evidence bytes remain frozen. The current pointer advances only after the new checks pass. The stronger scale classification is documented as a semantic extension, not a proven conservative/equivalent migration.

## Sources checked on 2026-10-05

- NIST CSRC, “Exposure” glossary and its source-specific entries: https://csrc.nist.gov/glossary/term/exposure . Supports the ambiguity boundary; does not prescribe the new property design.
- gUFO 1.0.0, individual/type distinction and situations: https://nemo-ufes.github.io/gufo/ . The implementation uses the already pinned local gUFO release; current documentation is interpretive support, not an unpinned import.
- OntoUML specification, Subkind constraints C1–C3: https://ontouml.readthedocs.io/en/latest/classes/sortals/subkind/index.html . Supports the single inherited identity provider and rigidity checks.
- Local design provenance: `conceptualization/core/core-concept-registry-v0.1.csv` row SR-CPT-010; `relational/sql/V001__paper1_projection.sql` table core.exposure; `relational/sql/V007__qualified_assessment_context.sql` table assessment.numeric_scale; rc.3 artifact identity decision D2.

No new empirical observations or expert responses are represented here. Full OntoUML certification, a universal exposure definition, and complete relational projection remain unsupported claims.
