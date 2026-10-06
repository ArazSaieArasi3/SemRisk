# Post-calculation ownership-scope clarification

Independent review identified an ambiguity in the frozen protocol's phrase “local class declarations.” The intended population was already fixed by the domain/helper registries, but the completeness sentence did not explicitly distinguish locally **owned** terms from external vocabulary redeclarations inside local module files.

The seven local module files assert 47 `owl:Class` subjects: 46 SemRisk-owned terms whose IRIs begin `urn:semrisk:`, plus external `http://www.w3.org/2004/02/skos/core#Concept`. D∪H exhausts the 46 SemRisk-owned declarations. The local SKOS redeclaration is ontology scaffolding for external vocabulary, not a new SemRisk domain/helper class. Imported gUFO declarations are also outside the selected populations.

This clarification was added after the first metric calculation and must not be represented as part of the untouched pre-calculation protocol commit `7a7f50bd699985faf5e2136b9daf2d35dabe1e7b`. The original protocol file remains unchanged. No population member, formula, input ontology or computed value changed; the result now exposes the excluded external declaration explicitly and binds this clarification's hash. This is an ownership-scope clarification, not a result-driven metric selection change.
