#!/usr/bin/env python3
"""Positive/source/render projections and deliberately corrupted offline surfaces."""
import argparse,copy,json,subprocess,sys
from pathlib import Path
from rdflib import Graph,URIRef,Literal
from rdflib.namespace import RDFS
from check_rc4_surface_history import verify as verify_history
from build_rc4_documentation_surfaces import ROOT,OUT,DOC,SR,G,AC,REPO,build,validate,links_check,digest,check_existing,verify_source_lock

def rejects(label,fn,expected):
 try:fn()
 except (ValueError,KeyError) as e:
  if expected not in str(e):raise AssertionError((label,str(e),expected))
 else:raise AssertionError('ACCEPTED_MUTATION: '+label)
 return label

def run():
 outputs,g,rows,m=build()
 for p,v in outputs.items():
  if (ROOT/p).read_text()!=v:raise ValueError('GENERATED_DRIFT: '+str(p))
 negatives=[]
 lock=verify_source_lock();target='ontology/releases/0.2.0-rc.4/core.ttl'
 changed=(ROOT/target).read_bytes()+b'\n# Changed after the claimed source commit\n'
 # Recomputing a working source hash cannot change the independently pinned baseline lock.
 refreshed=dict(lock);refreshed['files']=dict(lock['files']);refreshed['files'][target]={'sha256':digest(changed),'git_blob_sha':'0'*40}
 negatives.append(rejects('changed source despite refreshed working hashes',lambda:verify_source_lock(lambda p:changed if p==target else (ROOT/p).read_bytes()),'PINNED_SOURCE_DRIFT'))
 negatives.append(rejects('rewritten baseline lock',lambda:verify_source_lock(lambda p:json.dumps(refreshed).encode() if p==str(DOC/'baseline-source-lock.json') else (ROOT/p).read_bytes()),'BASELINE_LOCK_DRIFT'))
 for label,change,expected in [
 ('missing inventory row',lambda r:r.pop(),'INVENTORY_DENOMINATOR'),
 ('duplicate inventory ID',lambda r:r[-1].update(iri=r[0]['iri']),'INVENTORY_DENOMINATOR'),
 ('source hash drift',lambda r:r[0].update(source_sha256='0'*64),'INVENTORY_SOURCE')]:
  r=copy.deepcopy(rows);change(r);negatives.append(rejects(label,lambda:validate(g,r,m),expected))
 for label,s,p,old,new,expected in [
 ('scenario wrong category',URIRef(SR+'SR-CPT-006'),RDFS.subClassOf,URIRef(G+'SituationType'),URIRef(G+'Event'),'CRITICAL_PARENT'),
 ('critical label drift',URIRef(SR+'SR-CPT-001'),RDFS.label,Literal('Risk',lang='en'),Literal('Workflow State',lang='en'),'CRITICAL_LABEL'),
 ('scale identity drift',URIRef(AC+'NumericScale'),RDFS.subClassOf,URIRef('urn:semrisk:profile:information-state:ArtifactVersion'),URIRef(G+'Quality'),'CRITICAL_PARENT')]:
  h=Graph();h+=g;h.remove((s,p,old));h.add((s,p,new));negatives.append(rejects(label,lambda:validate(h,rows,m),expected))
 for label,change,expected in [
 ('broken anchor',lambda o:o.__setitem__(OUT/'guide.html',o[OUT/'guide.html'].replace('index.html#term-SR-CPT-001','index.html#missing')),'BROKEN_ANCHOR'),
 ('stale source ref',lambda o:o.__setitem__(OUT/'index.html',o[OUT/'index.html'].replace(REPO,REPO.replace('bd7b6a8ae55c959383a4a10c9b03744cdfaa9cb6','main'))),'UNPINNED_LINK'),
 ('duplicate HTML ID',lambda o:o.__setitem__(OUT/'index.html',o[OUT/'index.html'].replace('<main id="main">','<main id="main"><div id="main"></div>')),'DUPLICATE_ANCHOR'),
 ('missing guide file',lambda o:o.pop(OUT/'guide.html'),'BROKEN_LOCAL_LINK'),
 ('active content',lambda o:o.__setitem__(OUT/'guide.html',o[OUT/'guide.html']+'<script>alert(1)</script>'),'ACTIVE_CONTENT')]:
  o=dict(outputs);change(o);negatives.append(rejects(label,lambda:links_check(o),expected))
 historical=json.loads((ROOT/'docs/ontology/pages-version-registry-v0.1.json').read_text())
 current=json.loads(outputs[DOC/'surface-bindings.json'])
 def routes(xs):
  rs=[x['route'] for x in xs]
  if len(rs)!=len(set(rs)):raise ValueError('DUPLICATE_ROUTE')
 routes(historical['versions']+[current]);negatives.append(rejects('duplicate version route',lambda:routes(historical['versions']+[current,current]),'DUPLICATE_ROUTE'))
 # New file content is accepted only when absent or identical: deliberately changed existing data rejects.
 check_existing(None,'new');check_existing('same','same');negatives.append(rejects('overwrite frozen route',lambda:check_existing('old','new'),'IMMUTABLE_OUTPUT_CHANGED'))
 frozen=json.loads(outputs[DOC/'surface-bindings.json']);read=lambda p:outputs[Path(p)].encode()
 verify_history(frozen,frozen,read)
 wrong=copy.deepcopy(frozen);wrong['source_commit']='0'*40
 negatives.append(rejects('history source commit changed',lambda:verify_history(frozen,wrong,read),'FROZEN_ROUTE_IDENTITY'))
 wrong=copy.deepcopy(frozen);wrong['output_sha256'].pop(next(iter(wrong['output_sha256'])))
 negatives.append(rejects('history output removed',lambda:verify_history(frozen,wrong,read),'FROZEN_ROUTE_BYTES'))
 negatives.append(rejects('history output changed',lambda:verify_history(frozen,frozen,lambda p:read(p)+b'x'),'FROZEN_ROUTE_BYTES'))
 result={'result':'PASS_OFFLINE_SOURCE_PROJECTION_ONLY','source_commit':current['source_commit'],'local_terms':116,'critical_terms':14,'fd_sections':10,'mutations_rejected':negatives,'mutation_count':len(negatives),'builder_sha256':digest((ROOT/'tools/build_rc4_documentation_surfaces.py').read_bytes()),'checker_sha256':digest(Path(__file__).read_bytes()),'output_sha256':current['output_sha256'],'live_wiki_parity':'NOT_ESTABLISHED','pages_deployment':'NOT_PERFORMED','release_acceptance':'NOT_ESTABLISHED'}
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();result=run();text=json.dumps(result,indent=2)+'\n';target=ROOT/DOC/'validation-results.json'
 if a.write:target.write_text(text)
 elif target.read_text()!=text:raise ValueError('VALIDATION_REPORT_DRIFT')
 print(text)
