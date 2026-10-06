#!/usr/bin/env python3
"""Reuse WebVOWL 1.1.7 with explicit bounded asserted projections and preset-only loading."""
import csv,json,re,shutil,hashlib
from pathlib import Path
from rdflib import Graph,URIRef,Literal
from rdflib.namespace import RDF,RDFS,OWL
from build_public_ontology_docs import ROOT,OUT,DOC,REF,MODULES,esc,sha
BASE=ROOT/'docs/ontology/generated/webvowl-viewer-candidate-v0.1'
DEST=OUT/'explorer'
def patch_function(text,name,body):
 pat=(r'function '+re.escape(name)+r'\s*\([^)]*\)\s*\{' if '.' not in name else re.escape(name)+r'\s*=\s*function\s*\([^)]*\)\s*\{')
 hits=list(re.finditer(pat,text));assert len(hits)==1,(name,len(hits));m=hits[0];end=text.find('\n\t  }',m.end());assert end>0,name
 return text[:m.end()]+'\n'+body+'\n\t  '+text[end+4:]
def build():
 if DEST.exists():shutil.rmtree(DEST) # This generator owns only its new documentation revision.
 DEST.mkdir(parents=True,exist_ok=True)
 for name in ['css','js','licenses']:shutil.copytree(BASE/name,DEST/name,dirs_exist_ok=True)
 shutil.copy2(BASE/'license.txt',DEST/'license.txt')
 shutil.copy2(ROOT/'ontology/vendor/GUFO-LICENSE',DEST/'licenses/GUFO-LICENSE.txt')
 g=Graph().parse(ROOT/'docs/formal/0.2.0-rc.4/asserted-closure.nt',format='nt');rows=list(csv.DictReader((ROOT/'docs/formal/0.2.0-rc.4/entity-inventory.csv').open()));by={r['iri']:r for r in rows}
 def label(iri):return next((str(x) for x in g.objects(URIRef(iri),RDFS.label)),iri.rsplit(':',1)[-1].rsplit('#',1)[-1])
 reports=[];names=['semrisk']+['semrisk-'+m for m in MODULES if m not in ['mappings','governance','pharma']];(DEST/'data').mkdir(exist_ok=True)
 for name in names:
  module=name.removeprefix('semrisk-') if name!='semrisk' else None
  selected=[r for r in rows if module is None or Path(r['source_path']).stem==module]
  classes={r['iri'] for r in selected if r['kind']=='class'};localclasses=set(classes);edges=[];omitted=[]
  for r in selected:
   if r['kind'] not in ['object_property','datatype_property']:continue
   p=URIRef(r['iri']);domains=list(g.objects(p,RDFS.domain));ranges=list(g.objects(p,RDFS.range))
   if len(domains)==len(ranges)==1 and isinstance(domains[0],URIRef) and isinstance(ranges[0],URIRef):
    a,b=str(domains[0]),str(ranges[0]);classes|={a,b};edges.append((r,a,b))
   else:omitted.append({'iri':r['iri'],'kind':r['kind'],'reason':'No unique asserted named domain/range pair; no invented endpoint.'})
  # Named superclass targets provide context only. Metatype rdf:type is never converted to subclass.
  supers=[]
  for iri in sorted(localclasses):
   for parent in sorted(str(x) for x in g.objects(URIRef(iri),RDFS.subClassOf) if isinstance(x,URIRef)):
    classes.add(parent);supers.append((iri,parent))
  ids={iri:str(i) for i,iri in enumerate(sorted(classes))};data={'_comment':'Bounded SemRisk asserted-source adapter; WebVOWL 1.1.7 renderer, not OWL2VOWL conversion or full OWL semantics.','header':{'languages':['en'],'baseIris':[],'iri':'urn:semrisk:documentation:rc4:'+name,'title':{'en':'SemRisk rc.4 '+(module or 'combined local declarations')},'description':{'en':'Only explicit named class hierarchy and properties with unique asserted endpoints are graphed. All 116 declarations and omitted semantics are available in the formal index.'}},'namespace':[],'class':[],'classAttribute':[],'property':[],'propertyAttribute':[]}
  for iri in sorted(classes):
   data['class'].append({'id':ids[iri],'type':'owl:Class'});attr={'id':ids[iri],'iri':iri,'baseIri':iri.rsplit(':',1)[0]+':','label':{'en':label(iri)},'instances':0}
   if iri not in localclasses:attr['attributes']=['external'];attr['label']['en']+=' (context reference)'
   comments=[str(x) for x in g.objects(URIRef(iri),RDFS.comment)]
   if comments:attr['comment']={'en':' '.join(comments)}
   data['classAttribute'].append(attr)
  for r,a,b in edges:
   n=str(len(ids)+len(data['property']));kind='owl:ObjectProperty' if r['kind']=='object_property' else 'owl:DatatypeProperty';data['property'].append({'id':n,'type':kind});data['propertyAttribute'].append({'id':n,'iri':r['iri'],'baseIri':r['iri'].rsplit(':',1)[0]+':','label':{'en':label(r['iri'])},'domain':ids[a],'range':ids[b],'attributes':['object' if r['kind']=='object_property' else 'datatype']})
  for a,b in supers:
   n=str(len(ids)+len(data['property']));data['property'].append({'id':n,'type':'rdfs:subClassOf'});data['propertyAttribute'].append({'id':n,'domain':ids[a],'range':ids[b]})
  raw=json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n';(DEST/'data'/f'{name}.json').write_text(raw)
  reports.append({'preset':name,'module':module or 'all','term_index_count':len(selected),'graph_local_classes':len(localclasses),'graph_explicit_property_iris':[x[0]['iri'] for x in edges],'graph_named_subclass_edges':len(supers),'graph_context_classes':len(classes-localclasses),'index_only_properties':omitted,'json_sha256':sha(raw.encode())})
 # Close every converter/upload network-capable implementation, not merely its UI.
 app=(BASE/'js/webvowl.app.js').read_text()
 blocked=['addFileDropEvents','setupConverterButtons','setupUploadButton','ontologyMenu.setIriText','getLoadingStatusOnceCallBacked','getLoadingStatusTimeLooped','callbackUpdateLoadingMessage','ontologyMenu.callbackLoad_Ontology_FromIRI','ontologyMenu.callbackLoad_Ontology_From_DirectInput','ontologyMenu.callbackLoad_JSON_FromURL','callbackLoadFromOntology','ontologyMenu.conversionFinished','loadingModule.from_JSON_URL','requestServerTimeStampForJSON_URL','loadingModule.requestServerTimeStampForDirectInput','loadingModule.from_IRI_URL','loadingModule.fromFileDrop','loadingModule.from_FileUpload','fallbackConversion','requestServerTimeStampForIRI_Converte','requestServerTimeStamp','loadingModule.directInput','loadingModule.loadFromOWL2VOWL','directInputModule.handleDirectUpload']
 for f in blocked:app=patch_function(app,f,'    return false; // Disabled in the read-only preset-only documentation bundle.')
 allowed=json.dumps(names)
 app=patch_function(app,'loadingModule.parseUrlAndLoadOntology','    var preset=location.hash.slice(1)||"semrisk";\n    if ('+allowed+'.indexOf(preset)===-1) { preset="semrisk"; }\n    graph.clearAllGraphData(); loadingModule.initializeLoader(false); ontologyIdentifierFromURL=preset;\n    loadingModule.from_presetOntology(preset);')
 app=patch_function(app,'loadPresetOntology','    if ('+allowed+'.indexOf(ontology)===-1) { return false; }\n    loadingWasSuccessFul=false;\n    d3.xhr("./data/"+ontology+".json", "application/json", function(error,request){\n      if(error){graph.handleOnLoadingError();loadingModule.setErrorMode();return;}\n      parseOntologyContent(request.responseText);\n    });')
 assert 'new XMLHttpRequest' not in app and 'new FormData' not in app
 assert app.count('d3.xhr(')==1,app.count('d3.xhr(')
 (DEST/'js/webvowl.app.js').write_text(app)
 core=(BASE/'js/webvowl.js').read_text();assert core.count('editMode = true,')==1;core=core.replace('editMode = true,','editMode = false,');core=patch_function(core,'graph.editorMode','    editMode = false; graph.options().setEditorModeForDefaultObject(false); return false; // Read-only internal and public state.');(DEST/'js/webvowl.js').write_text(core)
 page=(BASE/'index.html').read_text();start=page.index('        <aside id="semriskNotice"');end=page.index('        </aside>',start)+len('        </aside>')
 notice='<aside id="semriskNotice" role="note"><strong>SemRisk rc.4 · WebVOWL</strong><p>Interactive asserted overview, not OntoUML. Graphical readability is partial; zoom/pan or use the term index. Context references are labeled.</p><label for="semriskModuleSelect">Graph view</label><select id="semriskModuleSelect" aria-label="Choose ontology view">'+''.join('<option value="'+n+'">'+esc('All graph-supported declarations' if n=='semrisk' else n.removeprefix('semrisk-'))+'</option>' for n in names)+'<option value="index-governance">Governance (index only)</option><option value="index-pharma">Pharma (index only)</option><option value="index-mappings">Mappings (index only)</option></select><p><a href="../formal.html">Search all 116 terms</a> · <a href="../formal.html?module=mappings">Mappings metadata</a> · <a href="../diagrams.html">OntoUML views</a> · <a href="../index.html">Documentation</a></p><details><summary>Legend and omissions</summary><p>Circles denote classes; labeled edges denote asserted property signatures; subclass links show named asserted parents. External/context references are not local module definitions. Only 24 of 50 object properties have graphable endpoint pairs; all other properties remain in the complete term index. Enumeration, disjointness, anonymous expressions, metatypes and full imported semantics are not represented by graph layout.</p><p>WebVOWL MIT · D3 BSD · Lodash MIT. <a href="../sources.html#rights">gUFO source and CC BY 4.0 attribution</a>. <a href="licenses/GUFO-LICENSE.txt">Notice</a></p></details></aside>'
 page=page[:start]+notice+page[end:]
 page=page.replace('if ([...viewSelect.options].some(option => option.value === selected)) viewSelect.value = selected;', 'viewSelect.value = [...viewSelect.options].some(option => option.value === selected) ? selected : "semrisk";')
 page=page.replace('SemRisk P1-R2 | WebVOWL candidate','SemRisk rc.4 | Derived WebVOWL explorer')
 # Reuse existing selector via hashes rather than old rc.1 menu links.
 page=page.replace('viewSelect.addEventListener("change", () => document.getElementById(viewSelect.value).click());','viewSelect.addEventListener("change", () => { if(viewSelect.value.startsWith("index-")){location.href="../formal.html?module="+viewSelect.value.slice(6);}else{location.hash=viewSelect.value;} });')
 page=page.replace('<style>','<style>#semriskNotice{position:absolute;left:8rem;top:.6rem;z-index:1000;width:15rem;max-height:40vh;overflow:auto;background:white;color:#172b4d;padding:.6rem;border:1px solid #708595;font:14px/1.35 system-ui}#semriskNotice p{margin:.4rem 0}#semriskNotice summary{cursor:pointer}#c_select,#c_modes,#c_export,#m_select,#m_modes,#m_export,#editMode,#editorModeModuleCheckbox,#empty,#converter-option{display:none!important}')
 # No outbound loading endpoints; defense-in-depth CSP still permits only local data GET implementation.
 page=page.replace('<meta charset="utf-8" />','<meta charset="utf-8" /><meta http-equiv="Content-Security-Policy" content="default-src \'self\'; script-src \'self\' \'unsafe-inline\'; style-src \'self\' \'unsafe-inline\'; img-src \'self\' data:; connect-src \'self\'; object-src \'none\'; base-uri \'none\'; form-action \'none\'">')
 (DEST/'index.html').write_text(page)
 report={'source_commit':REF,'source_closure_sha256':sha((ROOT/'docs/formal/0.2.0-rc.4/asserted-closure.nt').read_bytes()),'all_declarations':116,'graph_policy':'Named asserted classes, named subclass edges and properties with one named asserted domain/range pair only. No entailment or inferred endpoint.','presets':reports,'index_only_kinds':['annotation_property','marker','named_individual'],'omitted_axiom_families':['owl:oneOf closure','owl:AllDifferent','disjointness visualization','anonymous restrictions and unions','metatype/punning semantics','inverse/property hierarchies and characteristics','full imported gUFO semantics'],'disabled_functions':blocked,'remaining_network_calls':'One allowlisted preset-only d3.xhr GET implementation','reader_participant_results':'NOT_EXECUTED','upstream_runtime':'WebVOWL1.1.7 at28e7dd9540622e8cb723dc000824b5eef5ae775f','original_runtime_manifest_sha256':sha((BASE/'manifest.json').read_bytes())}
 (DOC/'explorer-projection.json').write_text(json.dumps(report,indent=2)+'\n');(DEST/'projection.json').write_text(json.dumps(report,indent=2)+'\n')
 print('RC4 safe explorer built:',[(x['preset'],x['graph_local_classes'],len(x['graph_explicit_property_iris'])) for x in reports])
if __name__=='__main__':build()
