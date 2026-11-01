import { chromium } from 'playwright';
import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const base = process.env.BASE_URL || 'http://127.0.0.1:3000/mechanics/';
const ids = ['pendulum','projectile','ramp','cart','spring','collisions','coaster','orbits','torque','atwood','rolling','cradle','waves'];
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errors = [];
page.on('pageerror', e => errors.push('pageerror: ' + e.message));
page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
const external = [];
page.on('request', r => { const u = r.url(); if (/^https?:/.test(u) && !u.startsWith(base) && base.startsWith('http')) external.push(u); });

async function ready() { await page.waitForFunction(() => document.documentElement.dataset.mechanicsReady === 'true', { timeout: 15000 }); }
async function setRange(id, value) { await page.evaluate(([id, value]) => { const el = document.getElementById(id); el.value = value; el.dispatchEvent(new Event('input', { bubbles: true })); }, [id, value]); }
async function selectSim(id) { await page.click(`.mech-card[data-sim="${id}"]`); await page.waitForFunction(id => document.querySelector('.mech-card.active')?.dataset.sim === id, id); }

try {
  await page.goto(base, { waitUntil: 'load' });
  await ready();
  assert.equal(await page.locator('.mech-card').count(), ids.length, '13 experiment cards');
  assert.match(await page.locator('#mech-sim-title').textContent(), /Pendulum/);

  // Pendulum physics readout: T = 2π√(L/g).
  await setRange('ctl-L', 2);
  await page.waitForTimeout(200);
  const smallT = parseFloat(await page.locator('#ro-smallT').textContent());
  assert.ok(Math.abs(smallT - 2 * Math.PI * Math.sqrt(2 / 9.81)) < 0.01, `pendulum small-angle period ${smallT}`);
  await page.click('#mech-play');
  assert.equal(await page.locator('#mech-play').textContent(), 'Play');
  await page.click('#mech-play');
  assert.equal(await page.locator('#mech-play').textContent(), 'Pause');

  // Every simulation mounts, renders, steps, and exposes four readouts.
  for (const id of ids) {
    await selectSim(id);
    await page.waitForTimeout(80);
    assert.equal(await page.locator('#mech-readouts .mech-readout').count(), 4, `${id} readouts`);
    assert.ok(await page.locator('#mech-stage').evaluate(el => el.querySelectorAll('*').length) > 8, `${id} stage rendered`);
    await page.click('#mech-step');
    await page.click('#mech-step');
    const physics = await page.locator('#mech-physics-body').innerHTML();
    assert.ok(physics.length > 20, `${id} optional physics`);
  }

  // Challenge + passport.
  await selectSim('pendulum');
  await page.click('#mech-mark');
  assert.match(await page.locator('#mech-progress-text').textContent(), /1 \/ 13 explored/);
  assert.match(await page.locator('#mech-mark').textContent(), /Explored/);

  // Hash routing.
  const hashBase = base.split('#')[0] + '#spring';
  await page.goto(hashBase, { waitUntil: 'load' });
  await ready();
  await page.waitForFunction(() => document.querySelector('.mech-card.active')?.dataset.sim === 'spring');
  assert.match(await page.locator('#mech-sim-title').textContent(), /Spring/);

  // Mobile: no horizontal overflow.
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(base, { waitUntil: 'load' });
  await ready();
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  assert.ok(overflow <= 1, `mobile overflow ${overflow}px`);

  // Integration links on the live site.
  if (base.startsWith('http')) {
    const root = new URL('/', base).href;
    for (const rel of ['', 'explore/', 'teaching/', 'about/', 'club/', 'resources/']) {
      await page.goto(root + rel, { waitUntil: 'load' });
      assert.ok(await page.locator('nav.site-nav a', { hasText: 'Mechanics Lab' }).count() >= 1, `Mechanics Lab nav link on ${rel || 'home'}`);
      assert.ok(await page.locator('nav.site-nav a', { hasText: 'Club' }).count() >= 1, `Club nav link on ${rel || 'home'}`);
    }
    await page.goto(root + 'explore/', { waitUntil: 'load' });
    assert.equal(await page.locator('[data-mechanics-feature]').count(), 0, 'Explore Mechanics feature card removed');
  } else {
    assert.equal(external.length, 0, 'offline page makes no network requests');
  }
  assert.deepEqual(errors, [], 'no browser errors');
  console.log(`PASS mechanics (${base.startsWith('file') ? 'offline' : 'live'}): 13 simulations, controls, readouts, challenges, routing, mobile${base.startsWith('http') ? ', site integration' : ''}.`);
} finally { await browser.close(); }
