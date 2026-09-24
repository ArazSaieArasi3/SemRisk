#!/usr/bin/env python3
"""Static consistency checks for SemRisk #46 relational projection."""
from pathlib import Path
import csv, re, sys

ROOT=Path(__file__).resolve().parents[2]
design=ROOT/"relational"/"design"
sql_dir=ROOT/"relational"/"sql"

sql=(sql_dir/"V001__paper1_projection.sql").read_text(encoding="utf-8")+"\n"+(sql_dir/"V001__views.sql").read_text(encoding="utf-8")
implemented=set(m.group(1).lower() for m in re.finditer(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:TABLE|VIEW)\s+([a-z_]+\.[a-z_]+)",sql,re.I))

with (design/"schema-table-catalog-v0.1.csv").open(encoding="utf-8",newline="") as f:
    expected={f"{r['schema']}.{r['table']}".lower() for r in csv.DictReader(f)}

missing=sorted(expected-implemented)
if missing:
    raise SystemExit(f"Missing catalog objects: {missing}")

with (design/"ontology-rdb-mapping-v0.1.csv").open(encoding="utf-8",newline="") as f:
    mappings=list(csv.DictReader(f))
if len(mappings)!=71:
    raise SystemExit(f"Expected 71 ontology↔RDB mappings, found {len(mappings)}")

known_schemas={"meta","ref","core","assessment","treatment","enterprise","governance","pharma","staging"}
unresolved=[]
for row in mappings:
    refs=re.findall(r"\b([a-z_]+\.[a-z_]+)\b",row["rdb_representation"])
    for ref in refs:
        schema=ref.split(".",1)[0]
        if schema in known_schemas and ref.lower() not in implemented:
            unresolved.append((row["mapping_id"],ref,row["rdb_representation"]))
if unresolved:
    raise SystemExit(f"Unresolved mapped RDB objects: {unresolved}")

if "owner_id" in re.findall(r"CREATE\s+TABLE\s+core\.risk\s*\((.*?)\);",sql,re.I|re.S)[0].lower():
    raise SystemExit("Forbidden primitive owner_id found on core.risk")

if "enterprise.v_risk_owner" not in implemented:
    raise SystemExit("Derived risk-owner view missing")

print(f"PASS: {len(expected)}/{len(expected)} catalog objects implemented")
print(f"PASS: {len(mappings)}/71 ontology↔RDB mappings have implemented object targets or intentional metadata dispositions")
print(f"INFO: {len(implemented-expected)} implementation convenience views beyond frozen catalog: {sorted(implemented-expected)}")
