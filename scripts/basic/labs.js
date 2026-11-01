/* Original MAIS PAC Basic Astrophysics experiments. SVG only; no network requests. */
(() => {
'use strict';
const $=id=>document.getElementById(id), NS='http://www.w3.org/2000/svg';
const PI=Math.PI, SIGMA=5.670374419e-8, R=8.314462618, C=299792.458, V0=29.7846918;
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const fmt=(x,n=2)=>Number.isFinite(x)?x.toFixed(n):'—';
const sci=(x,n=3)=>x===0?'0':x.toExponential(n).replace('e+',' × 10^').replace('e-',' × 10⁻').replace(/10⁻(\d+)/,(_,d)=>'10⁻'+d.split('').map(c=>'⁰¹²³⁴⁵⁶⁷⁸⁹'[+c]).join(''));
const value=id=>Number($(id).value);
const out=(key,k,v)=>{const e=$(`out-${key}-${k}`);if(e)e.textContent=v;};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=(x,y,s,extra='')=>`<text x="${x}" y="${y}" fill="#526079" font-size="12" ${extra}>${esc(s)}</text>`;
const line=(x1,y1,x2,y2,col='#cbd5e1',extra='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" ${extra}/>`;
const path=(pts,col='#2457c5',extra='')=>`<polyline points="${pts.filter(p=>p.every(Number.isFinite)).map(p=>p.map(v=>v.toFixed(2)).join(',')).join(' ')}" fill="none" stroke="${col}" stroke-width="2.7" ${extra}/>`;
const dot=(x,y,r=6,col='#7c3aed')=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${col}"/>`;
function draw(key,body){const e=$('plot-'+key);if(e)e.innerHTML='<title>'+esc(key)+' interactive vector plot</title>'+body;}
function summary(key,s){$('summary-'+key).textContent=s;}
function axes(xlab,ylab){return line(65,270,640,270)+line(65,270,65,30)+text(350,313,xlab,'text-anchor="middle"')+text(20,22,ylab);}
function orbitModel(a,e,m){const q=Math.sqrt(1-e*e);return {period:Math.sqrt(a**3/m),rp:a*(1-e),ra:a*(1+e),vp:V0*Math.sqrt(m/a*(1+e)/(1-e)),va:V0*Math.sqrt(m/a*(1-e)/(1+e)),energy:-(V0**2)*m/(2*a)};}
function initOrbit(){
 let phase=0,playing=!matchMedia('(prefers-reduced-motion: reduce)').matches,last=0;
 function update(){const a=value('orbit-a'),e=value('orbit-e'),m=value('orbit-m'),r=orbitModel(a,e,m);
  [['period',fmt(r.period,3)+' yr'],['rp',fmt(r.rp,3)+' AU'],['ra',fmt(r.ra,3)+' AU'],['vp',fmt(r.vp,2)+' km/s'],['va',fmt(r.va,2)+' km/s'],['energy',fmt(r.energy,1)+' km²/s²']].forEach(([k,v])=>out('orbit',k,v));
  const scale=Math.min(250/(a*(1+e)),235/(a*(1-e)),115/(a*Math.sqrt(1-e*e))),cx=350,cy=160;
  let E=phase;for(let i=0;i<10;i++)E-=(E-e*Math.sin(E)-phase)/(1-e*Math.cos(E));
  const x=cx+a*(Math.cos(E)-e)*scale,y=cy-a*Math.sqrt(1-e*e)*Math.sin(E)*scale;
  let b=`<ellipse cx="${cx-a*e*scale}" cy="${cy}" rx="${a*scale}" ry="${a*Math.sqrt(1-e*e)*scale}" fill="#eff6ff" stroke="#2457c5" stroke-width="2"/>`;
  b+=line(cx,cy,x,y,'#94a3b8')+dot(cx,cy,12,'#f59e0b')+dot(x,y,7)+text(cx,cy+32,'focus','text-anchor="middle"')+text(340,24,'Two-body relative orbit · animation slowed','text-anchor="middle" font-weight="700"');
  b+=text(340,313,'rₚ = a(1 − e)        rₐ = a(1 + e)        T² = a³/M (AU, yr, M☉)','text-anchor="middle"');draw('orbit',b);
  summary('orbit',`At fixed total mass and semimajor axis, eccentricity changes the shape and speed range but not the period. Current period: ${fmt(r.period,3)} years.`);
  $('orbit-play').textContent=playing?'Pause orbit':'Animate orbit';
 }
 function loop(t){if(!last)last=t;const dt=Math.min((t-last)/1000,.05);last=t;if(playing){const r=orbitModel(value('orbit-a'),value('orbit-e'),value('orbit-m'));phase=(phase+dt*.7/r.period)%(2*PI);update();}requestAnimationFrame(loop);}
 ['orbit-a','orbit-e','orbit-m'].forEach(id=>$(id).addEventListener('input',()=>{$('range-'+id).textContent=$(id).value;update();}));
 $('orbit-play').addEventListener('click',()=>{playing=!playing;update();});
 document.querySelector('[data-reset="orbit"]').addEventListener('click',()=>{[['orbit-a',1],['orbit-e',.6],['orbit-m',1]].forEach(([id,v])=>{$(id).value=v;$('range-'+id).textContent=v;});phase=0;update();});update();requestAnimationFrame(loop);
}
const peakWavelength=T=>2.897771955e-3/T;
function planckShape(um,T){const lp=peakWavelength(T)*1e6,xp=4.965114231744276,x=14387.76877/(um*T);return (lp/um)**5*Math.expm1(xp)/Math.expm1(x);}
function initBlackbody(){
 function update(){const T=value('bb-t'),r=value('bb-r'),lp=peakWavelength(T)*1e6,flux=SIGMA*T**4,lum=r*r*(T/5772)**4;
  [['peak',fmt(lp,3)+' μm'],['flux',sci(flux)+' W/m²'],['lum',fmt(lum,3)+' L☉'],['photon',fmt(1.239841984/lp,3)+' eV']].forEach(([k,v])=>out('blackbody',k,v));
  let b=axes('Wavelength (μm)','Relative Bλ');for(let l=0;l<=3;l+=.5){const x=65+l/3*575;b+=line(x,270,x,275)+text(x,292,fmt(l,1),'text-anchor="middle"');}
  for(const [temp,col,extra] of [[5772,'#94a3b8','stroke-dasharray="6 5"'],[T,'#2457c5','']]){const pts=[];for(let i=0;i<=300;i++){const l=.03+i*2.97/300;pts.push([65+l/3*575,270-215*planckShape(l,temp)]);}b+=path(pts,col,extra);}
  b+=text(470,48,`${T} K`,'font-weight="700"')+text(470,69,'5772 K reference')+text(340,15,'Each curve normalized to its own peak','text-anchor="middle"');draw('blackbody',b);
  summary('blackbody',`L/L☉ = (R/R☉)²(T/5772 K)⁴. The plotted photon energy is hc/λ_peak, not the mean photon energy of the spectrum.`);
 }
 ['bb-t','bb-r'].forEach(id=>$(id).addEventListener('input',()=>{$('range-'+id).textContent=$(id).value;update();}));document.querySelector('[data-reset="blackbody"]').addEventListener('click',()=>{[['bb-t',5800],['bb-r',1]].forEach(([id,v])=>{$(id).value=v;$('range-'+id).textContent=v;});update();});update();
}
function gasModel(process,r){const n=1,T1=300,P1=1e5,V1=n*R*T1/P1,Cv=1.5*R,gamma=5/3;let T2,P2,V2,W;
 if(process==='isochoric'){V2=V1;P2=P1*r;T2=T1*r;W=0;}
 else {V2=V1*r;if(process==='isothermal'){T2=T1;P2=P1/r;W=n*R*T1*Math.log(r);}else if(process==='isobaric'){P2=P1;T2=T1*r;W=P1*(V2-V1);}else{T2=T1*r**(1-gamma);P2=P1*r**(-gamma);W=n*Cv*(T1-T2);}}
 const dU=n*Cv*(T2-T1);return {T2,P2,V2,W,dU,Q:dU+W};
}
function initGas(){
 function update(){const proc=$('gas-process').value,r=value('gas-r'),m=gasModel(proc,r);
  [['state',fmt(m.T2,1)+' K'],['pressure',fmt(m.P2/1000,2)+' kPa'],['work',fmt(m.W,1)+' J'],['heat',fmt(m.Q,1)+' J'],['internal',fmt(m.dU,1)+' J'],['volume',fmt(m.V2*1000,2)+' L']].forEach(([k,v])=>out('gas',k,v));
  const vmax=Math.max(m.V2,24.94/1000)*1.15,pmax=Math.max(m.P2,1e5)*1.15,X=v=>65+v/vmax*560,Y=p=>270-p/pmax*225;
  let b=axes('Volume (L)','Pressure (kPa)'),pts=[];for(let i=0;i<=100;i++){const q=1+(r-1)*i/100;let V,p;if(proc==='isochoric'){V=m.V2;p=1e5*q;}else{V=24.943387854e-3*q;p=proc==='isothermal'?1e5/q:proc==='isobaric'?1e5:1e5*q**(-5/3);}pts.push([X(V),Y(p)]);}
  b+=`<path d="M${pts[0][0]},270 L${pts.map(p=>p.join(',')).join(' L')} L${pts.at(-1)[0]},270 Z" fill="#dbeafe" fill-opacity=".65"/>`+path(pts)+dot(...pts[0],5,'#059669')+dot(...pts.at(-1),6)+text(340,17,'Shaded area = work done by the gas','text-anchor="middle"');
  for(let i=0;i<=4;i++){const v=vmax*i/4,p=pmax*i/4;b+=text(X(v),292,fmt(v*1000,0),'text-anchor="middle"')+text(58,Y(p)+4,fmt(p/1000,0),'text-anchor="end"');}draw('gas',b);
  summary('gas',`First-law check: Q − W = ${fmt(m.Q-m.W,1)} J, equal to ΔU = ${fmt(m.dU,1)} J. Monatomic gas: Cᵥ = 3R/2, γ = 5/3.`);
 }
 ['gas-process','gas-r'].forEach(id=>$(id).addEventListener('input',()=>{if($('range-'+id))$('range-'+id).textContent=$(id).value;update();}));document.querySelector('[data-reset="gas"]').addEventListener('click',()=>{$('gas-process').value='isothermal';$('gas-r').value=2;$('range-gas-r').textContent='2';update();});update();
}
function spectrumModel(lambda,v,T,res){const beta=v/C,center=lambda*Math.sqrt((1+beta)/(1-beta)),mass=(lambda===589?22.98977:1.00784)*1.6605390666e-27,sv=Math.sqrt(1.380649e-23*T/mass),thermal=2.354820045*center*sv/(C*1000),instrument=center/res,total=Math.hypot(thermal,instrument);return {center,shift:center-lambda,sv,thermal,instrument,total};}
function initSpectrum(){
 function update(){const l=value('spec-line'),m=spectrumModel(l,value('spec-v'),value('spec-t'),value('spec-r'));
  [['lambda',fmt(m.center,4)+' nm'],['shift',fmt(m.shift,4)+' nm'],['thermal',fmt(m.thermal,4)+' nm'],['instrument',fmt(m.instrument,4)+' nm'],['total',fmt(m.total,4)+' nm'],['velocity',fmt(m.sv/1000,2)+' km/s']].forEach(([k,v])=>out('spectrum',k,v));
  const half=Math.max(.22,m.total*4),lo=m.center-half,hi=m.center+half,sig=m.total/2.354820045,X=w=>65+(w-lo)/(hi-lo)*575;
  let b=axes('Wavelength (nm)','Relative intensity'),pts=[];for(let i=0;i<=350;i++){const w=lo+(hi-lo)*i/350;pts.push([X(w),70+170*Math.exp(-.5*((w-m.center)/sig)**2)]);}b+=path(pts);
  if(l>=lo&&l<=hi)b+=line(X(l),40,X(l),270,'#059669','stroke-dasharray="5 4"')+text(X(l),35,'rest','text-anchor="middle"');
  b+=line(X(m.center),45,X(m.center),270,'#7c3aed','stroke-dasharray="3 4"')+text(X(m.center),25,'observed centre','text-anchor="middle"');for(let i=0;i<=4;i++){const w=lo+(hi-lo)*i/4;b+=text(X(w),292,fmt(w,3),'text-anchor="middle"');}draw('spectrum',b);
  summary('spectrum','Thermal broadening uses H atoms for the hydrogen lines and Na atoms for Na D. Gaussian widths combine in quadrature; the instrument does not change the gas temperature.');
 }
 ['spec-line','spec-v','spec-t','spec-r'].forEach(id=>$(id).addEventListener('input',()=>{if($('range-'+id))$('range-'+id).textContent=$(id).value;update();}));document.querySelector('[data-reset="spectrum"]').addEventListener('click',()=>{[['spec-line',656.28],['spec-v',100],['spec-t',10000],['spec-r',20000]].forEach(([id,v])=>{$(id).value=v;if($('range-'+id))$('range-'+id).textContent=v;});update();});update();
}
const ISOTOPES={c14:{half:5730*31557600,unit:'yr',years:5730},i131:{half:8.02*86400,unit:'d',years:8.02/365.25},co60:{half:5.27*31557600,unit:'yr',years:5.27}};
function decayModel(n){return {fraction:2**(-n),remaining:1e12*2**(-n)};}
function initDecay(){
 function update(){const key=$('decay-isotope').value,n=value('decay-n'),iso=ISOTOPES[key],m=decayModel(n),lambda=Math.log(2)/iso.half,A=lambda*m.remaining;
  const activity=A>=1e6?fmt(A/1e6,3)+' MBq':A>=1000?fmt(A/1000,3)+' kBq':fmt(A,4)+' Bq';
  [['remaining',sci(m.remaining)],['fraction',fmt(m.fraction*100,3)+'%'],['activity',activity],['elapsed',fmt(n*iso.years,n*iso.years<10?3:1)+' '+iso.unit],['lambda',sci(lambda)+' s⁻¹'],['mean',fmt(1/Math.log(2),3)+' half-lives']].forEach(([k,v])=>out('decay',k,v));
  let b=axes('Elapsed half-lives','Surviving fraction'),pts=[];for(let i=0;i<=240;i++){const t=i/30;pts.push([65+t/8*570,270-220*2**(-t)]);}b+=path(pts);for(let t=0;t<=8;t++){const x=65+t/8*570;b+=line(x,270,x,275)+text(x,292,String(t),'text-anchor="middle"');}b+=dot(65+n/8*570,270-220*m.fraction,7)+text(350,20,'N/N₀ = 2⁻ⁿ; activity follows the same curve','text-anchor="middle"');draw('decay',b);
  summary('decay','A half-life is not a mean lifetime: τ = T½/ln 2 ≈ 1.443 T½. The activity is calculated in SI units from A = λN.');
 }
 ['decay-isotope','decay-n'].forEach(id=>$(id).addEventListener('input',()=>{if($('range-'+id))$('range-'+id).textContent=$(id).value;update();}));document.querySelector('[data-reset="decay"]').addEventListener('click',()=>{$('decay-isotope').value='c14';$('decay-n').value=1;$('range-decay-n').textContent='1';update();});update();
}
const init={orbit:initOrbit,blackbody:initBlackbody,gas:initGas,spectrum:initSpectrum,decay:initDecay};
for(const [key,start] of Object.entries(init))if($('plot-'+key))start();
window.BasicLabs={orbitModel,peakWavelength,planckShape,gasModel,spectrumModel,decayModel};
document.documentElement.dataset.basicReady='true';
})();
