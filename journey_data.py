# -*- coding: utf-8 -*-
"""
Single source of truth for the Mandatory Learning Journey's runtime data.

Reuses management_review_docx.py's STOPS / resolve_stop() / load_decks() —
the exact same 16-stop, 20-source-module selection already audited and
verified in the management review document — so the live product and the
management document can never drift apart.

Adds two things that only the live product needs:
  ASSESSMENT_POOL   15 real questions for the final graded assessment,
                    picked from indices NOT used as a lesson knowledge-check
                    (so nothing is answered twice in identical wording),
                    balanced across all 8 required subject areas.
  EXERCISE          the M-19 integration-exercise scenario.
"""

import importlib
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import management_review_docx as M

STAGES = [
    ("1. Foundation", "Foundation"),
    ("2. Understanding", "Understanding"),
    ("3. Practical AI Use", "Practical AI Use"),
    ("4. Prompt Engineering", "Prompt Engineering"),
    ("5. Workplace Application", "Workplace Application"),
    ("6. Professional Skills", "Professional Skills"),
    ("7. Security & Responsible Use", "Security & Responsible Use"),
    ("8. Practice", "Practice"),
    ("9. Assessment", "Assessment"),
]


def load():
    by_code, decks = M.load_decks()
    resolved = [M.resolve_stop(s, by_code) for s in M.STOPS]
    for r in resolved:
        r["time"] = M.stop_minutes(r)
    return by_code, decks, resolved


# ---------------------------------------------------------------------------
# ASSESSMENT_POOL — 15 real questions, indices chosen to avoid any question
# already shown as a lesson knowledge-check, balanced across all 8 areas.
# ---------------------------------------------------------------------------
ASSESSMENT_SPEC = [
    ("AI-01", 1, "AI Fundamentals"),
    ("AI-02", 1, "Generative AI"),
    ("AI-04", 1, "What AI Can and Cannot Do"),
    ("AI-05", 2, "AI Hallucinations & Fact-Checking"),
    ("AI-05", 3, "AI Hallucinations & Fact-Checking"),
    ("PE-01", 2, "Basic Prompting"),
    ("PE-02", 1, "Instructions, Context & Role"),
    ("DW-01", 1, "Writing Email With AI"),
    ("DW-10", 1, "Planning & Productivity With AI"),
    ("PS-01", 1, "Business Communication"),
    ("PS-04", 1, "Time Management"),
    ("SEC-01", 1, "Password Security & Multi-Factor Authentication"),
    ("SEC-02", 2, "Phishing & Social Engineering"),
    ("SEC-04", 1, "Data Protection & Confidential Information"),
    ("SEC-07", 2, "What Never to Paste Into AI"),
]


def assessment_pool(by_code):
    pool = []
    for code, idx, area in ASSESSMENT_SPEC:
        q = by_code[code]["quiz"][idx]
        pool.append({
            "module": area, "source": code,
            "q": q["q"], "stem": q.get("stem"),
            "options": [{"text": a["text"], "ok": bool(a["ok"]), "why": a["why"]}
                        for a in q["answers"]],
        })
    return pool


# ---------------------------------------------------------------------------
# M-19 — Integration Exercise. New scenario text (not copied from a source
# module — none of the 39 modules contains a combined end-to-end exercise),
# built from the same real transformation pattern DW-08 already teaches
# (raw notes -> structured summary -> action items -> follow-up message) and
# the same real safe-use rules SEC-07 already teaches. No company name,
# policy or fact is invented; the fictional site and people are clearly a
# training scenario, in the same style as the existing modules' Ramesh/
# Priya/Sanjay examples.
# ---------------------------------------------------------------------------
EXERCISE = {
    "code": "M-19",
    "title": "Integration Exercise — Put It Together",
    "stage": "8. Practice",
    "intro": (
        "One scenario, four of the skills from this journey. There is "
        "nothing to watch here — this is where you use what you have "
        "learned. Write your own answer in each box before you look at a "
        "strong example; the exercise only teaches you something if you "
        "try it first."
    ),
    "scenario_title": "Thursday, 4:50pm — the Chakan site review",
    "scenario": (
        "You run operations coordination for the Chakan distribution "
        "site. You have just come out of a 40-minute review call with the "
        "site supervisor, the transport lead and a client account "
        "manager. You typed rough notes on your phone during the call:\n\n"
        "“chakan wh — 2 of 6 dock doors down since tues, vendor says "
        "part on order, no date yet. transport lead: reroute 3 trucks fri "
        "morning to bhiwandi, extra cost approx ₹40k, needs sign off. "
        "client acct mgr (rept from Meridian Retail) — asked about their "
        "order MR-2291, promised weds, will slip to mon. site supervisor "
        "to send updated dock repair ETA by tues. i said i'd write it up "
        "and send to client by tonight. also — meridian sent their "
        "internal escalation email by mistake, cc'd to us, has their "
        "regional director's phone number and an unrelated pricing note "
        "in it.”\n\n"
        "It is 4:50pm. The client is expecting something before you log "
        "off."
    ),
    "steps": [
        {
            "id": "organise",
            "title": "1. Turn the raw notes into a structured summary",
            "instruction": (
                "Write the prompt you would give an AI assistant to turn "
                "these notes into a clean, structured summary — decisions, "
                "owners, dates. Use the real facts above; do not invent "
                "numbers that are not in the notes."
            ),
            "hint": "This is the same raw-notes-to-structure move DW-08 "
                    "taught you. Name the sections you want back.",
            "model_answer": (
                "“Turn these call notes into a structured summary with "
                "three sections: Decisions, Open Items, and Owners & "
                "Dates. Use only the facts in the notes below — do not add "
                "anything I have not written. Keep it under 120 words.\n\n"
                "[paste the notes]”\n\n"
                "Why this works: it names the exact structure, sets a "
                "word limit, and explicitly tells the tool not to add "
                "facts — the same rule DW-08 and AI-05 both teach."
            ),
            "type": "prompt",
        },
        {
            "id": "actions",
            "title": "2. Extract the action items",
            "instruction": (
                "List the action items from the notes yourself, each with "
                "an owner and a date, the way DW-08's transformation "
                "table showed."
            ),
            "hint": "There are at least three: the reroute sign-off, the "
                    "dock ETA, and the client update.",
            "model_answer": (
                "• Approve or decline the ₹40k reroute cost — you, "
                "before Friday morning\n"
                "• Send the dock repair ETA — site supervisor, by "
                "Tuesday\n"
                "• Send Meridian Retail their order update (MR-2291 "
                "now Monday, not Wednesday) — you, tonight"
            ),
            "type": "text",
        },
        {
            "id": "email",
            "title": "3. Draft the client follow-up",
            "instruction": (
                "Write the prompt you would use to draft the email to "
                "Meridian Retail about order MR-2291. Facts only: it was "
                "promised Wednesday, it will now arrive Monday, and the "
                "cause is a dock-door repair. Keep it short and calm."
            ),
            "hint": "This is the same shape as DW-01's late-delivery "
                    "prompt: facts, tone, length, in that order.",
            "model_answer": (
                "“Write a short, calm email to a client whose order is "
                "delayed. Facts: order MR-2291, promised Wednesday, now "
                "expected Monday, delay caused by a dock repair at our "
                "site. Tone: apologetic but factual. Under 100 words. End "
                "with the sender's name and role.”"
            ),
            "type": "prompt",
        },
        {
            "id": "safety",
            "title": "4. Spot the safety issue",
            "instruction": (
                "Something in this scenario should not go anywhere near "
                "an AI tool, or even into your own reply to Meridian. "
                "What is it, and what do you do with it?"
            ),
            "hint": "Re-read the last line of the notes.",
            "model_answer": (
                "Meridian's misdirected internal email — their regional "
                "director's phone number and an unrelated internal "
                "pricing note — landed in your inbox by accident. It is "
                "not yours to keep, forward, summarise, or paste into any "
                "AI tool. The right action is to leave it out of "
                "everything you write tonight and flag to your manager "
                "that a client's internal email arrived in error, exactly "
                "as SEC-07 and SEC-04 both teach: information that "
                "reaches you by accident is still confidential, and 'it "
                "would help the summary' is not authorisation to use it."
            ),
            "type": "text",
        },
    ],
    "knowledge_check": {
        "q": "What should you do with Meridian's misdirected internal "
             "email before you send anything tonight?",
        "options": [
            {"text": "Paste the useful parts into your AI summary so "
                     "nothing gets lost", "ok": False,
             "why": "It arrived by accident, not by authorisation. "
                    "Whatever is useful about it is not yours to use — "
                    "confidentiality does not depend on how the "
                    "information reached you."},
            {"text": "Leave it out of everything, and flag the misdirected "
                     "email to your manager", "ok": True,
             "why": "Correct. The email is confidential to Meridian "
                    "regardless of how it arrived. Reporting it is the "
                    "safe, professional response — the same rule SEC-04 "
                    "and SEC-07 both teach."},
            {"text": "Reply to Meridian's regional director directly using "
                     "the number in the email, since it is faster",
             "ok": False,
             "why": "Using contact details from a misdirected email is "
                    "still using information you were not meant to have. "
                    "Stay on the channel you were actually given."},
            {"text": "Delete it immediately so there is no record it ever "
                     "arrived", "ok": False,
             "why": "Deleting it does not undo the mistake and removes "
                    "the record your own manager or IT may need. Report "
                    "it; do not erase it."},
        ],
    },
}
