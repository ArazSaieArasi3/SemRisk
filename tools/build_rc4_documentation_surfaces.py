#!/usr/bin/env python3
"""Offline rc.4 source projections only. Never deploy or overwrite a historical route."""
import argparse,csv,hashlib,html,json,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import markdown
from rdflib import Graph,URIRef,Literal
from rdflib.namespace import RDF,RDFS,OWL
from generate_rc4_formal_reference import build as formal_build
ROOT=Path(__file__).resolve().parents[1]
REF='bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6';REPO='https://github.com/ArazSaieArasi3/SemRisk/blob/'+REF+'/'
OUT=Path('site/ontology/0.2.0-rc.4');DOC=Path('docs/documentation/rc4');WIKI=Path('docs/wiki/rc4/Formal-Reference.md')
BASE=Path('docs/formal/0.2.0-rc.4');CURATED=Path('docs/formal/formal-ontology-description-rc4.md')
SR='urn:semrisk:entity:';G='http://purl.org/nemo/gufo#';IS='urn:semrisk:profile:information-state:';AC='urn:semrisk:profile:assessment-context:'
CRITICAL={SR+'SR-CPT-001':None,SR+'SR-CPT-006':G+'SituationType',SR+'SR-CPT-007':G+'Event',SR+'SR-CPT-010':G+'Situation',SR+'SR-CPT-011':G+'Event',SR+'SR-CPT-013':IS+'ArtifactVersion',SR+'SR-CPT-026':IS+'ArtifactVersion',SR+'SR-CPT-027':IS+'ArtifactVersion',SR+'SR-CPT-028':G+'Event',SR+'SR-CPT-029':None,SR+'SR-CPT-033':IS+'ManagedInformationArtifact',SR+'SR-CPT-035':G+'Situation',SR+'SR-CPT-036':G+'QualityValue',AC+'NumericScale':IS+'ArtifactVersion'}
LABELS=dict(zip(list(CRITICAL)[:-1],['Risk','Risk Scenario','Risk Event','Exposure','Risk Assessment Activity','Risk Assessment Result','Risk Treatment Strategy','Risk Treatment Plan','Risk Treatment Activity','Control Mechanism','Risk Register Entry','Risk State','Workflow State']))
NOTICE='Offline rc.4 documentation candidate. Not a live Wiki update, deployed Pages site, final scholarly release, full OntoUML acceptance or independent domain validation.'
def digest(b):return hashlib.sha256(b).hexdigest()
def esc(v):return html.escape(str(v),quote=True)
def anchor(iri):return 'term-'+iri.rsplit(':',1)[-1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.hrefs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and 'href' in a:self.hrefs.append(a['href'])
def validate(g,rows,m):
 if len(rows)!=116 or len({r['iri'] for r in rows})!=116:raise ValueError('INVENTORY_DENOMINATOR')
 if len(g)!=1618 or m['asserted_triples']!=1618 or m['declared_entity_count']!=116:raise ValueError('GRAPH_DENOMINATOR')
 for iri,parent in CRITICAL.items():
  if iri in LABELS and not any(str(o)==LABELS[iri] for o in g.objects(URIRef(iri),RDFS.label)):raise ValueError('CRITICAL_LABEL')
  if iri not in {r['iri'] for r in rows}:raise ValueError('CRITICAL_ID')
  if parent and (URIRef(iri),RDFS.subClassOf,URIRef(parent)) not in g:raise ValueError('CRITICAL_PARENT')
  if not parent and list(g.objects(URIRef(iri),RDFS.subClassOf)):raise ValueError('PATTERN_BOUNDARY')
 for a,b in [(6,7),(11,13),(1,33),(35,36)]:
  a,b=URIRef(SR+f'SR-CPT-{a:03}'),URIRef(SR+f'SR-CPT-{b:03}')
  if (a,OWL.disjointWith,b) not in g and (b,OWL.disjointWith,a) not in g:raise ValueError('CRITICAL_DISJOINTNESS')
 if not any(set(g.items(head))=={URIRef(SR+f'SR-CPT-{n:03}') for n in [26,27,28,29]} for node in g.subjects(RDF.type,OWL.AllDisjointClasses) for head in g.objects(node,OWL.members)):raise ValueError('TREATMENT_DISJOINT_SET')
 if (URIRef(SR+'SR-CPT-029'),RDF.type,URIRef(G+'RoleMixin')) not in g:raise ValueError('CONTROL_METATYPE')
 for n,target in [(39,2),(40,3)]:
  p=URIRef(SR+f'SR-REL-{n:03}')
  if (p,RDFS.domain,URIRef(SR+'SR-CPT-010')) not in g or (p,RDFS.range,URIRef(SR+f'SR-CPT-{target:03}')) not in g:raise ValueError('EXPOSURE_ENDPOINT')
 for r in rows:
  p=ROOT/r['source_path']
  if not p.is_file() or digest(p.read_bytes())!=r['source_sha256']:raise ValueError('INVENTORY_SOURCE')
CSS='''body{font:17px/1.55 system-ui,sans-serif;color:#182b3a;background:white;margin:0}header,main,footer{max-width:74rem;margin:auto;padding:1.2rem}header{background:#edf4f7}h1{font-size:2rem;line-height:1.2}h2{font-size:1.4rem}a{color:#075b9a}a:focus-visible{outline:3px solid #965000;outline-offset:3px}code,pre{overflow-wrap:anywhere;white-space:pre-wrap}article{border-top:1px solid #a8bcc8;padding:1rem 0;scroll-margin-top:1rem}table{border-collapse:collapse;width:100%;table-layout:fixed}th,td{border:1px solid #a8bcc8;padding:.6rem;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#edf4f7}nav ul{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;padding-left:1.3rem}.notice{border-left:5px solid #b0731c;padding:.7rem;background:#fff6e6}.skip{position:absolute;left:-9999px}.skip:focus{position:static}@media(max-width:600px){body{font-size:16px}header,main,footer{padding:.8rem}h1{font-size:1.65rem}table{font-size:.9rem}th,td{padding:.4rem}}'''
def shell(title,body):return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>'+esc(title)+'</title><style>'+CSS+'</style></head><body><a class="skip" href="#main">Skip to content</a><header><h1>'+esc(title)+'</h1><p class="notice">'+NOTICE+'</p><nav aria-label="Reference navigation"><ul><li><a href="index.html">All 116 local terms</a></li><li><a href="guide.html">Curated FD-A–FD-J interpretation</a></li><li><a href="wiki-draft.md">Wiki draft source</a></li></ul></nav></header><main id="main">'+body+'</main><footer>Source snapshot <code>'+REF+'</code>. Historical Wiki and rc.1 routes remain separate.</footer></body></html>\n'
def links_check(outputs):
 for p,text in outputs.items():
  if p.suffix!='.html':continue
  parser=Links();parser.feed(text)
  if len(parser.ids)!=len(set(parser.ids)):raise ValueError('DUPLICATE_ANCHOR')
  if '<script' in text.lower() or '<iframe' in text.lower():raise ValueError('ACTIVE_CONTENT')
  for href in parser.hrefs:
   if href.startswith(REPO):
    target=href[len(REPO):].split('#')[0]
    if not (ROOT/target).is_file():raise ValueError('MISSING_PINNED_SOURCE')
    continue
   if urlsplit(href).scheme:raise ValueError('UNPINNED_LINK: '+href)
   target,_,fragment=href.partition('#');target=p.parent/(target or p.name)
   if target not in outputs:raise ValueError('BROKEN_LOCAL_LINK: '+href)
   if fragment:
    tp=Links();tp.feed(outputs[target])
    if fragment not in tp.ids:raise ValueError('BROKEN_ANCHOR: '+href)
LOCK_SHA256='1854781aed6f962fe98b4d1389d90e8039732ef54018eee90e6545850548b873'
def verify_source_lock(read_bytes=None):
 read_bytes=read_bytes or (lambda p:(ROOT/p).read_bytes())
 raw=read_bytes(str(DOC/'baseline-source-lock.json'))
 if digest(raw)!=LOCK_SHA256:raise ValueError('BASELINE_LOCK_DRIFT')
 lock=json.loads(raw)
 if lock['source_commit']!=REF:raise ValueError('BASELINE_COMMIT_DRIFT')
 for p,expected in lock['files'].items():
  data=read_bytes(p)
  if digest(data)!=expected['sha256'] or hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=expected['git_blob_sha']:raise ValueError('PINNED_SOURCE_DRIFT: '+p)
 return lock
def build():
 verify_source_lock()
 for p,v in formal_build(ROOT).items():
  if (ROOT/p).read_text()!=v:raise ValueError('FORMAL_PROJECTION_DRIFT: '+str(p))
 g=Graph().parse(ROOT/BASE/'asserted-closure.nt',format='nt');rows=list(csv.DictReader((ROOT/BASE/'entity-inventory.csv').open()));m=json.loads((ROOT/BASE/'source-manifest.json').read_text());validate(g,rows,m)
 ids={r['iri']:anchor(r['iri']) for r in rows}
 if len(set(ids.values()))!=116:raise ValueError('ANCHOR_COLLISION')
 def term(v):return '<a href="#'+ids[str(v)]+'"><code>'+esc(v)+'</code></a>' if str(v) in ids else '<code>'+esc(v)+'</code>'
 body='<h2>Exact version and counting units</h2><p>Seven modules plus pinned gUFO: 1,618 asserted triples; 116 local terms. The separate conceptual and relation-decision registries contain 47 and 40 rows. Anonymous expressions and imported statements remain in the <a href="'+REPO+str(BASE/'asserted-closure.nt')+'">complete graph</a>. This is not an entailment closure or quality score.</p><nav aria-label="Term index"><h2>Local term index</h2><ul>'+''.join('<li><a href="#'+ids[r['iri']]+'">'+esc(r['iri'].rsplit(':',1)[-1])+'</a></li>' for r in rows)+'</ul></nav>'
 for r in rows:
  iri=URIRef(r['iri']);labels=sorted(str(x) for x in g.objects(iri,RDFS.label));label=labels[0] if labels else r['iri'].rsplit(':',1)[-1]
  triples=sorted((str(p),str(o)) for p,o in g.predicate_objects(iri) if isinstance(o,(URIRef,Literal)))
  body+='<article id="'+ids[r['iri']]+'"><h2>'+esc(label)+'</h2><p><code>'+esc(iri)+'</code> · '+esc(r['kind'])+'</p><p><a href="'+REPO+r['source_path']+'">Authoritative local source</a> · SHA-256 <code>'+r['source_sha256']+'</code></p><ul>'+''.join('<li><code>'+esc(p)+'</code> → '+term(o)+'</li>' for p,o in triples)+'</ul></article>'
 curated=(ROOT/CURATED).read_text()
 def rebase(match):
  target=match.group(1)
  if urlsplit(target).scheme:raise ValueError('CURATED_EXTERNAL_LINK_REQUIRES_BINDING: '+target)
  path=(ROOT/CURATED.parent/target).resolve();path=path.relative_to(ROOT.resolve())
  if not (ROOT/path).is_file():raise ValueError('CURATED_BROKEN_SOURCE')
  return ']('+REPO+str(path)+')'
 curated=re.sub(r'\]\(([^)]+)\)',rebase,curated)
 wiki='# rc.4 offline Wiki draft\n\n> '+NOTICE+'\n\nThe existing live Wiki still represents its historical P1-R2 snapshot. This is a separate source projection; Pages remains disabled. The bundled guide and term index have no assigned public URL.\n\n'+curated
 md=markdown.Markdown(extensions=['tables','fenced_code','toc']);guide=md.convert(wiki)
 headings={x['name']:x['id'] for x in md.toc_tokens}
 # Flatten toc to retain every FD-A–J heading below the source title.
 def flatten(xs):
  for x in xs:yield x;yield from flatten(x['children'])
 fd=[x for x in flatten(md.toc_tokens) if re.match(r'FD-[A-J]\b',x['name'])]
 if len(fd)!=10:raise ValueError('FD_SECTION_COVERAGE')
 nav='<nav aria-label="Formal reference sections"><ul>'+''.join('<li><a href="#'+x['id']+'">'+esc(x['name'])+'</a></li>' for x in fd)+'</ul></nav>'
 critical='<section><h2>Critical source commitments</h2><table><thead><tr><th scope="col">Term</th><th scope="col">Asserted superclass</th></tr></thead><tbody>'+''.join('<tr><td><a href="index.html#'+ids[iri]+'">'+esc(iri.rsplit(':',1)[-1])+'</a></td><td><code>'+esc(parent or 'None; pattern / external identity boundary')+'</code></td></tr>' for iri,parent in CRITICAL.items())+'</tbody></table></section>'
 outputs={OUT/'index.html':shell('SemRisk rc.4 asserted formal reference',body),OUT/'guide.html':shell('SemRisk rc.4 curated formal reference',nav+critical+guide),OUT/'wiki-draft.md':wiki,WIKI:wiki}
 links_check(outputs)
 sourcepaths={r['source_path'] for r in rows}|{str(BASE/x) for x in ['entity-inventory.csv','source-manifest.json','asserted-closure.nt']}|{str(CURATED)}
 record={'version':'0.2.0-rc.4','route':'/ontology/0.2.0-rc.4/','source_commit':REF,'state':'OFFLINE_CANDIDATE_NOT_DEPLOYED','asserted_triples':len(g),'local_terms':116,'critical_terms':list(CRITICAL),'fd_sections':10,'source_sha256':{p:digest((ROOT/p).read_bytes()) for p in sorted(sourcepaths)},'output_sha256':{str(p):digest(v.encode()) for p,v in outputs.items()},'live_wiki_updated':False,'pages_deployed':False,'scholarly_release':False}
 outputs[DOC/'surface-bindings.json']=json.dumps(record,indent=2)+'\n'
 return outputs,g,rows,m

def check_existing(existing,proposed):
 if existing is not None and existing!=proposed:raise ValueError('IMMUTABLE_OUTPUT_CHANGED')
def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();outputs,*_=build()
 for path,text in outputs.items():
  if a.write:
   check_existing((ROOT/path).read_text() if (ROOT/path).exists() else None,text)
   (ROOT/path).parent.mkdir(parents=True,exist_ok=True);(ROOT/path).write_text(text)
  elif not (ROOT/path).exists() or (ROOT/path).read_text()!=text:raise ValueError('GENERATED_DRIFT: '+str(path))
 print('RC4_OFFLINE_SURFACE_PASS:116 terms;14 critical terms;10 FD sections;source/local-link checks;no deployment')
if __name__=='__main__':main()
