#!/usr/bin/env python3
"""Deterministic negative-control detector for SemRisk Issue #50.

This script succeeds only when the synthetic mutation pack is parseable and all
predeclared semantic defects are detected. It never imports the mutation pack
into the canonical ontology candidate.
"""
from pathlib import Path
import sys
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "testdata/negative/semantic-mutation-pack-issue50-v0.1.ttl"
SR = "urn:semrisk:entity:"
MUT = "urn:semrisk:test:mutation:"

EXPECTED = {
    "NC-SEM-001": ("SR-CPT-033", OWL.equivalentClass, "SR-CPT-001"),
    "NC-SEM-002": ("SR-CPT-036", OWL.equivalentClass, "SR-CPT-035"),
    "NC-SEM-003": ("SR-CPT-018", OWL.equivalentClass, "SR-CPT-001"),
}


def main() -> int:
    g = Graph()
    try:
        g.parse(PACK, format="turtle")
    except Exception as exc:
        print(f"ERROR: mutation pack is not parseable: {exc}")
        return 2

    missing = []
    for fixture_id, (s, p, o) in EXPECTED.items():
        triple = (URIRef(SR + s), p, URIRef(SR + o))
        if triple not in g:
            missing.append(fixture_id)

    # NC-SEM-004 is deliberately a mutation specification, not a fabricated
    # reasoner result. It remains NOT_RUN until the reasoned-graph mutation
    # harness executes removal of the expected SR-CPT-017 -> SR-CPT-013 edge.
    marker = URIRef(MUT + "NC-SEM-004")
    marker_present = any(g.triples((marker, RDF.type, None)))

    if missing:
        print("FAIL: expected semantic defects not detected: " + ", ".join(missing))
        return 1
    if not marker_present:
        print("FAIL: NC-SEM-004 mutation specification is missing")
        return 1

    print("PASS: detected NC-SEM-001..003; NC-SEM-004 specification present and remains NOT_RUN pending reasoner mutation harness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
