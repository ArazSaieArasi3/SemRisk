#!/usr/bin/env python3
"""Generate ontology-only Wiki publication inputs; no manuscript or private source bytes."""
from pathlib import Path
import csv,re
from build_public_ontology_docs import ROOT,REF,REPO,WIKI,BASEURL,rows,rebase_md
OUT=ROOT/'docs/wiki/public-20261006';PAGE=BASEURL+'ontology/0.2.0-rc.4/docs-20261006/'
ROUTES=['rc4-Overview','rc4-Domains-and-Concepts','rc4-Relations','rc4-Formal-Reference','rc4-Diagrams-and-Explorer','rc4-Tutorial','rc4-Sources-and-Limits']
def wrap(title,text):return '# '+title+'\n\n> Ontology documentation candidate 0.2.0-rc.4. Source snapshot `'+REF+'`. Not a scholarly release or independent domain validation. No manuscript is included.\n\n'+text+'\n\n## Navigation\n\n'+ ' · '.join('['+r.replace('rc4-','').replace('-',' ')+']('+WIKI+r+')' for r in ROUTES)+'\n\n[Home]('+WIKI+'Home) · [Versioned Pages]('+PAGE+'index.html) · [Canonical repository]('+REPO+'ontology/releases/0.2.0-rc.4/README.md)\n'
def build():
 OUT.mkdir(parents=True,exist_ok=True);out={}
 out['rc4-Overview']=wrap('SemRisk rc.4 overview','''SemRisk separates managed risk from its records, scenario types from realized events, assessment activities from issued results, and situational risk states from workflow values. These are selected modeled commitments; full domain adequacy and independent validation remain open.

## Exact counting units

- Seven version-bound modules plus pinned gUFO: 1,618 asserted triples.
- 116 local declarations: 46 classes (35 domain, 11 helpers), 50 object properties, eight datatype properties, one annotation property, seven named individuals and four markers.
- The governed conceptual inventory separately contains 47 concepts and 40 relation decisions.

Researchers can follow definitions → formal interpretation → source/limitation records. Engineers can follow the term index → exact Turtle source → bounded tutorial. An asserted graph is not an entailment closure, and a diagram is not an independent semantic authority.

## Version boundary

The older P1-R2/rc.1 pages and source snapshots are historical. Full current SQL parity is deferred. Independent reader/domain review, transfer evidence, complete OntoUML acceptance and final release identity remain open.''')
 cs=rows('conceptualization/core/core-concept-registry-v0.1.csv');text='Concept definitions below are copied from the governed concept registry. Module/profile assignments are not OWL subclass assertions. Planned domain scopes are available in the [domain portfolio]('+PAGE+'catalog.html#domains); planning priority does not mean implementation.\n'
 for c in cs:text+='\n## '+c['semantic_id']+' — '+c['preferred_term']+'\n\n'+c['definition']+'\n\nScope: '+c['module_profile']+'. Status: '+c['concept_status']+'.\n\nInherited registry note: '+c['conflicts_uncertainty']+'\n'+('\nCurrent disposition: Trigger is event-only; enabling conditions are modeled separately. The older alternatives are superseded by the current definition.\n' if c['semantic_id']=='SR-CPT-005' else '')
 text+='\n[Governed concept registry]('+REPO+'conceptualization/core/core-concept-registry-v0.1.csv).'
 out['rc4-Domains-and-Concepts']=wrap('All 47 concepts and domain assignments',text)
 text='The 40 current relation decisions are separate from 50 OWL object-property declarations. Conceptual endpoints and multiplicity proposals must not be mistaken for global OWL constraints.\n'
 for r in rows('foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv'):text+='\n## '+r['relation_id']+' — '+r['label']+'\n\nConceptual endpoints: '+r['domain_conceptual']+' → '+r['range_conceptual']+'.\n\nFormal status: '+r['formal_status']+'. Asserted domain: '+(r['asserted_domains'] or 'not asserted')+'. Asserted range: '+(r['asserted_ranges'] or 'not asserted')+'.\n\nMultiplicity status: '+r['diagram_multiplicity_status']+'. Inherited registry note: '+r['semantic_warning']+'\n'+('\nCurrent formal disposition: SR-REL-038 is an OWL annotation property, not an object-property edge; the earlier alternative remains historical.\n' if r['relation_id']=='SR-REL-038' else '')
 text+='\n[Current relation audit]('+REPO+'foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv).'
 out['rc4-Relations']=wrap('All 40 relation decisions',text)
 p='docs/formal/formal-ontology-description-rc4.md';text=rebase_md((ROOT/p).read_text(),p).replace('Readable paper example','Readable ontology example')
 out['rc4-Formal-Reference']=wrap('Formal interpretation and source authority','[Search all 116 local terms]('+PAGE+'formal.html). The complete source projection preserves URI-level assertions and links to exact modules; anonymous expressions remain in the linked graph.\n\n'+text)
 out['rc4-Diagrams-and-Explorer']=wrap('Diagrams and bounded Explorer','[Browse all 15 canonical conceptual views]('+PAGE+'diagrams.html) or [open the rc.4 WebVOWL explorer]('+PAGE+'explorer/index.html).\n\nThe conceptual views retain their original source identity and limitations. The complete original atlas fails 170 mm print readability; native-editor and complete OntoUML acceptance remain open. No unpublished print companion is included.\n\nThe existing WebVOWL 1.1.7 renderer is reused with a bounded asserted-source adapter. It is not OntoUML. The graph includes 46 local classes and 24 object properties with explicit named endpoint pairs. The remaining 26 object properties and all eight datatype properties stay in the exhaustive searchable term index; no missing endpoint is invented. Enumeration closure, disjointness visualization, anonymous expressions, metatypes and complete imported semantics are not represented by graph layout.\n\nUse the graph selector for Core, Enterprise, Method or assessment-context. Governance, Pharma and Mappings remain accessible through index-only links where no graphable pair exists. Search by stable ID or IRI in the formal index. Use zoom, center and details controls; keyboard focus is visible. Uploads, remote conversion, arbitrary URL loading and editing are disabled in this read-only bundle.\n\nGraphical readability remains partial, especially in dense or narrow-screen views; use zoom/pan or the complete term index for readable definitions. Independent engineering-reader and academic/domain-reader tasks have not been executed. Browser automation is technical preflight, not participant evidence. Runtime notices and gUFO attribution are linked in the Explorer and source page.')
 out['rc4-Tutorial']=wrap('Bounded rc.4 source tutorial',(ROOT/'docs/pages/2026-10-06/tutorial.md').read_text())
 out['rc4-Sources-and-Limits']=wrap('Sources attribution and limits','''The repository owns versioned formal sources, governed registries, code and authorized test artifacts. Wiki explains concepts and examples. Pages provides searchable references, diagrams and a bounded explorer. None is an independent semantic authority.

## Corpus and standards

'''+ '\n'.join('- ['+p+']('+REPO+p+')' for p in ['literature/review-protocol.md','literature/search-log.csv','literature/closest-ontology-technical-baseline.md','literature/closest-work-comparison-matrix.csv','literature/standards-frameworks-baseline.md'])+'''

Missing comparator locators are evidence gaps, not proof of absent capabilities. Source roles, observed results, synthetic examples and interpretation remain separate.

## Rights and boundaries

The pinned gUFO source by João Paulo A. Almeida, Giancarlo Guizzardi, Tiago Sales and Ricardo Falbo carries CC BY 4.0. WebVOWL, D3 and Lodash retain their bundled notices. No repository-wide SemRisk reuse license is selected or inferred by documentation publication. Original private workbooks and unpublished manuscripts are excluded. Final release/citation/availability and independent review gates remain open.

'''+ '[gUFO attribution]('+REPO+'ontology/vendor/GUFO-ATTRIBUTION.md) · [gUFO license]('+REPO+'ontology/vendor/GUFO-LICENSE) · [Candidate source manifest]('+REPO+'ontology/releases/0.2.0-rc.4/manifest.json)')
 out['Home']='# SemRisk ontology documentation\n\nCurrent documentation describes **0.2.0-rc.4**, an ontology candidate, not a scholarly release or independently validated domain model. Canonical sources and governed registries remain authoritative. Manuscript content and downloads are excluded.\n\n## Researcher route\n\n[Overview]('+WIKI+'rc4-Overview) → [Domains and all 47 concepts]('+WIKI+'rc4-Domains-and-Concepts) → [Formal interpretation]('+WIKI+'rc4-Formal-Reference) → [Sources and limits]('+WIKI+'rc4-Sources-and-Limits).\n\n## Engineer route\n\n[All 40 relation decisions]('+WIKI+'rc4-Relations) → [Search all 116 formal terms]('+PAGE+'formal.html) → [Diagrams and Explorer]('+WIKI+'rc4-Diagrams-and-Explorer) → [Run the bounded tutorial]('+WIKI+'rc4-Tutorial).\n\n[Versioned Pages index]('+BASEURL+') · [Exact candidate sources]('+REPO+'ontology/releases/0.2.0-rc.4/README.md).\n\n## Historical documentation\n\nThe following pages retain the older P1-R2/0.1.0-rc.1 scope; their results must not be attributed to rc.4. They remain available with history preserved.\n\n'+ '\n'.join('- ['+p.replace('-',' ')+']('+WIKI+p+')' for p in ['Scope-and-Contributions','Semantic-Architecture','Formal-Reference','Pharma-Case','Relational-Projection','Evidence-and-VVEAA','Reproduce-and-Release'])+'\n\nSQL parity is deferred; independent reader/domain review, transfer evidence, complete OntoUML acceptance and final release/license identity remain open.\n'
 for name,text in out.items():
  assert not re.search(r'\]\([^)]*(?:publications/|manuscript|\.docx)',text,re.I)
  (OUT/(name+'.md')).write_text(text)
 print('Built 8 ontology-only Wiki page inputs')
if __name__=='__main__':build()
