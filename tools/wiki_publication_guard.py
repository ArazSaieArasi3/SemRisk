"""Check the eight source-controlled Wiki pages and publication link contract.

This checks source files only. Live Wiki revisions, rendering and access need a
separate read-back at each publication baseline.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "docs/wiki/pages"
MANIFEST = ROOT / "docs/wiki/p1-r2-wiki-publish-manifest-v0.1.json"
PREPUBLICATION_REF = "c5f947eae0d801428e9ac3cb43382ef02bfd1326"
WIKI_ROOT = "https://github.com/ArazSaieArasi3/SemRisk/wiki"
NAMES = ("Home", "Scope-and-Contributions", "Semantic-Architecture",
         "Formal-Reference", "Evidence-and-VVEAA", "Relational-Projection",
         "Pharma-Case", "Reproduce-and-Release")


def build():
    found = {p.stem for p in PAGES.glob("*.md")}
    if found != set(NAMES):
        raise ValueError("Wiki page set drift: " + str(found ^ set(NAMES)))
    entries = []
    for name in NAMES:
        path = PAGES / (name + ".md")
        data = path.read_bytes()
        content = data.decode("utf-8")
        if "P1-R2 candidate" not in content or "pending #55/#56" not in content:
            raise ValueError("Candidate/nonclaim banner drift: " + name)
        if any(token.lower() in content.lower() for token in ("jira risk attributes.xlsx", "Bearer ", "raw Jira row:")):
            raise ValueError("Protected-data marker: " + name)
        local_links = [target for target in re.findall(r"\]\(([^)#]+\.md)\)", content)
                       if not target.startswith(("https://", "http://"))]
        if local_links:
            raise ValueError("Unpublished relative Wiki navigation: " + name + " -> " + str(local_links))
        wiki_links = sorted(set(re.findall(r"\]\((https://github\.com/ArazSaieArasi3/SemRisk/wiki(?:/[^)#]+)?)\)", content)))
        allowed = {WIKI_ROOT, *(WIKI_ROOT + "/" + target for target in NAMES[1:])}
        expected_home = sorted(allowed - {WIKI_ROOT})
        if ((name == "Home" and wiki_links != expected_home)
                or (name != "Home" and (WIKI_ROOT not in wiki_links or not set(wiki_links) <= allowed))):
            raise ValueError("Published Wiki navigation drift: " + name + " -> " + str(wiki_links))
        entries.append({"page": name, "source_path": path.relative_to(ROOT).as_posix(),
                        "sha256": hashlib.sha256(data).hexdigest(), "navigation_targets": wiki_links})
    if len(set(x["sha256"] for x in entries)) != 8:
        raise ValueError("Duplicate Wiki page bodies")
    return {"candidate": "P1-R2/0.1.0-rc.1", "state": "PUBLIC_WIKI_CANDIDATE_PENDING_FULL_DRIFT_AUDIT",
            "prepublication_source_commit": PREPUBLICATION_REF, "wiki_root": WIKI_ROOT,
            "pages": entries,
            "publication_rule": "Preserve existing live pages/revisions; verify content, navigation, access and rollback after sync. No scholarly release claim."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(expected)
    elif not MANIFEST.is_file() or MANIFEST.read_text() != expected:
        raise SystemExit("WIKI_SOURCE_MANIFEST_DRIFT")
    print("SEM_RISK_WIKI_SOURCE_LINKS_PASS | 8 pages; exact source hashes; live drift audit separate")


if __name__ == "__main__":
    main()
