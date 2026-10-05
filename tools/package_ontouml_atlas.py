#!/usr/bin/env python3
"""Bind exact Graphviz geometry into OntoUML JSON, draw.io and vector PDF/SVG."""
import json,re,copy,math,hashlib,html
from pathlib import Path
from xml.etree import ElementTree as ET
from io import BytesIO
import cairosvg
from pypdf import PdfReader,PdfWriter
from jsonschema import Draft202012Validator
from build_ontouml_atlas import ROOT,OUT,DATE,named
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
def bare(id,type,**kw):return dict(id=id,type=type,created=DATE,modified=DATE,**kw)
def main():
 spec=json.loads((OUT/'view-spec.json').read_text());project=json.loads((OUT/'model-base.json').read_text());elems=project['elements'];base_ids={x['id'] for x in elems};drawio=ET.Element('mxfile',host='app.diagrams.net',version='24.7.17');writer=PdfWriter();master=ET.Element('{'+NS+'}svg',width='1800',height=str(740*math.ceil(len(spec['views'])/2)+120),viewBox=f"0 0 1800 {740*math.ceil(len(spec['views'])/2)+120}")
 ET.SubElement(master,'{'+NS+'}rect',width='100%',height='100%',fill='white')
 def txt(parent,x,y,text,size=18,weight='normal',fill='#14283e'):
  e=ET.SubElement(parent,'{'+NS+'}text',x=str(x),y=str(y),attrib={'font-family':'Arial, Helvetica, sans-serif','font-size':str(size),'font-weight':weight,'fill':fill});e.text=text;return e
 txt(master,30,38,'SemRisk 0.2.0-rc.3 | Complete candidate diagram atlas',26,'bold')
 txt(master,30,68,'47 concepts | 38 registered relations | 11 helper classes | Explicit pattern and external boundaries',17)
 metrics=[]
 for ix,v in enumerate(spec['views']):
  layout=json.loads((OUT/'views'/f"{v['id']}.layout.json").read_text());bb=list(map(float,layout['bb'].split(',')));height=bb[3];did='D-'+v['id'];views=[];drawdiag=ET.SubElement(drawio,'diagram',id=did,name=v['title']);mx=ET.SubElement(drawdiag,'mxGraphModel',grid='1',gridSize='10',page='1',pageWidth='1169',pageHeight='827');rr=ET.SubElement(mx,'root');ET.SubElement(rr,'mxCell',id='0');ET.SubElement(rr,'mxCell',id='1',parent='0');obj={o['_gvid']:o for o in layout.get('objects',[])}
  for o in layout.get('objects',[]):
   if o.get('name') not in spec['nodes']:continue
   id=o['name'];n=spec['nodes'][id];x,y=map(float,o['pos'].split(','));w,h=float(o['width'])*72,float(o['height'])*72;x=x-w/2+24;y=height-y-h/2+24;vid=did+'-'+id;rid=vid+'-rect'
   elems += [bare(rid,'Rectangle',topLeft={'x':round(x),'y':round(y)},width=math.ceil(w),height=math.ceil(h)),bare(vid,'ClassView',isViewOf=id,rectangle=rid)];views.append(vid)
   st='«'+n['stereotype']+'»' if n['stereotype'] else n['status'].upper();value=html.escape(st)+'<br><b>'+html.escape(n['label'])+'</b>'
   if n['attributes']:value+='<hr>'+'<br>'.join(map(html.escape,n['attributes']))
   color='#e7f2fc' if n['status'] in ['implemented','external category'] else '#e8f5f0' if n['status']=='profile helper' else '#fff0cf' if n['status'] in ['pattern boundary','unclassified OWL helper'] else '#f0e9fb'
   cell=ET.SubElement(rr,'mxCell',id=vid,value=value,style=f'rounded=0;whiteSpace=wrap;html=1;fillColor={color};strokeColor=#40546c;fontSize=14;',vertex='1',parent='1');ET.SubElement(cell,'mxGeometry',x=str(round(x)),y=str(round(y)),width=str(math.ceil(w)),height=str(math.ceil(h)),attrib={'as':'geometry'})
  for le in layout.get('edges',[]):
   eid=le.get('id')
   if not eid:continue # purely invisible grid layout constraints are not ontology edges
   e=spec['edges'][eid];vid=did+'-'+eid;pathid=vid+'-path';points=[]
   for token in le['pos'].split():
    a=token.split(',')
    if len(a)==2:
     x,y=map(float,a);points.append(dict(x=round(x+24),y=round(height-y+24)))
   if len(points)<2:raise ValueError('Missing edge geometry '+eid)
   source=did+'-'+e['source'];target=did+'-'+e['target']
   if e['kind']=='metadata':
    x,y=map(float,le.get('lp','0,0').split(','));rid=vid+'-text';elems += [bare(rid,'Text',topLeft={'x':round(x+24),'y':round(height-y+24)},width=240,height=50),bare(vid,'NoteView',isViewOf=eid,text=rid)];views.append(vid)
    for end in ['source','target']:
     aid=eid+'-anchor-'+end
     if aid not in base_ids:
      a=named(aid,'Anchor','metadata annotation');a.update(note=eid,element=e[end]);elems.append(a);base_ids.add(aid)
     av=vid+'-'+end;pid=av+'-path';ep=points[0] if end=='source' else points[-1];elems += [bare(pid,'Path',points=[{'x':round(x+24),'y':round(height-y+24)},ep]),bare(av,'AnchorView',isViewOf=aid,sourceView=vid,targetView=did+'-'+e[end],path=pid)];views.append(av)
   else:
    elems += [bare(pathid,'Path',points=points),bare(vid,'GeneralizationView' if e['kind']=='generalization' else 'BinaryRelationView',isViewOf=eid,sourceView=source,targetView=target,path=pathid)];views.append(vid)
   label='' if e['kind']=='generalization' else (('«'+e['stereotype']+'» ' if e['stereotype'] else '')+e['label']+(' [metadata]' if e['kind']=='metadata' else ''))
   style='edgeStyle=none;html=1;rounded=0;strokeColor=#526477;fontSize=11;'
   style+='endArrow=block;endFill=0;' if e['kind']=='generalization' else 'endArrow=open;dashed=1;' if e['kind']=='metadata' else 'endArrow=none;'
   cell=ET.SubElement(rr,'mxCell',id=vid+'-edge',value=label,style=style,edge='1',parent='1',source=source,target=target);geo=ET.SubElement(cell,'mxGeometry',relative='1',attrib={'as':'geometry'});arr=ET.SubElement(geo,'Array',attrib={'as':'points'})
   for p in points:ET.SubElement(arr,'mxPoint',x=str(p['x']),y=str(p['y']))
   if e['kind']=='association':
    for end,x in [('source',-.88),('target',.88)]:
     ce=ET.SubElement(rr,'mxCell',id=vid+'-'+end+'-label',value=e[end+'_cardinality'],style='edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];',vertex='1',connectable='0',parent=vid+'-edge');ET.SubElement(ce,'mxGeometry',x=str(x),y='-10',relative='1',attrib={'as':'geometry'})
  d=named(did,'Diagram',v['title'],v['note']);d.update(owner='root-package',views=views);elems.append(d)
  svg=ET.parse(OUT/'views'/f"{v['id']}.svg").getroot();vw=list(map(float,svg.attrib['viewBox'].split()));sw,sh=vw[2],vw[3];svg.set('width',str(sw));svg.set('height',str(sh))
  # Full-page review layout at A3 landscape in PDF points.
  pw,ph=1190.55,841.89;scale=min((pw-90)/sw,(ph-200)/sh)
  page=ET.Element('{'+NS+'}svg',width=f'{pw}pt',height=f'{ph}pt',viewBox=f'0 0 {pw} {ph}');ET.SubElement(page,'{'+NS+'}rect',width='100%',height='100%',fill='white')
  txt(page,45,45,f"{ix+1:02}   {v['title']}",24,'bold');txt(page,45,75,'SemRisk 0.2.0-rc.3 | OntoUML-based view with explicit scope boundaries',13)
  sub=ET.SubElement(page,'{'+NS+'}g',transform=f'translate({(pw-sw*scale)/2} 110) scale({scale})');sub.append(copy.deepcopy(svg))
  import textwrap
  for j,line in enumerate(textwrap.wrap(v['note'],145)):txt(page,45,ph-62+j*16,line,12)
  txt(page,45,ph-20,'Blue: implemented | Green: profile helper | Amber: pattern/unclassified | Violet: external/planned',11)
  page_bytes=ET.tostring(page);(OUT/'views'/f"{v['id']}-review.svg").write_bytes(page_bytes)
  pdf=PdfReader(BytesIO(cairosvg.svg2pdf(bytestring=page_bytes)));writer.add_page(pdf.pages[0])
  # Master sheet duplicates the same SVG views; no alternative semantic source.
  x=(ix%2)*900;y=110+(ix//2)*740;txt(master,x+25,y+28,f"{ix+1:02}   {v['title']}",20,'bold');ms=min(850/sw,625/sh);gg=ET.SubElement(master,'{'+NS+'}g',transform=f'translate({x+(900-sw*ms)/2} {y+52}) scale({ms})');gg.append(copy.deepcopy(svg));txt(master,x+25,y+710,'See the PDF atlas for scope and multiplicity notes.',13)
  fonts=[float(n.attrib['font-size']) for n in svg.iter() if 'font-size' in n.attrib];minimum=min(fonts) if fonts else 10
  metrics.append(dict(view=v['id'],source_width=sw,source_height=sh,min_font_pt_at_A3=round(minimum*scale,2),min_font_pt_at_170mm_width=round(minimum*(170/25.4*72)/sw,2),class_nodes=len(v['nodes']),model_edges=len(v['edges'])))
 # Validate project and each element through the upstream entry point.
 schema=json.loads((OUT/'vendor/ontouml-schema.json').read_text());validator=Draft202012Validator(schema);validator.validate(project)
 for e in elems:
  ev=validator if e['type']!='Diagram' else Draft202012Validator({'$defs':schema['$defs'],'allOf':[{'$ref':'#/$defs/Diagram'},schema['$defs']['NamedElement']['allOf'][0],schema['$defs']['OntoumlElement']['allOf'][0]]})
  errors=list(ev.iter_errors(e))
  if errors:raise ValueError(e['id']+': '+errors[0].message)
 (OUT/'SemRisk-rc3.ontouml.json').write_text(json.dumps(project,indent=2)+'\n');ET.ElementTree(drawio).write(OUT/'SemRisk-rc3.drawio',encoding='utf-8',xml_declaration=True)
 ET.ElementTree(master).write(OUT/'SemRisk-rc3-complete.svg',encoding='utf-8',xml_declaration=True)
 with (OUT/'SemRisk-rc3-review-atlas.pdf').open('wb') as f:writer.write(f)
 # One honest IEEE-size proof: full master is unsuitable at this width, so this is explicitly a scoped scenario panel.
 v=spec['views'][0];svg=ET.parse(OUT/'views'/f"{v['id']}.svg").getroot();width=170/25.4*72;sw=float(svg.attrib['viewBox'].split()[2]);height=float(svg.attrib['viewBox'].split()[3])*width/sw;svg.set('width',str(width)+'pt');svg.set('height',str(height)+'pt');(OUT/'SemRisk-rc3-paper-panel.svg').write_bytes(ET.tostring(svg));cairosvg.svg2pdf(bytestring=ET.tostring(svg),write_to=str(OUT/'SemRisk-rc3-paper-panel.pdf'))
 m=dict(schema_id=schema['$id'],schema_project='PASS',schema_elements=len(elems),view_metrics=metrics,full_master_IEEE_170mm='FAIL_READABILITY',paper_panel='Scoped scenario panel only; not the full ontology',minimum_review_font_pt=min(x['min_font_pt_at_A3'] for x in metrics),native_visual_paradigm_roundtrip='NOT_EXECUTED')
 (OUT/'render-metrics.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps({k:v for k,v in m.items() if k!='view_metrics'},indent=2))
if __name__=='__main__':main()
