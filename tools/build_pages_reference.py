"""Build and check an offline, versioned Pages candidate from exact SemRisk sources.

No deployment is performed. The registry pins source blobs and the output digest;
changing a frozen route requires a new version entry instead of overwriting it.
"""

import argparse
import csv
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("docs/ontology/pages-version-registry-v0.1.json")
INVENTORY = Path("docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv")
MANIFEST = Path("docs/ontology/generated/p1-r2-closure-manifest.json")
CRITICAL = ("SR-CPT-001", "SR-CPT-006", "SR-CPT-007", "SR-CPT-033", "SR-CPT-035", "SR-CPT-036")
STRUCTURAL = (RDFS.subClassOf, RDFS.domain, RDFS.range, RDFS.subPropertyOf,
              OWL.inverseOf, OWL.disjointWith, OWL.equivalentClass)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def clean(value):
    return html.escape(str(value), quote=True)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError("Duplicate HTML ID: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.hrefs.append(attrs["href"])


def build(version):
    source_ref = version["source_commit"]
    if len(source_ref) != 40 or any(x not in "0123456789abcdef" for x in source_ref):
        raise ValueError("A complete exact source commit is required")
    manifest = json.loads((ROOT / MANIFEST).read_text())
    if manifest["candidate"] != "P1-R2/" + version["id"]:
        raise ValueError("Candidate version mismatch")
    if manifest["canonical_nt_sha256"] != version["asserted_graph_sha256"]:
        raise ValueError("Asserted graph digest mismatch")
    graph_file = ROOT / "docs/ontology/generated/p1-r2-asserted-closure.nt"
    if sha256(graph_file.read_bytes()) != version["asserted_graph_sha256"]:
        raise ValueError("Asserted graph file drift")
    for file in manifest["files"]:
        if blob_sha((ROOT / file["path"]).read_bytes()) != file["git_blob_sha"]:
            raise ValueError("Source blob drift: " + file["path"])
    rows = list(csv.DictReader((ROOT / INVENTORY).open(newline="")))
    if len(rows) != 76 or len({r["semantic_id"] for r in rows}) != 76:
        raise ValueError("Local entity inventory must contain 76 unique IDs")
    for row in rows:
        source = next((f for f in manifest["files"] if f["path"] == row["source_path"]), None)
        if source is None or source["git_blob_sha"] != row["source_blob_sha"]:
            raise ValueError("Inventory source blob mismatch: " + row["semantic_id"])
    graph = Graph().parse(graph_file, format="nt")
    if len(graph) != manifest["unique_asserted_triples"]:
        raise ValueError("Asserted graph count mismatch")
    wiki = (ROOT / "docs/wiki/pages/Semantic-Architecture.md").read_text()
    for semantic_id in CRITICAL:
        if f"`{semantic_id}`" not in wiki or semantic_id not in {r["semantic_id"] for r in rows}:
            raise ValueError("Critical ID Wiki/source drift: " + semantic_id)
    for left, right in (("SR-CPT-006", "SR-CPT-007"),
                        ("SR-CPT-033", "SR-CPT-001"),
                        ("SR-CPT-035", "SR-CPT-036")):
        a, b = (URIRef("urn:semrisk:entity:" + x) for x in (left, right))
        if (a, OWL.disjointWith, b) not in graph and (b, OWL.disjointWith, a) not in graph:
            raise ValueError("Critical disjointness drift: " + left + "/" + right)

    repo = "https://github.com/ArazSaieArasi3/SemRisk/blob/" + source_ref + "/"
    lines = ["<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<meta name="robots" content="noindex,nofollow">',
             '<title>SemRisk P1-R2 candidate formal reference</title>',
             "<style>",
             ':root{color-scheme:light dark;font:16px/1.55 system-ui,sans-serif;max-width:76rem;margin:auto;padding:1.2rem}',
             'body{background:#fff;color:#17212b}a{color:#0b538a}a:focus-visible{outline:3px solid #cc7a00;outline-offset:3px}',
             'table{border-collapse:collapse;width:100%}th,td{border:1px solid #7b8794;padding:.55rem;text-align:left;vertical-align:top}',
             'th{background:#dce9f2}code{overflow-wrap:anywhere}section{border-top:2px solid #7b8794;padding:1rem 0}',
             '@media(max-width:52rem){table,thead,tbody,tr,th,td{display:block}thead{position:absolute;clip:rect(0 0 0 0)}td:before{content:attr(data-label) ": ";font-weight:700}}',
             '@media(prefers-color-scheme:dark){body{background:#14202b;color:#eef3f7}a{color:#91caff}th{background:#233e52}th,td,section{border-color:#8094a5}}',
             "</style>", "</head>", "<body>",
             '<main><h1>SemRisk P1-R2 formal reference</h1>',
             '<p><strong>Candidate 0.1.0-rc.1 — offline Pages bundle, not deployed or released.</strong> This is a generated projection of the asserted graph. Canonical Turtle sources and governed evidence remain authoritative. No OWL entailment, human validation or publication decision is implied.</p>',
             '<p>Source commit: <code>' + clean(source_ref) + '</code>. Asserted graph SHA-256: <code>' + clean(version["asserted_graph_sha256"]) + '</code>. Seven catalog-resolved files, ' + str(len(graph)) + ' unique asserted triples, 76 local declarations.</p>',
             '<nav aria-label="Page sections"><a href="#sources">Sources</a> · <a href="#formal">FD-A–FD-J</a> · <a href="#entities">Entities</a> · <a href="#limits">Limits</a></nav>',
             '<section id="sources"><h2>Exact sources and imports</h2><ul>']
    for f in manifest["files"]:
        path = f["path"]
        lines.append('<li><a href="' + clean(repo + path) + '"><code>' + clean(path) + '</code></a> — Git blob <code>' + clean(f["git_blob_sha"]) + '</code>; imports: ' + clean(", ".join(f["imports"]) or "none") + '</li>')
    lines += ['</ul></section>', '<section id="formal"><h2>Curated interpretation</h2>',
              '<p><a href="' + clean(repo + 'docs/ontology/formal-ontology-description-p1-r2-v0.2.md') + '">FD-A–FD-J formal description</a> explains identity, modules, selected axioms, SHACL, rules, reasoning limits, conceptual trace and CQs. This generated index is a separate read-only view.</p></section>',
              '<section id="entities"><h2>Local declarations</h2>',
              '<p>Jump to critical distinctions: ' + ' · '.join('<a href="#' + x + '">' + x + '</a>' for x in CRITICAL) + '</p>']
    for row in sorted(rows, key=lambda x: x["semantic_id"]):
        subject = URIRef(row["iri"])
        rdf_type = {"owl:Class": OWL.Class, "owl:ObjectProperty": OWL.ObjectProperty,
                    "skos:Concept": URIRef("http://www.w3.org/2004/02/skos/core#Concept")}[row["rdf_type"]]
        if (subject, RDF.type, rdf_type) not in graph:
            raise ValueError("Missing declared type in graph: " + row["semantic_id"])
        assertions = []
        for predicate in STRUCTURAL:
            for obj in graph.objects(subject, predicate):
                assertions.append((predicate.split("#")[-1], str(obj) if isinstance(obj, URIRef) else "anonymous expression in full graph"))
        assertions.sort()
        source_link = repo + row["source_path"]
        lines += ['<article id="' + clean(row["semantic_id"]) + '"><h3><code>' + clean(row["semantic_id"]) + '</code> — ' + clean(row["label"]) + '</h3>',
                  '<p>' + clean(row["rdf_type"]) + ' · ' + clean(row["module"]) + ' · <a href="' + clean(source_link) + '">source</a></p>',
                  '<ul>' + ''.join('<li><code>' + clean(p) + '</code>: <code>' + clean(o) + '</code></li>' for p, o in assertions) + '</ul></article>']
    lines += ['</section><section id="limits"><h2>Scope and nonclaims</h2>',
              '<p>The displayed statements are asserted across the catalog-resolved graph. External gUFO terms and anonymous expressions are preserved in the repository graph, not expanded into this local-ID index. SHACL validation and SQL constraints are separate. This candidate is not a live Wiki, deployed Pages site, independent domain validation or scholarly release.</p>',
              '<p><a href="' + clean(repo + 'docs/ontology/generated/p1-r2-generated-reference.md') + '">Complete repository index and canonical graph</a> · <a href="' + clean(repo + 'docs/ontology/generated/p1-r2-closure-manifest.json') + '">source manifest</a></p>',
              '</section></main></body></html>', '']
    result = "\n".join(lines)
    parser = Links()
    parser.feed(result)
    if any(href.startswith("#") and href[1:] not in parser.ids for href in parser.hrefs):
        raise ValueError("Broken internal anchor")
    if len([x for x in parser.ids if x.startswith("SR-")]) != 76:
        raise ValueError("Missing entity anchor")
    if any(href.startswith("https://") and not href.startswith(repo) for href in parser.hrefs):
        raise ValueError("Unpinned external link in Pages bundle")
    for token in ("jira risk attributes", "private Jira row", "real patient", "Bearer "):
        if token.lower() in result.lower():
            raise ValueError("Possible private data marker in Pages bundle")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    registry = json.loads((ROOT / REGISTRY).read_text())
    versions = registry["versions"]
    routes = [v["route"] for v in versions]
    if len(routes) != len(set(routes)) or len({v["id"] for v in versions}) != len(versions):
        raise ValueError("Version or route collision")
    for version in versions:
        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+-rc\.[0-9]+", version["id"]):
            raise ValueError("Invalid candidate version ID")
        route = "ontology/" + version["id"] + "/"
        if version["route"] != "/" + route or version["state"] != "OFFLINE_CANDIDATE_NOT_DEPLOYED":
            raise ValueError("Route/state mismatch")
        output = ROOT / "site" / route / "index.html"
        content = build(version)
        digest = sha256(content.encode())
        if version["html_sha256"] != digest:
            raise ValueError("Immutable version digest mismatch: " + version["id"])
        if args.check:
            if not output.is_file() or output.read_text() != content:
                raise ValueError("Versioned Pages bundle drift: " + str(output))
        else:
            if output.exists() and output.read_text() != content:
                raise ValueError("Refusing to overwrite immutable route: " + str(output))
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(content)
    print("SEM_RISK_VERSIONED_PAGES_OFFLINE_PASS | " + str(len(versions)) + " pinned version(s); no deployment")


if __name__ == "__main__":
    main()
