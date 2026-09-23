#!/usr/bin/env python3
"""NC-SEM-004 negative control for SemRisk Issue #50.

Mutate a HermiT-produced reasoned graph by removing one independently declared
expected entailment, then prove the post-reasoning validator rejects it.
The canonical ontology and the unmodified reasoned baseline are never changed.
"""
from pathlib import Path
import subprocess
import sys

from rdflib import Graph, URIRef
from rdflib.namespace import RDFS

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "semantic-ci"
SOURCE = BUILD / "reasoned.owl"
MUTATED = BUILD / "nc-sem-004-missing-entailment.owl"
SUBJECT = URIRef("urn:semrisk:entity:SR-CPT-017")
OBJECT = URIRef("urn:semrisk:entity:SR-CPT-013")
TRIPLE = (SUBJECT, RDFS.subClassOf, OBJECT)


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: NC-SEM-004 requires the HermiT reasoned baseline: {SOURCE}")
        return 2

    graph = Graph()
    graph.parse(SOURCE)
    if TRIPLE not in graph:
        print("ERROR: baseline lacks the independently declared expected entailment; fixture cannot prove detector sensitivity.")
        return 2

    graph.remove(TRIPLE)
    graph.serialize(destination=str(MUTATED), format="xml")

    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "semrisk_semantic_ci.py"), "--stage", "post", "--reasoned", str(MUTATED)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    (BUILD / "nc-sem-004-detector-output.txt").write_text(proc.stdout + proc.stderr, encoding="utf-8")

    if proc.returncode == 0:
        print("FAIL: NC-SEM-004 removed an expected entailment but the governed post-reasoning validator accepted the mutation.")
        return 1

    if "SR-CPT-017<SR-CPT-013" not in (proc.stdout + proc.stderr):
        print("FAIL: validator failed, but not for the intended NC-SEM-004 missing-entailment defect.")
        return 1

    print("PASS: NC-SEM-004 removed SR-CPT-017 -> SR-CPT-013 and the governed post-reasoning validator detected the missing entailment.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
