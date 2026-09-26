"""Reject edits/removals of versioned Pages routes already present in a parent.

The first parent is the previous main commit on push and the base on the
GitHub-generated pull-request merge ref. New version directories are allowed.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "site/ontology/"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def altered_existing(previous, current):
    return sorted(path for path, old in previous.items() if current.get(path) != old)


def main():
    # Small contract check for the comparison itself.
    assert altered_existing({"v1": b"a"}, {"v1": b"a", "v2": b"b"}) == []
    assert altered_existing({"v1": b"a"}, {"v1": b"b"}) == ["v1"]
    assert altered_existing({"v1": b"a"}, {}) == ["v1"]

    parent = git("rev-parse", "HEAD^").decode().strip()
    paths = git("ls-tree", "-r", "--name-only", parent, "--", PREFIX).decode().splitlines()
    previous = {path: git("show", parent + ":" + path) for path in paths}
    current = {path: (ROOT / path).read_bytes() for path in paths if (ROOT / path).is_file()}
    changed = altered_existing(previous, current)
    if changed:
        raise SystemExit("IMMUTABLE_PAGES_ROUTE_OVERWRITE_REJECTED: " + ", ".join(changed))
    print("SEM_RISK_PAGES_PRIOR_ROUTES_UNCHANGED | " + str(len(paths)) + " prior files")


if __name__ == "__main__":
    main()
