import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const browser=await chromium.launch({headless:true});
try {
  for (const [html,pdf] of [['06.01.html','06.01.pdf'],['06.01-solutions.html','06.01-solutions.pdf']]) {
    const page=await browser.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:1});
    await page.goto(pathToFileURL(path.join(root,'handouts',html)).href,{waitUntil:'load'});
    if(html==='06.01.html') await page.waitForFunction(()=>document.documentElement.dataset.cosmologyReady==='true');
    await page.evaluate(()=>document.fonts.ready);
    await page.emulateMedia({media:'print'});
    const target=path.join(root,'handouts','pdf',pdf);
    fs.mkdirSync(path.dirname(target),{recursive:true});
    await page.pdf({path:target,format:'A4',printBackground:true,preferCSSPageSize:true,
      displayHeaderFooter:true,
      headerTemplate:'<span></span>',
      footerTemplate:'<div style="width:100%;padding:0 15mm;font:9px Arial,sans-serif;color:#6e767d;display:flex;justify-content:space-between"><span>MAIS PAC · Cosmology · 06.01</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
      tagged:true,outline:true});
    console.log(`Exported ${pdf} (${fs.statSync(target).size.toLocaleString()} bytes)`);
    await page.close();
  }
} finally {await browser.close();}
