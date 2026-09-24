# SemRisk Paper-1 Pre-Assurance Threat Snapshot

**Issue:** #56  
**Date:** 2026-09-24  
**State:** PRE_ASSURANCE_SNAPSHOT_v1.0  
**Purpose:** mandatory input to #53 claim calibration and #54 assurance.

## Executive conclusion

No current threat invalidates the formal/structural results already reported for the exact evaluated candidate, but several threats **materially constrain manuscript claims**. The most consequential residual limitations are evidence circularity, pending expert semantic validation, bounded external/domain evidence, incomplete independent transferability, comparator/standards evidence tail, and public-reproducibility limits from private/licensed sources.

The snapshot therefore recommends:
- **retain but bound** formal correctness and task-specific projection claims;
- **retain but narrow** operational-schema and Pharma federation claims;
- **downgrade transferability** from transfer/generalization to bounded cross-context applicability unless independent E11 evidence is executed;
- **keep novelty/comparative wording provisional** until #14/E10 is complete;
- **prohibit semantic-validation wording** until real #51 reviewer evidence is analyzed;
- **state reproducibility with access limits**, not as unrestricted public reproduction.

## Highest-impact active constraints

### 1. Design/validation circularity
SRC-OP-001 and DS-003 helped shape SemRisk. They are valid discovery/design/reconciliation/application evidence but cannot independently validate the same commitments. This directly bounds SR-CL01, SR-CL02, SR-CL05 and SR-CL06.

### 2. Human semantic validation not yet executed
The #51 protocol is frozen but no expert judgments exist yet. Any wording such as “expert validated”, “semantically validated”, “accepted by experts” or similar is currently prohibited.

### 3. Transferability evidence is not independent
The operational schema and Pharma case show heterogeneous applicability, but both influenced design. DS-002 remains protected and unexecuted; DS-004 remains file-level blocked. SR-CL06 cannot currently support independent/general transferability.

### 4. Projection fidelity is task-specific
#49 produced 5 task-equivalent pairs, 2 equivalent after declared normalization and 1 partial representation. Therefore SR-CL04 is defensible only for selected tasks; “lossless ontology-to-RDB mapping” is prohibited.

### 5. Closest-work/standards tail remains open
#14 comparator saturation and #13 clause/schema completeness are not final. Strong novelty, completeness, conformance or broad standards-alignment wording must remain provisional.

### 6. Reproducibility is access-bounded
The governed software, ontology, synthetic data and CI path are reconstructable, but the private Jira source cannot be publicly redistributed and some external sources are license/access limited.

## Claim decisions forced by this snapshot

- SR-CL01: narrow pending #51.
- SR-CL02: supported only as governed operational mapping, not correctness proof.
- SR-CL03: partial until stronger enterprise/standards validation.
- SR-CL04: supported with explicit task-bounded partiality.
- SR-CL05: supported for one bounded Pharma federation case; expert review pending.
- SR-CL06: insufficient for independent transferability; use bounded cross-context applicability wording.
- SR-CL07: provisional descriptive differentiation only.
- SR-CL08: supported as exact-scope formal consistency statement.
- SR-CL09: supported with explicit private/licensed access limitations.

## Threats that must remain visible in Abstract/Conclusion if relevant

If the final abstract/conclusion mentions:
- semantic validity → disclose expert-review scope/limits;
- transferability → use bounded applicability unless independent E11 succeeds;
- relational fidelity → state task-specific parity with partiality;
- reproducibility → state access/licensing limits;
- standards alignment → avoid conformance language.

## Handoff

This snapshot is now authoritative input to #53 and #54. It is **not** the final #56 closure because #51 results and the final #55 release/availability wording must still be incorporated.
