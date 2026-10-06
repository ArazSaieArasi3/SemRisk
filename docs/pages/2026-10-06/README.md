# Ontology-only Wiki and Pages publication candidate

Source: `67247f13ba5d0c7d32163f2b3e848af15067d92e`. This publication scope is ontology documentation, not a manuscript, scholarly release, license grant or scientific acceptance.

The exact 41-file deployment allowlist is bound by `publication-byte-lock.json`: searchable 47-concept and 40-relation catalogs, 116-term asserted reference, FD-A–FD-J interpretation, 15 existing canonical diagrams, a bounded rc.4 source tutorial, current and historical documentation routes, and reused WebVOWL runtime with explicit graphical omissions. All 100 frozen source inputs match that Git commit. No unpublished manuscript, manuscript projection, original private workbook or unpublished print companion is included. The deployment must never use the repository root or an unrestricted `docs/` folder as its source.

## Reproduce

Install `rdflib==7.6.0` and `Markdown==3.9`, then run:

```
python tools/build_public_ontology_docs.py
python tools/build_rc4_safe_explorer.py
python tools/build_public_wiki_docs.py
python tools/check_public_ontology_docs.py --stage /new/empty/output-directory
```

The stage path must be empty. The checker rejects source/output drift, unexpected files, unsafe links, invented graph endpoints, changed subclass edges and runtime injection. Existing immutable routes are preserved; the new `docs-20261006` paths distinguish this documentation revision. Fifteen corruption controls must reject. The documented tutorial runs in CI using exactly its published Python block.

## Explorer scope

All 116 local declarations are searchable in the formal term index. The graphical view shows 46 local classes and the 24 object properties with one explicitly asserted named domain/range pair. The remaining 26 object properties and all eight datatype properties are index-only. Governance, Pharma and Mappings have explicit index routes rather than fabricated graph endpoints. Five graph presets keep source ownership separate from context references. Enumeration closure, anonymous axioms, metatypes, disjointness visualization, property characteristics and complete imported semantics remain outside the graph representation.

WebVOWL 1.1.7 is reused; its renderer is not OntoUML. Converter/upload implementations and arbitrary URL/hash loading are disabled. Editing is forced off; only allowlisted local preset GETs remain. Upstream notices and gUFO CC BY 4.0 attribution are preserved. No SemRisk root reuse license is selected.

## Publication and acceptance

This source-controlled candidate alone is not proof of deployment. Exact-head source/build/browser CI and independent technical review precede merge. Pages must be configured to a dedicated reviewed documentation-only branch, then the real URL must return all exact manifest bytes. Wiki pages require published-body readback and real navigation checks. Record these outcomes in a dated receipt after execution, never in advance.

Independent reader protocols remain NOT_EXECUTED. Human/domain validation, independent transfer, full current SQL parity, complete OntoUML acceptance, manuscript publication and final scholarly release/license/availability decisions remain separate. No whole issue or author requirement is accepted merely because this bundle builds.

The current Wiki manuscript navigation link was removed under the owner's instruction on 2026-10-06. Historical repository/Wiki content was not deleted or rewritten; removing navigation is not a privacy-restoration claim.
