# -*- coding: utf-8 -*-
"""DW-02 — Research with AI. Content only."""

DECK = {
    "module_code": "DW-02",
    "area": "02-ai-daily-work",
    "filename": "02-02-research-with-ai.pptx",
    "title": "Research with AI",
    "subtitle": "Using it to find the right questions fast — without letting "
                "it invent the answers.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Vikram has two hours to prepare",
        "icon": "search",
        "scenario": "Vikram sells industrial fasteners from Ahmedabad. A "
                    "meeting with a pharmaceutical client is at four. He knows "
                    "nothing about pharma cleanroom requirements and does not "
                    "know what he does not know.",
        "cost": "Two hours of reading, and still the wrong questions in the "
                "room.",
        "fix": "Ten minutes to map the subject. Then real sources for the "
               "facts.",
    },

    "outcomes": [
        ("list", "Map an unfamiliar subject in ten minutes, not two hours"),
        ("chat", "Get the questions worth asking, instead of invented answers"),
        ("search", "Know which half of research AI can do and which it cannot"),
        ("eye", "Spot a confident answer that has no source behind it"),
        ("doc", "Turn a real document into notes without reading every page"),
    ],

    "sections": [
        ("Two halves of research", "Mapping and verifying", "s_halves"),
        ("Mapping a new subject", "Ten minutes, no facts needed", "s_map"),
        ("Where facts come from", "Never from the model", "s_facts"),
        ("Reading a long document", "Grounded and safe", "s_read"),
        ("Do this now", "Map something real", "s_do"),
        ("Choose what you'd do", "A Thursday afternoon decision", "scenario"),
        ("Watch this", "A 14-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_halves",
            "label": "Two halves of research",
            "title": "Research has two halves",
            "lead": "AI is genuinely excellent at one of them and actively "
                    "dangerous at the other.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Mapping", "tone": "good",
                    "title": "AI does this well",
                    "items": [
                        "What are the main concepts here?",
                        "What questions should I be asking?",
                        "What usually goes wrong in this area?",
                        "What would an expert want to know first?",
                    ],
                },
                "right": {
                    "tag": "Verifying", "tone": "bad",
                    "title": "AI cannot do this",
                    "items": [
                        "What is the current standard number?",
                        "What did the regulator say last month?",
                        "What does this supplier actually charge?",
                        "Which of these claims is true today?",
                    ],
                },
            },
        },
        {
            "label": "Two halves of research",
            "title": "Why mapping is safe",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You ask for questions", "Not for answers, and not for "
                                              "numbers."),
                    ("It lists concepts", "Drawn from very common patterns, "
                                          "so broadly reliable."),
                    ("You recognise gaps", "\"I have never heard of that\" is "
                                           "the useful output."),
                    ("You go and verify", "With sources, in the half hour you "
                                          "just saved."),
                ],
            },
        },
        {
            "anchor": "s_map",
            "label": "Mapping a new subject",
            "title": "Ten minutes to map a subject",
            "visual": {
                "type": "prompt",
                "text": "I am meeting a customer in an industry I do not know: "
                        "pharmaceutical manufacturing. Give me three things. "
                        "One: the eight terms I will hear and what each means "
                        "in one line. Two: the five questions a buyer there "
                        "would expect a supplier to ask. Three: the three "
                        "things suppliers usually get wrong. No numbers, no "
                        "standards, no prices.",
                "caption": "\"No numbers, no standards\" is what keeps this "
                           "safe.",
                "why": [
                    "Terms and questions are stable, common knowledge.",
                    "Banning numbers removes the part it would invent.",
                    "You walk in able to ask, not pretending to know.",
                ],
            },
        },
        {
            "label": "Mapping a new subject",
            "title": "Ask for questions, not answers",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Asking for answers",
                "bad": [
                    "\"What cleanroom standard applies to this customer?\"",
                    "You get a specific standard number, stated plainly.",
                    "You repeat it in the meeting. It is the wrong one.",
                ],
                "good_tag": "Asking for questions",
                "good": [
                    "\"What should I ask this customer about their cleanroom "
                    "requirements?\"",
                    "You get six questions, three of which you would never "
                    "have thought of.",
                    "You ask them. The customer tells you the real answer.",
                ],
                "note": "The person in the room knows. Your job was to know "
                        "what to ask them.",
            },
        },
        {
            "anchor": "s_facts",
            "label": "Where facts come from",
            "title": "Facts come from sources",
            "gloss": ["Grounding"],
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "A number or rate — the official site, dated today",
                    "A standard or regulation — the published document itself",
                    "A supplier's capability — ask the supplier, in writing",
                    "A market claim — a named report you can actually open",
                ],
            },
        },
        {
            "label": "Where facts come from",
            "title": "The invented citation",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "It will produce a reference that looks perfect "
                            "and does not exist.",
                "sub": "Report titles, section numbers, author names and years "
                       "are all easy patterns to generate.",
                "cols": 2,
                "items": [
                    "A study title with a plausible year attached",
                    "A section number in a real regulation",
                    "An industry body that sounds entirely real",
                    "A statistic quoted to one decimal place",
                ],
            },
        },
        {
            "anchor": "s_read",
            "label": "Reading a long document",
            "title": "Forty pages, four minutes",
            "lead": "This is grounded research: it can only describe text you "
                    "actually gave it.",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this document prompt",
                "text": "Using only the document below, answer three "
                        "questions. What does it require us to do? What "
                        "deadlines does it set? What does it leave unclear? "
                        "Quote the exact wording for anything you say it "
                        "requires. If something is not in the document, say "
                        "\"not stated\".",
                "caption": "\"Quote the exact wording\" is the line that makes "
                           "this checkable.",
                "out_title": "What comes back",
                "out": [
                    "Three short answers with quoted phrases you can search "
                    "for in the original.",
                    "\"Not stated\" against the things you assumed were "
                    "covered.",
                    "Forty pages reduced to the six lines that affect you.",
                ],
            },
        },
        {
            "label": "Reading a long document",
            "title": "Check the document is yours to paste",
            "visual": {
                "type": "tree",
                "question": "Is this document public, or ours to keep private?",
                "yes": {
                    "path": "Public", "tone": "good", "label": "Paste it",
                    "detail": "A published circular, a standard, a public "
                              "tender, a manufacturer's datasheet. It is "
                              "already on the open internet.",
                },
                "no": {
                    "path": "Private", "tone": "bad", "label": "Do not paste",
                    "detail": "A contract, a customer's specification, an "
                              "internal policy, anything marked confidential. "
                              "Read it yourself and describe what you need.",
                },
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: map something",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick a subject you will need to sound competent in this "
                    "month.",
                    "Paste the prompt on the right with that subject in it.",
                    "Mark every term you did not already know.",
                    "Look up two of them properly, from a real source.",
                ],
                "prompt": "I need to get up to speed on [SUBJECT] for a "
                          "[MEETING / REPORT] next week. Give me: eight terms "
                          "and one-line definitions, five questions I should "
                          "ask, and three common mistakes outsiders make. No "
                          "numbers, no standards, no prices, no company names.",
                "caption": "The last sentence is what stops it inventing.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits for research",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Ask for questions before you ask for answers.",
                    "Ban numbers and citations in any mapping prompt.",
                    "Paste real documents rather than asking about them.",
                    "Verify anything you will repeat out loud in a meeting.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Repeating a statistic from an AI answer",
                     "It sounds researched, it convinces the room, and nobody "
                     "can find the source afterwards."),
                    ("Asking what a regulation says",
                     "It has never read your regulation. It describes a "
                     "regulation that sounds like it."),
                    ("Trusting a citation because it has a year on it",
                     "Titles, authors and years are extremely easy patterns to "
                     "generate convincingly."),
                    ("Pasting a customer's specification in",
                     "That is their confidential document, shared with us and "
                     "nobody else."),
                    ("Stopping once the answer sounds complete",
                     "Completeness is the default. It is not a signal that "
                     "anything was verified."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "What good research looks like",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "list", "label": "Questions first",
                     "sub": "You walk into the meeting able to ask well, not "
                            "pretending to know already."},
                    {"icon": "doc", "label": "Documents pasted",
                     "sub": "Anything it says about a public document can be "
                            "searched for in the original."},
                    {"icon": "check", "label": "Facts from sources",
                     "sub": "Every number you repeat came from a page you "
                            "opened, not a sentence it produced."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The research rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Use it to find out what to ask. Never to find out "
                            "what is true.",
                "sub": "That division makes AI the fastest research assistant "
                       "you have, and a safe one.",
                "cols": 3,
                "items": [
                    "Questions and concepts — ask it.",
                    "Numbers and rules — open the source.",
                    "Private documents — read them yourself.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Thursday, 2:00 pm",
        "situation": "A meeting with a pharmaceutical buyer is at four. You "
                     "have never sold into pharma. You have two hours and a "
                     "product catalogue.",
        "choices": [
            {
                "text": "Ask the AI what standards apply and quote them in the "
                        "meeting.",
                "tone": "bad",
                "headline": "You will be corrected in front of the buyer",
                "consequence": "It gives you a standard number that sounds "
                               "right and belongs to a different application. "
                               "You quote it at 4:15. The buyer, who works "
                               "with these daily, corrects you. Everything you "
                               "say afterwards is discounted.",
                "rule": "Never repeat a number you have not seen on a real "
                        "page.",
            },
            {
                "text": "Ask for the terms, the questions and the common "
                        "mistakes, with no numbers.",
                "tone": "good",
                "headline": "You walk in able to have the conversation",
                "consequence": "Ten minutes gives you eight terms, five buyer "
                               "questions and three supplier mistakes. You "
                               "spend the remaining time on the catalogue. At "
                               "four you ask good questions and let the buyer "
                               "supply the specifics, which is what they "
                               "expected anyway.",
                "rule": "Map the territory. Let the expert in the room fill in "
                        "the detail.",
            },
            {
                "text": "Read industry websites for two hours instead.",
                "tone": "ok",
                "headline": "Thorough, and you may still miss the point",
                "consequence": "You learn a lot, unevenly. Without knowing "
                               "which questions matter you read whatever comes "
                               "up first, and arrive with detail on one topic "
                               "and nothing on the four the buyer actually "
                               "cares about.",
                "rule": "Map first, then read. It makes the reading far more "
                        "efficient.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=ld3XMuXwLcE",
        "title": "How to Use ChatGPT’s Deep Research to Save HOURS on "
                 "Research",
        "channel": "Andy Stapleton",
        "duration": "13:59",
        "heading": "Fourteen minutes on deep research",
        "note": "Aimed at academic research. The habits transfer; our rules "
                "on what you may paste do not change.",
        "how": [
            "Optional. The mapping prompt above is the core.",
            "Useful if your tool has a deep-research mode.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which research task fits AI?",
            "remember": "Questions and concepts, never facts.",
            "answers": [
                {"text": "\"What is the current standard for this?\"",
                 "ok": False,
                 "why": "A specific, checkable fact it has no access to. You "
                        "will get a standard number that looks entirely "
                        "plausible and may belong to a different application "
                        "or a superseded version."},
                {"text": "\"What should I ask a buyer in this industry?\"",
                 "ok": True,
                 "why": "Questions are stable, general and low-risk. Even an "
                        "imperfect list makes you better prepared, and the "
                        "person in the meeting supplies the real answers."},
                {"text": "\"What does this supplier charge?\"", "ok": False,
                 "why": "It has no visibility of any supplier's pricing. Any "
                        "figure is invented, and pricing is exactly the sort "
                        "of number people repeat without checking."},
                {"text": "\"Summarise last month's regulatory update\"",
                 "ok": False,
                 "why": "Last month is after its cut-off. It will produce a "
                        "fluent summary of an update it has never seen."},
            ],
        },
        {
            "q": "Why ban numbers in a mapping prompt?",
            "remember": "Remove the part it would invent.",
            "answers": [
                {"text": "Numbers make the answer longer", "ok": False,
                 "why": "Length is not the issue. The issue is that a number "
                        "is the single most repeatable and most damaging thing "
                        "in the answer."},
                {"text": "Numbers are the part most likely to be invented",
                 "ok": True,
                 "why": "Terms and questions are broadly stable patterns. "
                        "Specific figures and standard references are not, and "
                        "they are exactly what people quote out loud "
                        "afterwards."},
                {"text": "The tool refuses to give numbers anyway", "ok": False,
                 "why": "It will give you numbers readily and confidently. "
                        "Nothing stops it, which is precisely why the "
                        "instruction has to come from you."},
                {"text": "Numbers are usually irrelevant to research",
                 "ok": False,
                 "why": "They are often the most relevant part. That is why "
                        "they must come from a real source rather than from a "
                        "sentence the tool produced."},
            ],
        },
        {
            "q": "Which document is safe to paste?",
            "remember": "Public, yes. Private, never.",
            "answers": [
                {"text": "A customer's technical specification", "ok": False,
                 "why": "Their confidential document, shared with us under an "
                        "expectation of confidence. Pasting it moves it onto a "
                        "system neither we nor they control."},
                {"text": "A published government circular", "ok": True,
                 "why": "Already public, already indexed, and nothing about "
                        "pasting it exposes anyone. This is the ideal grounded "
                        "research case."},
                {"text": "Our internal pricing policy", "ok": False,
                 "why": "Internal by definition. Even if the answer would be "
                        "useful, the policy itself is exactly what should "
                        "never leave the company."},
                {"text": "A signed contract, with names removed", "ok": False,
                 "why": "Removing names does not make commercial terms public. "
                        "Prices, penalties and obligations still belong to a "
                        "relationship, not to a chat window."},
            ],
        },
        {
            "q": "What makes a citation suspicious?",
            "remember": "You cannot open it.",
            "answers": [
                {"text": "It is more than five years old", "ok": False,
                 "why": "Age says nothing about whether a source exists. Plenty "
                        "of genuine standards and studies are decades old and "
                        "still current."},
                {"text": "You cannot find it when you search for it",
                 "ok": True,
                 "why": "That is the whole test. A real reference can be "
                        "opened in thirty seconds. An invented one has a "
                        "plausible title, a plausible author and no page "
                        "behind it."},
                {"text": "It has a very specific section number", "ok": False,
                 "why": "Real references usually do. Specificity makes an "
                        "invention more convincing, but it is not by itself "
                        "evidence either way — opening it is."},
                {"text": "The tool mentioned it without being asked",
                 "ok": False,
                 "why": "Volunteered references are no less reliable than "
                        "requested ones. Both need the same thirty-second "
                        "check before you repeat them."},
            ],
        },
        {
            "q": "What should you do before quoting?",
            "remember": "Open the page it came from.",
            "answers": [
                {"text": "Ask the tool if it is sure", "ok": False,
                 "why": "You will get confident reassurance produced exactly "
                        "the way the original claim was. Two generations are "
                        "not a check on each other."},
                {"text": "Open the actual source and read the line", "ok": True,
                 "why": "It takes under a minute and it is the only thing that "
                        "converts an answer into a fact. Anything you say out "
                        "loud in a meeting should have survived this."},
                {"text": "Check it against a second AI tool", "ok": False,
                 "why": "Better than nothing, but still two generations rather "
                        "than a source. Common patterns produce the same "
                        "convincing inventions across different tools."},
                {"text": "Rephrase it so it sounds less specific", "ok": False,
                 "why": "That hides the problem rather than solving it. A "
                        "vaguely stated invention is still an invention, and "
                        "harder for anyone else to catch."},
            ],
        },
    ],

    "recap": {
        "title": "Research with AI on one screen",
        "points": [
            ("Research has two halves",
             "Mapping a subject, and verifying facts. AI does the first well "
             "and the second never."),
            ("Ask for questions, not answers",
             "The person in the meeting knows. Your job is knowing what to ask "
             "them."),
            ("Ban numbers in mapping prompts",
             "\"No numbers, no standards, no prices\" removes what it would "
             "invent."),
            ("Paste public documents",
             "Grounded reading of a real circular is safe, fast and "
             "checkable."),
            ("Never paste private ones",
             "Contracts, customer specifications and internal policy stay "
             "where they are."),
            ("Open the source before quoting",
             "Anything you will repeat out loud has to survive a thirty-second "
             "check."),
        ],
        "oneliner": "Use it to find out what to ask. Never to find out what is "
                    "true.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("search", "The subject-mapping prompt",
             "Eight terms, five questions, three mistakes, no numbers."),
            ("doc", "The document-reading prompt",
             "Requires, deadlines, unclear — with exact wording quoted."),
            ("shield", "The public-or-private test",
             "Published document, paste it. Ours, read it yourself."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-03, Report Preparation with AI. Turning what "
                "you already know into a report somebody will actually read.",
    },

    "glossary": [
        ("Grounding", "Giving the tool the actual source text so its answer "
                      "has something real to stand on."),
        ("Citation", "A reference to a real document. AI produces convincing "
                     "ones that do not exist."),
        ("Mapping", "Learning the shape of a subject: its terms, its "
                    "questions, its usual mistakes."),
        ("Cut-off date", "The point where a model's training text stops. "
                         "Nothing after it was ever seen."),
        ("Hallucination", "A confident, invented answer. Citations and "
                          "statistics are the classic cases."),
        ("Source", "A document, system or person you can point at. A model is "
                   "never one."),
    ],
}
