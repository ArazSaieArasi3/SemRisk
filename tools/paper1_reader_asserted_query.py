#!/usr/bin/env python3
"""A small reader task over the pinned *asserted* P1-R2 source graph.

This is an exact-source lookup exercise, not OWL reasoning or semantic validation.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

CORE = "ontology/core/semrisk-core-v0.1.0-rc.1.ttl"
MANIFEST = "docs/ontology/generated/p1-r2-closure-manifest.json"
GRAPH = "docs/ontology/generated/p1-r2-asserted-closure.nt"
INVENTORY = "docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
OWL_CLASS = "http://www.w3.org/2002/07/owl#Class"
OWL_OBJECT_PROPERTY = "http://www.w3.org/2002/07/owl#ObjectProperty"
OWL_DISJOINT = "http://www.w3.org/2002/07/owl#disjointWith"
RDFS_DOMAIN = "http://www.w3.org/2000/01/rdf-schema#domain"
RDFS_RANGE = "http://www.w3.org/2000/01/rdf-schema#range"


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def iri(s):
    return f"<{s}>"


def triple(s, p, o):
    return f"{iri(s)} {iri(p)} {iri(o)} ."


def run(root):
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    assert manifest["status"] == "ASSERTED_CLOSURE_ONLY", "Not an asserted-closure manifest"
    assert manifest["unique_asserted_triples"] == 1409, "Unexpected graph scope"
    files = {x["path"]: x for x in manifest["files"]}
    core_bytes = (root / CORE).read_bytes()
    assert git_blob_sha(core_bytes) == files[CORE]["git_blob_sha"], "Core source blob drift"
    graph_bytes = (root / GRAPH).read_bytes()
    assert hashlib.sha256(graph_bytes).hexdigest() == manifest["canonical_nt_sha256"], "Graph SHA-256 drift"
    graph = set(graph_bytes.decode("utf-8").splitlines())
    assert len(graph) == manifest["unique_asserted_triples"], "Graph triple-count drift"
    with (root / INVENTORY).open(newline="", encoding="utf-8") as fh:
        rows = {r["semantic_id"]: r for r in csv.DictReader(fh)}
    scenario, event, relation = (rows[x] for x in ("SR-CPT-006", "SR-CPT-007", "SR-REL-003"))
    assert all(r["source_path"] == CORE and r["source_blob_sha"] == files[CORE]["git_blob_sha"]
               for r in (scenario, event, relation)), "Inventory/Core source binding drift"
    assert scenario["label"] == "Risk Scenario" and event["label"] == "Risk Event"
    assert relation["label"] == "realizedAs", "Selected reader-task identity drift"
    a, b, p = scenario["iri"], event["iri"], relation["iri"]
    for line in (triple(a, RDF_TYPE, OWL_CLASS), triple(b, RDF_TYPE, OWL_CLASS),
                 triple(p, RDF_TYPE, OWL_OBJECT_PROPERTY), triple(p, RDFS_DOMAIN, a),
                 triple(p, RDFS_RANGE, b)):
        assert line in graph, f"Missing asserted triple: {line}"
    assert (triple(a, OWL_DISJOINT, b) in graph or
            triple(b, OWL_DISJOINT, a) in graph), "Scenario/Event disjointness not asserted"
    print("SEM_RISK_READER_ASSERTED_QUERY_PASS | P1-R2/0.1.0-rc.1; 7 files; 1,409 asserted triples")
    print("SR-CPT-006 Risk Scenario and SR-CPT-007 Risk Event: local Core OWL classes; explicit disjointWith")
    print("SR-REL-003 realizedAs: asserted domain Scenario, range Event; source ontology/core/semrisk-core-v0.1.0-rc.1.ttl")
    print("BOUNDARY: asserted source lookup only; no inferred closure, domain validation, cardinality or occurrence claim")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Exact SemRisk checkout root (default: script's repository)")
    args = parser.parse_args()
    run(args.root.resolve())
