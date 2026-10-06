#!/usr/bin/env python3
"""Bounded source/print QA. Does not certify full OntoUML or final manuscript."""
import copy,json,re,math
from pathlib import Path
from xml.etree import ElementTree as ET
from pypdf import PdfReader
from pypdf.generic import ContentStream
from build_publication_assets_rc4 import ROOT,OUT,SOURCE,SOURCES,NS,SELECTED,EDGE_IDS,build,read,sha

def verify(svg,manifest,spec):
 root=ET.fromstring(svg)
 width=float(root.attrib['width'].removesuffix('mm'));coord=float(root.attrib['viewBox'].split()[2])
 fonts=[float(e.attrib['font-size'])*width/25.4*72/coord for e in root.iter() if 'font-size' in e.attrib]
 if min(fonts)<7:raise ValueError('PRINT_FONT_TOO_SMALL')
 nodes=[e for e in root.iter() if 'data-concept-id' in e.attrib];edges=[e for e in root.iter() if 'data-edge-id' in e.attrib]
 if {n.attrib['data-concept-id'] for n in nodes}!=set(SELECTED):raise ValueError('SELECTED_NODE_COVERAGE')
 if {e.attrib['data-edge-id'] for e in edges}!=set(EDGE_IDS) or len(edges)!=len(EDGE_IDS):raise ValueError('SELECTED_EDGE_COVERAGE')
 for node in nodes:
  d=spec['nodes'][node.attrib['data-concept-id']];texts=[e.text for e in node.iter('{'+NS+'}text')]
  if texts[0]!=('«'+d['stereotype']+'»' if d['stereotype'] else 'PATTERN BOUNDARY'):raise ValueError('STEREOTYPE_DRIFT')
  if ' '.join(texts[1:])!=d['label']:raise ValueError('NODE_LABEL_DRIFT')
 for edge in edges:
  d=spec['edges'][edge.attrib['data-edge-id']];texts=[e.text for e in edge.iter('{'+NS+'}text')]
  if texts[-2:]!=[d['source_cardinality'],d['target_cardinality']]:raise ValueError('CARDINALITY_DRIFT')
  if ''.join(texts[:-2])!=d['label']:raise ValueError('RELATION_LABEL_DRIFT')
  if any('marker-end' in e.attrib or 'marker-start' in e.attrib for e in edge.iter()):raise ValueError('INVENTED_DIRECTION')
  panel=next(p for p in root.iter() if edge in list(p))
  line=next(edge.iter('{'+NS+'}polyline'));points=[tuple(map(float,p.split(','))) for p in line.attrib['points'].split()]
  for end,point in [('source',points[0]),('target',points[-1])]:
   node=next(n for n in panel if n.attrib.get('data-concept-id')==d[end])
   rect=next(node.iter('{'+NS+'}rect'));x,y,w,h=[float(rect.attrib[k]) for k in ['x','y','width','height']];px,py=point
   inside=x-1e-6<=px<=x+w+1e-6 and y-1e-6<=py<=y+h+1e-6
   boundary=min(abs(px-x),abs(px-x-w),abs(py-y),abs(py-y-h))<1e-6
   if not inside or not boundary:raise ValueError('ENDPOINT_ATTACHMENT_DRIFT')

 if manifest['sources']!={p:sha(p) for p in SOURCES}:raise ValueError('SOURCE_HASH_DRIFT')
 if manifest['full_atlas_print_gate']!='FAIL_READABILITY_RETAINED':raise ValueError('FULL_ATLAS_OVERCLAIM')
 return min(fonts)

def run():
 outputs=build()
 for name,value in outputs.items():
  if (OUT/name).read_text()!=value:raise ValueError('GENERATED_DRIFT: '+name)
 svg=outputs['figure1-selected-rc4.svg'];manifest=json.loads(outputs['manifest.json']);spec=read(SOURCE);minimum=verify(svg,manifest,spec)
 cases=['missing_node','changed_stereotype','changed_cardinality','invented_arrow','stale_source','shrunk_print','miswired_endpoint']
 expected=['SELECTED_NODE_COVERAGE','STEREOTYPE_DRIFT','CARDINALITY_DRIFT','INVENTED_DIRECTION','SOURCE_HASH_DRIFT','PRINT_FONT_TOO_SMALL','ENDPOINT_ATTACHMENT_DRIFT']
 for name,marker in zip(cases,expected):
  root=ET.fromstring(svg);m=copy.deepcopy(manifest)
  if name=='missing_node':
   for e in root.iter():
    for child in list(e):
     if child.attrib.get('data-concept-id')==SELECTED[1]:e.remove(child)
  elif name=='changed_stereotype':
   n=next(e for e in root.iter() if 'data-concept-id' in e.attrib);next(n.iter('{'+NS+'}text')).text='«kind»'
  elif name=='changed_cardinality':
   e=next(e for e in root.iter() if 'data-edge-id' in e.attrib);list(e.iter('{'+NS+'}text'))[-1].text='1'
  elif name=='invented_arrow':next(e for e in root.iter() if e.tag=='{'+NS+'}polyline').set('marker-end','url(#arrow)')
  elif name=='stale_source':m['sources'][SOURCE]='0'*64
  elif name=='shrunk_print':root.set('width','85mm')
  elif name=='miswired_endpoint':
   line=next(e for e in root.iter() if e.tag=='{'+NS+'}polyline');line.set('points','116,60 116,168')
  try:verify(ET.tostring(root,encoding='unicode'),m,spec)
  except ValueError as exc:
   if marker not in str(exc):raise
  else:raise ValueError('NEGATIVE_ACCEPTED: '+name)
 pdf=PdfReader(OUT/'figure1-selected-rc4.pdf');assert len(pdf.pages)==1
 page=pdf.pages[0];assert abs(float(page.mediabox.width)-170/25.4*72)<.01 and abs(float(page.mediabox.height)-400)<.01
 text=' '.join(page.extract_text().split())
 for n in SELECTED:assert spec['nodes'][n]['label'] in text,spec['nodes'][n]['label']
 font_sizes=[]
 def font_probe(value,cm,tm,font,size):
  if value.strip():font_sizes.append(float(size)*math.hypot(tm[2]*cm[0]+tm[3]*cm[2],tm[2]*cm[1]+tm[3]*cm[3]))
 page.extract_text(visitor_text=font_probe)
 assert min(font_sizes)>=7
 print(json.dumps({'result':'PASS_SELECTED_PUBLICATION_ASSETS','concepts':'9/47','relations':'8/40','source_files':len(SOURCES),'table_rows':6,'negative_controls_rejected':cases,'svg_min_print_font_pt':round(minimum,3),'pdf_min_effective_font_pt':min(font_sizes),'pdf_width_mm':round(float(page.mediabox.width)/72*25.4,3),'pdf_height_mm':round(float(page.mediabox.height)/72*25.4,3),'full_atlas_readability':'FAIL_RETAINED','native_editor':'NOT_EXECUTED','final_manuscript':'NOT_INTEGRATED'},indent=2))
if __name__=='__main__':run()
