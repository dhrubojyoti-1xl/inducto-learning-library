# -*- coding: utf-8 -*-
"""
Build the Mandatory Learning Journey into the live Inducto site.

    python journeygen.py

Generates:
    site/journey.html                the journey map / home
    site/journey/m01.html .. m16.html  the 16 lesson pages
    site/journey/m19.html            the integration exercise
    site/journey/recap-*.html        nothing — stage recaps render inline
    site/js/journey.js               lesson-page behaviour
    site/data/library.js             patched: + `journey`, assessment pool
                                      replaced with the 15-question mandatory
                                      pool (data/library.js must already
                                      exist — run sitegen.py first)

Every video, reading sentence, workplace example, prompt, checklist item and
quiz question is quoted from journey_data.py / management_review_docx.py,
which themselves quote content/areaNN/*.py verbatim. The only newly authored
text is short "what to notice" framing lines, the stage recaps (mechanically
assembled from real checklist/objective/mistake text — see build_recaps()),
and the M-19 integration exercise (journey_data.EXERCISE).
"""

import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import journey_data as J
import sitegen
import theme as T

ROOT = sitegen.ROOT
SITE = sitegen.SITE
JDIR = os.path.join(SITE, "journey")

BRAND = "Inducto"


def e(s):
    return html.escape("" if s is None else str(s), quote=True)


def yt_id(url):
    m = re.search(r"[?&]v=([A-Za-z0-9_\-]{6,})", url or "")
    return m.group(1) if m else None


def head(title, desc, up):
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<meta name=\"description\" content=\"%s\">\n"
        "<meta name=\"theme-color\" content=\"#101826\">\n"
        "<title>%s</title>\n"
        "<link rel=\"preconnect\" href=\"https://www.youtube-nocookie.com\">\n"
        "<link rel=\"stylesheet\" href=\"%scss/inducto.css\">\n"
        "</head>\n" % (e(desc), e(title), up))


def topbar(up, right_html):
    return (
        "<a class=\"skip\" href=\"#main\">Skip to content</a>\n"
        "<header class=\"topbar\"><div class=\"wrap topbar__in\">"
        "<a class=\"brand\" href=\"%sindex.html\">"
        "<span class=\"brand__mark\" aria-hidden=\"true\"></span>%s</a>"
        "<span class=\"topbar__spacer\"></span>%s</div></header>\n"
        % (up, BRAND, right_html))


def foot(up, scripts):
    s = "".join('<script src="%s%s"></script>\n' % (up, sc) for sc in scripts)
    return (
        "<footer class=\"foot\"><div class=\"wrap\">"
        "<p>%s · Mandatory Learning Journey. Every video, example, "
        "prompt and question here is drawn from the audited course "
        "content — see the Optional Extended Library for the full-depth "
        "version of every topic.</p></div></footer>\n"
        "<div id=\"live\" class=\"sr\" role=\"status\" aria-live=\"polite\"></div>\n"
        "<script src=\"%sjs/progress.js\"></script>\n%s"
        "</body>\n</html>\n" % ("Inducto Learning & Knowledge Library", up, s))


def prompt_card(text, ctx_id):
    return (
        '<div class="prompt"><div class="prompt__bar"><span>Copy this prompt</span>'
        '<button type="button" class="copybtn" data-copy="%s">Copy</button></div>'
        '<div class="prompt__body" id="%s">%s</div></div>'
        % (ctx_id, ctx_id, e(text)))


# ---------------------------------------------------------------------------
# stage recaps — mechanically assembled from real content, not hand-written
# ---------------------------------------------------------------------------
def build_recaps(by_code, resolved):
    from management_review_docx import find_visual
    recaps = {}
    stages = []
    for r in resolved:
        if not stages or stages[-1][0] != r["stage"]:
            stages.append((r["stage"], []))
        stages[-1][1].append(r)

    for stage_name, stops in stages:
        remember = [r["objective"] for r in stops]
        do = []
        for r in stops:
            if r["checklist"]:
                do.append(r["checklist"][0])
        avoid = []
        primary_code = stops[0]["sources"][0]
        _, mv = find_visual(by_code[primary_code], "mistakes")
        if mv:
            for what, why in mv["items"][:2]:
                avoid.append(what)
        if not avoid:
            avoid = ["Treating any AI output as a fact you can act on "
                    "without checking it first."]
        recaps[stage_name] = {"remember": remember, "do": do[:4],
                              "avoid": avoid[:3]}
    return recaps


# ---------------------------------------------------------------------------
# "what to notice" — real, derived from the video/topic, not generic filler
# ---------------------------------------------------------------------------
def notice_line(r):
    if r["video"] and not r["video_note_only"]:
        return ("As you watch, notice how %s frames this topic — the "
               "reading below builds directly on it."
               % r["video"]["channel"])
    return None


# ===========================================================================
def render_lesson(r, prev_r, next_r, stage_recap, stage_is_last):
    code = r["code"]
    slug = sitegen.slug(code)
    o = [head("%s · %s · Mandatory Journey" % (r["title"], BRAND),
             "Mandatory Learning Journey stop %s: %s." % (code, r["title"]),
             "../")]
    o.append("<body data-area=\"01-ai-general\">\n")
    o.append(topbar("../",
                    "<span class=\"topbar__meta\" id=\"jpct\">Journey "
                    "0%</span><a class=\"btn btn--sm btn--quiet\" "
                    "href=\"../journey.html\">Journey map</a>"))
    o.append("<main id=\"main\" class=\"wrap\">\n")
    o.append("<nav class=\"crumb\" aria-label=\"Breadcrumb\">"
             "<a href=\"../journey.html\">Mandatory Journey</a> / "
             "<span>%s</span> / %s</nav>\n" % (e(r["stage"]), e(code)))

    o.append("<header class=\"mhead\" data-journey-stop=\"%s\">" % e(code))
    o.append("<div class=\"chiprow\" style=\"margin:20px 0 16px\">"
             "<span class=\"chip chip--solid\">%s</span>"
             "<span class=\"chip\">%s</span>"
             "<span class=\"chip\">%.1f min</span></div>"
             % (e(code), e(r["stage"]), r["time"]["total_min"]))
    o.append("<h1>%s</h1>" % e(r["title"]))
    src_titles = " + ".join(r["module_titles"])
    o.append("<p class=\"lead\">From the audited course: <em>%s</em></p>"
             % e(src_titles))
    o.append("<div class=\"bar\" id=\"stopbarwrap\" role=\"progressbar\" "
             "aria-valuemin=\"0\" aria-valuemax=\"100\" aria-valuenow=\"0\">"
             "<div class=\"bar__fill\" id=\"stopbar\" style=\"width:0%\">"
             "</div></div>")
    o.append("</header>\n")

    o.append("<section class=\"step\" id=\"objective\">"
             "<div class=\"step__eyebrow\">What you'll learn</div>"
             "<p class=\"lead\">By the end of this stop you can %s.</p>"
             "</section>\n" % e((r["objective"][0].lower()
                                 + r["objective"][1:]).rstrip(".")))

    if r["video"] and not r["video_note_only"]:
        v = r["video"]
        vid = yt_id(v["url"])
        o.append("<section class=\"step\" id=\"video\">"
                 "<div class=\"step__eyebrow\">Watch</div>")
        o.append('<div class="video__frame"><iframe loading="lazy" '
                 'src="https://www.youtube-nocookie.com/embed/%s?rel=0" '
                 'title="%s" allow="accelerometer; clipboard-write; '
                 'encrypted-media; picture-in-picture" allowfullscreen>'
                 '</iframe></div>' % (e(vid), e(v["title"])))
        o.append('<div class="video__meta"><span class="chip">%s</span>'
                 '<span class="chip">%s</span>'
                 '<a class="chip" href="%s" target="_blank" '
                 'rel="noopener noreferrer">Open on YouTube ↗</a></div>'
                 % (e(v["channel"]), e(v["duration"]), e(v["url"])))
        o.append('<p style="margin-top:12px"><strong>%s</strong></p>'
                 % e(v["title"]))
        nl = notice_line(r)
        if nl:
            o.append('<p class="note">%s</p>' % e(nl))
        o.append("</section>\n")
    elif r["video_note_only"]:
        v = r["video"]
        opt_href = "../modules/%s.html#video" % sitegen.slug(
            r["video_ref_module"])
        o.append("<section class=\"step\" id=\"video\">"
                 "<div class=\"step__eyebrow\">About the video for this "
                 "topic</div>"
                 '<div class="video__gap"><strong>“%s” (%s, %s) '
                 "runs longer than fits this short mandatory stop.</strong>"
                 '<p style="margin:8px 0 0">The reading below covers the '
                 "essential point. Watch the full video any time in the "
                 '<a href="%s">Optional Extended Library</a>.</p></div>'
                 "</section>\n" % (e(v["title"]), e(v["channel"]),
                                   e(v["duration"]), e(opt_href)))

    o.append("<section class=\"step\" id=\"reading\">"
             "<div class=\"step__eyebrow\">Why this matters at work</div>"
             "<p>%s</p></section>\n" % e(r["reading"]))

    if r["example"]:
        o.append("<section class=\"step\" id=\"example\">"
                 "<div class=\"step__eyebrow\">Workplace example</div>"
                 "<h2>%s</h2><p>%s</p></section>\n"
                 % (e(r["example_title"] or ""), e(r["example"])))

    if r["prompt"]:
        o.append("<section class=\"step\" id=\"prompt\">"
                 "<div class=\"step__eyebrow\">Try it — copy-paste "
                 "prompt</div>%s</section>\n"
                 % prompt_card(r["prompt"], "p_" + slug))

    if r["checklist"]:
        o.append("<section class=\"step\" id=\"checklist\">"
                 "<div class=\"step__eyebrow\">Checklist</div>"
                 '<ul class="checklist">')
        for i, item in enumerate(r["checklist"]):
            key = "%s-%d" % (code, i)
            o.append('<li class="checkitem"><label>'
                     '<input type="checkbox" data-key="%s"><span>%s</span>'
                     "</label></li>" % (e(key), e(item)))
        o.append("</ul></section>\n")

    o.append("<section class=\"step\" id=\"check\" data-quiz>"
             "<div class=\"step__eyebrow\">Knowledge check</div>"
             "<h2>Check what stuck</h2>"
             '<p class="prose">Practice — retry as often as you like. '
             "This does not count towards the final assessment.</p>")
    for qi, q in enumerate(r["quiz"]):
        o.append('<div class="q" data-remember="%s"><h3>%s</h3>'
                 % (e(q["remember"]), e(q["q"])))
        if q.get("stem"):
            o.append('<div class="q__stem">%s</div>' % e(q["stem"]))
        o.append('<div class="q__opts" role="group" '
                 'aria-label="Answer options">')
        for ai, a in enumerate(q["answers"]):
            o.append('<button type="button" class="opt" data-correct="%s" '
                     'data-why="%s"><span class="opt__k">%s</span>'
                     "<span>%s</span></button>"
                     % ("1" if a["ok"] else "0", e(a["why"]), "ABCDE"[ai],
                        e(a["text"])))
        o.append('</div><div class="fb"></div></div>')
    o.append('<div class="qscore" id="qscore" hidden></div></section>\n')

    if stage_is_last:
        rc = stage_recap
        o.append("<section class=\"step\" id=\"recap\">"
                 "<div class=\"step__eyebrow\">Stage recap — %s</div>"
                 "<h2>What to carry forward</h2>" % e(r["stage"]))
        o.append('<div class="split"><div class="panel panel--accent">'
                 "<h3>What I should remember</h3><ul>")
        for it in rc["remember"]:
            o.append("<li><span>%s</span></li>" % e(it))
        o.append('</ul></div><div class="panel panel--good">'
                 "<h3>What I should do</h3><ul>")
        for it in rc["do"]:
            o.append("<li><span>%s</span></li>" % e(it))
        o.append('</ul></div></div>'
                 '<div class="panel panel--bad" style="margin-top:16px">'
                 "<h3>What I should avoid</h3><ul>")
        for it in rc["avoid"]:
            o.append("<li><span>%s</span></li>" % e(it))
        o.append("</ul></div></section>\n")

    o.append('<section class="step" id="finish">'
             '<div class="done" id="doneBox" hidden>'
             '<div class="done__tick" aria-hidden="true">✓</div>'
             "<h2>Stop complete</h2>"
             '<p class="prose" style="margin:0 auto">Saved to your '
             "journey progress.</p><div class=\"done__actions\">")
    if next_r:
        o.append('<a class="btn" href="%s.html">Next: %s →</a>'
                 % (sitegen.slug(next_r["code"]), e(next_r["title"])))
    else:
        o.append('<a class="btn" href="m19.html">Next: Integration '
                 "Exercise →</a>")
    o.append('<a class="btn btn--ghost" href="../journey.html">Journey '
             "map</a></div></div>")
    o.append('<p style="text-align:center"><button class="btn" '
             'id="completeBtn">Mark this stop complete</button></p>')
    o.append("</section>\n")

    o.append('<nav class="linklist" style="margin-top:32px" '
             'aria-label="Stop navigation">')
    if prev_r:
        o.append('<a class="linkitem" href="%s.html"><span>← '
                 'Previous: %s</span><small>%s</small></a>'
                 % (sitegen.slug(prev_r["code"]), e(prev_r["title"]),
                    e(prev_r["code"])))
    if next_r:
        o.append('<a class="linkitem" href="%s.html"><span>Next: %s '
                 '→</span><small>%s</small></a>'
                 % (sitegen.slug(next_r["code"]), e(next_r["title"]),
                    e(next_r["code"])))
    o.append("</nav>\n</main>\n")
    o.append(foot("../", ["data/library.js", "js/journey.js"]))
    return "".join(o)


# ===========================================================================
def render_exercise(ex, prev_r):
    o = [head("%s · %s" % (ex["title"], BRAND),
             "The Mandatory Journey integration exercise.", "../")]
    o.append("<body data-area=\"01-ai-general\">\n")
    o.append(topbar("../", '<a class="btn btn--sm btn--quiet" '
                          'href="../journey.html">Journey map</a>'))
    o.append("<main id=\"main\" class=\"wrap\">\n")
    o.append("<nav class=\"crumb\"><a href=\"../journey.html\">Mandatory "
             "Journey</a> / %s / %s</nav>\n" % (e(ex["stage"]), ex["code"]))
    o.append("<header class=\"mhead\" data-exercise>")
    o.append('<div class="chiprow" style="margin:20px 0 16px">'
             '<span class="chip chip--solid">M-19</span>'
             '<span class="chip">%s</span><span class="chip">~3 min'
             "</span></div>" % e(ex["stage"]))
    o.append("<h1>%s</h1><p class=\"lead\">%s</p></header>\n"
             % (e(ex["title"]), e(ex["intro"])))

    o.append('<section class="step"><div class="step__eyebrow">The '
             "scenario</div><h2>%s</h2>"
             '<div class="q__stem" style="white-space:pre-wrap">%s</div>'
             "</section>\n" % (e(ex["scenario_title"]), e(ex["scenario"])))

    for i, step in enumerate(ex["steps"], 1):
        sid = step["id"]
        o.append('<section class="step" id="step-%s" data-exercise-step="%s">'
                 '<div class="step__eyebrow">Your turn</div><h3>%s</h3>'
                 "<p>%s</p>" % (sid, sid, e(step["title"]), e(step["instruction"])))
        o.append('<p class="note">Hint: %s</p>' % e(step["hint"]))
        o.append('<label class="sr" for="in-%s">Your answer for %s</label>'
                 '<textarea id="in-%s" class="prompt__body" '
                 'style="width:100%%;min-height:110px;background:var(--surface);'
                 'color:var(--ink);border:1px solid var(--line);'
                 'border-radius:var(--r);padding:14px;font-family:var(--font);'
                 'font-size:.95rem" placeholder="Write your answer here '
                 'before revealing the example..."></textarea>'
                 % (sid, e(step["title"]), sid))
        o.append('<p style="margin-top:12px">'
                 '<button type="button" class="btn btn--ghost btn--sm" '
                 'data-reveal="%s">Reveal a strong example</button></p>'
                 % sid)
        o.append('<div class="reveal" id="reveal-%s" hidden>'
                 '<div class="card" style="padding:16px;margin-top:8px">'
                 '<div class="step__eyebrow">A strong example</div>'
                 '<p style="white-space:pre-wrap;margin:0">%s</p></div>'
                 "</div></section>\n" % (sid, e(step["model_answer"])))

    kc = ex["knowledge_check"]
    o.append('<section class="step" id="check" data-quiz>'
             '<div class="step__eyebrow">Knowledge check</div>'
             "<h2>%s</h2>"
             '<div class="q"><div class="q__opts" role="group" '
             'aria-label="Answer options">' % e(kc["q"]))
    for ai, a in enumerate(kc["options"]):
        o.append('<button type="button" class="opt" data-correct="%s" '
                 'data-why="%s"><span class="opt__k">%s</span>'
                 "<span>%s</span></button>"
                 % ("1" if a["ok"] else "0", e(a["why"]), "ABCD"[ai],
                    e(a["text"])))
    o.append('</div><div class="fb"></div></div>'
             '<div class="qscore" id="qscore" hidden></div></section>\n')

    o.append('<section class="step" id="finish">'
             '<div class="done" id="doneBox" hidden>'
             '<div class="done__tick" aria-hidden="true">✓</div>'
             "<h2>Exercise complete</h2>"
             '<p class="prose" style="margin:0 auto">You have used every '
             "skill from the journey in one scenario. One step left."
             '</p><div class="done__actions">'
             '<a class="btn" href="../assessment.html">Take the final '
             "assessment →</a>"
             '<a class="btn btn--ghost" href="../journey.html">Journey map'
             "</a></div></div>")
    o.append('<p style="text-align:center"><button class="btn" '
             'id="completeBtn">Mark exercise complete</button></p>'
             "</section>\n")
    o.append('<nav class="linklist" style="margin-top:32px">')
    if prev_r:
        o.append('<a class="linkitem" href="%s.html"><span>← Back to '
                 '%s</span><small>%s</small></a>'
                 % (sitegen.slug(prev_r["code"]), e(prev_r["title"]),
                    e(prev_r["code"])))
    o.append('<a class="linkitem" href="../assessment.html"><span>Final '
             "assessment →</span><small>M-20</small></a></nav>\n")
    o.append("</main>\n")
    o.append(foot("../", ["data/library.js", "js/journey.js"]))
    return "".join(o)


# ===========================================================================
def render_journey_map(resolved, ex, total_min):
    o = [head("Mandatory Learning Journey · " + BRAND,
             "The 16-stop mandatory journey every employee completes: AI "
             "fundamentals through security and responsible use, in about "
             "%d minutes." % round(total_min), "")]
    o.append("<body data-area=\"01-ai-general\">\n")
    o.append(topbar("", '<a class="btn btn--sm btn--quiet" '
                       'href="index.html">Optional library</a>'
                       '<a class="btn btn--sm" href="assessment.html">'
                       "Final assessment</a>"))
    o.append("<main id=\"main\">\n")
    o.append('<section class="hero"><div class="wrap hero__grid"><div>'
             "<h1>Mandatory Learning Journey</h1>"
             "<p>16 stops, 9 stages, about %d minutes. Everyone completes "
             "this. The 39-module Optional Extended Library goes deeper on "
             "every topic, any time.</p>"
             '<div class="chiprow" style="margin-top:20px">'
             '<span class="chip" style="color:#c9d1de;'
             'border-color:rgba(255,255,255,.25)">16 stops</span>'
             '<span class="chip" style="color:#c9d1de;'
             'border-color:rgba(255,255,255,.25)">24 knowledge checks'
             '</span><span class="chip" style="color:#c9d1de;'
             'border-color:rgba(255,255,255,.25)">~%d min</span></div>'
             "</div>" % (round(total_min), round(total_min)))
    o.append('<div class="hero__stats">'
             '<div class="stat"><span class="stat__n" id="jStatDone">0'
             '</span><span class="stat__l">Stops complete</span></div>'
             '<div class="stat"><span class="stat__n" id="jStatPct">0%'
             '</span><span class="stat__l">Journey progress</span></div>'
             '</div></div></section>\n')

    o.append('<div class="wrap">\n')
    o.append('<div class="resume" id="jResume"></div>\n')
    o.append('<div class="bar" id="jBarWrap" role="progressbar" '
             'aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" '
             'style="margin-top:24px"><div class="bar__fill" id="jBar" '
             'style="width:0%"></div></div>\n')
    o.append('<p class="note" id="storageWarn" hidden>Your browser is '
             "blocking local storage, so progress cannot be saved on this "
             "device. Everything still works — it just will not be "
             "remembered.</p>\n")

    stages = []
    for r in resolved:
        if not stages or stages[-1][0] != r["stage"]:
            stages.append((r["stage"], []))
        stages[-1][1].append(r)

    for stage_name, stops in stages:
        o.append('<section class="track" data-area="01-ai-general">'
                 '<div class="track__head"><div class="track__rule">'
                 "</div><h2 style=\"margin:0\">%s</h2>"
                 '<span class="track__count">%d stop%s</span></div>'
                 '<div class="grid grid--3">'
                 % (e(stage_name), len(stops), "" if len(stops) == 1 else "s"))
        for r in stops:
            o.append('<a class="mcard" href="journey/%s.html" '
                     'data-journey-card="%s">'
                     '<div class="mcard__top"><span class="mcard__code">%s'
                     '</span><span class="chip" data-journey-status="%s">'
                     "NOT STARTED</span></div>"
                     "<h3>%s</h3>"
                     '<p class="mcard__desc">%s</p>'
                     '<div class="mcard__foot"><span>%.1f min</span>'
                     "<span>Start →</span></div></a>"
                     % (sitegen.slug(r["code"]), e(r["code"]), e(r["code"]),
                        e(r["code"]), e(r["title"]),
                        e(r["reading_heading"] or ""), r["time"]["total_min"]))
        o.append("</div></section>\n")

    o.append('<section class="track" data-area="01-ai-general">'
             '<div class="track__head"><div class="track__rule"></div>'
             "<h2 style=\"margin:0\">8. Practice</h2>"
             '<span class="track__count">1 stop</span></div>'
             '<div class="grid grid--3">'
             '<a class="mcard" href="journey/m19.html" '
             'data-journey-card="M-19"><div class="mcard__top">'
             '<span class="mcard__code">M-19</span>'
             '<span class="chip" data-journey-status="M-19">NOT STARTED'
             '</span></div><h3>%s</h3>'
             '<p class="mcard__desc">One realistic scenario, four of the '
             'skills from this journey.</p>'
             '<div class="mcard__foot"><span>~3 min</span>'
             "<span>Start →</span></div></a></div></section>\n"
             % e(ex["title"]))

    o.append('<section class="track" data-area="01-ai-general">'
             '<div class="track__head"><div class="track__rule"></div>'
             "<h2 style=\"margin:0\">9. Assessment</h2></div>"
             '<div class="card"><div class="step__eyebrow">M-20</div>'
             "<h3>Final graded assessment</h3>"
             '<p class="prose">15 questions across every stage of this '
             "journey. Pass mark 70%. Three attempts; further action "
             "requires an HR decision after a third unsuccessful attempt."
             '</p><p><a class="btn" href="assessment.html">Go to the '
             "final assessment →</a></p></div></section>\n")

    o.append("</div>\n</main>\n")
    o.append(foot("", ["data/library.js", "js/journey.js"]))
    return "".join(o)


# ===========================================================================
def patch_library_js(resolved, ex, by_code, total_min):
    path = os.path.join(SITE, "data", "library.js")
    raw = io.open(path, encoding="utf-8").read()
    payload = json.loads(raw.split("=", 1)[1].strip().rstrip(";\n"))

    stops_json = []
    for r in resolved:
        stops_json.append({
            "code": r["code"], "title": r["title"], "stage": r["stage"],
            "href": "journey/%s.html" % sitegen.slug(r["code"]),
            "minutes": r["time"]["total_min"],
            "hasVideo": bool(r["video"] and not r["video_note_only"]),
            "sources": r["sources"],
            "sectionCount": 4,   # objective/reading/checklist(or example)/check
        })
    payload["journey"] = {
        "totalMinutes": round(total_min, 1),
        "stopCount": len(resolved),
        "questionCount": sum(len(r["quiz"]) for r in resolved),
        "stages": [{"name": name} for name in
                  dict.fromkeys([r["stage"] for r in resolved])],
        "stops": stops_json,
        "exercise": {"code": "M-19", "href": "journey/m19.html",
                    "title": ex["title"]},
    }

    pool = J.assessment_pool(by_code)
    payload["assessment"] = {"passMark": 0.7, "questionCount": len(pool),
                             "maxAttempts": 3, "questions": pool}

    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write("/* Generated by sitegen.py + journeygen.py. Do not edit "
                "by hand. */\nwindow.INDUCTO_DATA = ")
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    return payload


# ===========================================================================
def main():
    os.makedirs(JDIR, exist_ok=True)
    by_code, decks, resolved = J.load()
    total_min = (sum(r["time"]["total_min"] for r in resolved)
                + 3 + 12)   # + practice (3) + assessment (12), see mgmt doc
    recaps = build_recaps(by_code, resolved)

    stages_order = []
    for r in resolved:
        if not stages_order or stages_order[-1] != r["stage"]:
            stages_order.append(r["stage"])
    last_of_stage = {}
    for stage in stages_order:
        stops_in_stage = [r for r in resolved if r["stage"] == stage]
        last_of_stage[stops_in_stage[-1]["code"]] = True

    for i, r in enumerate(resolved):
        prev_r = resolved[i - 1] if i else None
        next_r = resolved[i + 1] if i + 1 < len(resolved) else None
        is_last = last_of_stage.get(r["code"], False)
        page = render_lesson(r, prev_r, next_r, recaps[r["stage"]], is_last)
        with io.open(os.path.join(JDIR, sitegen.slug(r["code"]) + ".html"), "w",
                    encoding="utf-8") as fh:
            fh.write(page)

    ex_page = render_exercise(J.EXERCISE, resolved[-1])
    with io.open(os.path.join(JDIR, "m19.html"), "w", encoding="utf-8") as fh:
        fh.write(ex_page)

    map_page = render_journey_map(resolved, J.EXERCISE, total_min)
    with io.open(os.path.join(SITE, "journey.html"), "w",
                encoding="utf-8") as fh:
        fh.write(map_page)

    payload = patch_library_js(resolved, J.EXERCISE, by_code, total_min)

    print("Wrote journey.html + %d lesson pages + m19.html" % len(resolved))
    print("Journey total: %.1f minutes, %d quiz questions"
         % (total_min, payload["journey"]["questionCount"]))
    print("Assessment pool: %d questions" % len(payload["assessment"]["questions"]))


if __name__ == "__main__":
    main()
