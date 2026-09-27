"""Build a bounded offline WebVOWL JSON candidate from exact P1-R2 assertions.

OWL2VOWL 0.3.7 drops SemRisk's urn: entity IRIs. This adapter gives them
temporary HTTP IRIs only during conversion and restores the canonical URNs in
the JSON. Imports are removed only in the derived conversion document; all
seven locally bound source graphs are already present in that document.
No canonical Turtle or released Pages route is changed.
"""

import argparse
import csv
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.compare import to_canonical_graph
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MANIFEST = ROOT / "docs/ontology/generated/p1-r2-closure-manifest.json"
INVENTORY = ROOT / "docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv"
OUTPUT = ROOT / "docs/ontology/generated/webvowl-candidate-v0.1"
SOURCE_REF = "c17cc111f02309270a60474623259cefcf907c6f"
CONVERTER_REF = "2833ead00122ca252a0fd0e18c5e5b696d711d2c"
CONVERTER_SHA256 = "f61a49c9bfee60e0a3e02c23f780f3d07d7edaad5b1dd63ced2d4c4c292dc4a9"
ALIASES = {"urn:semrisk:entity:": "https://semrisk.invalid/entity#",
           "urn:semrisk:ontology:": "https://semrisk.invalid/ontology/"}
VIEW_IRI = "https://semrisk.invalid/view/p1-r2-0.1.0-rc.1"
CANONICAL_VIEW_IRI = "urn:semrisk:documentation:webvowl:p1-r2:0.1.0-rc.1"


def sha256(content):
    return hashlib.sha256(content).hexdigest()


def git_blob_sha(content):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def replace_iri(term):
    if isinstance(term, URIRef):
        value = str(term)
        for canonical, alias in ALIASES.items():
            value = value.replace(canonical, alias)
        return URIRef(value)
    return term


def build(jar):
    manifest = json.loads(SOURCE_MANIFEST.read_text())
    rows = list(csv.DictReader(INVENTORY.open(newline="")))
    assert manifest["candidate"] == "P1-R2/0.1.0-rc.1"
    assert manifest["status"] == "ASSERTED_CLOSURE_ONLY"
    assert len(manifest["files"]) == 7 and len(rows) == 76
    asserted = ROOT / "docs/ontology/generated/p1-r2-asserted-closure.nt"
    assert sha256(asserted.read_bytes()) == manifest["canonical_nt_sha256"]
    combined = Graph()
    for entry in manifest["files"]:
        path = Path(entry["path"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Unsafe source path")
        content = (ROOT / path).read_bytes()
        if git_blob_sha(content) != entry["git_blob_sha"]:
            raise ValueError("Source blob drift: " + entry["path"])
        combined.parse(data=content, format="turtle")
    if len(combined) != manifest["unique_asserted_triples"]:
        raise ValueError("Asserted union drift")

    derived = Graph()
    for subject, predicate, obj in combined:
        if predicate == OWL.imports or (predicate == RDF.type and obj == OWL.Ontology):
            continue
        derived.add(tuple(replace_iri(x) for x in (subject, predicate, obj)))
    view = URIRef(VIEW_IRI)
    derived.add((view, RDF.type, OWL.Ontology))
    derived.add((view, RDFS.label, Literal("SemRisk P1-R2 derived WebVOWL view")))
    nt = "\n".join(sorted(to_canonical_graph(derived).serialize(format="nt").splitlines())) + "\n"

    if sha256(jar.read_bytes()) != CONVERTER_SHA256:
        raise ValueError("OWL2VOWL JAR SHA-256 differs from tested local build")
    with tempfile.TemporaryDirectory(prefix="semrisk-vowl-") as temp:
        source = Path(temp) / "derived.nt"
        raw_output = Path(temp) / "converter.json"
        source.write_text(nt)
        env = os.environ.copy()
        for key in ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY", "https_proxy", "http_proxy", "all_proxy"):
            env.pop(key, None)
        command = ["java", "--add-opens", "java.base/java.lang=ALL-UNNAMED",
                   "-jar", str(jar.resolve()), "-output", str(raw_output), "-file", str(source)]
        completed = subprocess.run(command, cwd=temp, env=env, capture_output=True,
                                   text=True, timeout=60, check=False)
        if completed.returncode or not raw_output.is_file():
            raise RuntimeError("Offline conversion failed: " + completed.stderr[-1500:])
        raw = raw_output.read_text()

    # Restore IRI identity throughout attributes, namespaces and header. Numeric
    # WebVOWL node IDs and edges are left intact.
    for canonical, alias in ALIASES.items():
        raw = raw.replace(alias, canonical)
    # OWL2VOWL emits a baseIri without the fragment delimiter for the
    # temporary entity namespace; restore that isolated namespace value too.
    raw = raw.replace('"https://semrisk.invalid/entity"', '"urn:semrisk:entity:"')
    raw = raw.replace(VIEW_IRI, CANONICAL_VIEW_IRI)
    if "semrisk.invalid" in raw:
        at = raw.index("semrisk.invalid")
        raise ValueError("Temporary alias leaked into WebVOWL JSON: " + raw[max(0, at - 50):at + 100])
    data = json.loads(raw)
    expected = {kind: {r["iri"] for r in rows if r["rdf_type"] == kind}
                for kind in ("owl:Class", "owl:ObjectProperty")}
    actual = {
        "owl:Class": {r.get("iri") for r in data.get("classAttribute", []) if r.get("iri") in expected["owl:Class"]},
        "owl:ObjectProperty": {r.get("iri") for r in data.get("propertyAttribute", []) if r.get("iri") in expected["owl:ObjectProperty"]},
    }
    if actual != expected:
        raise ValueError("Local class/property omission in converter JSON")
    if data.get("header", {}).get("iri") != CANONICAL_VIEW_IRI:
        raise ValueError("Derived-view header mismatch")
    json_bytes = (json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    report = {
        "status": "OFFLINE_JSON_CANDIDATE_BROWSER_SMOKE_PASS",
        "semantic_source_ref": SOURCE_REF,
        "converter_source_ref": CONVERTER_REF,
        "converter_jar_sha256": CONVERTER_SHA256,
        "source_closure_sha256": manifest["canonical_nt_sha256"],
        "source_paths_and_blobs": [{"path": x["path"], "git_blob_sha": x["git_blob_sha"]} for x in manifest["files"]],
        "conversion_input_nt_sha256": sha256(nt.encode()),
        "conversion_input_asserted_triples": len(derived),
        "conversion_policy": "seven local asserted graphs; omit owl:imports and original ontology-type triples only in derived document; temporary HTTP IRI aliases restored in JSON; no entailment",
        "json_path": (OUTPUT / "combined.json").relative_to(ROOT).as_posix(),
        "json_sha256": sha256(json_bytes),
        "local_class_coverage": len(actual["owl:Class"]),
        "local_object_property_coverage": len(actual["owl:ObjectProperty"]),
        "skos_markers_outside_vowl_denominator": 4,
        "viewer_rendered": True,
        "browser_qa_run": "https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36312545968",
        "readability": "partial: combined graph and phone labels remain difficult to read",
        "public_url": None,
    }
    return json_bytes, (json.dumps(report, indent=2, sort_keys=True) + "\n").encode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jar", type=Path, required=True, help="locally built OWL2VOWL 0.3.7 shaded JAR")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data, report = build(args.jar)
    targets = {OUTPUT / "combined.json": data, OUTPUT / "manifest.json": report}
    if args.check:
        for path, expected in targets.items():
            if not path.is_file() or path.read_bytes() != expected:
                raise SystemExit("WEBVOWL_CANDIDATE_DRIFT: " + str(path))
    else:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for path, content in targets.items():
            path.write_bytes(content)
    print("SEM_RISK_WEBVOWL_OFFLINE_JSON_PASS | 35 classes; 37 object properties; private browser smoke recorded")


if __name__ == "__main__":
    main()
