/* Render exact SVG and Graphviz geometry. Node package is pinned in requirements. */
const fs=require('fs'),path=require('path');
const runtime=process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
const vizPackage=runtime ? path.join(runtime,'@viz-js/viz') : '@viz-js/viz';
const {instance}=require(vizPackage);
(async()=>{
 const root=path.resolve(__dirname,'..'),dir=path.join(root,'diagrams/ontouml/0.2.0-rc.4'),spec=JSON.parse(fs.readFileSync(path.join(dir,'view-spec.json'),'utf8'));
 const viz=await instance();
 for(const v of spec.views){const dot=fs.readFileSync(path.join(dir,'views',v.id+'.dot'),'utf8');
  fs.writeFileSync(path.join(dir,'views',v.id+'.svg'),viz.renderString(dot,{format:'svg'}));
  fs.writeFileSync(path.join(dir,'views',v.id+'.layout.json'),viz.renderString(dot,{format:'json'}));
 }
 console.log('Rendered '+spec.views.length+' SVG views and exact layout sources.');
})().catch(e=>{console.error(e);process.exit(1)});
