# -*- coding: utf-8 -*-
"""DW-10 — Planning & Personal Productivity with AI. Content only."""

DECK = {
    "module_code": "DW-10",
    "area": "02-ai-daily-work",
    "filename": "02-10-planning-and-productivity-with-ai.pptx",
    "title": "Planning with AI",
    "subtitle": "Turning a long list of intentions into a week you can "
                "actually finish.",
    "duration_min": 16,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Arun's list gets longer every week",
        "icon": "clock",
        "scenario": "Arun runs production planning near Coimbatore. His "
                    "to-do list has 47 items. Every Friday he adds six and "
                    "closes four. He is working hard and falling behind, and "
                    "he cannot see which of the 47 actually matter.",
        "cost": "A list that grows faster than it shrinks, indefinitely.",
        "fix": "Sort by what breaks if it slips. Then plan only three days "
               "ahead.",
    },

    "outcomes": [
        ("list", "Sort a long list by consequence instead of by feeling"),
        ("clock", "Plan a realistic day instead of an optimistic one"),
        ("ban", "Identify the tasks worth deliberately not doing"),
        ("cycle", "Break a stuck task into a first step you can start today"),
        ("check", "Run a five-minute weekly review that actually changes "
                  "things"),
    ],

    "sections": [
        ("Sorting by consequence", "Not by urgency or feeling", "s_sort"),
        ("Planning three days", "Not five, and never a month", "s_three"),
        ("The stuck task", "Breaking it into a first step", "s_stuck"),
        ("Deciding not to do things", "The list you keep separately", "s_not"),
        ("Do this now", "Sort your real list", "s_do"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "A 6-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_sort",
            "label": "Sorting by consequence",
            "title": "Sort by what breaks",
            "lead": "Urgency is a feeling and it is usually somebody else's. "
                    "Consequence is a fact you can check.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Sorting by urgency", "tone": "bad",
                    "title": "How lists usually get done",
                    "items": [
                        "Whoever asked most recently wins",
                        "Loud requests beat important ones",
                        "Quick wins get done to feel productive",
                        "The one that matters most has no deadline yet",
                    ],
                },
                "right": {
                    "tag": "Sorting by consequence", "tone": "good",
                    "title": "What actually breaks",
                    "items": [
                        "A line stops if this slips",
                        "A customer notices if this slips",
                        "A colleague is blocked until this is done",
                        "Nothing happens at all if this slips",
                    ],
                },
            },
        },
        {
            "label": "Sorting by consequence",
            "title": "The consequence prompt",
            "visual": {
                "type": "prompt",
                "text": "Below is my task list. Sort every item into four "
                        "groups. STOPS SOMETHING: work halts if this slips. "
                        "CUSTOMER NOTICES: someone outside sees the delay. "
                        "BLOCKS A COLLEAGUE: somebody is waiting on me. NO "
                        "CONSEQUENCE: nothing happens this month if it slips. "
                        "Put each item in exactly one group. No commentary.",
                "caption": "Paste your real list underneath. It can be as "
                           "messy as it is.",
                "why": [
                    "Four groups is enough to decide and few enough to scan.",
                    "\"No consequence\" is usually a third of any long list.",
                    "It sorts without knowing your job, because you named the "
                    "tests.",
                ],
            },
        },
        {
            "anchor": "s_three",
            "label": "Planning three days",
            "title": "Plan three days, not five",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Monday is knowable", "You know roughly what will land."),
                    ("Wednesday is a guess", "Half of it will be replaced by "
                                             "something new."),
                    ("Friday is fiction", "Nothing planned on Monday survives "
                                          "to Friday intact."),
                    ("So plan three", "And re-plan on Wednesday, in five "
                                      "minutes."),
                ],
            },
        },
        {
            "label": "Planning three days",
            "title": "A realistic day",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this day-planning prompt",
                "text": "Here are my tasks for tomorrow with rough time "
                        "estimates. I have six working hours after meetings. "
                        "Tell me which of these fit, in what order, and which "
                        "do not fit at all. Assume every estimate is 50 per "
                        "cent optimistic. Do not suggest working longer.",
                "caption": "\"Assume estimates are 50 per cent optimistic\" is "
                           "the useful line.",
                "out_title": "What comes back",
                "out": [
                    "A realistic order for three or four tasks, not nine.",
                    "An explicit list of what will not happen tomorrow.",
                    "The uncomfortable but accurate answer you would not have "
                    "written yourself.",
                ],
            },
        },
        {
            "anchor": "s_stuck",
            "label": "The stuck task",
            "title": "The task that never starts",
            "lead": "Tasks that sit on a list for weeks are almost always "
                    "unclear rather than hard.",
            "visual": {
                "type": "prompt",
                "header": "Copy this unsticking prompt",
                "text": "This task has been on my list for three weeks and I "
                        "keep not starting it: [describe the task in one "
                        "line]. Give me the first five minutes of it as a "
                        "single concrete action, and tell me what information "
                        "I would need before I could finish it.",
                "caption": "Five minutes, one action, no plan.",
                "why": [
                    "A three-week-old task usually has a missing input, not a "
                    "size problem.",
                    "A five-minute first step is small enough to actually "
                    "begin.",
                    "Naming the missing information often reveals it belongs "
                    "to somebody else.",
                ],
            },
        },
        {
            "label": "The stuck task",
            "title": "Why tasks stick",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "chat", "label": "It is not a task",
                     "sub": "\"Sort out the vendor issue\" is a project. "
                            "Nothing starts because nothing is defined."},
                    {"icon": "person", "label": "It needs somebody else",
                     "sub": "You are waiting for information and have not "
                            "asked for it. Ask today."},
                    {"icon": "warn", "label": "You do not want to",
                     "sub": "A difficult conversation. The five-minute step is "
                            "usually writing the first sentence."},
                ],
            },
        },
        {
            "anchor": "s_not",
            "label": "Deciding not to do things",
            "title": "The not-doing list",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Anything in NO CONSEQUENCE that is over a month old",
                    "Anything you have rescheduled more than three times",
                    "Anything somebody else could do adequately",
                    "Anything you only kept because you felt guilty",
                ],
            },
        },
        {
            "label": "Deciding not to do things",
            "title": "Moved, not deleted",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "One list of 47",
                "bad": [
                    "Every item you have ever thought of, in one place.",
                    "You reread all 47 every morning to find the four that "
                    "matter.",
                    "The list is a source of guilt rather than a tool.",
                ],
                "good_tag": "Two lists",
                "good": [
                    "Nine active items, sorted by consequence.",
                    "Thirty-eight in a \"not now\" file you look at monthly.",
                    "Nothing was deleted, and the morning takes ninety "
                    "seconds.",
                ],
                "note": "Moving something to \"not now\" is a decision. "
                        "Leaving it on the main list is avoiding one.",
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: sort your list",
            "visual": {
                "type": "steps",
                "items": [
                    "Copy your actual task list into a blank document.",
                    "Remove customer names and replace them with roles.",
                    "Run the consequence prompt on it.",
                    "Move everything in NO CONSEQUENCE to a separate file.",
                ],
                "prompt": "Sort my list into four groups: STOPS SOMETHING, "
                          "CUSTOMER NOTICES, BLOCKS A COLLEAGUE, NO "
                          "CONSEQUENCE. Each item in exactly one group. Then "
                          "tell me the three items I should do first and why, "
                          "in one line each. No other commentary.",
                "caption": "Two minutes, and most lists shrink by a third.",
            },
        },
        {
            "label": "Do this now",
            "title": "The five-minute weekly review",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "What did I plan on Monday that did not happen, and why?",
                    "What arrived this week that was not on any list?",
                    "What has moved three times and should go to \"not now\"?",
                    "What are the three things that must happen next week?",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Planning a full week in detail",
                     "By Wednesday half of it is obsolete, so the whole plan "
                     "gets abandoned rather than adjusted."),
                    ("Sorting by urgency",
                     "Urgency belongs to whoever shouted last. Consequence "
                     "belongs to the work."),
                    ("Keeping one list of everything",
                     "You reread forty items every morning to find the four "
                     "that matter."),
                    ("Trusting your own time estimates",
                     "Almost everyone is around fifty per cent optimistic, "
                     "consistently."),
                    ("Letting a task sit unstarted for weeks",
                     "It is not hard, it is undefined. Ask for the first five "
                     "minutes."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "What not to paste into a planner",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A task list is a surprisingly detailed picture of "
                            "what the company is doing.",
                "sub": "Sorting works just as well with roles instead of "
                       "names.",
                "cols": 2,
                "items": [
                    "Customer names against deals or complaints",
                    "Colleague names against performance issues",
                    "Unannounced projects, sites or product plans",
                    "Anything from a contract, tender or board paper",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Planning is not the work",
            "visual": {
                "type": "tree",
                "question": "Have I re-planned this week more than twice?",
                "yes": {
                    "path": "Yes", "tone": "bad", "label": "Stop planning",
                    "detail": "Re-planning feels productive and produces "
                              "nothing. If the list is sorted and the first "
                              "task is clear, the problem is starting, not "
                              "planning.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Plan and go",
                    "detail": "Five minutes on Monday, five on Wednesday. That "
                              "is the whole system, and anything more is "
                              "usually avoidance.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The planning rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Sort by what breaks. Plan three days. Decide what "
                            "you will not do.",
                "sub": "Three habits, about ten minutes a week, and the list "
                       "stops growing faster than it shrinks.",
                "cols": 3,
                "items": [
                    "Consequence, not urgency.",
                    "Three days, not five.",
                    "Not-now, not never.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 8:30 am",
        "situation": "Forty-seven items on your list, six hours of actual "
                     "working time today after meetings, and three people "
                     "already waiting on you.",
        "choices": [
            {
                "text": "Work down the list from the top, as fast as you can.",
                "tone": "bad",
                "headline": "Busy all day, and the line still stops on Friday",
                "consequence": "You close nine small items and feel "
                               "productive. The material release that stops the "
                               "packing line on Friday was item 31, and it is "
                               "still item 31 tomorrow. On Friday the line "
                               "stops.",
                "rule": "List order is history, not priority.",
            },
            {
                "text": "Sort by consequence first, then plan three days.",
                "tone": "good",
                "headline": "Ten minutes, and the right four things get done",
                "consequence": "Sorting takes two minutes and puts four items "
                               "in STOPS SOMETHING, including the material "
                               "release. Nineteen fall into NO CONSEQUENCE and "
                               "move to a separate file. You plan three days "
                               "and finish the four that mattered.",
                "rule": "Sorting is faster than working, and it decides "
                        "whether the work counts.",
            },
            {
                "text": "Block out the whole week in your calendar in detail.",
                "tone": "ok",
                "headline": "A good plan, obsolete by Wednesday",
                "consequence": "Ninety minutes of careful scheduling. On "
                               "Tuesday a customer escalation takes half a "
                               "day, and by Wednesday the plan no longer "
                               "matches reality. Most people then abandon the "
                               "plan entirely rather than adjust it.",
                "rule": "Plan three days and re-plan midweek. Detailed weeks "
                        "do not survive contact.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=EG4rVXK3XQU",
        "title": "How to Plan Your Entire Week in 5 Minutes Using ChatGPT",
        "channel": "Del Denney",
        "duration": "6:22",
        "heading": "Six minutes on planning a week",
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
            "q": "What should you sort a list by?",
            "remember": "What breaks if it slips.",
            "answers": [
                {"text": "Urgency", "ok": False,
                 "why": "Urgency reflects who asked most recently and most "
                        "loudly. The task that stops a line on Friday is "
                        "rarely the one anybody is shouting about on Monday."},
                {"text": "What breaks if it slips", "ok": True,
                 "why": "A consequence is a fact you can check, and it does "
                        "not change with mood or with who is in your inbox. It "
                        "is also the only test that finds the quiet critical "
                        "item."},
                {"text": "How long each will take", "ok": False,
                 "why": "Useful for scheduling once you have decided what "
                        "matters. Sorting by duration means doing the quick "
                        "things regardless of whether they count."},
                {"text": "The order they arrived", "ok": False,
                 "why": "That is what an unsorted list already does, and it is "
                        "why the important item sits at number 31 for a "
                        "fortnight."},
            ],
        },
        {
            "q": "How far ahead should you plan?",
            "remember": "Three days, then re-plan.",
            "answers": [
                {"text": "The full week, in detail", "ok": False,
                 "why": "By Wednesday half of it is obsolete, and most people "
                        "respond by abandoning the plan rather than adjusting "
                        "it. Ninety minutes of scheduling, wasted."},
                {"text": "About three days, then re-plan midweek", "ok": True,
                 "why": "Three days is roughly how far ahead you can predict "
                        "in most operational jobs. Re-planning on Wednesday "
                        "takes five minutes and keeps the plan real."},
                {"text": "Just today", "ok": False,
                 "why": "Too short to protect anything with a lead time. You "
                        "will keep discovering on Thursday that something "
                        "needed starting on Tuesday."},
                {"text": "A month, so nothing is a surprise", "ok": False,
                 "why": "A month of detailed personal planning is fiction. "
                        "Monthly horizons are useful for commitments and "
                        "deadlines, not for daily task order."},
            ],
        },
        {
            "q": "A task has sat for three weeks. Why?",
            "remember": "Usually undefined, not hard.",
            "answers": [
                {"text": "It is too difficult", "ok": False,
                 "why": "Difficult tasks usually get started and then stall. "
                        "Tasks that never begin at all are almost always "
                        "unclear rather than hard."},
                {"text": "It is unclear, or waiting on somebody else",
                 "ok": True,
                 "why": "\"Sort out the vendor issue\" is a project with no "
                        "first action. Ask for the first five minutes and the "
                        "missing input, and it usually turns out somebody else "
                        "owes you something."},
                {"text": "It is not important", "ok": False,
                 "why": "Sometimes true, and worth testing with the "
                        "consequence sort. But plenty of genuinely critical "
                        "tasks sit for weeks purely because nobody defined the "
                        "first step."},
                {"text": "You are disorganised", "ok": False,
                 "why": "An unhelpful diagnosis that leads nowhere. The "
                        "practical question is what the first concrete five "
                        "minutes would be."},
            ],
        },
        {
            "q": "What goes on the not-now list?",
            "remember": "No consequence, and rescheduled repeatedly.",
            "answers": [
                {"text": "Anything you dislike doing", "ok": False,
                 "why": "Disliking something says nothing about whether it "
                        "matters. Several of the tasks that stop a line are "
                        "unpleasant conversations."},
                {"text": "Items with no consequence that keep being moved",
                 "ok": True,
                 "why": "If nothing happens this month when it slips, and you "
                        "have already moved it three times, you have already "
                        "decided not to do it. Writing that down makes it a "
                        "decision instead of a background guilt."},
                {"text": "Anything older than a week", "ok": False,
                 "why": "Age alone is not a test. Some long-standing items are "
                        "genuinely important and simply need a defined first "
                        "step."},
                {"text": "Everything you cannot finish today", "ok": False,
                 "why": "That would empty the list every evening and lose "
                        "everything with a lead time. Not-now is for things "
                        "with no consequence, not things with no time today."},
            ],
        },
        {
            "q": "Why assume estimates are optimistic?",
            "remember": "Almost everyone is about half out.",
            "answers": [
                {"text": "To create slack for emergencies", "ok": False,
                 "why": "Slack is a good side effect, but the reason is "
                        "simpler: the original estimates were wrong, "
                        "consistently and in the same direction."},
                {"text": "Because most people underestimate by roughly half",
                 "ok": True,
                 "why": "It is one of the most reliable patterns in how people "
                        "plan work. Applying the correction gives you a day "
                        "with three or four real tasks instead of nine "
                        "imaginary ones."},
                {"text": "To make the plan easier to achieve", "ok": False,
                 "why": "It is not about feeling successful. It is about the "
                        "plan matching what will actually happen, so you can "
                        "tell people the truth about what is not getting "
                        "done."},
                {"text": "Because interruptions are unpredictable", "ok": False,
                 "why": "Interruptions are a separate problem and worth "
                        "planning around too. The optimism correction applies "
                        "even to uninterrupted work."},
            ],
        },
    ],

    "recap": {
        "title": "Planning on one screen",
        "points": [
            ("Sort by consequence",
             "What breaks if it slips. Urgency belongs to whoever shouted "
             "last."),
            ("Plan three days",
             "Friday is fiction on Monday. Re-plan midweek in five minutes."),
            ("Halve your estimates",
             "Almost everyone is about fifty per cent optimistic, "
             "consistently."),
            ("Stuck means undefined",
             "Ask for the first five minutes and the information you are "
             "missing."),
            ("Keep a not-now list",
             "Moved, not deleted. It turns background guilt into a decision."),
            ("Re-planning is not working",
             "Twice a week is a system. Four times is avoidance."),
        ],
        "oneliner": "Sort by what breaks, plan three days, and decide what you "
                    "are not going to do.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The consequence sort",
             "Stops something, customer notices, blocks a colleague, no "
             "consequence."),
            ("clock", "The realistic day prompt",
             "Six hours, estimates halved, and what will not fit."),
            ("cycle", "The unsticking prompt",
             "First five minutes, and the input you are missing."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-11, Automation Basics. Spotting the jobs "
                "worth automating, and describing one clearly enough for "
                "somebody to build it.",
    },

    "glossary": [
        ("Consequence", "What actually happens if a task slips. The only "
                        "reliable way to sort a long list."),
        ("Not-now list", "A separate file for items with no consequence, "
                         "reviewed monthly rather than daily."),
        ("Planning horizon", "How far ahead you can usefully plan. Around "
                             "three days for most operational roles."),
        ("First action", "The concrete five minutes that starts a stuck task."),
        ("Prompt", "Everything you type in: your list and the sorting tests "
                   "you want applied."),
        ("Output", "What comes back. A suggested order, which you still "
                   "decide on."),
    ],
}
