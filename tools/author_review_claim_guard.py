#!/usr/bin/env python3
"""Bounded author-review claim guard for SemRisk Paper 1 v0.3.

This is a textual regression aid. Passing it does not replace scientific review.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "publications/2026-icae/manuscript-working-draft-v0.3.md"
MATRIX = ROOT / "publications/2026-icae/author-review-claim-evidence-v0.2.csv"

REQUIRED = {
    "27/27": r"27/27.{0,110}(jira|schema|fields|attributes)",
    "eight task denominator": r"eight predeclared SQL.{0,220}all eight pairs",
    "CQ breakdown": r"26.{0,50}seven.{0,50}six.{0,55}one.{0,30}deferred",
    "not global equivalence": r"(not|does not).{0,100}(global|lossless).{0,80}(equivalence|equivalent)",
    "human validation pending": r"(expert semantic validation|human semantic validation).{0,55}(pending|not yet executed|remain pending)",
    "DS-004 blocked": r"DS-004.{0,110}(blocked|not loaded)",
    "DS-002 protected": r"DS-002.{0,110}(protected|unopened)",
    "synthetic qualification": r"synthetic.{0,140}(not evidence|not observed|regression|fixture)",
}
UNSAFE = [
    r"expert[- ]validated (ontology|SemRisk)|ontology is expert[- ]validated",
    r"independent transferability (has been |is )?(demonstrated|validated|proven)",
    r"(global|lossless) ontology[-– ](to[-– ])?database equivalence (has been |is )?(demonstrated|proven|established)",
    r"(complete|full) (ISO|NIST|ICH|TOGAF|ArchiMate|standards?) (conformance|compliance)",
    r"27/27 (proves|demonstrates) (ERM|ontology) completeness",
    r"DS-003 (proves|demonstrates) (treatment effectiveness|observed impact)",
    r"DS-002 (validates|proves) (antibiotic|shortage)",
]

def check(text, rows):
    failures = []
    flat = " ".join(text.split())
    for label, pattern in REQUIRED.items():
        if not re.search(pattern, flat, re.I):
            failures.append(f"missing bounded claim: {label}")
    ids = [r.get("claim_id") for r in rows]
    expected = [f"SR-CL{i:02d}" for i in range(1,10)]
    if ids != expected:
        failures.append(f"claim matrix IDs/order mismatch: {ids}")
    for r in rows:
        if not r.get("primary_evidence") or not r.get("claim_ceiling") or not r.get("negative_or_pending"):
            failures.append(f"missing evidence/ceiling/negative: {r.get('claim_id')}")
    for p in UNSAFE:
        for match in re.finditer(p, flat, re.I):
            prefix = flat[max(0, match.start()-140):match.start()]
            clause = re.split(r"[.;!?]", prefix)[-1]
            if re.search(r"\b(no|not|never|without|cannot|can't)\b", clause, re.I):
                continue
            failures.append(f"affirmative overclaim matched: {p}")
    return failures

def selftest(rows):
    base = MANUSCRIPT.read_text(encoding="utf-8")
    assert not check(base, rows), check(base, rows)
    for phrase in [
        "The ontology is expert-validated.",
        "Independent transferability has been demonstrated.",
        "Global ontology-to-database equivalence has been established.",
        "Complete ISO conformance is demonstrated.",
        "27/27 proves ERM completeness.",
        "DS-003 demonstrates treatment effectiveness.",
        "DS-002 validates antibiotic shortage.",
    ]:
        faults = check(base + "\n" + phrase, rows)
        assert any("affirmative overclaim" in x for x in faults), phrase
    assert not check(base + "\nNo global ontology-to-database equivalence is demonstrated.", rows)
    print("SEM_RISK_PAPER1_CLAIM_GUARD_SELFTEST_PASS")

def main():
    with MATRIX.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if "--selftest" in sys.argv:
        selftest(rows)
    failures = check(MANUSCRIPT.read_text(encoding="utf-8"), rows)
    if failures:
        print("\n".join("FAIL: " + x for x in failures), file=sys.stderr)
        return 1
    print("SEM_RISK_PAPER1_AUTHOR_REVIEW_CLAIMS_PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
