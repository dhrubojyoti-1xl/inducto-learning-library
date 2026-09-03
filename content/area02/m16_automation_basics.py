# -*- coding: utf-8 -*-
"""DW-11 — Automation Basics. Content only."""

DECK = {
    "module_code": "DW-11",
    "area": "02-ai-daily-work",
    "filename": "02-11-automation-basics.pptx",
    "title": "Automation Basics",
    "subtitle": "Spotting the jobs worth automating, and describing one "
                "clearly enough that somebody can actually build it.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "flow",
    "cover_image": "assets/hero-automation.jpg",

    "why": {
        "title": "The same report, 240 times a year",
        "icon": "cycle",
        "scenario": "Every weekday, someone in a Chennai office downloads two "
                    "files, pastes them into a third, deletes four columns, "
                    "and emails the result to six people. It takes 25 "
                    "minutes. It has been done this way for three years.",
        "cost": "About 100 hours a year, on copying and deleting.",
        "fix": "You do not need to build it. You need to describe it well "
               "enough.",
    },

    "outcomes": [
        ("eye", "Spot which of your regular jobs is worth automating"),
        ("ban", "Recognise the ones that should never be automated"),
        ("doc", "Write a request clear enough for somebody to build from"),
        ("list", "Describe a process as triggers, steps and exceptions"),
        ("shield", "Know what a running automation must never be allowed to "
                   "do"),
    ],

    "sections": [
        ("What can be automated", "Rules, not judgement", "s_what"),
        ("Spotting a candidate", "Four questions", "s_spot"),
        ("Describing it properly", "Trigger, steps, exceptions", "s_describe"),
        ("What must stay manual", "Where automation hurts", "s_manual"),
        ("Do this now", "Describe one real job", "s_do"),
        ("Choose what you'd do", "A process-review decision", "scenario"),
        ("Watch this", "A 7-minute outside overview", "video"),
    ],

    "slides": [
        {
            "anchor": "s_what",
            "label": "What can be automated",
            "title": "Rules can be automated",
            "lead": "If you can write the job as \"when this happens, do "
                    "exactly that\", it can be automated. If you cannot, it "
                    "cannot.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Automatable", "tone": "good",
                    "title": "Same input, same action",
                    "items": [
                        "Move files that arrive into a dated folder",
                        "Email a report every Monday at eight",
                        "Flag any invoice over a set value",
                        "Copy fields from a form into a sheet",
                    ],
                },
                "right": {
                    "tag": "Not automatable", "tone": "bad",
                    "title": "Requires a judgement",
                    "items": [
                        "Decide whether a complaint deserves a credit",
                        "Choose which supplier to trust this quarter",
                        "Word a difficult message to a client",
                        "Decide when a rule should be broken",
                    ],
                },
            },
        },
        {
            "label": "What can be automated",
            "title": "The three parts of any automation",
            "gloss": ["Trigger"],
            "visual": {
                "type": "flow",
                "steps": [
                    ("A trigger", "What starts it. A time, a file, an email, "
                                  "a form."),
                    ("Steps", "Exactly what happens, in order, with no "
                              "choices."),
                    ("Exceptions", "What to do when reality does not match "
                                   "the rule."),
                    ("A human", "Who gets told when an exception happens."),
                ],
            },
        },
        {
            "anchor": "s_spot",
            "label": "Spotting a candidate",
            "title": "Four questions that find one",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Do I do this more than twice a week?",
                    "Do I do it exactly the same way every time?",
                    "Would a colleague do it identically from my instructions?",
                    "Does it move or reshape data rather than judge it?",
                ],
            },
        },
        {
            "label": "Spotting a candidate",
            "title": "Four yeses is a candidate",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "cycle", "label": "Frequent",
                     "sub": "Twice a week is 100 times a year. Twenty-five "
                            "minutes each is a working fortnight."},
                    {"icon": "list", "label": "Identical",
                     "sub": "If it varies, write down what varies. That is "
                            "usually the exception list."},
                    {"icon": "sheet", "label": "Mechanical",
                     "sub": "Copying, moving, renaming, filtering, sending. No "
                            "decisions in the middle."},
                ],
            },
        },
        {
            "anchor": "s_describe",
            "label": "Describing it properly",
            "title": "Describe it, do not build it",
            "lead": "Most automation requests fail because the description is "
                    "vague, not because the tool was wrong.",
            "visual": {
                "type": "prompt",
                "header": "Copy this description prompt",
                "text": "Help me describe a manual process so somebody could "
                        "automate it. Ask me one question at a time until you "
                        "have: the trigger, every step in order, every "
                        "exception, and who should be told when an exception "
                        "happens. Do not suggest tools yet. Start with your "
                        "first question.",
                "caption": "One question at a time is what makes this work.",
                "why": [
                    "Interviewing you finds steps you would not have written "
                    "down.",
                    "\"No tools yet\" keeps the focus on the process.",
                    "You end up with a specification, not a wish.",
                ],
            },
        },
        {
            "label": "Describing it properly",
            "title": "Vague request, clear request",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "What usually gets asked",
                "bad": [
                    "\"Can we automate the daily report?\"",
                    "Nobody knows which files, which columns, or who receives "
                    "it.",
                    "Three meetings later it is still being discussed.",
                ],
                "good_tag": "What gets built",
                "good": [
                    "\"Every weekday at 07:00, take the two files from this "
                    "folder...\"",
                    "\"...remove columns D, F, H and K, merge on order number, "
                    "email to this group.\"",
                    "\"If either file is missing at 07:15, email me and stop.\"",
                ],
                "note": "The second one can be built by somebody who has never "
                        "seen your job. That is the whole test.",
            },
        },
        {
            "anchor": "s_manual",
            "label": "What must stay manual",
            "title": "Where automation hurts",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Automating an approval",
                     "The approval was the control. Automating it removes the "
                     "only place a human looked."),
                    ("Auto-sending to customers",
                     "One bad input becomes 400 wrong emails before anybody "
                     "notices."),
                    ("Automating a broken process",
                     "You now do the wrong thing reliably, at speed, without "
                     "anyone watching."),
                    ("Hiding the exceptions",
                     "If nobody is told when it fails, it fails silently for "
                     "months."),
                    ("Automating something one person understands",
                     "When they leave, nobody knows what it does or how to "
                     "stop it."),
                ],
            },
        },
        {
            "label": "What must stay manual",
            "title": "The rule about approvals",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Automate the work. Never automate the check on "
                            "the work.",
                "sub": "If a step exists so that a human looks at something, "
                       "that step is the point.",
                "cols": 3,
                "items": [
                    "Payments — a person approves.",
                    "Customer messages — a person sends.",
                    "Anything irreversible — a person decides.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: describe one job",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick the job you do most often that has no thinking in "
                    "it.",
                    "Run the interview prompt and answer its questions "
                    "honestly.",
                    "Add every exception you can remember from the last year.",
                    "Send the result to [COMPANY INPUT NEEDED: who handles "
                    "automation requests].",
                ],
                "prompt": "Interview me one question at a time to document a "
                          "manual process for automation. I need: the trigger, "
                          "the steps in order, every exception, and who is "
                          "told when an exception happens. Do not suggest "
                          "tools. Do not ask for real data. Begin.",
                "caption": "Twenty minutes of questions produces something "
                           "buildable.",
            },
        },
        {
            "label": "Do this now",
            "title": "Exceptions are the hard part",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this exception prompt",
                "text": "Here is a process description. List every way this "
                        "could go wrong in practice: missing input, wrong "
                        "format, duplicate, late arrival, partial data, and "
                        "anything else. For each, suggest what the automation "
                        "should do instead of guessing. One line each.",
                "caption": "Most automations fail on the cases nobody listed.",
                "out_title": "What comes back",
                "out": [
                    "Ten to fifteen failure cases, several you had not "
                    "considered.",
                    "A suggested safe behaviour for each, usually \"stop and "
                    "tell a human\".",
                    "The list that turns a fragile script into a reliable one.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Three rules for anything running",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "It must stop and tell someone when reality does not "
                    "match.",
                    "A named person owns it, and anyone can switch it off.",
                    "It never sends externally without a human pressing send.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "What must never be in the description",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Describing a process needs the shape of the data, "
                            "never the data itself.",
                "sub": "Column names and formats are enough for anyone to "
                       "build from.",
                "cols": 2,
                "items": [
                    "Real customer records used as the example",
                    "Passwords, API keys or shared login details",
                    "Internal system addresses posted outside the company",
                    "Live financial figures used to illustrate a step",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Is it worth automating?",
            "visual": {
                "type": "tree",
                "question": "Does this cost more than a day a year?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Write it up",
                    "detail": "Twenty-five minutes a day is a hundred hours a "
                              "year. Even a rough automation that handles the "
                              "normal case pays for itself in weeks.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Leave it alone",
                    "detail": "A monthly ten-minute job costs two hours a "
                              "year. Automating it costs more than that to "
                              "build, document and maintain.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The automation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If you cannot write it as rules with no choices "
                            "in the middle, it is not ready to automate.",
                "sub": "The writing is the work. Building is usually the easy "
                       "part afterwards.",
                "cols": 3,
                "items": [
                    "Rules — automate.",
                    "Judgement — keep.",
                    "Exceptions — always to a human.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Process review, Wednesday",
        "situation": "Your manager asks which of your jobs could be automated. "
                     "You have the daily report, the monthly reconciliation "
                     "and the credit note approvals.",
        "choices": [
            {
                "text": "Propose automating the credit note approvals — they "
                        "take longest.",
                "tone": "bad",
                "headline": "You would be removing the control, not the work",
                "consequence": "Approvals take time because somebody is "
                               "looking. Automate that and credit notes issue "
                               "themselves against rules that cannot see "
                               "context. The first disputed one has no human "
                               "decision behind it at all.",
                "rule": "If a step exists so a person looks, that step is the "
                        "point.",
            },
            {
                "text": "Propose the daily report, described as trigger, steps "
                        "and exceptions.",
                "tone": "good",
                "headline": "Twenty-five minutes a day, and no judgement in it",
                "consequence": "You write it up properly: 07:00 trigger, named "
                               "folders, exact columns, the recipient group, "
                               "and \"if a file is missing by 07:15, email me "
                               "and stop\". It is built in two days and saves a "
                               "hundred hours a year.",
                "rule": "Frequent, identical, mechanical. Four yeses is a "
                        "candidate.",
            },
            {
                "text": "Say nothing is automatable — every job needs "
                        "judgement.",
                "tone": "ok",
                "headline": "True of parts, and not of the copying",
                "consequence": "Real judgement lives in the approvals and the "
                               "exceptions. But deleting four columns and "
                               "merging two files involves no judgement "
                               "whatsoever, and it is a fortnight of your year.",
                "rule": "Separate the judgement from the copying. Automate "
                        "only the second.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=dFSnam97YbQ",
        "title": "From Idea to AI: Building Applications with Generative AI",
        "channel": "IBM Technology",
        "duration": "7:12",
        "heading": "Seven minutes on how it fits together",
        "note": "Aimed at people building systems. Watch for the overview, not "
                "for the rules — those are in this module.",
        "how": [
            "Optional. You do not need to build anything yourself.",
            "Useful for understanding what you are asking for.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which job can be automated?",
            "remember": "Rules yes, judgement no.",
            "answers": [
                {"text": "Deciding whether a complaint deserves a credit",
                 "ok": False,
                 "why": "That is a judgement weighing history, relationship "
                        "and context. A rule can flag candidates for a person "
                        "to look at, but it cannot make the call."},
                {"text": "Merging two files and emailing the result each "
                         "morning", "ok": True,
                 "why": "Same trigger, same steps, same output, no decisions "
                        "in the middle. Twenty-five minutes a day is a hundred "
                        "hours a year for a process with no thinking in it."},
                {"text": "Choosing which supplier to use this quarter",
                 "ok": False,
                 "why": "A commercial judgement with money and relationships "
                        "attached. Automation could assemble the comparison, "
                        "but the choice stays with a person."},
                {"text": "Wording a reply to an unhappy customer", "ok": False,
                 "why": "Every one is different and the tone depends on "
                        "context a rule cannot see. Draft it with AI by all "
                        "means, but a person sends it."},
            ],
        },
        {
            "q": "What is the hard part of a spec?",
            "remember": "The exceptions, not the steps.",
            "answers": [
                {"text": "Choosing the right tool", "ok": False,
                 "why": "Tool choice is usually the easiest decision and "
                        "belongs to whoever builds it. A clear description "
                        "makes the tool almost obvious."},
                {"text": "Listing what happens when reality does not match",
                 "ok": True,
                 "why": "Normal-case steps take ten minutes to write. Missing "
                        "files, duplicates, wrong formats and late arrivals "
                        "are where automations actually fail, usually "
                        "silently."},
                {"text": "Writing the steps in order", "ok": False,
                 "why": "You already know the order, because you do it every "
                        "day. Getting it out of your head is quick with a good "
                        "interview prompt."},
                {"text": "Estimating the time saved", "ok": False,
                 "why": "Straightforward arithmetic: minutes times frequency. "
                        "Useful for making the case, and not the hard part of "
                        "the specification."},
            ],
        },
        {
            "q": "What must an automation always do?",
            "remember": "Stop and tell someone.",
            "answers": [
                {"text": "Run without any human involvement", "ok": False,
                 "why": "That is the goal for the normal case and a serious "
                        "risk for the abnormal one. Something running "
                        "unattended with no failure route fails silently for "
                        "months."},
                {"text": "Stop and notify a person when something is wrong",
                 "ok": True,
                 "why": "Every automation meets a case nobody predicted. "
                        "Stopping and telling a named person turns a silent "
                        "failure into a five-minute fix."},
                {"text": "Log everything it does", "ok": False,
                 "why": "Good practice and not sufficient. A log nobody reads "
                        "does not help when the report has been wrong for "
                        "three weeks."},
                {"text": "Be built by the IT team", "ok": False,
                 "why": "Who builds it matters far less than whether the "
                        "exceptions were described and somebody is named as "
                        "its owner."},
            ],
        },
        {
            "q": "Which should stay manual?",
            "remember": "Anything that exists so a human looks.",
            "answers": [
                {"text": "Moving arriving files into dated folders", "ok": False,
                 "why": "Purely mechanical, high frequency, no judgement. One "
                        "of the easiest and safest things to automate."},
                {"text": "Approving a payment", "ok": True,
                 "why": "The approval is a control, not a task. Its whole "
                        "purpose is that a person looked before money moved, "
                        "and automating it removes the only check in the "
                        "chain."},
                {"text": "Emailing a fixed report to a fixed group", "ok": False,
                 "why": "Fine to automate internally, as long as it stops and "
                        "tells somebody when an input is missing rather than "
                        "sending an empty report."},
                {"text": "Flagging invoices over a threshold", "ok": False,
                 "why": "Flagging is ideal automation — a rule with no "
                        "judgement. What happens after the flag is where the "
                        "person comes in."},
            ],
        },
        {
            "q": "Is a monthly ten-minute job worth it?",
            "remember": "Two hours a year rarely pays for the build.",
            "answers": [
                {"text": "Yes — all repetition should be automated", "ok": False,
                 "why": "Two hours a year does not repay the time to specify, "
                        "build, document and maintain it. Automations also "
                        "need looking after, and rare ones get forgotten."},
                {"text": "No — it costs more to build and maintain than it "
                         "saves", "ok": True,
                 "why": "Ten minutes monthly is two hours a year. Specifying "
                        "and building it costs more than that, and then "
                        "somebody has to remember what it does when it breaks "
                        "next year."},
                {"text": "Yes, if it is easy to build", "ok": False,
                 "why": "Ease of building is only part of the cost. Every "
                        "running automation carries ongoing maintenance and "
                        "the risk of failing quietly."},
                {"text": "Only if a customer sees the output", "ok": False,
                 "why": "Customer-facing output is a reason for more caution, "
                        "not less. It is also a reason to keep a human "
                        "pressing send."},
            ],
        },
    ],

    "recap": {
        "title": "Automation on one screen",
        "points": [
            ("Rules can be automated",
             "\"When this happens, do exactly that.\" If you cannot write it "
             "that way, it is not ready."),
            ("Four questions find a candidate",
             "Frequent, identical, transferable, mechanical. Four yeses and it "
             "is worth writing up."),
            ("Describe, do not build",
             "Trigger, steps in order, exceptions, and who gets told."),
            ("Exceptions are the real work",
             "Missing files, duplicates and wrong formats are where things "
             "fail silently."),
            ("Never automate the check",
             "If a step exists so a person looks, that step is the whole "
             "point."),
            ("Someone owns it, someone can stop it",
             "Named owner, documented purpose, and an off switch anyone can "
             "use."),
        ],
        "oneliner": "Automate the copying. Keep the judgement. Send every "
                    "exception to a human.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The interview prompt",
             "One question at a time until the process is documented."),
            ("warn", "The exception prompt",
             "Every way it could go wrong, and what to do instead."),
            ("check", "The four-question test",
             "Frequent, identical, transferable, mechanical."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next track: PS-01, Business Communication. The skills that "
                "decide whether any of this writing actually lands.",
    },

    "glossary": [
        ("Trigger", "What starts an automation: a time, a file arriving, an "
                    "email, a form submission."),
        ("Exception", "A case where reality does not match the rule. The "
                      "automation should stop and tell someone."),
        ("Specification", "A description clear enough that somebody who has "
                          "never seen your job could build it."),
        ("Owner", "The named person responsible for an automation and for "
                  "switching it off."),
        ("Judgement", "A decision needing context a rule cannot see. Never "
                      "automated."),
        ("Prompt", "Everything you type in: your process description and the "
                   "constraints."),
    ],
}
