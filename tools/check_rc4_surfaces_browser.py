from pathlib import Path
import json
from playwright.sync_api import sync_playwright
repo=Path(__file__).resolve().parents[1];root=repo/'site/ontology/0.2.0-rc.4';out=repo/'build/rc4-surface-browser';out.mkdir(parents=True,exist_ok=True);results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True)
 for name,width,height in [('desktop',1440,1000),('mobile',390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  for fn in ['index.html','guide.html']:
   page.goto((root/fn).as_uri());page.wait_for_load_state('load')
   assert page.locator('h1').count()>=1
   assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'),(name,fn,'horizontal overflow')
   assert page.locator('script').count()==0
   page.screenshot(path=str(out/f'{name}-{fn}-top.png'))
   if fn=='index.html':
    assert page.locator('article').count()==116
    page.locator('#term-NumericScale').scroll_into_view_if_needed();page.screenshot(path=str(out/f'{name}-numeric-scale.png'))
    page.locator('a[href="guide.html"]').first.click();assert page.url.endswith('guide.html')
   else:
    assert page.locator('nav[aria-label="Formal reference sections"] a').count()==10
    page.locator('nav[aria-label="Formal reference sections"] a').nth(4).click();page.screenshot(path=str(out/f'{name}-fd-e.png'))
    page.locator('a[href="index.html#term-SR-CPT-036"]').click();assert page.url.endswith('#term-SR-CPT-036');assert page.locator('#term-SR-CPT-036').is_visible()
   results.append({'viewport':name,'file':fn,'horizontal_overflow':False,'local_navigation':'PASS'})
  page.close()
 browser.close()
(out/'browser-smoke.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results))
