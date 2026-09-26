#!/usr/bin/env python3
"""Validate OWL2VOWL JSON for the SemRisk P1-R2 candidate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

LOCAL_PREFIX = "urn:semrisk:entity:"
EXPECTED_LOCAL_CLASSES = 35
EXPECTED_LOCAL_PROPERTIES = 37


def ids_with_prefix(items, prefix):
    return {
        item.get("iri")
        for item in items or []
        if isinstance(item, dict) and isinstance(item.get("iri"), str) and item["iri"].startswith(prefix)
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("--scope", choices=["local", "imports"], required=True)
    args = parser.parse_args()

    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    class_attrs = data.get("classAttribute", [])
    prop_attrs = data.get("propertyAttribute", [])

    local_classes = ids_with_prefix(class_attrs, LOCAL_PREFIX + "SR-CPT-")
    local_props = ids_with_prefix(prop_attrs, LOCAL_PREFIX + "SR-REL-")

    if len(local_classes) != EXPECTED_LOCAL_CLASSES:
        raise SystemExit(
            f"local class reconciliation failed: expected {EXPECTED_LOCAL_CLASSES}, got {len(local_classes)}"
        )
    if len(local_props) != EXPECTED_LOCAL_PROPERTIES:
        raise SystemExit(
            f"local property reconciliation failed: expected {EXPECTED_LOCAL_PROPERTIES}, got {len(local_props)}"
        )

    metrics = data.get("metrics") or {}
    result = {
        "scope": args.scope,
        "webvowl_metrics": metrics,
        "local_classes_reconciled": len(local_classes),
        "local_object_properties_reconciled": len(local_props),
        "class_attribute_records": len(class_attrs),
        "property_attribute_records": len(prop_attrs),
    }
    print("SEM_RISK_WEBVOWL_JSON_PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
