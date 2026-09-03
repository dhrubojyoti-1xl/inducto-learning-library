"""
Attach the newly sourced videos to the 23 decks that had none.

Title, channel and duration are taken from newvideos.json, which was written
by a verified oEmbed + watch-page lookup. Nothing here is typed by hand.
"""

import json
import os
import sys

FILES = {
    "AI-03": "content/area01/m03_ai_capabilities.py",
    "AI-04": "content/area01/m04_ai_limitations.py",
    "DW-02": "content/area02/m07_research_with_ai.py",
    "DW-03": "content/area02/m08_report_preparation.py",
    "DW-04": "content/area02/m09_data_analysis.py",
    "DW-06": "content/area02/m11_presentations_with_ai.py",
    "DW-07": "content/area02/m12_documentation_with_ai.py",
    "DW-08": "content/area02/m13_meeting_notes.py",
    "DW-09": "content/area02/m14_brainstorming.py",
    "DW-10": "content/area02/m15_planning_productivity.py",
    "PE-02": "content/area03/m18_instructions_context.py",
    "PE-03": "content/area03/m19_role_prompts.py",
    "PE-05": "content/area03/m21_advanced_prompting.py",
    "PE-07": "content/area03/m23_evaluating_responses.py",
    "PS-01": "content/area04/m24_business_communication.py",
    "PS-03": "content/area04/m26_english_grammar.py",
    "PS-05": "content/area04/m28_productivity_systems.py",
    "PS-06": "content/area04/m29_problem_solving.py",
    "SEC-02": "content/area05/m34_phishing.py",
    "SEC-03": "content/area05/m35_mfa.py",
    "SEC-04": "content/area05/m36_data_protection.py",
    "SEC-05": "content/area05/m37_confidential_information.py",
    "SEC-07": "content/area05/m39_never_paste.py",
}

STD_NOTE = ("An outside video, not company material. Where it differs from "
            "this module, follow this module.")
STD_HOW = ["Optional. Everything you need is already in this deck.",
           "Useful if you prefer watching to reading.",
           "It opens in your browser. Turn the sound on."]

COPY = {
    "AI-03": ("A 14-minute tour of real uses", "Fourteen minutes of real uses",
              "An outside video, not company material. It shows tools rather "
              "than the method — the method is in this module.",
              ["Optional. The four job shapes above are the method.",
               "Useful for seeing what other people actually do with it.",
               "It opens in your browser. Turn the sound on."]),
    "AI-04": ("A 9-minute outside explainer", "Nine minutes on what it cannot do",
              STD_NOTE, STD_HOW),
    "DW-02": ("A 14-minute outside walkthrough",
              "Fourteen minutes on deep research",
              "Aimed at academic research. The habits transfer; our rules on "
              "what you may paste do not change.",
              ["Optional. The mapping prompt above is the core.",
               "Useful if your tool has a deep-research mode.",
               "It opens in your browser. Turn the sound on."]),
    "DW-03": ("A 9-minute outside walkthrough", "Nine minutes on report writing",
              STD_NOTE, STD_HOW),
    "DW-04": ("A 12-minute outside walkthrough", "Twelve minutes, shown on screen",
              "An outside video, not company material. Follow this module's "
              "rule on aggregating and anonymising before you paste.",
              ["Optional. Excel still does the arithmetic.",
               "Useful for seeing the workflow demonstrated.",
               "It opens in your browser. Turn the sound on."]),
    "DW-06": ("A 13-minute outside walkthrough", "Thirteen minutes on AI decks",
              STD_NOTE, STD_HOW),
    "DW-07": ("A 5-minute outside walkthrough", "Five minutes on writing SOPs",
              STD_NOTE, STD_HOW),
    "DW-08": ("A 4-minute outside walkthrough", "Four minutes on meeting minutes",
              "An outside video from a tool vendor. Follow this module's rules "
              "on recording and consent regardless of what it shows.",
              ["Optional. The three-section prompt is the core.",
               "Ignore the product pitch; watch the method.",
               "It opens in your browser. Turn the sound on."]),
    "DW-09": ("A 13-minute outside walkthrough", "Thirteen minutes, three methods",
              STD_NOTE, STD_HOW),
    "DW-10": ("A 6-minute outside walkthrough", "Six minutes on planning a week",
              STD_NOTE, STD_HOW),
    "PE-02": ("A 6-minute outside explainer", "Six minutes on what is missing",
              STD_NOTE, STD_HOW),
    "PE-03": ("A 4-minute outside explainer", "Four minutes on role prompts",
              STD_NOTE, STD_HOW),
    "PE-05": ("A 13-minute outside explainer", "Thirteen minutes, four methods",
              STD_NOTE, STD_HOW),
    "PE-07": ("A 7-minute outside explainer", "Seven minutes on judging output",
              "Made for a university audience. The tests it teaches are the "
              "same ones you need at work.", STD_HOW),
    "PS-01": ("A 4-minute outside guide", "Four minutes on writing sharply",
              STD_NOTE, STD_HOW),
    "PS-03": ("A 10-minute outside exercise", "Ten minutes, spot the mistakes",
              "An outside English lesson, not company material. Try to spot "
              "each error before he explains it.",
              ["Optional. The six patterns above are the working set.",
               "Best watched as a test rather than a lecture.",
               "It opens in your browser. Turn the sound on."]),
    "PS-05": ("A 7-minute outside walkthrough", "Seven minutes, one simple system",
              STD_NOTE, STD_HOW),
    "PS-06": ("An 8-minute outside explainer", "Eight minutes on five whys",
              STD_NOTE, STD_HOW),
    "SEC-02": ("A 9-minute outside guide", "Nine minutes on spotting them",
               "An outside video using UK examples. The signals are identical "
               "here; the reporting route is ours.", STD_HOW),
    "SEC-03": ("A 3-minute outside explainer", "Three minutes on the second lock",
               STD_NOTE, STD_HOW),
    "SEC-04": ("A 3-minute regulator explainer", "Three minutes from a regulator",
               "From the UK's data protection regulator. The principles match "
               "India's DPDP Act and UAE law closely.", STD_HOW),
    "SEC-05": ("A 4-minute outside explainer", "Four minutes on the four classes",
               STD_NOTE, STD_HOW),
    "SEC-07": ("A 7-minute outside warning", "Seven minutes on what leaks",
               STD_NOTE, STD_HOW),
}


def lit(text, indent, first_prefix):
    """Emit a wrapped Python string literal block."""
    width = 74 - indent
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if len(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    pad = " " * indent
    out = []
    for i, ln in enumerate(lines):
        esc = ln.replace("\\", "\\\\").replace('"', '\\"')
        prefix = first_prefix if i == 0 else pad
        tail = " " if i < len(lines) - 1 else ""
        out.append('%s"%s%s"' % (prefix, esc, tail))
    return "\n".join(out)


def block(v, heading, note, how):
    L = []
    L.append("    # Title, channel and runtime were read back from YouTube")
    L.append("    # itself. See newvideos.json.")
    L.append('    "video": {')
    L.append('        "url": "%s",' % v["url"])
    L.append(lit(v["title"], 17, '        "title": ') + ",")
    L.append('        "channel": "%s",' % v["channel"].replace('"', '\\"'))
    L.append('        "duration": "%s",' % v["duration"])
    L.append('        "heading": "%s",' % heading)
    L.append(lit(note, 16, '        "note": ') + ",")
    L.append('        "how": [')
    for h in how:
        L.append(lit(h, 12, "            ") + ",")
    L.append("        ],")
    L.append("    },")
    L.append("")
    return "\n".join(L) + "\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    vids = json.load(open("newvideos.json", encoding="utf-8"))
    done = 0
    for code, path in FILES.items():
        v = vids[code]
        sub, heading, note, how = COPY[code]
        s = open(path, encoding="utf-8").read()
        if '"video":' in s:
            print("skip  %-7s already has a video" % code)
            continue

        anchor = ', "scenario"),\n    ],'
        if anchor not in s:
            print("FAIL  %-7s no sections anchor" % code)
            continue
        s = s.replace(anchor,
                      ', "scenario"),\n        ("Watch this", "%s", "video"),'
                      '\n    ],' % sub, 1)

        if '\n    "quiz": [' not in s:
            print("FAIL  %-7s no quiz anchor" % code)
            continue
        s = s.replace('\n    "quiz": [',
                      "\n" + block(v, heading, note, how) + '    "quiz": [', 1)

        open(path, "w", encoding="utf-8").write(s)
        done += 1
        print("ok    %-7s %-6s %s" % (code, v["duration"], v["title"][:52]))
    print("\nattached %d videos" % done)


if __name__ == "__main__":
    main()
