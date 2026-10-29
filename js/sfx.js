/* Tiny chiptune sound engine — no audio files, everything is synthesised. */

const STORAGE_KEY = 'mais-pac-sfx';
let ctx = null;
let master = null;
let enabled = false;

function ensure() {
  if (ctx) return ctx;
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) return null;
  ctx = new AC();
  master = ctx.createGain();
  master.gain.value = 0.18;
  master.connect(ctx.destination);
  return ctx;
}

function blip({ freq = 440, to = null, type = 'square', dur = 0.12, vol = 0.5, when = 0 }) {
  const c = ensure();
  if (!c) return;
  const t0 = c.currentTime + when;
  const osc = c.createOscillator();
  const gain = c.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, t0);
  if (to) osc.frequency.exponentialRampToValueAtTime(Math.max(40, to), t0 + dur);
  gain.gain.setValueAtTime(0.0001, t0);
  gain.gain.exponentialRampToValueAtTime(vol, t0 + 0.012);
  gain.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  osc.connect(gain).connect(master);
  osc.start(t0);
  osc.stop(t0 + dur + 0.02);
}

function noise({ dur = 0.18, vol = 0.35, when = 0 }) {
  const c = ensure();
  if (!c) return;
  const len = Math.floor(c.sampleRate * dur);
  const buffer = c.createBuffer(1, len, c.sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < len; i++) {
    data[i] = (Math.random() * 2 - 1) * (1 - i / len) ** 2;
  }
  const src = c.createBufferSource();
  src.buffer = buffer;
  const filter = c.createBiquadFilter();
  filter.type = 'bandpass';
  filter.frequency.value = 1200;
  const gain = c.createGain();
  gain.gain.value = vol;
  src.connect(filter).connect(gain).connect(master);
  src.start(c.currentTime + when);
}

const PRESETS = {
  click: () => blip({ freq: 660, to: 880, dur: 0.07, vol: 0.35 }),
  open: () => { blip({ freq: 520, dur: 0.07 }); blip({ freq: 780, dur: 0.09, when: 0.06 }); },
  close: () => blip({ freq: 420, to: 260, dur: 0.1, vol: 0.32 }),
  coin: () => { blip({ freq: 988, dur: 0.07, vol: 0.4 }); blip({ freq: 1319, dur: 0.14, vol: 0.4, when: 0.07 }); },
  big: () => { blip({ freq: 659, dur: 0.08 }); blip({ freq: 880, dur: 0.08, when: 0.08 }); blip({ freq: 1175, dur: 0.18, when: 0.16 }); },
  hit: () => { blip({ freq: 220, to: 90, type: 'sawtooth', dur: 0.22, vol: 0.5 }); noise({ dur: 0.16, vol: 0.3 }); },
  jump: () => blip({ freq: 340, to: 760, dur: 0.16, vol: 0.4 }),
  start: () => { blip({ freq: 392, dur: 0.09 }); blip({ freq: 523, dur: 0.09, when: 0.09 }); blip({ freq: 659, dur: 0.09, when: 0.18 }); blip({ freq: 784, dur: 0.2, when: 0.27 }); },
  over: () => { blip({ freq: 392, dur: 0.12 }); blip({ freq: 330, dur: 0.12, when: 0.12 }); blip({ freq: 262, dur: 0.3, when: 0.24 }); },
  star: () => blip({ freq: 1046, dur: 0.1, type: 'triangle', vol: 0.4 }),
  toggle: () => blip({ freq: 880, to: 1320, dur: 0.12, vol: 0.4 })
};

export function loadPreference() {
  try {
    enabled = localStorage.getItem(STORAGE_KEY) === '1';
  } catch {
    enabled = false;
  }
  return enabled;
}

export function isEnabled() {
  return enabled;
}

export function setEnabled(value) {
  enabled = Boolean(value);
  try { localStorage.setItem(STORAGE_KEY, enabled ? '1' : '0'); } catch { /* private mode */ }
  if (enabled) {
    const c = ensure();
    if (c && c.state === 'suspended') c.resume();
  }
  return enabled;
}

export function play(name) {
  if (!enabled) return;
  const preset = PRESETS[name];
  if (!preset) return;
  try {
    const c = ensure();
    if (c && c.state === 'suspended') c.resume();
    preset();
  } catch { /* audio is a bonus, never break the page */ }
}
