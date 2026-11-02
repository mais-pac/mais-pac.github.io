"""Original inline-SVG figures for the IPhO curriculum.

Every figure is a plain f-string of SVG: no external assets, no network
requests, and it prints identically in the browser and in the exported PDF.
The module is organised as a small drawing kit (frame, curve, arrow, ...)
followed by one section per topic. Figure ids must be unique on a page.
"""
from math import sin, cos, pi, log10, log, exp, sqrt, tan, atan2, atan, radians

# --------------------------------------------------------------------------
# Drawing kit
# --------------------------------------------------------------------------

INK = '#1e3a8a'
BLUE = '#2457c5'
GREEN = '#059669'
PURPLE = '#7c3aed'
AMBER = '#b45309'
RED = '#b91c1c'
GREY = '#64748b'
LIGHT = '#cbd5e1'
PALE = '#eff6ff'


MARKERS = {'blue': BLUE, 'grey': GREY, 'green': GREEN, 'purple': PURPLE,
           'amber': AMBER, 'red': RED, 'ink': INK}


def marker_name(colour):
    for name, value in MARKERS.items():
        if colour.lower() == value.lower():
            return name
    return 'blue'


def _id(key):
    return key.replace('_', '-')


def wrap(key, title, desc, body, caption, h=320, w=680):
    key = _id(key)
    return (
        f'<figure class="cosmo-figure" id="fig-{key}">'
        f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
        f'aria-labelledby="fig-{key}-title fig-{key}-desc" '
        f'xmlns="http://www.w3.org/2000/svg">'
        f'<title id="fig-{key}-title">{title}</title>'
        f'<desc id="fig-{key}-desc">{desc}</desc>'
        f'{body}</svg><figcaption>{caption}</figcaption></figure>'
    )


def t(x, y, s, color=INK, size=13, anchor='middle', weight=400, style=''):
    # Raw '<' and '>' would terminate or corrupt the SVG element, so escape them.
    s = str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    extra = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{extra}>{s}</text>')


def line(x1, y1, x2, y2, color=LIGHT, width=2, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}"{d}/>')


def arrow(key, x1, y1, x2, y2, color=BLUE, width=2.4, dash='', head=9.0):
    """A line with a filled triangular head drawn explicitly (no SVG markers)."""
    from math import atan2, cos, sin
    angle = atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * cos(angle), y2 - head * sin(angle)
    px, py = -sin(angle) * head * 0.42, cos(angle) * head * 0.42
    d = f' stroke-dasharray="{dash}"' if dash else ''
    shaft = (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{color}" '
             f'stroke-width="{width}"{d}/>')
    tip = (f'<polygon points="{x2:.1f},{y2:.1f} {bx + px:.1f},{by + py:.1f} {bx - px:.1f},{by - py:.1f}" '
           f'fill="{color}"/>')
    return shaft + tip


def dot(x, y, r=5, fill=BLUE):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'


def circle(x, y, r, stroke=LIGHT, fill='none', width=1.6, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{width}"{d}/>')


def rect(x, y, w, h, fill=PALE, stroke=BLUE, rx=7, width=1.6, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{width}"{d}/>')


def box(x, y, w, h, label, fill=PALE, stroke=BLUE, size=12, color=INK, rx=7):
    body = rect(x, y, w, h, fill, stroke, rx)
    lines = label.split('|')
    for i, text_line in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (len(lines) - 1) / 2) * (size + 3)
        body += t(x + w / 2, yy, text_line, color, size)
    return body


def poly(points, fill='none', stroke=BLUE, width=2.4, opacity=1.0, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)
    return (f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" '
            f'opacity="{opacity}"{d}/>')


def polyline(points, stroke=BLUE, width=2.6, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)
    return f'<polyline points="{pts}" fill="none" stroke="{stroke}" stroke-width="{width}"{d}/>'


def curve(fn, x0, x1, y0, y1, box_, n=200, stroke=BLUE, width=2.6, dash=''):
    """Plot y = fn(x) inside the pixel box (left, top, right, bottom)."""
    left, top, right, bottom = box_
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        try:
            y = fn(x)
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
        if y is None or y != y or y in (float('inf'), float('-inf')):
            continue
        if y < y0 - 1e-12 or y > y1 + 1e-12:
            if pts:
                break
            continue
        px = left + (x - x0) / (x1 - x0) * (right - left)
        py = bottom - (y - y0) / (y1 - y0) * (bottom - top)
        pts.append((px, py))
    return polyline(pts, stroke, width, dash)


def frame(xlab, ylab, box_=(70, 40, 640, 270), xticks=(), yticks=(),
          xfmt='{:.0f}', yfmt='{:.0f}', title='', xsize=12, tick_both=False):
    left, top, right, bottom = box_
    body = line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    for value, px in xticks:
        body += line(px, bottom, px, bottom + 6, GREY, 1.4)
        body += t(px, bottom + 20, xfmt.format(value), GREY, xsize)
    for value, py in yticks:
        body += line(left - 6, py, left, py, GREY, 1.4)
        body += t(left - 10, py + 4, yfmt.format(value), GREY, xsize, 'end')
    body += t((left + right) / 2, bottom + 44, xlab, GREY, 12)
    body += f'<g transform="translate(18,{(top + bottom) / 2}) rotate(-90)">' + \
            t(0, 0, ylab, GREY, 12) + '</g>'
    if title:
        body += t((left + right) / 2, 22, title, INK, 13, weight=700)
    return body


def grid(box_, cols=5, rows=4):
    left, top, right, bottom = box_
    body = ''
    for i in range(1, cols):
        x = left + (right - left) * i / cols
        body += line(x, top, x, bottom, '#e8eef8', 1)
    for j in range(1, rows):
        y = top + (bottom - top) * j / rows
        body += line(left, y, right, y, '#e8eef8', 1)
    return body


def scale_map(x0, x1, y0, y1, box_):
    left, top, right, bottom = box_
    return (lambda x: left + (x - x0) / (x1 - x0) * (right - left),
            lambda y: bottom - (y - y0) / (y1 - y0) * (bottom - top))


def legend(items, y=288, x0=100, dx=170, size=12):
    """Row of coloured line samples with labels: items are (colour, label[, dash])."""
    body = ''
    for i, item in enumerate(items):
        colour, label = item[0], item[1]
        dash = item[2] if len(item) > 2 else ''
        x = x0 + i * dx
        body += line(x, y, x + 26, y, colour, 3, dash)
        body += t(x + 33, y + 4, label, colour, size, 'start', 700)
    return body


def tag(x, y, label, colour=BLUE, size=11.5):
    width = max(30, 7.2 * len(label))
    return (rect(x, y - 14, width, 21, '#ffffff', colour, 4, 1.2)
            + t(x + width / 2, y + 1, label, colour, size, 'middle', 700))


def chart(key, title, caption_text, xlabel, ylabel, series, xr=(0, 1), yr=(0, 1),
          xticks=(), yticks=(), height=350, xfmt='{:.0f}', yfmt='{:.0f}', notes=()):
    """Standard plot: frame, grid, curves, automatic legend and a caption.

    series: list of (label, colour, function_of_x); the extra optional fourth
    element is a dash pattern. notes: (x, y, text, colour) in data coordinates.
    """
    top, bottom, left, right = 46, 208, 92, 640
    box_ = (left, top, right, bottom)
    X = lambda x: left + (x - xr[0]) / (xr[1] - xr[0]) * (right - left)
    Y = lambda y: bottom - (y - yr[0]) / (yr[1] - yr[0]) * (bottom - top)
    body = grid(box_, 4, 4) + frame(xlabel, ylabel, box_,
                                    [(v, X(v)) for v in xticks], [(v, Y(v)) for v in yticks],
                                    xfmt=xfmt, yfmt=yfmt)
    for item in series:
        dash = item[3] if len(item) > 3 else ''
        body += curve(item[2], xr[0], xr[1], yr[0], yr[1], box_, 240, item[1], 2.6, dash)
    for x, y, label, colour in notes:
        body += t(X(x), Y(y), label, colour, 11.5, 'start', 700)
    body += t(340, 22, title, INK, 13, weight=700)
    count = max(1, len(series))
    step = min(200, 540 // count)
    start = 100 if count >= 3 else 150
    items = [(s[1], s[0], s[3] if len(s) > 3 else '') for s in series]
    if len(items) <= 3:
        body += legend(items, 276, start, min(200, 520 // max(1, len(items))))
    else:
        half = (len(items) + 1) // 2
        body += legend(items[:half], 270, 100, 210)
        body += legend(items[half:], 292, 100, 210)
    body += t(340, height - 16, caption_text, GREY, 11.5)
    return wrap(key, title, caption_text, body, caption('Figure.', caption_text), height)


def flow(key, title, caption_text, steps, columns=None, height=250, width=600, left=40):
    """Chain of labelled boxes, left to right, with arrows between them."""
    count = len(steps)
    columns = columns or count
    rows = (count + columns - 1) // columns
    cell = (width - (columns - 1) * 18) / columns
    body = t(340, 28, title, INK, 13, weight=700)
    for index, label in enumerate(steps):
        row, col = divmod(index, columns)
        x = left + col * (cell + 18)
        y = 56 + row * (74 + 34)
        body += box(x, y, cell, 74, label, PALE if index < count - 1 else '#f0fdf7',
                    BLUE if index < count - 1 else GREEN, 11.5)
        if col < columns - 1 and index < count - 1:
            body += arrow(key, x + cell + 1, y + 37, x + cell + 16, y + 37, GREY, 2)
        if row < rows - 1 and col == columns - 1:
            body += arrow(key, x + cell / 2, y + 75, x + cell / 2, y + 108, GREY, 2)
    body += t(340, height - 16, caption_text, GREY, 11.5)
    return wrap(key, title, caption_text, body, caption('Figure.', caption_text), height)


def bars(key, title, caption_text, values, labels, colours=None, xlabel='', ylabel='',
         height=310, note='', log=None):
    left, top, right, bottom = 92, 52, 640, 218
    scale = (lambda v: log10(max(v, 1e-9))) if log else (lambda v: v)
    top_value = scale(max(values)) * 1.12 or 1
    low = min(0, scale(min(values)))
    body = line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    step = (right - left) / len(values)
    colours = colours or [BLUE]
    for i, v in enumerate(values):
        h = (bottom - top) * (scale(v) - low) / (top_value - low)
        colour = colours[i % len(colours)]
        body += rect(left + i * step + step * 0.16, bottom - h, step * 0.68, max(h, 1.5), colour, colour, 3, 0)
        body += t(left + i * step + step / 2, bottom + 18, labels[i], GREY, 11.5)
        body += t(left + i * step + step / 2, bottom - h - 8, f'{v:g}', INK, 11.5, weight=700)
    body += t(340, 24, title, INK, 13, weight=700)
    body += t(340, bottom + 44, xlabel, GREY, 12)
    if ylabel:
        body += f'<g transform="translate(22,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, ylabel, GREY, 12) + '</g>'
    if note:
        body += t(340, height - 16, note, GREY, 11.5)
    return wrap(key, title, caption_text, body, caption('Figure.', caption_text), height)


def caption(fig, text):
    return f'<strong>{fig}</strong> {text}'
