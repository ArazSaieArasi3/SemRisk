# DS-003 v4 label reconciliation checkpoint

**Issue:** #17; stage 2 remains IN_PROGRESS. **Input baseline:** `0881a751ba59db67913c0a2baf27572ef660c249`. This is an analyst label/context review for #18, not an adopted ontology mapping or independent validation.

## Source and exact denominator

- Source: SRC-DS-003, DOI `10.25375/uct.29178665.v4`, file `55440170`, sheet `Codebook`, rows 2–252. File/version/license/checksums are bound in [the manifest](ds003-v4-file-manifest-2026-10-02.json).
- The unchanged [raw extraction](ds003-v4-codebook-codes-2026-10-02.csv) contains 251 coding rows and 152 distinct case-sensitive full `Name` paths. Its SHA-256 is `753bab778b43ca6ddd32d281a993a59e15b4274a9d9c948f78619786412225ea`.
- [Label reconciliation](ds003-v4-label-reconciliation-2026-10-02.csv) records 152/152 label dispositions, exact native spellings, original locators/folders, analyst topic, uncertainty and conditional candidate IDs.
- [Row lineage](ds003-v4-code-label-lineage-2026-10-02.csv) connects all 251/251 extraction IDs to exactly one native-label review row. Country contexts and original full paths remain separate. No source/reference count is summed into participant prevalence.
- 250/251 original rows have no native definition. The single definition in `Codebook!C135` was checked in the original XLS and recorded only as a locator-specific definition for the `Sociological factors` label. Other rows with that same label do not thereby acquire a native definition.

## Lexical decisions

All native strings are retained. Analyst-normalized paths apply case folding, repeated-space/hyphen-space normalization and explicitly inspected spelling corrections: `transperancy`, `artifcial`, `land scape`, `key drivers fro shortages link to manufacturing`, `thier`, `intcentivisation`, `disicentivising`, `exisitng processes for delaing with shortages`, `existing processes fro dealing with shortages`, `key stake holders`, `forcasting`, `goverment`, `neccessity`, `stategies`, `raw material manufature`, `instituttion`, and `paitent`.

The result is **133 lexical review groups**, including **17 groups containing multiple native labels**. These are review groupings, not 133 distinct domain concepts. No original row is removed and no semantic equivalence is asserted. In particular:

- `Current procurement and supply chain` stays separate from `Current procurement and supply chain landscape`.
- `Key drivers of shortages linked to manufacturing` stays separate from `Key drivers for shortages linked to manufacturing`.
- Missing or additional path components, singular/plural differences and substantively different sentences are retained.
- A heading for causes, forecasting, policy or communication cannot establish a causal relation, assessment result, governance criterion or Signal.

## Semantic dispositions and proposed review anchors

The 152 labels have dispositions across **22 analyst topics**. These topic names organize the review; they are not new SemRisk domains, classes or source-native definitions. Full paths and leaf/context differences remain in every row.

**25 labels** have conditional related-review anchors to existing concept IDs. The remaining **127 labels** have topic/ambiguity dispositions only. All candidate mappings have `LOW_LABEL_CONTEXT_ONLY` confidence; `asserted_equivalence` is `NONE` throughout.

| Label family | Candidate review | Required distinction |
| --- | --- | --- |
| Selected demand/economic/manufacturing drivers | Risk Source / Predisposing Condition | A participant coding label does not prove causation or intrinsic Vulnerability. |
| Selected impact/outcome labels | Consequence | Effects are distinct from Impact Assessment Result; Health Harm remains deferred. |
| Selected mitigation strategies | Risk Treatment Strategy / Risk Treatment Activity | Proposed strategy, selected information artifact and performed activity need source-context separation. |
| Shortage duration | Risk Event context | Duration is a potential attribute of a contextualized occurrence, not itself an event class. |
| Manufacturing/API concentration | Risk Source / Predisposing Condition; API reference | API is mentioned inside the code; it is not equivalent to the whole code. The API external bridge remains unresolved. |
| Surveillance technology | Observation Activity / Observation Result context | Infrastructure is distinct from the activity it enables and information it produces. |
| Others | Explicitly unmapped | No semantic anchor without the underlying passages. |

Participant quotations were not republished. The labels are design evidence from the CC BY 4.0 source package. Attribution is retained through SRC-DS-003, the DOI and the publisher manifest; publication does not turn those codes into independent evaluation evidence.

## Remaining work and acceptance

This completes the **label-disposition and reversible lexical-review pass**, not full semantic reconciliation. Next, check proposed mappings against transcript/results/instrument context with exact locators; separate proposed versus performed responses, actors versus accountability, sources versus causal claims, and events versus reported descriptions. Complete remaining file coverage before claiming source-complete DS-003 mining.

#17 stays OPEN. DS-004 exact-file access is still blocked; DS-001's inspected supplement is not its underlying primary data. DS-002 record-level holdout and the frozen #28 case remain unchanged. Any new semantic adoption must enter #18 and an impact review.

## Validation

Checks cover a bijective 251-row lineage to the raw extraction, 152 unique label IDs, exact native label/locator/folder preservation, definition locator and candidate-ID resolution against the existing concept registry. Lexical groups are computed from the separately retained normalized path, and never written over source labels or canonical registries. No ontology, case fixture, WebVOWL bundle or frozen release file is changed by this checkpoint.
