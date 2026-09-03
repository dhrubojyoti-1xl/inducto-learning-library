# -*- coding: utf-8 -*-
"""SEC-06 — Safe Use of AI at Work. Content only."""

DECK = {
    "module_code": "SEC-06",
    "area": "05-security-privacy",
    "filename": "05-06-safe-use-of-ai-at-work.pptx",
    "title": "Safe Use of AI at Work",
    "subtitle": "Which tools are approved, which settings to switch off, and "
                "how to keep a trail you can actually explain.",
    "duration_min": 17,
    "audience": "Mandatory for all staff",
    "motif": "network",

    "why": {
        "title": "Harish cannot answer a simple question",
        "icon": "shield",
        "scenario": "Harish runs projects in Abu Dhabi. A client asks, during "
                    "an audit, whether any of their drawings have been "
                    "processed by AI tools. He genuinely does not know. Nor "
                    "does anyone else, because nobody kept a record.",
        "cost": "A question we could not answer, in front of a client.",
        "fix": "Approved tools, the right settings, and a habit of noting "
               "what you used.",
    },

    "outcomes": [
        ("check", "Tell an approved tool from an unapproved one at a glance"),
        ("lock", "Switch off the settings that let your work train a model"),
        ("doc", "Keep a record that answers an audit question in one line"),
        ("eye", "Recognise AI hidden inside tools you already use"),
        ("person", "Say plainly when AI helped, without over-explaining"),
    ],

    "sections": [
        ("Approved and unapproved", "The account decides", "s_approved"),
        ("The settings that matter", "Two switches", "s_settings"),
        ("AI you did not notice", "Already inside your tools", "s_hidden"),
        ("Keeping a trail", "Answering the audit question", "s_trail"),
        ("Do this now", "Check your own setup", "s_do"),
        ("Choose what you'd do", "An audit-week decision", "scenario"),
        ("Watch this", "A 13-minute outside overview", "video"),
    ],

    "slides": [
        {
            "anchor": "s_approved",
            "label": "Approved and unapproved",
            "title": "The account decides everything",
            "lead": "The same model can be safe or unsafe depending entirely "
                    "on which account you signed in with.",
            "gloss": ["Approved tool"],
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Unapproved", "tone": "bad",
                    "title": "Personal login, free tier",
                    "items": [
                        "No agreement anybody here has read",
                        "Chats often used to improve the service",
                        "No record of what was shared",
                        "Nothing can be deleted on our behalf",
                    ],
                },
                "right": {
                    "tag": "Approved", "tone": "good",
                    "title": "[COMPANY INPUT NEEDED: approved AI tool]",
                    "items": [
                        "Covered by terms the company agreed",
                        "Business tiers normally exclude training on your "
                        "data",
                        "Access is managed and can be withdrawn",
                        "Somebody can answer questions about it later",
                    ],
                },
            },
        },
        {
            "label": "Approved and unapproved",
            "title": "Signs you are in the wrong place",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "mark": "ban",
                "items": [
                    "You signed in with a personal email, not your work one",
                    "There was no single sign-on screen or company logo",
                    "The site offered a free trial or asked for a card",
                    "You found it through a search result or a social post",
                ],
            },
        },
        {
            "anchor": "s_settings",
            "label": "The settings that matter",
            "title": "Two switches worth finding",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "ban", "label": "Training on your data",
                     "sub": "Consumer accounts often use chats to improve the "
                            "service. Business tiers usually do not. Check "
                            "which you are on."},
                    {"icon": "clock", "label": "Chat history",
                     "sub": "Turning history off usually turns training off "
                            "too, and leaves less sitting there to leak."},
                    {"icon": "person", "label": "Shared workspaces",
                     "sub": "Check whether colleagues can see your "
                            "conversations. Sometimes they can."},
                ],
            },
        },
        {
            "label": "The settings that matter",
            "title": "Settings are not a substitute",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Switching training off reduces the risk. It does "
                            "not make confidential data safe to paste.",
                "sub": "The text still travels, is still stored, and is still "
                       "outside our control.",
                "cols": 3,
                "items": [
                    "Settings reduce reuse.",
                    "They do not stop transmission.",
                    "The paste rules still apply.",
                ],
            },
        },
        {
            "anchor": "s_hidden",
            "label": "AI you did not notice",
            "title": "It is already in your tools",
            "lead": "Most people using AI at work today did not decide to. It "
                    "arrived inside software they already had.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Your email suggests replies", "That is a model reading "
                                                    "your message."),
                    ("Your notes app summarises", "Meeting notes processed "
                                                  "somewhere else."),
                    ("Your browser offers to rewrite", "Selected text sent "
                                                       "off for a suggestion."),
                    ("A plugin joins your call", "Recording and transcribing, "
                                                 "often unnoticed."),
                ],
            },
        },
        {
            "label": "AI you did not notice",
            "title": "The uninvited meeting bot",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("A note-taking bot joins the call",
                     "Somebody's personal tool is now recording a meeting "
                     "nobody consented to."),
                    ("A browser extension rewrites your email",
                     "The text was sent to a service the company has never "
                     "assessed."),
                    ("A free PDF summariser",
                     "You uploaded a contract to a website to save ten "
                     "minutes of reading."),
                    ("A phone keyboard with AI suggestions",
                     "Everything typed, including in work apps, may be "
                     "processed elsewhere."),
                ],
            },
        },
        {
            "anchor": "s_trail",
            "label": "Keeping a trail",
            "title": "Answering the audit question",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "No record",
                "bad": [
                    "\"Has any of our material been through an AI tool?\"",
                    "\"I do not think so, but I could not say for certain.\"",
                    "That answer is worse than a yes with a record behind it.",
                ],
                "good_tag": "One line per use",
                "good": [
                    "\"Drafting assistance only, on the approved tool, with no "
                    "client drawings uploaded.\"",
                    "Backed by a note in the project file, written at the "
                    "time.",
                    "The question takes thirty seconds and ends there.",
                ],
                "note": "Nobody is asking you to justify using a tool. They "
                        "are asking whether you know what happened to their "
                        "material.",
            },
        },
        {
            "label": "Keeping a trail",
            "title": "The one-line note",
            "visual": {
                "type": "prompt",
                "header": "Copy this note format",
                "text": "AI use: [what for — drafting / summarising / "
                        "formatting]. Tool: [approved tool name]. Data "
                        "provided: [description, e.g. dates and quantities "
                        "only, no client documents]. Output checked by: [your "
                        "name]. Date: [date].",
                "caption": "Five fields, twenty seconds, kept in the project "
                           "file.",
                "why": [
                    "\"Data provided\" is the field the auditor cares about.",
                    "\"Checked by\" makes clear a person owned the output.",
                    "Written at the time, it takes seconds. Reconstructed "
                    "later, it is guesswork.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: check your setup",
            "visual": {
                "type": "steps",
                "items": [
                    "Open every AI tool you have used for work in the last "
                    "month.",
                    "Check which account you are signed in with on each.",
                    "Find the data and privacy settings and turn training "
                    "off.",
                    "Remove any browser extension you cannot name the vendor "
                    "of.",
                ],
                "prompt": "Explain, for someone with no technical background, "
                          "what the difference is between a consumer AI "
                          "account and a business one in terms of how data is "
                          "handled. Six lines maximum. Do not recommend "
                          "specific products.",
                "caption": "Useful background before you check your own "
                           "settings.",
            },
        },
        {
            "label": "Do this now",
            "title": "Saying that AI helped",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Never present AI output as a source or as research.",
                    "If asked, say plainly that you drafted it with AI "
                    "assistance.",
                    "Do not claim a level of checking you did not do.",
                    "The work is yours either way, because you sent it.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The three rules that never change",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Approved tool, work account",
                     "sub": "Every time, including for quick questions."},
                    {"label": "Facts, never files",
                     "sub": "Describe the situation. Do not upload the "
                            "document."},
                    {"label": "A person checks the output",
                     "sub": "And a person is accountable for it afterwards."},
                ],
                "note": "Settings, tools and policies will change. These three "
                        "have not changed since the first of these tools "
                        "arrived, and will not.",
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Using a personal account for a quick question",
                     "Quick questions carry the same data as slow ones, with "
                     "none of the protections."),
                    ("Installing a browser extension that rewrites text",
                     "Everything you select goes to a service nobody here has "
                     "assessed."),
                    ("Letting a note-taking bot into a client call",
                     "You have recorded people who never agreed to be "
                     "recorded."),
                    ("Assuming settings make pasting safe",
                     "They reduce reuse. The data still leaves, and is still "
                     "stored."),
                    ("Keeping no record at all",
                     "\"I do not know\" is the worst possible answer to an "
                     "audit question."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The safe use rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Approved tool, work account, facts not files, and "
                            "a person who checked it.",
                "sub": "Four conditions. If all four hold, you are almost "
                       "always fine.",
                "cols": 3,
                "items": [
                    "Approved tool and work account.",
                    "Facts described, files kept back.",
                    "A named person checked the output.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Audit week, Tuesday",
        "situation": "A client auditor asks whether their technical drawings "
                     "have been processed by any AI tool. You used an "
                     "assistant during the project, but not on the drawings.",
        "choices": [
            {
                "text": "Say no — you are fairly sure the drawings were never "
                        "uploaded.",
                "tone": "bad",
                "headline": "A confident answer you cannot support",
                "consequence": "You are probably right and you cannot show it. "
                               "If the auditor asks a second question — which "
                               "tool, which account, who else on the team — "
                               "the answer becomes \"I would have to check\", "
                               "which reads as a no that was never verified.",
                "rule": "An unsupported no is worse than a documented yes.",
            },
            {
                "text": "Say what you used it for, on which tool, and what you "
                        "did not upload.",
                "tone": "good",
                "headline": "Thirty seconds, and the question closes",
                "consequence": "\"Drafting assistance on the approved tool for "
                               "progress reports. No client drawings were "
                               "uploaded at any point.\" You show the one-line "
                               "note in the project file. The auditor moves "
                               "on.",
                "rule": "Specific and documented beats reassuring and vague.",
            },
            {
                "text": "Say nobody on the project used AI at all.",
                "tone": "bad",
                "headline": "A statement you cannot possibly know",
                "consequence": "You cannot speak for six people's browser "
                               "extensions, phone keyboards and note-taking "
                               "apps. If any of them did use something, your "
                               "answer becomes a false statement to a client "
                               "auditor, which is a far larger problem than "
                               "the original question.",
                "rule": "Answer for what you know. Never for what others did.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=pR7FfNWjEe8",
        "title": "How to Secure AI Business Models",
        "channel": "IBM Technology",
        "duration": "13:13",
        "heading": "Thirteen minutes on the wider picture",
        "note": "Aimed at people building AI systems. Watch for context, not "
                "for the daily rules — those are in this module.",
        "how": [
            "Optional. The four conditions above are what you need.",
            "Useful if you want to understand what governance means.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What makes a tool approved?",
            "remember": "An agreement and an account, not the brand.",
            "answers": [
                {"text": "It is a well-known brand", "ok": False,
                 "why": "Brand tells you nothing about the terms you are "
                        "using. The same well-known tool is safe on a company "
                        "account and unassessed on a personal free one."},
                {"text": "The company has an agreement and you use your work "
                         "account", "ok": True,
                 "why": "Those two together give terms somebody has read, "
                        "managed access, and a person who can answer questions "
                        "about it afterwards. Without them, none of that "
                        "exists."},
                {"text": "It has a privacy policy", "ok": False,
                 "why": "Every service has one, and almost nobody at this "
                        "company has read the one on a free consumer tier. A "
                        "policy is not an agreement we negotiated."},
                {"text": "You turned the training setting off", "ok": False,
                 "why": "That helps and it does not create an agreement, a "
                        "record or any ability to delete data later. Settings "
                        "are one layer, not the whole thing."},
            ],
        },
        {
            "q": "What do the settings actually do?",
            "remember": "Reduce reuse. They do not stop transmission.",
            "answers": [
                {"text": "Stop your data leaving your laptop", "ok": False,
                 "why": "Nothing about a privacy setting keeps text local. "
                        "Whatever you type still travels to the service and is "
                        "processed there."},
                {"text": "Reduce the chance your text is reused for training",
                 "ok": True,
                 "why": "That is a genuine and worthwhile reduction. It does "
                        "not change the fact that the data was transmitted, "
                        "stored and is outside our control."},
                {"text": "Delete your conversations immediately", "ok": False,
                 "why": "Some services retain content for a period regardless, "
                        "for abuse monitoring. Turning history off is not the "
                        "same as instant deletion."},
                {"text": "Make confidential data safe to paste", "ok": False,
                 "why": "They never do this. The paste rules are unchanged by "
                        "any setting on any tier of any product."},
            ],
        },
        {
            "q": "Where does unnoticed AI usually arrive?",
            "remember": "Inside tools you already had.",
            "answers": [
                {"text": "Through deliberate downloads", "ok": False,
                 "why": "Deliberate use is the visible, manageable kind. The "
                        "risk is the features that appeared in software you "
                        "were already using."},
                {"text": "As new features in email, browsers and meeting apps",
                 "ok": True,
                 "why": "Reply suggestions, rewrite buttons, meeting "
                        "summaries and note-taking bots. Most people using AI "
                        "at work never chose to."},
                {"text": "Only in tools with AI in the name", "ok": False,
                 "why": "Almost none of them are named that way. The feature "
                        "is usually a small button or an automatic suggestion "
                        "with no label at all."},
                {"text": "Through the IT department", "ok": False,
                 "why": "IT-deployed tools are the assessed ones. Unnoticed AI "
                        "arrives through vendor updates and extensions "
                        "individuals install themselves."},
            ],
        },
        {
            "q": "Why keep a one-line note?",
            "remember": "\"I do not know\" is the worst audit answer.",
            "answers": [
                {"text": "To prove you followed policy", "ok": False,
                 "why": "Partly, and the real purpose is narrower. The "
                        "question is almost always what happened to the "
                        "client's material, not whether you behaved well."},
                {"text": "So you can answer what data was provided", "ok": True,
                 "why": "That single field is what an auditor or client "
                        "actually wants. Written at the time it takes twenty "
                        "seconds; reconstructed a year later it is guesswork."},
                {"text": "Because the law requires a log", "ok": False,
                 "why": "Requirements vary and are changing. The practical "
                        "reason stands on its own: you cannot remember, and "
                        "you will be asked."},
                {"text": "To justify the cost of the tool", "ok": False,
                 "why": "A different conversation entirely. The note exists "
                        "for the data question, not for the budget one."},
            ],
        },
        {
            "q": "A bot joins your client call.",
            "remember": "Nobody consented. Stop and ask.",
            "answers": [
                {"text": "Let it run — somebody must have arranged it",
                 "ok": False,
                 "why": "Somebody arranged it for themselves. Everyone else on "
                        "the call, including the client, is being recorded "
                        "without having agreed to it."},
                {"text": "Ask whose it is and whether everyone agreed",
                 "ok": True,
                 "why": "Ten seconds, and it is a reasonable question anyone "
                        "can ask. Recording people needs their knowledge and "
                        "agreement, and a client call raises that sharply."},
                {"text": "Leave the call", "ok": False,
                 "why": "Disruptive and it does not stop the recording of "
                        "everyone else. Asking the question is more useful and "
                        "less dramatic."},
                {"text": "Carry on and mention it afterwards", "ok": False,
                 "why": "By then the recording exists and the client has been "
                        "captured. The moment to raise it is before anything "
                        "substantive is said."},
            ],
        },
    ],

    "recap": {
        "title": "Safe AI use on one screen",
        "points": [
            ("The account decides",
             "The same model is safe on a work account and unassessed on a "
             "personal one."),
            ("Two settings worth finding",
             "Training on your data, and chat history. Turn both off where you "
             "can."),
            ("Settings are not permission",
             "They reduce reuse. The paste rules do not change."),
            ("AI is already in your tools",
             "Reply suggestions, rewrite buttons, meeting bots. Mostly nobody "
             "chose them."),
            ("Keep a one-line note",
             "What for, which tool, what data, who checked it, when."),
            ("A person is always accountable",
             "You sent it, so it is yours, whatever helped you write it."),
        ],
        "oneliner": "Approved tool, work account, facts not files, and a named "
                    "person who checked the output.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("doc", "The one-line AI note",
             "Purpose, tool, data provided, who checked, date."),
            ("check", "The four conditions",
             "Approved tool, work account, facts only, human check."),
            ("eye", "The settings sweep",
             "Training off, history off, extensions you can name."),
        ],
        "links": [
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
        ],
        "next": "Companion module: SEC-07, What Never to Paste Into AI. The "
                "five red lines and the two-second test, in detail.",
    },

    "glossary": [
        ("Approved tool", "An AI service the company holds an agreement with, "
                          "used through your work account."),
        ("Consumer tier", "A free or personal subscription. Terms nobody here "
                          "negotiated, and often training on your input."),
        ("Training on your data", "Using what you type to improve the service. "
                                  "Usually switchable on business tiers."),
        ("Shadow AI", "AI tools in use at work that nobody assessed or "
                      "approved. Usually browser extensions and bots."),
        ("Audit trail", "A record of what was used, on what, by whom. Written "
                        "at the time, not reconstructed."),
        ("Accountability", "A named person owns the output, regardless of what "
                           "helped produce it."),
    ],
}
