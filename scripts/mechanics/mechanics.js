/* MAIS PAC Mechanics Playground. Original interactive SVG experiments.
   Equations are optional; the primary interface is prediction → play → explain. */
(() => {
'use strict';
const NS='http://www.w3.org/2000/svg';
const $=id=>document.getElementById(id);
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const rad=d=>d*Math.PI/180, deg=r=>r*180/Math.PI;
const fmt=(x,d=2)=>Number.isFinite(x)?Number(x).toFixed(d):'—';
function el(tag,attrs={},parent){const n=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs)){if(k==='text')n.textContent=v;else n.setAttribute(k,v);}if(parent)parent.appendChild(n);return n;}
function clear(n){while(n.firstChild)n.removeChild(n.firstChild);}
function vector(g,x,y,dx,dy,color='#2457c5',label){const len=Math.hypot(dx,dy);if(len<1)return;const ux=dx/len,uy=dy/len;el('line',{x1:x,y1:y,x2:x+dx,y2:y+dy,stroke:color,'stroke-width':3},g);const hx=x+dx,hy=y+dy,s=8;el('path',{d:`M${hx},${hy} L${hx-ux*s-uy*s*.6},${hy-uy*s+ux*s*.6} L${hx-ux*s+uy*s*.6},${hy-uy*s-ux*s*.6} Z`,fill:color},g);if(label)el('text',{x:hx+ux*10,y:hy+uy*10,fill:color,'font-size':12,'font-weight':600,text:label},g);}
function energyBars(g,x,y,items,max){const w=150,h=12;items.forEach((it,i)=>{const yy=y+i*24;el('text',{x,y:yy+10,'font-size':11,fill:'#526079',text:it.label},g);el('rect',{x:x+70,y:yy,width:w,height:h,rx:3,fill:'#eef2f7'},g);el('rect',{x:x+70,y:yy,width:clamp(it.value/max,0,1)*w,height:h,rx:3,fill:it.color},g);});}
const iconSvg=p=>`<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${p}</svg>`;
const ICON={
 pendulum:iconSvg('<path d="M4 4h16"/><path d="M12 4l5 12"/><circle cx="17" cy="17" r="3"/>'),
 projectile:iconSvg('<path d="M3 19Q10 3 21 13"/><circle cx="19" cy="17" r="3"/><circle cx="19" cy="17" r="1"/>'),
 ramp:iconSvg('<path d="M3 20h18L3 8z"/><rect x="8" y="10" width="5" height="4" transform="rotate(33 10 12)"/>'),
 cart:iconSvg('<rect x="4" y="8" width="13" height="7" rx="1"/><circle cx="7" cy="18" r="2"/><circle cx="14" cy="18" r="2"/><path d="M17 11h4m-2-2 2 2-2 2"/>'),
 spring:iconSvg('<path d="M3 12h2l2-5 3 10 3-10 3 10 2-5h3"/><rect x="18" y="9" width="3" height="6"/>'),
 collisions:iconSvg('<rect x="3" y="10" width="6" height="5"/><rect x="15" y="10" width="6" height="5"/><path d="M9 12h3m-1-1 1 1-1 1M15 12h-3m1-1-1 1 1 1"/>'),
 coaster:iconSvg('<path d="M2 18Q6 4 10 12t6 2q3-6 6 4"/><circle cx="10" cy="12" r="2"/>'),
 orbits:iconSvg('<circle cx="12" cy="12" r="3"/><ellipse cx="12" cy="12" rx="10" ry="5"/><circle cx="21" cy="10" r="1.6"/>'),
 torque:iconSvg('<path d="M3 9h18M12 9v10m-4 0h8"/><rect x="4" y="5" width="4" height="4"/><rect x="16" y="5" width="4" height="4"/>'),
 atwood:iconSvg('<circle cx="12" cy="5" r="3"/><path d="M9 5v9m6-9v6"/><rect x="6" y="14" width="6" height="5"/><rect x="15" y="11" width="6" height="5"/>'),
 rolling:iconSvg('<path d="M3 20h18M4 16l16-8"/><circle cx="13" cy="10" r="4"/><path d="M13 6v8m-4-4h8"/>'),
 cradle:iconSvg('<path d="M4 3h16M7 3v10m5-10v10m5-10v10"/><circle cx="7" cy="15" r="2"/><circle cx="12" cy="15" r="2"/><circle cx="17" cy="15" r="2"/>'),
 waves:iconSvg('<path d="M2 12q3-8 6 0t6 0 6 0"/><circle cx="8" cy="12" r="1"/><circle cx="14" cy="12" r="1"/><circle cx="20" cy="12" r="1"/>')
};

const SIMS=[];
function register(sim){SIMS.push(sim);}

/* ---------------- Pendulum ---------------- */
register({
 id:'pendulum',title:'Pendulum lab',tag:'Oscillations · featured',icon:ICON.pendulum,
 blurb:'Drag the bob, change the planet, and time the swing. Does mass matter? Does a big swing take longer?',
 hint:'Tip: drag the bob sideways and release it. Try the Moon, then try a very large angle.',
 challenge:'<strong>Challenge:</strong> On Earth, make the measured period as close as possible to 2.00 s. Then switch to the Moon and predict what happens before you look.',
 physics:`<p>For small swings, <span class="eq-line">T ≈ 2π √(L / g)</span> so the period depends on length and gravity, not mass. Large swings are slower than this simple formula predicts. Damping removes mechanical energy.</p>`,
 controls:[
  {key:'L',label:'Length',min:.2,max:3,step:.01,value:1,unit:'m'},
  {key:'g',label:'Gravity',type:'select',value:'9.81',options:[['9.81','Earth · 9.81'],['1.62','Moon · 1.62'],['3.71','Mars · 3.71'],['24.79','Jupiter · 24.79']]},
  {key:'theta0',label:'Release angle',min:5,max:170,step:1,value:35,unit:'°',reset:true},
  {key:'mass',label:'Bob mass',min:.2,max:5,step:.1,value:1,unit:'kg'},
  {key:'damping',label:'Damping',min:0,max:.5,step:.01,value:.02,unit:'s⁻¹'},
  {key:'trail',label:'Show trail',type:'check',value:true}
 ],
 readouts:[['angle','Angle'],['period','Measured period'],['smallT','Small-angle T'],['energy','Energy']],
 create(api){const p=api.params,g=el('g',{},api.stage);let th,om,t,lastCross,period,trail,prev;
  const pivot={x:400,y:62},scale=118;
  function reset(){th=rad(p.theta0);om=0;t=0;lastCross=null;period=null;trail=[];prev=th;}
  function deriv(th,om){return[om,-(p.g/p.L)*Math.sin(th)-p.damping*om];}
  function step(dt){const n=Math.max(1,Math.ceil(dt/0.004)),h=dt/n;for(let i=0;i<n;i++){const k1=deriv(th,om),k2=deriv(th+h/2*k1[0],om+h/2*k1[1]),k3=deriv(th+h/2*k2[0],om+h/2*k2[1]),k4=deriv(th+h*k3[0],om+h*k3[1]);th+=h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]);om+=h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]);t+=h;if(prev<0&&th>=0&&om>0){if(lastCross!==null)period=t-lastCross;lastCross=t;}prev=th;}const pos=bob();trail.push(pos);if(trail.length>220)trail.shift();}
  function bob(){return{x:pivot.x+p.L*scale*Math.sin(th),y:pivot.y+p.L*scale*Math.cos(th)};}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);el('line',{x1:250,y1:pivot.y,x2:550,y2:pivot.y,stroke:'#94a3b8','stroke-width':4},g);el('line',{x1:pivot.x,y1:pivot.y,x2:pivot.x,y2:pivot.y+p.L*scale+18,stroke:'#e2e8f0','stroke-dasharray':'4 5'},g);if(p.trail&&trail.length>1)el('polyline',{points:trail.map(q=>`${q.x},${q.y}`).join(' '),fill:'none',stroke:'#c7d2fe','stroke-width':2},g);const b=bob();el('line',{x1:pivot.x,y1:pivot.y,x2:b.x,y2:b.y,stroke:'#334155','stroke-width':3},g);el('circle',{cx:pivot.x,cy:pivot.y,r:6,fill:'#1e3a8a'},g);const r=12+4*Math.sqrt(p.mass);el('circle',{cx:b.x,cy:b.y,r,fill:'#2457c5',stroke:'#1e3a8a','stroke-width':2,cursor:'grab'},g);vector(g,b.x,b.y,Math.cos(th)*om*p.L*14,-Math.sin(th)*om*p.L*14,'#059669','v');const KE=.5*p.mass*(p.L*om)**2,PE=p.mass*p.g*p.L*(1-Math.cos(th));energyBars(g,20,360,[{label:'Kinetic',value:KE,color:'#2457c5'},{label:'Potential',value:PE,color:'#7c3aed'}],Math.max(1,p.mass*p.g*p.L*(1-Math.cos(rad(p.theta0)))));el('text',{x:400,y:430,'text-anchor':'middle','font-size':12,fill:'#6e767d',text:'Drag the bob · mass changes the size, not the ideal period'},g);}
  function read(){const KE=.5*p.mass*(p.L*om)**2,PE=p.mass*p.g*p.L*(1-Math.cos(th));api.out('angle',fmt(deg(th),1)+'°');api.out('period',period?fmt(period,3)+' s':'timing…');api.out('smallT',fmt(2*Math.PI*Math.sqrt(p.L/p.g),3)+' s');api.out('energy',fmt(KE+PE,2)+' J');}
  function pointer(ev){const rect=api.stage.getBoundingClientRect();const x=(ev.clientX-rect.left)/rect.width*800,y=(ev.clientY-rect.top)/rect.height*450;th=clamp(Math.atan2(x-pivot.x,y-pivot.y),-rad(175),rad(175));om=0;t=0;lastCross=null;period=null;trail=[];prev=th;render();read();}
  let dragging=false;api.stage.addEventListener('pointerdown',e=>{dragging=true;api.stage.setPointerCapture(e.pointerId);pointer(e);});api.stage.addEventListener('pointermove',e=>{if(dragging)pointer(e);});api.stage.addEventListener('pointerup',()=>dragging=false);api.stage.addEventListener('pointercancel',()=>dragging=false);
  reset();return{step,render,read,reset};}
});

/* ---------------- Projectile ---------------- */
register({
 id:'projectile',title:'Projectile launcher',tag:'Kinematics',icon:ICON.projectile,
 blurb:'Launch a ball, turn air resistance on and off, and try to hit the target.',
 hint:'The dashed ghost is the no-air prediction. The solid ball is the real run.',
 challenge:'<strong>Challenge:</strong> Hit the target with air resistance on. Which angle changes most when drag is added?',
 physics:`<p>Without drag, horizontal speed is constant and vertical acceleration is −g. With quadratic drag, acceleration also contains <span class="eq-line">−k |v| v</span>, which shortens the range and makes the descent steeper.</p>`,
 controls:[
  {key:'v0',label:'Launch speed',min:5,max:45,step:.5,value:25,unit:'m/s',reset:true},
  {key:'angle',label:'Angle',min:5,max:85,step:1,value:45,unit:'°',reset:true},
  {key:'h0',label:'Launch height',min:0,max:20,step:.5,value:5,unit:'m',reset:true},
  {key:'g',label:'Gravity',min:1,max:25,step:.1,value:9.81,unit:'m/s²',reset:true},
  {key:'drag',label:'Air drag k',min:0,max:.05,step:.001,value:0,unit:'m⁻¹',reset:true},
  {key:'newTarget',label:'New target',type:'button',action:'target'}
 ],
 readouts:[['time','Flight time'],['range','Range'],['maxh','Max height'],['score','Target']],
 create(api){const p=api.params,g=el('g',{},api.stage);let x,y,vx,vy,t,maxh,landed,trail,target=55,hit=false;
  const ox=58,oy=392,s=6.6;
  function reset(){x=0;y=p.h0;vx=p.v0*Math.cos(rad(p.angle));vy=p.v0*Math.sin(rad(p.angle));t=0;maxh=y;landed=false;trail=[];hit=false;}
  function action(a){if(a==='target'){target=20+Math.random()*65;reset();}}
  function step(dt){if(landed)return;const n=Math.max(1,Math.ceil(dt/.008)),h=dt/n;for(let i=0;i<n;i++){const v=Math.hypot(vx,vy);const ax=-p.drag*v*vx,ay=-p.g-p.drag*v*vy;vx+=ax*h;vy+=ay*h;x+=vx*h;y+=vy*h;t+=h;maxh=Math.max(maxh,y);if(y<=0&&t>.02){y=0;landed=true;hit=Math.abs(x-target)<2.5;break;}}trail.push([x,y]);if(trail.length>600)trail.shift();}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);el('line',{x1:ox,y1:oy,x2:770,y2:oy,stroke:'#94a3b8','stroke-width':2},g);for(let m=0;m<=100;m+=10){el('line',{x1:ox+m*s,y1:oy,x2:ox+m*s,y2:oy+5,stroke:'#94a3b8'},g);el('text',{x:ox+m*s,y:oy+18,'font-size':10,fill:'#6e767d','text-anchor':'middle',text:m+' m'},g);}const tx=ox+target*s;el('line',{x1:tx,y1:oy,x2:tx,y2:oy-34,stroke:'#b45309','stroke-width':3},g);el('path',{d:`M${tx},${oy-34} l22,8 l-22,8 Z`,fill:hit?'#059669':'#f59e0b'},g);el('rect',{x:tx-16,y:oy-3,width:32,height:6,rx:2,fill:hit?'#a7f3d0':'#fde68a'},g);const ghost=[];for(let tt=0;tt<8;tt+=.05){const gx=p.v0*Math.cos(rad(p.angle))*tt,gy=p.h0+p.v0*Math.sin(rad(p.angle))*tt-.5*p.g*tt*tt;if(gy<0)break;ghost.push([ox+gx*s,oy-gy*s]);}if(ghost.length>1)el('polyline',{points:ghost.map(q=>q.join(',')).join(' '),fill:'none',stroke:'#cbd5e1','stroke-width':2,'stroke-dasharray':'5 5'},g);if(trail.length>1)el('polyline',{points:trail.map(q=>`${ox+q[0]*s},${oy-q[1]*s}`).join(' '),fill:'none',stroke:'#2457c5','stroke-width':2.5},g);el('circle',{cx:ox+x*s,cy:oy-y*s,r:8,fill:hit?'#059669':'#2457c5'},g);vector(g,ox+x*s,oy-y*s,vx*3,-vy*3,'#7c3aed');el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:hit?'Target hit!':landed?'Landed — reset to try again':'In flight'},g);}
  function read(){api.out('time',fmt(t,2)+' s');api.out('range',fmt(x,2)+' m');api.out('maxh',fmt(maxh,2)+' m');api.out('score',hit?'HIT ✓':landed?'miss':'—');}
  reset();return{step,render,read,reset,action};}
});

/* ---------------- Ramp & friction ---------------- */
register({
 id:'ramp',title:'Ramp & friction',tag:'Forces',icon:ICON.ramp,
 blurb:'Tilt the ramp and apply a push. Will the block stick, slide, or stay balanced?',
 hint:'Static friction can hold the block until the downhill pull is too large.',
 challenge:'<strong>Challenge:</strong> With no push, find the angle where the block just begins to slip. Compare tan(angle) with μₛ.',
 physics:`<p>Along the slope, gravity pulls with <span class="eq-line">mg sin θ</span>. Static friction can supply up to <span class="eq-line">μₛ mg cos θ</span>; once sliding, kinetic friction is <span class="eq-line">μₖ mg cos θ</span>.</p>`,
 controls:[
  {key:'angle',label:'Ramp angle',min:0,max:60,step:1,value:20,unit:'°',reset:true},
  {key:'muS',label:'Static friction μₛ',min:0,max:1.2,step:.01,value:.5,reset:true},
  {key:'muK',label:'Kinetic friction μₖ',min:0,max:1.2,step:.01,value:.3,reset:true},
  {key:'mass',label:'Mass',min:.5,max:10,step:.1,value:2,unit:'kg',reset:true},
  {key:'F',label:'Push up slope',min:-30,max:60,step:.5,value:0,unit:'N',reset:true}
 ],
 readouts:[['status','State'],['acc','Acceleration'],['fric','Friction'],['normal','Normal force']],
 create(api){const p=api.params,g=el('g',{},api.stage);let sPos,v,a,fric,status;
  function reset(){sPos=0;v=0;a=0;fric=0;status='ready';}
  function step(dt){const th=rad(p.angle);const down=p.mass*9.81*Math.sin(th),N=p.mass*9.81*Math.cos(th),drive=down-p.F;const maxS=p.muS*N;if(Math.abs(v)<1e-4&&Math.abs(drive)<=maxS){v=0;a=0;fric=-drive;status='stuck (static)';}else{const dir=Math.abs(v)>1e-4?Math.sign(v):Math.sign(drive);fric=-dir*p.muK*N;a=(drive+fric)/p.mass;v+=a*dt;sPos+=v*dt;status=v>0?'sliding down':v<0?'moving up':'sliding';if(sPos>7){sPos=7;v=0;status='bottom';}if(sPos<0){sPos=0;v=0;status='top';}}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const th=rad(p.angle),bx=120,by=380,L=560;const tx=bx+L*Math.cos(th),ty=by-L*Math.sin(th);el('path',{d:`M${bx},${by} L${tx},${ty} L${tx},${by} Z`,fill:'#f3f6ff',stroke:'#94a3b8','stroke-width':2},g);const f=sPos/7,px=tx+(bx-tx)*f,py=ty+(by-ty)*f;const nx=-Math.sin(th),ny=-Math.cos(th);const cx=px+nx*26,cy=py+ny*26;el('rect',{x:cx-24,y:cy-24,width:48,height:48,rx:5,fill:'#2457c5',transform:`rotate(${-p.angle} ${cx} ${cy})`},g);vector(g,cx,cy,0,p.mass*9.81*2,'#334155','mg');vector(g,cx,cy,nx*p.mass*9.81*Math.cos(th)*2,ny*p.mass*9.81*Math.cos(th)*2,'#059669','N');if(Math.abs(fric)>.1)vector(g,cx,cy,-Math.cos(th)*fric*2,Math.sin(th)*fric*2,'#b45309','f');if(Math.abs(p.F)>.1)vector(g,cx,cy,Math.cos(th)*p.F*2,-Math.sin(th)*p.F*2,'#7c3aed','push');el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:status},g);}
  function read(){const th=rad(p.angle);api.out('status',status);api.out('acc',fmt(a,2)+' m/s²');api.out('fric',fmt(fric,2)+' N');api.out('normal',fmt(p.mass*9.81*Math.cos(th),2)+' N');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Newton cart ---------------- */
register({
 id:'cart',title:'Force & motion cart',tag:'Newton’s laws',icon:ICON.cart,
 blurb:'Push a cart with a steady force. Change the mass and watch acceleration respond.',
 hint:'Same force, double mass: what happens to acceleration?',
 challenge:'<strong>Challenge:</strong> Keep the force fixed. Double the mass and check whether the acceleration halves.',
 physics:`<p>Newton’s second law: <span class="eq-line">a = F_net / m</span>. Friction subtracts from the push once the cart is moving.</p>`,
 controls:[
  {key:'F',label:'Push force',min:0,max:50,step:.5,value:10,unit:'N'},
  {key:'mass',label:'Cart mass',min:.5,max:10,step:.1,value:2,unit:'kg'},
  {key:'mu',label:'Friction μ',min:0,max:.8,step:.01,value:.1}
 ],
 readouts:[['acc','Acceleration'],['vel','Speed'],['pos','Position'],['net','Net force']],
 create(api){const p=api.params,g=el('g',{},api.stage);let x,v,a,net;
  function reset(){x=0;v=0;a=0;net=0;}
  function step(dt){const fr=p.mu*p.mass*9.81;if(Math.abs(v)<1e-4&&p.F<=fr){net=0;a=0;v=0;}else{net=p.F-Math.sign(v||1)*fr;a=net/p.mass;v+=a*dt;if(v<0)v=0;x+=v*dt;}if(x>10){x=10;v=0;}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);el('line',{x1:50,y1:320,x2:750,y2:320,stroke:'#94a3b8','stroke-width':3},g);const px=70+x*66;el('rect',{x:px-35,y:270,width:70,height:45,rx:6,fill:'#2457c5'},g);el('circle',{cx:px-20,cy:320,r:10,fill:'#1e3a8a'},g);el('circle',{cx:px+20,cy:320,r:10,fill:'#1e3a8a'},g);vector(g,px-40,292,p.F*3,0,'#7c3aed','F');if(p.mu>0)vector(g,px+40,300,-p.mu*p.mass*9.81*3,0,'#b45309','friction');el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:`a = ${fmt(a,2)} m/s²`},g);}
  function read(){api.out('acc',fmt(a,2)+' m/s²');api.out('vel',fmt(v,2)+' m/s');api.out('pos',fmt(x,2)+' m');api.out('net',fmt(net,2)+' N');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Spring ---------------- */
register({
 id:'spring',title:'Spring & resonance',tag:'Oscillations',icon:ICON.spring,
 blurb:'Stretch a spring, add damping, then drive it. Find the frequency that makes it respond most.',
 hint:'Try driving near the natural frequency with low damping.',
 challenge:'<strong>Challenge:</strong> Set driving frequency close to √(k/m). What happens to the amplitude when damping is small?',
 physics:`<p>A mass on a spring obeys <span class="eq-line">m x″ + c x′ + k x = F_d cos(ω_d t)</span>. Natural angular frequency is <span class="eq-line">ω₀ = √(k/m)</span>.</p>`,
 controls:[
  {key:'m',label:'Mass',min:.2,max:5,step:.1,value:1,unit:'kg'},
  {key:'k',label:'Spring k',min:2,max:80,step:1,value:20,unit:'N/m'},
  {key:'c',label:'Damping',min:0,max:5,step:.05,value:.3,unit:'N·s/m'},
  {key:'x0',label:'Initial stretch',min:-2,max:2,step:.05,value:1.2,unit:'m',reset:true},
  {key:'Fd',label:'Drive force',min:0,max:20,step:.5,value:0,unit:'N'},
  {key:'wd',label:'Drive frequency',min:.2,max:15,step:.1,value:4.5,unit:'rad/s'}
 ],
 readouts:[['x','Displacement'],['v','Velocity'],['T','Natural period'],['E','Energy']],
 create(api){const p=api.params,g=el('g',{},api.stage);let x,v,t;
  function reset(){x=p.x0;v=0;t=0;}
  function step(dt){const n=Math.max(1,Math.ceil(dt/.005)),h=dt/n;for(let i=0;i<n;i++){const a=(-p.k*x-p.c*v+p.Fd*Math.cos(p.wd*t))/p.m;v+=a*h;x+=v*h;t+=h;}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const wall=90,eq=430,scale=90,mx=eq+x*scale;el('line',{x1:wall,y1:120,x2:wall,y2:300,stroke:'#94a3b8','stroke-width':5},g);el('line',{x1:eq,y1:120,x2:eq,y2:300,stroke:'#e2e8f0','stroke-dasharray':'4 5'},g);const coils=12,pts=[[wall,210]];for(let i=1;i<coils*2;i++){const xx=wall+(mx-wall)*i/(coils*2);pts.push([xx,210+(i%2?18:-18)]);}pts.push([mx,210]);el('polyline',{points:pts.map(q=>q.join(',')).join(' '),fill:'none',stroke:'#2457c5','stroke-width':3},g);el('rect',{x:mx-28,y:180,width:56,height:60,rx:7,fill:'#7c3aed'},g);el('text',{x:eq,y:330,'text-anchor':'middle','font-size':12,fill:'#6e767d',text:'equilibrium'},g);const E=.5*p.k*x*x+.5*p.m*v*v;energyBars(g,20,365,[{label:'Spring',value:.5*p.k*x*x,color:'#2457c5'},{label:'Kinetic',value:.5*p.m*v*v,color:'#059669'}],Math.max(1,.5*p.k*p.x0*p.x0+1));}
  function read(){api.out('x',fmt(x,2)+' m');api.out('v',fmt(v,2)+' m/s');api.out('T',fmt(2*Math.PI*Math.sqrt(p.m/p.k),2)+' s');api.out('E',fmt(.5*p.k*x*x+.5*p.m*v*v,2)+' J');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Collisions ---------------- */
register({
 id:'collisions',title:'Collision carts',tag:'Momentum',icon:ICON.collisions,
 blurb:'Send two carts together. Choose elastic, inelastic, or sticky collisions.',
 hint:'Momentum stays the same; kinetic energy may not.',
 challenge:'<strong>Challenge:</strong> Use equal masses and an elastic collision. What happens to their velocities?',
 physics:`<p>Momentum is conserved: <span class="eq-line">m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂</span>. The restitution coefficient e sets how much relative speed survives.</p>`,
 controls:[
  {key:'m1',label:'Mass 1',min:.5,max:5,step:.1,value:1,unit:'kg',reset:true},
  {key:'m2',label:'Mass 2',min:.5,max:5,step:.1,value:1,unit:'kg',reset:true},
  {key:'u1',label:'Velocity 1',min:-6,max:6,step:.1,value:3,unit:'m/s',reset:true},
  {key:'u2',label:'Velocity 2',min:-6,max:6,step:.1,value:-1,unit:'m/s',reset:true},
  {key:'e',label:'Bounciness e',min:0,max:1,step:.05,value:1,reset:true}
 ],
 readouts:[['p','Total momentum'],['ke','Kinetic energy'],['v1','Velocity 1'],['v2','Velocity 2']],
 create(api){const p=api.params,g=el('g',{},api.stage);let x1,x2,v1,v2,collided,ke0;
  function reset(){x1=-4;x2=4;v1=p.u1;v2=p.u2;collided=false;ke0=.5*p.m1*p.u1**2+.5*p.m2*p.u2**2;}
  function step(dt){x1+=v1*dt;x2+=v2*dt;if(!collided&&x1+0.6>=x2-0.6){const m1=p.m1,m2=p.m2,e=p.e;const nv1=((m1-e*m2)*v1+(1+e)*m2*v2)/(m1+m2);const nv2=((m2-e*m1)*v2+(1+e)*m1*v1)/(m1+m2);v1=nv1;v2=nv2;collided=true;x1=x2-1.2;}if(x1<-7||x2>7){/* let them leave; reset manually */}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);el('line',{x1:40,y1:300,x2:760,y2:300,stroke:'#94a3b8','stroke-width':3},g);const X=x=>400+x*50;[[x1,v1,p.m1,'#2457c5','1'],[x2,v2,p.m2,'#7c3aed','2']].forEach(([x,v,m,c,lab])=>{const w=34+8*m;el('rect',{x:X(x)-w/2,y:250,width:w,height:45,rx:6,fill:c},g);el('text',{x:X(x),y:278,'text-anchor':'middle',fill:'#fff','font-weight':700,text:lab},g);vector(g,X(x),240,v*14,0,c);});const ke=.5*p.m1*v1**2+.5*p.m2*v2**2;energyBars(g,20,360,[{label:'Momentum',value:Math.abs(p.m1*v1+p.m2*v2),color:'#2457c5'},{label:'KE now',value:ke,color:'#059669'},{label:'KE start',value:ke0,color:'#cbd5e1'}],Math.max(1,ke0,Math.abs(p.m1*p.u1+p.m2*p.u2)));el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:collided?'After collision':'Before collision'},g);}
  function read(){api.out('p',fmt(p.m1*v1+p.m2*v2,2)+' kg·m/s');api.out('ke',fmt(.5*p.m1*v1**2+.5*p.m2*v2**2,2)+' J');api.out('v1',fmt(v1,2)+' m/s');api.out('v2',fmt(v2,2)+' m/s');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Energy coaster ---------------- */
register({
 id:'coaster',title:'Energy roller coaster',tag:'Energy',icon:ICON.coaster,
 blurb:'Release a cart from a hill. Watch potential energy become kinetic energy—and heat when friction is on.',
 hint:'Can the cart reach the end if you start lower or add friction?',
 challenge:'<strong>Challenge:</strong> Find the smallest starting height that lets the cart reach the far end with friction enabled.',
 physics:`<p>Without friction, <span class="eq-line">mgh + ½mv²</span> stays constant. Friction transfers mechanical energy into thermal energy.</p>`,
 controls:[
  {key:'H',label:'Starting height',min:5,max:35,step:.5,value:25,unit:'m',reset:true},
  {key:'mu',label:'Friction',min:0,max:.15,step:.005,value:.02,reset:true},
  {key:'mass',label:'Cart mass',min:.5,max:5,step:.1,value:1,unit:'kg',reset:true}
 ],
 readouts:[['speed','Speed'],['ke','Kinetic'],['pe','Potential'],['thermal','Thermal loss']],
 create(api){const p=api.params,g=el('g',{},api.stage);let x,dir,E0,thermal,done;
  const L=100;function h(xx){return p.H*(0.55+0.45*Math.cos(2*Math.PI*xx/90))*Math.exp(-xx/180)+2;}
  function hp(xx){return (h(xx+.05)-h(xx-.05))/.1;}
  function reset(){x=0;dir=1;E0=9.81*h(0);thermal=0;done=false;}
  function step(dt){if(done)return;const slope=hp(x),ang=Math.atan(slope),cos=Math.cos(ang);const pe=9.81*h(x);let speed=Math.sqrt(Math.max(0,2*(E0-thermal-pe)));if(speed<.02){if(Math.abs(Math.sin(ang))>p.mu*cos){dir=-Math.sign(slope)||1;}else{done=true;return;}}const ds=speed*dt;thermal+=p.mu*9.81*cos*ds;x+=dir*ds*cos;if(x>=L){x=L;done=true;}if(x<0){x=0;dir=1;}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const X=xx=>60+xx*6.8,Y=hh=>390-hh*9;let d='';for(let xx=0;xx<=L;xx+=1){d+=(xx===0?'M':'L')+X(xx)+','+Y(h(xx));}el('path',{d,fill:'none',stroke:'#2457c5','stroke-width':4},g);const pe=9.81*h(x),ke=Math.max(0,E0-thermal-pe);el('circle',{cx:X(x),cy:Y(h(x))-10,r:10,fill:done?'#059669':'#7c3aed'},g);energyBars(g,20,20,[{label:'Potential',value:p.mass*pe,color:'#7c3aed'},{label:'Kinetic',value:p.mass*ke,color:'#2457c5'},{label:'Thermal',value:p.mass*thermal,color:'#b45309'}],Math.max(1,p.mass*E0));el('text',{x:20,y:130,'font-size':13,fill:'#1e3a8a','font-weight':700,text:done?(x>=L?'Reached the end!':'Stopped'):'Rolling'},g);}
  function read(){const pe=9.81*h(x),ke=Math.max(0,E0-thermal-pe);api.out('speed',fmt(Math.sqrt(2*ke),2)+' m/s');api.out('ke',fmt(p.mass*ke,1)+' J');api.out('pe',fmt(p.mass*pe,1)+' J');api.out('thermal',fmt(p.mass*thermal,1)+' J');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Orbits ---------------- */
register({
 id:'orbits',title:'Orbit builder',tag:'Gravity',icon:ICON.orbits,
 blurb:'Launch a satellite around a planet. Find circular orbit, ellipse, or escape.',
 hint:'Circular speed is the sweet spot; √2 times that is escape speed.',
 challenge:'<strong>Challenge:</strong> Set the speed factor to 1.00 for a circle. Then try 1.41. What changes?',
 physics:`<p>Gravity supplies centripetal acceleration: <span class="eq-line">v_circ = √(GM/r)</span>. Escape speed is <span class="eq-line">v_esc = √2 v_circ</span>.</p>`,
 controls:[
  {key:'GM',label:'Planet gravity GM',min:2000,max:12000,step:100,value:6000,reset:true},
  {key:'r0',label:'Starting radius',min:70,max:220,step:5,value:140,reset:true},
  {key:'vf',label:'Speed factor',min:.4,max:1.8,step:.01,value:1,reset:true}
 ],
 readouts:[['r','Radius'],['speed','Speed'],['type','Orbit'],['vc','Circular speed']],
 create(api){const p=api.params,g=el('g',{},api.stage);let pos,vel,trail,crashed,escaped;
  function reset(){const vc=Math.sqrt(p.GM/p.r0);pos=[p.r0,0];vel=[0,vc*p.vf];trail=[];crashed=false;escaped=false;}
  function acc(q){const r=Math.hypot(q[0],q[1]);return[-p.GM*q[0]/r**3,-p.GM*q[1]/r**3];}
  function step(dt){if(crashed||escaped)return;const n=Math.max(1,Math.ceil(dt/.01)),h=dt/n;for(let i=0;i<n;i++){const a1=acc(pos);const nh=[pos[0]+vel[0]*h+.5*a1[0]*h*h,pos[1]+vel[1]*h+.5*a1[1]*h*h];const a2=acc(nh);vel=[vel[0]+.5*(a1[0]+a2[0])*h,vel[1]+.5*(a1[1]+a2[1])*h];pos=nh;const r=Math.hypot(...pos);if(r<24){crashed=true;break;}if(r>900){escaped=true;break;}}trail.push([...pos]);if(trail.length>700)trail.shift();}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const cx=400,cy=225;if(trail.length>1)el('polyline',{points:trail.map(q=>`${cx+q[0]},${cy+q[1]}`).join(' '),fill:'none',stroke:'#c7d2fe','stroke-width':2},g);el('circle',{cx,cy,r:22,fill:'#1e3a8a'},g);el('circle',{cx,cy,r:30,fill:'none',stroke:'#dbe4ff'},g);if(!crashed)el('circle',{cx:cx+pos[0],cy:cy+pos[1],r:7,fill:'#059669'},g);vector(g,cx+pos[0],cy+pos[1],vel[0]*4,vel[1]*4,'#7c3aed');el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:crashed?'Crashed — reset':escaped?'Escaping!':'Orbiting'},g);}
  function read(){const r=Math.hypot(...pos),sp=Math.hypot(...vel),E=.5*sp*sp-p.GM/r;api.out('r',fmt(r,0));api.out('speed',fmt(sp,1));api.out('type',crashed?'crash':escaped?'escape':E<0?'bound':'unbound');api.out('vc',fmt(Math.sqrt(p.GM/r),1));}
  reset();return{step,render,read,reset};}
});

/* ---------------- Torque ---------------- */
register({
 id:'torque',title:'Balance & torque',tag:'Rotation',icon:ICON.torque,
 blurb:'Place masses on a seesaw. Balance it by matching turning effects, not just weights.',
 hint:'A small mass far from the pivot can balance a large mass close in.',
 challenge:'<strong>Challenge:</strong> Balance a 4 kg mass at 1 m using a 1 kg mass. Where must it go?',
 physics:`<p>Torque is <span class="eq-line">τ = r F⊥</span>. For balance, clockwise and anticlockwise torques match: <span class="eq-line">m₁ x₁ = m₂ x₂</span>.</p>`,
 controls:[
  {key:'m1',label:'Left mass',min:.5,max:6,step:.1,value:2,unit:'kg'},
  {key:'x1',label:'Left distance',min:.2,max:3.5,step:.05,value:2,unit:'m'},
  {key:'m2',label:'Right mass',min:.5,max:6,step:.1,value:1,unit:'kg'},
  {key:'x2',label:'Right distance',min:.2,max:3.5,step:.05,value:3,unit:'m'}
 ],
 readouts:[['tl','Left torque'],['tr','Right torque'],['net','Net torque'],['bal','Balance']],
 create(api){const p=api.params,g=el('g',{},api.stage);let ang=0,av=0;
  function reset(){ang=0;av=0;}
  function step(dt){const tl=p.m1*9.81*p.x1,tr=p.m2*9.81*p.x2,net=tr-tl;const I=p.m1*p.x1**2+p.m2*p.x2**2+8;av+=(net/I)*dt*2;av*=Math.exp(-1.5*dt);ang+=av*dt;ang=clamp(ang,-.42,.42);}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const cx=400,cy=250;el('path',{d:`M${cx-34},380 L${cx+34},380 L${cx},250 Z`,fill:'#94a3b8'},g);const grp=el('g',{transform:`rotate(${deg(ang)} ${cx} ${cy})`},g);el('rect',{x:cx-280,y:cy-8,width:560,height:16,rx:5,fill:'#2457c5'},grp);const s=78;[[ -p.x1,p.m1,'#7c3aed'],[p.x2,p.m2,'#059669']].forEach(([x,m,c])=>{el('rect',{x:cx+x*s-18,y:cy-8-36,width:36,height:36,rx:5,fill:c},grp);el('text',{x:cx+x*s,y:cy-26,'text-anchor':'middle',fill:'#fff','font-size':12,'font-weight':700,text:fmt(m,1)},grp);});const net=(p.m2*p.x2-p.m1*p.x1)*9.81;el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:Math.abs(net)<.5?'Balanced!':'Unbalanced'},g);}
  function read(){const tl=p.m1*9.81*p.x1,tr=p.m2*9.81*p.x2;api.out('tl',fmt(tl,1)+' N·m');api.out('tr',fmt(tr,1)+' N·m');api.out('net',fmt(tr-tl,1)+' N·m');api.out('bal',Math.abs(tr-tl)<.5?'yes':'no');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Atwood ---------------- */
register({
 id:'atwood',title:'Atwood machine',tag:'Connected masses',icon:ICON.atwood,
 blurb:'Two masses share a rope over a pulley. Predict which way the system accelerates.',
 hint:'Equal masses balance; a small difference still moves the whole system.',
 challenge:'<strong>Challenge:</strong> Make the masses almost equal. Is the acceleration small even though the masses are large?',
 physics:`<p>For an ideal pulley, <span class="eq-line">a = (m₂−m₁)g / (m₁+m₂)</span> and <span class="eq-line">T = 2m₁m₂g / (m₁+m₂)</span>.</p>`,
 controls:[
  {key:'m1',label:'Left mass',min:.5,max:8,step:.1,value:2,unit:'kg',reset:true},
  {key:'m2',label:'Right mass',min:.5,max:8,step:.1,value:3,unit:'kg',reset:true}
 ],
 readouts:[['acc','Acceleration'],['tension','Tension'],['vel','Speed'],['dist','Displacement']],
 create(api){const p=api.params,g=el('g',{},api.stage);let y,v,stopped;
  function reset(){y=0;v=0;stopped=false;}
  function step(dt){if(stopped)return;const a=(p.m2-p.m1)*9.81/(p.m1+p.m2);v+=a*dt;y+=v*dt;if(Math.abs(y)>2){y=Math.sign(y)*2;v=0;stopped=true;}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const cx=400,cy=90;el('circle',{cx,cy,r:34,fill:'#e2e8f0',stroke:'#94a3b8','stroke-width':3},g);const lx=cx-34,rx=cx+34,ly=220+y*55,ry=220-y*55;el('path',{d:`M${lx},${ly} L${lx},${cy} A34,34 0 0 1 ${rx},${cy} L${rx},${ry}`,fill:'none',stroke:'#334155','stroke-width':3},g);[[lx,ly,p.m1,'#2457c5'],[rx,ry,p.m2,'#7c3aed']].forEach(([x,yy,m,c])=>{const h=30+4*m;el('rect',{x:x-24,y:yy,width:48,height:h,rx:5,fill:c},g);el('text',{x,y:yy+20,'text-anchor':'middle',fill:'#fff','font-weight':700,text:fmt(m,1)+' kg'},g);});}
  function read(){const a=(p.m2-p.m1)*9.81/(p.m1+p.m2),T=2*p.m1*p.m2*9.81/(p.m1+p.m2);api.out('acc',fmt(a,2)+' m/s²');api.out('tension',fmt(T,1)+' N');api.out('vel',fmt(v,2)+' m/s');api.out('dist',fmt(y,2)+' m');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Rolling race ---------------- */
register({
 id:'rolling',title:'Rolling race',tag:'Rotational energy',icon:ICON.rolling,
 blurb:'Race a sphere, a disk, and a hoop down the same ramp. Which wins—and why?',
 hint:'Mass does not decide the winner; how mass is spread out does.',
 challenge:'<strong>Challenge:</strong> Predict the order before releasing. Then change the ramp angle. Does the order change?',
 physics:`<p>Rolling acceleration is <span class="eq-line">a = g sin θ / (1 + I/(mR²))</span>. Sphere: 2/5, disk: 1/2, hoop: 1.</p>`,
 controls:[
  {key:'angle',label:'Ramp angle',min:5,max:45,step:1,value:20,unit:'°',reset:true},
  {key:'mass',label:'Mass of each',min:.5,max:5,step:.1,value:1,unit:'kg',reset:true}
 ],
 readouts:[['winner','Winner'],['ts','Sphere time'],['td','Disk time'],['th','Hoop time']],
 create(api){const p=api.params,g=el('g',{},api.stage);const objs=[{name:'Sphere',c:.4,color:'#2457c5'},{name:'Disk',c:.5,color:'#059669'},{name:'Hoop',c:1,color:'#7c3aed'}];let st;
  function reset(){st=objs.map(()=>({s:0,v:0,t:null}));}
  function step(dt){const a0=9.81*Math.sin(rad(p.angle));objs.forEach((o,i)=>{const q=st[i];if(q.t!==null)return;const a=a0/(1+o.c);q.v+=a*dt;q.s+=q.v*dt;if(q.s>=8){q.s=8;q.t=Math.sqrt(16/a);}});}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);objs.forEach((o,i)=>{const y=110+i*105;el('line',{x1:90,y1:y,x2:710,y2:y,stroke:'#e2e8f0','stroke-width':3},g);el('text',{x:20,y:y+5,'font-size':13,fill:o.color,'font-weight':700,text:o.name},g);const x=90+st[i].s/8*600;el('circle',{cx:x,cy:y-16,r:16,fill:o.color},g);if(o.c===1)el('circle',{cx:x,cy:y-16,r:9,fill:'#fff'},g);if(st[i].t!==null)el('text',{x:730,y:y+5,'font-size':12,fill:'#047857',text:fmt(st[i].t,2)+' s'},g);});}
  function read(){const done=st.map((q,i)=>q.t!==null?i:-1).filter(i=>i>=0);const winner=done.length?objs[done.sort((a,b)=>st[a].t-st[b].t)[0]].name:'racing…';api.out('winner',winner);api.out('ts',st[0].t?fmt(st[0].t,2)+' s':'—');api.out('td',st[1].t?fmt(st[1].t,2)+' s':'—');api.out('th',st[2].t?fmt(st[2].t,2)+' s':'—');}
  reset();return{step,render,read,reset};}
});

/* ---------------- Newton's cradle ---------------- */
register({
 id:'cradle',title:'Newton’s cradle',tag:'Momentum & energy',icon:ICON.cradle,
 blurb:'Lift balls on one side and release. Watch momentum and energy pass through the row.',
 hint:'In the ideal case, the same number of balls swings out on the other side.',
 challenge:'<strong>Challenge:</strong> Lift two balls. How many leave the far side? Try three.',
 physics:`<p>Nearly elastic collisions between equal masses transfer velocity. Conserving both momentum and kinetic energy explains why the same number of balls emerges.</p>`,
 controls:[
  {key:'n',label:'Balls',min:3,max:7,step:1,value:5,reset:true},
  {key:'lift',label:'Lift count',min:1,max:3,step:1,value:1,reset:true},
  {key:'damping',label:'Damping',min:0,max:.2,step:.005,value:.01,reset:true}
 ],
 readouts:[['side','Active side'],['energy','Relative energy'],['swings','Transfers'],['note','Pattern']],
 create(api){const p=api.params,g=el('g',{},api.stage);let th,om,side,transfers,E0;
  function reset(){th=rad(45);om=0;side='left';transfers=0;E0=1-Math.cos(th);}
  function step(dt){const n=Math.max(1,Math.ceil(dt/.006)),h=dt/n;for(let i=0;i<n;i++){const prev=th;const a=-9.81/1.2*Math.sin(th)-p.damping*om;om+=a*h;th+=om*h;if(prev>0&&th<=0&&om<0){side=side==='left'?'right':'left';th=0;om=-om;transfers++;}}}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const n=Math.round(p.n),k=Math.min(Math.round(p.lift),n-1),cx=400,cy=80,sp=34,L=210;el('line',{x1:cx-n*sp/2-30,y1:cy,x2:cx+n*sp/2+30,y2:cy,stroke:'#94a3b8','stroke-width':5},g);for(let i=0;i<n;i++){let angle=0;const leftGroup=i<k,rightGroup=i>=n-k;if(side==='left'&&leftGroup)angle=-Math.abs(th);if(side==='right'&&rightGroup)angle=Math.abs(th);const px=cx+(i-(n-1)/2)*sp;const bx=px+L*Math.sin(angle),by=cy+L*Math.cos(angle);el('line',{x1:px,y1:cy,x2:bx,y2:by,stroke:'#64748b','stroke-width':2},g);el('circle',{cx:bx,cy:by,r:15,fill:'#2457c5',stroke:'#1e3a8a'},g);}el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:`Lift ${k} · active ${side}`},g);}
  function read(){const E=1-Math.cos(th)+.5*(1.2*om)**2/9.81;api.out('side',side);api.out('energy',fmt(E/Math.max(.001,E0)*100,0)+'%');api.out('swings',String(transfers));api.out('note',`${Math.min(Math.round(p.lift),Math.round(p.n)-1)} in → ${Math.min(Math.round(p.lift),Math.round(p.n)-1)} out`);}
  reset();return{step,render,read,reset};}
});

/* ---------------- Waves ---------------- */
register({
 id:'waves',title:'Standing waves',tag:'Mechanical waves',icon:ICON.waves,
 blurb:'Shake a string into harmonics. Change tension and density to change wave speed.',
 hint:'Higher tension speeds waves up; heavier string slows them down.',
 challenge:'<strong>Challenge:</strong> Find the mode with three antinodes. How does its frequency compare with the fundamental?',
 physics:`<p>Wave speed on a string is <span class="eq-line">v = √(T/μ)</span>. Fixed-end harmonics have <span class="eq-line">λₙ = 2L/n</span> and <span class="eq-line">fₙ = n v/(2L)</span>.</p>`,
 controls:[
  {key:'mode',label:'Harmonic mode',min:1,max:6,step:1,value:1},
  {key:'T',label:'Tension',min:2,max:50,step:1,value:10,unit:'N'},
  {key:'mu',label:'Linear density',min:.02,max:.5,step:.01,value:.1,unit:'kg/m'},
  {key:'A',label:'Amplitude',min:5,max:60,step:1,value:35,unit:'px'}
 ],
 readouts:[['speed','Wave speed'],['lambda','Wavelength'],['freq','Frequency'],['nodes','Nodes']],
 create(api){const p=api.params,g=el('g',{},api.stage);let phase=0;const L=2;
  function reset(){phase=0;}
  function step(dt){const v=Math.sqrt(p.T/p.mu),f=p.mode*v/(2*L);phase+=2*Math.PI*f*dt*.15;}
  function render(){clear(g);el('rect',{x:0,y:0,width:800,height:450,fill:'#fff'},g);const x0=80,x1=720,y0=225;el('line',{x1:x0,y1:y0,x2:x1,y2:y0,stroke:'#e2e8f0','stroke-dasharray':'4 5'},g);el('rect',{x:x0-10,y:y0-50,width:10,height:100,fill:'#94a3b8'},g);el('rect',{x:x1,y:y0-50,width:10,height:100,fill:'#94a3b8'},g);let d='';for(let i=0;i<=240;i++){const f=i/240,x=x0+(x1-x0)*f,y=y0-p.A*Math.sin(p.mode*Math.PI*f)*Math.cos(phase);d+=(i===0?'M':'L')+x+','+y;}el('path',{d,fill:'none',stroke:'#2457c5','stroke-width':3},g);for(let j=0;j<=p.mode;j++){const x=x0+(x1-x0)*j/p.mode;el('circle',{cx:x,cy:y0,r:4,fill:'#7c3aed'},g);}el('text',{x:20,y:28,'font-size':13,fill:'#1e3a8a','font-weight':700,text:`Mode ${Math.round(p.mode)} · slow-motion view`},g);}
  function read(){const v=Math.sqrt(p.T/p.mu),lam=2*L/p.mode,f=v/lam;api.out('speed',fmt(v,1)+' m/s');api.out('lambda',fmt(lam,2)+' m');api.out('freq',fmt(f,2)+' Hz');api.out('nodes',String(Math.round(p.mode)+1));}
  reset();return{step,render,read,reset};}
});

/* ---------------- Framework ---------------- */
let active=null,instance=null,playing=false,speed=1,last=0,raf=0,lastRead=0;
const exploredKey='mais-pac-mechanics-explored-v1';
function getExplored(){try{return new Set(JSON.parse(localStorage.getItem(exploredKey)||'[]'));}catch(e){return new Set();}}
function saveExplored(set){try{localStorage.setItem(exploredKey,JSON.stringify([...set]));}catch(e){}}
function updateProgress(){const set=getExplored();const pct=SIMS.length?set.size/SIMS.length*100:0;$('mech-progress-fill').style.width=pct+'%';$('mech-progress-text').textContent=`${set.size} / ${SIMS.length} explored`;document.querySelectorAll('.mech-card').forEach(c=>{const mark=c.querySelector('.explored-mark');if(mark)mark.textContent=set.has(c.dataset.sim)?'✓ explored':'';});}
function buildControls(sim){const box=$('mech-controls');clear(box);const params={};sim.controls.forEach(c=>{params[c.key]=c.type==='check'?!!c.value:c.type==='select'?(Number.isFinite(Number(c.value))?Number(c.value):c.value):Number(c.value);const wrap=document.createElement('div');wrap.className='mech-control'+(c.type==='check'?' check':'');if(c.type==='button'){const b=document.createElement('button');b.type='button';b.className='mech-btn';b.textContent=c.label;b.addEventListener('click',()=>{instance.action?.(c.action);instance.render();updateReadouts();});wrap.className='mech-control-buttons';wrap.appendChild(b);box.appendChild(wrap);return;}const label=document.createElement('label');label.htmlFor='ctl-'+c.key;label.textContent=c.label;wrap.appendChild(label);let input;if(c.type==='select'){input=document.createElement('select');c.options.forEach(([v,t])=>{const o=document.createElement('option');o.value=v;o.textContent=t;if(String(v)===String(c.value))o.selected=true;input.appendChild(o);});}else if(c.type==='check'){input=document.createElement('input');input.type='checkbox';input.checked=!!c.value;}else{input=document.createElement('input');input.type='range';input.min=c.min;input.max=c.max;input.step=c.step;input.value=c.value;}input.id='ctl-'+c.key;wrap.appendChild(input);let out;if(c.type==='range'){out=document.createElement('output');out.textContent=fmt(c.value,c.step<1?2:0)+(c.unit?' '+c.unit:'');wrap.appendChild(out);}input.addEventListener('input',()=>{const val=c.type==='check'?input.checked:c.type==='select'?(Number.isFinite(Number(input.value))?Number(input.value):input.value):Number(input.value);params[c.key]=val;if(out)out.textContent=fmt(val,c.step<1?2:0)+(c.unit?' '+c.unit:'');if(c.reset){instance.reset();}else instance.onParam?.(c.key);instance.render();updateReadouts();});box.appendChild(wrap);});return params;}
function buildReadouts(sim){const box=$('mech-readouts');clear(box);sim.readouts.forEach(([key,label])=>{const d=document.createElement('div');d.className='mech-readout';d.innerHTML=`<span>${label}</span><output id="ro-${key}">—</output>`;box.appendChild(d);});}
function updateReadouts(){if(instance?.read)instance.read();}
function selectSim(id){const sim=SIMS.find(s=>s.id===id)||SIMS[0];active=sim;if(raf)cancelAnimationFrame(raf);$('mech-sim-tag').textContent=sim.tag;$('mech-sim-title').textContent=sim.title;$('mech-sim-blurb').textContent=sim.blurb;$('mech-stage-hint').textContent=sim.hint;$('mech-challenge').innerHTML=sim.challenge;$('mech-physics-body').innerHTML=sim.physics;const stage=$('mech-stage');clear(stage);el('title',{text:sim.title+' interactive simulation'},stage);const params=buildControls(sim);buildReadouts(sim);const api={stage,params,out:(key,val)=>{const o=$('ro-'+key);if(o)o.textContent=val;}};instance=sim.create(api);instance.reset();instance.render();updateReadouts();document.querySelectorAll('.mech-card').forEach(c=>c.classList.toggle('active',c.dataset.sim===sim.id));const done=getExplored().has(sim.id);$('mech-mark').classList.toggle('done',done);$('mech-mark').textContent=done?'✓ Explored':'Mark explored';try{history.replaceState(null,'','#'+sim.id);}catch(e){location.hash=sim.id;}last=0;raf=requestAnimationFrame(loop);}
function loop(now){if(!last)last=now;let dt=(now-last)/1000;last=now;dt=Math.min(dt,.05)*speed;if(playing&&instance){instance.step(dt);instance.render();}if(now-lastRead>120){updateReadouts();lastRead=now;}raf=requestAnimationFrame(loop);}
function setPlaying(v){playing=v;$('mech-play').textContent=v?'Pause':'Play';$('mech-play').setAttribute('aria-pressed',String(v));}
function buildGallery(){const grid=$('mech-grid');clear(grid);SIMS.forEach(sim=>{const b=document.createElement('button');b.type='button';b.className='mech-card';b.dataset.sim=sim.id;b.innerHTML=`<span class="mech-card-icon" aria-hidden="true">${sim.icon}</span><small>${sim.tag}</small><h3>${sim.title}</h3><p>${sim.blurb}</p><span class="explored-mark"></span>`;b.addEventListener('click',()=>{selectSim(sim.id);$('mech-lab').scrollIntoView({behavior:'smooth',block:'start'});});grid.appendChild(b);});}
function init(){if(!$('mech-stage'))return;buildGallery();$('mech-play').addEventListener('click',()=>setPlaying(!playing));$('mech-reset').addEventListener('click',()=>{instance.reset();instance.render();updateReadouts();});$('mech-step').addEventListener('click',()=>{instance.step(1/60);instance.render();updateReadouts();});$('mech-speed').addEventListener('input',e=>{speed=Number(e.target.value);$('mech-speed-out').textContent=fmt(speed,2)+'×';});$('mech-mark').addEventListener('click',()=>{const set=getExplored();set.add(active.id);saveExplored(set);updateProgress();$('mech-mark').classList.add('done');$('mech-mark').textContent='✓ Explored';});document.addEventListener('keydown',e=>{if(e.target.matches('input,select,textarea,button'))return;if(e.code==='Space'){e.preventDefault();setPlaying(!playing);}if(e.key.toLowerCase()==='r'){instance.reset();instance.render();updateReadouts();}});const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;const hash=location.hash.slice(1);selectSim(SIMS.some(s=>s.id===hash)?hash:'pendulum');window.addEventListener('hashchange',()=>{const h=location.hash.slice(1);if(SIMS.some(s=>s.id===h)&&active?.id!==h)selectSim(h);});setPlaying(!reduced);updateProgress();document.documentElement.dataset.mechanicsReady='true';window.MechanicsPlayground={SIMS,selectSim,getInstance:()=>instance,getParams:()=>active?Object.fromEntries(active.controls.map(c=>[c.key,document.getElementById('ctl-'+c.key)?.value])):{}};}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
