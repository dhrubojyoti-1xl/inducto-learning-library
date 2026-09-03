# -*- coding: utf-8 -*-
"""
The master index deck: one clickable map of all 39 modules.

Module rows link to the .pptx files by relative path, so the whole /output
folder must be kept together for the links to resolve.
"""

import json
import os

import theme as T
import visuals as V
from visuals import P
import components as C
import textfit as TF

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "output")

SPEC = {
    "module_code": "INDEX",
    "area": "01-ai-general",
    "filename": "00-master-index.pptx",
    "title": "Inducto Learning Library",
    "footer_title": "Master index",
    "subtitle": "Thirty-nine modules across five tracks. Start anywhere — "
                "every module works on its own.",
    "duration_min": 5,
    "audience": "Everybody",
    "motif": "network",
}

AREA_BLURB = {
    "01-ai-general": "What AI is, what it can do, and where it breaks.",
    "02-ai-daily-work": "The jobs you already do, done in less time.",
    "03-prompt-engineering": "Asking well enough to get a usable answer.",
    "04-professional-skills": "The skills AI assists and never replaces.",
    "05-security-privacy": "Keeping our data, and our customers', where it "
                           "belongs.",
}

PATHS = [
    {
        "anchor": "p_new",
        "name": "New Joiner — Week 1",
        "sub": "Six modules, about 100 minutes. Do these in your first week.",
        "why": "Enough to work safely and to get value from the tools on day "
               "one. Nothing here assumes you have used AI before.",
        "codes": ["AI-01", "SEC-01", "SEC-02", "SEC-07", "PS-01", "PS-02"],
    },
    {
        "anchor": "p_ai",
        "name": "AI Basics",
        "sub": "Six modules, about 110 minutes. The full grounding.",
        "why": "Take these in order. By the end you will know what these "
               "tools do, where they fail, and how to ask well.",
        "codes": ["AI-01", "AI-02", "AI-03", "AI-04", "AI-05", "PE-01"],
    },
    {
        "anchor": "p_mgr",
        "name": "Manager track",
        "sub": "Six modules, about 100 minutes. For anyone who runs work.",
        "why": "Communication, judgement and handover. The parts of the job "
               "that decide whether a team's work actually lands.",
        "codes": ["PS-01", "PS-04", "PS-06", "PS-07", "PS-08", "PS-09"],
    },
]


def load_decks():
    with open(os.path.join(OUT, "manifest.json"), encoding="utf-8") as fh:
        decks = json.load(fh)["decks"]
    return [d for d in decks if d["module_code"] != "INDEX"]


def area_slide(dk, area, decks):
    ac = T.accent(area)
    name = T.AREAS[area]["name"]
    sl = dk.new("a_" + area)
    dk.chrome(sl, name, "%d modules in this track" % len(decks))
    V.tbox(sl, T.MARGIN, T.RULE_Y + 0.06, T.CONTENT_W, 0.24,
           [P(AREA_BLURB[area] + "  Click any row to open that module.",
              T.F_BODY, T.SZ_CAPTION, T.GREY)], name="cell:areablurb",
           shrink=False)

    cols = 2 if len(decks) > 6 else 1
    rows = (len(decks) + cols - 1) // cols
    gap = 0.12
    top = T.BODY_TOP + 0.12
    rw = (T.CONTENT_W - (0.24 if cols == 2 else 0)) / cols
    rh = (T.BODY_BOTTOM - top - gap * (rows - 1)) / rows

    for i, d in enumerate(decks):
        c, r = divmod(i, rows)
        bx = T.MARGIN + c * (rw + 0.24)
        by = top + r * (rh + gap)
        sh = V.rrect(sl, bx, by, rw, rh, fill=T.SURFACE_ALT, radius=0.08,
                     name="nav:modulerow")
        V.rect(sl, bx, by, 0.06, rh, fill=ac, name="vis:rowbar")
        V.tbox(sl, bx + 0.24, by + 0.06, 0.86, rh - 0.12,
               [P(d["module_code"], T.F_HEAD, T.SZ_CAPTION, ac)], anchor="m",
               name="cell:rowcode", shrink=False)
        tw = rw - 1.10 - 0.90
        V.tbox(sl, bx + 1.16, by + 0.06, tw, rh - 0.12,
               [P(d["title"], T.F_HEAD, T.SZ_CAPTION + 2, T.INK)], anchor="m",
               name="cell:rowtitle")
        V.tbox(sl, bx + rw - 0.86, by + 0.06, 0.66, rh - 0.12,
               [P("%d min" % d["duration_min"], T.F_BODY, T.SZ_CAPTION,
                  T.GREY, align="r")], anchor="m", name="cell:rowmins",
               shrink=False)
        rel = d["file"].replace("output/", "")
        dk.file_link(sh, rel)
    return sl


def path_slide(dk, path, by_code):
    sl = dk.new(path["anchor"])
    dk.chrome(sl, "Learning path", path["name"])
    V.tbox(sl, T.MARGIN, T.RULE_Y + 0.06, T.CONTENT_W, 0.24,
           [P(path["sub"], T.F_BODY, T.SZ_CAPTION, T.GREY)],
           name="cell:pathsub", shrink=False)

    V.rrect(sl, T.MARGIN, T.BODY_TOP + 0.10, T.CONTENT_W, 0.86, fill=T.INK,
            radius=0.10, name="vis:pathwhy")
    V.icon(sl, "bulb", T.MARGIN + 0.30, T.BODY_TOP + 0.34, 0.40, dk.ac_lt)
    V.tbox(sl, T.MARGIN + 0.94, T.BODY_TOP + 0.22, T.CONTENT_W - 1.28, 0.62,
           [P(path["why"], T.F_BODY, T.SZ_CAPTION + 2, T.SURFACE)],
           anchor="m", name="body:pathwhy")

    top = T.BODY_TOP + 1.22
    n = len(path["codes"])
    gap = 0.12
    rh = (T.BODY_BOTTOM - top - gap * (n - 1)) / n
    for i, code in enumerate(path["codes"]):
        d = by_code[code]
        ac = T.accent(d["area"])
        by = top + i * (rh + gap)
        sh = V.rrect(sl, T.MARGIN, by, T.CONTENT_W, rh, fill=T.SURFACE_ALT,
                     radius=0.08, name="nav:pathrow")
        V.oval(sl, T.MARGIN + 0.22, by + (rh - 0.34) / 2, 0.34, 0.34, fill=ac,
               name="vis:pathnum")
        V.tbox(sl, T.MARGIN + 0.22, by + (rh - 0.34) / 2 + 0.075, 0.34, 0.22,
               [P(str(i + 1), T.F_HEAD, T.SZ_CHIP, T.SURFACE, align="c")],
               name="vis:pathnumtext", shrink=False)
        V.tbox(sl, T.MARGIN + 0.72, by + 0.06, 0.86, rh - 0.12,
               [P(code, T.F_HEAD, T.SZ_CAPTION, ac)], anchor="m",
               name="cell:pathcode", shrink=False)
        V.tbox(sl, T.MARGIN + 1.64, by + 0.06, T.cw(6), rh - 0.12,
               [P(d["title"], T.F_HEAD, T.SZ_CAPTION + 2, T.INK)], anchor="m",
               name="cell:pathtitle")
        V.tbox(sl, T.SLIDE_W - T.MARGIN - 1.10, by + 0.06, 0.90, rh - 0.12,
               [P("%d min" % d["duration_min"], T.F_BODY, T.SZ_CAPTION, T.GREY,
                  align="r")], anchor="m", name="cell:pathmins", shrink=False)
        dk.file_link(sh, d["file"].replace("output/", ""))
    return sl


def build():
    decks = load_decks()
    by_code = {d["module_code"]: d for d in decks}
    by_area = {}
    for d in decks:
        by_area.setdefault(d["area"], []).append(d)
    for a in by_area:
        by_area[a].sort(key=lambda d: d["module_code"])

    dk = C.Deck(SPEC)
    C.cover(dk)

    # ---- how to use ----
    sl = dk.new("how")
    dk.chrome(sl, "How to use this library", "Start anywhere. Nothing is "
                                             "locked.")
    V.checklist(sl, T.MARGIN, T.BODY_TOP, T.CONTENT_W, T.BODY_H, [
        "Every module stands alone. You never need to have done another one "
        "first.",
        "Open a deck and press F5 or Slide Show. The menu and quiz only work "
        "in that mode.",
        "Each module takes 15 to 20 minutes and ends with a recap card you "
        "can screenshot.",
        "The quizzes are for you. Nothing is recorded and nobody sees your "
        "answers.",
    ], dk.ac, cols=2)

    # ---- menu ----
    order = ["01-ai-general", "02-ai-daily-work", "03-prompt-engineering",
             "04-professional-skills", "05-security-privacy"]
    sections = [(T.AREAS[a]["name"], "%d modules" % len(by_area.get(a, [])),
                 "a_" + a) for a in order]
    sections += [(p["name"], p["sub"].split(".")[0], p["anchor"])
                 for p in PATHS]
    sl = dk.new("menu")
    dk.chrome(sl, "Interactive menu", "Tap a track or a learning path",
              nav=False)
    V.tbox(sl, T.MARGIN, T.RULE_Y + 0.06, T.CONTENT_W, 0.24,
           [P("Every slide has a Menu button in the top-right corner to bring "
              "you back here.", T.F_BODY, T.SZ_CAPTION, T.GREY)],
           name="cell:menuhint", shrink=False)
    n = len(sections)
    gap = 0.10
    top = T.BODY_TOP + 0.12
    rh = (T.BODY_BOTTOM - top - gap * (n - 1)) / n
    for i, (label, sub, anchor) in enumerate(sections):
        y = top + i * (rh + gap)
        ac = T.accent(order[i]) if i < 5 else dk.ac
        sh = V.rrect(sl, T.MARGIN, y, T.CONTENT_W, rh, fill=T.SURFACE_ALT,
                     radius=0.08, name="nav:menurow")
        V.rect(sl, T.MARGIN, y, 0.075, rh, fill=ac, name="vis:menubar")
        V.tbox(sl, T.MARGIN + 0.34, y + 0.06, 0.44, rh - 0.12,
               [P("%02d" % (i + 1), T.F_HEAD, T.SZ_NODE, ac)], anchor="m",
               name="vis:menunum", shrink=False)
        V.tbox(sl, T.MARGIN + 0.92, y + 0.06, T.cw(5), rh - 0.12,
               [P(label, T.F_HEAD, T.SZ_NODE + 2, T.INK)], anchor="m",
               name="cell:menulabel")
        V.tbox(sl, T.cx(7), y + 0.06, T.cw(4), rh - 0.12,
               [P(sub, T.F_BODY, T.SZ_CAPTION + 1, T.GREY)], anchor="m",
               name="cell:menusub")
        V.line(sl, T.SLIDE_W - T.MARGIN - 0.52, y + rh / 2,
               T.SLIDE_W - T.MARGIN - 0.28, y + rh / 2, ac, T.LINE_W,
               arrow=True, name="vis:menuarrow")
        dk.link(sh, anchor)

    for a in order:
        area_slide(dk, a, by_area.get(a, []))
    for p in PATHS:
        path_slide(dk, p, by_code)

    # ---- closing ----
    sl = dk.new("close")
    dk.chrome(sl, "Where to start", "If you only do one thing this week")
    V.rrect(sl, T.MARGIN, T.BODY_TOP, T.cw(7), 2.40, fill=T.INK, radius=0.10,
            name="vis:startcard")
    V.tbox(sl, T.MARGIN + 0.36, T.BODY_TOP + 0.34, T.cw(7) - 0.72, 0.28,
           [P("START HERE", T.F_HEAD, T.SZ_LABEL, dk.ac_lt, spc=1.4)],
           name="seclabel", shrink=False)
    V.tbox(sl, T.MARGIN + 0.36, T.BODY_TOP + 0.80, T.cw(7) - 0.72, 1.40,
           [P("AI Fundamentals, then What Never to Paste Into AI. Thirty-four "
              "minutes, and you can use these tools safely from that "
              "afternoon.", T.F_HEAD, 20, T.SURFACE)], name="body:startcard")
    V.checklist(sl, T.cx(8), T.BODY_TOP, T.cw(4), 2.40, [
        "AI-01 — AI Fundamentals",
        "SEC-07 — What Never to Paste Into AI",
    ], dk.ac, cols=1)
    V.tbox(sl, T.MARGIN, T.BODY_TOP + 2.70, T.CONTENT_W, 0.30,
           [P("KEEP THE FOLDER TOGETHER", T.F_HEAD, T.SZ_LABEL, dk.ac,
              spc=1.4)], name="seclabel", shrink=False)
    V.tbox(sl, T.MARGIN, T.BODY_TOP + 3.10, T.cw(9), 0.90,
           [P("The links on the track pages open the other decks by relative "
              "path. Move a deck out of its folder and its link stops "
              "working.", T.F_BODY, T.SZ_CAPTION + 2, T.INK_SOFT)],
           name="body:foldernote")

    path = os.path.join(OUT, SPEC["filename"])
    dk.save(path)
    return {
        "module_code": "INDEX",
        "title": SPEC["title"],
        "area": "index",
        "area_name": "Master index",
        "file": os.path.relpath(path, ROOT).replace("\\", "/"),
        "slide_count": len(dk.slides),
        "hidden_slides": 0,
        "duration_min": SPEC["duration_min"],
        "audience": SPEC["audience"],
        "is_index": True,
        "content_points": None,
        "external_links": list(dk.ext_links),
        "deck_links": sorted(getattr(dk, "file_links", [])),
        "company_input_needed": [],
    }


if __name__ == "__main__":
    info = build()
    print("built  %-7s %-42s %3d slides  %d deck links" %
          (info["module_code"], info["title"], info["slide_count"],
           len(info["deck_links"])))
