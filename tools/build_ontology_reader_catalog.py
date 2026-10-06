#!/usr/bin/env python3
"""Render a reader index from governed registries without changing semantics."""
import argparse
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/ontology/domain-concept-reader-catalog.md'


def rows(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def table(headers, data):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(map(cell, row)) + ' |' for row in data])


def build():
    concepts = rows('conceptualization/core/core-concept-registry-v0.1.csv')
    modules = rows('architecture/g2/module-profile-registry-v0.1.csv')
    formal = rows('docs/ontology/p1-r2-formal-source-entity-reference-v0.1.csv')
    f_by_id = {r['semantic_id']: r for r in formal}
    assert len({r['semantic_id'] for r in concepts}) == len(concepts)
    roadmap = (ROOT / 'docs/research/domain-profile-roadmap.md').read_text()
    portfolio = []
    for line in roadmap.splitlines():
        if line.startswith('| `P'):
            fields = [x.strip() for x in line.strip('|').split('|')]
            portfolio.append((fields[1].replace('**', ''), fields[2], fields[0]))
    assert len(portfolio) == 12, 'Review changed roadmap table structure'
    scope_names = sorted({s for r in concepts for s in r['module_profile'].split('/')})
    scopes = [r[0] for r in portfolio] + [s for s in scope_names if s not in {r[0] for r in portfolio}]
    counts = Counter(r['rdf_type'] for r in formal)
    text = '''# SemRisk domains, concepts and diagrams

This reader view is generated from the governed registries. It distinguishes the planned domain portfolio, conceptual assignments and the frozen formal candidate `0.1.0-rc.1`. It does not adopt new concepts or change an ontology definition.

The current tested successor is [0.2.0-rc.4](../../ontology/releases/0.2.0-rc.4/README.md), selected by [current-candidate.json](../../ontology/current-candidate.json). Its additional context terms are listed separately in the [profile IRI registry](../../ontology/releases/0.2.0-rc.4/profile-iri-registry.csv); the formal-count join below remains explicitly historical. The current concept registry includes the successor Trigger, confidence, indicator, threshold, heterogeneous-owner, scenario, register and workflow definitions. The [complete foundational audit](../../foundational/semantic-identity-v0.2.0-rc.3/decisions.md) records the remaining diagram gates.

Start with [domain definitions](#domain-definitions), [domains and their concepts](#domains-and-their-concepts), [concept definitions](#concept-definitions), or [diagrams](#diagrams).

## Domain definitions

The following scope descriptions are copied from the [domain profile roadmap](../research/domain-profile-roadmap.md#2-priority-profile-portfolio). Priority is a planning priority, not implementation status. Core is the shared foundation; other rows are planned profiles. Method is a supporting module listed below, not a new application domain.

'''
    text += table(['Domain / profile', 'Scope definition from roadmap', 'Priority'], portfolio)
    text += '''

## Governed modules and implementation boundary

The [module registry](../../architecture/g2/module-profile-registry-v0.1.csv) also includes mapping and application packages. These ten architectural responsibilities are not ten implemented OWL domain ontologies. The six formal source modules are Core, Enterprise, Method, Governance, Pharma and Mappings; Architecture uses external references and Health has no standalone formal module in this candidate.

'''
    text += table(['Module', 'Type', 'Responsibility', 'Paper-1 status'],
                  [(r['module_name'], r['type'], r['responsibility'], r['paper1_status']) for r in modules])
    text += '''

## Domains and their concepts

Membership below splits the exact `module_profile` field of the [concept registry](../../conceptualization/core/core-concept-registry-v0.1.csv) on `/`. Shared concepts therefore appear in more than one row. These are conceptual assignments, not OWL declaration ownership, subclass assertions, or additive counts. A blank portfolio area has no concept assigned in this registry; it is not proof that no research or source vocabulary exists for it.

'''
    text += table(['Domain / scope', 'Concepts currently assigned in registry'],
                  [(s, '; '.join(f"{r['semantic_id']} — {r['preferred_term']}" for r in concepts if s in r['module_profile'].split('/')) or 'No assigned entries in this registry; planned portfolio scope.') for s in scopes])
    text += f'''

## Concept definitions

All {len(concepts)} definitions below are copied exactly from the concept registry. Formal status is joined by stable semantic ID to the [source-derived entity inventory](p1-r2-formal-source-entity-reference-v0.1.csv). Of these concepts, {sum(f_by_id.get(r['semantic_id'], {}).get('rdf_type') == 'owl:Class' for r in concepts)} are declared OWL classes and {sum(f_by_id.get(r['semantic_id'], {}).get('rdf_type') == 'skos:Concept' for r in concepts)} are SKOS markers in the frozen candidate. The remaining concepts have no local declaration there; their conceptual status remains visible. A SKOS marker is not an OWL class.

'''
    text += table(['ID', 'Concept', 'Definition', 'Conceptual status', 'Formal declaration / module'],
                  [(r['semantic_id'], r['preferred_term'], r['definition'], r['concept_status'],
                    (f_by_id[r['semantic_id']]['rdf_type'] + ' / ' + f_by_id[r['semantic_id']]['module']) if r['semantic_id'] in f_by_id else 'Not declared in frozen candidate') for r in concepts])
    text += f'''

## Diagrams

| View | Link | Boundary |
| --- | --- | --- |
| Ontology atlas | [Open SVG](diagrams/p1-r2-local-ontology-atlas-v0.1.svg) | All {len(formal)} local IDs: {counts['owl:Class']} OWL classes, {counts['owl:ObjectProperty']} object properties and {counts['skos:Concept']} SKOS markers, grouped by formal module. |
| Relation diagram | [Open SVG](diagrams/p1-r2-local-relations-v0.1.svg) | Asserted signatures of all {counts['owl:ObjectProperty']} object properties; no inferred causal interpretation or cardinality. |
| Formal reference | [Read definitions and assertions](generated/p1-r2-generated-reference.md) | Generated from the exact formal source; external imports are distinguished from local entities. |
| WebVOWL | [Bundle and local viewing instructions](generated/webvowl-viewer-candidate-v0.1/README.md) | Candidate files exist. GitHub displays their source; this link is not a hosted interactive viewer. |

At the 2026-10-02 repository metadata check, GitHub Pages was disabled. Public WebVOWL availability still requires the #56 license disposition, a new versioned candidate with visible gUFO attribution and disabled dormant upload paths, and #119/#117 browser/accessibility/public-access QA. The old `site/ontology/0.1.0-rc.1/` route remains frozen. No public viewer URL or calendar delivery date is claimed here.

## Rebuild and authority

Run `python tools/build_ontology_reader_catalog.py` to regenerate or add `--check` to detect drift. The concept registry owns conceptual definitions, the module/ownership registries own architecture decisions, and Turtle owns formal assertions. The roadmap describes future scope. This page is a reading aid, not a fourth authority.
'''
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    rendered = build()
    if args.check:
        if not OUT.exists() or OUT.read_text() != rendered:
            raise SystemExit('Reader catalog is stale; regenerate it.')
        print('Reader catalog matches source registries.')
    else:
        OUT.write_text(rendered, encoding='utf-8')
        print(OUT.relative_to(ROOT))
