import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const codes=['01.01','01.02','01.03','01.04','01.05'];
const browser=await chromium.launch({headless:true});
try {
 for(const code of codes) for(const [html,pdf,label] of [[`${code}.html`,`${code}.pdf`,'Lecture + Problems'],[`${code}-solutions.html`,`${code}-solutions.pdf`,'Worked Solutions']]) {
  const page=await browser.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:1,reducedMotion:'reduce'});
  await page.goto(pathToFileURL(path.join(root,'handouts',html)).href,{waitUntil:'load'});
  if(!html.includes('solutions')) await page.waitForFunction(()=>document.documentElement.dataset.basicReady==='true');
  await page.evaluate(()=>document.fonts.ready);
  await page.emulateMedia({media:'print'});
  const target=path.join(root,'handouts','pdf',pdf);fs.mkdirSync(path.dirname(target),{recursive:true});
  await page.pdf({path:target,format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,
   headerTemplate:'<span></span>',
   footerTemplate:`<div style="width:100%;padding:0 15mm;font:9px Arial,sans-serif;color:#6e767d;display:flex;justify-content:space-between"><span>MAIS PAC · Basic Astrophysics · ${code} · ${label}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
   tagged:true,outline:true});
  console.log(`Exported ${pdf} (${fs.statSync(target).size.toLocaleString()} bytes)`);await page.close();
 }
} finally {await browser.close();}
