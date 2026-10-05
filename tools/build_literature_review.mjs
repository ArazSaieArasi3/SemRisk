import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const [dataDir,outDir]=process.argv.slice(2);
if(!dataDir||!outDir)throw Error('Usage: build_literature_review.mjs DATA_DIRECTORY OUTPUT_DIRECTORY');
const get=async name=>JSON.parse(await fs.readFile(path.join(dataDir,name),'utf8'));
const rows=await get('statements.json'), maps=await get('mappings.json'), sources=await get('sources.json');
const wb=Workbook.create();
const sheet=wb.worksheets.add('Statements');
const values=[['ID','Category','Source paraphrase','Mapping','Source and locator','Mapping limits']];
for(const r of rows){const m=maps.find(x=>x.statement_id===r.statement_id);const s=sources.find(x=>x.source_id===r.source_id);values.push([r.statement_id,r.enterprise_context,r.statement_paraphrase,m.mapping_status,`${r.source_id} | https://doi.org/${s.doi}\n${r.source_locator}`,m.mapping_rationale]);}
sheet.getRange(`A1:F${values.length}`).values=values;
const ss=wb.worksheets.add('Sources');
const sv=[['ID','Publication','Evidence role','Context','Rights','Limitations']];
for(const s of sources)sv.push([s.source_id,`${s.authors} (${s.year}). ${s.title}.\nhttps://doi.org/${s.doi}`,s.source_role+'; applicability only',s.study_context,s.rights_note,s.limitations]);
ss.getRange(`A1:F${sv.length}`).values=sv;
for(const [sh,n,widths] of [[sheet,values.length,[14,17,57,16,61,62]],[ss,sv.length,[14,65,23,37,44,64]]]){
 const all=sh.getRange(`A1:F${n}`);all.format.font={name:'Arial',size:11};all.format.wrapText=true;all.format.verticalAlignment='top';
 sh.getRange('A1:F1').format.fill='#17324D';sh.getRange('A1:F1').format.font={name:'Arial',size:11,bold:true,color:'#FFFFFF'};
 sh.getRange('A1:F1').format.rowHeight=28;
 widths.forEach((w,i)=>{sh.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${n}`).format.columnWidth=w;});
 sh.getRange(`A2:F${n}`).format.rowHeight=sh===sheet?92:150;
 sh.freezePanes.freezeRows(1);sh.showGridLines=false;
 sh.tables.add(`A1:F${n}`,true,sh===sheet?'StatementReview':'PublicationSources');
}
wb.recalculate();
await fs.mkdir(outDir,{recursive:true});
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20},summary:'Review workbook error scan'});
console.log(errors.ndjson);
for(const [name,range,file] of [['Statements','A1:F9','statements-1'],['Statements','A10:F17','statements-2'],['Statements','A18:F25','statements-3'],['Sources','A1:F7','sources']]){
 const img=await wb.render({sheetName:name,range,scale:1,format:'png'});await fs.writeFile(path.join(outDir,file+'.png'),new Uint8Array(await img.arrayBuffer()));
}
const out=await SpreadsheetFile.exportXlsx(wb);await out.save(path.join(outDir,'pharma-literature-pilot-v0.1.0.xlsx'));
console.log(JSON.stringify({statements:rows.length,sources:sources.length,sheets:2,exported:true}));
