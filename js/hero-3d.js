/* ============================================================
   hero-3d.js — a small interactive cosmos for the hero.
   three.js is vendored locally, so there are no third-party
   requests at runtime. Everything here is procedural.
   ============================================================ */

import * as THREE from '../assets/vendor/three.module.min.js';

const PALETTE = {
  cyan: 0x35c6ff,
  yellow: 0xffc21a,
  orange: 0xff6a1f,
  purple: 0xa06bff,
  green: 0x6ee06b,
  pink: 0xff4d97,
  blue: 0x3d7bff
};

export function supportsWebGL() {
  try {
    const canvas = document.createElement('canvas');
    return Boolean(
      window.WebGLRenderingContext &&
      (canvas.getContext('webgl2') || canvas.getContext('webgl'))
    );
  } catch {
    return false;
  }
}

function starTexture() {
  const size = 64;
  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = size;
  const ctx = canvas.getContext('2d');
  const g = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
  g.addColorStop(0, 'rgba(255,255,255,1)');
  g.addColorStop(0.22, 'rgba(255,255,255,.92)');
  g.addColorStop(0.45, 'rgba(190,220,255,.42)');
  g.addColorStop(0.75, 'rgba(120,170,255,.1)');
  g.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, size, size);
  const tex = new THREE.CanvasTexture(canvas);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

function nebulaTexture(inner, outer) {
  const size = 256;
  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = size;
  const ctx = canvas.getContext('2d');
  const g = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
  g.addColorStop(0, inner);
  g.addColorStop(0.45, outer);
  g.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, size, size);
  const tex = new THREE.CanvasTexture(canvas);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

const DISK_VERT = /* glsl */`
  varying vec2 vLocal;
  void main() {
    vLocal = position.xy;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const DISK_FRAG = /* glsl */`
  uniform float uTime;
  uniform float uInner;
  uniform float uOuter;
  varying vec2 vLocal;

  void main() {
    float r = length(vLocal);
    float t = clamp((r - uInner) / (uOuter - uInner), 0.0, 1.0);
    float angle = atan(vLocal.y, vLocal.x);

    float swirlA = sin(angle * 22.0 + t * 34.0 - uTime * 1.9) * 0.5 + 0.5;
    float swirlB = sin(angle * 8.0 - t * 15.0 + uTime * 1.1) * 0.5 + 0.5;
    float streak = mix(0.45, 1.0, pow(swirlA, 2.2)) * mix(0.7, 1.0, swirlB);

    float doppler = 0.62 + 0.38 * smoothstep(-1.2, 1.2, sin(angle + 0.6));

    vec3 hot = vec3(1.0, 0.95, 0.72);
    vec3 mid = vec3(1.0, 0.52, 0.11);
    vec3 cool = vec3(0.46, 0.07, 0.05);
    vec3 col = mix(hot, mid, smoothstep(0.0, 0.4, t));
    col = mix(col, cool, smoothstep(0.42, 1.0, t));

    float edge = smoothstep(0.0, 0.09, t) * (1.0 - smoothstep(0.62, 1.0, t));
    float alpha = edge * streak * 0.92;

    gl_FragColor = vec4(col * (0.85 + 0.75 * streak) * doppler, alpha);
  }
`;

const RIM_VERT = /* glsl */`
  varying vec3 vNormal;
  varying vec3 vView;
  void main() {
    vec4 mv = modelViewMatrix * vec4(position, 1.0);
    vNormal = normalize(normalMatrix * normal);
    vView = normalize(-mv.xyz);
    gl_Position = projectionMatrix * mv;
  }
`;

const RIM_FRAG = /* glsl */`
  uniform vec3 uColor;
  uniform float uPower;
  varying vec3 vNormal;
  varying vec3 vView;
  void main() {
    float f = pow(1.0 - clamp(dot(vNormal, vView), 0.0, 1.0), uPower);
    gl_FragColor = vec4(uColor * f * 1.6, f);
  }
`;

const PLANET_VERT = /* glsl */`
  varying vec3 vNormal;
  varying vec3 vPos;
  void main() {
    vNormal = normalize(normalMatrix * normal);
    vPos = position;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const PLANET_FRAG = /* glsl */`
  uniform vec3 uDeep;
  uniform vec3 uLight;
  uniform vec3 uShine;
  varying vec3 vNormal;
  varying vec3 vPos;

  void main() {
    float bands = sin(vPos.y * 14.0 + sin(vPos.x * 5.0) * 1.6) * 0.5 + 0.5;
    vec3 base = mix(uDeep, uShine, pow(bands, 2.0) * 0.7);
    vec3 lightDir = normalize(vec3(-0.55, 0.42, 0.72));
    float shade = clamp(dot(normalize(vNormal), lightDir), 0.0, 1.0);
    float rim = pow(1.0 - clamp(dot(normalize(vNormal), vec3(0.0, 0.0, 1.0)), 0.0, 1.0), 2.4);
    vec3 col = base * (0.32 + 0.9 * shade) + uLight * rim * 0.55;
    gl_FragColor = vec4(col, 1.0);
  }
`;

function makeStarLayer(count, spread, size, texture) {
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(count * 3);
  const colors = new Float32Array(count * 3);
  const tints = [
    [1, 1, 1],
    [0.78, 0.9, 1],
    [1, 0.92, 0.72],
    [0.82, 0.86, 1]
  ];

  for (let i = 0; i < count; i++) {
    positions[i * 3] = (Math.random() - 0.5) * spread;
    positions[i * 3 + 1] = (Math.random() - 0.5) * spread * 0.75;
    positions[i * 3 + 2] = (Math.random() - 0.5) * spread * 0.8 - 4;
    const tint = tints[Math.floor(Math.random() * tints.length)];
    const brightness = 0.55 + Math.random() * 0.45;
    colors[i * 3] = tint[0] * brightness;
    colors[i * 3 + 1] = tint[1] * brightness;
    colors[i * 3 + 2] = tint[2] * brightness;
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size,
    map: texture,
    vertexColors: true,
    transparent: true,
    opacity: 0.95,
    depthWrite: false,
    blending: THREE.AdditiveBlending,
    sizeAttenuation: true
  });

  const points = new THREE.Points(geometry, material);
  return points;
}

export function init(canvas) {
  if (!canvas) return null;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
  } catch {
    return null;
  }

  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.setClearColor(0x000000, 0);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.8));

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 120);
  camera.position.set(0, 0.15, 10);

  const world = new THREE.Group();
  scene.add(world);

  const sprite = starTexture();

  /* ---------- stars ---------- */
  const starsFar = makeStarLayer(900, 46, 0.28, sprite);
  const starsNear = makeStarLayer(260, 34, 0.5, sprite);
  scene.add(starsFar, starsNear);

  /* ---------- nebulae ---------- */
  const nebulaA = new THREE.Sprite(new THREE.SpriteMaterial({
    map: nebulaTexture('rgba(160,107,255,.55)', 'rgba(90,40,210,.18)'),
    transparent: true,
    opacity: 0.55,
    depthWrite: false,
    blending: THREE.AdditiveBlending
  }));
  nebulaA.position.set(-8.5, 4, -15);
  nebulaA.scale.set(20, 20, 1);
  scene.add(nebulaA);

  const nebulaB = new THREE.Sprite(new THREE.SpriteMaterial({
    map: nebulaTexture('rgba(53,198,255,.42)', 'rgba(20,90,190,.14)'),
    transparent: true,
    opacity: 0.5,
    depthWrite: false,
    blending: THREE.AdditiveBlending
  }));
  nebulaB.position.set(9, -5, -17);
  nebulaB.scale.set(24, 24, 1);
  scene.add(nebulaB);

  /* ---------- black hole ---------- */
  const blackHole = new THREE.Group();
  const horizon = new THREE.Mesh(
    new THREE.SphereGeometry(1, 48, 32),
    new THREE.MeshBasicMaterial({ color: 0x000000 })
  );
  blackHole.add(horizon);

  const rim = new THREE.Mesh(
    new THREE.SphereGeometry(1.035, 48, 32),
    new THREE.ShaderMaterial({
      vertexShader: RIM_VERT,
      fragmentShader: RIM_FRAG,
      uniforms: {
        uColor: { value: new THREE.Color(0xff8a2a) },
        uPower: { value: 2.6 }
      },
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      side: THREE.FrontSide
    })
  );
  blackHole.add(rim);

  const photonRing = new THREE.Mesh(
    new THREE.RingGeometry(1.03, 1.1, 128),
    new THREE.MeshBasicMaterial({
      color: 0xfff2c4,
      transparent: true,
      opacity: 0.5,
      side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    })
  );
  photonRing.rotation.x = -Math.PI / 2;
  blackHole.add(photonRing);

  const disk = new THREE.Mesh(
    new THREE.RingGeometry(1.22, 4.2, 256, 1),
    new THREE.ShaderMaterial({
      vertexShader: DISK_VERT,
      fragmentShader: DISK_FRAG,
      uniforms: {
        uTime: { value: 0 },
        uInner: { value: 1.22 },
        uOuter: { value: 4.2 }
      },
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      side: THREE.DoubleSide
    })
  );
  disk.rotation.x = -Math.PI / 2;
  blackHole.add(disk);

  const diskHalo = new THREE.Mesh(
    new THREE.RingGeometry(4.1, 5.4, 128),
    new THREE.MeshBasicMaterial({
      color: 0xff5a1a,
      transparent: true,
      opacity: 0.1,
      side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    })
  );
  diskHalo.rotation.x = -Math.PI / 2;
  blackHole.add(diskHalo);

  blackHole.position.set(3.4, 2.35, -5.2);
  blackHole.rotation.set(0.72, 0, -0.3);
  blackHole.scale.setScalar(0.86);
  world.add(blackHole);

  /* ---------- ringed planet ---------- */
  const planet = new THREE.Group();
  const planetBody = new THREE.Mesh(
    new THREE.SphereGeometry(0.62, 48, 32),
    new THREE.ShaderMaterial({
      vertexShader: PLANET_VERT,
      fragmentShader: PLANET_FRAG,
      uniforms: {
        uDeep: { value: new THREE.Color(0x0d1f5e) },
        uShine: { value: new THREE.Color(0x4fa8ff) },
        uLight: { value: new THREE.Color(0x9fdcff) }
      }
    })
  );
  planet.add(planetBody);

  const planetRing = new THREE.Mesh(
    new THREE.RingGeometry(0.82, 1.42, 96, 1),
    new THREE.ShaderMaterial({
      vertexShader: DISK_VERT,
      fragmentShader: /* glsl */`
        uniform float uTime;
        varying vec2 vLocal;
        void main() {
          float r = length(vLocal);
          float t = clamp((r - 0.82) / 0.6, 0.0, 1.0);
          float gap = smoothstep(0.34, 0.4, t) * (1.0 - smoothstep(0.52, 0.58, t));
          float band = 0.55 + 0.45 * sin(t * 28.0 + uTime * 0.4);
          vec3 col = mix(vec3(0.55, 0.82, 1.0), vec3(1.0, 0.86, 0.5), t);
          float a = (1.0 - gap) * band * (1.0 - smoothstep(0.86, 1.0, t)) * smoothstep(0.0, 0.08, t) * 0.55;
          gl_FragColor = vec4(col, a);
        }
      `,
      uniforms: { uTime: { value: 0 } },
      transparent: true,
      side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    })
  );
  planetRing.rotation.x = -Math.PI / 2 + 0.28;
  planetRing.rotation.z = 0.16;
  planet.add(planetRing);
  planet.position.set(-5.1, -2.2, -3.4);
  planet.rotation.z = 0.32;
  planet.scale.setScalar(1.25);
  world.add(planet);

  /* ---------- cosmic web wireframe ---------- */
  const web = new THREE.LineSegments(
    new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(3.1, 1)),
    new THREE.LineBasicMaterial({
      color: 0x3f6bff,
      transparent: true,
      opacity: 0.13,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    })
  );
  web.position.set(0.9, -1.5, -8);
  web.rotation.set(0.4, 0.2, 0.1);
  world.add(web);

  /* ---------- floating pixel cubes ---------- */
  const cubes = [];
  const cubeColors = [PALETTE.cyan, PALETTE.yellow, PALETTE.purple, PALETTE.orange, PALETTE.blue, PALETTE.pink];
  const cubeGeo = new THREE.BoxGeometry(0.16, 0.16, 0.16);
  for (let i = 0; i < 16; i++) {
    const mesh = new THREE.Mesh(
      cubeGeo,
      new THREE.MeshBasicMaterial({
        color: cubeColors[i % cubeColors.length],
        transparent: true,
        opacity: 0.85
      })
    );
    const radius = 3 + Math.random() * 3.6;
    const angle = Math.random() * Math.PI * 2;
    const y = (Math.random() - 0.5) * 5.2;
    mesh.position.set(Math.cos(angle) * radius * 0.55, y, Math.sin(angle) * radius * 0.35 - 3);
    mesh.userData = {
      angle,
      radius: radius * 0.55,
      speed: 0.04 + Math.random() * 0.09,
      bob: Math.random() * Math.PI * 2,
      spin: (Math.random() - 0.5) * 0.5
    };
    cubes.push(mesh);
    world.add(mesh);
  }

  /* ---------- sizing ---------- */
  let width = 1;
  let height = 1;

  const resize = () => {
    const w = canvas.clientWidth || canvas.parentElement?.clientWidth || window.innerWidth;
    const h = canvas.clientHeight || canvas.parentElement?.clientHeight || window.innerHeight;
    if (!w || !h) return;
    width = w;
    height = h;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    // pull the camera back a touch on narrow screens so the black hole still fits
    camera.position.z = w < 760 ? 13.5 : 10;
    camera.updateProjectionMatrix();
  };

  const ro = new ResizeObserver(resize);
  ro.observe(canvas);

  /* ---------- interaction ---------- */
  const state = {
    targetX: 0,
    targetY: 0,
    currentX: 0,
    currentY: 0,
    dragBaseX: 0,
    dragBaseY: 0,
    dragging: false,
    pointerX: 0,
    pointerY: 0,
    pointerId: null,
    startX: 0,
    startY: 0,
    visible: true,
    running: false,
    t: 0
  };

  const clamp = (v, min, max) => Math.min(max, Math.max(min, v));

  const onPointerDown = (event) => {
    if (event.pointerType === 'mouse' && event.button !== 0) return;
    state.dragging = true;
    state.pointerId = event.pointerId;
    state.startX = event.clientX;
    state.startY = event.clientY;
    state.dragBaseX = state.targetX;
    state.dragBaseY = state.targetY;
    canvas.classList.add('is-dragging');
    canvas.setPointerCapture?.(event.pointerId);
    if (!state.running) renderFrame(0);
  };

  const onPointerMove = (event) => {
    const rect = canvas.getBoundingClientRect();
    state.pointerX = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    state.pointerY = ((event.clientY - rect.top) / rect.height) * 2 - 1;

    if (!state.dragging) return;
    const dx = (event.clientX - state.startX) / rect.width;
    const dy = (event.clientY - state.startY) / rect.height;
    state.targetX = clamp(state.dragBaseX + dx * 1.5, -0.7, 0.7);
    state.targetY = clamp(state.dragBaseY + dy * 0.9, -0.4, 0.4);
    if (!state.running) renderFrame(0);
  };

  const endDrag = (event) => {
    if (!state.dragging) return;
    state.dragging = false;
    canvas.classList.remove('is-dragging');
    if (state.pointerId !== null && canvas.hasPointerCapture?.(state.pointerId)) {
      canvas.releasePointerCapture(state.pointerId);
    }
    state.pointerId = null;
  };

  canvas.addEventListener('pointerdown', onPointerDown);
  canvas.addEventListener('pointermove', onPointerMove);
  canvas.addEventListener('pointerup', endDrag);
  canvas.addEventListener('pointercancel', endDrag);
  canvas.addEventListener('pointerleave', () => {
    state.pointerX = 0;
    state.pointerY = 0;
  });

  const io = new IntersectionObserver((entries) => {
    state.visible = entries[0]?.isIntersecting ?? true;
    if (state.visible) start();
    else stop();
  }, { threshold: 0.02 });
  io.observe(canvas);

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop();
    else if (state.visible) start();
  });

  /* ---------- render loop ---------- */
  let raf = 0;
  let last = 0;

  function renderFrame(dt) {
    state.t += dt;

    // ease toward the drag target
    state.currentX += (state.targetX - state.currentX) * Math.min(1, dt * 6);
    state.currentY += (state.targetY - state.currentY) * Math.min(1, dt * 6);

    const px = reduceMotion ? 0 : state.pointerX;
    const py = reduceMotion ? 0 : state.pointerY;
    world.rotation.y = state.currentX + px * 0.1;
    world.rotation.x = state.currentY + py * 0.06;

    starsFar.rotation.y += dt * 0.006;
    starsNear.rotation.y -= dt * 0.012;
    starsFar.position.x = px * 0.5;
    starsFar.position.y = -py * 0.3;
    starsNear.position.x = px * 0.9;
    starsNear.position.y = -py * 0.6;

    disk.material.uniforms.uTime.value = state.t;
    planetRing.material.uniforms.uTime.value = state.t;
    planet.rotation.y += dt * 0.06;
    web.rotation.y += dt * 0.03;
    web.rotation.x += dt * 0.012;

    for (const cube of cubes) {
      const d = cube.userData;
      d.angle += dt * d.speed;
      cube.position.x = Math.cos(d.angle) * d.radius;
      cube.position.z = Math.sin(d.angle) * d.radius * 0.6 - 3;
      cube.position.y += Math.sin(state.t * 0.7 + d.bob) * dt * 0.12;
      cube.rotation.x += dt * d.spin;
      cube.rotation.y += dt * d.spin * 1.4;
    }

    nebulaA.material.opacity = 0.5 + Math.sin(state.t * 0.2) * 0.08;
    nebulaB.material.opacity = 0.45 + Math.cos(state.t * 0.16) * 0.08;

    renderer.render(scene, camera);
    canvas.classList.add('is-live');
  }

  function loop(now) {
    if (!state.running) return;
    const seconds = now / 1000;
    const dt = Math.min(0.05, last ? seconds - last : 0.016);
    last = seconds;
    renderFrame(dt);
    raf = requestAnimationFrame(loop);
  }

  function start() {
    if (state.running || reduceMotion) {
      if (reduceMotion) renderFrame(0.4);
      return;
    }
    state.running = true;
    last = 0;
    raf = requestAnimationFrame(loop);
  }

  function stop() {
    state.running = false;
    cancelAnimationFrame(raf);
  }

  resize();
  if (reduceMotion) {
    renderFrame(0.6);
  } else {
    start();
  }

  return {
    stop,
    start,
    dispose() {
      stop();
      ro.disconnect();
      io.disconnect();
      scene.traverse((obj) => {
        if (obj.geometry) obj.geometry.dispose();
        if (obj.material) {
          const materials = Array.isArray(obj.material) ? obj.material : [obj.material];
          materials.forEach((m) => {
            if (m.map && m.map !== sprite) m.map.dispose();
            m.dispose();
          });
        }
      });
      sprite.dispose();
      renderer.dispose();
    }
  };
}
