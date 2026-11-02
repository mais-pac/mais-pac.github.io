"""Load the per-topic figure and experiment packs.

Each syllabus topic contributes one file `scripts/ipho/_parts/NN.NN.py` that
defines a `FIGURES` dict of drawing functions and a `LABS` dict of experiment
shells. The packs are executed with the shared drawing and laboratory kit as
their globals, so a pack file stays short: it only describes one topic.

Component names must be unique across the whole programme. A silent override
would hide a figure behind a better-named one, so collisions raise.
"""
from pathlib import Path
import types

from ipho import figures as _figures
from ipho import labs as _labs

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / '_parts'


def _kit():
    kit = {}
    for module in (_figures, _labs):
        for name, value in vars(module).items():
            if name.startswith('_') or isinstance(value, types.ModuleType):
                continue
            kit[name] = value
    kit['FIGURES'] = {}
    kit['LABS'] = {}
    return kit


def load():
    figures, labs = {}, {}
    for path in sorted(PARTS.glob('*.py')):
        if path.name.startswith('__'):
            continue
        namespace = _kit()
        exec(compile(path.read_text(), str(path), 'exec'), namespace)
        for name, fn in namespace.get('FIGURES', {}).items():
            if name in figures:
                raise ValueError(f'Duplicate figure component {name!r} in {path.name}')
            figures[name] = fn
        for name, fn in namespace.get('LABS', {}).items():
            if name in labs:
                raise ValueError(f'Duplicate lab component {name!r} in {path.name}')
            labs[name] = fn
    return figures, labs


FIGURES, LABS = load()
