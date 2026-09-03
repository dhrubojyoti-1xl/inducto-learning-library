# -*- coding: utf-8 -*-
"""PS-05 — Personal Productivity Systems. Content only."""

DECK = {
    "module_code": "PS-05",
    "area": "04-professional-skills",
    "filename": "04-05-personal-productivity-systems.pptx",
    "title": "Productivity Systems",
    "subtitle": "A system simple enough that you will still be using it in "
                "March.",
    "duration_min": 16,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Latika's fourth system this year",
        "icon": "cycle",
        "scenario": "Latika manages purchasing in Jaipur. In January she "
                    "started a new app. In March she moved to a notebook. In "
                    "June she tried colour-coded folders. Each lasted about "
                    "three weeks, and things still slip through.",
        "cost": "Four fresh starts, and the same forgotten commitments.",
        "fix": "One place, one daily review, and a rule for what goes where.",
    },

    "outcomes": [
        ("list", "Keep one place for commitments instead of six"),
        ("clock", "Run a two-minute daily review you will actually do"),
        ("check", "Capture a commitment in under ten seconds"),
        ("eye", "Recognise why your last system stopped working"),
        ("cycle", "Recover from a week where you abandoned it entirely"),
    ],

    "sections": [
        ("Why systems fail", "Complexity, not discipline", "s_fail"),
        ("One place for everything", "The capture rule", "s_capture"),
        ("The two-minute review", "Daily, not weekly", "s_review"),
        ("When it collapses", "Restarting without guilt", "s_collapse"),
        ("Do this now", "Set up the minimum", "s_do"),
        ("Choose what you'd do", "A Thursday morning decision", "scenario"),
        ("Watch this", "A 7-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_fail",
            "label": "Why systems fail",
            "title": "Complexity, not discipline",
            "lead": "People blame themselves for abandoning a system. Usually "
                    "the system was asking for more than any working week "
                    "allows.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Systems that fail", "tone": "bad",
                    "title": "Too much structure",
                    "items": [
                        "Projects, contexts, energy levels and tags",
                        "A weekly review that takes ninety minutes",
                        "Three apps that need to stay in sync",
                        "Perfect for two weeks, abandoned in the third",
                    ],
                },
                "right": {
                    "tag": "Systems that last", "tone": "good",
                    "title": "Almost no structure",
                    "items": [
                        "One list, one file, one place",
                        "A review that takes two minutes",
                        "Works on paper if the laptop dies",
                        "Survives a bad week without collapsing",
                    ],
                },
            },
        },
        {
            "label": "Why systems fail",
            "title": "The third-week test",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Week one", "Everything is captured. It feels excellent."),
                    ("Week two", "Still going, with a little effort."),
                    ("Week three", "A crisis arrives. The system is skipped."),
                    ("Week four", "It is now out of date, so it is "
                                  "abandoned."),
                ],
            },
        },
        {
            "anchor": "s_capture",
            "label": "One place for everything",
            "title": "One place, always",
            "gloss": ["Capture"],
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "ONE LIST — every commitment you make, wherever you made "
                    "it",
                    "TEN SECONDS — if capturing takes longer, you will stop",
                    "NO SORTING AT CAPTURE — write it down, sort it later",
                    "ALWAYS WITH YOU — phone or notebook, not the desktop",
                ],
            },
        },
        {
            "label": "One place for everything",
            "title": "Where commitments actually arrive",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "chat", "label": "In corridors",
                     "sub": "\"Can you look at that by Friday?\" Half of all "
                            "commitments are made standing up."},
                    {"icon": "person", "label": "In meetings",
                     "sub": "Agreed verbally, minuted vaguely, remembered "
                            "differently by everyone present."},
                    {"icon": "mail", "label": "In messages",
                     "sub": "Buried in a thread you will not find again in "
                            "three days."},
                ],
            },
        },
        {
            "anchor": "s_review",
            "label": "The two-minute review",
            "title": "Two minutes, daily",
            "lead": "A weekly review is a good idea that most people never do "
                    "twice. A daily one takes two minutes and survives.",
            "visual": {
                "type": "prompt",
                "header": "Copy these four questions",
                "text": "1. What did I commit to today that is not written "
                        "down?  2. What is overdue that I have quietly "
                        "stopped looking at?  3. What is the one thing that "
                        "must move tomorrow?  4. What can I strike off "
                        "entirely?",
                "caption": "Ask these at the same point every day. The end of "
                           "the day works best.",
                "why": [
                    "Question one catches corridor commitments before they "
                    "vanish.",
                    "Question two is the one people avoid, and the most "
                    "useful.",
                    "Question four is why the list does not grow forever.",
                ],
            },
        },
        {
            "label": "The two-minute review",
            "title": "Daily beats weekly",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "The weekly review",
                "bad": [
                    "Ninety minutes, scheduled for Friday afternoon.",
                    "Skipped whenever Friday is busy, which is most Fridays.",
                    "After two skips the list is stale and gets abandoned.",
                ],
                "good_tag": "The daily two minutes",
                "good": [
                    "Four questions, at the end of the day, every day.",
                    "Skipping one day costs nothing at all.",
                    "The list is never more than a day out of date.",
                ],
                "note": "A system's real quality is how well it survives the "
                        "week you ignore it.",
            },
        },
        {
            "anchor": "s_collapse",
            "label": "When it collapses",
            "title": "Restarting without guilt",
            "visual": {
                "type": "steps",
                "items": [
                    "Do not read the old list. It is stale and it will "
                    "depress you.",
                    "Write down everything on your mind right now, in five "
                    "minutes.",
                    "Then skim the old list and move across only what is still "
                    "live.",
                    "Delete the rest. Nothing bad has ever come of this.",
                ],
                "prompt": "Here is a long, messy list of things I have "
                          "committed to. Sort it into: OVERDUE, THIS WEEK, "
                          "NOT NOW. Put each item in exactly one group. Then "
                          "tell me the three I should do first. No commentary.",
                "caption": "Use this when the list has become a source of "
                           "guilt rather than a tool.",
            },
        },
        {
            "label": "When it collapses",
            "title": "The list is not the work",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Time spent organising the list is not time spent "
                            "doing the work.",
                "sub": "Tidying a system is the most convincing form of "
                       "procrastination there is.",
                "cols": 3,
                "items": [
                    "Two minutes a day is the budget.",
                    "New app is almost never the answer.",
                    "If it is tidy and nothing moved, that is a bad day.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: set the minimum",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick one place. A note on your phone is genuinely fine.",
                    "Write down every commitment you can remember making.",
                    "Set a daily reminder for the four review questions.",
                    "Do it tomorrow, even if you write nothing new down.",
                ],
                "prompt": "Ask me the four review questions one at a time, "
                          "wait for my answer to each, and at the end give me "
                          "back a short list of what I said. Do not add "
                          "advice, do not add tasks I did not mention, and do "
                          "not ask about anything else.",
                "caption": "Useful on the days you cannot face the list "
                           "alone.",
            },
        },
        {
            "label": "Do this now",
            "title": "What goes where",
            "visual": {
                "type": "tree",
                "question": "Does this have a fixed time attached to it?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Calendar",
                    "detail": "Meetings, deadlines, protected blocks and "
                              "anything that must happen at a particular "
                              "moment. If it is not in the calendar, it does "
                              "not exist.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "The list",
                    "detail": "Everything else. Tasks, commitments, things to "
                              "chase, things to read. One list, sorted by "
                              "consequence rather than by date.",
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
                    "Capture in ten seconds, wherever you are standing.",
                    "One list. Never two, and never an app you are trialling.",
                    "Four questions daily, at the same point every day.",
                    "Strike things off deliberately, not by forgetting them.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Starting a new app when the old one fails",
                     "The app was never the problem. The setup cost buys three "
                     "more weeks and the same collapse."),
                    ("Sorting at the moment of capture",
                     "Ten seconds becomes ninety, so you stop capturing at "
                     "all."),
                    ("Keeping commitments in your head",
                     "The ones made in corridors are exactly the ones that get "
                     "forgotten."),
                    ("A weekly review that takes ninety minutes",
                     "It gets skipped twice and then abandoned. Daily and tiny "
                     "survives."),
                    ("Treating an out-of-date list as a failure",
                     "Every list goes stale. Restarting takes five minutes and "
                     "no guilt is required."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The productivity rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "The best system is the one still running in "
                            "March.",
                "sub": "Simplicity is not a compromise here. It is the whole "
                       "design requirement.",
                "cols": 3,
                "items": [
                    "One place to capture.",
                    "Two minutes to review.",
                    "Restart without guilt.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Thursday, 8:40 am",
        "situation": "You have not opened your task list in nine days. It is "
                     "long, out of date and slightly frightening. Two things "
                     "have already been chased this week.",
        "choices": [
            {
                "text": "Set up a proper system this weekend and start "
                        "fresh Monday.",
                "tone": "bad",
                "headline": "The fourth system this year",
                "consequence": "You spend Saturday choosing an app and "
                               "designing categories. It works beautifully for "
                               "eleven days. Then a crisis week arrives, you "
                               "skip it twice, and by the end of the month you "
                               "are back exactly here.",
                "rule": "The setup is never the problem. The third week is.",
            },
            {
                "text": "Spend five minutes writing down everything on your "
                        "mind, then skim the old list.",
                "tone": "good",
                "headline": "Five minutes, and you are current again",
                "consequence": "Writing from memory captures the live "
                               "commitments, because the live ones are the "
                               "ones you are worrying about. Skimming the old "
                               "list adds four more and lets you delete "
                               "nineteen. You are current by nine o'clock.",
                "rule": "Start from your head, not from the stale list.",
            },
            {
                "text": "Work from your inbox until things calm down.",
                "tone": "bad",
                "headline": "The inbox is somebody else's priorities",
                "consequence": "You are busy all day and everything you do was "
                               "chosen by whoever emailed most recently. The "
                               "two things being chased are not in your inbox, "
                               "because the people chasing gave up on email "
                               "and rang your manager instead.",
                "rule": "An inbox is a list of other people's priorities, "
                        "sorted by time.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=7M6bIeVbCqA",
        "title": "My Simple Productivity System (for normal people)!",
        "channel": "Jeff Su",
        "duration": "7:04",
        "heading": "Seven minutes, one simple system",
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
            "q": "Why do most systems get abandoned?",
            "remember": "They ask for more than a bad week allows.",
            "answers": [
                {"text": "People lack discipline", "ok": False,
                 "why": "The same people run complex operations reliably every "
                        "day. If a system only works in calm weeks, the system "
                        "is badly designed for the job."},
                {"text": "They demand more upkeep than a bad week allows",
                 "ok": True,
                 "why": "Week three always brings a crisis. A system needing "
                        "ninety minutes weekly gets skipped, goes stale, and "
                        "is then abandoned because it is out of date."},
                {"text": "The apps are not good enough", "ok": False,
                 "why": "Apps are not the constraint. People run perfectly "
                        "good systems on paper, and abandon excellent apps for "
                        "the same reason."},
                {"text": "Work is too unpredictable to plan", "ok": False,
                 "why": "Unpredictability is exactly why capture matters. It "
                        "is an argument for a simpler system, not for none."},
            ],
        },
        {
            "q": "What matters most about capture?",
            "remember": "Under ten seconds, or you will stop.",
            "answers": [
                {"text": "That it is in the right category", "ok": False,
                 "why": "Sorting at capture is what turns ten seconds into "
                        "ninety. Write it down anywhere in the one place, and "
                        "sort during the review."},
                {"text": "That it takes under ten seconds", "ok": True,
                 "why": "If capturing is slow, you skip it when you are busy — "
                        "which is exactly when commitments are being made at "
                        "you in corridors."},
                {"text": "That it is typed rather than written", "ok": False,
                 "why": "Either is fine. What matters is that the one place is "
                        "always with you, whether that is a phone or a "
                        "notebook."},
                {"text": "That you review it immediately", "ok": False,
                 "why": "Immediate review defeats the point of fast capture. "
                        "Capture now, review once a day."},
            ],
        },
        {
            "q": "Why daily rather than weekly review?",
            "remember": "Skipping a day costs nothing.",
            "answers": [
                {"text": "Daily reviews are more thorough", "ok": False,
                 "why": "They are far less thorough, deliberately. Two minutes "
                        "cannot be thorough, and that is what makes it "
                        "survive."},
                {"text": "Missing one day does no damage", "ok": True,
                 "why": "Missing one weekly review leaves the list a fortnight "
                        "stale, which is usually the point of abandonment. "
                        "Missing one daily review costs a day."},
                {"text": "Weekly reviews are old-fashioned", "ok": False,
                 "why": "They work well for people who genuinely do them. The "
                        "problem is empirical rather than fashionable — most "
                        "people do not."},
                {"text": "Managers expect daily updates", "ok": False,
                 "why": "This is about your own system, not reporting. Nobody "
                        "else needs to see it."},
            ],
        },
        {
            "q": "The list is nine days stale. Best move?",
            "remember": "Start from your head, then skim the old list.",
            "answers": [
                {"text": "Read the whole old list carefully first", "ok": False,
                 "why": "It is demoralising and most of it is dead. Reading it "
                        "first is how people decide the system has failed and "
                        "give up entirely."},
                {"text": "Write everything on your mind, then skim the old "
                         "list", "ok": True,
                 "why": "The live commitments are the ones you are already "
                        "worrying about, so five minutes from memory captures "
                        "them. The old list then adds a few and lets you "
                        "delete many."},
                {"text": "Delete it and start completely fresh", "ok": False,
                 "why": "Close, and you would lose the handful of genuine "
                        "commitments in there. Skim it once before deleting."},
                {"text": "Rebuild it properly over the weekend", "ok": False,
                 "why": "Weekend rebuilding is the pattern that produces four "
                        "systems a year. Five minutes on a Thursday morning is "
                        "enough."},
            ],
        },
        {
            "q": "What belongs in the calendar?",
            "remember": "Anything with a fixed time.",
            "answers": [
                {"text": "Everything, so nothing is forgotten", "ok": False,
                 "why": "A calendar full of tasks with invented times becomes "
                        "unreadable, and you start ignoring it — including the "
                        "real appointments."},
                {"text": "Anything that must happen at a particular time",
                 "ok": True,
                 "why": "Meetings, deadlines and protected blocks. Everything "
                        "else lives on the list, sorted by consequence rather "
                        "than by an arbitrary time."},
                {"text": "Only meetings with other people", "ok": False,
                 "why": "Your protected block is the most important "
                        "appointment in the week, and it only survives if it "
                        "is booked like one."},
                {"text": "Nothing — the list covers it", "ok": False,
                 "why": "A list cannot hold a time-specific commitment safely. "
                        "Anything with a clock on it needs to be where the "
                        "clock is."},
            ],
        },
    ],

    "recap": {
        "title": "Productivity systems on one screen",
        "points": [
            ("Simplicity is the requirement",
             "The best system is the one still running in March, not the "
             "cleverest one."),
            ("One place to capture",
             "Always with you, under ten seconds, no sorting at the moment of "
             "writing."),
            ("Two minutes daily",
             "Four questions at the same point every day. Skipping one costs "
             "nothing."),
            ("Calendar for times, list for everything else",
             "If it has a clock on it, it belongs where the clock is."),
            ("Restart from your head",
             "The live commitments are the ones you are already worrying "
             "about."),
            ("Tidying is not working",
             "Organising the list is the most convincing procrastination there "
             "is."),
        ],
        "oneliner": "The best system is the one you are still using in March.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The four review questions",
             "Uncaptured, overdue, tomorrow's one thing, what to strike."),
            ("cycle", "The restart routine",
             "Five minutes from memory, then skim and delete."),
            ("check", "The where-does-it-go test",
             "Fixed time means calendar. Everything else means list."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-06, Problem-Solving. Finding the actual cause "
                "before you spend a fortnight fixing the wrong thing.",
    },

    "glossary": [
        ("Capture", "Writing a commitment down the moment it is made, in under "
                    "ten seconds."),
        ("Daily review", "Four questions at the same point each day. Two "
                         "minutes, and it survives bad weeks."),
        ("Stale list", "A list nobody has opened for days. Restart from memory "
                       "rather than reading it."),
        ("Consequence", "What breaks if a task slips. A better sort order than "
                        "urgency or date."),
        ("Protected block", "Time booked in the calendar for work needing "
                            "concentration."),
        ("Inbox", "A list of other people's priorities, sorted by when they "
                  "were sent."),
    ],
}
