# SemRisk External Ontology Artifact Binding — W1 Baseline

**Date:** 2026-09-21
**Purpose:** bind exact external ontology/release identities required by P1-R0/P1-R1 without silently treating moving `main` branches as scholarly versions.

## 1. COVER — SRC-ON-001 / DEP-001

- Repository: `unibz-core/value-and-risk-ontology`
- Default branch: `main`
- W1 bound repository commit: `898a7d87d1da0f8c292620d966754a630ae3b57b`
- Formal file: `owl/cover.ttl`
- Formal-file blob SHA: `185064e68ac63b602bf97247da92e10b729a77fa`
- Namespace: `https://purl.org/krdb-core/cover#`
- License: Apache License 2.0
- Publication DOI: `10.1007/978-3-030-00847-5_11`
- Release/tag status: no governed semantic release/tag was identified in the inspected public repository metadata; W1 therefore uses immutable commit binding.

### Binding caution
The current Turtle source contains an ontology declaration written as `<thttps://purl.org/krdb-core/cover>` while the namespace is `https://purl.org/krdb-core/cover#`. This must be treated as a source-level formalization anomaly to verify during #21/#29; SemRisk must not silently repair it in a quoted external artifact.

### W1 decision
`COMMIT_BOUND_REFERENCE`. Suitable for exact comparison/reuse analysis. Any import/reuse in a SemRisk release must preserve attribution/license and must be regression-tested against the pinned commit.

## 2. ROSE — SRC-ON-002 / DEP-002

- Repository: `unibz-core/security-ontology`
- Default branch: `main`
- W1 bound repository commit: `50ef107989d747a5d38cba1653c5309bff328048`
- Formal file: `owl/rose_gufo.owl`
- PURL: `https://purl.org/security-ontology`
- Formal ontology base in inspected file: `http://rose.com`
- License: MIT
- Publication DOI: `10.1007/978-3-031-17995-2_26`
- Repository status: corrected repository version explicitly includes the ER-paper erratum for characterization cardinality.
- Release/tag status: no governed semantic release/tag was identified in the inspected public repository metadata; W1 uses immutable commit binding.

### W1 decision
`COMMIT_BOUND_CORRECTED_REFERENCE`. SemRisk comparisons/reuse decisions must reference the corrected repository artifact rather than reproducing the known paper cardinality error.

## 3. CM-PharmE — DEP-003

- Repository: `ArazSaieArasi3/CM-PharmE`
- Current repository head inspected: `5099888668d35f798e4759e3534e707ed906db24`
- Stable semantic baseline declared by repository: `v1.0.0`
- Frozen release manifest: `releases/v1.0.0/manifest.yaml`
- Historical release baseline commit: `9efd0e3ac909e4065012fae7aeb6b0a94029c440`
- Semantic inventory: 39 canonical concepts; 40 canonical relations; 5 domains.
- Release rule: historical release artifacts marked immutable.
- License: **UNRESOLVED owner-governance decision** in current repository release-readiness documentation.
- Planned namespace: `https://w3id.org/cm-pharme/`; redirect not yet deployed.

### W1 decision
`FROZEN_RELEASE_BOUND_WITH_LICENSE_GAP`. Paper-1 semantic bridge design should use the frozen `v1.0.0` registries/model baseline, not mutable `main`. Release-bound redistribution/import must remain license-aware; mapping/citation can proceed with explicit external ownership.

## 4. IOF Biopharma Risk Management — SRC-ON-006 / DEP-008

- Public suite/repository: `iofoundry/ontology`
- Module IRI: `https://spec.industrialontologies.org/ontology/biopharma/BiopharmaRiskManagement/`
- Portal release inspected: `202603`
- Portal maturity: `Provisional`
- Portal license: MIT
- Portal scope: 26 classes; risk management, assessment, control, communication, review, risk estimates, residual risk, FMEA/HAZOP and documented outputs.
- Current GitHub module path: `biopharma/BiopharmaRiskManagement.rdf`
- Current fetched file blob SHA: `ce412eedf9399dc0057379159484876ae353af75`
- Current repository search snapshot commit for biopharma documentation: `b5384d757082397a1a8bedd0fddf950f356045de`

### Version discrepancy
The official portal is labeled **Release 202603**, but the currently fetched repository RDF declares `owl:versionIRI` as `.../202602/biopharma/BiopharmaRiskManagement/`. IOF documentation states that RDF `owl:versionIRI`/maturity metadata are the source of truth for exact versions. Therefore SemRisk must not silently equate the portal's 202603 label with the current repository file's 202602 version identity.

### W1 decision
`PROVISIONAL_REFERENCE_BOUND_WITH_VERSION_DISCREPANCY`. The ontology is safe as current comparative/reuse evidence and strongly material to Pharma mapping, but release-bound import/alignment must wait until the portal/RDF version discrepancy is resolved or an exact release RDF is archived/pinned.

## 5. Consequence for P1-R0 / G1

- COVER exact reference/license blocker: **resolved for W1 by immutable commit binding**.
- ROSE exact reference/license/erratum blocker: **resolved for W1 by immutable commit binding**.
- CM-PharmE exact semantic baseline: **resolved to frozen v1.0.0**, with license governance still open for redistribution.
- IOF Biopharma identity/license/maturity: **substantially resolved**, but exact portal-vs-RDF version binding remains conditional.

These decisions reduce artifact-identity uncertainty without prematurely deciding #21 reuse/import semantics.