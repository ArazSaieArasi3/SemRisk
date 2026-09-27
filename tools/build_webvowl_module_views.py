"""Build source-bound, module-only WebVOWL JSON views for offline exploration.

Each view uses the asserted triples in one SemRisk Turtle module, with imports
omitted only in its derived conversion input. References to other modules or
gUFO are therefore context stubs, not their imported definitions. The combined
seven-file JSON remains the separate asserted-union view.
"""

import argparse
import csv
import json
import os
import subprocess
import tempfile
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.compare import to_canonical_graph
from rdflib.namespace import OWL, RDF, RDFS

from build_webvowl_candidate import (
    ALIASES, CONVERTER_REF, CONVERTER_SHA256, INVENTORY, ROOT,
    SOURCE_MANIFEST, SOURCE_REF, git_blob_sha, replace_iri, sha256,
)

OUTPUT = ROOT / "docs/ontology/generated/webvowl-module-v0.1"
MODULES = ("Core", "Enterprise", "Method", "Governance", "Pharma")
VIEW_HTTP = "https://semrisk.invalid/view/p1-r2-0.1.0-rc.1/module/"
VIEW_URN = "urn:semrisk:documentation:webvowl:p1-r2:0.1.0-rc.1:module:"


def build(jar):
    if sha256(jar.read_bytes()) != CONVERTER_SHA256:
        raise ValueError("OWL2VOWL JAR differs from the pinned local build")
    source_manifest = json.loads(SOURCE_MANIFEST.read_text())
    rows = list(csv.DictReader(INVENTORY.open(newline="")))
    assert source_manifest["candidate"] == "P1-R2/0.1.0-rc.1"
    assert len(source_manifest["files"]) == 7 and len(rows) == 76
    results = {}
    reports = []
    for module in MODULES:
        source = [entry for entry in source_manifest["files"]
                  if entry["path"].startswith("ontology/" + module.lower() + "/")]
        if len(source) != 1:
            raise ValueError("Module source not uniquely pinned: " + module)
        entry = source[0]
        content = (ROOT / entry["path"]).read_bytes()
        if git_blob_sha(content) != entry["git_blob_sha"]:
            raise ValueError("Source blob drift: " + entry["path"])
        graph = Graph().parse(data=content, format="turtle")
        derived = Graph()
        for subject, predicate, obj in graph:
            if predicate == OWL.imports or (predicate == RDF.type and obj == OWL.Ontology):
                continue
            derived.add(tuple(replace_iri(term) for term in (subject, predicate, obj)))
        slug = module.lower()
        view_iri = VIEW_HTTP + slug
        derived.add((URIRef(view_iri), RDF.type, OWL.Ontology))
        derived.add((URIRef(view_iri), RDFS.label, Literal("SemRisk " + module + " source-only view")))
        nt = ("\n".join(sorted(to_canonical_graph(derived).serialize(format="nt").splitlines())) + "\n").encode()
        with tempfile.TemporaryDirectory(prefix="semrisk-vowl-module-") as temp:
            source_nt = Path(temp) / "derived.nt"
            output_json = Path(temp) / "converter.json"
            source_nt.write_bytes(nt)
            env = os.environ.copy()
            for key in ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY",
                        "https_proxy", "http_proxy", "all_proxy"):
                env.pop(key, None)
            command = ["java", "--add-opens", "java.base/java.lang=ALL-UNNAMED",
                       "-jar", str(jar.resolve()), "-output", str(output_json),
                       "-file", str(source_nt)]
            run = subprocess.run(command, cwd=temp, env=env, capture_output=True,
                                 text=True, timeout=60, check=False)
            if run.returncode or not output_json.is_file():
                raise RuntimeError("Module conversion failed: " + module + ": " + run.stderr[-1000:])
            raw = output_json.read_text()
        for canonical, alias in ALIASES.items():
            raw = raw.replace(alias, canonical)
        raw = raw.replace('"https://semrisk.invalid/entity"', '"urn:semrisk:entity:"')
        raw = raw.replace(view_iri, VIEW_URN + slug)
        if "semrisk.invalid" in raw:
            raise ValueError("Temporary alias leaked: " + module)
        data = json.loads(raw)
        expected = {
            kind: {row["iri"] for row in rows if row["module"] == module and row["rdf_type"] == kind}
            for kind in ("owl:Class", "owl:ObjectProperty")
        }
        actual = {
            "owl:Class": {row.get("iri") for row in data.get("classAttribute", [])
                          if row.get("iri") in expected["owl:Class"]},
            "owl:ObjectProperty": {row.get("iri") for row in data.get("propertyAttribute", [])
                                   if row.get("iri") in expected["owl:ObjectProperty"]},
        }
        if actual != expected or data.get("header", {}).get("iri") != VIEW_URN + slug:
            raise ValueError("Module IRI coverage/header mismatch: " + module)
        json_bytes = (json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
        results[OUTPUT / (slug + ".json")] = json_bytes
        reports.append({
            "module": module,
            "source_path": entry["path"],
            "source_blob_sha": entry["git_blob_sha"],
            "derived_input_nt_sha256": sha256(nt),
            "derived_input_triples": len(derived),
            "json_sha256": sha256(json_bytes),
            "local_class_coverage": len(actual["owl:Class"]),
            "local_object_property_coverage": len(actual["owl:ObjectProperty"]),
            "visualizer_class_nodes": len(data.get("class", [])),
            "visualizer_property_nodes": len(data.get("property", [])),
        })
    manifest = {
        "status": "OFFLINE_MODULE_JSON_BROWSER_SMOKE_PASS_READABILITY_PARTIAL",
        "semantic_source_ref": SOURCE_REF,
        "converter_source_ref": CONVERTER_REF,
        "converter_jar_sha256": CONVERTER_SHA256,
        "policy": "One exact SemRisk module per view; omit owl:imports and ontology-type triples only in derived input; no imported gUFO or cross-module definitions, no entailment. Referenced terms are context stubs. Combined asserted-union view remains separate.",
        "modules": reports,
        "browser_qa_run": "https://github.com/ArazSaieArasi3/SemRisk/actions/runs/36319497749",
        "readability": "partial: focused views reduce nodes, but external context stubs and edge clipping require reader review",
        "skos_markers_outside_owl_views": {
            "Core": 1, "Mappings": 3,
            "note": "Mappings contains no local OWL class/object-property declaration and is intentionally not presented as an empty WebVOWL module."
        },
        "public_url": None,
    }
    results[OUTPUT / "manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    results = build(args.jar)
    if args.check:
        for path, expected in results.items():
            if not path.is_file() or path.read_bytes() != expected:
                raise SystemExit("WEBVOWL_MODULE_DRIFT: " + str(path))
    else:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for path, data in results.items():
            path.write_bytes(data)
    print("SEM_RISK_WEBVOWL_MODULE_JSON_PASS | five OWL-relevant module views; source-only projection")


if __name__ == "__main__":
    main()
