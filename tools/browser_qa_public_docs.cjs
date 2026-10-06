const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {spawn}=require('node:child_process');const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..'),art=path.join(root,'public-docs-browser-artifacts');fs.mkdirSync(art,{recursive:true});
const manifest=JSON.parse(fs.readFileSync(path.join(root,'docs/pages/2026-10-06/deployment-manifest.json'))),relative='ontology/0.2.0-rc.4/docs-20261006/';
const base=process.env.LIVE_BASE||'http://127.0.0.1:18768/';let server;
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
async function ready(){for(let i=0;i<50;i++){try{if((await fetch(base)).ok)return;}catch{}await new Promise(r=>setTimeout(r,200));}throw Error('server not ready');}
async function main(){
 if(!process.env.LIVE_BASE)server=spawn('python3',['-m','http.server','18768','--bind','127.0.0.1','--directory',path.join(root,'public-docs-stage')],{stdio:'ignore'});
 await ready();
 const bytes=[];for(const [p,hash] of Object.entries(manifest.files)){const r=await fetch(base+p);assert.equal(r.status,200,p);const b=Buffer.from(await r.arrayBuffer());assert.equal(digest(b),hash,'published byte mismatch '+p);bytes.push(p);}
 const browser=await chromium.launch({headless:true});const report={surface:process.env.LIVE_BASE?'LIVE_PUBLISHED_BYTES':'LOCAL_CI_CANDIDATE',base,exact_files:bytes.length,viewports:[],reader_participant_results:'NOT_EXECUTED'};
 try{for(const [name,viewport] of [['desktop',{width:1440,height:1000}],['mobile',{width:390,height:844}]]){
  const page=await browser.newPage({viewport}),errors=[],badRequests=[],badResponses=[];
  page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{const u=new URL(r.url());if(r.method()!=='GET'||u.origin!==new URL(base).origin||/\/(convert|directInput|read|serverTimeStamp|loadingStatus|conversionDone)(?:\?|$)/.test(u.pathname+u.search))badRequests.push(r.method()+' '+r.url());});page.on('response',r=>{if(r.status()>=400)badResponses.push(r.status()+' '+r.url());});
  for(const file of ['index.html','catalog.html','relations.html','formal.html','guide.html','diagrams.html','tutorial.html','sources.html']){
   await page.goto(base+relative+file,{waitUntil:'networkidle'});assert(await page.locator('h1').count());
   const fits=await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2);if(!fits){await page.screenshot({path:path.join(art,`${name}-${file}-overflow.png`),fullPage:false});const offenders=await page.locator('body *').evaluateAll(es=>es.map(e=>({tag:e.tagName,id:e.id,className:typeof e.className==='string'?e.className:'',left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right,width:e.getBoundingClientRect().width})).filter(e=>e.right>innerWidth+2||e.left<0));fs.writeFileSync(path.join(art,`${name}-${file}-overflow.json`),JSON.stringify(offenders,null,2));}assert(fits,'overflow '+name+' '+file);
   const imageCount=await page.locator('img').count();if(imageCount)assert(await page.locator('img').evaluateAll(a=>a.every(x=>x.complete&&x.naturalWidth>0)));
   if(file==='catalog.html'){await page.locator('#query').fill('SR-CPT-001');assert.equal(await page.locator('.concept:visible').count(),1);await page.locator('#query').fill('');}
   if(file==='formal.html'){for(const s of fs.readFileSync(path.join(root,'docs/formal/0.2.0-rc.4/entity-inventory.csv'),'utf8').trim().split(/\r?\n/).slice(1).map(l=>l.split(',')[0])){await page.locator('#query').fill(s);assert.equal(await page.locator('article.term:visible').count(),1);}await page.locator('#query').fill('');await page.locator('#module').selectOption('mappings');assert.equal(await page.locator('article.term:visible').count(),4);await page.locator('a[href="formal.html#term-SR-CPT-001"]').first().click();await page.waitForFunction(()=>!document.getElementById('term-SR-CPT-001').hidden);assert.equal(await page.locator('#module').inputValue(),'');await page.locator('#query').fill('SR-REL-003');await page.locator('#term-SR-REL-003 a[href="formal.html#term-SR-CPT-006"]').first().click();await page.waitForFunction(()=>!document.getElementById('term-SR-CPT-006').hidden);assert.equal(await page.locator('#query').inputValue(),'');}
   await page.screenshot({path:path.join(art,`${name}-${file}.png`),fullPage:false});
  }
  const presets=['semrisk','semrisk-core','semrisk-enterprise','semrisk-method','semrisk-assessment-context'];
  await page.goto(base+relative+'explorer/index.html',{waitUntil:'domcontentloaded'});
  for(const preset of presets){if(preset!=='semrisk'){const loaded=page.waitForResponse(r=>r.url().endsWith('/data/'+preset+'.json'));await page.locator('#semriskModuleSelect').selectOption(preset);await loaded;}await page.waitForFunction(()=>document.querySelectorAll('#graph svg.vowlGraph .nodeContainer .node').length>0,null,{timeout:90000});await page.locator('#loading-info').waitFor({state:'hidden',timeout:90000});assert(!(await page.locator('body').innerText()).includes('Editing mode activated'),'editing hint in read-only explorer');const hints=page.locator('[id^="killFilterMessages_"]');for(let i=0;i<await hints.count();i++){if(await hints.nth(i).isVisible())await hints.nth(i).click();}await page.screenshot({path:path.join(art,`${name}-${preset}.png`),fullPage:false});}
  await Promise.all([page.waitForResponse(r=>r.url().endsWith('/data/semrisk.json')&&r.status()===200),page.locator('#semriskModuleSelect').selectOption('semrisk')]);await page.locator('#loading-info').waitFor({state:'hidden',timeout:90000});
  const readOnlyCount=await page.locator('#graph svg.vowlGraph .nodeContainer .node').count();await page.mouse.dblclick(viewport.width-130,viewport.height-150);await page.waitForTimeout(250);assert.equal(await page.locator('#graph svg.vowlGraph .nodeContainer .node').count(),readOnlyCount,'double click created a node');
  await page.locator('#search-input-text').fill('Risk Scenario');await page.locator('#search-input-text').press('Enter');
  for(const id of ['zoomInButton','zoomOutButton']){const before=await page.locator('#graph svg.vowlGraph > g').getAttribute('transform');await page.locator('#'+id).focus();await page.keyboard.down('Enter');await page.waitForTimeout(450);await page.keyboard.up('Enter');await page.waitForTimeout(350);assert.notEqual(await page.locator('#graph svg.vowlGraph > g').getAttribute('transform'),before,'keyboard '+id+' did not change graph');}
  await page.locator('#centerGraphButton').focus();await page.keyboard.press('Enter');
  await page.locator('#sidebarExpandButton').focus();await page.keyboard.press('Enter');await page.waitForFunction(()=>!document.querySelector('#detailsArea').classList.contains('hidden'));await page.keyboard.press('Enter');await page.waitForFunction(()=>document.querySelector('#detailsArea').classList.contains('hidden'));
  await page.locator('#search-input-text').fill('https://example.com/private.ttl');await page.locator('#search-input-text').press('Enter');
  for(const hash of ['url=https://example.com/private.json','iri=https://example.com/private.ttl','file=test.ttl','../private','%2e%2e%2fprivate','opts=editorMode=true;#new_ontology1']){
   await Promise.all([page.waitForResponse(r=>r.url().endsWith('/data/semrisk.json')&&r.status()===200),page.goto(base+relative+'explorer/index.html#'+hash,{waitUntil:'domcontentloaded'})]);await page.locator('#loading-info').waitFor({state:'hidden',timeout:90000});await page.waitForFunction(()=>document.querySelectorAll('#graph svg.vowlGraph .nodeContainer .node').length>0);
  }
  assert.equal(await page.locator('#semriskModuleSelect').inputValue(),'semrisk');
  await page.locator('#directUploadBtn').dispatchEvent('click');await page.locator('#file-converter-button').dispatchEvent('click');
  const transfer=await page.evaluateHandle(()=>new DataTransfer());await page.locator('#canvasArea').dispatchEvent('drop',{dataTransfer:transfer});await transfer.dispose();
  for(const m of ['governance','pharma','mappings']){await page.goto(base+relative+'explorer/index.html');await page.locator('#semriskModuleSelect').selectOption('index-'+m);await page.waitForURL('**/formal.html?module='+m);assert.equal(await page.locator('#module').inputValue(),m);assert((await page.locator('article.term:visible').count())>0);}
  await page.emulateMedia({colorScheme:'dark'});for(const file of ['index.html','formal.html']){await page.goto(base+relative+file);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await page.screenshot({path:path.join(art,`${name}-dark-${file}.png`),fullPage:false});}
  assert.equal(errors.length,0,JSON.stringify(errors));assert.equal(badRequests.length,0,JSON.stringify(badRequests));assert.equal(badResponses.length,0,JSON.stringify(badResponses));
  report.viewports.push({name,viewport,documentation_pages:8,graph_presets:5,all_term_search_count:116,keyboard_zoom_assertions:2,keyboard_details_toggle:true,filtered_anchor_regressions:2,center_key_exercised:true,dark_mode_pages:2,negative_hash_routes:6,page_errors:errors.length,forbidden_requests:badRequests.length,failed_responses:badResponses.length});await page.close();
 }
 fs.writeFileSync(path.join(art,'report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;}).finally(()=>{if(server)server.kill();});
