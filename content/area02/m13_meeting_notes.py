# -*- coding: utf-8 -*-
"""DW-08 — Meeting Notes & Follow-ups with AI. Content only."""

DECK = {
    "module_code": "DW-08",
    "area": "02-ai-daily-work",
    "filename": "02-08-meeting-notes-and-followups.pptx",
    "title": "Meeting Notes & Follow-ups",
    "subtitle": "Turning an hour of discussion into decisions and owners, "
                "before anyone leaves the room.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "flow",
    "cover_image": "assets/hero-meetings.jpg",

    "why": {
        "title": "Nobody remembers who agreed what",
        "icon": "person",
        "scenario": "A weekly production meeting in Pune runs for an hour. "
                    "Everyone leaves clear about the decisions. Nine days "
                    "later, two of the four actions have not started, and "
                    "each person believed somebody else owned them.",
        "cost": "Nine days lost, and the same discussion happening again.",
        "fix": "Three columns — decision, owner, date — sent within the hour.",
    },

    "outcomes": [
        ("list", "Turn rough notes into decisions and owners in five minutes"),
        ("person", "Write actions nobody can misread as somebody else's job"),
        ("clock", "Send follow-ups the same day, every time"),
        ("shield", "Take useful notes without recording anyone unlawfully"),
        ("cycle", "Chase an overdue action without starting an argument"),
    ],

    "sections": [
        ("Notes nobody uses", "Why minutes fail", "s_fail"),
        ("Decisions, owners, dates", "The only three columns", "s_three"),
        ("Rough notes to actions", "Five minutes after the meeting", "s_rough"),
        ("Recording and consent", "Before you press record", "s_record"),
        ("Do this now", "Process a real meeting", "s_do"),
        ("Choose what you'd do", "A Friday afternoon decision", "scenario"),
        ("Watch this", "A 4-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_fail",
            "label": "Notes nobody uses",
            "title": "Why minutes fail",
            "lead": "Most meeting notes record the conversation. Almost nobody "
                    "needs the conversation.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "What gets written", "tone": "bad",
                    "title": "The discussion",
                    "items": [
                        "Who said what, in order",
                        "Points raised and considered",
                        "Background nobody disputed",
                        "\"It was agreed to look into it\"",
                    ],
                },
                "right": {
                    "tag": "What gets used", "tone": "good",
                    "title": "The decisions",
                    "items": [
                        "What was actually decided",
                        "One named owner per action",
                        "A date, not \"next week\"",
                        "What is still open, and who will close it",
                    ],
                },
            },
        },
        {
            "label": "Notes nobody uses",
            "title": "\"We agreed to look into it\"",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Unowned action",
                "bad": [
                    "\"The team will review the supplier issue and revert.\"",
                    "Four people read it. Each assumes one of the others owns "
                    "it.",
                    "Nine days later nothing has started and nobody is at "
                    "fault.",
                ],
                "good_tag": "Owned action",
                "good": [
                    "\"Priya to get written confirmation of the revised lead "
                    "time. By Thursday 14th.\"",
                    "One name, one deliverable, one date.",
                    "If it slips, everybody knows on Friday morning.",
                ],
                "note": "\"The team\" is not an owner. Every action needs one "
                        "person's name on it.",
            },
        },
        {
            "anchor": "s_three",
            "label": "Decisions, owners, dates",
            "title": "Only three columns matter",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "DECISION — what was settled, in one sentence",
                    "OWNER — one person, by name, never a team",
                    "DATE — a specific day, never \"next week\"",
                    "OPEN — what was not settled, and who will bring it back",
                ],
            },
        },
        {
            "label": "Decisions, owners, dates",
            "title": "Everything else is optional",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "check", "label": "Decisions carry",
                     "sub": "Six months later, this is the only part anyone "
                            "goes back to read."},
                    {"icon": "person", "label": "Owners prevent drift",
                     "sub": "An action with two owners has none. An action "
                            "with a team has fewer."},
                    {"icon": "clock", "label": "Dates create movement",
                     "sub": "\"Soon\" and \"next week\" are both read as "
                            "\"whenever\"."},
                ],
            },
        },
        {
            "anchor": "s_rough",
            "label": "Rough notes to actions",
            "title": "Five minutes after the meeting",
            "visual": {
                "type": "prompt",
                "text": "Below are my rough notes from a meeting. Produce "
                        "three sections and nothing else. DECISIONS: one line "
                        "each. ACTIONS: one line each, with the owner's name "
                        "and a date. OPEN: anything not settled. Use only my "
                        "notes. Where no owner or date was given, write "
                        "[OWNER?] or [DATE?].",
                "caption": "Type your notes however rough. Order does not "
                           "matter.",
                "why": [
                    "[OWNER?] shows you exactly what to chase before you send "
                    "it.",
                    "Three sections stop it summarising the discussion.",
                    "Five minutes now saves the nine days later.",
                ],
            },
        },
        {
            "label": "Rough notes to actions",
            "title": "The markers are the point",
            "visual": {
                "type": "prompt_out",
                "header": "What the markers give you",
                "text": "Send me back only the lines containing [OWNER?] or "
                        "[DATE?], as questions I can ask in one message. Keep "
                        "them short and put them in the order they came up in "
                        "the meeting.",
                "caption": "One message to the group closes every gap at "
                           "once.",
                "out_title": "What comes back",
                "out": [
                    "Three or four short questions you can send in a single "
                    "message.",
                    "Usually one action everybody assumed somebody else was "
                    "doing.",
                    "The notes go out complete, the same afternoon.",
                ],
            },
        },
        {
            "anchor": "s_record",
            "label": "Recording and consent",
            "title": "Before you press record",
            "gloss": ["Personal data"],
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A recording or transcript of a meeting is "
                            "personal data about everyone in it.",
                "sub": "Consent, storage and who can access it all have to be "
                       "settled first.",
                "cols": 2,
                "items": [
                    "Tell everyone before recording starts, not afterwards",
                    "Use only the tool the company has approved for this",
                    "Never upload a recording to a personal AI account",
                    "Never record a conversation about a person's performance",
                ],
            },
        },
        {
            "label": "Recording and consent",
            "title": "Notes are usually enough",
            "visual": {
                "type": "tree",
                "question": "Do I need every word, or just the decisions?",
                "yes": {
                    "path": "Just decisions", "tone": "good",
                    "label": "Type rough notes",
                    "detail": "For almost every internal meeting, five bullet "
                              "points typed as you go are enough. No consent "
                              "question, no storage question, no transcript to "
                              "protect.",
                },
                "no": {
                    "path": "Every word", "tone": "bad",
                    "label": "Get approval first",
                    "detail": "Disputes, formal processes, customer "
                              "commitments. Tell everyone, use the approved "
                              "tool, and check with [COMPANY INPUT NEEDED: who "
                              "approves meeting recordings].",
                },
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: process a meeting",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the notes from your most recent meeting.",
                    "Remove any customer names and replace them with roles.",
                    "Run the three-section prompt on them.",
                    "Send one message asking about every [OWNER?] and "
                    "[DATE?].",
                ],
                "prompt": "Turn my notes into three sections and nothing else. "
                          "DECISIONS, one line each. ACTIONS, one line each "
                          "with an owner and a date. OPEN, what is unsettled. "
                          "Use only my notes. Mark missing owners [OWNER?] and "
                          "missing dates [DATE?].",
                "caption": "The single most useful five minutes after any "
                           "meeting.",
            },
        },
        {
            "label": "Do this now",
            "title": "Chasing without an argument",
            "visual": {
                "type": "prompt",
                "header": "Copy this chaser",
                "text": "Write a short message chasing an action that is three "
                        "days overdue. Facts: agreed at the review on the 6th, "
                        "due the 14th, no update received. Tone: neutral and "
                        "factual, not passive-aggressive, no apology from me. "
                        "Under 50 words. End by asking for a new date.",
                "caption": "Neutral is a real instruction and it works.",
                "why": [
                    "\"Not passive-aggressive\" removes the usual edge.",
                    "\"No apology from me\" stops it softening your position.",
                    "Asking for a new date gives them something easy to do.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits after every meeting",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Write the actions before you leave the room or the call.",
                    "Read the owners and dates aloud while everyone is still "
                    "there.",
                    "Send the notes the same day, not the next morning.",
                    "Put the open items at the top of the next agenda.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Writing \"the team will\"",
                     "Four people read it and each assumes one of the others "
                     "owns it."),
                    ("Recording without telling people",
                     "A transcript is personal data about everyone in the "
                     "room, taken without consent."),
                    ("Minuting the discussion instead of the decisions",
                     "Two pages nobody reads, and the one decision buried in "
                     "the middle."),
                    ("Sending notes three days later",
                     "By then people have half-remembered a different version "
                     "and started acting on it."),
                    ("Using \"next week\" as a deadline",
                     "It is read as \"whenever\", and it always is."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The follow-up that ends a meeting",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "One message, same day",
                     "sub": "Decisions, actions with owners, open items."},
                    {"label": "No discussion in it",
                     "sub": "Nobody re-reads who argued what, ever."},
                    {"label": "Under 150 words",
                     "sub": "Long enough to be complete, short enough to be "
                            "read."},
                ],
                "note": "The whole value of a meeting is what happens in the "
                        "nine days afterwards. This message is what decides "
                        "whether anything does.",
            },
        },
        {
            "label": "Do this now",
            "title": "The meeting notes rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Every action needs one name and one date, or it "
                            "is not an action.",
                "sub": "That single test removes most of what goes wrong after "
                       "meetings.",
                "cols": 3,
                "items": [
                    "No name — nobody does it.",
                    "No date — nobody hurries.",
                    "Sent tomorrow — already too late.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Friday, 4:50 pm",
        "situation": "The weekly review has just finished. You have a page of "
                     "scribbled notes, four actions somewhere in them, and ten "
                     "minutes before you want to leave.",
        "choices": [
            {
                "text": "Send the raw notes to everyone and tidy them Monday.",
                "tone": "bad",
                "headline": "Monday's version will be a different meeting",
                "consequence": "Over the weekend, four people read four "
                               "different things into the same scribbles. On "
                               "Monday two have started work nobody asked for "
                               "and one has not started the thing they own. "
                               "Your tidy version now contradicts what people "
                               "already did.",
                "rule": "Ambiguous notes do not stay neutral. People fill the "
                        "gaps.",
            },
            {
                "text": "Run the three-section prompt, chase the gaps, send it "
                        "by five.",
                "tone": "good",
                "headline": "Eight minutes, and the week actually moves",
                "consequence": "The prompt produces four decisions, four "
                               "actions and two [OWNER?] markers. You ask both "
                               "questions in one message, get answers within "
                               "three minutes because everyone is still at "
                               "their desk, and send the final note at 4:58.",
                "rule": "The gaps are closeable while people are still in the "
                        "building.",
            },
            {
                "text": "Upload the meeting recording to an AI tool for a full "
                        "transcript.",
                "tone": "bad",
                "headline": "You just shared everyone's voice and words",
                "consequence": "The recording is personal data about six "
                               "people, none of whom agreed to it leaving the "
                               "company. It also produces four pages of "
                               "transcript when what you needed was four lines "
                               "of action.",
                "rule": "A transcript is rarely what you need and always more "
                        "than you should share.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=56pilLKRGJc",
        "title": "How to Use ChatGPT for Meeting Minutes in 2025",
        "channel": "Tactiq",
        "duration": "4:24",
        "heading": "Four minutes on meeting minutes",
        "note": "An outside video from a tool vendor. Follow this module's "
                "rules on recording and consent regardless of what it "
                "shows.",
        "how": [
            "Optional. The three-section prompt is the core.",
            "Ignore the product pitch; watch the method.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What makes an action real?",
            "remember": "One name, one date.",
            "answers": [
                {"text": "It is written in the minutes", "ok": False,
                 "why": "Being written down is necessary and nowhere near "
                        "sufficient. \"The team will review this\" is written "
                        "down and will not happen."},
                {"text": "It names one person and one date", "ok": True,
                 "why": "An action with two owners has none, and one with no "
                        "date is read as \"whenever\". Both gaps are invisible "
                        "in the room and obvious nine days later."},
                {"text": "Everybody agreed to it", "ok": False,
                 "why": "Agreement in the room is exactly what everyone "
                        "remembers afterwards. Ownership is the part that gets "
                        "forgotten."},
                {"text": "It has a clear description", "ok": False,
                 "why": "A clearly described action with no owner still does "
                        "not happen. Description is the easy half."},
            ],
        },
        {
            "q": "Why mark [OWNER?] rather than guess?",
            "remember": "A guessed owner is worse than a visible gap.",
            "answers": [
                {"text": "It makes the notes shorter", "ok": False,
                 "why": "Length is unaffected. The value is that a gap you can "
                        "see is a gap you can close before sending."},
                {"text": "A guessed owner will be quietly ignored", "ok": True,
                 "why": "If the tool assigns an owner nobody agreed to, that "
                        "person either does not read it or resents it. Either "
                        "way the action does not happen and now there is "
                        "friction too."},
                {"text": "The tool cannot read names", "ok": False,
                 "why": "It reads names in your notes perfectly well. The "
                        "marker is for cases where your notes genuinely do not "
                        "say who agreed to do it."},
                {"text": "It shows you were paying attention", "ok": False,
                 "why": "It is not about appearances. It is about closing four "
                        "real gaps in one message while people are still at "
                        "their desks."},
            ],
        },
        {
            "q": "Before recording a meeting, what first?",
            "remember": "Tell everyone, and use an approved tool.",
            "answers": [
                {"text": "Check the audio quality", "ok": False,
                 "why": "Practical and beside the point. The question that has "
                        "to be settled first is whether you may record these "
                        "people at all."},
                {"text": "Tell everyone, and check the tool is approved",
                 "ok": True,
                 "why": "A recording is personal data about every person in "
                        "the room. Consent, an approved tool and a known "
                        "storage location all have to be settled before you "
                        "press the button."},
                {"text": "Ask your manager afterwards", "ok": False,
                 "why": "Afterwards is far too late. The recording already "
                        "exists and the people in it were never given the "
                        "chance to object."},
                {"text": "Nothing — internal meetings are fine to record",
                 "ok": False,
                 "why": "Internal does not remove the consent question. "
                        "Colleagues have the same rights over their own voice "
                        "and words as anyone else."},
            ],
        },
        {
            "q": "When should notes go out?",
            "remember": "The same day, before people leave.",
            "answers": [
                {"text": "Within a week is fine", "ok": False,
                 "why": "By then everybody has half-remembered a different "
                        "version and some have acted on it. Your notes now "
                        "contradict work already done."},
                {"text": "The same day, while people can still answer",
                 "ok": True,
                 "why": "Two things matter: the meeting is fresh, and the "
                        "people who can close your [OWNER?] gaps are still at "
                        "their desks. Both stop being true overnight."},
                {"text": "Only after your manager reviews them", "ok": False,
                 "why": "Sensible for board minutes, unnecessary for a weekly "
                        "review, and it usually means they go out three days "
                        "late or not at all."},
                {"text": "At the start of the next meeting", "ok": False,
                 "why": "That is a week of nothing happening, followed by a "
                        "discussion about why nothing happened."},
            ],
        },
        {
            "q": "How do you chase without friction?",
            "remember": "Neutral, factual, and ask for a new date.",
            "answers": [
                {"text": "Copy in their manager", "ok": False,
                 "why": "That escalates a three-day slip into a formal "
                        "problem. Keep it between you first, and it usually "
                        "resolves the same day."},
                {"text": "State the dates, stay neutral, ask for a new date",
                 "ok": True,
                 "why": "Facts remove the accusation, and asking for a new "
                        "date gives them something easy to reply to. Most "
                        "overdue actions are forgotten, not refused."},
                {"text": "Apologise for chasing", "ok": False,
                 "why": "You have nothing to apologise for, and it makes the "
                        "message read as optional. \"No apology from me\" is a "
                        "genuinely useful instruction here."},
                {"text": "Wait — they will get to it", "ok": False,
                 "why": "Sometimes true, and the cost of being wrong is "
                        "another week. A fifty-word neutral message costs "
                        "almost nothing."},
            ],
        },
    ],

    "recap": {
        "title": "Meeting notes on one screen",
        "points": [
            ("Record decisions, not discussion",
             "Nobody ever goes back to read who said what."),
            ("One name, one date",
             "\"The team will\" is not an action. It is a gap with a sentence "
             "around it."),
            ("Mark the gaps, do not guess",
             "[OWNER?] and [DATE?] get closed in one message the same "
             "afternoon."),
            ("Send it the same day",
             "Overnight, people half-remember a different meeting and act on "
             "it."),
            ("Recording needs consent",
             "A transcript is personal data about everyone in the room."),
            ("Chase neutrally",
             "State the dates, ask for a new one, and skip the apology."),
        ],
        "oneliner": "Every action needs one name and one date, or it is not an "
                    "action.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The three-section prompt",
             "Decisions, actions with owners, open items."),
            ("person", "The gap-closing message",
             "Every [OWNER?] and [DATE?] as one short question set."),
            ("clock", "The neutral chaser",
             "Dates stated, no apology, new date requested."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-09, Brainstorming with AI. Getting twenty "
                "ideas in two minutes, and knowing which three are worth "
                "keeping.",
    },

    "glossary": [
        ("Action", "Something one named person will do by a stated date. "
                   "Anything else is a discussion point."),
        ("Owner", "The single person accountable. Never a team, never two "
                  "people."),
        ("Open item", "Something not settled, with a named person bringing it "
                      "back."),
        ("Transcript", "A written record of everything said. Personal data "
                       "about everyone present."),
        ("Personal data", "Anything identifying a person, including their "
                          "recorded voice and words."),
        ("Prompt", "Everything you type in: your rough notes and the structure "
                   "you want back."),
    ],
}
