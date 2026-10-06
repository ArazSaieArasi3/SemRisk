#!/usr/bin/env python3
"""Fail closed on deployable paths, source drift, links and graph/index count conflation."""
import argparse,csv,hashlib,json,re,shutil,tempfile
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from rdflib import Graph,URIRef
from rdflib.namespace import RDFS
from build_public_ontology_docs import ROOT,OUT,DOC,REF,ROUTE
LOCK_SHA256='276b04a6644c5b1a22ac1db21967de37e4d4c3499a0534838d93f49a747178de'
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.assets=[]
 def handle_starttag(self,t,aa):
  a=dict(aa)
  if 'id' in a:self.ids.append(a['id'])
  if t=='a' and 'href' in a:self.links.append(a['href'])
  if t in ['script','img','link'] and ('src' in a or 'href' in a):self.assets.append(a.get('src',a.get('href')))
def sha(b):return hashlib.sha256(b).hexdigest()
def paths():
 roots=[ROOT/'site/index.html',OUT,ROOT/'site/ontology/0.1.0-rc.1/docs-20261006']
 return sorted(p for r in roots for p in ([r] if r.is_file() else r.rglob('*')) if p.is_file())
def permitted(path):
 s=str(path).lower();return not any(x in s for x in ['manuscript','publications/','print-companion','editorial-change','private','workbook']) and path.suffix.lower() in ['.html','.js','.css','.json','.svg','.txt']
def check(files=None):
 files=files or {p:p.read_bytes() for p in paths()};assert files
 raw=(DOC/'publication-byte-lock.json').read_bytes()
 if sha(raw)!=LOCK_SHA256:raise ValueError('LOCK_DRIFT')
 lock=json.loads(raw)
 for p,h in lock['source_sha256'].items():
  if sha((ROOT/p).read_bytes())!=h:raise ValueError('SOURCE_DRIFT:'+p)
 expected={ROOT/'site'/p:h for p,h in lock['exact_deploy_file_sha256'].items()}
 if set(files)!=set(expected):raise ValueError('EXACT_DEPLOY_ALLOWLIST')
 for p,h in expected.items():
  if sha(files[p])!=h:raise ValueError('OUTPUT_BINDING:'+str(p))
 cache={}
 def parsed(p):
  if p not in cache:
   h=HTML();h.feed(files[p].decode());cache[p]=h
  return cache[p]
 for p,b in files.items():
  if not permitted(p.relative_to(ROOT/'site')):raise ValueError('FORBIDDEN_DEPLOY_PATH')
  if p.suffix not in ['.html','.json']:continue
  text=b.decode()
  if re.search(r'(?:href|src)=[\"\'][^\"\']*(?:manuscript|publications/|print-companion|\.docx)',text,re.I):raise ValueError('MANUSCRIPT_LINK')
  if p.suffix!='.html':continue
  h=parsed(p)
  if len(h.ids)!=len(set(h.ids)):raise ValueError('DUPLICATE_ID:'+str(p))
  for href in h.links+h.assets:
   u=urlsplit(href)
   if u.scheme:
    if href in h.assets and not href.startswith('data:'):raise ValueError('REMOTE_ASSET')
    if u.scheme not in ['https','http','data','mailto']:raise ValueError('UNSAFE_PROTOCOL')
    if u.netloc=='github.com' and '/blob/' in u.path:
     z=u.path.split('/blob/',1)[1].split('/',1)
     if z[0]==REF and not (ROOT/z[1]).is_file():raise ValueError('BROKEN_SOURCE:'+href)
    continue
   if p.parent.name=='explorer' and href.startswith('#'):continue # viewer state, not DOM anchors
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   if target.is_dir():target=target/'index.html'
   if target not in files:raise ValueError('BROKEN_LOCAL:'+str(p)+':'+href)
   if u.fragment and target.suffix=='.html':
    hh=parsed(target)
    if unquote(u.fragment) not in hh.ids:raise ValueError('BROKEN_ANCHOR:'+href)
 # Inventory independently cross-checks graph signatures and term index anchors.
 inv=list(csv.DictReader((ROOT/'docs/formal/0.2.0-rc.4/entity-inventory.csv').open()));g=Graph().parse(ROOT/'docs/formal/0.2.0-rc.4/asserted-closure.nt',format='nt')
 h=HTML();h.feed(files[OUT/'formal.html'].decode());expected={'term-'+r['iri'].rsplit(':',1)[-1] for r in inv}
 if not expected.issubset(set(h.ids)) or len(expected)!=116:raise ValueError('TERM_INDEX_COVERAGE')
 data=json.loads(files[OUT/'explorer/data/semrisk.json']);actual={x.get('iri') for x in data['classAttribute'] if x.get('iri') in {r['iri'] for r in inv}}
 if actual!={r['iri'] for r in inv if r['kind']=='class'}:raise ValueError('GRAPH_CLASS_COVERAGE')
 edges={x.get('iri'):x for x in data['propertyAttribute'] if x.get('iri')};expected_edges={}
 for r in inv:
  if r['kind'] not in ['object_property','datatype_property']:continue
  d=list(g.objects(URIRef(r['iri']),RDFS.domain));v=list(g.objects(URIRef(r['iri']),RDFS.range))
  if len(d)==len(v)==1 and isinstance(d[0],URIRef) and isinstance(v[0],URIRef):expected_edges[r['iri']]=(str(d[0]),str(v[0]))
 if set(edges)!=set(expected_edges) or len(edges)!=24:raise ValueError('GRAPH_PROPERTY_COVERAGE')
 ids={x['id']:x['iri'] for x in data['classAttribute']}
 for iri,e in edges.items():
  if (ids[e['domain']],ids[e['range']])!=expected_edges[iri]:raise ValueError('INVENTED_ENDPOINT')
 projection=json.loads(files[OUT/'explorer/projection.json'])
 if projection['all_declarations']!=116 or projection['source_commit']!=REF:raise ValueError('PROJECTION_IDENTITY')
 for preset in projection['presets']:
  module=preset['module'];selected=[r for r in inv if module=='all' or Path(r['source_path']).stem==module]
  local={r['iri'] for r in selected if r['kind']=='class'};expected_props={r['iri']:expected_edges[r['iri']] for r in selected if r['iri'] in expected_edges}
  expected_supers={(i,str(p)) for i in local for p in g.objects(URIRef(i),RDFS.subClassOf) if isinstance(p,URIRef)}
  data=json.loads(files[OUT/'explorer/data'/(preset['preset']+'.json')]);names={x['id']:x['iri'] for x in data['classAttribute']};types={x['id']:x['type'] for x in data['property']}
  props={x['iri']:(names[x['domain']],names[x['range']]) for x in data['propertyAttribute'] if x.get('iri')}
  supers={(names[x['domain']],names[x['range']]) for x in data['propertyAttribute'] if types[x['id']]=='rdfs:subClassOf'}
  expected_nodes=local|{i for pair in expected_props.values() for i in pair}|{p for _,p in expected_supers}
  if props!=expected_props or supers!=expected_supers or set(names.values())!=expected_nodes:raise ValueError('MODULE_ASSERTION_PARITY')
  omitted={r['iri'] for r in selected if r['kind'] in ['object_property','datatype_property'] and r['iri'] not in expected_props}
  if {x['iri'] for x in preset['index_only_properties']}!=omitted or preset['term_index_count']!=len(selected) or preset['graph_local_classes']!=len(local):raise ValueError('OMISSION_LEDGER')
  if set(preset['graph_explicit_property_iris'])!=set(expected_props) or preset['json_sha256']!=sha(files[OUT/'explorer/data'/(preset['preset']+'.json')]):raise ValueError('PRESET_MANIFEST')
 app=files[OUT/'explorer/js/webvowl.app.js'].decode()
 if any(x in app for x in ['new XMLHttpRequest','new FormData']) or app.count('d3.xhr(')!=1:raise ValueError('NETWORK_CODE')
 core=files[OUT/'explorer/js/webvowl.js'].decode()
 if 'editMode = true,' in core or 'editMode = false; graph.options().setEditorModeForDefaultObject(false); return false;' not in core:raise ValueError('EDITOR_STATE_ENABLED')
 if 'indexOf(ontology)===-1' not in app or 'indexOf(preset)===-1' not in app:raise ValueError('PRESET_ALLOWLIST')
 return {'deploy_files':len(files),'term_index':116,'graph_local_classes':46,'graph_explicit_object_properties':24,'index_only_object_properties':26,'index_only_datatype_properties':8,'manuscript_payloads':0}
def negatives():
 original={p:p.read_bytes() for p in paths()};tests=[]
 def reject(name,mutate):
  f=dict(original);mutate(f)
  try:check(f)
  except (ValueError,AssertionError,KeyError):tests.append(name)
  else:raise AssertionError('MUTATION_ACCEPTED:'+name)
 reject('manuscript_path',lambda f:f.update({ROOT/'site/manuscript.html':b'<p>x</p>'}))
 reject('docx_payload',lambda f:f.update({ROOT/'site/file.docx':b'x'}))
 reject('publication_link',lambda f:f.update({OUT/'index.html':f[OUT/'index.html'].replace(b'</main>',b'<a href="publications/draft.md">paper</a></main>')}))
 reject('remote_asset',lambda f:f.update({OUT/'index.html':f[OUT/'index.html'].replace(b'</main>',b'<img src="https://example.com/x.png"></main>')}))
 reject('missing_local_link',lambda f:f.update({OUT/'index.html':f[OUT/'index.html'].replace(b'catalog.html',b'absent.html')}))
 reject('missing_term',lambda f:f.update({OUT/'formal.html':f[OUT/'formal.html'].replace(b'id="term-SR-CPT-001"',b'id="wrong"')}))
 reject('upload_implementation',lambda f:f.update({OUT/'explorer/js/webvowl.app.js':f[OUT/'explorer/js/webvowl.app.js']+b'new XMLHttpRequest();'}))
 reject('unbounded_loader',lambda f:f.update({OUT/'explorer/js/webvowl.app.js':f[OUT/'explorer/js/webvowl.app.js'].replace(b'indexOf(preset)===-1',b'false')}))
 def badedge(f):
  p=OUT/'explorer/data/semrisk.json';d=json.loads(f[p]);next(x for x in d['propertyAttribute'] if x.get('iri'))['domain']='99999';f[p]=json.dumps(d).encode()
 reject('invented_endpoint',badedge)
 reject('arbitrary_extra_json',lambda f:f.update({ROOT/'site/notes.json':b'{}'}))
 def alter(p,old,new):return lambda f:f.update({p:f[p].replace(old,new,1)})
 reject('formal_semantic_drift',alter(OUT/'formal.html',b'disjointWith',b'equivalentClass'))
 reject('module_data_drift',alter(OUT/'explorer/data/semrisk-core.json',b'"domain":"',b'"domain":"999'))
 reject('runtime_fetch_injection',lambda f:f.update({OUT/'explorer/js/webvowl.js':f[OUT/'explorer/js/webvowl.js']+b'fetch("https://example.com")'}))
 def subclass(f):
  p=OUT/'explorer/data/semrisk.json';d=json.loads(f[p]);ids={x['id'] for x in d['property'] if x['type']=='rdfs:subClassOf'};e=next(x for x in d['propertyAttribute'] if x['id'] in ids);e['domain'],e['range']=e['range'],e['domain'];f[p]=json.dumps(d).encode()
 reject('reversed_subclass',subclass)
 reject('editor_initial_state',alter(OUT/'explorer/js/webvowl.js',b'editMode = false,',b'editMode = true,'))
 return tests
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--stage',type=Path);a=ap.parse_args();result=check();result['negative_controls']=negatives()
 if a.stage:
  if a.stage.exists() and any(a.stage.iterdir()):raise ValueError('STAGING_DESTINATION_NOT_EMPTY')
  a.stage.mkdir(parents=True,exist_ok=True)
  for p in paths():d=a.stage/p.relative_to(ROOT/'site');d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes(p.read_bytes())
  (a.stage/'.nojekyll').write_text('')
 manifest={'source_commit':REF,'route':str(ROUTE.relative_to('site')),'files':{str(p.relative_to(ROOT/'site')):sha(p.read_bytes()) for p in paths()},'validation':result}
 (DOC/'deployment-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(result,indent=2))
