# -*- coding: utf-8 -*-
"""PS-08 — Presentation Skills. Content only."""

DECK = {
    "module_code": "PS-08",
    "area": "04-professional-skills",
    "filename": "04-08-presentation-skills.pptx",
    "title": "Presentation Skills",
    "subtitle": "Standing up and saying it — including when you are "
                "interrupted on slide three.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "layers",
    "cover_image": "assets/hero-presentation-skills.jpg",

    "why": {
        "title": "Rohit reads his slides out loud",
        "icon": "person",
        "scenario": "Rohit presents the monthly review in Vadodara. He reads "
                    "each slide aloud, in order, without stopping. Halfway "
                    "through, two people are on their phones. He has all the "
                    "right information and nobody is receiving it.",
        "cost": "Forty minutes of the right facts, landing on nobody.",
        "fix": "Say the point, then show the evidence. Never the other way "
               "round.",
    },

    "outcomes": [
        ("chat", "Open with the conclusion instead of the agenda"),
        ("person", "Handle an interruption without losing your thread"),
        ("eye", "Say the point of a slide before showing its detail"),
        ("warn", "Answer a question you do not know the answer to"),
        ("clock", "Finish early, deliberately, and be thanked for it"),
    ],

    "sections": [
        ("Point before evidence", "Why reading fails", "s_point"),
        ("The first ninety seconds", "You get one opening", "s_open"),
        ("Being interrupted", "It is normal, not an attack", "s_interrupt"),
        ("Questions you cannot answer", "Three honest options", "s_dontknow"),
        ("Do this now", "Rehearse one opening", "s_do"),
        ("Choose what you'd do", "A slide-three decision", "scenario"),
        ("Watch this", "A 5-minute outside guide", "video"),
    ],

    "slides": [
        {
            "anchor": "s_point",
            "label": "Point before evidence",
            "title": "Point first, evidence second",
            "lead": "If people do not know what a slide is for, they read it "
                    "instead of listening to you.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Evidence first",
                "bad": [
                    "\"This chart shows dispatches by week for the quarter.\"",
                    "The room reads the chart while you are still talking.",
                    "By the time you reach the point, they have formed their "
                    "own.",
                ],
                "good_tag": "Point first",
                "good": [
                    "\"Volumes held up. The problem is rejects, not "
                    "output.\"",
                    "\"You can see it in weeks six and seven here.\"",
                    "They now look at the chart for the thing you named.",
                ],
                "note": "A room reads faster than you speak. Give them the "
                        "point before they build their own.",
            },
        },
        {
            "label": "Point before evidence",
            "title": "Never read the slide",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "eye", "label": "They read it faster",
                     "sub": "Reading aloud is slower than reading silently. "
                            "You are holding the room back."},
                    {"icon": "chat", "label": "Say what is not on it",
                     "sub": "The slide carries the data. You carry the "
                            "meaning, the caveat and the recommendation."},
                    {"icon": "list", "label": "One point per slide",
                     "sub": "If you need three sentences to say what a slide "
                            "shows, it is three slides."},
                ],
            },
        },
        {
            "anchor": "s_open",
            "label": "The first ninety seconds",
            "title": "You get one opening",
            "visual": {
                "type": "prompt",
                "header": "Copy this opening",
                "text": "\"Three things today. One: volumes held, so capacity "
                        "is not our problem. Two: rejects doubled in weeks six "
                        "and seven and I know why. Three: I need a decision on "
                        "the film supplier by Friday. I will take questions as "
                        "we go.\"",
                "caption": "Under thirty seconds, and the room knows the whole "
                           "shape.",
                "why": [
                    "Naming three things tells people when it will end.",
                    "The decision is stated at the start, not discovered at "
                    "the end.",
                    "\"Questions as we go\" prevents the awkward held hand.",
                ],
            },
        },
        {
            "label": "The first ninety seconds",
            "title": "What not to open with",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "The first thirty seconds are the only ones where "
                            "you have everybody. Do not spend them on "
                            "housekeeping.",
                "sub": "Agendas, apologies and background all belong later, or "
                       "nowhere.",
                "cols": 2,
                "items": [
                    "\"Let me start with a bit of background\"",
                    "\"Apologies, I only got this together this morning\"",
                    "\"I know we are short on time so I will be quick\"",
                    "An agenda slide nobody has ever needed",
                ],
            },
        },
        {
            "anchor": "s_interrupt",
            "label": "Being interrupted",
            "title": "Interruptions are normal",
            "lead": "Being stopped on slide three usually means somebody is "
                    "engaged. It is not an attack, and it is not a failure.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "ANSWER IT — if it is quick, take it now and move on",
                    "DEFER IT — \"That is slide seven, can I come to it "
                    "there?\"",
                    "PARK IT — \"Good question, let me take that offline\"",
                    "NEVER SAY — \"I was just about to explain that\"",
                ],
            },
        },
        {
            "label": "Being interrupted",
            "title": "Finding your place again",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Finish the answer", "Do not trail off looking at the "
                                          "screen."),
                    ("Name where you are", "\"So — back to rejects.\""),
                    ("Restate the point", "One sentence. It helps you and the "
                                          "room."),
                    ("Carry on", "Nobody remembers the pause. They remember "
                                 "the fluster."),
                ],
            },
        },
        {
            "anchor": "s_dontknow",
            "label": "Questions you cannot answer",
            "title": "Three honest options",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "What people do", "tone": "bad",
                    "title": "Guessing under pressure",
                    "items": [
                        "An invented figure, stated confidently",
                        "A vague answer nobody can act on",
                        "\"I think it was around...\"",
                        "It gets quoted back to you in six weeks",
                    ],
                },
                "right": {
                    "tag": "What works", "tone": "good",
                    "title": "Three honest answers",
                    "items": [
                        "\"I do not know — I will find out by Thursday.\"",
                        "\"I have a rough figure but I would not quote it.\"",
                        "\"That is outside what I looked at. Ops would know.\"",
                        "Nobody has ever lost credibility this way",
                    ],
                },
            },
        },
        {
            "label": "Questions you cannot answer",
            "title": "The commitment matters",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "\"I do not have that to hand and I would rather not "
                        "guess at it. I will check and come back to you by "
                        "Thursday.\"  Then write it down, in the room, where "
                        "they can see you writing it.",
                "caption": "Writing it down in front of them is the half "
                           "people forget.",
                "why": [
                    "Saying you would rather not guess is respected, not "
                    "penalised.",
                    "A date turns a non-answer into a commitment.",
                    "Visibly writing it means they stop worrying you will "
                    "forget.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: rehearse one opening",
            "visual": {
                "type": "steps",
                "items": [
                    "Take the next presentation you owe anybody.",
                    "Write your opening as three numbered things.",
                    "Say it out loud, standing up, timed. Aim under thirty "
                    "seconds.",
                    "Say it again. The second attempt is always the one you "
                    "use.",
                ],
                "prompt": "Turn my three main points into a spoken opening of "
                          "under 70 words. Number them out loud. State the "
                          "decision I need at the end. Write it the way "
                          "somebody would actually say it, not the way it "
                          "would be written.",
                "caption": "Read it aloud. If you stumble, the sentence is too "
                           "long.",
            },
        },
        {
            "label": "Do this now",
            "title": "Finishing early is a gift",
            "visual": {
                "type": "tree",
                "question": "Have I made my three points and got my decision?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Stop there",
                    "detail": "\"That is everything from me — we have ten "
                              "minutes back.\" Nobody has ever resented this, "
                              "and it is remembered far more warmly than a "
                              "thorough overrun.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Say what is "
                                                             "left",
                    "detail": "\"We are short on time — the one thing I still "
                              "need is the supplier decision.\" Protect the "
                              "decision, drop the detail.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Say the point of a slide before you show its detail.",
                    "Open with three numbered things and the decision you "
                    "need.",
                    "Never say \"I was just about to explain that\".",
                    "Write down anything you promised to come back on.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Reading the slides aloud",
                     "The room reads faster than you speak. You are holding "
                     "them back and they know it."),
                    ("Apologising in the opening",
                     "It tells the room to expect something poor, before they "
                     "have judged for themselves."),
                    ("Guessing a number under pressure",
                     "It gets written down and quoted back six weeks later, "
                     "with your name on it."),
                    ("Treating an interruption as an attack",
                     "It is usually engagement. The fluster costs more than "
                     "the question did."),
                    ("Running over to cover every slide",
                     "The decision you needed is on the last slide nobody "
                     "reached."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Nerves are not the problem",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "person", "label": "Nobody can see them",
                     "sub": "Almost everything you feel is invisible from four "
                            "metres away."},
                    {"icon": "clock", "label": "The first minute is worst",
                     "sub": "Which is exactly why the opening is the part "
                            "worth rehearsing out loud."},
                    {"icon": "check", "label": "Preparation beats confidence",
                     "sub": "A rehearsed opening and three known points do "
                            "more than any amount of feeling calm."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The presentation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Say the point, show the evidence, and stop when "
                            "you have your decision.",
                "sub": "Three habits that separate a presentation people act "
                       "on from one they sit through.",
                "cols": 3,
                "items": [
                    "Point before evidence.",
                    "Three things, numbered, up front.",
                    "Stop early, on purpose.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monthly review, slide three",
        "situation": "You are three slides into a twelve-slide review. A "
                     "director interrupts to ask about a figure that is not on "
                     "screen until slide nine.",
        "choices": [
            {
                "text": "Say \"I was just about to come to that\" and carry "
                        "on.",
                "tone": "bad",
                "headline": "It reads as a brush-off, whether you meant it or "
                            "not",
                "consequence": "The director now waits six slides for an "
                               "answer, half-listening. When you reach slide "
                               "nine they have lost interest, and the question "
                               "gets asked again afterwards in a less friendly "
                               "form.",
                "rule": "Never make somebody wait six slides for an answer "
                        "you have.",
            },
            {
                "text": "Answer it now in one sentence, then say where you "
                        "are.",
                "tone": "good",
                "headline": "Ten seconds, and you keep the room",
                "consequence": "\"It is 2.1 per cent, up from 1.4 — I will "
                               "show the weekly split on slide nine. So, back "
                               "to volumes.\" The director has what they "
                               "needed, and you have named your place again "
                               "for everyone else.",
                "rule": "Answer, then name where you are. Both halves matter.",
            },
            {
                "text": "Jump forward to slide nine and present it now.",
                "tone": "ok",
                "headline": "Answers it, and loses your structure",
                "consequence": "You cover the reject detail six slides early, "
                               "then have to navigate back and re-establish "
                               "the thread. It works, and it usually costs you "
                               "five minutes and some of the room's sense of "
                               "where things are going.",
                "rule": "Jump only if the question is the whole point of the "
                        "meeting.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=PnWND7JpRDQ",
        "title": "How to Prepare a Presentation with the Correct Structure",
        "channel": "Carl Kwan",
        "duration": "4:48",
        "heading": "Five minutes on structure",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The opening formula above is the core of it.",
            "Useful if you want the structure explained a second way.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What comes first on a slide?",
            "remember": "The point, then the evidence.",
            "answers": [
                {"text": "A description of what the chart shows", "ok": False,
                 "why": "The room can already see what it shows, and faster "
                        "than you can say it. Describing it wastes the moment "
                        "they were listening."},
                {"text": "The point the slide is making", "ok": True,
                 "why": "\"Volumes held; the problem is rejects\" tells them "
                        "what to look for. They then read the chart for your "
                        "point rather than constructing their own."},
                {"text": "The methodology behind the figures", "ok": False,
                 "why": "Important if challenged, and not first. Method "
                        "belongs in an appendix or in your answer to a "
                        "question."},
                {"text": "An apology for the formatting", "ok": False,
                 "why": "It draws attention to something most people had not "
                        "noticed, and lowers their expectation of everything "
                        "that follows."},
            ],
        },
        {
            "q": "Interrupted on slide three. Best move?",
            "remember": "Answer briefly, then name where you are.",
            "answers": [
                {"text": "\"I was just about to explain that\"", "ok": False,
                 "why": "It reads as a brush-off however warmly you say it, "
                        "and it makes somebody wait for information you "
                        "already have."},
                {"text": "Answer in one sentence, then say where you are",
                 "ok": True,
                 "why": "The questioner gets what they needed and everyone "
                        "else gets a signpost back into your thread. Both "
                        "halves matter — without the second you lose the "
                        "room."},
                {"text": "Skip forward to the slide that covers it", "ok": False,
                 "why": "Sometimes right if it is the central question. "
                        "Usually it costs your structure and five minutes of "
                        "navigating."},
                {"text": "Ask them to hold questions to the end", "ok": False,
                 "why": "It reduces engagement, and the questions get asked "
                        "anyway, less helpfully, once you have finished."},
            ],
        },
        {
            "q": "You do not know the answer. Say what?",
            "remember": "Say so, and give a date.",
            "answers": [
                {"text": "An approximate figure, to keep momentum", "ok": False,
                 "why": "It gets written down and quoted back with your name "
                        "on it. Momentum is not worth a number you cannot "
                        "stand behind."},
                {"text": "\"I would rather not guess — I will confirm by "
                         "Thursday\"", "ok": True,
                 "why": "Nobody loses credibility for this. Add the date, and "
                        "write it down where they can see you writing it, so "
                        "they stop worrying it will be forgotten."},
                {"text": "\"That is not really relevant here\"", "ok": False,
                 "why": "It dismisses a question somebody thought was worth "
                        "asking, and it usually reads as defensiveness rather "
                        "than focus."},
                {"text": "Move on quickly and hope it is not repeated",
                 "ok": False,
                 "why": "It will be repeated, usually to somebody else, and "
                        "the second version will include the fact that you "
                        "avoided it."},
            ],
        },
        {
            "q": "What should the opening contain?",
            "remember": "Three numbered things and the decision you need.",
            "answers": [
                {"text": "An agenda and some background", "ok": False,
                 "why": "The only thirty seconds where you have everybody, "
                        "spent on housekeeping. Background belongs later or "
                        "nowhere at all."},
                {"text": "Three numbered points and the decision required",
                 "ok": True,
                 "why": "Numbering tells people when it ends, and stating the "
                        "decision at the start means the room is thinking "
                        "about it throughout rather than discovering it at "
                        "the finish."},
                {"text": "A summary of last month", "ok": False,
                 "why": "They were there. Recapping the known spends attention "
                        "you need for the new."},
                {"text": "An apology for the short notice", "ok": False,
                 "why": "It lowers expectations before anyone has judged the "
                        "content, and almost nobody had noticed the notice was "
                        "short."},
            ],
        },
        {
            "q": "You have five slides left and no time.",
            "remember": "Protect the decision, drop the detail.",
            "answers": [
                {"text": "Speed up and cover all five", "ok": False,
                 "why": "Five rushed slides communicate less than one clear "
                        "one, and the decision you needed is usually on the "
                        "last of them."},
                {"text": "Say what is left and ask for the decision", "ok": True,
                 "why": "\"We are short on time — the one thing I still need "
                        "is the supplier decision.\" You get what you came "
                        "for, and the detail can go round afterwards."},
                {"text": "Ask for another meeting", "ok": False,
                 "why": "Costs six people another hour for something you could "
                        "resolve in ninety seconds by naming the decision "
                        "now."},
                {"text": "Send the remaining slides afterwards without "
                         "comment", "ok": False,
                 "why": "Fine for the detail, and it leaves the decision "
                        "unmade. Ask for it while everybody is still in the "
                        "room."},
            ],
        },
    ],

    "recap": {
        "title": "Presenting on one screen",
        "points": [
            ("Point before evidence",
             "Tell them what a slide means before they build their own view "
             "of it."),
            ("Never read the slide",
             "They read faster than you speak. Say what is not written on it."),
            ("Three numbered things",
             "Plus the decision you need, in the first thirty seconds."),
            ("Answer, then signpost",
             "Deal with the interruption, then name where you are again."),
            ("Never guess a number",
             "\"I would rather not guess — I will confirm by Thursday.\""),
            ("Stop when you have the decision",
             "Finishing early is remembered far more warmly than finishing "
             "everything."),
        ],
        "oneliner": "Say the point, show the evidence, and stop when you have "
                    "your decision.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The thirty-second opening",
             "Three numbered things and the decision you need."),
            ("person", "The interruption move",
             "One-sentence answer, then name where you are."),
            ("check", "The honest non-answer",
             "\"I would rather not guess. Thursday.\" Then write it down."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-09, Teamwork & Collaboration. Handing work "
                "over so it arrives finished, and asking for help without "
                "friction.",
    },

    "glossary": [
        ("Point-first", "Stating what a slide means before showing its detail."),
        ("Signposting", "Telling the room where you are, especially after an "
                        "interruption."),
        ("Parking", "Agreeing to take a question outside the meeting, with a "
                    "date attached."),
        ("Appendix", "Slides kept after the end for questions you might be "
                     "asked."),
        ("Opening", "The first thirty seconds. The only moment you have "
                    "everybody's attention."),
        ("Overrun", "Going past the finish time. It costs the decision you "
                    "came for."),
    ],
}
