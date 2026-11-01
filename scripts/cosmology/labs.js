/* MAIS PAC Cosmology laboratories. Original code; no network requests.
   All plotted curves are SVG. Benchmark units: km/s/Mpc, Gpc, Gyr. */
(() => {
  'use strict';
  const C = 299792.458, MPC = 3.0856775814913673e19, GYR = 3.15576e16;
  const H0 = 70, OM = 0.3, OL = 0.7, T0 = 2.725;
  const DATA = __HUBBLE_DATA__;
  const $ = id => document.getElementById(id);
  const exists = id => !!$(id);
  const clamp = (x,a,b) => Math.max(a,Math.min(b,x));
  const fmt = (x,n=2) => Number(x).toFixed(n);
  const sci = x => { if (x === 0) return '0'; const e = Math.floor(Math.log10(Math.abs(x))); return `${(x/10**e).toFixed(2)} × 10^${e}`; };
  const th = (h=H0) => MPC/h/GYR;
  function simpson(f,a,b,n=768) {
    n += n%2; const h=(b-a)/n;
    let s=f(a)+f(b);
    for(let i=1;i<n;i++) s+=(i%2?4:2)*f(a+i*h);
    return s*h/3;
  }
  const E = (z,om=OM,ol=OL) => Math.sqrt(om*(1+z)**3+ol);
  const comovingGpc = (z,h=H0,om=OM,ol=OL) => C/h/1000*simpson(x=>1/E(x,om,ol),0,z,512);
  const lookbackGyr = (z,h=H0,om=OM,ol=OL) => th(h)*simpson(x=>1/((1+x)*E(x,om,ol)),0,z,512);
  const ageGyr = (h=H0,om=OM,ol=OL) => th(h)*2*simpson(y=>y*y/Math.sqrt(om+ol*y**6),0,1,768);
  function horizons(h=H0,om=OM,ol=OL) {
    const dh=C/h/1000;
    return {particle:dh*2*simpson(y=>1/Math.sqrt(om+ol*y**6),0,1,768),
      event:ol>0?dh*simpson(u=>1/Math.sqrt(ol+om*u**3),0,1,768):Infinity};
  }
  function fitHubble(rows) {
    const xx=rows.reduce((s,r)=>s+r.distance_mpc**2,0);
    const h=rows.reduce((s,r)=>s+r.distance_mpc*r.velocity_km_s,0)/xx;
    const err=Math.sqrt(rows.reduce((s,r)=>s+(r.distance_mpc*r.sigma_velocity_km_s)**2,0))/xx;
    const rms=Math.sqrt(rows.reduce((s,r)=>s+(r.velocity_km_s-h*r.distance_mpc)**2,0)/rows.length);
    return {h,err,rms,n:rows.length};
  }
  const esc = s => String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const text = (x,y,s,opts='') => `<text x="${x}" y="${y}" ${opts}>${esc(s)}</text>`;
  const line = (x1,y1,x2,y2,stroke='#cbd5e1',extra='') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" ${extra}/>`;
  const circle = (x,y,r,fill,extra='') => `<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" ${extra}/>`;
  const polyline = (pts,color,width=2.5,extra='') => `<polyline points="${pts.filter(p=>Number.isFinite(p[0])&&Number.isFinite(p[1])).map(p=>p.join(',')).join(' ')}" fill="none" stroke="${color}" stroke-width="${width}" ${extra}/>`;
  function plot(key,body,height=330,desc='Numerical readouts are provided below the plot.') {
    const el=$(`plot-${key}`); if(!el)return;
    el.setAttribute('viewBox',`0 0 680 ${height}`);
    el.innerHTML=`<title>${esc(key)} interactive vector plot</title><desc>${esc(desc)}</desc>${body}`;
  }
  const output = (key,value) => { const el=$(`out-${key}`); if(el)el.textContent=value; };
  const summary = (key,value) => { const el=$(`summary-${key}`); if(el)el.textContent=value; };
  function axes({xmin=0,xmax=1,ymin=0,ymax=1,xticks=[],yticks=[],xlabel='',ylabel='',height=330}) {
    const l=64,r=24,t=38,b=52,w=680-l-r,h=height-t-b;
    const X=x=>l+(x-xmin)/(xmax-xmin)*w, Y=y=>t+h-(y-ymin)/(ymax-ymin)*h;
    let s=`<rect x="1" y="1" width="678" height="${height-2}" rx="7" fill="#ffffff"/>`;
    for(const x of xticks){s+=line(X(x),t,X(x),t+h,'#e9ecef')+text(X(x),t+h+20,x,'text-anchor="middle" fill="#6e767d" font-size="11"');}
    for(const y of yticks){s+=line(l,Y(y),l+w,Y(y),'#e9ecef')+text(l-9,Y(y)+4,y,'text-anchor="end" fill="#6e767d" font-size="11"');}
    s+=line(l,t+h,l+w,t+h,'#94a3b8')+line(l,t,l,t+h,'#94a3b8');
    s+=text(l+w/2,height-10,xlabel,'text-anchor="middle" fill="#526079" font-size="12"');
    s+=text(16,t+h/2,ylabel,`text-anchor="middle" fill="#526079" font-size="12" transform="rotate(-90 16 ${t+h/2})"`);
    return {s,X,Y,l,r,t,b,w,h};
  }
  const legend = (items,x=78,y=20) => items.map((it,i)=>circle(x+i*177,y,4,it[1])+text(x+10+i*177,y+4,it[0],'fill="#526079" font-size="11"')).join('');

  // 1. Comoving expansion: positions change, galaxy sizes and distance ratios do not.
  let animation=0, lastTime=0;
  function stopAnimation(){if(animation)cancelAnimationFrame(animation);animation=0;lastTime=0;if(exists('expansion-play'))$('expansion-play').textContent='Animate expansion';}
  function expansion(){
    if(!exists('expansion-a'))return;
    const a=+$('expansion-a').value; $('range-expansion').textContent=fmt(a);
    let s='<rect x="1" y="1" width="678" height="308" rx="7" fill="#fff"/>';
    for(let iy=-2;iy<=2;iy++)for(let ix=-3;ix<=3;ix++){
      const x=340+ix*52*a,y=130+iy*27*a;
      let fill='#94a3b8',r=3.5;
      if(ix===0&&iy===0){fill='#2457c5';r=6;}
      if(iy===0&&ix===1){fill='#059669';r=5;}
      if(iy===0&&ix===3){fill='#7c3aed';r=5;}
      s+=circle(x,y,r,fill);
    }
    s+=line(340,195,340+52*a,195,'#059669','stroke-width="2"')+line(340,215,340+156*a,215,'#7c3aed','stroke-width="2"');
    s+=text(340+26*a,188,'A','text-anchor="middle" fill="#047857" font-size="12"')+text(340+78*a,235,'B','text-anchor="middle" fill="#6d28d9" font-size="12"');
    s+=text(340,25,'Blue: observer   ·   Green: A   ·   Purple: B','text-anchor="middle" fill="#526079" font-size="12"');
    const pts=[];for(let i=0;i<=150;i++){const x=80+i*1.0*a;pts.push([x,278+9*Math.sin(i/150*6*Math.PI)]);}
    s+=polyline(pts,'#4338ca',2)+text(465,282,'Wave length also scales as a','fill="#4338ca" font-size="12"');
    plot('expansion',s,310,`Scale factor ${fmt(a)}. Galaxy A is ${fmt(100*a,0)} Mpc away; B is ${fmt(300*a,0)} Mpc away. Their ratio remains three.`);
    output('exp-a',fmt(a));output('exp-da',`${fmt(100*a,0)} Mpc`);output('exp-db',`${fmt(300*a,0)} Mpc`);output('exp-ratio','3.00');
    summary('expansion',`At a = ${fmt(a)}, the separations are ${fmt(100*a,0)} and ${fmt(300*a,0)} Mpc. Their ratio stays 3; the galaxy symbols do not expand.`);
  }
  function animate(t){
    if(!lastTime)lastTime=t;const dt=Math.min((t-lastTime)/1000,.25);lastTime=t;
    let a=+$('expansion-a').value+dt*.35;
    if(a>=2){$('expansion-a').value='2';expansion();stopAnimation();return;}
    $('expansion-a').value=String(a);expansion();animation=requestAnimationFrame(animate);
  }

  // 2. Flat matter + Lambda expansion history.
  function dynamics(){
    if(!exists('dynamics-om'))return;
    const om=+$('dynamics-om').value,ol=1-om,h=+$('dynamics-h0').value;
    $('range-dynamics-om').textContent=fmt(om);$('range-dynamics-h0').textContent=fmt(h,0);
    const ax=axes({xmax:4,ymin:-1,ymax:12,xticks:[0,1,2,3,4],yticks:[-1,0,3,6,9,12],xlabel:'Redshift z',ylabel:'Dimensionless expansion / deceleration',height:330});
    let s=ax.s+legend([['E(z) = H/H₀','#2457c5'],['q(z)','#059669']],80,20);
    const ep=[],qp=[];for(let i=0;i<=240;i++){const z=4*i/240,e=E(z,om,ol);ep.push([ax.X(z),ax.Y(e)]);qp.push([ax.X(z),ax.Y((.5*om*(1+z)**3-ol)/(e*e))]);}
    s+=polyline(ep,'#2457c5')+polyline(qp,'#059669');
    const zacc=ol>om/2?(2*ol/om)**(1/3)-1:null,zeq=ol>0?(ol/om)**(1/3)-1:null;
    if(zacc!==null&&zacc<=4)s+=line(ax.X(zacc),ax.Y(0),ax.X(zacc),ax.t,'#a7f3d0','stroke-dasharray="4 4"')+circle(ax.X(zacc),ax.Y(0),4,'#059669');
    plot('dynamics',s,330,`Flat model with matter density ${fmt(om)} and Lambda density ${fmt(ol)}. Present age ${fmt(ageGyr(h,om,ol))} Gyr.`);
    output('dyn-ol',fmt(ol));output('dyn-age',`${fmt(ageGyr(h,om,ol))} Gyr`);output('dyn-q',fmt(om/2-ol));output('dyn-zeq',zeq===null?'none (Λ = 0)':fmt(zeq,3));output('dyn-zacc',zacc===null?'not yet / none':fmt(zacc,3));
    summary('dynamics',`Ωm0 = ${fmt(om)}, ΩΛ0 = ${fmt(ol)}. The age is ${fmt(ageGyr(h,om,ol))} Gyr and q₀ = ${fmt(om/2-ol)}. Radiation is intentionally omitted.`);
  }

  // 3. Planck shape in wavelength units, with independently normalized peaks.
  function planckShape(lambdaMicron,T){
    const x=.01438776877/(lambdaMicron*1e-6*T),xp=4.9651142317;
    if(x>700)return 0;
    return (x/xp)**5*Math.expm1(xp)/Math.expm1(x);
  }
  function cmb(){
    if(!exists('cmb-log'))return;
    const v=+$('cmb-log').value,r=10**v,T=T0*r,peak=2.897771955e-3/T*1e6;
    $('range-cmb').textContent=fmt(v);
    const ax=axes({xmin:-7,xmax:5,ymax:1.12,xticks:[-7,-5,-3,-1,1,3,5],yticks:[0,.25,.5,.75,1],xlabel:'Wavelength λ [μm], logarithmic: tick labels are log₁₀(λ/μm)',ylabel:'Bλ / its own peak',height:330});
    let s=ax.s+legend([['Selected epoch','#2457c5'],['Today (also normalized)','#94a3b8']],80,20);
    const p=[],p0=[];for(let i=0;i<=480;i++){const lx=-7+12*i/480,l=10**lx;p.push([ax.X(lx),ax.Y(planckShape(l,T))]);p0.push([ax.X(lx),ax.Y(planckShape(l,T0))]);}
    s+=polyline(p0,'#94a3b8',1.7,'stroke-dasharray="5 4"')+polyline(p,'#2457c5',2.5);
    const lp=Math.log10(peak);s+=line(ax.X(lp),ax.Y(0),ax.X(lp),ax.Y(1),'#c7d2fe','stroke-dasharray="4 4"')+circle(ax.X(lp),ax.Y(1),4,'#2457c5');
    plot('cmb',s,330,`At redshift ${fmt(r-1)}, the CMB temperature is ${fmt(T)} kelvin and the wavelength-spectrum peak is ${peak.toPrecision(4)} micrometres. Peaks are normalized separately.`);
    output('cmb-z',r<1000?fmt(r-1,2):sci(r-1));output('cmb-t',T<1e5?`${fmt(T,1)} K`:`${sci(T)} K`);output('cmb-peak',peak>=.01?`${fmt(peak,3)} μm`:`${sci(peak)} μm`);output('cmb-u',sci(r**4));
    summary('cmb',`1 + z = ${sci(r)}. T = ${T<1e5?fmt(T,1):sci(T)} K. Both plotted curves have unit peak height by design; the actual energy density is ${sci(r**4)} times today's.`);
  }

  // 4. Distances from the same expansion integral.
  const horizonCache=horizons();
  function distances(){
    if(!exists('distances-z'))return;
    const z=+$('distances-z').value; $('range-distances').textContent=fmt(z);
    const ax=axes({xmax:10,ymax:120,xticks:[0,2,4,6,8,10],yticks:[0,30,60,90,120],xlabel:'Redshift z',ylabel:'Distance [Gpc]',height:350});
    let s=ax.s+legend([['dL','#2457c5'],['DC','#7c3aed'],['dA','#059669']],80,20);
    const paths=[[],[],[]];
    for(let i=0;i<=200;i++){const zz=10*i/200,d=comovingGpc(zz);paths[0].push([ax.X(zz),ax.Y(d*(1+zz))]);paths[1].push([ax.X(zz),ax.Y(d)]);paths[2].push([ax.X(zz),ax.Y(d/(1+zz))]);}
    s+=polyline(paths[0],'#2457c5')+polyline(paths[1],'#7c3aed')+polyline(paths[2],'#059669');
    const d=comovingGpc(z),dl=d*(1+z),da=d/(1+z);
    s+=line(ax.X(z),ax.t,ax.X(z),ax.Y(0),'#94a3b8','stroke-dasharray="4 4"');
    [[dl,'#2457c5'],[d,'#7c3aed'],[da,'#059669']].forEach(([y,c])=>s+=circle(ax.X(z),ax.Y(y),4,c));
    plot('distances',s,350,`At z ${fmt(z)}, comoving distance ${fmt(d)} Gpc, luminosity distance ${fmt(dl)} Gpc, and angular-diameter distance ${fmt(da)} Gpc.`);
    output('dist-dc',`${fmt(d,3)} Gpc`);output('dist-dl',`${fmt(dl,3)} Gpc`);output('dist-da',`${fmt(da,3)} Gpc`);output('dist-time',`${fmt(lookbackGyr(z),3)} Gyr`);output('dist-v',fmt(d/(C/H0/1000),3));output('dist-horizons',`${fmt(horizonCache.particle*3.261563777,1)} / ${fmt(horizonCache.event*3.261563777,1)} Gly`);
    summary('distances',`At z = ${fmt(z)}, light has travelled for ${fmt(lookbackGyr(z))} Gyr. The present proper separation is ${fmt(d)} Gpc, not c times the lookback time. The present recession rate is ${fmt(d/(C/H0/1000))} c.`);
  }

  // 5. Transparent synthetic Hubble-law regression.
  let selectedRows=DATA;
  function hubble(){
    if(!exists('hubble-cut'))return;
    const cut=+$('hubble-cut').value;selectedRows=DATA.filter(r=>r.z>=cut);
    const f=fitHubble(selectedRows),show=$('hubble-errors').checked;
    const ax=axes({xmax:650,ymax:45000,xticks:[0,100,200,300,400,500,600],yticks:[0,10000,20000,30000,40000],xlabel:'Independent teaching distance D [Mpc]',ylabel:'cz [km s⁻¹]',height:350});
    let s=ax.s+legend([['Included','#2457c5'],['Excluded','#cbd5e1'],['Origin-constrained fit','#b45309']],80,20);
    s+=polyline([[ax.X(0),ax.Y(0)],[ax.X(650),ax.Y(f.h*650)]],'#b45309',2);
    for(const r of DATA){const x=ax.X(r.distance_mpc),y=ax.Y(r.velocity_km_s),inc=r.z>=cut;
      if(inc&&show)s+=line(x,ax.Y(r.velocity_km_s-200),x,ax.Y(r.velocity_km_s+200),'#64748b','stroke-width="1.2"');
      s+=`<circle cx="${x}" cy="${y}" r="4" fill="${inc?'#2457c5':'#cbd5e1'}"><title>${esc(r.id)}: z=${r.z}, D=${r.distance_mpc} Mpc, cz=${r.velocity_km_s} km/s</title></circle>`;
    }
    plot('hubble',s,350,`Synthetic data: ${f.n} galaxies included, fitted Hubble constant ${fmt(f.h)} kilometres per second per megaparsec. This is not real survey data.`);
    output('hub-h',fmt(f.h,2));output('hub-err',`±${fmt(f.err,2)}`);output('hub-n',String(f.n));output('hub-rms',`${fmt(f.rms,1)} km s⁻¹`);
    summary('hubble',`Synthetic-data fit: H₀ = ${fmt(f.h,2)} ± ${fmt(f.err,2)} km s⁻¹ Mpc⁻¹ (formal statistical error only), using ${f.n} galaxies. The generating value was 72; this is not an observational result.`);
    const tbody=$('hubble-table-body');if(tbody)tbody.innerHTML=DATA.map(r=>`<tr class="${r.z>=cut?'':'excluded-row'}"><td>${esc(r.id)}</td><td>${r.z.toFixed(3)}</td><td>${r.distance_mpc.toFixed(2)}</td><td>${r.velocity_km_s.toFixed(1)}</td><td>200</td></tr>`).join('');
  }
  function addDataTable(){
    const lab=$('lab-hubble');if(!lab||$('hubble-table-body'))return;
    const details=document.createElement('details');details.className='lab-data';
    details.innerHTML='<summary>View the synthetic catalogue and uncertainties</summary><div class="table-scroll"><table><caption>Fixed teaching perturbations; not a published survey catalogue.</caption><thead><tr><th>ID</th><th>z</th><th>D [Mpc]</th><th>cz [km/s]</th><th>σᵥ [km/s]</th></tr></thead><tbody id="hubble-table-body"></tbody></table></div>';
    lab.querySelector('.lab-prompt').before(details);
  }
  function exportCSV(){
    const keys=['id','z','distance_mpc','velocity_km_s','sigma_velocity_km_s'];
    const csv=keys.join(',')+'\n'+selectedRows.map(r=>keys.map(k=>r[k]).join(',')).join('\n');
    const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
    const a=document.createElement('a');a.href=url;a.download='synthetic-hubble-selected.csv';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  function reset(key){
    stopAnimation();
    if(key==='expansion')$('expansion-a').value='1';
    if(key==='dynamics'){$('dynamics-om').value='.3';$('dynamics-h0').value='70';}
    if(key==='cmb')$('cmb-log').value='3.0378';
    if(key==='distances')$('distances-z').value='1';
    if(key==='hubble'){$('hubble-cut').value='0';$('hubble-errors').checked=true;}
    ({expansion,dynamics,cmb,distances,hubble}[key])();
  }
  function init(){
    if(!exists('lab-expansion'))return;
    addDataTable();
    ['expansion-a','dynamics-om','dynamics-h0','cmb-log','distances-z'].forEach(id=>$(id).addEventListener('input',({'expansion-a':expansion,'dynamics-om':dynamics,'dynamics-h0':dynamics,'cmb-log':cmb,'distances-z':distances})[id]));
    $('hubble-cut').addEventListener('change',hubble);$('hubble-errors').addEventListener('change',hubble);$('hubble-export').addEventListener('click',exportCSV);
    document.querySelectorAll('[data-reset]').forEach(b=>b.addEventListener('click',()=>reset(b.dataset.reset)));
    document.querySelectorAll('[data-preset]').forEach(b=>b.addEventListener('click',()=>{stopAnimation();$('dynamics-om').value=b.dataset.preset==='eds'?'1':'.3';$('dynamics-h0').value='70';dynamics();}));
    document.querySelectorAll('[data-cmb]').forEach(b=>b.addEventListener('click',()=>{$('cmb-log').value=b.dataset.cmb;cmb();}));
    $('expansion-play').addEventListener('click',()=>{if(animation){stopAnimation();return;}if(+$('expansion-a').value>=1.999)$('expansion-a').value='.5';$('expansion-play').textContent='Pause animation';lastTime=0;animation=requestAnimationFrame(animate);});
    document.addEventListener('visibilitychange',()=>{if(document.hidden)stopAnimation();});
    expansion();dynamics();cmb();distances();hubble();
    document.documentElement.dataset.cosmologyReady='true';
  }
  window.CosmologyLabs={E,comovingGpc,lookbackGyr,ageGyr,horizons,fitHubble,planckShape,data:DATA,version:'1.0.0'};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
