"""
Build one deck, all decks, or a named list.

    python build.py                 # everything in the registry
    python build.py AI-01 PE-01     # only these module codes
"""

import importlib
import json
import os
import sys

import theme as T
import components as C

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "output")

REGISTRY = [
    # Area 1 — AI Courses (General)
    "content.area01.m01_ai_fundamentals",
    "content.area01.m02_generative_ai",
    "content.area01.m03_ai_capabilities",
    "content.area01.m04_ai_limitations",
    "content.area01.m05_hallucinations",
    # Area 2 — AI for Day-to-Day Work
    "content.area02.m06_email_with_ai",
    "content.area02.m07_research_with_ai",
    "content.area02.m08_report_preparation",
    "content.area02.m09_data_analysis",
    "content.area02.m10_excel_with_ai",
    "content.area02.m11_presentations_with_ai",
    "content.area02.m12_documentation_with_ai",
    "content.area02.m13_meeting_notes",
    "content.area02.m14_brainstorming",
    "content.area02.m15_planning_productivity",
    "content.area02.m16_automation_basics",
    # Area 3 — Prompt Engineering
    "content.area03.m17_basic_prompting",
    "content.area03.m18_instructions_context",
    "content.area03.m19_role_prompts",
    "content.area03.m20_examples_structured",
    "content.area03.m21_advanced_prompting",
    "content.area03.m22_reusable_prompts",
    "content.area03.m23_evaluating_responses",
    # Area 4 — Professional Skills
    "content.area04.m24_business_communication",
    "content.area04.m25_professional_email",
    "content.area04.m26_english_grammar",
    "content.area04.m27_time_management",
    "content.area04.m28_productivity_systems",
    "content.area04.m29_problem_solving",
    "content.area04.m30_critical_thinking",
    "content.area04.m31_presentation_skills",
    "content.area04.m32_teamwork",
    # Area 5 — Security & Data Privacy
    "content.area05.m33_password_security",
    "content.area05.m34_phishing",
    "content.area05.m35_mfa",
    "content.area05.m36_data_protection",
    "content.area05.m37_confidential_information",
    "content.area05.m38_safe_ai_use",
    "content.area05.m39_never_paste",
]


# --------------------------------------------------------------------------
def count_points(spec):
    """
    A content point is: one teachable slide, one quiz item, one copy-paste
    template, or one checklist item. Counted here, reported in the manifest.
    """
    teachable = len(spec["slides"])
    quiz = len(spec["quiz"])
    templates = 0
    checks = 0
    for s in spec["slides"]:
        v = s.get("visual") or {}
        if v.get("type") in ("prompt", "prompt_out"):
            templates += 1
        if v.get("type") == "steps" and v.get("prompt"):
            templates += 1
        if v.get("type") in ("checklist", "bandlist"):
            checks += len(v.get("items", []))
    scenario = 1 if spec.get("scenario") else 0
    return {
        "teachable_slides": teachable,
        "quiz_items": quiz,
        "copy_paste_templates": templates,
        "checklist_items": checks,
        "scenario_decisions": scenario,
        "total": teachable + quiz + templates + checks + scenario,
    }


def find_tokens(obj, found=None):
    """Collect every [COMPANY INPUT NEEDED: ...] token in the content."""
    if found is None:
        found = []
    if isinstance(obj, str):
        i = 0
        while True:
            a = obj.find("[COMPANY INPUT NEEDED:", i)
            if a < 0:
                break
            b = obj.find("]", a)
            found.append(" ".join(obj[a:b + 1].split()))
            i = b + 1
    elif isinstance(obj, dict):
        for v in obj.values():
            find_tokens(v, found)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            find_tokens(v, found)
    return found


# --------------------------------------------------------------------------
def build_deck(spec):
    dk = C.Deck(spec)
    C.cover(dk)
    C.why(dk)
    C.outcomes(dk)
    C.menu(dk, spec["sections"])
    for s in spec["slides"]:
        C.content_slide(dk, s)
    C.scenario(dk, spec["scenario"])
    if spec.get("video"):
        C.video_slide(dk, spec["video"])
    C.quiz(dk, spec["quiz"])
    C.recap(dk, spec["recap"])
    C.toolkit(dk, spec["toolkit"])
    C.glossary(dk, spec["glossary"])

    folder = os.path.join(OUT, spec["area"])
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, spec["filename"])
    dk.save(path)

    hidden = sum(1 for s in dk.slides if s._element.get("show") == "0")
    return {
        "module_code": spec["module_code"],
        "title": spec["title"],
        "area": spec["area"],
        "area_name": T.AREAS[spec["area"]]["name"],
        "file": os.path.relpath(path, ROOT).replace("\\", "/"),
        "slide_count": len(dk.slides),
        "hidden_slides": hidden,
        "duration_min": spec["duration_min"],
        "audience": spec["audience"],
        "content_points": count_points(spec),
        "external_links": list(dk.ext_links),
        "video": ({k: spec["video"][k] for k in
                   ("title", "channel", "duration", "url")}
                  if spec.get("video") else None),
        "company_input_needed": find_tokens(spec),
    }


def main(argv):
    wanted = set(a.upper() for a in argv[1:])
    os.makedirs(OUT, exist_ok=True)
    entries = []
    for mod_path in REGISTRY:
        mod = importlib.import_module(mod_path)
        importlib.reload(mod)
        spec = mod.DECK
        if wanted and spec["module_code"].upper() not in wanted:
            continue
        info = build_deck(spec)
        entries.append(info)
        cp = info["content_points"]
        print("built  %-7s %-42s %3d slides  %2d points" %
              (info["module_code"], info["title"], info["slide_count"],
               cp["total"]))

    if not wanted:
        import master
        entries.append(master.build())
        print("built  %-7s %-42s %3d slides" %
              ("INDEX", "Inducto Learning Library", entries[-1]["slide_count"]))

    mpath = os.path.join(OUT, "manifest.json")
    existing = {}
    if os.path.exists(mpath):
        with open(mpath, "r", encoding="utf-8") as fh:
            try:
                existing = {d["module_code"]: d
                            for d in json.load(fh).get("decks", [])}
            except Exception:
                existing = {}
    for e in entries:
        existing[e["module_code"]] = e
    decks = sorted(existing.values(), key=lambda d: d["module_code"])
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump({"library": "Inducto Learning & Knowledge Library",
                   "deck_count": len(decks),
                   "decks": decks}, fh, indent=2, ensure_ascii=False)
    print("manifest -> %s  (%d decks)" % (mpath, len(decks)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
