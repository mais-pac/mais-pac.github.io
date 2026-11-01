import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const topics=[
 ['07.01','Instrumentation and Space Technologies'],['07.02','Instrumentation and Space Technologies'],
 ['08.01','Mathematical Methods and Tools'],['08.02','Mathematical Methods and Tools'],['08.03','Mathematical Methods and Tools'],['08.04','Mathematical Methods and Tools'],['08.05','Mathematical Methods and Tools'],
 ['09.01','Practical Part'],['09.02','Practical Part'],['09.03','Practical Part'],['09.04','Practical Part'],
 ['10.01','Practical Part'],['10.02','Practical Part'],['10.03','Practical Part'],['10.04','Practical Part']
];
const browser=await chromium.launch({headless:true});
try {
 for(const [code,group] of topics) for(const [html,pdf,label] of [[`${code}.html`,`${code}.pdf`,'Lecture + Problems'],[`${code}-solutions.html`,`${code}-solutions.pdf`,'Worked Solutions']]) {
  const page=await browser.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:1,reducedMotion:'reduce'});
  await page.goto(pathToFileURL(path.join(root,'handouts',html)).href,{waitUntil:'load'});
  if(!html.includes('solutions')) await page.waitForFunction(()=>document.documentElement.dataset.curriculumReady==='true');
  await page.evaluate(()=>document.fonts.ready);
  await page.emulateMedia({media:'print'});
  const target=path.join(root,'handouts','pdf',pdf);fs.mkdirSync(path.dirname(target),{recursive:true});
  await page.pdf({path:target,format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,
   headerTemplate:'<span></span>',
   footerTemplate:`<div style="width:100%;padding:0 15mm;font:9px Arial,sans-serif;color:#6e767d;display:flex;justify-content:space-between"><span>MAIS PAC · ${group} · ${code} · ${label}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
   tagged:true,outline:true});
  console.log(`Exported ${pdf} (${fs.statSync(target).size.toLocaleString()} bytes)`);await page.close();
 }
} finally {await browser.close();}
