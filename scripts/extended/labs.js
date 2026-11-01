/* Original MAIS PAC extended-curriculum experiments (07–10). SVG only; no network requests. */
(() => {
'use strict';
const $=id=>document.getElementById(id), PI=Math.PI, D2R=PI/180, R2D=180/PI;
const value=id=>Number($(id).value);
const fmt=(x,n=2)=>Number.isFinite(x)?x.toFixed(n):'—';
const sci=(x,n=2)=>Number.isFinite(x)?x.toExponential(n):'—';
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const out=(key,k,v)=>{const e=$(`out-${key}-${k}`);if(e)e.textContent=v;};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=(x,y,s,extra='')=>`<text x="${x}" y="${y}" fill="#526079" font-size="12" ${extra}>${esc(s)}</text>`;
const line=(x1,y1,x2,y2,col='#cbd5e1',extra='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" ${extra}/>`;
const path=(pts,col='#2457c5',extra='')=>`<polyline points="${pts.filter(p=>p.every(Number.isFinite)).map(p=>p.map(v=>v.toFixed(2)).join(',')).join(' ')}" fill="none" stroke="${col}" stroke-width="2.6" ${extra}/>`;
const dot=(x,y,r=5,col='#7c3aed')=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${col}"/>`;
function draw(key,body){const e=$('plot-'+key);if(e)e.innerHTML='<title>'+esc(key)+' interactive vector plot</title>'+body;}
function summary(key,s){const e=$('summary-'+key);if(e)e.textContent=s;}
function axes(xlab,ylab){return line(60,275,645,275)+line(60,275,60,25)+text(350,315,xlab,'text-anchor="middle"')+text(18,20,ylab);}
function bind(key,update){
 const section=$('lab-'+key);if(!section)return;
 const controls=[...section.querySelectorAll('input,select')];
 const defaults=controls.map(el=>({el,value:el.value,checked:el.checked}));
 controls.forEach(el=>el.addEventListener('input',()=>{const r=$('range-'+el.id);if(r)r.textContent=el.value;update();}));
 const reset=section.querySelector('[data-reset]');if(reset)reset.addEventListener('click',()=>{defaults.forEach(d=>{d.el.value=d.value;if(d.el.type==='checkbox')d.el.checked=d.checked;const r=$('range-'+d.el.id);if(r)r.textContent=d.el.value;});update();});
 update();
}
function seeded(seed){let s=seed>>>0;return()=>{s=(1664525*s+1013904223)>>>0;return s/4294967296;};}
function normals(n,seed){const rnd=seeded(seed),a=[];for(let i=0;i<n;i++){const u=Math.max(rnd(),1e-9),v=rnd();a.push(Math.sqrt(-2*Math.log(u))*Math.cos(2*PI*v));}return a;}

/* 07.01 windows */
const peakUm=T=>2897.771955/T;
function bandOf(um){if(um<0.01)return 'X-ray';if(um<0.4)return 'Ultraviolet';if(um<0.7)return 'Visible';if(um<2.5)return 'Near-infrared';if(um<25)return 'Mid-infrared';return 'Far-infrared';}
function accessOf(um){if(um>=0.32&&um<=1.05)return 'Good optical window';if(um>1.05&&um<=2.4)return 'Near-IR windows (site dependent)';if(um>2.4&&um<=25)return 'Partial / high dry sites';return 'Poor from the ground';}
function initWindows(){bind('windows',()=>{const T=value('win-t'),z=value('win-z'),rest=peakUm(T),obs=rest*(1+z),E=1.239841984/obs;
 out('windows','rest',fmt(rest,3)+' μm');out('windows','obs',fmt(obs,3)+' μm');out('windows','band',bandOf(obs));out('windows','photon',fmt(E,3)+' eV');out('windows','access',accessOf(obs));
 let b=axes('Observed wavelength (μm)','Relative thermal shape');const max=Math.max(3,obs*3),X=um=>60+um/max*585,pts=[];for(let i=1;i<=300;i++){const um=max*i/300,xp=14387.77/(rest*T),x=14387.77/(um/(1+z)*T);const y=Math.pow(obs/um,5)*Math.expm1(xp)/Math.expm1(x);pts.push([X(um),275-220*clamp(y,0,1)]);}b+=path(pts);
 b+=`<rect x="${X(0.4)}" y="30" width="${X(0.7)-X(0.4)}" height="245" fill="#22c55e" opacity="0.10"/>`+text(X(0.55),45,'visible','text-anchor="middle"');draw('windows',b);
 summary('windows','The peak is a guide, not the whole spectrum. Redshift moves every wavelength by the same factor (1+z); atmospheric access depends on the observed wavelength.');});}

/* 07.02 telescope */
function telescopeModel(D,f,e,seeing){const fr=f/D,mag=f/e,pupil=D/mag,ray=138.4/D,eff=Math.max(ray,seeing),lim=2+5*Math.log10(D);return {fr,mag,pupil,ray,eff,lim};}
function initTelescope(){bind('telescope',()=>{const m=telescopeModel(value('tel-d'),value('tel-f'),value('tel-e'),value('tel-s'));
 out('telescope','fr','f/'+fmt(m.fr,1));out('telescope','mag',fmt(m.mag,1)+'×');out('telescope','pupil',fmt(m.pupil,2)+' mm');out('telescope','ray',fmt(m.ray,2)+'″');out('telescope','eff',fmt(m.eff,2)+'″');out('telescope','lim',fmt(m.lim,1));
 let b=axes('Angular radius (arcsec)','Relative intensity');const sig=m.eff/2.355,max=Math.max(3,m.eff*3),pts=[];for(let i=0;i<=300;i++){const r=max*i/300;pts.push([60+r/max*585,275-230*Math.exp(-.5*(r/sig)**2)]);}b+=path(pts)+text(350,20,'Effective PSF width ≈ '+fmt(m.eff,2)+'″','text-anchor="middle"');draw('telescope',b);
 summary('telescope','Magnification = focal length / eyepiece focal length. Exit pupil = aperture / magnification. The atmosphere usually sets the practical resolution.');});}

/* 08.01 root */
function kepler(M,e,method){const f=E=>E-e*Math.sin(E)-M;let E=method==='bisect'?PI:M,lo=0,hi=2*PI,it=0,last=NaN;
 for(let i=0;i<100;i++){let next;if(method==='newton'){next=E-f(E)/(1-e*Math.cos(E));}else if(method==='bisect'){next=(lo+hi)/2;if(f(lo)*f(next)<=0)hi=next;else lo=next;}else{next=M+e*Math.sin(E);}last=Math.abs(next-E);E=next;it=i+1;if(last<1e-12&&method!=='bisect')break;if(method==='bisect'&&hi-lo<1e-12)break;}
 return {E,res:f(E),iter:it,err:last};}
function initRoot(){bind('root',()=>{const M=value('root-m')*D2R,e=value('root-e'),method=$('root-method').value,r=kepler(M,e,method);
 out('root','E',fmt(r.E*R2D,4)+'°');out('root','res',sci(r.res));out('root','iter',String(r.iter));out('root','err',sci(r.err));
 let b=axes('E (rad)','M(E) − M');const pts=[];for(let i=0;i<=300;i++){const E=2*PI*i/300;pts.push([60+E/(2*PI)*585,150-(E-e*Math.sin(E)-M)*35]);}b+=path(pts)+line(60,150,645,150,'#94a3b8')+dot(60+r.E/(2*PI)*585,150,6);draw('root',b);
 summary('root','Newton uses the local slope; bisection brackets a root; fixed-point iteration repeats E = M + e sin E. Convergence is not guaranteed for every guess.');});}

/* 08.02 calculus */
function erf(x){const s=x<0?-1:1;x=Math.abs(x);const t=1/(1+0.3275911*x);const y=1-((((1.061405429*t-1.453152027)*t+1.421413741)*t-0.284496736)*t+0.254829592)*t*Math.exp(-x*x);return s*y;}
const CALC={sin:{f:x=>Math.sin(x),df:x=>Math.cos(x),int:x=>1-Math.cos(x)},gauss:{f:x=>Math.exp(-x*x),df:x=>-2*x*Math.exp(-x*x),int:x=>Math.sqrt(PI)/2*erf(x)},poly:{f:x=>x*x,df:x=>2*x,int:x=>x**3/3},lor:{f:x=>1/(1+x*x),df:x=>-2*x/(1+x*x)**2,int:x=>Math.atan(x)}};
function simpson(f,a,b,n=400){if(a===b)return 0;n+=n%2;const h=(b-a)/n;let s=f(a)+f(b);for(let i=1;i<n;i++)s+=(i%2?4:2)*f(a+i*h);return s*h/3;}
function initCalculus(){bind('calculus',()=>{const key=$('calc-f').value,x=value('calc-x'),h=value('calc-h'),c=CALC[key],df=(c.f(x+h)-c.f(x-h))/(2*h),I=simpson(c.f,0,x);
 out('calculus','f',fmt(c.f(x),4));out('calculus','df',fmt(df,4));out('calculus','exactdf',fmt(c.df(x),4));out('calculus','int',fmt(I,4));out('calculus','exactint',fmt(c.int(x),4));
 let b=axes('x','f(x)');const X=t=>60+(t+3)/6*585,Y=y=>150-y*70,pts=[],area=[];for(let i=0;i<=300;i++){const t=-3+6*i/300;pts.push([X(t),Y(c.f(t))]);}b+=path(pts);
 const n=120;for(let i=0;i<=n;i++){const t=x*i/n;area.push([X(t),Y(c.f(t))]);}if(area.length>1)b+=`<polygon points="${X(0)},${Y(0)} ${area.map(p=>p.join(',')).join(' ')} ${X(x)},${Y(0)}" fill="#2457c5" opacity="0.12"/>`;
 b+=line(X(x-1),Y(c.f(x)-c.df(x)),X(x+1),Y(c.f(x)+c.df(x)),'#7c3aed')+dot(X(x),Y(c.f(x)),6);draw('calculus',b);
 summary('calculus','The purple line is the tangent from the exact derivative. The shaded region is the signed integral from 0 to x.');});}

/* 08.03 vectors */
function vectorModel(a,ta,b,tb){const A=[a*Math.cos(ta*D2R),a*Math.sin(ta*D2R)],B=[b*Math.cos(tb*D2R),b*Math.sin(tb*D2R)],S=[A[0]+B[0],A[1]+B[1]];return {A,B,S,mag:Math.hypot(...S),dot:A[0]*B[0]+A[1]*B[1],cross:A[0]*B[1]-A[1]*B[0],angle:(a*b>0?Math.acos(clamp((A[0]*B[0]+A[1]*B[1])/(a*b),-1,1))*R2D:NaN)};}
function initVectors(){bind('vectors',()=>{const m=vectorModel(value('vec-a'),value('vec-ta'),value('vec-b'),value('vec-tb')),cx=340,cy=170,s=22;
 out('vectors','sum','('+fmt(m.S[0],2)+', '+fmt(m.S[1],2)+')');out('vectors','mag',fmt(m.mag,2));out('vectors','dot',fmt(m.dot,2));out('vectors','cross',fmt(m.cross,2));out('vectors','angle',fmt(m.angle,1)+'°');
 const P=v=>[cx+v[0]*s,cy-v[1]*s];let b=line(60,cy,645,cy)+line(cx,25,cx,300);const a=P(m.A),bb=P(m.B),ss=P(m.S);b+=`<polygon points="${cx},${cy} ${a[0]},${a[1]} ${ss[0]},${ss[1]} ${bb[0]},${bb[1]}" fill="#2457c5" opacity="0.08"/>`;
 b+=line(cx,cy,a[0],a[1],'#2457c5','stroke-width="3"')+line(cx,cy,bb[0],bb[1],'#059669','stroke-width="3"')+line(cx,cy,ss[0],ss[1],'#7c3aed','stroke-width="3"')+text(a[0]+8,a[1],'A')+text(bb[0]+8,bb[1],'B')+text(ss[0]+8,ss[1],'A+B');draw('vectors',b);
 summary('vectors','Dot product = |A||B|cos θ; cross-product z component = |A||B|sin θ. The parallelogram diagonal is the vector sum.');});}

/* 08.04 geometry */
function geometryModel(scale,len,pa){const sep=scale*len;return {sep,dra:sep*Math.sin(pa*D2R),ddec:sep*Math.cos(pa*D2R)};}
function initGeometry(){bind('geometry',()=>{const m=geometryModel(value('geo-scale'),value('geo-len'),value('geo-pa'));
 out('geometry','sep',fmt(m.sep,2)+'″');out('geometry','dra',fmt(m.dra,2)+'″');out('geometry','ddec',fmt(m.ddec,2)+'″');
 const cx=340,cy=180,L=110,dx=L*Math.sin(value('geo-pa')*D2R),dy=-L*Math.cos(value('geo-pa')*D2R);let b=line(cx,40,cx,300)+line(100,cy,600,cy)+text(cx,35,'N','text-anchor="middle"')+text(605,cy,'E')+line(cx,cy,cx+dx,cy+dy,'#7c3aed','stroke-width="3"')+dot(cx,cy,5)+dot(cx+dx,cy+dy,5);draw('geometry',b);
 summary('geometry','Position angle is measured eastward from north. Δα cos δ is the east component; Δδ is the north component.');});}

/* 08.05 stats */
function statsModel(n,sigma,outlier){const z=normals(n,42),vals=z.map(v=>10+sigma*v);if(outlier>0)vals[n-1]+=outlier;const mean=vals.reduce((a,b)=>a+b,0)/n,s=[...vals].sort((a,b)=>a-b),median=n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2,std=Math.sqrt(vals.reduce((a,v)=>a+(v-mean)**2,0)/(n-1)),sem=std/Math.sqrt(n),max=Math.max(...vals.map(v=>Math.abs(v-mean)));return {vals,mean,median,std,sem,max};}
function initStats(){bind('stats',()=>{const m=statsModel(value('stat-n'),value('stat-s'),value('stat-o'));
 out('stats','mean',fmt(m.mean,3));out('stats','median',fmt(m.median,3));out('stats','std',fmt(m.std,3));out('stats','sem',fmt(m.sem,3));out('stats','max',fmt(m.max,3));
 let b=axes('Measurement value','Count');const lo=Math.min(...m.vals)-.5,hi=Math.max(...m.vals)+.5,bins=12,counts=Array(bins).fill(0);m.vals.forEach(v=>{counts[clamp(Math.floor((v-lo)/(hi-lo)*bins),0,bins-1)]++;});const mx=Math.max(...counts);for(let i=0;i<bins;i++){const x=60+i/bins*585,w=585/bins-4,h=counts[i]/mx*220;b+=`<rect x="${x}" y="${275-h}" width="${w}" height="${h}" fill="#2457c5" opacity="0.75"/>`;}b+=line(60+(m.mean-lo)/(hi-lo)*585,30,60+(m.mean-lo)/(hi-lo)*585,275,'#7c3aed');draw('stats',b);
 summary('stats','The mean is sensitive to outliers; the median is robust. Standard error describes uncertainty in the mean, not the spread of individual readings.');});}

/* 09.01 naked eye */
const EYE_STARS=(()=>{const r=seeded(7),a=[];for(let i=0;i<220;i++){const m=6.4*Math.pow(r(),0.45);a.push({x:r()*2-1,y:r()*2-1,m});}return a;})();
function initNakedeye(){bind('nakedeye',()=>{const lim=value('eye-lim'),rot=value('eye-rot')*D2R,vis=EYE_STARS.filter(s=>s.m<=lim&&s.x*s.x+s.y*s.y<=1);
 out('nakedeye','count',String(vis.length));out('nakedeye','bright',vis.length?fmt(Math.min(...vis.map(s=>s.m)),1):'—');out('nakedeye','hand','6 fist widths');
 let b=`<circle cx="340" cy="165" r="135" fill="#0f172a"/>`;vis.forEach(s=>{const x=s.x*Math.cos(rot)-s.y*Math.sin(rot),y=s.x*Math.sin(rot)+s.y*Math.cos(rot);b+=dot(340+x*130,165+y*130,clamp(3.6-.45*s.m,0.7,3.6),'#f8fafc');});draw('nakedeye',b);
 summary('nakedeye','Star counts rise steeply toward fainter magnitudes. Light pollution reduces the limiting magnitude and removes many faint stars.');});}

/* 09.02 sky map */
const MAP_STARS=(()=>{const r=seeded(11),a=[];for(let i=0;i<90;i++)a.push({ra:r()*24,dec:-60+r()*150,m:6*Math.pow(r(),0.5)});return a;})();
function initSkymap(){bind('skymap',()=>{const lim=value('map-lim'),ra=value('map-ra'),dec=value('map-dec'),W=8,H=60;const vis=MAP_STARS.filter(s=>{let d=Math.abs(s.ra-ra);d=Math.min(d,24-d);return s.m<=lim&&d<=W/2&&Math.abs(s.dec-dec)<=H/2;});
 out('skymap','count',String(vis.length));out('skymap','bright',vis.length?fmt(Math.min(...vis.map(s=>s.m)),1):'—');out('skymap','field','8 h × 60°');
 let b=axes('RA offset (h)','Dec offset (deg)');for(let g=-4;g<=4;g+=2)b+=line(340+g/8*585,30,340+g/8*585,275,'#e2e8f0');for(let g=-30;g<=30;g+=20)b+=line(60,152-g/60*245,645,152-g/60*245,'#e2e8f0');
 vis.forEach(s=>{let d=s.ra-ra;if(d>12)d-=24;if(d<-12)d+=24;b+=dot(340+d/8*585,152-(s.dec-dec)/60*245,clamp(4-.5*s.m,1,4),'#1e3a8a');});draw('skymap',b);
 summary('skymap','Catalogues list positions and magnitudes; charts project them. A magnitude-limited chart is not the same as a volume-limited sample.');});}

/* 09.03 coordinates */
function coordModel(ra,dec,lst,lat){let H=(lst-ra)*15;H=((H+180)%360+360)%360-180;const φ=lat*D2R,δ=dec*D2R,Hr=H*D2R;const alt=Math.asin(Math.sin(φ)*Math.sin(δ)+Math.cos(φ)*Math.cos(δ)*Math.cos(Hr))*R2D;let az=Math.atan2(-Math.cos(δ)*Math.sin(Hr),Math.sin(δ)*Math.cos(φ)-Math.cos(δ)*Math.cos(Hr)*Math.sin(φ))*R2D;az=(az+360)%360;const cosH0=-Math.tan(φ)*Math.tan(δ);let state=alt>0?'Above horizon':'Below horizon';if(cosH0<-1)state='Circumpolar (always up)';else if(cosH0>1)state='Never rises';const air=alt>0?1/(Math.sin(alt*D2R)+0.50576*Math.pow(alt+6.07995,-1.6364)):NaN;return {H,alt,az,air,state};}
function initCoords(){bind('coords',()=>{const m=coordModel(value('coord-ra'),value('coord-dec'),value('coord-lst'),value('coord-lat'));
 out('coords','ha',fmt(m.H,2)+'°');out('coords','alt',fmt(m.alt,2)+'°');out('coords','az',fmt(m.az,2)+'°');out('coords','air',Number.isFinite(m.air)?fmt(m.air,2):'—');out('coords','state',m.state);
 let b=`<path d="M100 250 A240 240 0 0 1 580 250" fill="#eff6ff" stroke="#94a3b8"/>`+line(80,250,600,250)+text(340,270,'Horizon','text-anchor="middle"');const r=220,θ=m.alt*D2R,A=m.az*D2R,x=340+r*Math.cos(θ)*Math.sin(A),y=250-r*Math.sin(θ);b+=dot(x,y,7)+text(x+10,y-10,'target');draw('coords',b);
 summary('coords','Altitude and azimuth change with time and location; RA and Dec are catalogue coordinates. Airmass grows rapidly near the horizon; the lab uses the finite Kasten–Young approximation.');});}

/* 09.04 exposure */
function exposureModel(D,mag,t,sky){const area=(D/1000)**2,src=1e6*area*10**(-.4*mag)*t,skyE=1e6*area*10**(-.4*sky)*t,dark=.01*t,read=25,noise=Math.sqrt(src+skyE+dark+read),snr=src/noise;let lo=0,hi=1e5;for(let i=0;i<60;i++){const mid=(lo+hi)/2,s=1e6*area*10**(-.4*mag)*mid,n=Math.sqrt(s+1e6*area*10**(-.4*sky)*mid+.01*mid+25);if(s/n<5)lo=mid;else hi=mid;}return {src,sky:skyE,snr,t5:(lo+hi)/2};}
function initExposure(){bind('exposure',()=>{const m=exposureModel(value('exp-d'),value('exp-m'),value('exp-t'),value('exp-sky'));
 out('exposure','src',sci(m.src));out('exposure','sky',sci(m.sky));out('exposure','snr',fmt(m.snr,2));out('exposure','t5',fmt(m.t5,1)+' s');
 let b=axes('Exposure (s)','SNR');const pts=[];for(let i=0;i<=200;i++){const t=300*i/200,mm=exposureModel(value('exp-d'),value('exp-m'),t,value('exp-sky'));pts.push([60+t/300*585,275-clamp(mm.snr,0,50)/50*230]);}b+=path(pts)+line(60,275-5/50*230,645,275-5/50*230,'#94a3b8','stroke-dasharray="5 4"');draw('exposure',b);
 summary('exposure','In the source-dominated regime SNR grows as √t; in the sky-dominated regime it also grows as √t but with a smaller coefficient. Read noise matters for short exposures.');});}

/* 10.01 errors */
function errorModel(trueV,bias,sigma,n){const rand=sigma/Math.sqrt(n);return {mean:trueV+bias,rand,total:Math.hypot(bias,rand),bias};}
function initErrors(){bind('errors',()=>{const m=errorModel(value('err-true'),value('err-bias'),value('err-sig'),value('err-n'));
 out('errors','mean',fmt(m.mean,3));out('errors','rand',fmt(m.rand,3));out('errors','total',fmt(m.total,3));out('errors','bias',fmt(m.bias,3));
 let b=axes('Error component','Magnitude');const items=[['Random',m.rand,'#2457c5'],['Bias',Math.abs(m.bias),'#b45309'],['Total',m.total,'#7c3aed']],mx=Math.max(...items.map(i=>i[1]),.1);items.forEach((it,i)=>{const x=130+i*180,h=it[1]/mx*210;b+=`<rect x="${x}" y="${275-h}" width="90" height="${h}" fill="${it[2]}"/>`+text(x+45,295,it[0],'text-anchor="middle"');});draw('errors',b);
 summary('errors','Random uncertainty falls as 1/√n. A known systematic offset should be corrected, not averaged away. The RSS bar is illustrative only if the bias is treated as a standard uncertainty.');});}

/* 10.02 fit */
function fitModel(slope,noise,n,outlier){const z=normals(n,17),xs=[],ys=[];for(let i=0;i<n;i++){const x=i/(n-1)*10;xs.push(x);ys.push(slope*x+1+noise*z[i]);}if(outlier)ys[n-1]+=6;const mx=xs.reduce((a,b)=>a+b)/n,my=ys.reduce((a,b)=>a+b)/n;let sxx=0,sxy=0;for(let i=0;i<n;i++){sxx+=(xs[i]-mx)**2;sxy+=(xs[i]-mx)*(ys[i]-my);}const b=sxy/sxx,a=my-b*mx;let ssr=0,sst=0;for(let i=0;i<n;i++){ssr+=(ys[i]-a-b*xs[i])**2;sst+=(ys[i]-my)**2;}const r2=1-ssr/sst,serr=Math.sqrt(ssr/(n-2)/sxx);return {xs,ys,a,b,r2,serr};}
function initFit(){bind('fit',()=>{const m=fitModel(value('fit-slope'),value('fit-noise'),value('fit-n'),$('fit-out').checked);
 out('fit','slope',fmt(m.b,3));out('fit','intercept',fmt(m.a,3));out('fit','r2',fmt(m.r2,4));out('fit','serr',fmt(m.serr,3));
 const ymax=Math.max(1,...m.ys.map(Math.abs),Math.abs(m.a),Math.abs(m.a+m.b*10))*1.15,X=x=>60+x/10*585,Y=y=>145-y/ymax*105;let b=line(60,35,60,255)+line(60,145,645,145,'#94a3b8')+text(350,22,'Fit: y versus x','text-anchor="middle"')+line(X(0),Y(m.a),X(10),Y(m.a+m.b*10),'#7c3aed');m.xs.forEach((x,i)=>{b+=dot(X(x),Y(m.ys[i]),4,'#2457c5');});const res=m.ys.map((y,i)=>y-(m.a+m.b*m.xs[i])),rmax=Math.max(.1,...res.map(Math.abs))*1.2;b+=line(60,285,645,285,'#94a3b8')+text(350,318,'Residuals (observed − fit)','text-anchor="middle"');m.xs.forEach((x,i)=>{b+=line(X(x),285,X(x),285-res[i]/rmax*28,'#cbd5e1')+dot(X(x),285-res[i]/rmax*28,3.5,'#059669');});draw('fit',b);
 summary('fit','Least squares minimizes squared vertical residuals. R² alone can hide outliers or curvature; always inspect residuals.');});}

/* 10.03 double star */
function doubleModel(sep,pa,scale,err){return {mm:sep/scale,sep,unc:err*scale,pa};}
function initDoublestar(){bind('doublestar',()=>{const m=doubleModel(value('ds-sep'),value('ds-pa'),value('ds-scale'),value('ds-err'));
 out('doublestar','mm',fmt(m.mm,2)+' mm');out('doublestar','sep',fmt(m.sep,2)+'″');out('doublestar','unc','±'+fmt(m.unc,2)+'″');out('doublestar','pa',fmt(m.pa,0)+'°');
 const cx=300,cy=170,L=120,dx=L*Math.sin(m.pa*D2R),dy=-L*Math.cos(m.pa*D2R);let b=dot(cx,cy,8,'#f59e0b')+dot(cx+dx,cy+dy,6,'#2457c5')+line(cx,cy,cx+dx,cy+dy,'#94a3b8','stroke-dasharray="5 4"')+text(cx,cy-20,'A')+text(cx+dx,cy+dy-16,'B');draw('doublestar',b);
 summary('doublestar','Angular uncertainty = ruler uncertainty × plate scale. A smaller plate scale (arcsec/mm) reduces the angular effect of the same reading error.');});}

/* 10.04 photometry */
function photModel(depth,phase,noise,comp){const g=(p,c,w)=>Math.exp(-.5*((p-c)/w)**2);const eclipse=depth*(g(phase,0,.04)+g(phase,1,.04))+0.4*depth*g(phase,.5,.05);const trend=0.05*Math.sin(2*PI*phase);const target=eclipse+trend+noise*Math.sin(37*phase),comparison=trend+comp+noise*Math.sin(23*phase); /* deterministic synthetic ripple, not random noise */const delta=target-comparison;return {delta,model:eclipse,res:delta-eclipse,depth};}
function initPhotometry(){bind('photometry',()=>{const m=photModel(value('ph-depth'),value('ph-phase'),value('ph-noise'),value('ph-comp'));
 out('photometry','delta',fmt(m.delta,4)+' mag');out('photometry','model',fmt(m.model,4)+' mag');out('photometry','res',fmt(m.res,4)+' mag');out('photometry','depth',fmt(m.depth,3)+' mag');
 let b=axes('Orbital phase','Differential magnitude');const pts=[];for(let i=0;i<=300;i++){const p=i/300,mm=photModel(value('ph-depth'),p,value('ph-noise'),value('ph-comp'));pts.push([60+p*585,80+mm.delta*300]);}b+=path(pts)+dot(60+value('ph-phase')*585,80+m.delta*300,6,'#7c3aed');draw('photometry',b);
 summary('photometry','Differential photometry removes shared transparency trends. A constant comparison-star offset shifts the zero point but not the eclipse shape. The ripple is deterministic synthetic scatter for teaching.');});}

const init={windows:initWindows,telescope:initTelescope,root:initRoot,calculus:initCalculus,vectors:initVectors,geometry:initGeometry,stats:initStats,nakedeye:initNakedeye,skymap:initSkymap,coords:initCoords,exposure:initExposure,errors:initErrors,fit:initFit,doublestar:initDoublestar,photometry:initPhotometry};
for(const [key,start] of Object.entries(init))if($('plot-'+key))start();
window.CurriculumLabs={peakUm,bandOf,telescopeModel,kepler,CALC,simpson,vectorModel,geometryModel,statsModel,coordModel,exposureModel,errorModel,fitModel,doubleModel,photModel};
document.documentElement.dataset.curriculumReady='true';
})();
