"""Interactive experiments for the IPhO curriculum.

Each experiment is pure HTML form controls plus an SVG canvas that a companion
script (`labs.js`) redraws on input. No network requests, no external files:
the controls and the canvas print in the exported PDF, and the lecture stays
readable with JavaScript disabled.
"""


def slider(key, label, lo, hi, step, value, unit=''):
    return (f'<label for="{key}">{label}<span class="lab-unit">{unit}</span>'
            f'<input id="{key}" type="range" min="{lo}" max="{hi}" step="{step}" value="{value}"></label>'
            f'<output class="range-value" id="range-{key}">{value}</output>')


def select(key, label, options):
    return (f'<label for="{key}">{label}<select id="{key}">'
            + ''.join(f'<option value="{v}">{label_}</option>' for v, label_ in options)
            + '</select></label>')


def check(key, label, checked=True):
    return (f'<label class="lab-check"><input type="checkbox" id="{key}"'
            f'{" checked" if checked else ""}> {label}</label>')


def shell(key, title, desc, controls, outputs, prompt):
    outs = ''.join(f'<div><span>{label}</span><output id="out-{key}-{k}">—</output></div>'
                   for k, label in outputs)
    return (
        f'<section class="cosmo-lab" id="lab-{key}" aria-labelledby="lab-{key}-title">'
        f'<div class="lab-heading"><span class="lab-kicker">Interactive experiment</span>'
        f'<h3 id="lab-{key}-title">{title}</h3><p>{desc}</p></div>'
        f'<div class="lab-controls">{controls}'
        f'<button type="button" class="print-btn" data-reset="{key}">Reset experiment</button></div>'
        f'<div class="lab-outputs">{outs}</div>'
        f'<svg class="lab-canvas" id="plot-{key}" viewBox="0 0 680 330" role="img" '
        f'aria-labelledby="plot-{key}-title"><title id="plot-{key}-title">{title}: interactive plot</title></svg>'
        f'<p class="lab-summary" id="summary-{key}" aria-live="polite"></p>'
        f'<div class="lab-prompt"><strong>Try this.</strong> {prompt}</div>'
        f'<p class="print-only lab-print-note">Snapshot of the experiment. Open the HTML edition to change the controls.</p>'
        f'<noscript><p class="lab-noscript">Enable JavaScript to use the experiment. The lecture and problems remain readable.</p></noscript>'
        f'</section>'
    )
