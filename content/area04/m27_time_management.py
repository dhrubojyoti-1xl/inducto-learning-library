# -*- coding: utf-8 -*-
"""PS-04 — Time Management. Content only."""

DECK = {
    "module_code": "PS-04",
    "area": "04-professional-skills",
    "filename": "04-04-time-management.pptx",
    "title": "Time Management",
    "subtitle": "Protecting the two hours a day where your real work actually "
                "gets done.",
    "duration_min": 16,
    "audience": "New joiners + staff",
    "motif": "layers",
    "cover_image": "assets/hero-time-management.jpg",

    "why": {
        "title": "Arjun is busy from nine to seven",
        "icon": "clock",
        "scenario": "Arjun coordinates dispatch in Surat. He arrives at nine "
                    "and leaves at seven. He is genuinely busy the whole time. "
                    "The two things his manager actually asked for have not "
                    "moved in a fortnight.",
        "cost": "Ten hours a day, and the important work untouched.",
        "fix": "Two protected hours, and a rule for everything that "
               "interrupts.",
    },

    "outcomes": [
        ("clock", "Protect two hours a day for work that needs concentration"),
        ("ban", "Say no to a request without damaging the relationship"),
        ("list", "Handle an interruption in under thirty seconds"),
        ("eye", "Tell the difference between busy and productive, honestly"),
        ("check", "Finish the day knowing what actually moved"),
    ],

    "sections": [
        ("Busy is not productive", "Ten hours, nothing moved", "s_busy"),
        ("The protected block", "Two hours, defended", "s_block"),
        ("Handling interruptions", "Thirty seconds each", "s_interrupt"),
        ("Saying no", "Without damaging anything", "s_no"),
        ("Do this now", "Book tomorrow's block", "s_do"),
        ("Choose what you'd do", "A Tuesday morning decision", "scenario"),
        ("Watch this", "A 3-minute outside summary", "video"),
    ],

    "slides": [
        {
            "anchor": "s_busy",
            "label": "Busy is not productive",
            "title": "Ten hours, nothing moved",
            "lead": "Reactive work fills any space you give it. It also feels "
                    "productive, which is why it wins.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Reactive work", "tone": "bad",
                    "title": "Fills the day",
                    "items": [
                        "Answering as messages arrive",
                        "Attending anything you were invited to",
                        "Solving problems people bring to your desk",
                        "Feels productive, and leaves no trace",
                    ],
                },
                "right": {
                    "tag": "Deliberate work", "tone": "good",
                    "title": "Has to be defended",
                    "items": [
                        "The analysis your manager asked for",
                        "The process that keeps breaking",
                        "The proposal that would win the account",
                        "Never urgent, and the only thing remembered",
                    ],
                },
            },
        },
        {
            "label": "Busy is not productive",
            "title": "The honest end-of-day test",
            "visual": {
                "type": "flow",
                "steps": [
                    ("What did I finish?", "Not touched, not progressed. "
                                           "Finished."),
                    ("Was it on my list this morning?", "Or did it arrive and "
                                                        "take over?"),
                    ("Would my manager count it?", "Against what they "
                                                   "actually asked for."),
                    ("If none — that was a reactive day", "Two of those a "
                                                          "week is normal. "
                                                          "Five is a "
                                                          "problem."),
                ],
            },
        },
        {
            "anchor": "s_block",
            "label": "The protected block",
            "title": "Two hours, defended",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "SAME TIME DAILY — habit beats willpower, every time",
                    "IN THE CALENDAR — as a real booking, not an intention",
                    "NOTIFICATIONS OFF — email, chat and phone, all of them",
                    "ONE TASK ONLY — decided the evening before, not at the "
                    "start",
                ],
            },
        },
        {
            "label": "The protected block",
            "title": "Two hours is enough",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Not the whole day",
                     "sub": "Nobody in an operational job protects six hours. "
                            "Two is achievable and it changes the week."},
                    {"icon": "person", "label": "Tell people once",
                     "sub": "\"I am heads-down until eleven, catch me after.\" "
                            "Most people simply adjust."},
                    {"icon": "check", "label": "Decide the night before",
                     "sub": "Choosing what to work on inside the block wastes "
                            "twenty minutes of it."},
                ],
            },
        },
        {
            "anchor": "s_interrupt",
            "label": "Handling interruptions",
            "title": "Thirty seconds each",
            "lead": "The cost of an interruption is not the two minutes. It is "
                    "the fifteen it takes to get back to where you were.",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "\"I am in the middle of something until eleven — is "
                        "it a two-minute thing or a twenty-minute thing?\"  "
                        "If two minutes: deal with it now.  If twenty: \"Let "
                        "us do it at eleven, I will come to you.\"",
                "caption": "Works in person, on chat, and on the phone.",
                "why": [
                    "It does not refuse, so nobody feels turned away.",
                    "It makes them size the request, which they rarely have.",
                    "You commit to a time, so it does not become a "
                    "brush-off.",
                ],
            },
        },
        {
            "label": "Handling interruptions",
            "title": "The interruption ledger",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Every interruption taken",
                "bad": [
                    "Eleven interruptions between nine and one.",
                    "Each one costs two minutes plus fifteen to refocus.",
                    "That is more than three hours, and it does not feel like "
                    "it.",
                ],
                "good_tag": "Batched to eleven",
                "good": [
                    "Two dealt with instantly, nine held to eleven o'clock.",
                    "Those nine take forty minutes together, once.",
                    "The morning block survives, and nobody waited long.",
                ],
                "note": "Batching is not avoiding people. It is answering nine "
                        "of them properly instead of eleven of them badly.",
            },
        },
        {
            "anchor": "s_no",
            "label": "Saying no",
            "title": "Saying no without damage",
            "visual": {
                "type": "prompt",
                "header": "Copy these three",
                "text": "\"I can do that, but it would push the dispatch "
                        "report to Thursday — is that the right trade?\"  /  "
                        "\"Not this week. I could pick it up Monday if that "
                        "works.\"  /  \"That one sits with Ops — worth asking "
                        "them, they will do it faster than me.\"",
                "caption": "Trade, defer, redirect. Almost nothing needs a "
                           "flat no.",
                "why": [
                    "The trade version makes the cost visible to them.",
                    "The defer version says yes, just later.",
                    "The redirect version helps them and costs you nothing.",
                ],
            },
        },
        {
            "label": "Saying no",
            "title": "Make the trade visible",
            "visual": {
                "type": "tree",
                "question": "Is this coming from my manager?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Offer the trade",
                    "detail": "\"Happy to — which of these two should slip?\" "
                              "Managers usually do not know what is on your "
                              "plate, and almost always pick one when asked.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Defer or "
                                                             "redirect",
                    "detail": "A colleague's request rarely needs your "
                              "immediate week. \"Monday\" or \"Ops will be "
                              "faster\" resolves most of them without any "
                              "friction.",
                },
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: book tomorrow",
            "visual": {
                "type": "steps",
                "items": [
                    "Open your calendar and find two hours tomorrow morning.",
                    "Book them as a real appointment with a name on it.",
                    "Write down now which single task you will do in them.",
                    "Turn notifications off before you start, not after.",
                ],
                "prompt": "I have these tasks and about six working hours "
                          "tomorrow after meetings. Tell me the single task "
                          "worth protecting two hours for, and which of the "
                          "rest can be batched into one afternoon block. "
                          "Assume my estimates are 50 per cent optimistic.",
                "caption": "Deciding tonight is what makes the block work.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Same two hours every day, booked in the calendar.",
                    "Decide the task the evening before, never at the start.",
                    "Batch interruptions to one point in the day.",
                    "End the day by naming one thing you actually finished.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Leaving the important work until you feel free",
                     "You never feel free. Reactive work expands to fill "
                     "whatever you leave open."),
                    ("Protecting time but not notifications",
                     "One chat notification costs fifteen minutes of "
                     "refocusing, whatever your calendar says."),
                    ("Choosing the task at the start of the block",
                     "Twenty minutes of the two hours gone before anything "
                     "moves."),
                    ("Saying yes to everything to be helpful",
                     "You become reliable for small things and unreliable for "
                     "large ones."),
                    ("Judging the day by how tired you are",
                     "Tiredness measures interruption, not progress. Ask what "
                     "finished instead."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The meeting you did not need",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "An hour-long meeting with six people costs six "
                            "hours. Almost nobody prices it that way.",
                "sub": "Declining politely, with a reason and an offer, is "
                       "normal professional behaviour.",
                "cols": 3,
                "items": [
                    "No agenda — ask for one first.",
                    "No decision — ask if notes would do.",
                    "Not your decision — send someone or read the notes.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The time management rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Two protected hours a day beats ten reactive "
                            "ones, every week.",
                "sub": "The work people remember is almost never the work that "
                       "was urgent.",
                "cols": 3,
                "items": [
                    "Two hours, same time, defended.",
                    "Interruptions batched, not refused.",
                    "Trade offered, not a flat no.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 9:40 am",
        "situation": "You are twenty minutes into your protected block on the "
                     "analysis your manager asked for. A colleague appears at "
                     "your desk with a question about a delivery.",
        "choices": [
            {
                "text": "Deal with it now — it is only a couple of minutes.",
                "tone": "ok",
                "headline": "Two minutes, plus fifteen to get back",
                "consequence": "The question genuinely takes two minutes. "
                               "Returning to where you were in the analysis "
                               "takes another fifteen. Four more colleagues "
                               "arrive before eleven, and the block produces "
                               "nothing.",
                "rule": "The cost of an interruption is the refocusing, not "
                        "the answer.",
            },
            {
                "text": "Ask whether it is a two-minute or twenty-minute "
                        "thing.",
                "tone": "good",
                "headline": "Thirty seconds, and the block survives",
                "consequence": "They think about it and say twenty. You agree "
                               "eleven o'clock and go to them then. Two others "
                               "get the same answer, and all three get a "
                               "better conversation than an interrupted one "
                               "would have been.",
                "rule": "Make them size it. Most people have never been "
                        "asked.",
            },
            {
                "text": "Say you are busy and cannot help right now.",
                "tone": "bad",
                "headline": "Protects the block, damages the relationship",
                "consequence": "The block survives and the colleague leaves "
                               "with nothing. If it genuinely was two minutes, "
                               "you have made an enemy over 120 seconds. They "
                               "will remember it next time you need "
                               "something.",
                "rule": "Never refuse without offering a time. The offer is "
                        "the whole difference.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=A895Mu8GcGw",
        "title": "Master Your Minutes - Time Management Hacks (3 Minutes)",
        "channel": "BioTech Whisperer",
        "duration": "3:00",
        "heading": "Three minutes, quick summary",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. Three minutes, so it costs almost nothing.",
            "Useful as a reminder rather than an introduction.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What does an interruption actually cost?",
            "remember": "The refocusing, not the answer.",
            "answers": [
                {"text": "The two minutes it takes to answer", "ok": False,
                 "why": "That is the visible part and much the smaller one. "
                        "The expensive part is getting back to where you were "
                        "in the work."},
                {"text": "The two minutes plus about fifteen to refocus",
                 "ok": True,
                 "why": "This is why eleven small interruptions can consume a "
                        "morning without anyone noticing where it went. The "
                        "arithmetic is invisible until you do it."},
                {"text": "Nothing, if you were not concentrating", "ok": False,
                 "why": "If you were not concentrating, the block was already "
                        "lost. The cost applies precisely when the work "
                        "mattered."},
                {"text": "It depends on who is interrupting", "ok": False,
                 "why": "Seniority changes how you respond, not what it costs "
                        "your attention. A director's question breaks focus "
                        "the same way."},
            ],
        },
        {
            "q": "Why decide the task the night before?",
            "remember": "Choosing inside the block eats the block.",
            "answers": [
                {"text": "It helps you sleep better", "ok": False,
                 "why": "It might, and that is not the operational reason. The "
                        "reason is what happens at nine the next morning."},
                {"text": "Choosing at the start wastes twenty minutes of it",
                 "ok": True,
                 "why": "Deciding is real work, and doing it inside your two "
                        "protected hours spends the freshest part of them on "
                        "something you could have settled in thirty seconds "
                        "the evening before."},
                {"text": "Your manager may change priorities overnight",
                 "ok": False,
                 "why": "Occasionally, and that is an argument for a quick "
                        "check rather than for not deciding. Most mornings "
                        "nothing has changed."},
                {"text": "It makes the block feel longer", "ok": False,
                 "why": "It makes it genuinely longer, in usable minutes. "
                        "Feeling is not the point."},
            ],
        },
        {
            "q": "Your manager adds a task. Best reply?",
            "remember": "Offer the trade.",
            "answers": [
                {"text": "\"Yes, no problem\" and work later", "ok": False,
                 "why": "They do not learn what is on your plate, and "
                        "something else slips silently. Working later is not a "
                        "plan, it is a way of hiding the problem."},
                {"text": "\"Happy to — which of these two should slip?\"",
                 "ok": True,
                 "why": "Managers usually have no visibility of your full "
                        "load, and almost always choose when asked. It also "
                        "makes you look organised rather than obstructive."},
                {"text": "\"I am completely full this week\"", "ok": False,
                 "why": "It is a refusal without information. They cannot help "
                        "you prioritise, and it reads as unwillingness rather "
                        "than capacity."},
                {"text": "Take it and drop something without saying", "ok": False,
                 "why": "The worst outcome. Something important stops moving "
                        "and nobody knows, until it is noticed at the worst "
                        "possible moment."},
            ],
        },
        {
            "q": "How do you judge whether a day worked?",
            "remember": "Ask what finished, not how tired you are.",
            "answers": [
                {"text": "By how many hours you worked", "ok": False,
                 "why": "Ten busy hours with nothing finished is a bad day "
                        "that feels like a good one. Hours measure effort, not "
                        "output."},
                {"text": "By naming one thing you actually finished", "ok": True,
                 "why": "Finished, not touched. If you cannot name one on most "
                        "days, the reactive work is winning and the block is "
                        "not being defended."},
                {"text": "By how tired you feel", "ok": False,
                 "why": "Tiredness measures interruption and context "
                        "switching, which are exactly the things that produce "
                        "nothing."},
                {"text": "By how many emails you cleared", "ok": False,
                 "why": "A cleared inbox is a good feeling and rarely the work "
                        "you were hired for. It is the most seductive form of "
                        "reactive work there is."},
            ],
        },
        {
            "q": "When should you decline a meeting?",
            "remember": "No agenda, or no decision that needs you.",
            "answers": [
                {"text": "Whenever you are busy", "ok": False,
                 "why": "Everyone is busy, so it is not a criterion. The "
                        "question is whether your presence changes what the "
                        "meeting produces."},
                {"text": "When there is no agenda or your input is not needed",
                 "ok": True,
                 "why": "Ask for an agenda first — often that alone improves "
                        "the meeting. If you are not part of the decision, "
                        "notes will do, and an hour with six people costs six "
                        "hours."},
                {"text": "Never — declining looks uncommitted", "ok": False,
                 "why": "Attending everything is not commitment, it is an "
                        "absence of prioritisation. Declining politely with a "
                        "reason and an offer is normal."},
                {"text": "When your manager is not attending", "ok": False,
                 "why": "Their attendance is not the test. Plenty of important "
                        "meetings do not involve them, and plenty of "
                        "unnecessary ones do."},
            ],
        },
    ],

    "recap": {
        "title": "Time management on one screen",
        "points": [
            ("Busy is not productive",
             "Reactive work fills any space you leave and leaves no trace."),
            ("Two hours, defended",
             "Same time daily, in the calendar, notifications off, one task."),
            ("Decide the night before",
             "Choosing inside the block spends its freshest twenty minutes."),
            ("Size the interruption",
             "\"Two minutes or twenty?\" Batch the twenties to one point."),
            ("Trade, defer, redirect",
             "Almost nothing needs a flat no, and a flat no costs the most."),
            ("Judge by what finished",
             "Not by hours worked, emails cleared, or how tired you feel."),
        ],
        "oneliner": "Two protected hours a day beats ten reactive ones, every "
                    "single week.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("clock", "The interruption question",
             "\"Two-minute thing or twenty-minute thing?\""),
            ("chat", "Three ways to say no",
             "Offer the trade, defer to Monday, redirect to the right team."),
            ("check", "The end-of-day test",
             "Name one thing that actually finished."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-05, Personal Productivity Systems. A system "
                "simple enough that you will still be using it in March.",
    },

    "glossary": [
        ("Reactive work", "Work that arrives and demands a response. It fills "
                          "any space you leave open."),
        ("Protected block", "Two hours booked in the calendar, with "
                            "notifications off and one task decided."),
        ("Context switching", "Moving between tasks. Costs roughly fifteen "
                              "minutes of refocusing each time."),
        ("Batching", "Holding several small requests and handling them "
                     "together at one point in the day."),
        ("The trade", "Offering a choice about what slips, rather than "
                      "accepting silently or refusing."),
        ("Deep work", "Work needing sustained concentration. It never feels "
                      "urgent, and it is what gets remembered."),
    ],
}
