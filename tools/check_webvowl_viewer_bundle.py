"""Check the source-bound offline WebVOWL bundle without running a browser.

This is an integrity and static asset check, not rendered usability or privacy QA.
"""

import hashlib
import html.parser
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "docs/ontology/generated/webvowl-viewer-candidate-v0.1"


class AssetParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                raise ValueError(f"duplicate HTML id: {element_id}")
            self.ids.add(element_id)
        if tag == "script" and attrs.get("src"):
            self.assets.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.assets.append(attrs["href"])


def check():
    manifest = json.loads((BUNDLE / "manifest.json").read_text())
    assert manifest["status"] == "OFFLINE_BROWSER_SMOKE_PASS_READABILITY_PARTIAL"
    assert manifest["verification"]["browser_rendered"] is True
    assert manifest["verification"]["mobile_readability_checked"] is True
    assert manifest["verification"]["public_access_checked"] is False
    source = ROOT / manifest["json_source"]
    assert (BUNDLE / "data/semrisk.json").read_bytes() == source.read_bytes()
    module_manifest = json.loads((ROOT / manifest["module_json_source"]).read_text())
    assert module_manifest["status"] == "OFFLINE_MODULE_JSON_BROWSER_SMOKE_PASS_READABILITY_PARTIAL"
    assert manifest["module_browser_qa"] == module_manifest["browser_qa_run"]
    assert sum(row["local_class_coverage"] for row in module_manifest["modules"]) == 35
    assert sum(row["local_object_property_coverage"] for row in module_manifest["modules"]) == 37
    for module in module_manifest["modules"]:
        slug = module["module"].lower()
        source_bytes = (ROOT / module["source_path"]).read_bytes()
        source_blob = hashlib.sha1(b"blob " + str(len(source_bytes)).encode() + b"\0" + source_bytes).hexdigest()
        assert source_blob == module["source_blob_sha"], slug
        module_json = ROOT / "docs/ontology/generated/webvowl-module-v0.1" / (slug + ".json")
        bundled_json = BUNDLE / "data" / ("semrisk-" + slug + ".json")
        assert bundled_json.read_bytes() == module_json.read_bytes(), slug
        assert hashlib.sha256(bundled_json.read_bytes()).hexdigest() == module["json_sha256"], slug
        assert ('href="#semrisk-' + slug + '"') in (BUNDLE / "index.html").read_text(), slug

    expected = {}
    for entry in manifest["files"]:
        rel = Path(entry["path"])
        if rel.is_absolute() or ".." in rel.parts or rel.as_posix() in expected:
            raise ValueError(f"unsafe or duplicate manifest path: {rel}")
        content = (BUNDLE / rel).read_bytes()
        assert len(content) == entry["bytes"], str(rel)
        assert hashlib.sha256(content).hexdigest() == entry["sha256"], str(rel)
        expected[rel.as_posix()] = content
    assert {"license.txt", "licenses/d3-3.5.17-LICENSE.txt", "licenses/lodash-4.18.1-LICENSE.txt", "data/semrisk.json"} <= set(expected)
    assert b"Michael Bostock" in expected["licenses/d3-3.5.17-LICENSE.txt"]
    assert b"OpenJS Foundation" in expected["licenses/lodash-4.18.1-LICENSE.txt"]
    assert "lodash/lodash#4.18.1" in expected["js/webvowl.js"].decode(), "bundled Lodash version drift"
    assert "index.html" in expected
    present = {p.relative_to(BUNDLE).as_posix() for p in BUNDLE.rglob("*") if p.is_file()}
    assert present == set(expected) | {"README.md", "manifest.json"}, sorted(present ^ (set(expected) | {"README.md", "manifest.json"}))

    parser = AssetParser()
    parser.feed(expected["index.html"].decode())
    assert parser.assets, "no HTML assets"
    for name in parser.assets:
        parsed = urlsplit(name)
        if parsed.scheme or parsed.netloc or name.startswith("/") or ".." in Path(parsed.path).parts:
            raise ValueError(f"external or unsafe HTML asset: {name}")
        assert parsed.path in expected, f"missing HTML asset: {name}"
    for name, content in expected.items():
        if name.endswith(".css") and re.search(rb"url\(\s*['\"]?(?:https?:)?//", content, re.I):
            raise ValueError(f"remote CSS asset in {name}")
    assert 'semrisk' in expected["js/webvowl.app.js"].decode(), "default SemRisk JSON not referenced"
    assert 'semrisk.invalid' not in expected["data/semrisk.json"].decode(), "temporary converter alias leaked"
    data = json.loads(expected["data/semrisk.json"])
    assert data["header"]["iri"] == "urn:semrisk:documentation:webvowl:p1-r2:0.1.0-rc.1"
    print("SEM_RISK_WEBVOWL_STATIC_BUNDLE_PASS | source JSON, hashes and local assets; independent browser QA recorded")


if __name__ == "__main__":
    check()
