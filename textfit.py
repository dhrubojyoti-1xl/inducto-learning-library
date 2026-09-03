"""
Deterministic text measurement.

Used at build time (to pick a size that fits) and again by verify.py (to prove
nothing overflows). Because every text frame in this library sets explicit line
spacing and zero internal margins, predicted height is exact rather than a
guess: lines * line_spacing.
"""

import os
from functools import lru_cache
from PIL import ImageFont

FONT_FILES = {
    "Segoe UI": r"C:\Windows\Fonts\segoeui.ttf",
    "Segoe UI Semibold": r"C:\Windows\Fonts\seguisb.ttf",
    "Segoe UI Bold": r"C:\Windows\Fonts\segoeuib.ttf",
    "Consolas": r"C:\Windows\Fonts\consola.ttf",
}

# 1 pt = 1/72 in.  Render at 4x pt for sub-pixel accuracy.
SCALE = 4
LINE_FACTOR = 1.30       # line spacing we set explicitly on every paragraph


@lru_cache(maxsize=64)
def _font(name: str, pt: float):
    path = FONT_FILES.get(name, FONT_FILES["Segoe UI"])
    if not os.path.exists(path):
        path = FONT_FILES["Segoe UI"]
    return ImageFont.truetype(path, int(round(pt * SCALE)))


def text_w_in(text: str, name: str, pt: float, spc_pt: float = 0.0) -> float:
    """Width of a single line, in inches."""
    if not text:
        return 0.0
    f = _font(name, pt)
    w = f.getlength(text) / SCALE            # in points
    w += spc_pt * max(0, len(text) - 1)      # letter tracking
    return w / 72.0


def wrap(text: str, name: str, pt: float, width_in: float, spc_pt: float = 0.0):
    """Greedy word wrap. Returns list of lines."""
    if not text:
        return [""]
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if text_w_in(trial, name, pt, spc_pt) <= width_in or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def block_h_in(paras, width_in: float) -> float:
    """
    Height of a stack of paragraphs.
    paras: list of dicts {text, font, pt, space_after_pt, spc_pt, bullet_indent_in}
    """
    total = 0.0
    for p in paras:
        w = width_in - p.get("bullet_indent_in", 0.0)
        lines = wrap(p["text"], p["font"], p["pt"], w, p.get("spc_pt", 0.0))
        total += len(lines) * p["pt"] * LINE_FACTOR / 72.0
        total += p.get("space_after_pt", 0.0) / 72.0
    return total


def fits(paras, width_in: float, height_in: float, tol_in: float = 0.0) -> bool:
    return block_h_in(paras, width_in) <= height_in + tol_in


def longest_line_in(paras, width_in: float) -> float:
    """Widest rendered line — catches single unwrappable words."""
    widest = 0.0
    for p in paras:
        w = width_in - p.get("bullet_indent_in", 0.0)
        for ln in wrap(p["text"], p["font"], p["pt"], w, p.get("spc_pt", 0.0)):
            widest = max(widest, text_w_in(ln, p["font"], p["pt"], p.get("spc_pt", 0.0))
                         + p.get("bullet_indent_in", 0.0))
    return widest


def truncate(text: str, name: str, pt: float, width_in: float) -> str:
    """Shorten to fit one line, with an ellipsis. Used for displayed URLs."""
    if text_w_in(text, name, pt) <= width_in:
        return text
    ell = "…"
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if text_w_in(text[:mid] + ell, name, pt) <= width_in:
            lo = mid
        else:
            hi = mid - 1
    return text[:lo].rstrip() + ell
