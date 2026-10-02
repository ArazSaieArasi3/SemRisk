"""Bounded, read-only scan of reachable Git history for credential shapes.

This is a triage aid for #56, not a proof that the repository is free of
private information. It prints only object counts and affected object IDs.
Run from a full clone so older reachable blobs are included.
"""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str, input_data: bytes | None = None) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, input=input_data, capture_output=True, check=True
    ).stdout


PATTERNS = {
    "pem_private_key": re.compile(rb"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
    "github_token": re.compile(rb"(?:gh[pousr]_[A-Za-z0-9_]{25,}|github_pat_[A-Za-z0-9_]{40,})"),
    "aws_access_key": re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "openai_key": re.compile(rb"\bsk-[A-Za-z0-9_-]{24,}\b"),
    "bearer_header": re.compile(rb"(?im)^\s*authorization\s*:\s*bearer\s+\S+"),
    "credential_assignment": re.compile(
        rb"(?im)^\s*(?:password|passwd|client_secret|api_key|access_token)\s*[:=]\s*['\"]?[^\s'\"#]{8,}"
    ),
}
SENSITIVE_SUFFIXES = (".xlsx", ".xls", ".sqlite", ".db", ".env", ".p12", ".pfx", ".pem")


def main() -> None:
    if git("rev-parse", "--is-shallow-repository").strip() != b"false":
        raise SystemExit("Full Git history required; run git fetch --unshallow first")

    commits = int(git("rev-list", "--count", "HEAD").strip())
    object_ids = [line.split(b" ", 1)[0] for line in git("rev-list", "--objects", "--all").splitlines()]
    ids = b"\n".join(object_ids) + b"\n"
    types = subprocess.run(
        ["git", "cat-file", "--batch-check=%(objectname) %(objecttype)"],
        cwd=ROOT, input=ids, capture_output=True, check=True
    ).stdout.splitlines()
    blobs = [row.split()[0] for row in types if row.endswith(b" blob")]
    hits: dict[str, list[str]] = {name: [] for name in PATTERNS}
    proc = subprocess.run(
        ["git", "cat-file", "--batch"], cwd=ROOT,
        input=b"\n".join(blobs) + b"\n", capture_output=True, check=True
    )
    stream = memoryview(proc.stdout)
    position = 0
    for oid in blobs:
        end = proc.stdout.index(b"\n", position)
        size = int(stream[position:end].tobytes().split()[-1])
        content = stream[end + 1:end + 1 + size]
        for name, pattern in PATTERNS.items():
            if pattern.search(content):
                hits[name].append(oid.decode()[:12])
        position = end + size + 2
    assert position == len(stream), "Git batch stream was not completely parsed"

    paths = set(git("log", "--all", "--name-only", "--format=").decode("utf-8", "replace").splitlines()) - {""}
    named = sorted(path for path in paths if path.lower().endswith(SENSITIVE_SUFFIXES) or Path(path).name.lower() == ".env")
    print(f"HEAD commits={commits}; reachable blobs={len(blobs)}; historical paths={len(paths)}")
    print(f"credential-shape hit counts={{{', '.join(f'{k}: {len(v)}' for k, v in hits.items())}}}")
    print(f"sensitive-filename path count={len(named)}")
    if any(hits.values()) or named:
        # IDs and paths alone allow a reviewer to investigate without leaking file content.
        for name, ids in hits.items():
            if ids:
                print(f"{name} object prefixes: {', '.join(ids)}")
        for path in named:
            print(f"historical sensitive filename: {path}")
        raise SystemExit(1)
    print("SEM_RISK_PUBLIC_HISTORY_HEURISTIC_SCAN_PASS")


if __name__ == "__main__":
    main()
