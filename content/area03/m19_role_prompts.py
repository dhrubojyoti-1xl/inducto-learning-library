# -*- coding: utf-8 -*-
"""PE-03 — Role-Based Prompts. Content only."""

DECK = {
    "module_code": "PE-03",
    "area": "03-prompt-engineering",
    "filename": "03-03-role-based-prompts.pptx",
    "title": "Role-Based Prompts",
    "subtitle": "\"Act as a…\" — what it actually changes, when it helps, and "
                "when it is just decoration.",
    "duration_min": 16,
    "audience": "New joiners + staff",
    "motif": "prompt",
    "cover_image": "assets/hero-role-prompts.jpg",

    "why": {
        "title": "Meera gets an answer for engineers",
        "icon": "person",
        "scenario": "Meera runs quality checks at a Coimbatore plant. She "
                    "asks for an explanation of a rejection trend to send to "
                    "the sales team. What comes back is full of process "
                    "capability indices. Sales read two lines and call her "
                    "instead.",
        "cost": "The explanation was correct and completely unusable.",
        "fix": "One line naming the reader, and the same facts land first "
               "time.",
    },

    "outcomes": [
        ("person", "Write a role line that changes the answer, not just the "
                   "tone"),
        ("eye", "Tell a useful role from a decorative one"),
        ("chat", "Use the reader's role instead of the writer's, and see why"),
        ("list", "Ask the same question from three roles to stress-test a plan"),
        ("warn", "Avoid the roles that invite invented authority"),
    ],

    "sections": [
        ("What a role changes", "Vocabulary, depth, assumptions", "s_change"),
        ("Reader beats writer", "Who receives it matters more", "s_reader"),
        ("Roles that earn their place", "Three that work", "s_work"),
        ("Roles that do nothing", "Or worse than nothing", "s_bad"),
        ("Do this now", "Three roles, one question", "s_do"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "A 4-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_change",
            "label": "What a role changes",
            "title": "What a role actually changes",
            "lead": "It does not make the tool an expert. It shifts which "
                    "words and which level of detail become likely.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You name a role", "\"Explain this to a sales manager.\""),
                    ("Vocabulary shifts", "Fewer technical terms, more "
                                          "commercial ones."),
                    ("Depth shifts", "Less method, more consequence."),
                    ("Assumptions shift", "It stops explaining what they "
                                          "already know."),
                ],
            },
        },
        {
            "label": "What a role changes",
            "title": "The same facts, two readers",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "No role given",
                "bad": [
                    "\"Explain why rejections rose from 1.4 to 2.1 per cent.\"",
                    "You get capability indices, sampling method and a control "
                    "chart reference.",
                    "Correct, and unreadable for the person who asked.",
                ],
                "good_tag": "Reader named",
                "good": [
                    "\"Explain this to a sales manager who will talk to the "
                    "customer.\"",
                    "You get: what it means for delivery, what we are doing, "
                    "what to say.",
                    "Same facts, ordered by what the reader has to do next.",
                ],
                "note": "The role did not add knowledge. It changed which "
                        "parts of the answer came first.",
            },
        },
        {
            "anchor": "s_reader",
            "label": "Reader beats writer",
            "title": "Name the reader, not the expert",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Weaker", "tone": "neutral", "mark": "chat",
                    "title": "\"Act as a quality engineer\"",
                    "items": [
                        "Shifts vocabulary towards jargon",
                        "Adds depth nobody asked for",
                        "Does not know who will read it",
                        "Sounds authoritative about our plant",
                    ],
                },
                "right": {
                    "tag": "Stronger", "tone": "good", "mark": "check",
                    "title": "\"Write this for a sales manager\"",
                    "items": [
                        "Shifts vocabulary towards the reader",
                        "Cuts detail the reader cannot use",
                        "Orders points by what they must do",
                        "Claims no authority it does not have",
                    ],
                },
            },
        },
        {
            "label": "Reader beats writer",
            "title": "The reader line, ready to use",
            "visual": {
                "type": "prompt",
                "text": "Write this for a sales manager who will speak to the "
                        "customer this afternoon and has no technical "
                        "background. They need to know what changed, what it "
                        "means for delivery, and what we are doing about it. "
                        "Under 120 words, no jargon, three short paragraphs.",
                "caption": "Reader, purpose, then the usual instructions.",
                "why": [
                    "\"Has no technical background\" removes the jargon.",
                    "\"Will speak this afternoon\" sets the urgency and length.",
                    "The three things they need decide the three paragraphs.",
                ],
            },
        },
        {
            "anchor": "s_work",
            "label": "Roles that earn their place",
            "title": "Three roles that work",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "person", "label": "The reader",
                     "sub": "\"For a warehouse supervisor with ten minutes.\" "
                            "Sets vocabulary, length and what to leave out."},
                    {"icon": "eye", "label": "The critic",
                     "sub": "\"Read this as the customer would and list what "
                            "annoys them.\" Finds problems you cannot see."},
                    {"icon": "list", "label": "The checker",
                     "sub": "\"As an auditor, what would you ask for "
                            "evidence of?\" Produces questions, not claims."},
                ],
            },
        },
        {
            "label": "Roles that earn their place",
            "title": "The critic role, ready to use",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this critic prompt",
                "text": "Read the message below as if you are the customer "
                        "receiving it, and you are already annoyed. List the "
                        "three things most likely to irritate you, in order. "
                        "Do not rewrite it. Just list the three things.",
                "caption": "\"Do not rewrite it\" is what makes this useful.",
                "out_title": "What comes back",
                "out": [
                    "Three specific objections, usually including one you had "
                    "not considered.",
                    "No rewrite, so you keep control of the wording.",
                    "You fix two of them in a minute and ignore the third on "
                    "purpose.",
                ],
            },
        },
        {
            "anchor": "s_bad",
            "label": "Roles that do nothing",
            "title": "Roles that do nothing",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"Act as a world-class expert\"",
                     "Adds confident phrasing and no accuracy. It was always "
                     "going to sound certain."),
                    ("\"You are a lawyer\"",
                     "Produces legal-sounding text with no jurisdiction, no "
                     "date and no liability behind it."),
                    ("\"Act as our CFO\"",
                     "Invents the priorities of a person who exists and can "
                     "be quoted back at you."),
                    ("\"Pretend you have access to our data\"",
                     "It will pretend. Everything after that line is fiction "
                     "presented as record."),
                ],
            },
        },
        {
            "label": "Roles that do nothing",
            "title": "The authority trap",
            "gloss": ["Hallucination"],
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A role changes the wording. It never changes what "
                            "the tool actually knows.",
                "sub": "\"Act as a tax adviser\" produces tax-adviser "
                       "sentences, not tax advice.",
                "cols": 3,
                "items": [
                    "It gains no new facts.",
                    "It gains no jurisdiction.",
                    "It gains a more confident voice.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: three roles",
            "visual": {
                "type": "steps",
                "items": [
                    "Take a plan or proposal you are working on.",
                    "Paste it in and ask the first role question on the right.",
                    "Ask the same question again as the second role, then the "
                    "third.",
                    "Keep every objection that appears in two of the three "
                    "answers.",
                ],
                "prompt": "Read the plan below three times and answer "
                          "separately each time. First as the person who has "
                          "to do the work. Then as the person paying for it. "
                          "Then as the customer receiving the result. Each "
                          "time, list the two biggest problems you see.",
                "caption": "One prompt, three viewpoints, six objections.",
            },
        },
        {
            "label": "Do this now",
            "title": "Why three viewpoints work",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "One viewpoint",
                     "sub": "Finds the problems you already suspected."},
                    {"label": "Three viewpoints",
                     "sub": "Finds the conflicts between them."},
                    {"label": "What survives all three",
                     "sub": "That is the objection worth fixing first."},
                ],
                "note": "The value is not the tool's opinion. It is being made "
                        "to look at your own plan from a seat you were not "
                        "sitting in.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits with roles",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Name the reader before you name any expert.",
                    "Say what the reader must do next, not just who they are.",
                    "Use a role to find problems, never to grant authority.",
                    "Never role-play a real named person from the company.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Naming a role and nothing else",
                     "\"Act as a manager\" with no reader, no task and no "
                     "length changes almost nothing."),
                    ("Treating expert wording as expert judgement",
                     "It sounds more certain, which is the opposite of what "
                     "you needed."),
                    ("Role-playing a named colleague",
                     "You are inventing the views of someone who can be shown "
                     "the transcript."),
                    ("Asking a role to confirm your plan",
                     "It will agree. Ask it to attack the plan instead."),
                    ("Using a professional role for real advice",
                     "Legal, tax and medical answers need a person who carries "
                     "the liability."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "When to skip the role entirely",
            "visual": {
                "type": "tree",
                "question": "Does the reader change what should be said?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Name the reader",
                    "detail": "Explanations, proposals, escalations, training "
                              "notes. Who receives it decides the vocabulary, "
                              "the order and the length.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Skip it",
                    "detail": "Reformatting a table, shortening a paragraph, "
                              "fixing grammar. A role adds words to your "
                              "prompt and nothing to the answer.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The role rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Name who is reading it. Never claim who wrote it.",
                "sub": "The first makes the answer usable. The second makes it "
                       "sound trustworthy without being any more true.",
                "cols": 3,
                "items": [
                    "Reader named — better answer.",
                    "Critic named — better questions.",
                    "Expert claimed — false confidence.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 9:20 am",
        "situation": "Rejections rose from 1.4 to 2.1 per cent. Sales need an "
                     "explanation they can give a customer at 11. You have the "
                     "quality data and twenty minutes.",
        "choices": [
            {
                "text": "Ask it to act as a quality engineer and explain the "
                        "rise.",
                "tone": "ok",
                "headline": "Technically excellent, practically useless",
                "consequence": "You get capability indices, a sampling note "
                               "and a control chart reference. All of it is "
                               "reasonable and none of it can be said to a "
                               "customer at 11 am. Sales ring you anyway, and "
                               "you explain it verbally.",
                "rule": "An expert role writes for experts. Your reader was "
                        "not one.",
            },
            {
                "text": "Ask it to write for a sales manager with no technical "
                        "background.",
                "tone": "good",
                "headline": "Same facts, in the order sales needed them",
                "consequence": "You get three short paragraphs: what changed, "
                               "what it means for their delivery, what we are "
                               "doing about it. Sales use it almost verbatim "
                               "at 11, and nobody has to ring you.",
                "rule": "Name the reader and what they must do next.",
            },
            {
                "text": "Ask it to act as your quality head and issue the "
                        "explanation.",
                "tone": "bad",
                "headline": "You put words in a real person's mouth",
                "consequence": "The text reads like an official position from "
                               "a named colleague who has not seen it. If it "
                               "reaches the customer, they will quote your "
                               "quality head on a cause nobody has confirmed.",
                "rule": "Never role-play a real person who can be quoted back "
                        "at you.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=Gd2N8bCKO98",
        "title": "Role and Persona-Based Prompting",
        "channel": "AppDirect",
        "duration": "3:49",
        "heading": "Four minutes on role prompts",
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
            "q": "What does a role actually change?",
            "remember": "Wording and depth. Never knowledge.",
            "answers": [
                {"text": "What the tool knows about the subject", "ok": False,
                 "why": "Nothing changes about what it knows. The same "
                        "patterns are there before and after the role line — "
                        "only which ones become likely has shifted."},
                {"text": "The vocabulary, the depth and what it assumes",
                 "ok": True,
                 "why": "That is exactly it. A role makes certain words and a "
                        "certain level of detail more likely, and stops it "
                        "explaining things that reader would already know."},
                {"text": "How accurate the answer is", "ok": False,
                 "why": "Accuracy is unaffected. \"Act as an expert\" produces "
                        "more confident phrasing around exactly the same "
                        "reliability, which is a worse position, not a better "
                        "one."},
                {"text": "Whether it can access your systems", "ok": False,
                 "why": "No role grants access to anything. \"Pretend you can "
                        "see our data\" produces pretending, presented in the "
                        "same tone as fact."},
            ],
        },
        {
            "q": "Which role line is strongest?",
            "remember": "Name the reader and what they must do.",
            "answers": [
                {"text": "\"Act as a world-class consultant\"", "ok": False,
                 "why": "Pure decoration. It adds assured phrasing and nothing "
                        "else, and assurance is the last thing an unverified "
                        "answer needs more of."},
                {"text": "\"Write for a supervisor who has ten minutes\"",
                 "ok": True,
                 "why": "It sets vocabulary, length, depth and priority all at "
                        "once, and every one of those is checkable by you when "
                        "the answer arrives."},
                {"text": "\"You are an experienced quality engineer\"",
                 "ok": False,
                 "why": "Better than nothing, but it aims the answer at "
                        "experts. If your reader is not one, you have made the "
                        "text harder to use."},
                {"text": "\"Act as our operations director\"", "ok": False,
                 "why": "This invents the views of a real person. Anything it "
                        "produces can be quoted back as their position, and "
                        "they have never seen it."},
            ],
        },
        {
            "q": "What is the critic role for?",
            "remember": "Finding objections, not writing text.",
            "answers": [
                {"text": "Rewriting your draft more sharply", "ok": False,
                 "why": "That is a different job, and mixing them loses you "
                        "control. Ask for the objections, decide which matter, "
                        "then fix the wording yourself."},
                {"text": "Listing what a hostile reader would object to",
                 "ok": True,
                 "why": "It puts you in a seat you were not sitting in. Add "
                        "\"do not rewrite it\" so you get a list you can act "
                        "on rather than a version you have to review."},
                {"text": "Confirming your plan is sound", "ok": False,
                 "why": "It will confirm almost anything you seem to want. "
                        "Agreement from a tool is not evidence, and asking for "
                        "it wastes the one genuinely useful move here."},
                {"text": "Checking your facts are correct", "ok": False,
                 "why": "It cannot check facts. A critic role finds weaknesses "
                        "in argument and tone, which is real value, but "
                        "verification still needs the source."},
            ],
        },
        {
            "q": "When should you skip the role?",
            "remember": "If the reader does not change the content, skip it.",
            "answers": [
                {"text": "When the task is short", "ok": False,
                 "why": "Length is not the test. A two-line escalation still "
                        "changes completely depending on whether it goes to a "
                        "supplier or to your own director."},
                {"text": "When you are reformatting or fixing grammar",
                 "ok": True,
                 "why": "There is no reader-dependent judgement in turning a "
                        "list into a table. A role adds words to your prompt "
                        "and nothing to the result."},
                {"text": "When you are in a hurry", "ok": False,
                 "why": "Being in a hurry is when it helps most. One clause "
                        "naming the reader saves you the rewrite you would "
                        "otherwise do afterwards."},
                {"text": "When the answer will go to a customer", "ok": False,
                 "why": "That is precisely when to name the reader. A customer "
                        "audience changes vocabulary, length and what you must "
                        "not say."},
            ],
        },
        {
            "q": "Why not role-play a colleague?",
            "remember": "Never invent the views of a real person.",
            "answers": [
                {"text": "The tool refuses to do it", "ok": False,
                 "why": "It will usually do it without hesitation. That is the "
                        "problem — nothing stops you, so the judgement has to "
                        "be yours."},
                {"text": "It invents a real person's position", "ok": True,
                 "why": "The output reads like their view, can be forwarded as "
                        "their view, and they have never seen it. That is a "
                        "genuinely difficult conversation to have afterwards."},
                {"text": "It produces worse writing", "ok": False,
                 "why": "The writing is often perfectly good. The problem is "
                        "not quality, it is that the words are attributed to "
                        "someone who did not say them."},
                {"text": "It is slower than other roles", "ok": False,
                 "why": "Speed is identical. The objection is entirely about "
                        "attributing an invented position to a named "
                        "colleague."},
            ],
        },
    ],

    "recap": {
        "title": "Role prompts on one screen",
        "points": [
            ("A role shifts words, not knowledge",
             "Vocabulary, depth and assumptions change. What it knows does "
             "not."),
            ("Name the reader first",
             "Who receives it decides the language, the order and the length."),
            ("Say what they must do next",
             "\"Will speak to the customer at 11\" sets urgency and shape in "
             "one clause."),
            ("Use roles to attack, not to agree",
             "\"List what annoys you about this\" is worth far more than "
             "approval."),
            ("Three seats beat one",
             "Ask as doer, payer and receiver. Fix whatever appears in two of "
             "three."),
            ("Never impersonate a colleague",
             "You would be inventing the position of someone who can read the "
             "transcript."),
        ],
        "oneliner": "Name who is reading it. Never claim who wrote it.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("person", "The reader line",
             "Who they are, what they lack, what they must do next."),
            ("eye", "The critic prompt",
             "Three objections, in order, and no rewriting."),
            ("list", "The three-seats prompt",
             "Doer, payer, receiver. Two problems each."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-04, Examples & Structured Prompts. Showing "
                "one good example beats three paragraphs describing what good "
                "looks like.",
    },

    "glossary": [
        ("Role prompt", "A line naming who the answer is written by or for, "
                        "which shifts vocabulary and depth."),
        ("Persona", "Another word for the role you give the tool. It changes "
                    "style, never knowledge."),
        ("Context", "The background you give so the tool knows the situation "
                    "it is writing about."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Hallucination", "A confident, invented answer. A role makes these "
                          "sound more authoritative, not less likely."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
