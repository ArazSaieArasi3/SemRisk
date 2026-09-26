"""Generate a deterministic, offline asserted import-closure reference for P1-R2.

This is a source projection, not a reasoner closure or publication release.
No remote import resolution is permitted. Run from the repository root.
"""

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree

from rdflib import BNode, Graph, Literal, URIRef
from rdflib.compare import to_canonical_graph
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
OUT = Path("docs/ontology/generated")
INVENTORY = Path("docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv")
LOCAL = "urn:semrisk:entity:"
CATALOG_NS = {"c": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def text_term(term):
    if isinstance(term, BNode):
        return "_:" + str(term)
    if isinstance(term, Literal):
        return term.n3()
    return "<" + str(term) + ">"


def build():
    rows = list(csv.DictReader((ROOT / INVENTORY).open(newline="")))
    assert len(rows) == len({r["iri"] for r in rows}) == 76
    roots = sorted({r["source_path"] for r in rows})
    catalog = ElementTree.parse(ROOT / "ontology/catalog-v001.xml")
    bindings = {}
    for entry in catalog.findall("c:uri", CATALOG_NS):
        path = Path("ontology") / entry.attrib["uri"]
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Unsafe catalog path: " + str(path))
        bindings[entry.attrib["name"]] = path.as_posix()

    graphs = {}
    visiting = set()

    def visit(path):
        if path in visiting:
            raise ValueError("Import cycle: " + path)
        if path in graphs:
            return
        visiting.add(path)
        file = ROOT / path
        if not file.is_file():
            raise ValueError("Missing local import target: " + path)
        graph = Graph().parse(data=file.read_bytes(), format="turtle")
        imports = sorted(str(x) for x in graph.objects(None, OWL.imports))
        for iri in imports:
            if iri not in bindings:
                raise ValueError("Unbound import: " + path + " -> " + iri)
            visit(bindings[iri])
        visiting.remove(path)
        graphs[path] = (graph, imports, blob_sha(file.read_bytes()))

    for path in roots:
        visit(path)
    assert len(graphs) == 7, "Expected six modules and the locally vendored gUFO dependency"
    for row in rows:
        if graphs[row["source_path"]][2] != row["source_blob_sha"]:
            raise ValueError("Source inventory blob drift: " + row["semantic_id"])

    combined = Graph()
    for graph, _, _ in graphs.values():
        combined += graph
    canonical = to_canonical_graph(combined)
    lines = sorted(canonical.serialize(format="nt").splitlines())
    assert len(lines) == len(canonical)
    nt = "\n".join(lines) + "\n"
    nt_sha = hashlib.sha256(nt.encode()).hexdigest()

    # Direct asserted local-entity statements, including cross-module statements.
    source_statements = defaultdict(list)
    for path, (graph, _, _) in sorted(graphs.items()):
        for subject, predicate, obj in graph:
            if isinstance(subject, URIRef) and str(subject).startswith(LOCAL):
                source_statements[str(subject)].append((path, str(predicate), obj))

    md = [
        "# P1-R2 generated asserted import-closure reference",
        "",
        "> Candidate `0.1.0-rc.1`; generated offline from six local modules and the catalog-bound gUFO v1.0.0 file. This is an **asserted graph**, not OWL entailment closure, independent validation or the #55 release.",
        "",
        f"The complete canonicalized graph is [`p1-r2-asserted-closure.nt`](p1-r2-asserted-closure.nt) ({len(lines)} unique triples; SHA-256 `{nt_sha}`). It includes anonymous OWL expressions and the vendored import. Local entity summaries below list direct URI-subject assertions from *all* seven files. Blank-node targets are represented in the canonical graph, while this readable index records their count rather than assigning unstable source-local identifiers.",
        "",
        "## Resolved source files",
        "",
        "| File | Git blob SHA | Asserted triples | Imports |",
        "| --- | --- | ---: | --- |",
    ]
    for path, (graph, imports, sha) in sorted(graphs.items()):
        md.append(f"| `{path}` | `{sha}` | {len(graph)} | {', '.join('`'+x+'`' for x in imports) or 'none'} |")
    md += ["", "## Locally declared entities and cross-file assertions", ""]
    for row in sorted(rows, key=lambda r: r["semantic_id"]):
        statements = source_statements[row["iri"]]
        # Cross-file assertions may add domain/range/subclass statements to an entity.
        by_path = Counter(path for path, _, _ in statements)
        structural = {str(RDF.type), str(RDFS.subClassOf), str(RDFS.domain), str(RDFS.range),
                      str(OWL.inverseOf), str(OWL.disjointWith), str(OWL.equivalentClass),
                      str(OWL.propertyDisjointWith), str(RDFS.subPropertyOf)}
        selected = sorted((path, pred, text_term(obj)) for path, pred, obj in statements
                          if pred in structural and not isinstance(obj, BNode))
        anonymous = sum(isinstance(obj, BNode) for _, _, obj in statements)
        md += [f"### `{row['semantic_id']}` — {row['label']}", "",
               f"Declared as `{row['rdf_type']}` in `{row['source_path']}`. Direct assertion counts by source: " +
               ", ".join(f"`{p}` {n}" for p, n in sorted(by_path.items())) + f". Anonymous-expression targets: {anonymous}.", ""]
        for path, pred, obj in selected:
            md.append(f"- `{pred}` → `{obj}` (`{path}`)")
        if not selected:
            md.append("- No selected structural URI-target assertion; inspect the canonical graph for labels, annotations and other predicates.")
        md.append("")
    md += ["## Interpretation boundary", "",
           "The `.nt` file contains every *asserted* triple in the catalog-resolved files. Duplicate triples across files collapse in the union. The Markdown index is a convenience projection and does not replace the Turtle sources or list every vendor term. No OWL inference, SHACL result, SQL constraint or live Wiki/Pages publication is implied.", ""]
    report = {
        "status": "ASSERTED_CLOSURE_ONLY", "candidate": "P1-R2/0.1.0-rc.1",
        "source_inventory": INVENTORY.as_posix(), "local_entity_count": len(rows),
        "source_file_count": len(graphs), "unique_asserted_triples": len(lines),
        "canonical_nt_sha256": nt_sha,
        "files": [{"path": path, "git_blob_sha": sha, "asserted_triples": len(graph), "imports": imports}
                  for path, (graph, imports, sha) in sorted(graphs.items())],
    }
    return {OUT / "p1-r2-asserted-closure.nt": nt,
            OUT / "p1-r2-generated-reference.md": "\n".join(md),
            OUT / "p1-r2-closure-manifest.json": json.dumps(report, indent=2, sort_keys=True) + "\n"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build()
    for path, expected in outputs.items():
        file = ROOT / path
        if args.check:
            if not file.is_file() or file.read_text() != expected:
                raise SystemExit("FORMAL_ASSERTED_REFERENCE_DRIFT: " + str(path))
        else:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(expected)
    print("SEM_RISK_ASSERTED_IMPORT_CLOSURE_PASS | " +
          str(json.loads(outputs[OUT / "p1-r2-closure-manifest.json"])["unique_asserted_triples"]) +
          " unique asserted triples; 7 local files; 76 local entities")


if __name__ == "__main__":
    main()
