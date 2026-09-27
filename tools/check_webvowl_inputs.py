"""Check exact local P1-R2 inputs before attempting an offline WebVOWL conversion.

This checks source identity and counts; it does not invoke OWL2VOWL or assert that
WebVOWL can render the ontology. Run from any working directory.
"""

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/ontology/generated/p1-r2-closure-manifest.json"
GRAPH = ROOT / "docs/ontology/generated/p1-r2-asserted-closure.nt"
INVENTORY = ROOT / "docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv"


def git_blob_sha(content):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def main():
    manifest = json.loads(MANIFEST.read_text())
    rows = list(csv.DictReader(INVENTORY.open(newline="")))
    assert manifest["candidate"] == "P1-R2/0.1.0-rc.1"
    assert manifest["status"] == "ASSERTED_CLOSURE_ONLY"
    assert len(manifest["files"]) == manifest["source_file_count"] == 7
    assert len(rows) == len({r["iri"] for r in rows}) == manifest["local_entity_count"] == 76
    assert hashlib.sha256(GRAPH.read_bytes()).hexdigest() == manifest["canonical_nt_sha256"]
    for item in manifest["files"]:
        path = Path(item["path"])
        assert not path.is_absolute() and ".." not in path.parts
        assert git_blob_sha((ROOT / path).read_bytes()) == item["git_blob_sha"], path
    types = Counter(r["rdf_type"] for r in rows)
    assert types["owl:Class"] == 35, types
    assert types["owl:ObjectProperty"] == 37, types
    assert sum(types.values()) - types["owl:Class"] - types["owl:ObjectProperty"] == 4, types
    source_paths = {r["source_path"] for r in rows}
    assert len(source_paths) == 6
    assert source_paths.issubset({x["path"] for x in manifest["files"]})
    print(json.dumps({"status": "INPUTS_PASS_CONVERTER_NOT_RUN", "candidate": manifest["candidate"],
                      "source_files": 7, "local_modules": 6, "local_classes": 35,
                      "local_object_properties": 37, "other_local_markers": 4,
                      "asserted_graph_sha256": manifest["canonical_nt_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
