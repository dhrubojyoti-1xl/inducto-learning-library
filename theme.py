"""
Inducto Learning & Knowledge Library — single source of design truth.

Nothing in components.py, visuals.py or any content file may hard-code a
colour, a font size or a coordinate. Everything comes from here so all 40
decks are pixel-identical siblings.
"""

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor


# --------------------------------------------------------------------------
# Canvas + 12-column grid
# --------------------------------------------------------------------------
SLIDE_W = 13.333
SLIDE_H = 7.5

MARGIN = 0.55          # outer margin, nothing may touch the edge
GUTTER = 0.20
COLS = 12
CONTENT_W = SLIDE_W - 2 * MARGIN                       # 12.233
COL_W = (CONTENT_W - (COLS - 1) * GUTTER) / COLS       # 0.8361


def cx(i: int) -> float:
    """Left edge (inches) of column i (0-based)."""
    return MARGIN + i * (COL_W + GUTTER)


def cw(n: int) -> float:
    """Width (inches) spanning n columns."""
    return n * COL_W + (n - 1) * GUTTER


# Vertical anchors — identical on every slide of every deck.
SEC_LABEL_Y = 0.40
SEC_LABEL_H = 0.26
TITLE_Y = 0.72
TITLE_H = 0.82
RULE_Y = 1.64
BODY_TOP = 1.88
BODY_BOTTOM = 6.58
BODY_H = BODY_BOTTOM - BODY_TOP        # 4.70
FOOTER_Y = 6.88
FOOTER_H = 0.30

NAV_W = 1.10
NAV_H = 0.36
NAV_Y = 0.38
NAV_X = SLIDE_W - MARGIN - NAV_W       # 11.683

TITLE_W = cw(10)                       # stops well clear of the nav button


# --------------------------------------------------------------------------
# Palette — one deep neutral base, one accent per area, one alert, one
# success, two greys. No other colours exist.
# --------------------------------------------------------------------------
INK = RGBColor(0x10, 0x18, 0x26)         # deep neutral base
INK_SOFT = RGBColor(0x2A, 0x35, 0x47)    # base, one step up
GREY = RGBColor(0x5B, 0x67, 0x79)        # grey 1 — body/secondary text
GREY_LT = RGBColor(0xC9, 0xD1, 0xDE)     # grey 2 — rules and borders ONLY
SURFACE = RGBColor(0xFF, 0xFF, 0xFF)
SURFACE_ALT = RGBColor(0xF3, 0xF6, 0xFB)
ALERT = RGBColor(0xC6, 0x28, 0x28)
SUCCESS = RGBColor(0x1B, 0x7F, 0x4B)

# Greys that must never carry text (checked by verify.py)
NON_TEXT_COLOURS = {str(GREY_LT)}


# --------------------------------------------------------------------------
# Areas — folder, accent, module-code prefix
# --------------------------------------------------------------------------
AREAS = {
    "01-ai-general": {
        "name": "AI Courses",
        "prefix": "AI",
        "accent": RGBColor(0x2F, 0x4B, 0xC4),   # indigo
    },
    "02-ai-daily-work": {
        "name": "AI for Day-to-Day Work",
        "prefix": "DW",
        "accent": RGBColor(0x0E, 0x6E, 0x75),   # teal
    },
    "03-prompt-engineering": {
        "name": "Prompt Engineering",
        "prefix": "PE",
        "accent": RGBColor(0x6A, 0x2F, 0xA0),   # violet
    },
    "04-professional-skills": {
        "name": "Professional Skills",
        "prefix": "PS",
        "accent": RGBColor(0x8A, 0x5A, 0x00),   # bronze
    },
    "05-security-privacy": {
        "name": "Security & Data Privacy",
        "prefix": "SEC",
        "accent": RGBColor(0x7A, 0x12, 0x20),   # deep maroon
    },
}


def accent(area: str) -> RGBColor:
    return AREAS[area]["accent"]


# --------------------------------------------------------------------------
# Type — fonts that ship with every standard Windows install
# --------------------------------------------------------------------------
F_HEAD = "Segoe UI Semibold"
F_BODY = "Segoe UI"
F_MONO = "Consolas"          # prompt cards only; ships with Windows

SZ_TITLE = 34
SZ_COVER = 44
SZ_SUB = 22
SZ_LABEL = 13                # uppercase, tracked
SZ_BODY = 18
SZ_CAPTION = 12
SZ_STAT = 40
SZ_NODE = 14                 # diagram node labels
SZ_CHIP = 12

MIN_PT = 12                  # hard floor, enforced by verify.py


# --------------------------------------------------------------------------
# Shape language
# --------------------------------------------------------------------------
RADIUS = 0.06        # rounded-rectangle adjustment value (consistent corner)
LINE_W = Pt(1.5)     # one line weight for the whole icon system
LINE_W_THIN = Pt(1.0)
CARD_PAD = 0.28


# --------------------------------------------------------------------------
# Contrast maths — used at build time and again by verify.py
# --------------------------------------------------------------------------
def _lin(c: float) -> float:
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb) -> float:
    r, g, b = rgb[0], rgb[1], rgb[2]
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def on(bg) -> RGBColor:
    """Pick the readable text colour for a given background."""
    return SURFACE if contrast(SURFACE, bg) >= contrast(INK, bg) else INK


AA = 4.5
AA_TARGET = 5.2          # aim above the line so rounding never trips it


def _mix(c1, c2, t):
    return RGBColor(int(round(c1[0] + (c2[0] - c1[0]) * t)),
                    int(round(c1[1] + (c2[1] - c1[1]) * t)),
                    int(round(c1[2] + (c2[2] - c1[2]) * t)))


def _lighten_until(base, bg, target=5.2):
    for i in range(0, 101):
        cand = _mix(base, SURFACE, i / 100.0)
        if contrast(cand, bg) >= target:
            return cand
    return SURFACE


_LIGHT_CACHE = {}


def accent_light(area: str, bg=INK) -> RGBColor:
    """
    The accent, lightened just enough to clear AA on a dark ground.
    The full-strength accent is only 2.5:1 on INK, so dark cards use this.
    """
    key = (area, str(bg))
    if key in _LIGHT_CACHE:
        return _LIGHT_CACHE[key]
    out = _lighten_until(accent(area), bg, AA_TARGET)
    _LIGHT_CACHE[key] = out
    return out


# Secondary text on the deep base. Plain GREY is only 3.1:1 there.
GREY_DK = _lighten_until(GREY, INK, AA_TARGET)
