#!/usr/bin/env python3
"""R1 foundational regression guardrails.

These checks prevent specific category regressions identified by the R1
specialist-style simulated foundational review. They are regression controls,
not evidence of independent expert validation or universal correctness.
"""
from pathlib import Path
from rdflib import Graph, URIRef, RDF, RDFS, OWL

ROOT = Path(__file__).resolve().parents[1]
SR = "urn:semrisk:entity:"
GUFO = "http://purl.org/nemo/gufo#"

files = sorted((ROOT / "ontology").glob("*/*.ttl"))
g = Graph()
for p in files:
    g.parse(p, format="turtle")

risk = URIRef(SR + "SR-CPT-001")
risk_source = URIRef(SR + "SR-CPT-003")
provenance = URIRef(SR + "SR-CPT-021")

def fail(msg):
    raise SystemExit("FAIL R1 guardrail: " + msg)

# G-R1-01: Risk Source is a cross-category contextual role/pattern.
for pred in (RDFS.subClassOf, OWL.equivalentClass):
    for obj in g.objects(risk_source, pred):
        if isinstance(obj, URIRef) and str(obj).startswith(GUFO):
            fail(f"Risk Source was forced under gUFO primitive via {pred}: {obj}")
for obj in g.objects(risk_source, RDF.type):
    if isinstance(obj, URIRef) and str(obj).startswith(GUFO):
        fail(f"Risk Source received gUFO metatype/stereotype: {obj}")

# G-R1-02: Provenance is a governed conceptual marker, realized through PROV-O.
if (provenance, RDF.type, OWL.Class) in g:
    fail("SR-CPT-021 Provenance became a local owl:Class")
for pred in (RDFS.subClassOf, OWL.equivalentClass):
    if any(True for _ in g.objects(provenance, pred)):
        fail(f"SR-CPT-021 Provenance received class-axiom commitment via {pred}")

# G-R1-03 / #69: Risk remains a derived SemRisk pattern rather than a
# convenience specialization of one gUFO primitive or an OWL key-driven class.
for pred in (RDFS.subClassOf, OWL.equivalentClass):
    for obj in g.objects(risk, pred):
        if isinstance(obj, URIRef) and str(obj).startswith(GUFO):
            fail(f"Risk was forced under gUFO primitive via {pred}: {obj}")
if any(True for _ in g.objects(risk, OWL.hasKey)):
    fail("Risk received owl:hasKey; mutable/operational key inference is prohibited")

print(f"PASS: parsed {len(files)} canonical ontology Turtle files")
print("PASS: Risk Source remains cross-category (no single gUFO primitive)")
print("PASS: Provenance remains PROV-O conceptual marker, not local owl:Class")
print("PASS: Risk remains derived pattern without gUFO convenience typing or owl:hasKey")
print("SEM_RISK_R1_FOUNDATIONAL_GUARDRAILS_PASS")
