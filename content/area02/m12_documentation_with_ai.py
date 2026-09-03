# -*- coding: utf-8 -*-
"""DW-07 — Documentation with AI. Content only."""

DECK = {
    "module_code": "DW-07",
    "area": "02-ai-daily-work",
    "filename": "02-07-documentation-with-ai.pptx",
    "title": "Documentation with AI",
    "subtitle": "SOPs, process notes and handovers somebody can follow without "
                "ringing you to ask what you meant.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "layers",
    "cover_image": "assets/hero-documentation.jpg",

    "why": {
        "title": "Fatima is the only one who knows",
        "icon": "doc",
        "scenario": "Fatima handles vendor onboarding for a Dubai office. She "
                    "has done it for four years and it lives entirely in her "
                    "head. When she took two weeks' leave, three onboardings "
                    "stalled and her phone rang eleven times.",
        "cost": "Eleven calls on annual leave, and three vendors kept waiting.",
        "fix": "Two hours of talking it through, and a process anyone can "
               "follow.",
    },

    "outcomes": [
        ("doc", "Turn what you know into a written process in under an hour"),
        ("list", "Write steps somebody can follow without asking questions"),
        ("eye", "Spot the step you left out because it is obvious to you"),
        ("cycle", "Keep a document current instead of letting it rot"),
        ("person", "Write a handover that actually survives your absence"),
    ],

    "sections": [
        ("The curse of knowing", "Why experts write bad steps", "s_curse"),
        ("Talk it, then shape it", "Dictate, do not compose", "s_talk"),
        ("Testing a procedure", "The new-joiner test", "s_test"),
        ("Keeping it current", "Documents that rot", "s_current"),
        ("Do this now", "Document one real process", "s_do"),
        ("Choose what you'd do", "A pre-holiday decision", "scenario"),
        ("Watch this", "A 5-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_curse",
            "label": "The curse of knowing",
            "title": "Experts write the worst steps",
            "lead": "The steps you leave out are exactly the ones you stopped "
                    "noticing years ago.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You know it cold", "Four years of doing it without "
                                         "thinking."),
                    ("The obvious vanishes", "Which system, which tab, whose "
                                             "approval."),
                    ("You write six steps", "Where a new joiner needs "
                                            "fourteen."),
                    ("They ring you", "At every gap you could not see."),
                ],
            },
        },
        {
            "label": "The curse of knowing",
            "title": "What gets left out",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "You wrote", "tone": "neutral", "mark": "list",
                    "title": "\"Raise the vendor record\"",
                    "items": [
                        "One line that feels complete",
                        "Obvious to anyone who has done it",
                        "Six words covering four minutes of work",
                        "No system, no field, no approval named",
                    ],
                },
                "right": {
                    "tag": "They need", "tone": "good",
                    "title": "Four separate steps",
                    "items": [
                        "Which system, and how to reach it",
                        "Which fields are mandatory, and what goes in them",
                        "Who approves it, and how long they take",
                        "What to do when the code already exists",
                    ],
                },
            },
        },
        {
            "anchor": "s_talk",
            "label": "Talk it, then shape it",
            "title": "Talk it through, do not compose",
            "lead": "Explaining it out loud to an imaginary new joiner "
                    "produces far better raw material than writing does.",
            "visual": {
                "type": "prompt",
                "header": "Copy this shaping prompt",
                "text": "Below is me explaining a process in my own words, in "
                        "no particular order. Turn it into numbered steps. "
                        "Each step must be one action a person can complete. "
                        "Use only what I said. Where I have skipped something "
                        "a beginner would need, write [GAP: what is missing] "
                        "instead of guessing.",
                "caption": "Type or dictate however you like. Order does not "
                           "matter.",
                "why": [
                    "[GAP] finds the steps you stopped noticing years ago.",
                    "\"One action per step\" stops four jobs hiding in one "
                    "line.",
                    "You can ramble. Reordering is exactly what it is good "
                    "at.",
                ],
            },
        },
        {
            "label": "Talk it, then shape it",
            "title": "What a good step looks like",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "STARTS WITH A VERB — \"Open\", \"Enter\", \"Send\", "
                    "\"Check\"",
                    "NAMES THE PLACE — which system, which screen, which "
                    "field",
                    "ONE ACTION ONLY — if it needs \"and\", it is two steps",
                    "SAYS WHAT SUCCESS LOOKS LIKE — \"the code turns green\"",
                ],
            },
        },
        {
            "anchor": "s_test",
            "label": "Testing a procedure",
            "title": "The new-joiner test",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this test prompt",
                "text": "Read these steps as somebody who joined the company "
                        "yesterday and has never seen this system. List every "
                        "point where you would have to stop and ask a "
                        "question. Do not rewrite the steps and do not answer "
                        "your own questions.",
                "caption": "The questions are the value. Ignore any urge to "
                           "have it fix them.",
                "out_title": "What comes back",
                "out": [
                    "Six to ten questions, most of which you would never have "
                    "predicted.",
                    "Usually one about an approval you forgot anyone needed.",
                    "You answer them in the document, and the phone stops "
                    "ringing.",
                ],
            },
        },
        {
            "label": "Testing a procedure",
            "title": "Then test it on a person",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Untested SOP",
                "bad": [
                    "Written by the expert, reviewed by the expert.",
                    "Reads perfectly to anyone who already knows the process.",
                    "First new joiner rings on step three.",
                ],
                "good_tag": "Tested SOP",
                "good": [
                    "Given to somebody who has never done it, with no help.",
                    "You watch and write down every place they hesitate.",
                    "Ten minutes of watching removes a year of phone calls.",
                ],
                "note": "The AI test finds the obvious gaps. A real person "
                        "finds the ones neither of you expected.",
            },
        },
        {
            "anchor": "s_current",
            "label": "Keeping it current",
            "title": "Documents rot quietly",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Date it",
                     "sub": "\"Last checked March 2026\" tells a reader "
                            "whether to trust it or ring you."},
                    {"icon": "person", "label": "Own it",
                     "sub": "One named role, not a team. Documents with no "
                            "owner are never updated."},
                    {"icon": "cycle", "label": "Fix on use",
                     "sub": "The moment somebody hits a wrong step, correct "
                            "the document, not just the person."},
                ],
            },
        },
        {
            "label": "Keeping it current",
            "title": "The update prompt",
            "visual": {
                "type": "prompt",
                "header": "Copy this update prompt",
                "text": "Here is an existing procedure and a description of "
                        "what has changed. Update only the steps affected by "
                        "the change. Leave every other step exactly as "
                        "written, including the wording. List at the end which "
                        "step numbers you changed.",
                "caption": "\"List which steps you changed\" makes review take "
                           "seconds.",
                "why": [
                    "Untouched steps stay untouched, so nothing drifts.",
                    "The change list is what you review, not the whole "
                    "document.",
                    "Updating becomes a two-minute job, so it actually "
                    "happens.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: document one",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick the process only you know how to do.",
                    "Explain it out loud into a document for ten minutes.",
                    "Run the shaping prompt, then the new-joiner test prompt.",
                    "Answer every [GAP] and every question it raises.",
                ],
                "prompt": "Turn my explanation below into numbered steps. One "
                          "action per step, starting with a verb, naming the "
                          "system and screen. Use only what I said. Write "
                          "[GAP: what is missing] wherever a beginner would "
                          "need something I have not mentioned.",
                "caption": "Two prompts and forty minutes replaces a year of "
                           "interruptions.",
            },
        },
        {
            "label": "Do this now",
            "title": "What not to put in a procedure",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "An SOP gets shared widely and lives for years. "
                            "Write it accordingly.",
                "sub": "Name roles and systems, never people and credentials.",
                "cols": 2,
                "items": [
                    "Passwords, PINs or shared login details",
                    "A named individual where a role would do",
                    "Real customer records used as the worked example",
                    "Internal system addresses posted outside the company",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Writing steps from memory, in order",
                     "You write what you remember doing, not what a beginner "
                     "has to do."),
                    ("Putting four actions in one step",
                     "\"Raise and approve the record and notify the vendor\" "
                     "is three steps and one guess."),
                    ("Naming a person instead of a role",
                     "The document breaks the day they change job, and nobody "
                     "notices for months."),
                    ("Never testing it on a real beginner",
                     "The expert review confirms only that experts can follow "
                     "it."),
                    ("Leaving it undated",
                     "A reader cannot tell whether it is current, so they ring "
                     "you to check anyway."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "How much detail is right?",
            "visual": {
                "type": "tree",
                "question": "Could somebody do this wrong and not realise?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Add the check",
                    "detail": "Name what success looks like at that step. "
                              "\"The status turns green\" or \"you receive a "
                              "confirmation email within ten minutes\".",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Keep it short",
                    "detail": "If a mistake is immediately obvious, one line "
                              "is enough. Over-documenting the obvious is how "
                              "SOPs become unreadable.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The handover document",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "What I do daily, weekly and monthly, with the deadlines",
                    "Who to ring for each thing, by role and by name",
                    "The three things most likely to go wrong while I am away",
                    "Where every document, login route and template lives",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The documentation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Write it for the person who has never done it, "
                            "not for the person who already can.",
                "sub": "Every phone call you get is a step you left out "
                       "because it was obvious to you.",
                "cols": 3,
                "items": [
                    "Talk it, then shape it.",
                    "Answer every [GAP].",
                    "Test it on a beginner.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Two days before annual leave",
        "situation": "You are away for a fortnight. Vendor onboarding is "
                     "entirely yours and nothing is written down. You have "
                     "about two hours spare.",
        "choices": [
            {
                "text": "Write the steps from memory as a quick bullet list.",
                "tone": "ok",
                "headline": "Better than nothing, and the phone still rings",
                "consequence": "You produce six confident bullets covering "
                               "what you remember doing. They are all correct "
                               "and none of them names the approval route or "
                               "what to do when a vendor code already exists. "
                               "You get six calls instead of eleven.",
                "rule": "Memory writes what you do, not what a beginner "
                        "needs.",
            },
            {
                "text": "Talk it through into a document, shape it, then run "
                        "the new-joiner test.",
                "tone": "good",
                "headline": "Ninety minutes, and the phone stays quiet",
                "consequence": "Ten minutes of talking gives you raw material. "
                               "The shaping prompt produces fourteen steps and "
                               "four [GAP] markers. The new-joiner test adds "
                               "seven questions, including one about an "
                               "approval you had forgotten existed. You answer "
                               "them all.",
                "rule": "The gaps you cannot see are exactly what these two "
                        "prompts are for.",
            },
            {
                "text": "Record a video walkthrough and leave it for the team.",
                "tone": "ok",
                "headline": "Useful, and nobody can search it",
                "consequence": "A twenty-minute video captures everything, "
                               "including the things you would have forgotten "
                               "to write. It also cannot be searched, scanned "
                               "or updated, so in six months it is out of date "
                               "and nobody knows which part.",
                "rule": "Record it if you like, then use it as the raw "
                        "material for a written procedure.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=xPAQEEYzOH0",
        "title": "How to Write SOPs With AI that ACTUALLY Work",
        "channel": "Layla at ProcessDriven",
        "duration": "5:16",
        "heading": "Five minutes on writing SOPs",
        "note": "An outside video, not company material. Where it differs "
                "from this module, follow this module.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Useful if you prefer watching to reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Why do experts write bad procedures?",
            "remember": "You stop seeing the obvious steps.",
            "answers": [
                {"text": "They write too much detail", "ok": False,
                 "why": "Usually the opposite. Experts write too little, "
                        "because four minutes of automatic work collapses into "
                        "a single six-word line."},
                {"text": "The steps they stopped noticing get left out",
                 "ok": True,
                 "why": "After four years, which system, which tab and whose "
                        "approval are invisible to you. They are the first "
                        "four questions a new joiner has."},
                {"text": "They use too much jargon", "ok": False,
                 "why": "Jargon is a real problem and an easy one to fix on "
                        "review. Missing steps are harder, because you cannot "
                        "see the hole."},
                {"text": "They write in the wrong order", "ok": False,
                 "why": "Order is usually the one thing experts get right. It "
                        "is completeness that suffers."},
            ],
        },
        {
            "q": "What makes a step followable?",
            "remember": "One action, starting with a verb, naming the place.",
            "answers": [
                {"text": "It explains why the step exists", "ok": False,
                 "why": "Useful context sometimes, but it does not make the "
                        "step doable. Someone can understand why and still not "
                        "know where to click."},
                {"text": "One action, a verb, and the system named", "ok": True,
                 "why": "\"Open the vendor master in SAP and enter the tax "
                        "code in field 4\" can be done. \"Raise the vendor "
                        "record\" cannot, by anyone new."},
                {"text": "It is under ten words", "ok": False,
                 "why": "Brevity is not the goal. A fifteen-word step that "
                        "names the screen beats a six-word one that assumes "
                        "you know it."},
                {"text": "It matches the system's own terminology", "ok": False,
                 "why": "Helpful, and not sufficient. Correct terminology in a "
                        "step that bundles three actions together is still "
                        "unfollowable."},
            ],
        },
        {
            "q": "What does the [GAP] marker find?",
            "remember": "Steps you never knew you were skipping.",
            "answers": [
                {"text": "Grammar problems in your explanation", "ok": False,
                 "why": "It is not a language check. It marks places where a "
                        "beginner would need information your explanation "
                        "never contained."},
                {"text": "Information a beginner needs that you did not give",
                 "ok": True,
                 "why": "Exactly the blind spot experts have. Without the "
                        "marker the tool fills the gap with a plausible step, "
                        "and a plausible wrong step is worse than a missing "
                        "one."},
                {"text": "Steps that are in the wrong order", "ok": False,
                 "why": "Reordering is a separate job it does well. [GAP] is "
                        "specifically about missing information, not sequence."},
                {"text": "Steps that could be automated", "ok": False,
                 "why": "A different and later question. First get the process "
                        "written down accurately, then look at what could be "
                        "automated."},
            ],
        },
        {
            "q": "Who should test the procedure?",
            "remember": "Somebody who has never done it.",
            "answers": [
                {"text": "The person who wrote it", "ok": False,
                 "why": "They will follow it perfectly, because they are "
                        "filling every gap from memory without noticing they "
                        "are doing it."},
                {"text": "Somebody who has never done the task", "ok": True,
                 "why": "Every place they hesitate is a defect in the "
                        "document. Watch without helping and write down each "
                        "pause — ten minutes of this is worth more than any "
                        "review."},
                {"text": "The manager who owns the process", "ok": False,
                 "why": "They know it too well to test it, and they usually "
                        "know a slightly different version, which produces "
                        "confusing feedback."},
                {"text": "Nobody — the AI test is enough", "ok": False,
                 "why": "The AI test finds the predictable gaps and it is "
                        "genuinely useful. A real beginner finds the ones "
                        "neither of you anticipated."},
            ],
        },
        {
            "q": "What keeps a document alive?",
            "remember": "A date, an owner, and fixing it on use.",
            "answers": [
                {"text": "A formal annual review", "ok": False,
                 "why": "Annual reviews catch a year of drift at once, badly, "
                        "and are usually skipped. Documents rot continuously, "
                        "not once a year."},
                {"text": "Correcting it the moment somebody hits a wrong step",
                 "ok": True,
                 "why": "The error is in front of you and the fix takes two "
                        "minutes. Correcting the person and not the document "
                        "guarantees the next person hits the same wall."},
                {"text": "Locking it so only one person can edit", "ok": False,
                 "why": "That makes updating slow, so updating stops. A named "
                        "owner who welcomes corrections beats a locked file."},
                {"text": "Keeping it short", "ok": False,
                 "why": "Length has little to do with rot. A short document "
                        "goes out of date exactly as fast as a long one."},
            ],
        },
    ],

    "recap": {
        "title": "Documentation on one screen",
        "points": [
            ("Experts leave out the obvious",
             "The steps you stopped noticing are the first four questions a "
             "beginner has."),
            ("Talk it, then shape it",
             "Explaining out loud produces better raw material than writing "
             "does."),
            ("One action per step",
             "Start with a verb, name the system, say what success looks "
             "like."),
            ("Answer every [GAP]",
             "The marker exists so a missing step is visible rather than "
             "invented."),
            ("Test it on a beginner",
             "Every hesitation is a defect. Watch, do not help, write it "
             "down."),
            ("Date it and own it",
             "Undated documents get ignored. Unowned documents never get "
             "fixed."),
        ],
        "oneliner": "Write it for the person who has never done it, not for "
                    "the person who already can.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("doc", "The shaping prompt",
             "Rambling explanation in, numbered steps and [GAP] markers out."),
            ("person", "The new-joiner test prompt",
             "Every point a beginner would stop and ask."),
            ("cycle", "The update prompt",
             "Change only affected steps, and list which ones."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-08, Meeting Notes & Follow-ups. Turning an "
                "hour of discussion into decisions and owners, before you "
                "leave the room.",
    },

    "glossary": [
        ("SOP", "Standard Operating Procedure. A written process somebody can "
                "follow without asking questions."),
        ("[GAP]", "A marker the tool writes where a beginner would need "
                  "information you did not supply."),
        ("Handover", "A document covering what you do, who to call, and what "
                     "usually goes wrong while you are away."),
        ("Curse of knowledge", "The habit of leaving out steps that have "
                               "become invisible to you through practice."),
        ("Prompt", "Everything you type in: your explanation and the "
                   "constraints on shaping it."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
