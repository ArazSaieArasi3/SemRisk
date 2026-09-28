#!/usr/bin/env python3
"""Integrity guard for the bounded E10 claim-critical locator checkpoint.

Checks row identity and source bytes; never treats cited prose as semantic validation.
"""
import argparse
import copy
import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "conceptualization/comparison/comparison-cell-evidence-index.csv"
DIMS = ROOT / "conceptualization/comparison/comparison-dimension-definitions.csv"
SELF = ROOT / "evaluation/e10/semrisk-p1-r2-self-row-v0.1.csv"
EXTERNAL = ROOT / "evaluation/e10/claim-critical-external-locator-ledger-v0.1.csv"
RESULTS = ROOT / "evaluation/e10/claim-unit-source-comparison-v0.1.csv"
SELF_STATUSES = {"SUPPORTED_BOUNDED", "PARTIAL", "NOT_ASSESSED"}
EXTERNAL_STATUSES = {
    "POSITIVE_PRIOR_ART", "PARTIAL_OVERLAP", "CORRECTION_PRIOR_ART",
    "POSITIVE_PUBLICATION_ARTIFACT_UNBOUND", "PARTIAL_BINDING", "ARTIFACT_UNKNOWN", "SEMANTIC_CONFLICT",
}

EXPECTED_AUDIT_IDS = {
    "PA006-D02",
    "PA006-D03",
    "PA006-D04",
    "PA006-D06",
    "PA006-D08",
    "PA006-D13",
    "PA006-D14",
    "PA006-D16",
    "PA009-D02",
    "PA009-D04",
    "PA009-D08",
    "PA009-D13",
    "PH003-D03",
    "PH003-D11",
    "PH003-D15",
    "PH003-D16",
    "COVER-D02",
    "COVER-D03",
    "COVER-D04",
    "COVER-D13",
    "COVER-D16",
    "ROSE-D02",
    "ROSE-D03",
    "ROSE-D04",
    "ROSE-D06",
    "ROSE-D13",
    "ROSE-D16",
    "ROSE-D17",
    "RISK-HUB-D03",
    "RISK-HUB-D04",
    "RISK-HUB-D05",
    "RISK-HUB-D08",
    "RISK-HUB-D13",
    "RISK-HUB-D14",
    "RISK-HUB-D15",
    "RISK-HUB-D16",
    "RISK-HUB-D17",
    "RISK-HUB-D07",
    "RISKMAN-D03",
    "RISKMAN-D04",
    "RISKMAN-D11",
    "RISKMAN-D12",
    "RISKMAN-D13",
    "RISKMAN-D14",
    "RISKMAN-D16",
    "RISKMAN-D17",
    "OLIVEIRA-D02",
    "OLIVEIRA-D03",
    "OLIVEIRA-D04",
    "OLIVEIRA-D06",
    "OLIVEIRA-D10",
    "OLIVEIRA-D13",
    "OLIVEIRA-D14",
    "OLIVEIRA-D16",
    "RISKG-D03",
    "RISKG-D04",
    "RISKG-D08",
    "RISKG-D13",
    "RISKG-D15",
    "RISKG-D16",
    "IOF-D03",
    "IOF-D04",
    "IOF-D07",
    "IOF-D11",
    "IOF-D13",
    "IOF-D16",
    "PA010-D04",
    "PA010-D06",
    "PA010-D13",
    "PA010-D16",
    "NIST-D03",
    "NIST-D04",
    "NIST-D05",
    "NIST-D07",
    "NIST-D08",
    "NIST-D12",
    "NIST-D15",
    "NIST-D16",
    "AIRO-D04",
    "AIRO-D06",
    "AIRO-D09",
    "AIRO-D12",
    "AIRO-D13",
    "AIRO-D16",
    "PH008-D06",
    "PH008-D11",
    "PH008-D13",
    "PH008-D14",
    "PH008-D16",
    "PH011-D03",
    "PH011-D08",
    "PH011-D13",
    "PH011-D17",
}

def rows(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def check(self_rows, external_rows, legacy_rows, dimensions, root=ROOT):
    errors = []
    legacy = {r["cell_id"]: r for r in legacy_rows}
    dim = {r["dimension_id"]: r["dimension"] for r in dimensions}
    expected_self = [r for r in legacy_rows if r["comparator_id"] == "CMP-012"]
    if len(expected_self) != 17 or len(self_rows) != 17:
        errors.append("CMP-012 self-row must have exactly 17 dimensions")
    if [r.get("old_cell_id") for r in self_rows] != [r["cell_id"] for r in expected_self]:
        errors.append("self-row old-cell order or identity drift")
    for row in self_rows:
        cid = row.get("old_cell_id", "?")
        old = legacy.get(cid)
        if not old or old["comparator_id"] != "CMP-012":
            errors.append(f"{cid}: self legacy cell missing/wrong comparator")
            continue
        if row.get("dimension_id") != old["dimension_id"] or row.get("dimension") != dim.get(old["dimension_id"]):
            errors.append(f"{cid}: dimension mismatch")
        if row.get("candidate") != "P1-R2/0.1.0-rc.1":
            errors.append(f"{cid}: candidate identity mismatch")
        if row.get("current_status") not in SELF_STATUSES:
            errors.append(f"{cid}: uncontrolled status")
        for field in ("observed_source_or_result", "unit_or_denominator", "claim_ids", "residual_or_unassessed"):
            if not (row.get(field) or "").strip():
                errors.append(f"{cid}: empty {field}")
        refs = (row.get("source_artifact_at_blob") or "").split(";")
        if not refs or any(not ref for ref in refs):
            errors.append(f"{cid}: empty source blob ref")
        for ref in refs:
            match = re.fullmatch(r"(.+)@([0-9a-f]{40})", ref)
            if not match:
                errors.append(f"{cid}: malformed source ref {ref}")
                continue
            path, expected_sha = match.groups()
            target = (root / path).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f"{cid}: missing/escaping source {path}")
            elif git_blob(target.read_bytes()) != expected_sha:
                errors.append(f"{cid}: source blob drift {path}")
    ids = [r.get("audit_id") for r in external_rows]
    if len(ids) != 93 or len(set(ids)) != 93 or set(ids) != EXPECTED_AUDIT_IDS:
        errors.append("external locator ledger must contain exactly the 93 selected audit IDs")
    mapped = 0
    mapped_ids = []
    source_comparator = {
        'SRC-ON-001': 'CMP-001', 'SRC-ON-002': 'CMP-002', 'SRC-PA-005': 'CMP-003',
        'SRC-PA-006': 'CMP-004', 'SRC-ST-007': 'CMP-005', 'SRC-PA-016': 'CMP-006',
        'SRC-PA-017': 'CMP-007', 'SRC-ON-004': 'CMP-008', 'SRC-ON-003': 'CMP-009',
        'SRC-PH-008': 'CMP-011',
    }
    for row in external_rows:
        aid = row.get("audit_id", "?")
        if None in row or any(value is None for value in row.values()):
            errors.append(f"{aid}: malformed column count")
        old_id = row.get("legacy_cell_id", "")
        if old_id:
            mapped += 1
            mapped_ids.append(old_id)
            old = legacy.get(old_id)
            if not old or old["comparator_id"] == "CMP-012":
                errors.append(f"{aid}: missing/nonexternal old cell")
            elif row.get("dimension_id") != old["dimension_id"] or row.get("legacy_status") != old["status"]:
                errors.append(f"{aid}: old dimension/status drift")
            elif old["comparator_id"] != source_comparator.get(row.get("source_id")):
                errors.append(f"{aid}: source/comparator mismatch")
        elif row.get("legacy_status") != "OUTSIDE_HISTORICAL_204":
            errors.append(f"{aid}: outside-row legacy status mismatch")
        if row.get("source_level_status") not in EXTERNAL_STATUSES:
            errors.append(f"{aid}: uncontrolled source-level status")
        if row.get("source_id") not in {"SRC-PA-006", "SRC-PA-009", "SRC-PH-003", "SRC-ON-001", "SRC-ON-002", "SRC-PA-017", "SRC-ON-004", "SRC-PA-005", "SRC-PA-016", "SRC-ON-006", "SRC-PA-010", "SRC-ST-007", "SRC-ON-003", "SRC-PH-008", "SRC-PH-011"}:
            errors.append(f"{aid}: unexpected source")
        if not (row.get("source_url") or "").startswith("https://"):
            errors.append(f"{aid}: missing HTTPS primary source")
        for field in ("exact_publication_locator", "observed_evidence", "calibrated_semrisk_consequence", "artifact_or_reproduction_limit"):
            if not (row.get(field) or "").strip():
                errors.append(f"{aid}: empty {field}")
    if len(set(mapped_ids)) != len(mapped_ids):
        errors.append("duplicate historical external cell")
    if mapped != 71:
        errors.append(f"expected 71 old external cells, got {mapped}")
    correction = [r for r in external_rows if r.get("audit_id") == "PA006-D08"]
    if len(correction) != 1 or correction[0].get("legacy_cell_id") != "CELL-059" or correction[0].get("legacy_status") != "not_in_scope" or correction[0].get("source_level_status") != "CORRECTION_PRIOR_ART":
        errors.append("CELL-059 prior-art correction missing")
    changed = [r for r in external_rows if r.get("audit_id") == "RISKG-D04"]
    if len(changed) != 1 or changed[0].get("legacy_cell_id") != "CELL-089" or changed[0].get("legacy_status") != "not_reported" or changed[0].get("source_level_status") != "CORRECTION_PRIOR_ART":
        errors.append("CELL-089 prior-art correction missing")
    iof = [r for r in external_rows if r.get("audit_id") == "IOF-D04"]
    if len(iof) != 1 or iof[0].get("source_level_status") != "CORRECTION_PRIOR_ART":
        errors.append("IOF assessment process/result counterexample missing")
    airo = [r for r in external_rows if r.get("audit_id") == "AIRO-D04"]
    if len(airo) != 1 or airo[0].get("source_level_status") != "SEMANTIC_CONFLICT":
        errors.append("AIRO residual-risk identity conflict missing")
    return errors


def selftest(self_rows, external_rows, legacy_rows, dimensions):
    assert not check(self_rows, external_rows, legacy_rows, dimensions)
    mutations = []
    s = copy.deepcopy(self_rows); s.pop(); mutations.append(("missing self cell", s, external_rows))
    s = copy.deepcopy(self_rows); s[0]["source_artifact_at_blob"] = "docs/ontology/generated/p1-r2-closure-manifest.json@" + "0" * 40; mutations.append(("wrong blob", s, external_rows))
    s = copy.deepcopy(self_rows); s[12]["current_status"] = "GLOBAL_PASS"; mutations.append(("invented status", s, external_rows))
    s = copy.deepcopy(self_rows); s[3]["residual_or_unassessed"] = ""; mutations.append(("hidden residual", s, external_rows))
    e = copy.deepcopy(external_rows); e[0]["legacy_status"] = "covered_by_assumption"; mutations.append(("historical status drift", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "PA006-D08")["source_level_status"] = "not_in_scope"; mutations.append(("lost counterevidence", self_rows, e))
    e = copy.deepcopy(external_rows); e[0]["source_url"] = ""; mutations.append(("missing primary URL", self_rows, e))
    e = copy.deepcopy(external_rows); e[-1]["source_url"] = None; mutations.append(("malformed external row", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "RISKG-D04")["source_level_status"] = "ARTIFACT_UNKNOWN"; mutations.append(("lost RisKG counterevidence", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "IOF-D04")["source_level_status"] = "ARTIFACT_UNKNOWN"; mutations.append(("lost IOF counterevidence", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "AIRO-D04")["source_level_status"] = "PARTIAL_OVERLAP"; mutations.append(("lost AIRO conflict", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "NIST-D04")["source_id"] = "SRC-ON-003"; mutations.append(("wrong source/comparator", self_rows, e))
    e = copy.deepcopy(external_rows); next(r for r in e if r["audit_id"] == "NIST-D05")["legacy_cell_id"] = "CELL-072"; mutations.append(("duplicate cell", self_rows, e))
    for label, s, e in mutations:
        if not check(s, e, legacy_rows, dimensions):
            raise AssertionError("negative control not detected: " + label)
    print(f"SEM_RISK_E10_LOCATOR_NEGATIVE_CONTROLS_PASS ({len(mutations)}/{len(mutations)})")


def check_results(result_rows, external_rows, self_rows):
    errors = []
    external = {r["audit_id"]: r for r in external_rows}
    current = {r["old_cell_id"]: r for r in self_rows}
    expected = {f"E10-U{i:02d}" for i in range(1, 8)}
    ids = [r.get("unit_id") for r in result_rows]
    if len(ids) != 7 or len(set(ids)) != 7 or set(ids) != expected:
        errors.append("E10 source result must have seven defined units")
    states = {
        "PRIOR_ART_OVERLAP_WITH_BOUNDED_INTEGRATION", "PRIOR_ART_OVERLAP_AND_SEMANTIC_CONFLICT",
        "DESCRIPTIVE_DIFFERENCE_UNPROVEN_EXCLUSIVITY", "MATERIAL_PRIOR_ART_SEMRISK_PARTIAL",
        "SEMRISK_TASK_RESULT_NO_HEAD_TO_HEAD", "BOUNDED_APPLICATION_PRIOR_ART",
        "NO_OVERALL_REPRODUCIBILITY_RANKING",
    }
    for row in result_rows:
        uid = row.get("unit_id", "?")
        if None in row or any(value is None for value in row.values()):
            errors.append(f"{uid}: malformed source-result row")
        if row.get("candidate_ref") != "P1-R2/0.1.0-rc.1":
            errors.append(f"{uid}: candidate ref drift")
        if row.get("comparative_disposition") not in states:
            errors.append(f"{uid}: uncontrolled comparison disposition")
        for field in ("claim_ids", "common_comparison_unit", "source_observed_prior_art",
                      "semrisk_observed_in_exact_candidate", "unassessed_or_adverse", "next_e10_action"):
            if not (row.get(field) or "").strip():
                errors.append(f"{uid}: empty {field}")
        cited = set((row.get("comparator_source_ids") or "").split(";"))
        for aid in (row.get("external_audit_ids") or "").split(";"):
            if aid not in external or external[aid]["source_id"] not in cited:
                errors.append(f"{uid}: missing/mismatched external audit ID {aid}")
        for cid in (row.get("semrisk_cell_ids") or "").split(";"):
            if cid not in current:
                errors.append(f"{uid}: missing self cell {cid}")
    return errors


def result_selftest(result_rows, external_rows, self_rows):
    assert not check_results(result_rows, external_rows, self_rows)
    x = copy.deepcopy(result_rows); x[0]["external_audit_ids"] += ";INVENTED-LOCATOR"
    if not check_results(x, external_rows, self_rows):
        raise AssertionError("missing external result reference not detected")
    x = copy.deepcopy(result_rows); x[1]["unassessed_or_adverse"] = ""
    if not check_results(x, external_rows, self_rows):
        raise AssertionError("hidden result limit not detected")
    print("SEM_RISK_E10_RESULT_NEGATIVE_CONTROLS_PASS (2/2)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    s, e, l, d, result_rows = rows(SELF), rows(EXTERNAL), rows(LEGACY), rows(DIMS), rows(RESULTS)
    failures = check(s, e, l, d) + check_results(result_rows, e, s)
    if failures:
        raise SystemExit("\n".join("FAIL: " + x for x in failures))
    if args.selftest:
        selftest(s, e, l, d)
        result_selftest(result_rows, e, s)
    print("SEM_RISK_E10_LOCATOR_INTEGRITY_PASS (17 self + 93 external selected rows + 7 source-result units)")


if __name__ == "__main__":
    main()
