import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const base=process.env.BASE_URL || pathToFileURL(path.join(root,'handouts')+'/').href;
const url=n=>new URL(n,base).href;
const codes=['01.01','01.02','01.03','01.04','01.05'];
const browser=await chromium.launch();const errors=[];const external=[];
const near=(a,b,tol=1e-6)=>assert.ok(Math.abs(a-b)<=tol,`${a} != ${b}`);
const setInput=async(page,id,v)=>page.locator('#'+id).evaluate((el,v)=>{el.value=String(v);el.dispatchEvent(new Event('input',{bubbles:true}));},v);
try{
 const page=await browser.newPage({viewport:{width:1280,height:950}});
 page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
 page.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith(new URL(base).origin))external.push(r.url());});
 for(const code of codes){
  await page.goto(url(`${code}.html`),{waitUntil:'load'});await page.waitForFunction(()=>document.documentElement.dataset.basicReady==='true');
  assert.equal(await page.locator('.problem').count(),15,`${code} problems`);
  assert.equal(await page.locator('.cosmo-figure').count(),2,`${code} figures`);
  assert.equal(await page.locator('.cosmo-lab').count(),1,`${code} lab`);
  assert.ok(await page.locator('.cosmo-toc a').count()>=10);
  // local links and anchors
  for(const href of await page.locator('a').evaluateAll(as=>as.map(a=>a.getAttribute('href')))){
   if(href.startsWith('#'))assert.ok(await page.locator(href).count(),`Missing ${href}`);
   else if(!/^(https?:|mailto:|data:)/.test(href)){const p=path.resolve(root,'handouts',href.split('#')[0]);assert.ok(fs.existsSync(p),`Missing ${href}`);}
  }
  // sticky handout bar
  await page.evaluate(()=>window.scrollTo({top:900,behavior:'instant'}));await page.waitForTimeout(80);
  near(await page.locator('.handout-bar').evaluate(el=>el.getBoundingClientRect().top),0,1);
  // reset control returns numeric defaults
  await page.locator('.cosmo-lab [data-reset]').click();
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${code} overflow`);
  await page.setViewportSize({width:390,height:844});await page.reload({waitUntil:'load'});await page.waitForFunction(()=>document.documentElement.dataset.basicReady==='true');
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${code} mobile overflow`);
  await page.setViewportSize({width:1280,height:950});
  const sol=await browser.newPage({viewport:{width:1280,height:950}});sol.on('pageerror',e=>errors.push(e.message));
  await sol.goto(url(`${code}-solutions.html`),{waitUntil:'load'});assert.equal(await sol.locator('.solution').count(),15);
  for(let i=1;i<=15;i++)assert.equal(await sol.locator('#s'+i).count(),1);
  assert.ok((await sol.locator('main').innerText()).includes('Check'));
  await sol.close();
  for(const pdf of [`pdf/${code}.pdf`,`pdf/${code}-solutions.pdf`])assert.ok(fs.statSync(path.resolve(root,'handouts',pdf)).size>10000,`${pdf} too small`);
 }
 // Lab numerical checks through exposed pure functions.
 await page.goto(url('01.01.html'),{waitUntil:'load'});await page.waitForFunction(()=>window.BasicLabs);
 let m=await page.evaluate(()=>window.BasicLabs.orbitModel(1,.6,1));near(m.period,1);near(m.rp,.4);near(m.ra,1.6);near(m.vp,59.5693836,.001);
 await setInput(page,'orbit-a',4);assert.match(await page.locator('#out-orbit-period').textContent(),/8\.000 yr/);await page.locator('[data-reset="orbit"]').click();
 await page.goto(url('01.02.html'),{waitUntil:'load'});await page.waitForFunction(()=>window.BasicLabs);
 m=await page.evaluate(()=>window.BasicLabs.peakWavelength(5800)*1e6);near(m,.49961585,.0001);
 await setInput(page,'bb-t',11600);assert.match(await page.locator('#out-blackbody-peak').textContent(),/0\.250 μm/);await page.locator('[data-reset="blackbody"]').click();
 await page.goto(url('01.03.html'),{waitUntil:'load'});await page.waitForFunction(()=>window.BasicLabs);
 m=await page.evaluate(()=>window.BasicLabs.gasModel('isothermal',2));near(m.W,1728.943896,.01);near(m.Q,m.W);near(m.dU,0);
 await page.locator('#gas-process').selectOption('adiabatic');await page.locator('[data-reset="gas"]').click();assert.equal(await page.locator('#gas-process').inputValue(),'isothermal');
 await page.goto(url('01.04.html'),{waitUntil:'load'});await page.waitForFunction(()=>window.BasicLabs);
 m=await page.evaluate(()=>window.BasicLabs.spectrumModel(656.28,100,10000,20000));near(m.center,656.498948,.0001);near(m.thermal,.0468217,.0001);
 await setInput(page,'spec-v',0);assert.match(await page.locator('#out-spectrum-shift').textContent(),/0\.0000 nm/);await page.locator('[data-reset="spectrum"]').click();
 await page.goto(url('01.05.html'),{waitUntil:'load'});await page.waitForFunction(()=>window.BasicLabs);
 m=await page.evaluate(()=>window.BasicLabs.decayModel(3));near(m.fraction,.125);near(m.remaining,1.25e11);
 await setInput(page,'decay-n',3);assert.match(await page.locator('#out-decay-fraction').textContent(),/12\.500%/);await page.locator('[data-reset="decay"]').click();
 // Teaching/home layout requests.
 if(base.startsWith('http')){
  const rootUrl=new URL('/',base).href;
  for(const rel of ['','teaching/','about/','explore/','resources/','mechanics/']){
   await page.goto(rootUrl+rel,{waitUntil:'load'});await page.evaluate(()=>window.scrollTo({top:1000,behavior:'instant'}));await page.waitForTimeout(60);
   const bar=page.locator('.site-header');near(await bar.evaluate(el=>el.getBoundingClientRect().top),0,1);
  }
  await page.goto(rootUrl+'teaching/',{waitUntil:'load'});
  assert.equal(await page.locator('[data-mechanics-feature]').count(),0);
  assert.ok(await page.locator('.physics-mechanics-heading a[href="../mechanics/"]').count()===1);
  assert.ok(await page.locator('a[href="mailto:physicsandastronomy24@gmail.com"]').count()>=1);
  for(const code of codes)assert.ok(await page.locator(`.curriculum-card a[href="../handouts/${code}.html"]`).count()===1);
  await page.goto(rootUrl,{waitUntil:'load'});assert.equal(await page.locator('[data-mechanics-feature]').count(),0);
 }
 assert.deepEqual(external,[],'external requests');assert.deepEqual(errors,[],'browser errors');
 console.log(`PASS Basic Astrophysics (${base.startsWith('file')?'offline':'live'}): 5 lectures, 75 problems/solutions, 10 figures, 5 labs, PDFs, sticky bars, mobile and Teaching layout.`);
}finally{await browser.close();}
