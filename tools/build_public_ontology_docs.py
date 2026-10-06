#!/usr/bin/env python3
"""Build only source-bound ontology documentation; never package manuscript inputs."""
import csv,hashlib,html,json,re,shutil,argparse
from pathlib import Path
import markdown
from rdflib import Graph,URIRef,Literal,BNode
from rdflib.namespace import RDF,RDFS,OWL
ROOT=Path(__file__).resolve().parents[1]
REF='67247f13ba5d0c7d32163f2b3e848af15067d92e'
REPO='https://github.com/ArazSaieArasi3/SemRisk/blob/'+REF+'/'
ROUTE=Path('site/ontology/0.2.0-rc.4/docs-20261006')
OUT=ROOT/ROUTE
DOC=ROOT/'docs/pages/2026-10-06'
SOURCE=ROOT/'docs/formal/0.2.0-rc.4'
WIKI='https://github.com/ArazSaieArasi3/SemRisk/wiki/'
BASEURL='https://arazsaiearasi3.github.io/SemRisk/'
MODULES=['core','enterprise','method','governance','pharma','mappings','assessment-context']
def sha(b):return hashlib.sha256(b).hexdigest()
def esc(s):return html.escape(str(s),quote=True)
def rows(path):return list(csv.DictReader((ROOT/path).open()))
def source(path,label):
 assert (ROOT/path).is_file(),path
 assert not path.startswith('publications/')
 return f'<a href="{REPO}{path}">{esc(label)}</a>'
CSS='''body{margin:0;background:#f8fafb;color:#182b3a;font:17px/1.55 system-ui,sans-serif}header,main,footer{max-width:76rem;margin:auto;padding:1.2rem}header{background:#e7f0f4}h1{line-height:1.15}a{color:#075b9a}nav{display:flex;gap:1rem;flex-wrap:wrap}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #a45b00;outline-offset:3px}article{border:1px solid #bbccd6;border-radius:.4rem;padding:1rem;margin:1rem 0;background:white;overflow-wrap:anywhere}code,pre{white-space:pre-wrap;overflow-wrap:anywhere}table{width:100%;border-collapse:collapse;table-layout:fixed}th,td{padding:.55rem;border:1px solid #bbccd6;text-align:left;vertical-align:top;overflow-wrap:anywhere}img{max-width:100%;height:auto}.notice{border-left:5px solid #a96600;background:#fff6e6;padding:.8rem}.controls{display:flex;gap:1rem;flex-wrap:wrap}.controls>label{display:flex;flex-direction:column;min-width:0;max-width:100%;flex:1 1 15rem}input,select,button{font:inherit;padding:.45rem;max-width:100%;box-sizing:border-box}input{width:28rem}.skip{position:absolute;left:-9999px}.skip:focus{position:static}.diagram{overflow:auto;max-height:75vh;background:white}.diagram img{max-width:none;width:1100px}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}@media(max-width:600px){body{font-size:16px}header,main,footer{padding:.8rem}table{font-size:.9rem}th,td{padding:.35rem}}@media(prefers-color-scheme:dark){body{background:#13212a;color:#edf4f7}header,article{background:#20343f}a{color:#8fceff}.notice{background:#3d3020}input,select,button{background:#20343f;color:#edf4f7}.diagram{background:white}}'''
NAV=[('index.html','Overview'),('catalog.html','Domains and concepts'),('relations.html','Relations'),('formal.html','Formal terms'),('guide.html','Formal interpretation'),('diagrams.html','Diagrams'),('explorer/index.html','Explorer'),('tutorial.html','Tutorial'),('sources.html','Sources and limits')]
def shell(title,body,extra=''):
 return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' | SemRisk rc.4</title><style>'+CSS+'</style></head><body><a class="skip" href="#main">Skip to content</a><header><h1>'+esc(title)+'</h1><p>SemRisk ontology documentation · 0.2.0-rc.4 · documentation revision 2026-10-06</p><nav aria-label="Documentation">'+''.join('<a href="'+p+'">'+t+'</a>' for p,t in NAV)+'</nav><p><a href="../../0.1.0-rc.1/docs-20261006/index.html">Historical rc.1</a> · <a href="../../../index.html">Version index</a> · <a href="'+WIKI+'Home">Wiki</a></p></header><main id="main"><p class="notice">Documentation candidate, not a scholarly release or independent validation. OWL sources and governed registries remain authoritative. No manuscript is included.</p>'+body+'</main><footer>Source snapshot <code>'+REF+'</code>. '+source('ontology/vendor/GUFO-LICENSE','gUFO CC BY 4.0 notice')+'; '+source('ontology/vendor/gufo-v1.0.0.ttl','vendored gUFO source')+'. No repository-wide reuse license is inferred. <a href="sources.html#rights">Attribution and rights</a></footer>'+extra+'</body></html>\n'
def search_script(selector):
 return '<script>const q=document.getElementById("query"),m=document.getElementById("module");function filter(){let n=0;document.querySelectorAll("'+selector+'").forEach(e=>{const raw=q.value.trim(),query=raw.toLowerCase(),isIri=raw.startsWith("urn:"),isId=/^sr-(cpt|rel)-[0-9]{3}$/i.test(raw),exact=e.dataset.iri&&(isIri||isId);const matched=exact?(isIri?e.dataset.iri===raw:e.dataset.iri.endsWith(":"+raw.toUpperCase())):e.textContent.toLowerCase().includes(query);const yes=matched&&(!m.value||e.dataset.module.split("/").includes(m.value));e.hidden=!yes;if(yes)n++;});document.getElementById("count").textContent=n+" matching entries";}q.addEventListener("input",filter);m.addEventListener("change",filter);const initial=new URLSearchParams(location.search).get("module");if(initial&&[...m.options].some(o=>o.value===initial))m.value=initial;filter();function revealHash(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}const target=document.getElementById(id);if(target&&target.matches("'+selector+'")){q.value="";m.value="";filter();target.scrollIntoView();}}window.addEventListener("hashchange",revealHash);document.querySelectorAll("a[href]").forEach(a=>a.addEventListener("click",()=>setTimeout(revealHash,0)));revealHash();</script>'
def controls(modules,label):return '<div class="controls"><label>'+label+' <input id="query" type="search"></label><label>Module or domain <select id="module"><option value="">All</option>'+''.join('<option>'+esc(m)+'</option>' for m in modules)+'</select></label></div><p id="count" role="status"></p>'
def markdown_body(text):return markdown.markdown(text,extensions=['tables','fenced_code','toc'])
def rebase_md(text,path):
 def f(m):
  v=m.group(1)
  if re.match(r'https?://',v):return m.group(0)
  if v.startswith('#'):return m.group(0)
  target,sep,fragment=v.partition('#');p=(ROOT/path).parent.joinpath(target).resolve().relative_to(ROOT.resolve()).as_posix()
  assert not p.startswith('publications/'),p
  assert (ROOT/p).exists(),p
  return ']('+REPO+p+('#'+fragment if sep else '')+')'
 return re.sub(r'\]\(([^)]+)\)',f,text)
def build():
 OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
 inventory=rows('docs/formal/0.2.0-rc.4/entity-inventory.csv');concepts=rows('conceptualization/core/core-concept-registry-v0.1.csv');relations=rows('conceptualization/core/relation-registry-v0.1.csv');audit=rows('foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv');g=Graph().parse(SOURCE/'asserted-closure.nt',format='nt')

 for a in audit:
  if a['relation_id'] not in {r['rel_id'] for r in relations}:
   iri=URIRef('urn:semrisk:entity:'+a['relation_id']);definition='; '.join(str(x) for x in g.objects(iri,RDFS.comment)) or a['label']
   relations.append({'rel_id':a['relation_id'],'label':a['label'],'definition':definition,'domain_candidate':a['domain_conceptual'],'range_candidate':a['range_conceptual'],'ownership':'Core','status':a['formal_status'],'conflicts_uncertainty':a['semantic_warning']})
 assert len(inventory)==116 and len(concepts)==47 and len(relations)==40 and len(g)==1618
 for r in inventory:assert sha((ROOT/r['source_path']).read_bytes())==r['source_sha256']
 output={}
 output['index.html']=shell('SemRisk ontology documentation','''<h2>Choose a reading path</h2><p>Researchers: read the domain and concept definitions, compare the formal commitments, then inspect source and limitation records. Engineers: locate a term, inspect its exact source and SHACL obligations, then run the bounded tutorial.</p><h2>Current source inventory</h2><ul><li>Seven version-bound modules plus pinned gUFO; 1,618 asserted triples.</li><li>116 local declarations: 46 classes (35 domain classes and 11 helpers), 50 object properties, eight datatype properties, one annotation property, seven named individuals and four markers.</li><li>The conceptual registry separately has 47 concepts and 40 relation decisions. These are different counting units.</li></ul><h2>What remains open</h2><p>Full current SQL parity is deferred. Independent domain review and transfer evidence, full OntoUML acceptance and final scholarly release remain open. Browser checks assess documentation behavior, not scientific validity.</p>'''+source('ontology/releases/0.2.0-rc.4/README.md','Current candidate source manifest'))
 # Concept catalog includes exact governed definitions; future domain portfolio is kept separate.
 roadmap_path='docs/research/domain-profile-roadmap.md';roadmap=(ROOT/roadmap_path).read_text();portfolio=[]
 for l in roadmap.splitlines():
  if l.startswith('| `P'):
   v=[x.strip() for x in l.strip('|').split('|')];portfolio.append((v[1].replace('**',''),v[2],v[0]))
 body='<h2 id="domains">Domain portfolio</h2><p>Planning priorities are not implemented domain ontologies. Concept memberships are registry assignments, not formal subclass axioms.</p><table><thead><tr><th>Domain</th><th>Scope</th><th>Priority</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(c)+'</td>' for c in row)+'</tr>' for row in portfolio)+'</tbody></table>'
 mods=sorted({m for r in concepts for m in r['module_profile'].split('/')});body+='<h2 id="concepts">All 47 concept definitions</h2>'+controls(mods,'Search concepts')
 for r in concepts:body+=f'<article class="concept" id="{r["semantic_id"]}" data-module="{esc(r["module_profile"])}"><h3>{esc(r["semantic_id"])} · {esc(r["preferred_term"])}</h3><p>{esc(r["definition"])}</p><p>Scope: {esc(r["module_profile"])}. Status: {esc(r["concept_status"])}.</p><p>Inherited registry note: {esc(r["conflicts_uncertainty"])}</p>'+('<p>Current disposition: Trigger is event-only; enabling conditions are modeled separately. The older alternatives in the inherited note are superseded by the current definition.</p>' if r['semantic_id']=='SR-CPT-005' else '')+source('conceptualization/core/core-concept-registry-v0.1.csv','Governed definition source')+'</article>'
 output['catalog.html']=shell('Domains and concepts',body,search_script('.concept'))
 body='<p>These 40 registry decisions are conceptual descriptions, not a claim of 40 OWL object properties. Candidate multiplicities are not imposed as universal constraints; see the actual formal sources.</p>'+controls(sorted({m for r in relations for m in r['ownership'].split('/')}),'Search relations')
 for r in relations:body+=f'<article class="relation" id="{r["rel_id"]}" data-module="{esc(r["ownership"])}"><h2>{esc(r["rel_id"])} · {esc(r["label"])}</h2><p>{esc(r["definition"])}</p><p>Candidate endpoints: {esc(r["domain_candidate"])} → {esc(r["range_candidate"])}.</p><p>Owner: {esc(r["ownership"])}; status: {esc(r["status"])}.</p><p>Inherited registry note: {esc(r["conflicts_uncertainty"])}</p>'+('<p>Current formal disposition: SR-REL-038 is an OWL annotation property; it is not an object-property edge. The earlier registry alternative is historical.</p>' if r['rel_id']=='SR-REL-038' else '')+source('foundational/exposure-scale-v0.2.0-rc.4/relation-formal-audit.csv','Current relation audit')+'</article>'
 output['relations.html']=shell('Relation decisions',body,search_script('.relation'))
 old=(ROOT/'site/ontology/0.2.0-rc.4/index.html').read_text();body=old.split('<main id="main">',1)[1].split('</main>',1)[0];body=body.replace('href="#term-','href="formal.html#term-');body='<p>Asserted-only source projection. Imported and anonymous expressions remain in the complete graph; no entailment completeness is claimed.</p>'+controls(MODULES,'Search all formal terms')+body
 # Add module tags to all term articles using exact inventory.
 for r in inventory:
  anchor='term-'+r['iri'].rsplit(':',1)[-1];body=body.replace('<article id="'+anchor+'">','<article class="term" data-iri="'+esc(r['iri'])+'" data-module="'+Path(r['source_path']).stem+'" id="'+anchor+'">')
 output['formal.html']=shell('All 116 formal terms',body,search_script('article.term'))
 curated=(ROOT/'docs/formal/formal-ontology-description-rc4.md').read_text().replace('Readable paper example','Readable ontology example')
 output['guide.html']=shell('Formal interpretation FD-A through FD-J',markdown_body(rebase_md(curated,'docs/formal/formal-ontology-description-rc4.md')))
 diagram=ROOT/'diagrams/ontouml/0.2.0-rc.4/views';svgs=sorted(p for p in diagram.glob('*.svg') if not p.stem.endswith('-review'));assert len(svgs)==15
 body='<p>Fifteen canonical views preserve the registry distinctions. Browser pan/zoom is a navigation aid; the original complete atlas fails 170 mm print readability. Native-editor and complete OntoUML acceptance remain open. These are existing source-bound views, not the unpublished print companion.</p><nav aria-label="Diagram views">'+''.join('<a href="#'+p.stem+'">'+esc(p.stem)+'</a>' for p in svgs)+'</nav>'
 for p in svgs:
  output['diagrams/'+p.name]=p.read_text();body+='<article id="'+p.stem+'"><h2>'+esc(p.stem)+'</h2><a href="diagrams/'+p.name+'">Open full-size SVG</a><div class="diagram" tabindex="0" role="region" aria-label="Scrollable '+esc(p.stem)+' diagram"><img src="diagrams/'+p.name+'" alt="'+esc(p.stem)+' OntoUML-derived view; exact concepts and relation definitions are available in the adjacent catalogs"></div></article>'
 output['diagrams.html']=shell('Navigable conceptual diagrams',body)
 tutorial='''# Bounded rc.4 tutorial

This engineering exercise reads committed synthetic ontology artifacts. It does not use private source workbooks, demonstrate treatment effects or test SQL parity.

## 1. Obtain the exact source snapshot

```sh
git clone https://github.com/ArazSaieArasi3/SemRisk.git
cd SemRisk
git checkout 67247f13ba5d0c7d32163f2b3e848af15067d92e
python -m venv .venv
. .venv/bin/activate
python -m pip install rdflib==7.6.0
```

## 2. Inspect an explicit asserted distinction

```python
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDFS
root = Path('.')
g = Graph().parse(root / 'docs/formal/0.2.0-rc.4/asserted-closure.nt', format='nt')
scenario = URIRef('urn:semrisk:entity:SR-CPT-006')
event = URIRef('urn:semrisk:entity:SR-CPT-007')
assert len(g) == 1618
assert (scenario, OWL.disjointWith, event) in g or (event, OWL.disjointWith, scenario) in g
assert (scenario, RDFS.subClassOf, URIRef('http://purl.org/nemo/gufo#SituationType')) in g
print('1618 asserted triples; scenario/event distinction found')
```

Expected output is the one printed line. This reads explicit triples; it does not run an OWL reasoner. Removing the checked disjointness triple makes the corresponding assertion fail. A record's workflow status does not by itself establish a change in the managed Risk.

## 3. Trace the interpretation

Locate SR-CPT-006 and SR-CPT-007 in the formal term index, read their exact source modules and compare the scenario/occurrence conceptual view. Use the Explorer only as a locator. Anonymous axioms and omitted constructs must be checked in the formal source, not inferred from graph position.

## 4. Keep versions separate

The historical rc.1 route and its tests retain their old inputs and denominators. Do not transfer its eight-task SQL result to the complete rc.4 candidate. External reader tasks and final release identity remain open.
'''
 output['tutorial.html']=shell('Reproduce a bounded source check',markdown_body(tutorial));(DOC/'tutorial.md').write_text(tutorial)
 corpus=['literature/closest-ontology-technical-baseline.md','literature/closest-work-comparison-matrix.csv','literature/standards-frameworks-baseline.md','literature/review-protocol.md','literature/search-log.csv','conceptualization/source-mining/source-registry-v0.1.csv']
 corpus=[p for p in corpus if (ROOT/p).is_file()]
 body='<h2>Source corpus and comparison</h2><ul>'+''.join('<li>'+source(p,p)+'</li>' for p in corpus)+'</ul><p>Comparator missing locators are evidence gaps, not proof of absent capability. Source roles and asserted/formal/application evidence remain distinct.</p><h2 id="rights">Attribution and rights</h2><p>gUFO by João Paulo A. Almeida, Giancarlo Guizzardi, Tiago Prince Sales and Ricardo A. Falbo; pinned vendored source and CC BY 4.0 notice below. The explorer reuses WebVOWL 1.1.7 under MIT, D3 3.5.17 under BSD-3-Clause and Lodash under its bundled MIT notice. Their notices are retained with the runtime. No root SemRisk reuse license is selected by this documentation deployment.</p><p>Only allowlisted ontology documentation and existing public diagram assets are included. No private workbook, manuscript, manuscript projection, Word/PDF manuscript download or unpublished diagram companion is packaged.</p><h2>Evaluation limits</h2><p>Independent reader/domain-review tasks are not completed by automation. SQL parity, independent transfer, complete OntoUML acceptance and scholarly release remain separate gates. Technical browser tests establish only their recorded routes, viewports and interactions.</p>'
 output['sources.html']=shell('Sources, attribution and limitations',body)
 for rel,content in output.items():p=OUT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
 # New historical presentation; original frozen route bytes are never modified.
 hist=ROOT/'site/ontology/0.1.0-rc.1/docs-20261006';hist.mkdir(parents=True,exist_ok=True)
 old=(ROOT/'site/ontology/0.1.0-rc.1/index.html').read_text().replace('offline Pages bundle, not deployed or released','historical source projection, not a scholarly release')
 old=old.replace('<body>','<body><p><a href="../../0.2.0-rc.4/docs-20261006/index.html">Current rc.4 documentation</a> · <a href="../../../index.html">Version index</a></p>')
 (hist/'index.html').write_text(old)
 root='<h1>SemRisk ontology documentation</h1><p>Version-specific documentation candidates; canonical OWL remains authoritative. No manuscript or scholarly release is included.</p><ul><li><a href="ontology/0.2.0-rc.4/docs-20261006/index.html">Current 0.2.0-rc.4 documentation</a></li><li><a href="ontology/0.1.0-rc.1/docs-20261006/index.html">Historical 0.1.0-rc.1 source reference</a></li></ul><p><a href="'+WIKI+'Home">Wiki reading paths</a></p>'
 (ROOT/'site/index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SemRisk versions</title><style>'+CSS+'</style></head><body><main>'+root+'</main></body></html>\n')
 print('Built ontology-only documentation; explorer generated separately')
if __name__=='__main__':build()
