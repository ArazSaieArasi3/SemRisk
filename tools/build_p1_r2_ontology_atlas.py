"""Deterministic SVG atlas of every locally declared P1-R2 semantic ID.

The atlas is a source projection, not an OntoUML model or imported OWL closure.
"""
import argparse
import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = Path("docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv")
OUTPUT = Path("docs/ontology/diagrams/p1-r2-local-ontology-atlas-v0.1.svg")
RELATIONS_OUTPUT = Path("docs/ontology/diagrams/p1-r2-local-relations-v0.1.svg")
SOURCE_REF = "c17cc111f02309270a60474623259cefcf907c6f"
MODULES = ("Core", "Enterprise", "Method", "Governance", "Pharma", "Mappings")
TYPE_ORDER = ("owl:Class", "owl:ObjectProperty", "skos:Concept")
COLORS = {
    "Core": ("#e8f3ff", "#14558a"), "Enterprise": ("#e9f8f2", "#16684c"),
    "Method": ("#fff0e0", "#9b5310"), "Governance": ("#f3edff", "#68409a"),
    "Pharma": ("#ffecef", "#a03953"), "Mappings": ("#edf2f4", "#455763"),
}
TYPES = {"owl:Class": OWL.Class, "owl:ObjectProperty": OWL.ObjectProperty,
         "skos:Concept": SKOS.Concept}


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def short(uri):
    value = str(uri)
    if value.startswith("urn:semrisk:entity:"):
        return value.rsplit(":", 1)[-1]
    if value.startswith("http://purl.org/nemo/gufo#"):
        return "gufo:" + value.split("#", 1)[1]
    return value


def text(x, y, value, size=16, color="#172632", weight="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(str(value))}</text>'


def card(x, y, w, h, fill, stroke, radius=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def build():
    rows = list(csv.DictReader((ROOT / INVENTORY).open(newline="")))
    if len(rows) != 76 or len({r["semantic_id"] for r in rows}) != 76:
        raise ValueError("76 unique source inventory IDs required")
    if Counter(r["rdf_type"] for r in rows) != Counter({"owl:Class": 35, "owl:ObjectProperty": 37, "skos:Concept": 4}):
        raise ValueError("Local declaration type count drift")
    if set(r["module"] for r in rows) != set(MODULES):
        raise ValueError("Module inventory drift")
    paths = sorted({r["source_path"] for r in rows})
    graph = Graph()
    for path in paths:
        data = (ROOT / path).read_bytes()
        for r in rows:
            if r["source_path"] == path and r["source_blob_sha"] != blob_sha(data):
                raise ValueError("Source blob mismatch: " + r["semantic_id"])
        graph.parse(data=data, format="turtle")
    for r in rows:
        if (URIRef(r["iri"]), RDF.type, TYPES[r["rdf_type"]]) not in graph:
            raise ValueError("Missing declaration: " + r["semantic_id"])
    pairs = sorted({tuple(sorted((short(a), short(b)))) for a, b in graph.subject_objects(OWL.disjointWith)
                    if short(a).startswith("SR-") and short(b).startswith("SR-")})
    if len(pairs) != 9:
        raise ValueError("Nine explicit local disjointness pairs expected")

    svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="3200" height="2080" viewBox="0 0 3200 2080" role="img" aria-labelledby="title desc">',
           '<title id="title">SemRisk P1-R2 local ontology atlas</title>',
           '<desc id="desc">All 76 locally declared semantic IDs, grouped by six modules: 35 OWL classes, 37 object properties, four SKOS markers. Nine selected explicit disjointness pairs appear below. Domain and range are OWL assertions, not database constraints. No cardinality is inferred.</desc>',
           '<rect width="3200" height="2080" fill="#f8fafc"/>',
           text(60, 68, "SemRisk · P1-R2 local ontology atlas", 38, weight="bold"),
           text(60, 108, "0.1.0-rc.1 candidate · 76 local declarations · six modules · asserted OWL only", 23),
           text(60, 143, "Source ref " + SOURCE_REF + " · generated from exact Turtle blobs; not an OntoUML stereotype assignment or publication release", 17, "#405466"),
           card(55, 174, 1900, 1508, *COLORS["Core"], 18),
           text(80, 219, "Core", 31, COLORS["Core"][1], "bold"),
           text(80, 251, "Owned identity and relations · declarations grouped by type; IDs remain canonical", 18)]
    by = defaultdict(list)
    for r in rows:
        by[(r["module"], r["rdf_type"])].append(r)

    def row(r, x, y, w=885):
        fill, stroke = COLORS[r["module"]]
        term = URIRef(r["iri"])
        kind = {"owl:Class": "«OWL Class»", "owl:ObjectProperty": "«Object Property»",
                "skos:Concept": "«SKOS marker»"}[r["rdf_type"]]
        signature = []
        if r["rdf_type"] == "owl:Class":
            supers = sorted(short(v) for v in graph.objects(term, RDFS.subClassOf) if isinstance(v, URIRef))
            if supers:
                signature.append("subClassOf " + ", ".join(supers))
        elif r["rdf_type"] == "owl:ObjectProperty":
            domains = sorted(short(v) for v in graph.objects(term, RDFS.domain) if isinstance(v, URIRef))
            ranges = sorted(short(v) for v in graph.objects(term, RDFS.range) if isinstance(v, URIRef))
            signature.append("D: " + (", ".join(domains) or "unspecified") + "   →   R: " + (", ".join(ranges) or "unspecified"))
        if not signature:
            signature.append("no local superclass asserted" if r["rdf_type"] == "owl:Class" else "reference marker; no local OWL class assertion")
        link = "https://github.com/ArazSaieArasi3/SemRisk/blob/" + SOURCE_REF + "/" + r["source_path"]
        return ['<a xlink:href="' + escape(link) + '">', card(x, y, w, 43, "#ffffff", stroke, 7),
                text(x + 11, y + 18, r["semantic_id"] + "  " + r["label"] + "  " + kind, 15, "#152c3a", "bold"),
                text(x + 11, y + 36, "; ".join(signature), 13, "#445765"), '</a>']

    for typ, x in (("owl:Class", 80), ("owl:ObjectProperty", 1030)):
        svg.append(text(x, 285, typ + " · " + str(len(by[("Core", typ)])), 20, COLORS["Core"][1], "bold"))
        for i, r in enumerate(sorted(by[("Core", typ)], key=lambda z: z["semantic_id"])):
            svg += row(r, x, 305 + i * 45)
    svg.append(text(80, 1632, "Core SKOS marker", 18, COLORS["Core"][1], "bold"))
    for r in by[("Core", "skos:Concept")]:
        svg += row(r, 320, 1600)

    y = 174
    for module in MODULES[1:]:
        mr = sorted((r for r in rows if r["module"] == module), key=lambda z: (TYPE_ORDER.index(z["rdf_type"]), z["semantic_id"]))
        h = 93 + len(mr) * 45
        fill, stroke = COLORS[module]
        svg += [card(1990, y, 1155, h, fill, stroke, 18), text(2014, y + 40, module + " · " + str(len(mr)) + " declarations", 26, stroke, "bold")]
        for i, r in enumerate(mr):
            svg += row(r, 2013, y + 60 + i * 45, 1109)
        y += h + 14
    svg += [card(55, 1710, 3090, 305, "#ffffff", "#617589", 14),
            text(80, 1752, "Nine explicit local owl:disjointWith pairs", 25, "#263d50", "bold")]
    for i, (a, b) in enumerate(pairs):
        x = 80 + (i % 3) * 1015
        py = 1800 + (i // 3) * 65
        svg += [card(x, py - 27, 965, 51, "#f3f6f8", "#9aaebd", 6), text(x + 15, py + 5, a + "   ⟂   " + b, 19)]
    svg += [text(80, 2043, "Legend: D/R = asserted OWL domain/range; unspecified ≠ unconstrained. No class cardinality is asserted by this diagram. External gUFO closure, SHACL, SQL and test data are outside its 76-ID denominator.", 17, "#405466"),
            '</svg>']
    result = "\n".join(svg) + "\n"
    # Every ID appears in a linked entity card; rendering must not silently omit one.
    if any(result.count(r["semantic_id"] + "  " + escape(r["label"])) != 1 for r in rows):
        raise ValueError("Missing or duplicate atlas card")
    return result


def build_relations():
    rows = list(csv.DictReader((ROOT / INVENTORY).open(newline="")))
    properties = sorted((r for r in rows if r["rdf_type"] == "owl:ObjectProperty"),
                        key=lambda r: (MODULES.index(r["module"]), r["semantic_id"]))
    if len(properties) != 37:
        raise ValueError("37 local object properties expected")
    graph = Graph()
    for path in {r["source_path"] for r in rows}:
        data = (ROOT / path).read_bytes()
        if any(r["source_blob_sha"] != blob_sha(data) for r in rows if r["source_path"] == path):
            raise ValueError("Source blob drift: " + path)
        graph.parse(data=data, format="turtle")
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="3200" height="1930" viewBox="0 0 3200 1930" role="img" aria-labelledby="title desc">',
           '<title id="title">SemRisk P1-R2 asserted object-property relation map</title>',
           '<desc id="desc">All 37 locally declared object properties. For each, the asserted OWL domain and range are shown, or explicitly marked not asserted. Arrows indicate domain to relation to range, not data flow or cardinality.</desc>',
           '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M1,1 L8,4.5 L1,8 Z" fill="#617589"/></marker></defs>',
           '<rect width="3200" height="1930" fill="#f8fafc"/>',
           text(60, 65, "SemRisk · asserted relation map", 37, weight="bold"),
           text(60, 105, "37 local OWL object properties · 19 asserted domain statements · 25 asserted range statements", 22),
           text(60, 139, "P1-R2 0.1.0-rc.1 · source ref " + SOURCE_REF + " · missing domain/range means not asserted locally", 17, "#405466"),
           text(70, 187, "OWL domain (if asserted)", 21, "#263d50", "bold"),
           text(1110, 187, "Object property · module", 21, "#263d50", "bold"),
           text(2250, 187, "OWL range (if asserted)", 21, "#263d50", "bold")]
    domain_count = range_count = 0
    for i, r in enumerate(properties):
        y = 209 + i * 44
        term = URIRef(r["iri"])
        domains = sorted(short(o) for o in graph.objects(term, RDFS.domain) if isinstance(o, URIRef))
        ranges = sorted(short(o) for o in graph.objects(term, RDFS.range) if isinstance(o, URIRef))
        domain_count += len(domains)
        range_count += len(ranges)
        if (term, RDF.type, OWL.ObjectProperty) not in graph:
            raise ValueError("Missing object property declaration: " + r["semantic_id"])
        fill, stroke = COLORS[r["module"]]
        source = "https://github.com/ArazSaieArasi3/SemRisk/blob/" + SOURCE_REF + "/" + r["source_path"]
        svg += [f'<line x1="970" y1="{y+20}" x2="1080" y2="{y+20}" stroke="#617589" stroke-width="2" marker-end="url(#arrow)"/>',
                f'<line x1="2120" y1="{y+20}" x2="2230" y2="{y+20}" stroke="#617589" stroke-width="2" marker-end="url(#arrow)"/>',
                card(70, y, 900, 40, "#ffffff", "#93a7b6", 5),
                text(82, y + 26, ", ".join(domains) if domains else "not asserted locally", 17),
                '<a xlink:href="' + escape(source) + '">', card(1090, y, 1030, 40, fill, stroke, 5),
                text(1103, y + 26, r["semantic_id"] + "  " + r["label"] + "  ·  " + r["module"], 17, "#172632", "bold"), '</a>',
                card(2240, y, 900, 40, "#ffffff", "#93a7b6", 5),
                text(2252, y + 26, ", ".join(ranges) if ranges else "not asserted locally", 17)]
    if (domain_count, range_count) != (19, 25):
        raise ValueError("Domain/range assertion count drift")
    svg += [text(70, 1883, "Arrows express the asserted property signature only. OWL domain/range infer types; they do not validate row completeness. Cardinalities, SHACL, SQL, inverses and inferred/imported effects are separate.", 17, "#405466"), '</svg>']
    return "\n".join(svg) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    for relative, result in ((OUTPUT, build()), (RELATIONS_OUTPUT, build_relations())):
        path = ROOT / relative
        if args.check:
            if not path.is_file() or path.read_text() != result:
                raise SystemExit("ONTOLOGY_ATLAS_DRIFT: " + str(path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(result)
    print("SEM_RISK_LOCAL_ONTOLOGY_ATLAS_PASS | 76 IDs, 37 relations, six modules, nine disjoint pairs")


if __name__ == "__main__":
    main()
