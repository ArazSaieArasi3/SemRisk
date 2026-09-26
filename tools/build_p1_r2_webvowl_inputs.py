#!/usr/bin/env python3
"""Build source-bound inputs for the SemRisk P1-R2 WebVOWL candidate.

This script never mutates canonical ontology source. It derives two visualization
inputs from the exact asserted closure produced under issue #115:
1) local-scope: local SemRisk entities plus blank-node closure and explicit
   external boundary references;
2) import-scope: the complete asserted import closure.

Neither graph is an OWL entailment closure.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

ROOT = Path(__file__).resolve().parents[1]
FULL_NT = ROOT / "docs/ontology/generated/p1-r2-asserted-closure.nt"
CLOSURE_MANIFEST = ROOT / "docs/ontology/generated/p1-r2-closure-manifest.json"
INVENTORY = ROOT / "docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv"
OUT = ROOT / "build/webvowl"

EXPECTED_GRAPH_SHA256 = "7f190ca4729b3b66aeb8146d89b71bfbacc9483ef57580cb05be8cd702215a8a"
EXPECTED_LOCAL_CLASSES = 35
EXPECTED_LOCAL_OBJECT_PROPERTIES = 37
EXPECTED_LOCAL_SKOS = 4
EXPECTED_LOCAL_ENTITIES = 76
EXPECTED_FULL_TRIPLES = 1409
EXPECTED_FULL_CLASSES = 93
EXPECTED_FULL_OBJECT_PROPERTIES = 77

SRV = Namespace("urn:semrisk:visualization:")
DCT = Namespace("http://purl.org/dc/terms/")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_inventory():
    rows = list(csv.DictReader(INVENTORY.open(encoding="utf-8")))
    local_iris = {URIRef(r["iri"]) for r in rows}
    classes = {URIRef(r["iri"]) for r in rows if r["rdf_type"] == "owl:Class"}
    props = {URIRef(r["iri"]) for r in rows if r["rdf_type"] == "owl:ObjectProperty"}
    skos = {URIRef(r["iri"]) for r in rows if r["rdf_type"] == "skos:Concept"}
    modules = sorted({r["module"] for r in rows})
    return rows, local_iris, classes, props, skos, modules


def add_blank_node_closure(source: Graph, target: Graph, seed_nodes: set[BNode]) -> None:
    pending = list(seed_nodes)
    seen: set[BNode] = set()
    while pending:
        node = pending.pop()
        if node in seen:
            continue
        seen.add(node)
        for triple in source.triples((node, None, None)):
            target.add(triple)
            if isinstance(triple[2], BNode):
                pending.append(triple[2])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    closure_manifest = json.loads(CLOSURE_MANIFEST.read_text(encoding="utf-8"))
    actual_sha = sha256(FULL_NT)
    if actual_sha != EXPECTED_GRAPH_SHA256:
        raise SystemExit(f"asserted graph SHA-256 drift: {actual_sha}")
    if closure_manifest["canonical_nt_sha256"] != EXPECTED_GRAPH_SHA256:
        raise SystemExit("closure manifest SHA-256 disagrees with pinned P1-R2 graph")

    full = Graph()
    full.parse(FULL_NT, format="nt")

    full_classes = set(full.subjects(RDF.type, OWL.Class))
    full_props = set(full.subjects(RDF.type, OWL.ObjectProperty))
    if len(full) != EXPECTED_FULL_TRIPLES:
        raise SystemExit(f"expected {EXPECTED_FULL_TRIPLES} triples, got {len(full)}")
    if len(full_classes) != EXPECTED_FULL_CLASSES:
        raise SystemExit(f"expected {EXPECTED_FULL_CLASSES} full-scope classes, got {len(full_classes)}")
    if len(full_props) != EXPECTED_FULL_OBJECT_PROPERTIES:
        raise SystemExit(
            f"expected {EXPECTED_FULL_OBJECT_PROPERTIES} full-scope object properties, got {len(full_props)}"
        )

    rows, local_iris, local_classes, local_props, local_skos, modules = load_inventory()
    if (len(local_classes), len(local_props), len(local_skos), len(local_iris)) != (
        EXPECTED_LOCAL_CLASSES,
        EXPECTED_LOCAL_OBJECT_PROPERTIES,
        EXPECTED_LOCAL_SKOS,
        EXPECTED_LOCAL_ENTITIES,
    ):
        raise SystemExit(
            "source inventory drift: "
            f"classes={len(local_classes)}, objectProperties={len(local_props)}, "
            f"skos={len(local_skos)}, entities={len(local_iris)}"
        )

    local = Graph()
    blank_seeds: set[BNode] = set()
    external_refs: set[URIRef] = set()

    for subject in local_iris:
        for s, p, o in full.triples((subject, None, None)):
            local.add((s, p, o))
            if isinstance(o, BNode):
                blank_seeds.add(o)
            elif isinstance(o, URIRef) and o not in local_iris:
                external_refs.add(o)

    add_blank_node_closure(full, local, blank_seeds)

    # Preserve labels for referenced external classes/properties so the boundary is
    # readable without importing their complete semantics.
    for ext in external_refs:
        for p in (RDFS.label,):
            for triple in full.triples((ext, p, None)):
                local.add(triple)

    wrapper = URIRef("urn:semrisk:ontology:webvowl-local:0.1.0-rc.1")
    local.add((wrapper, RDF.type, OWL.Ontology))
    local.add((wrapper, RDFS.label, Literal("SemRisk P1-R2 local visualization scope", lang="en")))
    local.add((wrapper, DCT.description, Literal(
        "Derived visualization input: 76 local SemRisk entities with external boundary references; no imported declaration closure and no inferred axioms.",
        lang="en",
    )))
    local.add((wrapper, SRV.sourceGraphSha256, Literal(EXPECTED_GRAPH_SHA256)))
    local.add((wrapper, SRV.scope, Literal("LOCAL_SEMRISK_ASSERTED")))

    local_ttl = OUT / "p1-r2-webvowl-local.ttl"
    import_ttl = OUT / "p1-r2-webvowl-import-closure.ttl"
    local.serialize(local_ttl, format="turtle")
    full.serialize(import_ttl, format="turtle")

    manifest = {
        "schema_version": "1.0",
        "candidate": "P1-R2/0.1.0-rc.1",
        "canonical_source_commit": "dfdd7ca68c7fae460f5764afc8d9965aa00c20ae",
        "asserted_graph_sha256": EXPECTED_GRAPH_SHA256,
        "asserted_graph_triples": len(full),
        "scope": {
            "local": {
                "file": str(local_ttl.relative_to(ROOT)),
                "sha256": sha256(local_ttl),
                "local_class_count": len(local_classes),
                "local_object_property_count": len(local_props),
                "local_skos_concept_count": len(local_skos),
                "local_entity_count": len(local_iris),
                "modules": modules,
                "external_reference_count": len(external_refs),
                "policy": "Local entity subjects plus blank-node closure; external labels only; owl:imports omitted.",
            },
            "import_closure": {
                "file": str(import_ttl.relative_to(ROOT)),
                "sha256": sha256(import_ttl),
                "class_declarations": len(full_classes),
                "object_property_declarations": len(full_props),
                "triples": len(full),
                "policy": "Complete asserted import closure including vendored gUFO; not an entailment closure.",
            },
        },
        "converter": {
            "project": "VisualDataWeb/OWL2VOWL",
            "version_label": "0.3.7 code line",
            "pinned_commit": "c6331c4c79b0034b8537a11cccd1a6587cedb0b9",
            "license": "MIT",
        },
        "viewer": {
            "project": "VisualDataWeb/WebVOWL",
            "release": "v1.1.7",
            "pinned_commit": "28e7dd9540622e8cb723dc000824b5eef5ae775f",
            "license": "MIT",
        },
        "route_candidate": "/ontology-explorer/0.1.0-rc.1/",
        "authority": "DERIVED_VISUALIZATION_ONLY",
    }
    (OUT / "p1-r2-webvowl-input-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print("SEM_RISK_WEBVOWL_INPUTS_PASS")
    print(json.dumps(manifest["scope"], indent=2))


if __name__ == "__main__":
    main()
