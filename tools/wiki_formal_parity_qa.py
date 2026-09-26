"""Check selected P1-R2 ID parity across source, generated graph and Wiki draft.

This does not inspect the live GitHub Wiki or a Pages deployment.
"""
import csv
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
ids = ("SR-CPT-001", "SR-CPT-006", "SR-CPT-007", "SR-CPT-033", "SR-CPT-035", "SR-CPT-036")
rows = {r["semantic_id"]: r for r in csv.DictReader(
    (ROOT / "docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv").open())}
index = (ROOT / "docs/ontology/generated/p1-r2-generated-reference.md").read_text()
wiki = (ROOT / "docs/wiki/pages/Semantic-Architecture.md").read_text()
graph = Graph().parse(ROOT / "docs/ontology/generated/p1-r2-asserted-closure.nt", format="nt")
local_graphs = {}

for semantic_id in ids:
    row = rows[semantic_id]
    term = URIRef(row["iri"])
    local = local_graphs.setdefault(row["source_path"], Graph().parse(ROOT / row["source_path"], format="turtle"))
    assert (term, RDF.type, OWL.Class) in local and (term, RDF.type, OWL.Class) in graph, semantic_id
    assert any(str(label) == row["label"] for label in graph.objects(term, RDFS.label)), semantic_id
    assert f"### `{semantic_id}` — {row['label']}" in index, semantic_id
    assert f"`{semantic_id}`" in wiki, semantic_id

for left, right in (("SR-CPT-006", "SR-CPT-007"),
                    ("SR-CPT-033", "SR-CPT-001"),
                    ("SR-CPT-035", "SR-CPT-036")):
    a, b = (URIRef(rows[x]["iri"]) for x in (left, right))
    assert (a, OWL.disjointWith, b) in graph or (b, OWL.disjointWith, a) in graph, (left, right)

print("SEM_RISK_WIKI_DRAFT_FORMAL_PARITY_PASS | 6 IDs; 3 explicit disjointness pairs; source/generated/draft only")
