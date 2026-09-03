# -*- coding: utf-8 -*-
"""AI-03 — AI Capabilities. Content only."""

DECK = {
    "module_code": "AI-03",
    "area": "01-ai-general",
    "filename": "01-03-ai-capabilities.pptx",
    "title": "AI Capabilities",
    "subtitle": "The tasks where these tools genuinely save you an hour — and "
                "how to spot one on your own desk.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Deepa loses every Monday to formatting",
        "icon": "clock",
        "scenario": "Deepa prepares the MIS pack for a Chennai office. Every "
                    "Monday she pastes the same 40 rows into a document, "
                    "rewrites the headings, and turns the numbers into "
                    "sentences for the management summary. The analysis takes "
                    "twenty minutes. The formatting takes three hours.",
        "cost": "Three hours a week on shape, not on the numbers themselves.",
        "fix": "The shape work is exactly what these tools do best.",
    },

    "outcomes": [
        ("sheet", "Name the four job shapes AI handles well, from memory"),
        ("eye", "Look at a task on your desk and tell in ten seconds if it fits"),
        ("cycle", "Convert a repeated weekly job into a prompt you reuse"),
        ("bulb", "Use it to get unstuck instead of staring at a blank page"),
        ("warn", "Recognise the tasks that look like a fit and are not"),
    ],

    "sections": [
        ("The four job shapes", "What it is actually good at", "s_shapes"),
        ("Turning shape into time", "The weekly jobs it removes", "s_time"),
        ("Getting unstuck", "When you cannot start", "s_stuck"),
        ("Spot one on your desk", "A ten-second test", "s_spot"),
        ("Where the value stops", "Fits that are not fits", "s_stop"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "A 14-minute tour of real uses", "video"),
    ],

    "slides": [
        {
            "anchor": "s_shapes",
            "label": "The four job shapes",
            "title": "Four shapes it handles well",
            "lead": "Almost every useful AI task at work is one of these four. "
                    "None of them require it to know anything.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "TURN INTO — facts into sentences, notes into a report",
                    "SHORTEN — twelve pages into the six lines that matter",
                    "RESHAPE — a paragraph into a table, formal into plain",
                    "GENERATE OPTIONS — ten subject lines, five ways to say no",
                ],
            },
        },
        {
            "label": "The four job shapes",
            "title": "What they have in common",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You already hold the facts", "Nothing has to be looked "
                                                   "up by the tool."),
                    ("The work is language", "Wording, ordering, length, "
                                             "tone, layout."),
                    ("You can check it fast", "Every line traces back to "
                                              "something you supplied."),
                    ("The risk is low", "The worst case is a clumsy draft, "
                                        "not a wrong fact."),
                ],
            },
        },
        {
            "anchor": "s_time",
            "label": "Turning shape into time",
            "title": "The weekly jobs it removes",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "The recurring write-up",
                     "sub": "A weekly delay note, a monthly summary, a site "
                            "visit report. Same shape, new facts each time."},
                    {"icon": "sheet", "label": "The reformat",
                     "sub": "Rows into prose. Prose into a table. A long "
                            "thread into a decision list."},
                    {"icon": "mail", "label": "The awkward reply",
                     "sub": "Chasing a payment, refusing a request, "
                            "apologising without accepting blame."},
                ],
            },
        },
        {
            "label": "Turning shape into time",
            "title": "Deepa's three hours, in one prompt",
            "visual": {
                "type": "prompt_out",
                "text": "Turn these figures into a 150-word management "
                        "summary. State the three biggest movements and "
                        "nothing else. Do not add causes I have not given "
                        "you. Figures: dispatches 412 against a plan of 460; "
                        "rejections 2.1 per cent against 1.4 last month; "
                        "overtime hours 380 against 250.",
                "caption": "Paste it as written, then swap in your own "
                           "figures.",
                "out_title": "What comes back",
                "out": [
                    "A 150-word summary naming the three movements, in the "
                    "order you listed them.",
                    "No invented causes, because you told it not to add any.",
                    "Three hours of formatting becomes ten minutes of "
                    "checking.",
                ],
            },
        },
        {
            "anchor": "s_stuck",
            "label": "Getting unstuck",
            "title": "When you cannot start",
            "lead": "A blank page costs more time than a bad draft ever will. "
                    "This is the cheapest use of all.",
            "visual": {
                "type": "prompt",
                "header": "Copy this unblocking prompt",
                "text": "I have to write a proposal for a client who wants "
                        "faster delivery at the same price. I do not know how "
                        "to structure it. Give me a five-part outline with one "
                        "line describing what goes in each part. Do not write "
                        "the proposal itself.",
                "caption": "Ask for the structure first. Write the content "
                           "yourself.",
                "why": [
                    "An outline is judgement you can check in seconds.",
                    "It cannot invent facts if you asked only for headings.",
                    "You start writing from part two, not from nothing.",
                ],
            },
        },
        {
            "label": "Getting unstuck",
            "title": "Three unblocking moves",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "list", "label": "Ask for a structure",
                     "sub": "\"Give me a five-part outline.\" You keep every "
                            "decision that matters."},
                    {"icon": "chat", "label": "Ask for the questions",
                     "sub": "\"What should I ask this supplier before I "
                            "agree?\" A checklist beats a blank page."},
                    {"icon": "bulb", "label": "Ask for ten, keep one",
                     "sub": "\"Ten subject lines for this email.\" Choosing is "
                            "far faster than inventing."},
                ],
            },
        },
        {
            "anchor": "s_spot",
            "label": "Spot one on your desk",
            "title": "The ten-second test",
            "visual": {
                "type": "tree",
                "question": "Do I already know everything the answer needs?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Good fit",
                    "detail": "You are asking for language, not for knowledge. "
                              "Give it your facts, set the length and tone, "
                              "and check the draft against what you typed.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Poor fit",
                    "detail": "You are asking it to supply a fact it has no "
                              "access to. It will produce one anyway. Go to "
                              "the system, the file or the person instead.",
                },
            },
        },
        {
            "label": "Spot one on your desk",
            "title": "Do this now: find one job",
            "visual": {
                "type": "steps",
                "items": [
                    "Look at your calendar for last week.",
                    "Find one task you did that was mostly typing, not "
                    "deciding.",
                    "Write down the facts you had before you started it.",
                    "Paste the prompt on the right, with those facts in it.",
                ],
                "prompt": "I am going to give you facts and I want you to "
                          "write the document. Do not add anything I have not "
                          "told you. If something important is missing, list "
                          "the questions at the end instead of guessing. Here "
                          "are the facts:",
                "caption": "The last sentence is what stops it inventing. Keep "
                           "it in every time.",
            },
        },
        {
            "anchor": "s_stop",
            "label": "Where the value stops",
            "title": "Fits that are not fits",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Looks like a fit", "tone": "bad",
                    "title": "But it is not",
                    "items": [
                        "\"Summarise our contract with this supplier\"",
                        "\"What is the current rate for this material?\"",
                        "\"Is this clause enforceable in the UAE?\"",
                        "\"How many units did we ship last month?\"",
                    ],
                },
                "right": {
                    "tag": "Actually a fit", "tone": "good",
                    "title": "Same job, reframed",
                    "items": [
                        "\"Draft questions to ask before I sign this\"",
                        "\"Word this rate request to the supplier\"",
                        "\"List what I should ask our lawyer\"",
                        "\"Turn these shipment figures into a summary\"",
                    ],
                },
            },
        },
        {
            "label": "Where the value stops",
            "title": "The reframe that rescues a task",
            "lead": "Most poor-fit tasks become good-fit tasks if you move the "
                    "knowledge back to your side.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Asking it to know",
                "bad": [
                    "\"What does our late-delivery penalty clause say?\"",
                    "It produces a clause. The clause sounds standard and "
                    "reasonable.",
                    "It is not your clause, and nothing on screen tells you "
                    "that.",
                ],
                "good_tag": "Asking it to write",
                "good": [
                    "You open the contract and read the clause yourself.",
                    "\"Explain this clause in plain English for a customer.\"",
                    "You get a clear explanation of the words you actually "
                    "pasted.",
                ],
                "note": "Move the knowing to your side of the desk. Leave the "
                        "wording on its side.",
            },
        },
        {
            "label": "Where the value stops",
            "title": "Four checks before you rely on it",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Every fact in the output appeared somewhere in my input.",
                    "Nothing has been added that I would have to defend.",
                    "The numbers match the source I copied them from.",
                    "I could explain where each line came from, if asked.",
                ],
            },
        },
        {
            "label": "Where the value stops",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Using it as a search engine",
                     "It answers rather than admitting it cannot look things "
                     "up. The answer looks identical either way."),
                    ("Giving it three words and expecting judgement",
                     "It matches the effort you put in. Four words in gives "
                     "you a form letter back."),
                    ("Asking it to decide, not to draft",
                     "It carries none of the consequences, so it will agree "
                     "with whatever you seem to want."),
                    ("Redoing the same prompt every week",
                     "The weekly job is the one worth saving. Store it once "
                     "and refill the facts."),
                    ("Not saying \"do not add anything\"",
                     "Without that line it will fill every gap it finds, and "
                     "the gaps are invisible to you."),
                ],
            },
        },
        {
            "label": "Where the value stops",
            "title": "What good use looks like",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Same job, less time",
                     "sub": "A three-hour formatting job becomes ten minutes "
                            "of checking. The judgement stays with you."},
                    {"icon": "check", "label": "Same quality, less strain",
                     "sub": "English you are not fully confident in stops "
                            "being the reason a good point lands badly."},
                    {"icon": "cycle", "label": "Better on the second try",
                     "sub": "You keep the prompt that worked, so next week "
                            "starts where this week finished."},
                ],
            },
        },
        {
            "label": "Where the value stops",
            "title": "The capability rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "It is excellent at language and useless at "
                            "knowing. Match your task to that.",
                "sub": "Every good use and every bad use of these tools comes "
                       "back to this one line.",
                "cols": 3,
                "items": [
                    "Language work — give it to the tool.",
                    "Knowledge work — keep it on your side.",
                    "Judgement work — that is your job, always.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 8:50 am",
        "situation": "The MIS pack is due at noon. You have the figures in a "
                     "spreadsheet and a blank management summary to write. "
                     "Your manager wants to know why rejections rose.",
        "choices": [
            {
                "text": "Paste the figures and ask it to explain why "
                        "rejections rose.",
                "tone": "bad",
                "headline": "It will give you a reason. It has none.",
                "consequence": "It produces three plausible causes — a "
                               "supplier change, an operator training gap, a "
                               "seasonal effect. None came from your data, "
                               "because your data contains no causes. Your "
                               "manager acts on the first one.",
                "rule": "It can describe what the numbers do. It cannot know "
                        "why they did it.",
            },
            {
                "text": "Ask it to state the three biggest movements, with no "
                        "causes added.",
                "tone": "good",
                "headline": "Exactly the right division of labour",
                "consequence": "You get a clean 150-word summary of what "
                               "changed, in the order you gave it. You then "
                               "spend fifteen minutes on the part only you can "
                               "do — calling the line supervisor to find out "
                               "why. The pack goes out at 11:20.",
                "rule": "Let it describe. Do the explaining yourself.",
            },
            {
                "text": "Write the whole summary by hand, as always.",
                "tone": "ok",
                "headline": "It will be fine. It will also be noon.",
                "consequence": "The summary is good, because you know the "
                               "numbers. It also takes three hours, and the "
                               "three hours went on sentence construction "
                               "rather than on the rejection question your "
                               "manager actually asked about.",
                "rule": "Spend your hours on the part that needs you.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=mWRe8w6YjO0",
        "title": "7 Life-Changing Uses of AI I Wish I Knew Earlier",
        "channel": "Kevin Stratvert",
        "duration": "14:29",
        "heading": "Fourteen minutes of real uses",
        "note": "An outside video, not company material. It shows tools "
                "rather than the method — the method is in this module.",
        "how": [
            "Optional. The four job shapes above are the method.",
            "Useful for seeing what other people actually do with it.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which of these is a good fit?",
            "remember": "Language work fits. Knowledge work does not.",
            "answers": [
                {"text": "\"Summarise our supplier contract\"", "ok": False,
                 "why": "It has never seen the contract. It will produce a "
                        "summary of a typical supplier contract, which reads "
                        "convincingly and describes an agreement you do not "
                        "have."},
                {"text": "\"Turn these six figures into a short summary\"",
                 "ok": True,
                 "why": "You supplied every number. The only work left is "
                        "language, and you can check each sentence against "
                        "your own figures in under a minute."},
                {"text": "\"What did we quote this customer last year?\"",
                 "ok": False,
                 "why": "That lives in your system, not in the model. Asking "
                        "here produces a number with no source, which is worse "
                        "than no number at all."},
                {"text": "\"Should we drop this product line?\"", "ok": False,
                 "why": "A judgement with money attached, and it holds none of "
                        "the history and none of the consequences. Ask it for "
                        "the questions to consider, never for the decision."},
            ],
        },
        {
            "q": "What makes a task a poor fit?",
            "remember": "If it has to know something you did not tell it, stop.",
            "answers": [
                {"text": "The task is long", "ok": False,
                 "why": "Length is not the problem. A twelve-page document you "
                        "paste in is a perfectly good fit, because you have "
                        "supplied everything it needs."},
                {"text": "It needs a fact you did not supply", "ok": True,
                 "why": "That is the whole test. Anything it must know rather "
                        "than write is a gap, and gaps get filled with "
                        "plausible inventions rather than left blank."},
                {"text": "The task is boring", "ok": False,
                 "why": "Boring and repetitive is the ideal case, not the "
                        "problem. The weekly reformat is exactly the job worth "
                        "handing over."},
                {"text": "You have done it before", "ok": False,
                 "why": "Having done it before is an advantage — you already "
                        "know what good looks like, so you can check the draft "
                        "in seconds."},
            ],
        },
        {
            "q": "Which line stops it inventing?",
            "stem": "You are writing a prompt that hands over a set of facts "
                    "and asks for a document back.",
            "remember": "\"Do not add anything I have not told you.\"",
            "answers": [
                {"text": "\"Please be accurate\"", "ok": False,
                 "why": "It has no way to act on that. It cannot tell which of "
                        "its own sentences are accurate, so asking for "
                        "accuracy changes nothing about the output."},
                {"text": "\"Do not add anything I have not given you\"",
                 "ok": True,
                 "why": "This is the single most useful line in any work "
                        "prompt. It converts silent gap-filling into visible "
                        "gaps, which you can then fill correctly yourself."},
                {"text": "\"Use only reliable sources\"", "ok": False,
                 "why": "There are no sources involved. It is not consulting "
                        "anything, so instructing it about source quality is "
                        "instructing it about something that does not happen."},
                {"text": "\"Check your answer before replying\"", "ok": False,
                 "why": "It will generate text that says it has checked. That "
                        "is not the same as checking, and there is nothing for "
                        "it to check against."},
            ],
        },
        {
            "q": "The blank page problem. Best move?",
            "remember": "Ask for the structure. Write the content.",
            "answers": [
                {"text": "Ask it to write the whole proposal", "ok": False,
                 "why": "You get 600 confident words about a client you have "
                        "not described. Almost all of it will need replacing, "
                        "and spotting what to replace takes longer than "
                        "writing."},
                {"text": "Ask for a five-part outline and write it yourself",
                 "ok": True,
                 "why": "An outline is pure structure — no facts to invent. "
                        "You can judge it in ten seconds, and then you are "
                        "starting from part two instead of from nothing."},
                {"text": "Wait until you feel clearer about it", "ok": False,
                 "why": "The blank page rarely improves with time. This is the "
                        "cheapest and lowest-risk use of the tool there is, "
                        "and it costs you thirty seconds."},
                {"text": "Copy last year's proposal and edit it", "ok": False,
                 "why": "Often reasonable, but it drags last year's assumptions "
                        "in with it. Those are much harder to spot than a "
                        "fresh outline you actively agreed with."},
            ],
        },
        {
            "q": "What should stay entirely yours?",
            "remember": "Describe with the tool. Decide without it.",
            "answers": [
                {"text": "The wording of a difficult email", "ok": False,
                 "why": "Wording is exactly what to hand over. You decide what "
                        "the email must achieve; the tool finds a clean way to "
                        "say it."},
                {"text": "The decision and the reason behind it", "ok": True,
                 "why": "It carries no consequences, holds none of the "
                        "history, and will agree with whatever you seem to "
                        "want. The decision, and your reason for it, stay on "
                        "your side of the desk."},
                {"text": "The layout of a table", "ok": False,
                 "why": "Pure shape work. Name your columns, say \"no extra "
                        "commentary\", and you get something you can paste "
                        "straight into a document."},
                {"text": "The length of a summary", "ok": False,
                 "why": "Say the number and it obeys. Length is one of the "
                        "easiest and most valuable things to hand over."},
            ],
        },
    ],

    "recap": {
        "title": "AI Capabilities on one screen",
        "points": [
            ("Four shapes it does well",
             "Turn into, shorten, reshape, generate options. All language, no "
             "knowledge."),
            ("The ten-second test",
             "Do I already know everything the answer needs? If no, it is a "
             "poor fit."),
            ("Reframe a poor fit",
             "Move the knowing to your side. Ask it to write, never to know."),
            ("The line that stops invention",
             "\"Do not add anything I have not given you.\" Put it in every "
             "prompt."),
            ("Save the weekly job",
             "The task you repeat is the one worth turning into a stored "
             "prompt."),
            ("Judgement stays with you",
             "It can describe what happened. It cannot know why, and it "
             "carries no consequences."),
        ],
        "oneliner": "It is excellent at language and useless at knowing. Every "
                    "good use of it starts from that one sentence.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("sheet", "The figures-into-summary prompt",
             "Three movements, no invented causes, 150 words."),
            ("list", "The outline prompt",
             "Five parts, one line each, and nothing written for you."),
            ("shield", "The no-invention line",
             "\"Do not add anything I have not given you.\""),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: AI-04, AI Limitations. It covers the places "
                "these tools break, why they break there, and what to reach "
                "for instead.",
    },

    "glossary": [
        ("Capability", "Something the tool can reliably do. Here it means "
                       "language work, not knowledge work."),
        ("Prompt", "Everything you type in: the request plus the facts you "
                   "supply."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
        ("Hallucination", "A confident, invented answer. Usually a name, a "
                          "number, a date or a policy."),
        ("Context", "The background you give so the tool knows who the text is "
                    "for and why."),
        ("Model", "The trained system behind the app you are typing into."),
    ],
}
