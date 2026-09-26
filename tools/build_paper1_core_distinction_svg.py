#!/usr/bin/env python3
"""Render the four selected P1-R2 OWL disjointness pairs for Paper 1.

Fails if a selected source assertion or class label changes. The diagram is a
small selected view, not a generated exhaustive ontology reference.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "ontology/core/semrisk-core-v0.1.0-rc.1.ttl"
ENTERPRISE = ROOT / "ontology/enterprise/semrisk-enterprise-v0.1.0-rc.1.ttl"
OUT = ROOT / "publications/2026-icae/paper1-core-distinction-figure-v0.1.svg"
PAIRS = [
    ("SR-CPT-001", "SR-CPT-033"),
    ("SR-CPT-006", "SR-CPT-007"),
    ("SR-CPT-011", "SR-CPT-013"),
    ("SR-CPT-035", "SR-CPT-036"),
]

def main():
    sources = {"Core": CORE.read_text(), "Enterprise": ENTERPRISE.read_text()}
    labels = {}
    for module, turtle in sources.items():
        for match in re.finditer(r'sr:(SR-CPT-\d+) a owl:Class\s*;.*?rdfs:label "([^"]+)"@en', turtle, re.S):
            labels[match.group(1)] = (match.group(2), module)
    assertions = set()
    # These four source statements each use a single target; fail closed on source changes.
    for turtle in sources.values():
        for left, right in re.findall(r'sr:(SR-CPT-\d+) owl:disjointWith sr:(SR-CPT-\d+)\s*\.', turtle):
            assertions.add(frozenset((left, right)))
    for left, right in PAIRS:
        if frozenset((left, right)) not in assertions or left not in labels or right not in labels:
            raise SystemExit(f"Selected pair or label missing in exact source: {left}/{right}")

    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="90mm" height="70mm" viewBox="0 0 900 700" role="img" aria-labelledby="title desc">',
             '<title id="title">Four selected explicit OWL disjointness pairs in SemRisk P1-R2</title>',
             '<desc id="desc">Risk versus Register Entry; Scenario versus Event; Assessment Activity versus Assessment Result; Risk State versus Workflow State. These are selected axioms, not a complete ontology diagram.</desc>',
             '<rect width="900" height="700" fill="#ffffff"/>',
             '<text x="42" y="64" font-family="DejaVu Sans,Arial,sans-serif" font-size="34" font-weight="bold" fill="#17324d">Selected semantic distinctions</text>',
             '<text x="42" y="96" font-family="DejaVu Sans,Arial,sans-serif" font-size="21" fill="#475569">P1-R2 · explicit OWL disjointness · Core / Enterprise</text>']
    for i, (left, right) in enumerate(PAIRS):
        y = 128 + 130*i
        for x, entity in ((42, left), (502, right)):
            label, module = labels[entity]
            fill, stroke = ("#e9f2fb", "#236596") if module == "Core" else ("#e8f5ef", "#277553")
            parts.append(f'<rect x="{x}" y="{y}" width="356" height="112" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            if len(label) > 21:
                first, last = label.rsplit(" ", 1)
                label_lines = (first, last)
                baselines = (y+38, y+68)
            else:
                label_lines = (label,)
                baselines = (y+53,)
            for line, baseline in zip(label_lines, baselines):
                parts.append(f'<text x="{x+18}" y="{baseline}" font-family="DejaVu Sans,Arial,sans-serif" font-size="25" font-weight="bold" fill="#172b3d">{html.escape(line)}</text>')
            parts.append(f'<text x="{x+18}" y="{y+96}" font-family="DejaVu Sans,Arial,sans-serif" font-size="22" fill="#425569">{entity} · {module}</text>')
        parts += [f'<line x1="400" y1="{y+56}" x2="500" y2="{y+56}" stroke="#8f3451" stroke-width="3"/>',
                  f'<rect x="421" y="{y+34}" width="58" height="42" rx="7" fill="#ffffff"/>',
                  f'<text x="450" y="{y+62}" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-size="21" font-weight="bold" fill="#8f3451">⊥</text>']
    parts += ['<text x="42" y="676" font-family="DejaVu Sans,Arial,sans-serif" font-size="20" fill="#475569">⊥ = explicitly disjoint; selected class pairs only.</text>', '</svg>']
    OUT.write_text("\n".join(parts) + "\n")
    print(OUT)

if __name__ == "__main__":
    main()
