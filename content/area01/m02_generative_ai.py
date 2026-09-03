# -*- coding: utf-8 -*-
"""AI-02 — Generative AI. Content only."""

DECK = {
    "module_code": "AI-02",
    "area": "01-ai-general",
    "filename": "01-02-generative-ai.pptx",
    "title": "Generative AI",
    "subtitle": "What it actually makes, why every answer is different, and "
                "where it beats a search box.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "network",
    "cover_image": "assets/hero-generative-ai.jpg",

    "why": {
        "title": "Shalini sends a line she never wrote",
        "icon": "warn",
        "scenario": "Shalini runs marketing for a Pune plant. She asks an AI "
                    "tool for a team note about a moved meeting. The note is "
                    "excellent. It also mentions a quarterly bonus review that "
                    "nobody has scheduled. Two people email HR about it.",
        "cost": "An afternoon spent explaining a sentence she did not write.",
        "fix": "You will know why it does that, and how to catch it in "
               "four seconds.",
    },

    "outcomes": [
        ("bulb", "Explain what \"generative\" means without using the word"),
        ("cycle", "Say why the same question gives two colleagues two answers"),
        ("search", "Choose between a search box and a generator, first time"),
        ("doc", "Get three usable versions of a message from one set of facts"),
        ("eye", "Spot an invented line in a draft before you send it"),
    ],

    "sections": [
        ("What generative means", "It builds, it does not fetch", "s_gen"),
        ("What it can make", "Text, structure, shorter versions, options", "s_makes"),
        ("Why answers change", "The same question, two answers", "s_vary"),
        ("Search box or generator?", "Pick the right one first time", "s_pick"),
        ("Do this now", "Make something in two minutes", "s_do"),
        ("Choose what you'd do", "A Wednesday morning decision", "scenario"),
        ("Watch this", "An 8-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_gen",
            "label": "What generative means",
            "title": "It builds. It does not fetch.",
            "lead": "There is no file it is copying from. Every sentence is "
                    "assembled the moment you ask for it.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You describe it", "In plain sentences, with your own "
                                        "facts in them."),
                    ("It builds", "Each word chosen to fit the words before it."),
                    ("Nothing is copied", "There is no stored answer being "
                                          "handed back to you."),
                    ("You get something new", "Text that did not exist a "
                                              "second earlier."),
                ],
            },
        },
        {
            "label": "What generative means",
            "title": "A generator is not a database",
            "gloss": ["Generative AI"],
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "A search index",
                     "sub": "Stores pages. Returns the ones that match."},
                    {"label": "A generative model",
                     "sub": "Stores patterns. Builds a fresh answer every time."},
                    {"label": "What that means for you",
                     "sub": "Never quote it. Always read it."},
                ],
                "note": "This is why two colleagues asking the same question "
                        "get different wording. Neither answer was retrieved. "
                        "Both were made.",
            },
        },
        {
            "anchor": "s_makes",
            "label": "What it can make",
            "title": "Four things it makes well",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Text — emails, SOP drafts, replies to a complaint",
                    "Structure — a messy list turned into a clean table",
                    "Shorter versions — twelve pages into six bullets",
                    "Options — ten subject lines, five ways to say no",
                ],
            },
        },
        {
            "label": "What it can make",
            "title": "It makes more than text",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "eye", "label": "Images and slides",
                     "sub": "Fine for a rough internal draft. Risky for "
                            "anything a customer will actually see."},
                    {"icon": "sheet", "label": "Formulas and code",
                     "sub": "Excel formulas, small scripts. Always test one "
                            "row before you trust the column."},
                    {"icon": "chat", "label": "Translation",
                     "sub": "Hindi to English, English to Arabic. Good for "
                            "the gist, never for a contract."},
                ],
            },
        },
        {
            "anchor": "s_vary",
            "label": "Why answers change",
            "title": "Same words, different answer",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "A search box", "tone": "neutral", "mark": "search",
                    "title": "Same words, same result",
                    "items": [
                        "Everyone gets the same ten links",
                        "Run it tomorrow and get the same list",
                        "You can cite the page you found",
                        "The result is a place, not a sentence",
                    ],
                },
                "right": {
                    "tag": "A generator", "tone": "accent", "mark": "chat",
                    "title": "Same words, new answer",
                    "items": [
                        "The wording differs every single time",
                        "Two colleagues get two versions",
                        "There is no page you could cite",
                        "The result is text, made only for you",
                    ],
                },
            },
        },
        {
            "label": "Why answers change",
            "title": "Turn that into an advantage",
            "lead": "Variation is a problem when you did not ask for it, and a "
                    "gift when you did.",
            "visual": {
                "type": "prompt",
                "text": "Give me three versions of this message: one formal, "
                        "one friendly, one very short. Message: our delivery "
                        "to the Sharjah site will now arrive on Thursday "
                        "instead of Tuesday, because of a customs hold.",
                "caption": "Three versions cost you the same as one.",
                "why": [
                    "You pick a tone instead of arguing with the tool.",
                    "Seeing three side by side makes the choice obvious.",
                    "The facts stay identical across all three.",
                ],
            },
        },
        {
            "anchor": "s_pick",
            "label": "Search box or generator?",
            "title": "Which one do I need?",
            "visual": {
                "type": "tree",
                "question": "Will anyone ask me where this came from?",
                "yes": {
                    "path": "Yes", "tone": "neutral", "label": "Use search",
                    "detail": "A duty rate, a rule, a specification, a news "
                              "report. If you will have to show the source, "
                              "you need the actual page.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Use the generator",
                    "detail": "A reply, a summary, a first draft, a set of "
                              "options. You already hold the facts and you "
                              "need them turned into sentences.",
                },
            },
        },
        {
            "label": "Search box or generator?",
            "title": "Gaps get filled, never flagged",
            "gloss": ["Hallucination"],
            "visual": {
                "type": "bandlist",
                "headline": "A missing detail does not produce a blank. It "
                            "produces something plausible.",
                "sub": "The tool has no way to leave a hole in a sentence, so "
                       "it closes it.",
                "cols": 2,
                "items": [
                    "Names of people, products and places you never supplied",
                    "Figures and dates that look exactly right",
                    "Quotes and references that exist nowhere",
                    "Policies it assumes a company like ours must have",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: make something",
            "visual": {
                "type": "steps",
                "items": [
                    "Open your approved assistant.",
                    "Think of one message you owe somebody today.",
                    "Paste the prompt on the right and press Enter.",
                    "Read it once, change one detail, and send it.",
                ],
                "prompt": "Write a short internal note telling the team that "
                          "the Friday review has moved from 11 am to 3 pm, and "
                          "that the monthly numbers are still due on Thursday "
                          "evening. Under 70 words. Friendly but clear.",
                "caption": "Works as written. Swap in your own meeting "
                           "afterwards.",
            },
        },
        {
            "label": "Do this now",
            "title": "The four seconds that matter",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Sent unread",
                "bad": [
                    "The note reads beautifully and mentions a \"quarterly "
                    "bonus review\" nobody has scheduled.",
                    "Two people email HR about the bonus that afternoon.",
                    "You spend an hour explaining a sentence you did not "
                    "write.",
                ],
                "good_tag": "Read once, then sent",
                "good": [
                    "The same note, read through once before sending.",
                    "You spot the invented line and delete it in four seconds.",
                    "Nobody ever knows it was there.",
                ],
                "note": "Generated text is a first draft with your name at the "
                        "bottom. Reading it once is the whole job.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits with generated text",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Read every line before it leaves you. Every line.",
                    "Delete anything you did not supply and cannot check.",
                    "Never present it as a quote, a source or a policy.",
                    "Save the prompt that produced a genuinely good result.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Sending the first version unread",
                     "Invented meetings, bonuses and policies reach the team "
                     "with your name on them."),
                    ("Asking it to \"find\" something",
                     "It does not search. It produces text that resembles a "
                     "finding."),
                    ("Trusting a precise-looking number",
                     "A figure quoted to one decimal place is the most "
                     "convincing kind of invention."),
                    ("Putting generated images in front of customers",
                     "Almost-words and wrong details are obvious, and they "
                     "read as carelessness."),
                    ("Asking again to check the first answer",
                     "You get a second generated answer, not a check on the "
                     "first one."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Where it genuinely earns its keep",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "First drafts",
                     "sub": "A blank page becomes 200 words you can edit. This "
                            "alone saves hours in a week."},
                    {"icon": "sheet", "label": "Changing shape",
                     "sub": "Long into short. A list into a table. Formal into "
                            "plain. Hindi into English."},
                    {"icon": "bulb", "label": "Options on demand",
                     "sub": "Ten ideas in twenty seconds. You are choosing "
                            "rather than inventing."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The one habit that matters",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "mark": "ban",
                "headline": "If you did not supply it and cannot check it, "
                            "take it out.",
                "sub": "That one rule removes almost every problem generated "
                       "text can cause you.",
                "cols": 3,
                "items": [
                    "Names you never typed",
                    "Numbers you cannot trace",
                    "Rules nobody has confirmed",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Wednesday, 11:05 am",
        "situation": "A customer in Abu Dhabi asks in writing what your "
                     "standard warranty period is. You are fairly sure it is "
                     "12 months, but you have not actually checked.",
        "choices": [
            {
                "text": "Ask the assistant what a standard warranty period "
                        "usually is, and quote that.",
                "tone": "bad",
                "headline": "You just invented company policy",
                "consequence": "It answers \"12 months\", because that is the "
                               "common pattern. Three months later a claim "
                               "arrives quoting your email. The contract says "
                               "six months for that product line, and the "
                               "customer has your written confirmation.",
                "rule": "Never let a generated pattern stand in for a policy "
                        "nobody has checked.",
            },
            {
                "text": "Open the contract, confirm the period, then ask the "
                        "tool to word the reply.",
                "tone": "good",
                "headline": "Thirty seconds checking, twenty seconds writing",
                "consequence": "The contract says six months for that line. "
                               "You hand the tool the number and the tone, and "
                               "it writes a clear two-line reply. The fact "
                               "came from the contract. The sentences came "
                               "from the tool. Nothing was guessed.",
                "rule": "Facts from the file. Wording from the tool.",
            },
            {
                "text": "Reply that you will confirm and come back tomorrow.",
                "tone": "ok",
                "headline": "Safe, but slower than it needed to be",
                "consequence": "Nothing goes wrong. The customer waits a day "
                               "for a number that was two clicks away in the "
                               "contract, and sends a chaser in the morning. "
                               "Being careful and being slow are not the same "
                               "thing.",
                "rule": "Check the fact now. It is usually faster than "
                        "promising to check it later.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=hfIUstzHs9A",
        "title": "What are Generative AI models?",
        "channel": "IBM Technology",
        "duration": "8:47",
        "heading": "Nine minutes on how it builds",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Watch it if you want the mechanism, not just the rule.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Why are the answers different?",
            "stem": "You and a colleague type the same question into the same "
                    "tool a minute apart, and get different wording back.",
            "remember": "Nothing is retrieved. Everything is built.",
            "answers": [
                {"text": "One of you made a typing mistake", "ok": False,
                 "why": "Not needed. Even a character-perfect repeat gives "
                        "different wording, because the answer is built fresh "
                        "rather than looked up. Identical input does not mean "
                        "identical output here."},
                {"text": "It builds a new answer every time", "ok": True,
                 "why": "Exactly. There is no stored answer to hand back. It "
                        "constructs text word by word, and tiny differences "
                        "compound. This is why you can never cite it and never "
                        "assume a colleague saw what you saw."},
                {"text": "The tool learned something in that minute",
                 "ok": False,
                 "why": "It did not. The model does not update between your "
                        "question and your colleague's. What changed is the "
                        "generation, not the model's knowledge."},
                {"text": "One of you is on a paid account", "ok": False,
                 "why": "Account tier changes speed and limits, not this. Two "
                        "people on identical paid accounts still get different "
                        "wording a minute apart."},
            ],
        },
        {
            "q": "Which job suits a generator best?",
            "remember": "You bring the facts. It brings the sentences.",
            "answers": [
                {"text": "\"Find the current customs duty on this part\"",
                 "ok": False,
                 "why": "It cannot look anything up. It will produce a duty "
                        "figure shaped exactly like a real one, and you will "
                        "have no way to tell. Use the official schedule."},
                {"text": "\"Turn these five bullets into a 150-word note\"",
                 "ok": True,
                 "why": "The facts are already yours. The tool only supplies "
                        "sentences, and you can check every line against your "
                        "own bullets in well under a minute."},
                {"text": "\"Tell me what our refund policy says\"", "ok": False,
                 "why": "It has never seen your policy. Rather than say so, it "
                        "will describe a refund policy that sounds entirely "
                        "reasonable and is not yours."},
                {"text": "\"Confirm whether this invoice was paid\"",
                 "ok": False,
                 "why": "It has no connection to your accounts system. This is "
                        "a question for the ledger, and no amount of good "
                        "prompting changes that."},
            ],
        },
        {
            "q": "There is a line you did not write.",
            "stem": "Your generated note refers to a \"quarterly bonus "
                    "review\". Nobody has scheduled one.",
            "remember": "If you did not supply it, take it out.",
            "answers": [
                {"text": "Leave it — it might be planned", "ok": False,
                 "why": "It is not planned; it was invented to close a gap in "
                        "a sentence. Leaving it in means your team hears about "
                        "a bonus review from you. That is a very hard sentence "
                        "to walk back."},
                {"text": "Delete it before sending", "ok": True,
                 "why": "Right, and it takes four seconds. Anything in a draft "
                        "that you did not supply and cannot confirm comes out "
                        "before the message leaves you."},
                {"text": "Ask the tool whether it is true", "ok": False,
                 "why": "It will generate an answer about its own answer, with "
                        "the same confidence and no more evidence. A second "
                        "generation is not a check on the first."},
                {"text": "Send it and correct it later", "ok": False,
                 "why": "By then it has been read, forwarded and believed. "
                        "Corrections travel far less widely than the original, "
                        "and the original had your name on it."},
            ],
        },
        {
            "q": "Where should generated images not go?",
            "remember": "Drafts internally. Never in front of a customer.",
            "answers": [
                {"text": "An internal brainstorming deck", "ok": False,
                 "why": "That is a reasonable place for them. Rough visuals "
                        "help people react to an idea, and everyone in the "
                        "room knows they are drafts."},
                {"text": "A proposal a customer will read", "ok": True,
                 "why": "Generated images carry small errors — text that is "
                        "almost words, details that are nearly right. In a "
                        "customer document they read as carelessness about "
                        "everything else too."},
                {"text": "A personal note to yourself", "ok": False,
                 "why": "Harmless. Nobody else sees it and nothing depends on "
                        "it being accurate."},
                {"text": "An early draft for your manager", "ok": False,
                 "why": "Fine, as long as you say what it is. A manager "
                        "reviewing a draft expects rough visuals in it."},
            ],
        },
        {
            "q": "What can you honestly call it?",
            "remember": "It is your draft. Never a source.",
            "answers": [
                {"text": "A source, as long as you name the tool", "ok": False,
                 "why": "Naming the tool does not make it a source. There is "
                        "no page, no author and no date behind the sentence — "
                        "it was built for you and for nobody else."},
                {"text": "Your draft, which you checked", "ok": True,
                 "why": "That is the honest description and the safe one. You "
                        "wrote the message using a tool, and you stand behind "
                        "every line because you read every line."},
                {"text": "A summary of general industry opinion", "ok": False,
                 "why": "It is not a survey of anything. Calling it industry "
                        "opinion invents a second layer of authority on top of "
                        "an answer that already had none."},
                {"text": "A starting point you can cite internally",
                 "ok": False,
                 "why": "Even internally, \"the AI said\" is not something a "
                        "colleague can act on or defend. Find the real source, "
                        "or present the point as your own judgement."},
            ],
        },
    ],

    "recap": {
        "title": "Generative AI on one screen",
        "points": [
            ("It builds, it does not fetch",
             "Every answer is constructed fresh. There is no page behind it."),
            ("Different every time",
             "Two colleagues asking the same thing get two answers. Neither is "
             "the record."),
            ("Gaps get filled, not flagged",
             "A missing fact produces a plausible invention, never a blank "
             "space."),
            ("Strong on shape, weak on truth",
             "Drafting, shortening, restructuring, options. Not lookups, not "
             "policy, not figures."),
            ("Read every line",
             "Anything you did not supply and cannot verify comes out before "
             "you send."),
            ("Never a source",
             "It is your draft, that you checked. That is the only honest "
             "description of it."),
        ],
        "oneliner": "Generative means it makes something new every time. That "
                    "is the power and the whole risk, in one sentence.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The three-versions prompt",
             "Formal, friendly and very short, from one set of facts."),
            ("doc", "The internal-note prompt",
             "Two changes, seventy words, friendly but clear."),
            ("eye", "The read-before-send check",
             "Delete anything you did not supply and cannot verify."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: AI-03, AI Capabilities. It maps the tasks where "
                "these tools genuinely save you an hour, and the ones where "
                "they quietly cost you one.",
    },

    "glossary": [
        ("Generative AI", "A system that builds new text, images or code "
                          "rather than retrieving something that already "
                          "exists."),
        ("Model", "The trained system behind the app. ChatGPT, Copilot and "
                  "Gemini are apps built around models."),
        ("Prompt", "Everything you type in: the request plus the facts you "
                   "choose to supply."),
        ("Hallucination", "A confident, invented answer. Usually a name, a "
                          "number, a date or a policy."),
        ("Training data", "The public text a model learned from, up to a fixed "
                          "cut-off date."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
