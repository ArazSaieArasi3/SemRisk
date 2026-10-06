# Native-editor compatibility gate — 2026-10-06

This is source-level analysis, not an executed import, compiled-binary inspection or native round-trip result. No compatible native editor was available in the inspected test environment at this checkpoint. No software installation, license acceptance or external model upload was performed.

## Version-bound inputs

SemRisk's pinned official schema 1.0.2 uses a flat Project `elements`/`root` representation and `BinaryRelation`/`BinaryRelationView`. The graphical round-trip input is `diagrams/ontouml/0.2.0-rc.4/SemRisk-rc4.ontouml.json`, containing all 15 diagrams. `model-base.json` is a builder input without diagrams.

The [released OntoUML Visual Paradigm plugin 0.5.3](https://github.com/OntoUML/ontouml-vp-plugin/releases/tag/0.5.3) resolves to commit `9fc02b8162db9910f21b8713549cafce2627dad0` and requires Visual Paradigm 16.3 or later. The following checks concern that tagged source, not a compiled binary.

| Source at the pinned plugin commit | Finding |
|---|---|
| [ProjectDeserializer](https://github.com/OntoUML/ontouml-vp-plugin/blob/9fc02b8162db9910f21b8713549cafce2627dad0/src/main/java/it/unibz/inf/ontouml/vp/model/ontouml/deserialization/ProjectDeserializer.java) / ProjectSerializer | Reads and writes nested `model` and `diagrams`. |
| [DeserializerUtils](https://github.com/OntoUML/ontouml-vp-plugin/blob/9fc02b8162db9910f21b8713549cafce2627dad0/src/main/java/it/unibz/inf/ontouml/vp/model/ontouml/deserialization/DeserializerUtils.java) | Dispatches Relation/RelationView; no BinaryRelation, Note, Anchor or their view cases. |
| PackageDeserializer / DiagramDeserializer | Their accepted element/view cases do not cover the native note/anchor path required here. |
| IClassDiagramLoader / IClassLoader | Replace incoming diagram/class IDs with generated native IDs; an explicit source/native identity map would be needed. |
| [IClassDiagramTransformer](https://github.com/OntoUML/ontouml-vp-plugin/blob/9fc02b8162db9910f21b8713549cafce2627dad0/src/main/java/it/unibz/inf/ontouml/vp/model/vp2ontouml/IClassDiagramTransformer.java) | Native export covers class/association/generalization/package objects, without note/anchor export. |

Exact source blobs and local artifact hashes are recorded in [the companion audit](compatibility-20261006.json).

## Preservation consequence

SR-REL-038 is deliberately a metadata Note anchored to B-Profile and B-Core. Recasting it as an association would change its meaning. A sidecar could preserve external information but would not establish native annotation round-trip preservation. Therefore a plain JSON adapter to this released plugin cannot by itself establish full native preservation.

A bounded semantic-subset adapter could be investigated with explicit field and identity mapping; preservation has not been demonstrated. Full coverage requires an annotation-capable import/export path or a separately reviewed plugin extension handling notes/anchors in both directions. A fresh Visual Paradigm installation also introduces installation/licensing eligibility steps; no eligibility or license grant is assumed. See the [vendor FAQ](https://www.visual-paradigm.com/support/faq.jsp).

The eventual acceptance experiment remains import → save → close/reopen → export → exact identity, stereotype, endpoint, cardinality, metadata and 15-view comparison. An import-success notification alone is insufficient. Remote advanced verification/transformation services are outside this local-file round-trip scope. #33 remains open.
