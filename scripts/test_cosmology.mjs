import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const base=process.env.BASE_URL || pathToFileURL(path.join(root,'handouts')+'/').href;
const url=name=>new URL(name,base).href;
const errors=[];
const browser=await chromium.launch({headless:true});
const near=(a,b,tol=0.015)=>assert.ok(Math.abs(a-b)<=tol,`${a} != ${b}`);
const text=async(page,id)=>page.locator('#'+id).textContent();
const setInput=async(page,id,value)=>page.locator('#'+id).evaluate((el,v)=>{el.value=String(v);el.dispatchEvent(new Event('input',{bubbles:true}));},value);
try {
  const page=await browser.newPage({viewport:{width:1280,height:1000}});
  page.on('pageerror',e=>errors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
  const external=[];
  page.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith(new URL(base).origin))external.push(r.url());});
  await page.goto(url('06.01.html'),{waitUntil:'load'});
  await page.waitForFunction(()=>document.documentElement.dataset.cosmologyReady==='true');
  assert.equal(await page.locator('.problem').count(),30);
  assert.equal(await page.locator('.cosmo-lab').count(),5);
  assert.equal(await page.locator('.cosmo-figure').count(),6);
  assert.equal(await page.locator('.cosmo-toc a').count(),20);
  assert.equal((await text(page,'out-dyn-age')).trim(),'13.47 Gyr');
  assert.equal((await text(page,'out-cmb-t')).trim(),'2972.8 K');
  assert.equal((await text(page,'out-dist-dc')).trim(),'3.304 Gpc');
  assert.equal((await text(page,'out-hub-h')).trim(),'72.06');
  const model=await page.evaluate(()=>{const m=window.CosmologyLabs;return {age:m.ageGyr(),dc:m.comovingGpc(1),lb:m.lookbackGyr(1),hor:m.horizons(),fit:m.fitHubble(m.data),shape:m.planckShape(2.897771955e-3/2.725*1e6,2.725)};});
  near(model.age,13.46698,.002);near(model.dc,3.30383,.002);near(model.lb,7.71534,.002);
  near(model.hor.particle,14.15481,.003);near(model.hor.event,4.88519,.003);near(model.fit.h,72.0621,.002);near(model.shape,1,1e-8);
  // Internal anchors and local deliverable links.
  const links=await page.locator('a').evaluateAll(as=>as.map(a=>a.getAttribute('href')));
  for(const href of links){
    if(href.startsWith('#'))assert.ok(await page.locator(href).count(),`Missing anchor ${href}`);
    else if(!/^(https?:|mailto:|data:)/.test(href)){
      const p=path.resolve(root,'handouts',href.split('#')[0]);assert.ok(fs.existsSync(p),`Missing local file ${href}`);
    }
  }
  // Expansion and animation.
  await setInput(page,'expansion-a',2);
  assert.equal(await text(page,'out-exp-da'),'200 Mpc');assert.equal(await text(page,'out-exp-db'),'600 Mpc');
  await page.locator('[data-reset="expansion"]').click();assert.equal(await text(page,'out-exp-da'),'100 Mpc');
  await page.locator('#expansion-play').click();await page.waitForTimeout(800);
  assert.ok(Number(await page.locator('#expansion-a').inputValue())>1);
  await page.locator('#expansion-play').click();const paused=await page.locator('#expansion-a').inputValue();await page.waitForTimeout(120);assert.equal(await page.locator('#expansion-a').inputValue(),paused);
  await page.locator('[data-reset="expansion"]').click();
  // Dynamics presets and reset.
  await page.locator('[data-preset="eds"]').click();assert.equal(await text(page,'out-dyn-age'),'9.31 Gyr');assert.equal(await text(page,'out-dyn-q'),'0.50');
  await page.locator('[data-preset="benchmark"]').click();assert.equal(await text(page,'out-dyn-age'),'13.47 Gyr');
  await setInput(page,'dynamics-h0',50);assert.equal(await text(page,'out-dyn-age'),'18.85 Gyr');
  await page.locator('[data-reset="dynamics"]').click();
  // CMB presets.
  await page.locator('[data-cmb="0"]').click();assert.equal(await text(page,'out-cmb-t'),'2.7 K');assert.equal(await text(page,'out-cmb-z'),'0.00');
  await page.locator('[data-cmb="3.0378"]').click();assert.equal(await text(page,'out-cmb-t'),'2972.8 K');
  await page.locator('[data-reset="cmb"]').click();
  // Distances and low-z limit.
  await setInput(page,'distances-z',0);assert.equal(await text(page,'out-dist-dc'),'0.000 Gpc');assert.equal(await text(page,'out-dist-time'),'0.000 Gyr');
  await setInput(page,'distances-z',2);assert.equal(await text(page,'out-dist-dc'),'5.180 Gpc');assert.equal(await text(page,'out-dist-da'),'1.727 Gpc');
  await page.locator('[data-reset="distances"]').click();
  // Hubble selection, error bars, table and CSV export.
  await page.locator('#hubble-cut').selectOption('0.05');assert.equal(await text(page,'out-hub-n'),'6');
  await page.locator('#hubble-errors').uncheck();await page.locator('#hubble-errors').check();
  await page.locator('.lab-data summary').click();assert.equal(await page.locator('#hubble-table-body tr').count(),12);
  const download=page.waitForEvent('download');await page.locator('#hubble-export').click();assert.equal((await download).suggestedFilename(),'synthetic-hubble-selected.csv');
  await page.locator('[data-reset="hubble"]').click();assert.equal(await text(page,'out-hub-n'),'12');
  // Keyboard-labelled controls and desktop overflow.
  const unlabelled=await page.locator('.lab-controls input,.lab-controls select').evaluateAll(els=>els.filter(e=>!e.labels?.length&&!e.getAttribute('aria-label')).map(e=>e.id));assert.deepEqual(unlabelled,[]);
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  // Mobile layout.
  await page.setViewportSize({width:390,height:844});await page.reload({waitUntil:'load'});await page.waitForFunction(()=>document.documentElement.dataset.cosmologyReady==='true');
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Mobile horizontal overflow');
  await page.locator('#lab-hubble').scrollIntoViewIfNeeded();assert.ok(await page.locator('#out-hub-h').isVisible());
  // Solutions, attribution and hard-problem explanations.
  const sol=await browser.newPage({viewport:{width:1280,height:1000}});sol.on('pageerror',e=>errors.push(e.message));
  await sol.goto(url('06.01-solutions.html'),{waitUntil:'load'});
  assert.equal(await sol.locator('.solution').count(),30);
  for(let i=1;i<=30;i++)assert.equal(await sol.locator('#s'+i).count(),1);
  const solText=await sol.locator('main').innerText();
  assert.ok((solText.match(/IOAA connection/g)||[]).length>=10);
  assert.ok((solText.match(/Why this is hard/g)||[]).length>=10);
  assert.ok(solText.includes('71.6'));
  assert.ok(await sol.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  await sol.setViewportSize({width:390,height:844});assert.ok(await sol.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Solutions mobile overflow');
  // PDFs are real, nontrivial files. Full pagination is checked separately.
  for(const name of ['pdf/06.01.pdf','pdf/06.01-solutions.pdf'])assert.ok(fs.statSync(path.resolve(root,'handouts',name)).size>10000);
  assert.deepEqual(external,[],'Unexpected external browser requests');
  assert.deepEqual(errors,[],'Browser errors');
  console.log('PASS: 30 problems, 30 solutions, 5 labs, 6 figures; numerical, interaction, offline, mobile, link and PDF checks.');
} finally {await browser.close();}
