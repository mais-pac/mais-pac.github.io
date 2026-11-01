import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const base=process.env.BASE_URL || pathToFileURL(path.join(root,'handouts')+'/').href;
const url=n=>new URL(n,base).href;
const topics=[
 ['07.01','windows'],['07.02','telescope'],['08.01','root'],['08.02','calculus'],['08.03','vectors'],['08.04','geometry'],['08.05','stats'],
 ['09.01','nakedeye'],['09.02','skymap'],['09.03','coords'],['09.04','exposure'],['10.01','errors'],['10.02','fit'],['10.03','doublestar'],['10.04','photometry']
];
const browser=await chromium.launch();const errors=[];const external=[];
const near=(a,b,tol=1e-6)=>assert.ok(Math.abs(a-b)<=tol,`${a} != ${b}`);
const checks={
 '07.01':()=>{const L=window.CurriculumLabs;if(Math.abs(L.peakUm(5800)-.49961585)>.0001)throw new Error('peakUm');if(L.bandOf(.55)!=='Visible')throw new Error('band');},
 '07.02':()=>{const m=window.CurriculumLabs.telescopeModel(200,1000,20,1.5);if(Math.abs(m.fr-5)>1e-9||Math.abs(m.mag-50)>1e-9||Math.abs(m.pupil-4)>1e-9||Math.abs(m.ray-.692)>.001||Math.abs(m.eff-1.5)>1e-9)throw new Error('telescope');},
 '08.01':()=>{const m=window.CurriculumLabs.kepler(1,.5,'newton');if(Math.abs(m.res)>1e-10||m.iter>=10)throw new Error('kepler');},
 '08.02':()=>{const L=window.CurriculumLabs;if(Math.abs(L.CALC.poly.df(3)-6)>1e-9||Math.abs(L.CALC.poly.int(3)-9)>1e-9||Math.abs(L.simpson(x=>x*x,0,1)-1/3)>1e-9)throw new Error('calculus');},
 '08.03':()=>{const m=window.CurriculumLabs.vectorModel(5,0,4,90);if(Math.abs(m.mag-Math.hypot(5,4))>1e-9||Math.abs(m.dot)>1e-9||Math.abs(m.cross-20)>1e-9)throw new Error('vectors');},
 '08.04':()=>{const m=window.CurriculumLabs.geometryModel(2,30,90);if(Math.abs(m.sep-60)>1e-9||Math.abs(m.dra-60)>1e-9||Math.abs(m.ddec)>1e-9)throw new Error('geometry');},
 '08.05':()=>{const m=window.CurriculumLabs.statsModel(20,.3,0);if(Math.abs(m.mean-10)>.5||m.std<=0)throw new Error('stats');},
 '09.01':()=>{if(typeof window.CurriculumLabs.peakUm!=='function')throw new Error('nakedeye');},
 '09.02':()=>{if(typeof window.CurriculumLabs.coordModel!=='function')throw new Error('skymap');},
 '09.03':()=>{const m=window.CurriculumLabs.coordModel(6,20,6,47.9);if(Math.abs(m.H)>1e-9||Math.abs(m.alt-62.1)>.2||m.state!=='Above horizon')throw new Error('coords');},
 '09.04':()=>{const m=window.CurriculumLabs.exposureModel(200,10,60,19);if(!(m.src>0&&m.snr>0&&m.t5>0))throw new Error('exposure');},
 '10.01':()=>{const m=window.CurriculumLabs.errorModel(10,.5,.3,10);if(Math.abs(m.rand-.3/Math.sqrt(10))>1e-9||Math.abs(m.total-Math.hypot(.5,.3/Math.sqrt(10)))>1e-9)throw new Error('errors');},
 '10.02':()=>{const m=window.CurriculumLabs.fitModel(2,0,12,false);if(Math.abs(m.b-2)>1e-9||Math.abs(m.a-1)>1e-9||Math.abs(m.r2-1)>1e-9)throw new Error('fit');},
 '10.03':()=>{const m=window.CurriculumLabs.doubleModel(8,60,1,.5);if(Math.abs(m.mm-8)>1e-9||Math.abs(m.unc-.5)>1e-9)throw new Error('doublestar');},
 '10.04':()=>{const m=window.CurriculumLabs.photModel(.1,0,0,0);if(Math.abs(m.delta-.1)>1e-9||Math.abs(m.model-.1)>1e-9||Math.abs(m.res)>1e-9)throw new Error('photometry');}
};
try{
 const page=await browser.newPage({viewport:{width:1280,height:950}});
 page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
 page.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith(new URL(base).origin))external.push(r.url());});
 for(const [code,key] of topics){
  await page.goto(url(`${code}.html`),{waitUntil:'load'});await page.waitForFunction(()=>document.documentElement.dataset.curriculumReady==='true');
  assert.equal(await page.locator('.problem').count(),10,`${code} problems`);
  assert.equal(await page.locator('.cosmo-figure').count(),2,`${code} figures`);
  assert.equal(await page.locator('.cosmo-lab').count(),1,`${code} lab`);
  assert.ok(await page.locator('.cosmo-toc a').count()>=8);
  assert.ok((await page.locator('#summary-'+key).textContent()).length>20,`${code} lab summary`);
  for(const href of await page.locator('a').evaluateAll(as=>as.map(a=>a.getAttribute('href')))){
   if(href.startsWith('#'))assert.ok(await page.locator(href).count(),`Missing ${href}`);
   else if(!/^(https?:|mailto:|data:)/.test(href)){const p=path.resolve(root,'handouts',href.split('#')[0]);assert.ok(fs.existsSync(p),`Missing ${href}`);}
  }
  await page.evaluate(()=>window.scrollTo({top:900,behavior:'instant'}));await page.waitForTimeout(60);
  near(await page.locator('.handout-bar').evaluate(el=>el.getBoundingClientRect().top),0,1);
  await page.locator('.cosmo-lab [data-reset]').click();
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${code} overflow`);
  const labCheck=checks[code];if(labCheck)await page.evaluate(labCheck);
  await page.setViewportSize({width:390,height:844});await page.reload({waitUntil:'load'});await page.waitForFunction(()=>document.documentElement.dataset.curriculumReady==='true');
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${code} mobile overflow`);
  await page.setViewportSize({width:1280,height:950});
  const sol=await browser.newPage({viewport:{width:1280,height:950}});sol.on('pageerror',e=>errors.push(e.message));
  await sol.goto(url(`${code}-solutions.html`),{waitUntil:'load'});assert.equal(await sol.locator('.solution').count(),10);
  for(let i=1;i<=10;i++)assert.equal(await sol.locator('#s'+i).count(),1);
  assert.ok((await sol.locator('main').innerText()).includes('Check'));
  await sol.close();
  for(const pdf of [`pdf/${code}.pdf`,`pdf/${code}-solutions.pdf`])assert.ok(fs.statSync(path.resolve(root,'handouts',pdf)).size>10000,`${pdf} too small`);
 }
 if(base.startsWith('http')){
  const rootUrl=new URL('/',base).href;
  await page.goto(rootUrl+'teaching/',{waitUntil:'load'});
  for(const [code] of topics){
   assert.ok(await page.locator(`.curriculum-card a[href="../handouts/${code}.html"]`).count()===1,`${code} Teaching lecture link`);
   assert.ok(await page.locator(`.curriculum-card a[href="../handouts/${code}-solutions.html"]`).count()===1,`${code} Teaching solutions link`);
   assert.equal(await page.locator(`a[href="pdf/${code}-problems.pdf"]`).count(),0,`${code} placeholder remains`);
  }
  assert.ok(await page.locator('a[href="mailto:physicsandastronomy24@gmail.com"]').count()>=1);
 }
 assert.deepEqual(external,[],'external requests');assert.deepEqual(errors,[],'browser errors');
 console.log(`PASS Extended curriculum (${base.startsWith('file')?'offline':'live'}): 15 lectures, 150 problems/solutions, 30 figures, 15 labs, 30 PDFs, sticky bars, mobile and Teaching links.`);
}finally{await browser.close();}
