# -*- coding: utf-8 -*-
"""
Generate the interactive HTML learning platform from the same content modules
that produce the PowerPoint decks.

    python sitegen.py

Nothing here invents training content. Every sentence written into the HTML is
read from content/areaNN/*.py — the single source that also builds the .pptx
files — so the two tracks cannot drift apart.

Outputs into site/:
    index.html                 the Learning Library (master index equivalent)
    assessment.html            the formal assessment (3 attempts, then HR)
    modules/<code>.html        one page per topic deck (39)
    data/library.js            window.INDUCTO_DATA for search/progress/index
    assets/images/*.jpg        hero images copied from assets/
"""

import html
import importlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build
import theme as T

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
MODDIR = os.path.join(SITE, "modules")
DATADIR = os.path.join(SITE, "data")
IMGDIR = os.path.join(SITE, "assets", "images")

BRAND = "Inducto"
LIB_NAME = "Inducto Learning &amp; Knowledge Library"

AREA_ORDER = ["01-ai-general", "02-ai-daily-work", "03-prompt-engineering",
              "04-professional-skills", "05-security-privacy"]

AREA_BLURB = {
    "01-ai-general": "What AI is, what it can do, and where it breaks.",
    "02-ai-daily-work": "The jobs you already do, done in less time.",
    "03-prompt-engineering": "Asking well enough to get a usable answer.",
    "04-professional-skills": "The skills AI assists and never replaces.",
    "05-security-privacy": "Keeping our data, and our customers', where it belongs.",
}

# Learning paths, identical to the ones in the master index deck.
PATHS = [
    {"id": "p_new", "name": "New Joiner — Week 1",
     "sub": "Six modules, about 100 minutes. Do these in your first week.",
     "codes": ["AI-01", "SEC-01", "SEC-02", "SEC-07", "PS-01", "PS-02"]},
    {"id": "p_ai", "name": "AI Basics",
     "sub": "Six modules, about 110 minutes. The full grounding.",
     "codes": ["AI-01", "AI-02", "AI-03", "AI-04", "AI-05", "PE-01"]},
    {"id": "p_mgr", "name": "Manager track",
     "sub": "Six modules, about 100 minutes. For anyone who runs work.",
     "codes": ["PS-01", "PS-04", "PS-06", "PS-07", "PS-08", "PS-09"]},
]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def e(s):
    """Escape for HTML text and double-quoted attributes."""
    return html.escape("" if s is None else str(s), quote=True)


def slug(code):
    return code.lower().replace("-", "")


def yt_id(url):
    m = re.search(r"[?&]v=([A-Za-z0-9_\-]{6,})", url or "")
    return m.group(1) if m else None


def first_sentence(text, limit=170):
    text = " ".join(str(text).split())
    cut = text.find(". ")
    if 40 <= cut <= limit:
        return text[:cut + 1]
    return text if len(text) <= limit else text[:limit - 1].rsplit(" ", 1)[0] + "…"


# ---------------------------------------------------------------------------
# visual renderers — each source slide visual becomes a native HTML component
# ---------------------------------------------------------------------------
def v_flow(v, ctx):
    out = ['<div class="flowsteps">']
    for i, (t, sub) in enumerate(v["steps"], 1):
        out.append(
            '<div class="flowstep"><div class="flowstep__n">%d</div>'
            "<h4>%s</h4><p>%s</p></div>" % (i, e(t), e(sub)))
    out.append("</div>")
    return "".join(out)


def v_nested(v, ctx):
    out = ['<div class="nest">']
    for i, layer in enumerate(v["layers"]):
        out.append('<div class="nest__layer" data-depth="%d">'
                   '<div class="nest__label">%s</div>'
                   '<p class="nest__sub">%s</p>' % (i, e(layer["label"]), e(layer["sub"])))
    out.append("</div>" * len(v["layers"]))
    out.append("</div>")
    if v.get("note"):
        out.append('<p class="note" style="margin-top:16px">%s</p>' % e(v["note"]))
    return "".join(out)


def v_iconrow(v, ctx):
    out = ['<div class="tiles">']
    for it in v["items"]:
        out.append('<div class="tile"><span class="tile__mark" aria-hidden="true"></span>'
                   "<h4>%s</h4><p>%s</p></div>" % (e(it["label"]), e(it["sub"])))
    out.append("</div>")
    return "".join(out)


TONE_CLASS = {"good": "panel--good", "bad": "panel--bad",
              "accent": "panel--accent", "neutral": ""}


def v_split(v, ctx):
    out = ['<div class="split">']
    for side in ("left", "right"):
        s = v[side]
        out.append('<div class="panel %s">' % TONE_CLASS.get(s.get("tone"), ""))
        out.append('<span class="chip">%s</span>' % e(s["tag"]))
        out.append("<h4>%s</h4><ul>" % e(s["title"]))
        for it in s["items"]:
            out.append("<li><span>%s</span></li>" % e(it))
        out.append("</ul></div>")
    out.append("</div>")
    return "".join(out)


BRANCH_CLASS = {"good": "branch--good", "bad": "branch--bad",
                "neutral": "branch--neutral", "ok": "branch--neutral"}


def v_tree(v, ctx):
    out = ['<div class="tree">',
           '<div class="tree__q">%s</div>' % e(v["question"]),
           '<div class="tree__branches">']
    for key in ("yes", "no"):
        b = v[key]
        out.append('<div class="branch %s">' % BRANCH_CLASS.get(b.get("tone"), ""))
        out.append('<div class="branch__path">%s</div>' % e(b["path"]))
        out.append("<h4>%s</h4><p>%s</p></div>" % (e(b["label"]), e(b["detail"])))
    out.append("</div></div>")
    return "".join(out)


def prompt_card(text, caption, header, ctx):
    cid = ctx.new_id("p")
    out = ['<div class="prompt"><div class="prompt__bar"><span>%s</span>'
           '<button type="button" class="copybtn" data-copy="%s">Copy</button></div>'
           '<div class="prompt__body" id="%s">%s</div>'
           % (e(header or "Copy this prompt"), cid, cid, e(text))]
    if caption:
        out.append('<div class="prompt__cap">%s</div>' % e(caption))
    out.append("</div>")
    return "".join(out)


def v_steps(v, ctx):
    steps = ['<ol class="numlist">']
    for it in v["items"]:
        steps.append("<li>%s</li>" % e(it))
    steps.append("</ol>")
    steps = "".join(steps)
    if not v.get("prompt"):
        return steps
    return ('<div class="split" style="align-items:start"><div>%s</div><div>%s</div></div>'
            % (steps, prompt_card(v["prompt"], v.get("caption"), "Copy this prompt", ctx)))


def v_beforeafter(v, ctx):
    out = ['<div class="ba">']
    for tag, items, cls in ((v["bad_tag"], v["bad"], "panel--bad"),
                            (v["good_tag"], v["good"], "panel--good")):
        out.append('<div class="panel %s"><span class="chip">%s</span><ul>' % (cls, e(tag)))
        for it in items:
            out.append("<li><span>%s</span></li>" % e(it))
        out.append("</ul></div>")
    out.append("</div>")
    if v.get("note"):
        out.append('<p class="ba__note">%s</p>' % e(v["note"]))
    return "".join(out)


def v_prompt(v, ctx):
    out = [prompt_card(v["text"], v.get("caption"), v.get("header"), ctx)]
    if v.get("why"):
        out.append('<div class="outcard" style="margin-top:16px">'
                   '<div class="step__eyebrow">Why this works</div><ul class="ticks">')
        for w in v["why"]:
            out.append("<li>%s</li>" % e(w))
        out.append("</ul></div>")
    return "".join(out)


def v_prompt_out(v, ctx):
    out = ['<div class="split" style="align-items:start"><div>']
    out.append(prompt_card(v["text"], v.get("caption"), v.get("header"), ctx))
    out.append('</div><div class="outcard"><div class="step__eyebrow">%s</div><ul class="ticks">'
               % e(v.get("out_title") or "What comes back"))
    for o in v["out"]:
        out.append("<li>%s</li>" % e(o))
    out.append("</ul></div></div>")
    return "".join(out)


def v_checklist(v, ctx):
    ban = v.get("mark") == "ban"
    out = ['<ul class="checklist">']
    for it in v["items"]:
        key = "%s-%d" % (ctx.anchor, ctx.next_check())
        out.append('<li class="checkitem%s"><label>'
                   '<input type="checkbox" data-key="%s"><span>%s</span></label></li>'
                   % (" checkitem--ban" if ban else "", e(key), e(it)))
    out.append("</ul>")
    if ban:
        out.append('<p class="note" style="margin-top:12px">Tick each one only '
                   "once you are sure you never do it.</p>")
    return "".join(out)


def v_bandlist(v, ctx):
    tone = v.get("tone")
    cls = "band band--accent" if tone in ("accent", "good", "neutral") else "band"
    out = ['<div class="%s"><strong>%s</strong>' % (cls, e(v["headline"]))]
    if v.get("sub"):
        out.append("<p>%s</p>" % e(v["sub"]))
    out.append("</div>")
    out.append('<ul class="ticks ticks--plain">')
    for it in v["items"]:
        out.append("<li>%s</li>" % e(it))
    out.append("</ul>")
    return "".join(out)


def v_mistakes(v, ctx):
    out = ['<div class="mistakes">']
    for i, (what, why) in enumerate(v["items"], 1):
        out.append('<div class="mistake"><div class="mistake__n">%d</div>'
                   '<div class="mistake__what">%s</div>'
                   '<div class="mistake__why">%s</div></div>' % (i, e(what), e(why)))
    out.append("</div>")
    return "".join(out)


RENDER = {
    "flow": v_flow, "nested": v_nested, "iconrow": v_iconrow, "split": v_split,
    "tree": v_tree, "steps": v_steps, "beforeafter": v_beforeafter,
    "prompt": v_prompt, "prompt_out": v_prompt_out, "checklist": v_checklist,
    "bandlist": v_bandlist, "mistakes": v_mistakes,
}


class Ctx(object):
    """Per-page counters so generated ids are unique and stable."""

    def __init__(self):
        self.n = 0
        self.checks = 0
        self.anchor = "s"

    def new_id(self, pre):
        self.n += 1
        return "%s%d" % (pre, self.n)

    def next_check(self):
        self.checks += 1
        return self.checks


# ---------------------------------------------------------------------------
# page chrome
# ---------------------------------------------------------------------------
def head(title, desc, up, area, extra_css=""):
    return (
        "<!doctype html>\n"
        '<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="description" content="%s">\n'
        '<meta name="theme-color" content="#101826">\n'
        "<title>%s</title>\n"
        '<link rel="preconnect" href="https://www.youtube-nocookie.com">\n'
        '<link rel="stylesheet" href="%scss/inducto.css">\n%s'
        "</head>\n" % (e(desc), e(title), up, extra_css))


def topbar(up, right_html):
    return (
        '<a class="skip" href="#main">Skip to content</a>\n'
        '<header class="topbar"><div class="wrap topbar__in">'
        '<a class="brand" href="%sindex.html">'
        '<span class="brand__mark" aria-hidden="true"></span>%s</a>'
        '<span class="topbar__spacer"></span>%s</div></header>\n'
        % (up, BRAND, right_html))


def foot(up, extra_js=""):
    return (
        '<footer class="foot"><div class="wrap">'
        "<p>%s · Internal learning material. "
        "Content mirrors the PowerPoint library module for module.</p>"
        '<p>Course owner and issuing body: [COMPANY INPUT NEEDED: name of the '
        "team that owns this training].</p></div></footer>\n"
        '<div id="live" class="sr" role="status" aria-live="polite"></div>\n'
        '<script src="%sjs/progress.js"></script>\n%s'
        "</body>\n</html>\n" % (LIB_NAME, up, extra_js))


# ---------------------------------------------------------------------------
# module page
# ---------------------------------------------------------------------------
def group_slides(deck):
    """Split the flat slide list into the sections declared by the deck."""
    groups, cur = [], None
    for s in deck["slides"]:
        if s.get("anchor") or cur is None:
            cur = {"anchor": s.get("anchor") or "s_%d" % len(groups), "slides": []}
            groups.append(cur)
        cur["slides"].append(s)
    return {g["anchor"]: g["slides"] for g in groups}


def section_plan(deck):
    """Every scrollable section on the page, in order, with its rail label."""
    plan = [("why", "Why this matters"), ("outcomes", "What you'll be able to do")]
    for name, sub, anchor in deck["sections"]:
        plan.append((anchor, name))
    plan += [("check", "Knowledge check"), ("recap", "Recap"),
             ("toolkit", "Toolkit"), ("glossary", "Glossary")]
    return plan


def render_module(deck, prev_mod, next_mod, gaps):
    ctx = Ctx()
    code = deck["module_code"]
    area = deck["area"]
    ainfo = T.AREAS[area]
    groups = group_slides(deck)
    plan = section_plan(deck)
    subs = {a: sub for (n, sub, a) in deck["sections"]}

    o = []
    o.append(head("%s · %s" % (deck["title"], BRAND),
                  first_sentence(deck["subtitle"]), "../", area))
    o.append('<body data-area="%s">\n' % e(area))
    o.append(topbar("../",
                    '<span class="topbar__meta"><span id="modpct">0%</span> of this module</span>'
                    '<a class="btn btn--sm btn--quiet" href="../index.html">All modules</a>'))
    o.append('<main id="main" class="wrap">\n')
    o.append('<nav class="crumb" aria-label="Breadcrumb"><a href="../index.html">Library</a> / '
             '<a href="../index.html#tracks">%s</a> / %s</nav>\n'
             % (e(ainfo["name"]), e(code)))
    o.append('<div class="mod" data-module-id="%s" data-section-count="%d">\n'
             % (e(code), len(plan)))

    # ---- rail ----
    o.append('<nav class="rail" aria-label="Module sections"><div class="rail__title">'
             "In this module</div><ol>")
    for anchor, label in plan:
        o.append('<li><a href="#%s"><span class="rail__tick" aria-hidden="true"></span>'
                 "<span>%s</span></a></li>" % (e(anchor), e(label)))
    o.append("</ol></nav>\n<div>\n")

    # ---- header ----
    o.append('<header class="mhead">')
    img = deck.get("cover_image")
    if img:
        fn = os.path.basename(img)
        o.append('<div class="mhead__hero"><img src="../assets/images/%s" alt="" '
                 'width="1280" height="560" fetchpriority="high"></div>' % e(fn))
    else:
        o.append('<div class="mhead__hero mhead__motif" data-motif="%s" aria-hidden="true">'
                 '<span>%s</span></div>' % (e(deck.get("motif", "network")), e(code)))
    o.append('<div class="chiprow" style="margin-bottom:16px">'
             '<span class="chip chip--solid">%s</span>'
             '<span class="chip">%s</span><span class="chip">%d min</span>'
             '<span class="chip">%s</span></div>'
             % (e(code), e(ainfo["name"]), deck["duration_min"], e(deck["audience"])))
    o.append("<h1>%s</h1>" % e(deck["title"]))
    o.append('<p class="lead">%s</p>' % e(deck["subtitle"]))
    o.append('<div class="bar" id="modbarwrap" role="progressbar" aria-valuemin="0" '
             'aria-valuemax="100" aria-valuenow="0" aria-label="Module progress">'
             '<div class="bar__fill" id="modbar" style="width:0%"></div></div>')
    o.append("</header>\n")

    # ---- why ----
    w = deck["why"]
    o.append('<section class="step" id="why"><div class="step__eyebrow">Why this matters</div>'
             "<h2>%s</h2>" % e(w["title"]))
    o.append('<div class="why"><div><div class="why__story"><p>%s</p></div>'
             '<div class="why__cost">%s</div></div>'
             '<div class="why__fix"><div class="step__eyebrow">What changes</div>'
             "<p style=\"margin:0\">%s</p></div></div></section>\n"
             % (e(w["scenario"]), e(w["cost"]), e(w["fix"])))

    # ---- outcomes ----
    o.append('<section class="step" id="outcomes">'
             '<div class="step__eyebrow">What you\'ll be able to do</div>'
             "<h2>By the end of this module</h2><ul class=\"objectives\">")
    for i, (icon, text) in enumerate(deck["outcomes"], 1):
        o.append('<li><span class="n" aria-hidden="true">%d</span><span>%s</span></li>'
                 % (i, e(text)))
    o.append("</ul></section>\n")

    # ---- content sections ----
    for name, sub, anchor in deck["sections"]:
        ctx.anchor = anchor
        if anchor == "scenario":
            o.append(render_scenario(deck, name, sub))
            continue
        if anchor == "video":
            o.append(render_video(deck, name, sub, gaps))
            continue
        o.append('<section class="step" id="%s"><div class="step__eyebrow">%s</div>'
                 "<h2>%s</h2>" % (e(anchor), e(name), e(sub)))
        for s in groups.get(anchor, []):
            o.append('<div class="lesson"><h3>%s</h3>' % e(s["title"]))
            if s.get("lead"):
                o.append('<p class="lead">%s</p>' % e(s["lead"]))
            v = s.get("visual")
            if v:
                o.append(RENDER[v["type"]](v, ctx))
            if s.get("gloss"):
                o.append('<p class="glosslink">Terms on this page: %s</p>'
                         % ", ".join('<a href="#glossary">%s</a>' % e(g) for g in s["gloss"]))
            o.append("</div>")
        o.append("</section>\n")

    # ---- knowledge check ----
    o.append(render_quiz(deck))

    # ---- recap ----
    r = deck["recap"]
    o.append('<section class="step" id="recap"><div class="step__eyebrow">Recap</div>'
             '<h2>%s</h2><div class="recap">' % e(r["title"]))
    for t, d in r["points"]:
        o.append('<div class="recap__item"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d)))
    o.append('</div><p class="oneliner">%s</p></section>\n' % e(r["oneliner"]))

    # ---- toolkit ----
    tk = deck["toolkit"]
    o.append('<section class="step" id="toolkit"><div class="step__eyebrow">Toolkit</div>'
             '<h2>%s</h2><div class="tiles">' % e(tk["title"]))
    for icon, t, d in tk["templates"]:
        o.append('<div class="tile"><span class="tile__mark" aria-hidden="true"></span>'
                 "<h3>%s</h3><p>%s</p></div>" % (e(t), e(d)))
    o.append("</div>")
    o.append('<div class="rail__title" style="margin-top:24px">Tools referenced</div>'
             '<div class="linklist">')
    for label, url in tk["links"]:
        o.append('<a class="linkitem" href="%s" target="_blank" rel="noopener noreferrer">'
                 "<span>%s</span><small>%s ↗</small></a>"
                 % (e(url), e(label), e(re.sub(r"^https?://", "", url).rstrip("/"))))
    o.append("</div>")
    o.append('<p class="note" style="margin-top:20px"><strong>Next:</strong> %s</p>'
             % e(tk["next"]))
    o.append("</section>\n")

    # ---- glossary ----
    o.append('<section class="step" id="glossary"><div class="step__eyebrow">Glossary</div>'
             '<h2>Words used in this module</h2><div class="gloss">')
    for term, definition in deck["glossary"]:
        o.append('<div class="card" style="padding:16px"><div class="gloss__t">%s</div>'
                 '<div class="gloss__d">%s</div></div>' % (e(term), e(definition)))
    o.append("</div></section>\n")

    # ---- completion ----
    o.append('<section class="step" id="finish">'
             '<div class="done" id="doneBox" hidden>'
             '<div class="done__tick" aria-hidden="true">✓</div>'
             "<h2>Module complete</h2>"
             "<p class=\"prose\" style=\"margin:0 auto\">This module is marked complete in "
             "your progress record. It stays on your device unless your organisation "
             "connects a learning system.</p><div class=\"done__actions\">")
    if next_mod:
        o.append('<a class="btn" href="%s.html">Next: %s →</a>'
                 % (e(slug(next_mod["module_code"])), e(next_mod["title"])))
    o.append('<a class="btn btn--ghost" href="../index.html">Back to library</a>'
             '<a class="btn btn--ghost" href="../assessment.html">Final assessment</a>'
             "</div></div>")
    o.append('<p style="text-align:center"><button class="btn" id="completeBtn">'
             "Mark this module complete</button></p>")
    o.append("</section>\n")

    # ---- prev / next ----
    o.append('<nav class="linklist" style="margin-top:32px" aria-label="Module navigation">')
    if prev_mod:
        o.append('<a class="linkitem" href="%s.html"><span>← Previous: %s</span>'
                 "<small>%s</small></a>"
                 % (e(slug(prev_mod["module_code"])), e(prev_mod["title"]),
                    e(prev_mod["module_code"])))
    if next_mod:
        o.append('<a class="linkitem" href="%s.html"><span>Next: %s →</span>'
                 "<small>%s</small></a>"
                 % (e(slug(next_mod["module_code"])), e(next_mod["title"]),
                    e(next_mod["module_code"])))
    o.append("</nav>\n")

    o.append("</div>\n</div>\n</main>\n")
    o.append(foot("../", '<script src="../js/module.js"></script>\n'))
    return "".join(o), len(plan)


def render_scenario(deck, name, sub):
    sc = deck["scenario"]
    o = ['<section class="step" id="scenario"><div class="step__eyebrow">%s</div>'
         "<h2>%s</h2>" % (e(name), e(sc["title"])),
         '<p class="lead">%s</p>' % e(sub)]
    o.append('<div class="q__stem">%s</div>' % e(sc["situation"]))
    o.append('<div data-scenario><div class="q__opts" role="group" '
             'aria-label="Choose what you would do">')
    for i, c in enumerate(sc["choices"]):
        o.append('<button type="button" class="opt" data-tone="%s" data-headline="%s" '
                 'data-consequence="%s" data-rule="%s">'
                 '<span class="opt__k">%s</span><span>%s</span></button>'
                 % (e(c["tone"]), e(c["headline"]), e(c["consequence"]), e(c["rule"]),
                    "ABCDE"[i], e(c["text"])))
    o.append('</div><div class="fb"></div></div>')
    o.append('<p class="note" style="margin-top:16px">Nothing is scored here. '
             "Pick one, read what happens, then try the others.</p>")
    o.append("</section>\n")
    return "".join(o)


def render_video(deck, name, sub, gaps):
    v = deck.get("video")
    o = ['<section class="step" id="video"><div class="step__eyebrow">%s</div>' % e(name)]
    if not v or not yt_id(v.get("url")):
        gaps.append({"module": deck["module_code"], "title": deck["title"],
                     "reason": "No verified video URL in the source content module."})
        o.append("<h2>%s</h2>" % e(sub))
        o.append('<div class="video__gap"><strong>No video is attached to this module.'
                 "</strong><p style=\"margin:8px 0 0\">Nothing has been substituted. "
                 "Recorded in VIDEO_GAPS.md.</p></div></section>\n")
        return "".join(o)
    vid = yt_id(v["url"])
    o.append("<h2>%s</h2>" % e(v.get("heading") or sub))
    o.append('<p class="lead">%s</p>' % e(sub))
    o.append('<div class="video__frame"><iframe loading="lazy" '
             'src="https://www.youtube-nocookie.com/embed/%s?rel=0" '
             'title="%s" allow="accelerometer; clipboard-write; encrypted-media; '
             'picture-in-picture" allowfullscreen></iframe></div>' % (e(vid), e(v["title"])))
    o.append('<div class="video__meta"><span class="chip">%s</span>'
             '<span class="chip">%s</span>'
             '<a class="chip" href="%s" target="_blank" rel="noopener noreferrer">'
             "Open on YouTube ↗</a></div>" % (e(v["channel"]), e(v["duration"]), e(v["url"])))
    o.append('<p style="margin-top:16px"><strong>%s</strong></p>' % e(v["title"]))
    o.append('<p class="note">%s</p>' % e(v["note"]))
    o.append('<ul class="ticks ticks--plain">')
    for h in v["how"]:
        o.append("<li>%s</li>" % e(h))
    o.append("</ul></section>\n")
    return "".join(o)


def render_quiz(deck):
    o = ['<section class="step" id="check">'
         '<div class="step__eyebrow">Knowledge check</div>'
         "<h2>Check what stuck</h2>"
         '<p class="prose">Practice, not the formal assessment. Wrong answers are '
         "explained one by one, and you can retry any question as often as you like. "
         'The graded test is on the <a href="../assessment.html">assessment page</a>.</p>'
         "<div data-quiz>"]
    for q in deck["quiz"]:
        o.append('<div class="q" data-remember="%s"><h3>%s</h3>' % (e(q["remember"]), e(q["q"])))
        if q.get("stem"):
            o.append('<div class="q__stem">%s</div>' % e(q["stem"]))
        o.append('<div class="q__opts" role="group" aria-label="Answer options">')
        for i, a in enumerate(q["answers"]):
            o.append('<button type="button" class="opt" data-correct="%s" data-why="%s">'
                     '<span class="opt__k">%s</span><span>%s</span></button>'
                     % ("1" if a["ok"] else "0", e(a["why"]), "ABCDE"[i], e(a["text"])))
        o.append('</div><div class="fb"></div></div>')
    o.append('</div><div class="qscore" id="qscore" hidden></div></section>\n')
    return "".join(o)


# ---------------------------------------------------------------------------
# index page
# ---------------------------------------------------------------------------
def render_index(mods, totals):
    o = [head("%s" % LIB_NAME.replace("&amp;", "&"),
              "Thirty-nine self-guided modules on AI, prompting, professional "
              "skills and data security.", "", "01-ai-general")]
    o.append('<body data-area="01-ai-general">\n')
    o.append(topbar("", '<a class="btn btn--sm btn--quiet" href="journey.html">'
                        'Mandatory Journey</a>'
                        '<a class="btn btn--sm btn--quiet" href="#optional">Optional '
                        'library</a>'
                        '<a class="btn btn--sm" href="assessment.html">Assessment</a>'))
    o.append('<main id="main">\n')

    # hero
    o.append('<section class="hero"><div class="wrap hero__grid"><div>'
             "<h1>%s</h1>"
             "<p>Every employee completes the 16-stop Mandatory Journey — about "
             "148 minutes. Go deeper any time in the %d-module Optional Extended "
             "Library below.</p>"
             '<div class="chiprow" style="margin-top:20px">'
             '<span class="chip" style="color:#c9d1de;border-color:rgba(255,255,255,.25)">'
             "16 mandatory stops</span>"
             '<span class="chip" style="color:#c9d1de;border-color:rgba(255,255,255,.25)">'
             "%d-module library</span>"
             '<span class="chip" style="color:#c9d1de;border-color:rgba(255,255,255,.25)">'
             "5 tracks</span></div></div>"
             % (LIB_NAME, totals["modules"], totals["modules"]))
    o.append('<div class="hero__stats">'
             '<div class="stat"><span class="stat__n" id="statDone">0</span>'
             '<span class="stat__l">Completed</span></div>'
             '<div class="stat"><span class="stat__n" id="statProg">0</span>'
             '<span class="stat__l">In progress</span></div>'
             '<div class="stat"><span class="stat__n" id="statPct">0%%</span>'
             '<span class="stat__l">Overall</span></div>'
             '<div class="stat"><span class="stat__n">%d</span>'
             '<span class="stat__l">Lessons</span></div></div>' % totals["lessons"])
    o.append("</div></section>\n")

    o.append('<div class="wrap">\n')
    o.append('<div class="resume resume--journey" id="journeyResume" '
             'style="margin-top:calc(var(--sp-6) * -1 - 8px)"></div>\n')
    o.append('<div class="resume" id="resume" style="margin-top:16px"></div>\n')
    o.append('<div class="bar" id="overallBarWrap" role="progressbar" aria-valuemin="0" '
             'aria-valuemax="100" aria-valuenow="0" aria-label="Overall progress" '
             'style="margin-top:24px"><div class="bar__fill" id="overallBar" '
             'style="width:0%"></div></div>')
    o.append('<p class="note" id="certState" style="margin-top:12px"></p>')
    o.append('<p class="note" id="storageWarn" hidden>Your browser is blocking local '
             "storage, so progress cannot be saved on this device. Everything still "
             "works — it just will not be remembered.</p>")

    # search
    o.append('<div class="search"><span class="search__icon" aria-hidden="true">⌕</span>'
             '<label class="sr" for="q">Search the library</label>'
             '<input id="q" type="search" autocomplete="off" '
             'placeholder="Search modules, lessons, terms and rules — press / to focus">'
             '</div><div class="search__out" id="qout" role="region" '
             'aria-live="polite" aria-label="Search results"></div>\n')

    # learning paths
    o.append('<section style="margin-top:48px" id="optional">'
             '<span class="chip">OPTIONAL · EXTENDED LIBRARY</span>'
             '<h2 style="margin-top:10px">Suggested paths through the full '
             "library</h2>"
             '<p class="prose">The Mandatory Journey above is required. '
             "Everything below is optional and is never required for "
             "mandatory completion: 20 of these 39 modules go deeper on a "
             "topic the journey already condensed, and 19 cover ground the "
             "journey does not touch at all. If you would rather be told "
             "what to take first, pick a path."
             "</p><div class=\"grid grid--3\">")
    by_code = {m["code"]: m for m in mods}
    for p in PATHS:
        items = [by_code[c] for c in p["codes"] if c in by_code]
        mins = sum(m["duration"] for m in items)
        o.append('<div class="card"><div class="step__eyebrow">Path</div>'
                 "<h3>%s</h3><p style=\"color:var(--grey);font-size:.92rem\">%s</p>"
                 '<ol class="numlist numlist--tight">' % (e(p["name"]), e(p["sub"])))
        for m in items:
            o.append('<li><a href="%s">%s</a></li>' % (e(m["href"]), e(m["title"])))
        o.append('</ol><p class="note" style="margin:0">%d modules · about %d minutes</p>'
                 "</div>" % (len(items), mins))
    o.append("</div></section>\n")

    # tracks
    o.append('<div id="tracks"></div>\n')

    # assessment card
    o.append('<section style="margin-top:48px"><div class="card">'
             '<div class="step__eyebrow">Formal assessment</div>'
             "<h2>Final assessment</h2>"
             '<p class="prose">A graded test drawn from across the library. '
             "You get three attempts. If all three are unsuccessful, further action "
             "requires an HR decision. The knowledge checks inside modules are "
             "practice and do not count towards this.</p>"
             '<p><a class="btn" href="assessment.html">Go to the assessment</a> '
             '<button class="btn btn--ghost" id="resetBtn" type="button">'
             "Reset my progress</button></p></div></section>\n")

    # glossary
    o.append('<section style="margin-top:48px"><h2>Glossary '
             '<span class="track__count">(<span id="glossCount">0</span> terms)</span></h2>'
             '<div class="gloss" id="glossary" style="margin-top:16px"></div></section>\n')

    o.append("</div>\n</main>\n")
    o.append(foot("", '<script src="data/library.js"></script>\n'
                      '<script src="js/library.js"></script>\n'))
    return "".join(o)


def render_assessment(totals):
    o = [head("Final assessment · " + BRAND,
              "The graded Inducto assessment. Three attempts.", "", "01-ai-general")]
    o.append('<body data-area="01-ai-general">\n')
    o.append(topbar("", '<a class="btn btn--sm btn--quiet" href="index.html">Library</a>'))
    o.append('<main id="main" class="wrap">\n'
             '<nav class="crumb"><a href="index.html">Library</a> / Final assessment</nav>\n'
             '<h1 style="margin-top:24px">Final assessment</h1>\n'
             '<div id="assessment" style="margin-top:24px"></div>\n'
             "</main>\n")
    o.append(foot("", '<script src="data/library.js"></script>\n'
                      '<script src="js/assessment.js"></script>\n'))
    return "".join(o)


# ---------------------------------------------------------------------------
# data file
# ---------------------------------------------------------------------------
def build_data(decks, sect_counts):
    modules, search, glossary, pool = [], [], [], []
    seen_terms = {}
    for d in decks:
        code = d["module_code"]
        href = "modules/%s.html" % slug(code)
        modules.append({
            "id": code, "code": code, "area": d["area"],
            "title": d["title"], "summary": first_sentence(d["subtitle"]),
            "duration": d["duration_min"], "audience": d["audience"],
            "href": href, "sectionCount": sect_counts[code],
            "lessons": len(d["slides"]),
            "video": bool(d.get("video") and yt_id(d["video"].get("url"))),
        })
        search.append({"k": "module", "t": d["title"], "s": first_sentence(d["subtitle"]),
                       "m": code, "h": href})
        # Only the first slide of a section carries an anchor, so carry the
        # current one forward: every lesson must link to its own section.
        anchor = "why"
        for s in d["slides"]:
            anchor = s.get("anchor") or anchor
            search.append({"k": "lesson", "t": s["title"],
                           "s": first_sentence(s.get("lead") or "", 110),
                           "m": code, "h": href + "#" + anchor})
        for t, dfn in d["glossary"]:
            search.append({"k": "term", "t": t, "s": first_sentence(dfn, 110),
                           "m": code, "h": href + "#glossary"})
            if t.lower() not in seen_terms:
                seen_terms[t.lower()] = True
                glossary.append({"term": t, "def": dfn, "module": code,
                                 "href": href + "#glossary"})
        for t, dfn in d["recap"]["points"]:
            search.append({"k": "rule", "t": t, "s": first_sentence(dfn, 110),
                           "m": code, "h": href + "#recap"})
        for icon, t, dfn in d["toolkit"]["templates"]:
            search.append({"k": "toolkit", "t": t, "s": first_sentence(dfn, 110),
                           "m": code, "h": href + "#toolkit"})

        # One question per module goes into the formal assessment pool. Taken
        # verbatim from the module, so nothing in the test is unteachable.
        q = d["quiz"][0]
        pool.append({
            "module": code, "q": q["q"], "stem": q.get("stem"),
            "options": [{"text": a["text"], "ok": bool(a["ok"]), "why": a["why"]}
                        for a in q["answers"]],
        })

    glossary.sort(key=lambda g: g["term"].lower())
    tracks = [{"id": a, "name": T.AREAS[a]["name"], "blurb": AREA_BLURB[a]}
              for a in AREA_ORDER]
    data = {
        "generated": True,
        "library": "Inducto Learning & Knowledge Library",
        "tracks": tracks,
        "modules": modules,
        "glossary": glossary,
        "search": search,
        "paths": PATHS,
        "assessment": {"passMark": 0.7, "questionCount": 15, "questions": pool},
        "org": {
            "name": None,          # COMPANY INPUT NEEDED: organisation name
            "owner": None,         # COMPANY INPUT NEEDED: team that owns the training
            "tenantId": None,      # set per company when deployed as SaaS
        },
    }
    return data


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    for d in (SITE, MODDIR, DATADIR, IMGDIR):
        os.makedirs(d, exist_ok=True)

    decks = [importlib.import_module(m).DECK for m in build.REGISTRY]
    order = {a: i for i, a in enumerate(AREA_ORDER)}
    decks.sort(key=lambda d: (order[d["area"]], d["module_code"]))

    gaps, sect_counts, images = [], {}, []
    for i, d in enumerate(decks):
        prev_mod = decks[i - 1] if i else None
        next_mod = decks[i + 1] if i + 1 < len(decks) else None
        page, n = render_module(d, prev_mod, next_mod, gaps)
        sect_counts[d["module_code"]] = n
        path = os.path.join(MODDIR, "%s.html" % slug(d["module_code"]))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(page)
        if d.get("cover_image"):
            images.append((d["module_code"], os.path.basename(d["cover_image"])))

    # copy the real hero images; never reference one that is not there
    copied = []
    for code, fn in images:
        src = os.path.join(ROOT, "assets", fn)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(IMGDIR, fn))
            copied.append(fn)
        else:
            raise SystemExit("missing hero image: %s (module %s)" % (fn, code))

    totals = {
        "modules": len(decks),
        "minutes": sum(d["duration_min"] for d in decks),
        "lessons": sum(len(d["slides"]) for d in decks),
    }

    data = build_data(decks, sect_counts)
    with open(os.path.join(DATADIR, "library.js"), "w", encoding="utf-8") as fh:
        fh.write("/* Generated by sitegen.py. Do not edit by hand. */\n"
                 "window.INDUCTO_DATA = ")
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")

    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(render_index(data["modules"], totals))
    with open(os.path.join(SITE, "assessment.html"), "w", encoding="utf-8") as fh:
        fh.write(render_assessment(totals))

    report = {
        "modulePages": len(decks),
        "sections": sum(sect_counts.values()),
        "lessons": totals["lessons"],
        "glossaryTerms": len(data["glossary"]),
        "searchRows": len(data["search"]),
        "assessmentPool": len(data["assessment"]["questions"]),
        "heroImages": len(set(copied)),
        "videoGaps": gaps,
    }
    with open(os.path.join(ROOT, "sitegen_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
