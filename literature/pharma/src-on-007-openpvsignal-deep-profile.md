# SRC-ON-007 Deep Profile and Artifact Binding — OpenPVSignal

**Source ID:** SRC-ON-007  
**Repository:** `inab-certh/OpenPVSignal`  
**W1 bound commit:** `b149f5177c84394a06cacfd4dfc4865c6adf9ba1`  
**Ontology file:** `OpenPVSignal.owl`, blob `6d9e132e3ca00d2244c7cc861a4e034d3ce30a92`  
**Ontology IRI:** `http://purl.org/OpenPVSignal/OpenPVSignal.owl`  
**Ontology versionInfo in bound file:** `draft-v0.9-20200521`  
**Repository license file:** GPL-3.0  
**Foundational paper:** Natsiavas et al. 2018, DOI `10.3389/fphar.2018.00609` (paper CC BY).

## 1. Scope

OpenPVSignal models pharmacovigilance signal reports for semantic publication, interlinking, reasoning, FAIR search/sharing/reuse and provenance. It reuses/imports established semantic resources including OAE, Micropublications, Web Annotation, PROV-O and Time.

## 2. Information-artifact and provenance prior art

The ontology explicitly represents pharmacovigilance signal reports, signals, individual reports, drugs, adverse effects, evidence/supporting information and provenance-oriented publication structures.

This is important for SemRisk because it proves that **signal/evidence/report/provenance modeling in Pharma is established prior art**. SemRisk should not claim novelty for merely representing a signal report with provenance.

## 3. Executable validation/test evidence

The repository includes SHACL-style test cases for signals, PV signal reports, individual/VigiBase reports, drug usage, patient and adverse-effect structures. This demonstrates executable semantic validation patterns around pharmacovigilance information artifacts.

## 4. 2025 operational extension

A 2025 Drug Safety publication, *OpenPVSignal Knowledge Graph: Pharmacovigilance Signal Reports in a Computationally Exploitable FAIR Representation* (DOI `10.1007/s40264-024-01503-8`), extends the lineage into a populated/operational Knowledge Graph and points to the same public repository and quality-assurance material.

## 5. SemRisk consequence

- Paper-1 Core novelty: not materially threatened because pharmacovigilance signal semantics are a bounded Pharma/profile/future-Risk-Intelligence concern.
- SR-C3: Pharma signal/evidence/report/provenance semantics must align/federate rather than be presented as first-of-kind.
- Future Newsium/Risk Intelligence: OpenPVSignal becomes a mandatory comparator for evidence/signal provenance and publication semantics.

## 6. License caution

The paper is CC BY while the repository carries GPL-3.0. SemRisk must bind license to the exact artifact being reused rather than assuming the article license applies to repository code/ontology artifacts.

## 7. W1 decision

`EXACT_REPOSITORY_ARTIFACT_BOUND / PROFILE_COMPARATOR`.