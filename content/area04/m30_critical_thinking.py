# -*- coding: utf-8 -*-
"""PS-07 — Critical Thinking. Content only."""

DECK = {
    "module_code": "PS-07",
    "area": "04-professional-skills",
    "filename": "04-07-critical-thinking.pptx",
    "title": "Critical Thinking",
    "subtitle": "Telling evidence from assertion — including in your own "
                "reasoning, which is the harder half.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "network",

    "why": {
        "title": "Nisha's number is repeated for a year",
        "icon": "eye",
        "scenario": "Nisha builds the monthly pack in Hyderabad. Someone once "
                    "said returns run at about eight per cent. It went into a "
                    "slide. It has been repeated in every pack since. Nobody "
                    "has ever calculated it.",
        "cost": "A year of decisions resting on a number nobody checked.",
        "fix": "Three questions, asked out loud, before a claim gets "
               "repeated.",
    },

    "outcomes": [
        ("eye", "Tell a fact from an assertion in somebody else's argument"),
        ("check", "Ask where a number came from without sounding "
                  "obstructive"),
        ("warn", "Catch the two biases that affect your own work most"),
        ("list", "Test whether a comparison is actually comparing like with "
                 "like"),
        ("person", "Disagree with a conclusion without attacking the person"),
    ],

    "sections": [
        ("Fact or assertion", "The three questions", "s_fact"),
        ("Where numbers come from", "Asking without friction", "s_numbers"),
        ("Your own two biases", "The ones that matter at work", "s_bias"),
        ("Bad comparisons", "Like with like", "s_compare"),
        ("Do this now", "Test a real claim", "s_do"),
        ("Choose what you'd do", "A review-meeting decision", "scenario"),
        ("Watch this", "A 6-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_fact",
            "label": "Fact or assertion",
            "title": "Three questions, every claim",
            "lead": "Most workplace claims are true, unchecked, or true once "
                    "and never re-examined. These three separate them.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "WHERE DID THIS COME FROM? — a system, a document, or "
                    "somebody's memory",
                    "WHEN WAS IT TRUE? — many claims were accurate two years "
                    "ago",
                    "WHAT WOULD CHANGE MY MIND? — if nothing would, it is not "
                    "a conclusion",
                ],
            },
        },
        {
            "label": "Fact or assertion",
            "title": "How a number becomes a fact",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Somebody estimates", "\"Returns are about eight per "
                                           "cent, I think.\""),
                    ("It gets written down", "The hedge disappears in the "
                                             "slide."),
                    ("It gets repeated", "Now three documents say eight per "
                                         "cent."),
                    ("It becomes the figure", "And decisions are made on it."),
                ],
            },
        },
        {
            "anchor": "s_numbers",
            "label": "Where numbers come from",
            "title": "Asking without friction",
            "visual": {
                "type": "prompt",
                "header": "Copy these three questions",
                "text": "\"Out of interest, where does the eight per cent come "
                        "from — is that from the system?\"  /  \"Do we know "
                        "roughly when that was last calculated?\"  /  \"Is "
                        "that all products, or the main line?\"",
                "caption": "Curious, not challenging. Almost nobody takes "
                           "offence at these.",
                "why": [
                    "\"Out of interest\" removes any accusation from the "
                    "question.",
                    "Asking when it was calculated is less confrontational "
                    "than asking if it is right.",
                    "The scope question often reveals the real problem.",
                ],
            },
        },
        {
            "label": "Where numbers come from",
            "title": "Three kinds of number",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Traceable", "tone": "good",
                    "title": "You can open the source",
                    "items": [
                        "Comes from a system report you can rerun",
                        "Has a date and a defined scope",
                        "Somebody can tell you how it is calculated",
                        "Safe to put in front of a customer",
                    ],
                },
                "right": {
                    "tag": "Folklore", "tone": "bad",
                    "title": "Nobody can point at it",
                    "items": [
                        "\"We have always said about eight per cent\"",
                        "No date, no scope, no method",
                        "Appears in three documents, all copying each other",
                        "Repeated confidently by everyone",
                    ],
                },
            },
        },
        {
            "anchor": "s_bias",
            "label": "Your own two biases",
            "title": "The two that matter at work",
            "gloss": ["Confirmation bias"],
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "eye", "label": "Confirmation",
                     "sub": "You notice the data that fits your view and "
                            "genuinely do not register the rest."},
                    {"icon": "person", "label": "Recency",
                     "sub": "Last week's complaint feels like a trend. Six "
                            "quiet months do not feel like anything."},
                    {"icon": "check", "label": "The counter",
                     "sub": "Ask what evidence would change your mind, before "
                            "you go looking at any evidence."},
                ],
            },
        },
        {
            "label": "Your own two biases",
            "title": "Deciding in advance",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Looking for support",
                "bad": [
                    "You think the new supplier is causing the rejects.",
                    "You pull the reject data and find three from their "
                    "batches.",
                    "You stop there, because you found what you expected.",
                ],
                "good_tag": "Deciding the test first",
                "good": [
                    "\"If their batches reject at the same rate as the old "
                    "supplier, I am wrong.\"",
                    "You pull both rates. Theirs is 2.1, the old one 1.9.",
                    "That is not the cause. You keep looking, a week earlier "
                    "than you would have.",
                ],
                "note": "Deciding what would change your mind before you look "
                        "is the only reliable protection against finding what "
                        "you expected.",
            },
        },
        {
            "anchor": "s_compare",
            "label": "Bad comparisons",
            "title": "Like with like",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Comparing a full month with a part month",
                     "November against three weeks of December. The drop is "
                     "the calendar, not the business."),
                    ("Comparing before and after a definition change",
                     "\"Rejects\" started including rework in April. The rise "
                     "is a counting change."),
                    ("Comparing a total with a rate",
                     "More rejects with far more volume can be a lower "
                     "rejection rate."),
                    ("Comparing across a changed scope",
                     "Two sites last year, four this year. Everything looks "
                     "like growth."),
                ],
            },
        },
        {
            "label": "Bad comparisons",
            "title": "The four checks",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "SAME PERIOD LENGTH — full month against full month",
                    "SAME DEFINITION — has anything changed about what counts?",
                    "SAME SCOPE — same sites, same products, same customers",
                    "RATE OR TOTAL — decide which one the question needs",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: test one claim",
            "visual": {
                "type": "steps",
                "items": [
                    "Find a number that appears in your regular reporting.",
                    "Ask where it came from and when it was last calculated.",
                    "Check whether the comparison periods are actually "
                    "comparable.",
                    "If nobody can answer, put a date and a source on it "
                    "yourself.",
                ],
                "prompt": "Here is a claim and the reasoning behind it. List "
                          "the assumptions it depends on, marking each as "
                          "STATED or UNSTATED. Then list what evidence would "
                          "show the claim is wrong. Do not tell me whether you "
                          "think it is true.",
                "caption": "\"Do not tell me whether you think it is true\" is "
                           "what makes this useful.",
            },
        },
        {
            "label": "Do this now",
            "title": "Disagreeing well",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "\"I might be missing something — can I check one "
                        "thing? The comparison is November against December, "
                        "but December only has three working weeks in it. "
                        "Does that account for most of the drop, or is there "
                        "something else?\"",
                "caption": "Question the reasoning, never the person.",
                "why": [
                    "\"I might be missing something\" costs nothing and lowers "
                    "the temperature.",
                    "It names one specific thing rather than doubting the "
                    "whole analysis.",
                    "It ends with a genuine question, so there is an easy way "
                    "out.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Ask where a number came from before you repeat it.",
                    "Put a date and a source next to any figure you publish.",
                    "Decide what would change your mind before you look.",
                    "Check the periods match before believing any comparison.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Repeating a number because it is in a previous deck",
                     "Three documents agreeing usually means one source copied "
                     "twice."),
                    ("Treating a hedge as a fact",
                     "\"About eight per cent, I think\" becomes \"8%\" in the "
                     "next slide."),
                    ("Looking for evidence after forming the view",
                     "You will find it. That is what confirmation bias "
                     "reliably does."),
                    ("Comparing periods of different lengths",
                     "The most common bad comparison in any monthly pack "
                     "anywhere."),
                    ("Challenging the person instead of the reasoning",
                     "The argument stops being about the number within one "
                     "sentence."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "When to stop questioning",
            "visual": {
                "type": "tree",
                "question": "Would a better number change what we do?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Keep asking",
                    "detail": "If the decision turns on it, the number "
                              "deserves a source and a date. Spend the hour — "
                              "it is much cheaper than the wrong decision.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Let it go",
                    "detail": "If we would do the same thing whether it is six "
                              "or ten per cent, precision is not worth a "
                              "meeting. Note it as approximate and move on.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The critical thinking rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Ask where it came from, when it was true, and "
                            "what would change your mind.",
                "sub": "The third question is the one people skip, and the "
                       "only one that works on your own reasoning.",
                "cols": 3,
                "items": [
                    "Where did it come from?",
                    "When was it true?",
                    "What would change my mind?",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Review meeting, Thursday",
        "situation": "A slide shows returns dropping from 8 per cent to 5 per "
                     "cent. Everyone is pleased. You notice the comparison is "
                     "November against December.",
        "choices": [
            {
                "text": "Say nothing — everyone is happy and you might be "
                        "wrong.",
                "tone": "bad",
                "headline": "The number goes into the quarterly pack",
                "consequence": "It is repeated upwards, and a decision to "
                               "reduce inspection follows in February. In "
                               "March the rate is back at eight per cent, "
                               "because it never actually fell. December "
                               "simply had three working weeks in it.",
                "rule": "An unchallenged number travels upwards and gets "
                        "harder to correct.",
            },
            {
                "text": "Ask whether the shorter December accounts for the "
                        "drop.",
                "tone": "good",
                "headline": "One question, and the pack gets fixed",
                "consequence": "\"I might be missing something — December only "
                               "has three working weeks. Does that account for "
                               "most of it?\" The analyst checks, agrees, and "
                               "reissues with a like-for-like comparison. "
                               "Nobody is embarrassed.",
                "rule": "Question the comparison, not the person, and do it "
                        "in the room.",
            },
            {
                "text": "Email the analyst afterwards so nobody is put on the "
                        "spot.",
                "tone": "ok",
                "headline": "Kind, and the room has already moved on",
                "consequence": "Everyone left the meeting believing returns "
                               "fell. The correction reaches one person, and "
                               "the version in six people's heads is never "
                               "updated. Sometimes right for a sensitive "
                               "point; usually too late for a number.",
                "rule": "Correct a number in the room. Correct a person "
                        "privately.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=BtqOeXsB36U",
        "title": "Improve your critical thinking skills in just 6 minutes | "
                 "Alex Edmans for Big Think+",
        "channel": "Big Think",
        "duration": "6:12",
        "heading": "Six minutes on checking claims",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The three questions above are the working version.",
            "Useful for why confirmation bias is so hard to notice.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which question do people skip?",
            "remember": "What would change my mind?",
            "answers": [
                {"text": "Where did this come from?", "ok": False,
                 "why": "People do ask this, at least sometimes. It is also "
                        "the easiest of the three, because it is about "
                        "somebody else's work."},
                {"text": "What would change my mind?", "ok": True,
                 "why": "It is the only one that works on your own reasoning, "
                        "which is why it gets skipped. If no evidence would "
                        "change your view, you are defending a position rather "
                        "than holding a conclusion."},
                {"text": "When was this true?", "ok": False,
                 "why": "Underused and still asked more often than the third. "
                        "It is a comfortable question because it blames time "
                        "rather than anyone's judgement."},
                {"text": "Who said it?", "ok": False,
                 "why": "Frequently asked and the least useful of the four. "
                        "Who said something tells you little about whether it "
                        "is true."},
            ],
        },
        {
            "q": "November against December. Problem?",
            "remember": "Different numbers of working days.",
            "answers": [
                {"text": "No — both are single months", "ok": False,
                 "why": "Calendar months are not equal working periods. "
                        "December often has three usable weeks against "
                        "November's four and a half, which moves every total."},
                {"text": "Yes — the working days differ substantially",
                 "ok": True,
                 "why": "A drop caused by fewer working days is not an "
                        "improvement. Compare like periods, or use a rate per "
                        "working day rather than a monthly total."},
                {"text": "Only if the business is seasonal", "ok": False,
                 "why": "Seasonality is an additional problem. The working-day "
                        "difference applies even in a business with no "
                        "seasonal pattern at all."},
                {"text": "Only for financial figures", "ok": False,
                 "why": "It affects any volume-driven measure: rejects, "
                        "dispatches, complaints, returns. Anything counted per "
                        "period."},
            ],
        },
        {
            "q": "How does a guess become a fact?",
            "remember": "The hedge gets dropped in the retelling.",
            "answers": [
                {"text": "Somebody deliberately misrepresents it", "ok": False,
                 "why": "Almost never deliberate. The hedge simply does not "
                        "survive being put on a slide, because slides have no "
                        "room for \"about, I think\"."},
                {"text": "The \"about, I think\" is dropped when written down",
                 "ok": True,
                 "why": "\"About eight per cent, I think\" becomes \"8%\" in a "
                        "table. Two documents later it has a decimal place, "
                        "and nobody remembers it began as a guess."},
                {"text": "It gets recalculated incorrectly", "ok": False,
                 "why": "Usually there was no calculation at any point. That "
                        "is precisely the problem — there is nothing to "
                        "recalculate."},
                {"text": "Managers demand certainty", "ok": False,
                 "why": "It contributes, and the mechanism is simpler. "
                        "Hedges are dropped by the format, not by anyone's "
                        "instruction."},
            ],
        },
        {
            "q": "How do you disagree well?",
            "remember": "Question the reasoning, not the person.",
            "answers": [
                {"text": "State plainly that the analysis is wrong", "ok": False,
                 "why": "It puts the analyst in a position where agreeing "
                        "means losing face. The conversation stops being about "
                        "the number almost immediately."},
                {"text": "Name one specific thing and ask a genuine question",
                 "ok": True,
                 "why": "\"I might be missing something — does the shorter "
                        "December explain most of it?\" is easy to answer "
                        "either way, and keeps everybody working on the "
                        "problem."},
                {"text": "Raise it privately afterwards", "ok": False,
                 "why": "Right for anything about a person, and usually too "
                        "late for a number. The room has already absorbed the "
                        "wrong figure."},
                {"text": "Ask the analyst to redo the whole thing", "ok": False,
                 "why": "Disproportionate to one comparison problem, and it "
                        "wastes work that was probably sound apart from a "
                        "single choice."},
            ],
        },
        {
            "q": "When is precision not worth chasing?",
            "remember": "When the decision would be the same either way.",
            "answers": [
                {"text": "When the number is small", "ok": False,
                 "why": "Small numbers can drive large decisions. Size is not "
                        "the test."},
                {"text": "When we would act the same whether it is six or "
                         "ten per cent", "ok": True,
                 "why": "If the decision does not change, precision buys "
                        "nothing and costs a meeting. Note it as approximate "
                        "and get on with the work."},
                {"text": "When nobody has time to check", "ok": False,
                 "why": "Lack of time is a constraint, not a reason. If the "
                        "decision turns on it, the hour is far cheaper than "
                        "being wrong."},
                {"text": "When it comes from a senior person", "ok": False,
                 "why": "Seniority does not create evidence. Senior estimates "
                        "become folklore faster than anyone else's, precisely "
                        "because they are less often questioned."},
            ],
        },
    ],

    "recap": {
        "title": "Critical thinking on one screen",
        "points": [
            ("Three questions, every claim",
             "Where from, when true, and what would change my mind."),
            ("Hedges vanish in writing",
             "\"About eight, I think\" becomes 8% two documents later."),
            ("Decide the test before you look",
             "It is the only reliable protection against finding what you "
             "expected."),
            ("Check like with like",
             "Same period length, same definition, same scope, rate or "
             "total."),
            ("Question reasoning, not people",
             "\"I might be missing something\" costs nothing and keeps "
             "everyone working."),
            ("Precision has a price",
             "If the decision would not change, note it as approximate and "
             "move on."),
        ],
        "oneliner": "Where did it come from, when was it true, and what would "
                    "change my mind?",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("eye", "The three claim questions",
             "Source, date, and what would change your mind."),
            ("chat", "The low-friction challenge",
             "\"I might be missing something — can I check one thing?\""),
            ("list", "The four comparison checks",
             "Period, definition, scope, rate or total."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-08, Presentation Skills. Standing up and "
                "saying it, including when you are interrupted on slide "
                "three.",
    },

    "glossary": [
        ("Assertion", "A claim stated without evidence. Often true, and not "
                      "yet demonstrated."),
        ("Confirmation bias", "Noticing evidence that fits your view and not "
                              "registering the rest."),
        ("Recency bias", "Treating the most recent event as a trend, and quiet "
                         "periods as nothing."),
        ("Like-for-like", "A comparison where period, definition and scope are "
                          "all the same."),
        ("Folklore", "A number everybody repeats that nobody can trace to a "
                     "source."),
        ("Falsification", "Deciding in advance what evidence would show you "
                          "are wrong."),
    ],
}
