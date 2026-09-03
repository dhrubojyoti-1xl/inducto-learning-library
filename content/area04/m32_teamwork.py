# -*- coding: utf-8 -*-
"""PS-09 — Teamwork & Collaboration. Content only."""

DECK = {
    "module_code": "PS-09",
    "area": "04-professional-skills",
    "filename": "04-09-teamwork-and-collaboration.pptx",
    "title": "Teamwork & Collaboration",
    "subtitle": "Handing work over so it arrives finished, and asking for help "
                "without friction.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "network",
    "cover_image": "assets/hero-teamwork.jpg",

    "why": {
        "title": "Anand's handover takes three days",
        "icon": "person",
        "scenario": "Anand passes a costing job to another team in Chennai. He "
                    "sends the file and says \"please complete\". Three days "
                    "and eleven messages later, they still do not know which "
                    "rate card to use or when it is due.",
        "cost": "Three days of messages, for a job that took four hours.",
        "fix": "Four lines with any handover, and the questions never start.",
    },

    "outcomes": [
        ("doc", "Hand work over so it comes back finished, first time"),
        ("chat", "Ask for help in a way that gets a fast answer"),
        ("person", "Say what \"done\" means before anyone starts"),
        ("warn", "Raise a problem with a colleague without a confrontation"),
        ("check", "Give feedback that changes something, not just feelings"),
    ],

    "sections": [
        ("The four-line handover", "What arrives finished", "s_handover"),
        ("Defining done", "The commonest failure", "s_done"),
        ("Asking for help", "Fast answers", "s_help"),
        ("Raising a problem", "Without a confrontation", "s_problem"),
        ("Do this now", "Rewrite one handover", "s_do"),
        ("Choose what you'd do", "A cross-team decision", "scenario"),
        ("Watch this", "A 15-minute outside guide", "video"),
    ],

    "slides": [
        {
            "anchor": "s_handover",
            "label": "The four-line handover",
            "title": "Four lines, no questions",
            "lead": "Most handover friction is not disagreement. It is four "
                    "missing lines that nobody thought to write.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "WHAT — the specific output, not the topic",
                    "DONE MEANS — what it looks like when it is finished",
                    "BY WHEN — a date and a time, not \"end of week\"",
                    "IF STUCK — who to ask, so nobody waits three days",
                ],
            },
        },
        {
            "label": "The four-line handover",
            "title": "The same job, two ways",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "\"Please complete\"",
                "bad": [
                    "A file, and two words.",
                    "Eleven messages over three days about scope and rates.",
                    "It comes back on Thursday in the wrong format.",
                ],
                "good_tag": "Four lines",
                "good": [
                    "\"Costing for the Sharjah tender, using the 2026 rate "
                    "card.\"",
                    "\"Done means every line priced, with exclusions listed at "
                    "the bottom.\"",
                    "\"By Wednesday 3pm. If a rate is missing, ask Priya "
                    "rather than estimating.\"",
                ],
                "note": "Four lines take ninety seconds to write and save "
                        "three days of messages. This is the highest-return "
                        "habit in the module.",
            },
        },
        {
            "anchor": "s_done",
            "label": "Defining done",
            "title": "\"Done\" is the failure point",
            "lead": "Two people can both be right about whether something is "
                    "finished, and disagree completely.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "You meant", "tone": "neutral", "mark": "person",
                    "title": "Ready to send",
                    "items": [
                        "Priced, checked and formatted",
                        "Exclusions listed explicitly",
                        "In the client template",
                        "Ready to go out under your name",
                    ],
                },
                "right": {
                    "tag": "They heard", "tone": "bad",
                    "title": "Numbers filled in",
                    "items": [
                        "All the cells have figures in them",
                        "Assumptions in their head, not written",
                        "In whatever format they work in",
                        "Expecting you to finish it off",
                    ],
                },
            },
        },
        {
            "label": "Defining done",
            "title": "Say what done looks like",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "Done means: every line priced using the 2026 rate "
                        "card, exclusions listed at the bottom, in the client "
                        "template, and ready to send without me editing it. If "
                        "anything is missing, leave it blank and note it "
                        "rather than estimating.",
                "caption": "\"Ready to send without me editing it\" is the "
                           "line that does the work.",
                "why": [
                    "It describes the finished state, not the activity.",
                    "It names the standard, so nobody has to guess.",
                    "\"Leave it blank and note it\" prevents invented "
                    "figures.",
                ],
            },
        },
        {
            "anchor": "s_help",
            "label": "Asking for help",
            "title": "Getting a fast answer",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"Can I pick your brain sometime?\"",
                     "No question, no time, no scope. It gets a yes and then "
                     "nothing happens."),
                    ("\"Are you free?\"",
                     "Nobody answers yes to this without knowing what it "
                     "commits them to."),
                    ("A paragraph of background before the question",
                     "The reader has to work out what is being asked before "
                     "deciding whether they can help."),
                    ("Asking without saying what you tried",
                     "They repeat the two things you already did, and you both "
                     "lose ten minutes."),
                ],
            },
        },
        {
            "label": "Asking for help",
            "title": "The three-line ask",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this structure",
                "text": "I am stuck on the Sharjah costing. I have tried the "
                        "2026 rate card and the old tender file, and neither "
                        "has a rate for site supervision. Do you know where "
                        "that lives, or who would? Two minutes would do it.",
                "caption": "Problem, what you tried, specific question, time "
                           "required.",
                "out_title": "Why it works",
                "out": [
                    "\"What I tried\" stops them suggesting what you already "
                    "did.",
                    "A specific question can be answered in one line, often "
                    "immediately.",
                    "\"Two minutes\" tells them the size before they commit.",
                ],
            },
        },
        {
            "anchor": "s_problem",
            "label": "Raising a problem",
            "title": "Without a confrontation",
            "lead": "Most cross-team problems are process problems that look "
                    "like people problems.",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "\"The costings have come back after the deadline "
                        "three times this quarter, and it is squeezing the "
                        "review. I do not think that is anyone dragging their "
                        "feet — I suspect we are handing them over too late. "
                        "Could we look at the dates together?\"",
                "caption": "Name the pattern, not the person. Offer to look "
                           "together.",
                "why": [
                    "\"Three times this quarter\" is a fact, not a "
                    "complaint.",
                    "Explicitly removing blame lets them engage without "
                    "defending.",
                    "\"Look at the dates together\" makes it a shared "
                    "problem.",
                ],
            },
        },
        {
            "label": "Raising a problem",
            "title": "Where to raise it",
            "visual": {
                "type": "tree",
                "question": "Is this the first or the fourth time?",
                "yes": {
                    "path": "First", "tone": "good", "label": "Direct and "
                                                             "informal",
                    "detail": "A call or a quiet word with the person "
                              "involved. Almost every first occurrence is a "
                              "misunderstanding, and it resolves in five "
                              "minutes without anyone else knowing.",
                },
                "no": {
                    "path": "Fourth", "tone": "neutral",
                    "label": "Involve the managers",
                    "detail": "With the dates written down and no commentary "
                              "about anybody. A repeated pattern is a process "
                              "problem, and process problems need the people "
                              "who own the process.",
                },
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: rewrite one handover",
            "visual": {
                "type": "steps",
                "items": [
                    "Find something you handed over that came back wrong.",
                    "Write the four lines you did not write at the time.",
                    "Notice which of the four would have prevented it.",
                    "Use all four on the next thing you hand over.",
                ],
                "prompt": "Turn my rough note into a handover with exactly "
                          "four labelled lines: WHAT, DONE MEANS, BY WHEN, IF "
                          "STUCK. Use only what I have written. Where I have "
                          "not said something, write [NEEDS ANSWER] rather "
                          "than inventing it.",
                "caption": "The [NEEDS ANSWER] markers are the questions you "
                           "would have been asked anyway.",
            },
        },
        {
            "label": "Do this now",
            "title": "Feedback that changes something",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Name the specific thing, not the general trait.",
                    "Say the effect it had, factually and without heat.",
                    "Say what you would like instead, concretely.",
                    "Do it within two days, or do not do it at all.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Handing over a file with \"please complete\"",
                     "Three days of messages establishing what you meant by "
                     "complete."),
                    ("Assuming done means the same to both of you",
                     "You meant ready to send. They heard numbers filled in. "
                     "Both were reasonable."),
                    ("Asking to \"pick someone's brain\"",
                     "No question and no time attached. It gets agreed to and "
                     "never happens."),
                    ("Raising a repeated problem as a personal one",
                     "The fourth late delivery is a process fault, and naming "
                     "a person ends the conversation."),
                    ("Giving feedback three weeks later",
                     "Nobody remembers the specifics, so it lands as a general "
                     "judgement about them."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Working across sites",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Say the time zone",
                     "sub": "\"3pm Dubai time\" removes an hour and a half of "
                            "ambiguity with an Indian office."},
                    {"icon": "doc", "label": "Write, then call",
                     "sub": "Written first gives everyone the same words. The "
                            "call resolves what the writing could not."},
                    {"icon": "person", "label": "Name one contact",
                     "sub": "\"Ask Priya\" beats \"ask the costing team\", "
                            "which reliably means asking nobody."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The collaboration rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Say what done looks like, when it is due, and who "
                            "to ask when it is not clear.",
                "sub": "Almost every cross-team problem is one of those three "
                       "lines missing.",
                "cols": 3,
                "items": [
                    "Done means what, exactly.",
                    "By when, with a time.",
                    "Ask whom, by name.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 11:00 am",
        "situation": "You need a costing from another team by Wednesday "
                     "afternoon for a tender. The last two came back late and "
                     "in the wrong format.",
        "choices": [
            {
                "text": "Send the file with \"please complete by tomorrow\".",
                "tone": "bad",
                "headline": "The third one goes the same way",
                "consequence": "They start on Wednesday morning because "
                               "\"tomorrow\" had no time on it. They use last "
                               "year's rate card because nobody said "
                               "otherwise. It arrives at five, in their own "
                               "format, and you rework it in the evening.",
                "rule": "The same handover produces the same result, every "
                        "time.",
            },
            {
                "text": "Send the four lines: what, done means, by when, if "
                        "stuck.",
                "tone": "good",
                "headline": "Ninety seconds of writing, and it arrives "
                            "finished",
                "consequence": "\"Costing for the Sharjah tender on the 2026 "
                               "rate card. Done means every line priced, "
                               "exclusions listed, in the client template, "
                               "ready to send. By Wednesday 3pm. If a rate is "
                               "missing, ask Priya rather than estimating.\" "
                               "It arrives at two.",
                "rule": "Four lines is the whole intervention. Nothing else "
                        "is needed.",
            },
            {
                "text": "Do the costing yourself to avoid the hassle.",
                "tone": "ok",
                "headline": "It gets done, and nothing improves",
                "consequence": "You lose an evening and the tender is fine. "
                               "The next one has the same problem, because the "
                               "handover was never fixed — and the other team "
                               "never learns what you actually needed.",
                "rule": "Doing it yourself solves today and guarantees next "
                        "month.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=RQmUJZvrthE",
        "title": "Mastering Task Delegation - A Guide to Effective Teamwork "
                 "(15 Minutes)",
        "channel": "Microlearning Daily",
        "duration": "15:00",
        "heading": "Fifteen minutes on handing work over",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The four-line handover is the working version.",
            "Useful if you delegate regularly and want more depth.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What is missing from \"please complete\"?",
            "remember": "Done means, by when, and who to ask.",
            "answers": [
                {"text": "Politeness", "ok": False,
                 "why": "It is perfectly polite. The problem is that it "
                        "contains none of the information the other person "
                        "needs in order to start."},
                {"text": "What done looks like, the deadline, and who to ask",
                 "ok": True,
                 "why": "Three of the four lines are absent. Each one produces "
                        "a round of messages, which is exactly where the three "
                        "days went."},
                {"text": "The reason the work is needed", "ok": False,
                 "why": "Helpful context and rarely the blocker. People "
                        "usually stall on scope and standard, not on "
                        "motivation."},
                {"text": "An offer to help", "ok": False,
                 "why": "\"If stuck, ask Priya\" covers this better, because "
                        "it names somebody specific rather than offering "
                        "vaguely."},
            ],
        },
        {
            "q": "Why does \"done\" cause so much trouble?",
            "remember": "Both people can be right and still disagree.",
            "answers": [
                {"text": "People are careless about finishing", "ok": False,
                 "why": "Usually not. Both sides are working carefully towards "
                        "different, entirely reasonable definitions of the "
                        "same word."},
                {"text": "It means different things to different people",
                 "ok": True,
                 "why": "\"Ready to send\" and \"numbers filled in\" are both "
                        "legitimate readings of done. Neither person is "
                        "careless, and nobody discovers the gap until the work "
                        "comes back."},
                {"text": "Deadlines are usually too short", "ok": False,
                 "why": "A separate problem. A short deadline with a clear "
                        "definition of done still produces the right thing, "
                        "just faster."},
                {"text": "The work is too complicated to define", "ok": False,
                 "why": "Almost any output can be described in one sentence of "
                        "finished state. \"Ready to send without me editing\" "
                        "works for most things."},
            ],
        },
        {
            "q": "What makes an ask for help work?",
            "remember": "Say what you tried, and how long it will take.",
            "answers": [
                {"text": "Being apologetic about interrupting", "ok": False,
                 "why": "Apology does not help them decide. What they need to "
                        "know is what is being asked and how big it is."},
                {"text": "Naming what you already tried and the time needed",
                 "ok": True,
                 "why": "\"What I tried\" stops them suggesting your first two "
                        "attempts. \"Two minutes\" lets them say yes without "
                        "worrying it becomes an hour."},
                {"text": "Giving full background first", "ok": False,
                 "why": "It makes them work out what is being asked before "
                        "they can decide whether they can help. Question "
                        "first, background if needed."},
                {"text": "Asking whether they are free", "ok": False,
                 "why": "Nobody can answer this. Free for what, and for how "
                        "long? It usually gets a yes followed by nothing."},
            ],
        },
        {
            "q": "Third late delivery. How do you raise it?",
            "remember": "Name the pattern, not the person.",
            "answers": [
                {"text": "Copy both managers on the next chaser", "ok": False,
                 "why": "That is an escalation before a conversation. It ends "
                        "cooperation, and it treats a probable process fault "
                        "as somebody's misconduct."},
                {"text": "State the dates, remove blame, and offer to look "
                         "together", "ok": True,
                 "why": "\"Three times this quarter — I suspect we hand over "
                        "too late rather than anyone dragging their feet.\" "
                        "The facts stand, nobody has to defend themselves, and "
                        "you usually find the real cause."},
                {"text": "Say nothing and build in more buffer", "ok": False,
                 "why": "It hides the problem and costs you time every month. "
                        "The other team also never learns that anything is "
                        "wrong."},
                {"text": "Ask who was responsible each time", "ok": False,
                 "why": "It frames a repeated process failure as individual "
                        "fault. People become careful rather than open, and "
                        "the cause stays hidden."},
            ],
        },
        {
            "q": "When is feedback worth giving?",
            "remember": "Within two days, or not at all.",
            "answers": [
                {"text": "At the annual review, so it is all together",
                 "ok": False,
                 "why": "Nobody can act on something from eight months ago, "
                        "and hearing a list at review is the worst possible "
                        "delivery. It also reads as ambush."},
                {"text": "Within about two days, about one specific thing",
                 "ok": True,
                 "why": "Both people still remember the specifics, so it is a "
                        "conversation about an event rather than a judgement "
                        "about a person. After a week it becomes the second."},
                {"text": "Whenever you feel calm enough", "ok": False,
                 "why": "Being calm matters and waiting a week does not help. "
                        "Wait an hour if you need to, not until the detail has "
                        "faded."},
                {"text": "Only if it is positive", "ok": False,
                 "why": "Then nothing ever improves. Specific, timely and "
                        "unheated feedback about one thing is usually received "
                        "perfectly well."},
            ],
        },
    ],

    "recap": {
        "title": "Collaboration on one screen",
        "points": [
            ("Four lines with every handover",
             "What, done means, by when, and who to ask if stuck."),
            ("Define done explicitly",
             "\"Ready to send without me editing it\" removes the whole "
             "ambiguity."),
            ("Give a time, not a day",
             "\"Wednesday 3pm\" starts work on Tuesday. \"Wednesday\" starts "
             "it on Wednesday."),
            ("Name one person to ask",
             "\"Ask Priya\" beats \"ask the team\", which means asking "
             "nobody."),
            ("Say what you already tried",
             "It is the difference between a two-minute answer and a "
             "ten-minute one."),
            ("Raise patterns, not people",
             "The fourth late delivery is a process fault. Name the dates, not "
             "the person."),
        ],
        "oneliner": "Say what done looks like, when it is due, and who to ask "
                    "when it is not clear.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("doc", "The four-line handover",
             "What, done means, by when, if stuck."),
            ("chat", "The three-line ask for help",
             "Problem, what you tried, specific question, time needed."),
            ("person", "The no-blame problem raise",
             "The dates, blame removed, an offer to look together."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "That completes the Professional Skills track. The master "
                "index lists every module and the recommended learning paths.",
    },

    "glossary": [
        ("Handover", "Passing work to somebody else. Needs four lines, not a "
                     "file and two words."),
        ("Definition of done", "What the finished output looks like, stated "
                               "before anyone starts."),
        ("Escalation", "Involving managers. Appropriate for a repeated "
                       "pattern, not a first occurrence."),
        ("Blocker", "Something stopping progress. Should reach a named person "
                    "within hours, not days."),
        ("Feedback", "One specific thing, its effect, and what you would like "
                     "instead. Within two days."),
        ("Buffer", "Extra time added to absorb delays. Useful, and it hides "
                   "the problem if used instead of fixing it."),
    ],
}
