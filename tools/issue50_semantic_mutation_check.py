#!/usr/bin/env python3
"""Deterministic negative-control detector for SemRisk Issue #50.

This script succeeds only when the synthetic semantic mutation pack is parseable,
all predeclared semantic defects are detected, and the parser negative control is
rejected as expected. It never imports mutation artifacts into the canonical
ontology candidate.
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

# NC-PARSE-001 is deliberately malformed Turtle. The expected outcome is
# defined independently of the canonical ontology: an RDF/Turtle parser must
# reject an unterminated IRI token. Keeping it inline prevents a deliberately
# invalid *.ttl artifact from being accidentally consumed by repository-wide
# checksum/ontology discovery while preserving the exact mutation bytes here.
NC_PARSE_001 = b"@prefix ex: <urn:semrisk:test:> .\nex:broken a <urn:semrisk:unterminated .\n"


def parser_negative_control() -> bool:
    g = Graph()
    try:
        g.parse(data=NC_PARSE_001, format="turtle")
    except Exception:
        return True
    return False


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

    # NC-SEM-004 remains represented by its stable mutation specification in
    # the pack; its actual missing-entailment execution is performed by the
    # dedicated reasoner harness later in Semantic CI.
    marker = URIRef(MUT + "NC-SEM-004")
    marker_present = any(g.triples((marker, RDF.type, None)))

    if missing:
        print("FAIL: expected semantic defects not detected: " + ", ".join(missing))
        return 1
    if not marker_present:
        print("FAIL: NC-SEM-004 mutation specification is missing")
        return 1
    if not parser_negative_control():
        print("FAIL: NC-PARSE-001 malformed Turtle unexpectedly parsed successfully")
        return 1

    print("PASS: detected NC-SEM-001..003; NC-SEM-004 specification present; NC-PARSE-001 malformed Turtle rejected as expected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
