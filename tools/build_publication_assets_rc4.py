#!/usr/bin/env python3
"""Source-derived selected paper figure and version-explicit evidence table."""
import argparse,csv,hashlib,html,io,json,re
from pathlib import Path
from collections import Counter
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'publications/2026-icaea-sbu/visuals-rc4'
SOURCE='diagrams/ontouml/0.2.0-rc.4/view-spec.json'
BASE='3bbe7e8e3a51d609bf09d9e92462e8d444a5f49b'
SELECTED=['SR-CPT-'+str(n).zfill(3) for n in [1,6,7,11,13,33,34,35,36]]
EDGE_IDS=['SR-REL-001-view-1-1','SR-REL-002','SR-REL-003','SR-REL-013','SR-REL-015','SR-REL-016','SR-REL-030','SR-REL-031']
SOURCES=[SOURCE,'docs/formal/0.2.0-rc.4/source-manifest.json','diagrams/ontouml/0.2.0-rc.4/validation-results.json','diagrams/ontouml/0.2.0-rc.4/render-metrics.json','evaluation/exposure-scale/v0.2.0-rc.4/ci-evidence.json','evaluation/cq/issue52-cq-results-v1.0.csv','evaluation/parity/p49-parity-results-v1.0.csv','case/pharma/literature-pilot-v0.1.0/metrics.json','docs/execution/2026-10-04/scientific-contract.md','diagrams/ontouml/0.2.0-rc.4/concept-coverage.csv','diagrams/ontouml/0.2.0-rc.4/relation-coverage.csv']
NS='http://www.w3.org/2000/svg';ET.register_namespace('',NS)
def read(path):return json.loads((ROOT/path).read_text())
def sha(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def text(parent,x,y,value,size=8,weight='normal',anchor='middle',color='#15263b'):
 el=ET.SubElement(parent,'{'+NS+'}text',{'x':str(x),'y':str(y),'font-family':'DejaVu Sans, sans-serif','font-size':str(size),'font-weight':weight,'text-anchor':anchor,'fill':color});el.text=value;return el

def build():
 spec=read(SOURCE);assert all(n in spec['nodes'] for n in SELECTED) and all(e in spec['edges'] for e in EDGE_IDS)
 assert {spec['edges'][e][s] for e in EDGE_IDS for s in ['source','target']}==set(SELECTED)
 width=170/25.4*72;height=400
 svg=ET.Element('{'+NS+'}svg',{'width':'170mm','height':str(height/72*25.4)+'mm','viewBox':f'0 0 {width} {height}','role':'img','aria-labelledby':'fig-title fig-desc'})
 ET.SubElement(svg,'{'+NS+'}title',id='fig-title').text='SemRisk rc.4 selected conceptual distinctions'
 ET.SubElement(svg,'{'+NS+'}desc',id='fig-desc').text='Four source-derived panels show scenario/event, assessment/result, risk/record and risk state. Nine of 47 concepts and eight of 40 relation decisions are selected. This is not the full ontology.'
 ET.SubElement(svg,'{'+NS+'}rect',width='100%',height='100%',fill='white')
 text(svg,8,13,'SemRisk 0.2.0-rc.4 · selected conceptual distinctions',10,'bold','start')
 occurrences=[]
 def panel(x,y,title):
  g=ET.SubElement(svg,'{'+NS+'}g',transform=f'translate({x} {y})')
  ET.SubElement(g,'{'+NS+'}rect',x='0',y='0',width='232',height='174',rx='3',fill='#fafbfd',stroke='#d9e0e8',attrib={'stroke-width':'0.5'})
  text(g,8,14,title,9,'bold','start');return g
 def node(g,n,x,y,w=100,h=35):
  id='SR-CPT-'+str(n).zfill(3);d=spec['nodes'][id];occurrences.append(id)
  group=ET.SubElement(g,'{'+NS+'}g',{'data-concept-id':id})
  ET.SubElement(group,'{'+NS+'}rect',x=str(x),y=str(y),width=str(w),height=str(h),fill='#fff1d3' if d['status']=='pattern boundary' else '#eaf2f8',stroke='#536779',attrib={'stroke-width':'0.7'})
  text(group,x+w/2,y+10,'«'+d['stereotype']+'»' if d['stereotype'] else 'PATTERN BOUNDARY',8)
  words=d['label'].split();lines=[];current=''
  for word in words:
   if len(current+' '+word)>20 and current:lines.append(current);current=word
   else:current=(current+' '+word).strip()
  lines.append(current)
  for i,line in enumerate(lines):text(group,x+w/2,y+21+i*9,line,8,'bold')
 def edge(g,id,points,lx,ly,lines=None,cards=None):
  e=spec['edges'][id];assert e['kind']=='association' and e['source_cardinality']==e['target_cardinality']=='0..*'
  eg=ET.SubElement(g,'{'+NS+'}g',{'data-edge-id':id})
  ET.SubElement(eg,'{'+NS+'}polyline',points=' '.join(f'{x},{y}' for x,y in points),fill='none',stroke='#536779',attrib={'stroke-width':'0.7'})
  lines=lines or [e['label']]
  assert ''.join(lines)==e['label']
  label_width=max(len(line) for line in lines)*4.4+4
  ET.SubElement(eg,'{'+NS+'}rect',x=str(lx-label_width/2),y=str(ly-7),width=str(label_width),height=str(len(lines)*9),fill='#fafbfd')
  for i,line in enumerate(lines):text(eg,lx,ly+i*9,line,8)
  if cards is None:
   a,b=points[0],points[-1];cards=[(a[0]+12,a[1]+(10 if points[1][1]>a[1] else -3)),(b[0]+12,b[1]+(-3 if points[-2][1]<b[1] else 10))]
  for x,y in cards:text(eg,x,y,'0..*',8)
 a=panel(5,25,'A · Scenario and occurrence')
 for n,y in [(34,25),(6,79),(7,133)]:node(a,n,66,y)
 edge(a,'SR-REL-002',[(116,60),(116,79)],193,65,['describes','Scenario'],cards=[(103,70),(130,76)])
 edge(a,'SR-REL-003',[(116,114),(116,133)],172,125,cards=[(103,124),(130,130)])
 b=panel(245,25,'B · Assessment and issued result')
 node(b,11,5,55);node(b,13,127,55);node(b,1,66,134)
 edge(b,'SR-REL-015',[(55,55),(55,42),(177,42),(177,55)],116,30,['produces','AssessmentResult'])
 edge(b,'SR-REL-013',[(55,90),(35,112),(66,150)],56,110,['performed','AssessmentOf'],cards=[(70,100),(51,153)])
 edge(b,'SR-REL-016',[(177,90),(197,112),(166,150)],177,110,['assessmentResult','Concerns'],cards=[(164,100),(180,153)])
 c=panel(5,207,'C · Record and workflow snapshot')
 node(c,33,66,29);node(c,1,5,131);node(c,36,127,131)
 edge(c,'SR-REL-001-view-1-1',[(90,64),(55,131)],53,91,['concernsRisk'])
 edge(c,'SR-REL-030',[(142,64),(177,131)],178,91,['hasWorkflow','State'])
 d=panel(245,207,'D · Risk state')
 node(d,1,66,32);node(d,35,66,118)
 edge(d,'SR-REL-031',[(116,67),(116,118)],165,92,['hasRiskState'])
 text(d,116,163,'Workflow value ≠ risk state',8)
 text(svg,8,392,'9/47 concepts · 8/40 relation decisions · full model and limits in companion',8,'normal','start')
 svg_text=ET.tostring(svg,encoding='unicode')+'\n'
 inventory=read(SOURCES[1]);formal=read(SOURCES[4]);pilot=read(SOURCES[7]);cq=Counter(r['state'] for r in csv.DictReader((ROOT/SOURCES[5]).open()));parity=list(csv.DictReader((ROOT/SOURCES[6]).open()))
 concept_rows=list(csv.DictReader((ROOT/SOURCES[9]).open()));relation_rows=list(csv.DictReader((ROOT/SOURCES[10]).open()))
 assert len(concept_rows)==47 and len(relation_rows)==40
 rows=[
 {'id':'T01','target':'rc.4 source inventory','unit':'locally declared terms','result':str(inventory['declared_entity_count'])+' terms; 47 concept rows; 40 relation rows','limit':'Counts are not semantic quality or validation','claim':'SR-CL01;SR-CL08','source':SOURCES[1]},
 {'id':'T02','target':'rc.4 diagram candidate','unit':'concept / relation coverage','result':f'{len(concept_rows)}/47 concepts; {len(relation_rows)}/40 relation decisions','limit':'Complete atlas fails 170 mm readability; no native-editor/full antipattern pass','claim':'SR-CL01','source':SOURCES[2]},
 {'id':'T03','target':'rc.4 synthetic tests at '+formal['tested_candidate_commit'][:7],'unit':'behavioral checks / formal probes','result':f"{formal['actual_results']['behavioral']['passed']}/{formal['actual_results']['behavioral']['total']} checks ({formal['actual_results']['behavioral']['negative_cases']} negatives); 4 entailments; 2 countermodels; 2 contradictions rejected",'limit':'Bounded verification, not domain-expert validation or complete conformance','claim':'SR-CL08','source':SOURCES[4]},
 {'id':'T04','target':'literature pilot v0.1.0 / rc.4','unit':'source-local statements / studies','result':f"{pilot['statement_count']} statements / {pilot['source_count']} studies: {pilot['mapping_status']['partial']} partial, {pilot['mapping_status']['ambiguous']} ambiguous, {pilot['mapping_status']['unmapped']} unmapped",'limit':'Applicability only; not observed incidents; zero independent validation sources','claim':'SR-CL05;SR-CL06','source':SOURCES[7]},
 {'id':'T05','target':'historical P1-R2 / 0.1.0-rc.1','unit':'original competency questions','result':f"{sum(cq.values())} CQs: {cq['executable']} executable, {cq['partially_executable']} partial, {cq['conceptual_only']} conceptual, {cq['deferred']} deferred",'limit':'Preserved classification; not a fresh full rc.4 rerun','claim':'SR-CL08','source':SOURCES[5]},
 {'id':'T06','target':'historical frozen P49 tasks','unit':'predeclared task answer sets','result':f"{sum(r['actual_class']=='equivalent_for_task' for r in parity)}/{len(parity)} equivalent for task",'limit':'No new SQL execution or complete rc.4 helper parity; #125 deferred','claim':'SR-CL04','source':SOURCES[6]}
 ]
 stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
 table=['# Candidate evidence table: targets and units remain separate','','Source baseline: `'+BASE+'`. No overall quality score. Claims refer to the calibrated scientific contract.','','| Target | Unit | Observed result | Claim limit |','| --- | --- | --- | --- |']
 table += ['| '+r['target']+' | '+r['unit']+' | '+r['result']+' | '+r['limit']+' |' for r in rows]
 table += ['','The full [machine-readable ledger](evidence-table.csv) preserves claim IDs and exact source paths. Final manuscript table placement, release binding and reader review remain open. Historical source ages and source-role limitations remain in the pilot README.']
 manifest={'baseline_commit':BASE,'candidate':'0.2.0-rc.4','figure_scope':'SELECTED_PROJECTION_NOT_COMPLETE_MODEL','selected_concepts':SELECTED,'selected_edges':EDGE_IDS,'selected_concept_count':len(SELECTED),'concept_denominator':47,'selected_relation_count':len(EDGE_IDS),'relation_denominator':40,'omitted_concepts_from_figure':38,'omitted_relations_from_figure':32,'concept_occurrences':occurrences,'print_width_mm':170,'print_height_mm':height/72*25.4,'minimum_font_pt':8,'minimum_allowed_font_pt':7,'full_atlas_print_gate':'FAIL_READABILITY_RETAINED','sources':{p:sha(p) for p in SOURCES},'figure_sha256':hashlib.sha256(svg_text.encode()).hexdigest(),'table_rows':len(rows),'limits':['No native editor roundtrip','No full antipattern certification','No full atlas readability claim','No scholarly release or final manuscript approval']}
 return {'figure1-selected-rc4.svg':svg_text,'evidence-table.csv':stream.getvalue(),'evidence-table.md':'\n'.join(table)+'\n','manifest.json':json.dumps(manifest,indent=2)+'\n'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--pdf',action='store_true');a=p.parse_args();OUT.mkdir(parents=True,exist_ok=True)
 for name,value in build().items():
  path=OUT/name
  if a.check:
   if not path.exists() or path.read_text()!=value:raise SystemExit('PUBLICATION_ASSET_DRIFT: '+name)
  else:path.write_text(value)
 if a.pdf:
  import cairosvg
  from pypdf import PdfReader,PdfWriter
  raw=cairosvg.svg2pdf(url=str(OUT/'figure1-selected-rc4.svg'))
  reader=PdfReader(io.BytesIO(raw));writer=PdfWriter();writer.add_page(reader.pages[0]);writer.add_metadata({'/Title':'SemRisk rc.4 selected conceptual distinctions','/Producer':'CairoSVG 2.8.2 / pypdf 6.1.3'})
  buf=io.BytesIO();writer.write(buf);pdf=OUT/'figure1-selected-rc4.pdf'
  if a.check:
   if not pdf.exists() or pdf.read_bytes()!=buf.getvalue():raise SystemExit('PUBLICATION_PDF_DRIFT')
  else:pdf.write_bytes(buf.getvalue())
 print('RC4_PUBLICATION_ASSETS_GENERATED: selected 9/47 concepts; 8/40 relations; six version-scoped table rows')
if __name__=='__main__':main()
