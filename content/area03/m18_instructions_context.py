# -*- coding: utf-8 -*-
"""PE-02 — Instructions & Context. Content only."""

DECK = {
    "module_code": "PE-02",
    "area": "03-prompt-engineering",
    "filename": "03-02-instructions-and-context.pptx",
    "title": "Instructions & Context",
    "subtitle": "How much background to give — and the point where adding more "
                "starts making the answer worse.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "prompt",

    "why": {
        "title": "Nikhil gets a plan for someone else",
        "icon": "doc",
        "scenario": "Nikhil coordinates projects for a Hyderabad office. He "
                    "asks for \"a project plan for a warehouse fit-out\". He "
                    "gets a polished twelve-week plan, with roles the company "
                    "does not have, for a country it does not operate in.",
        "cost": "Forty minutes deleting somebody else's assumptions.",
        "fix": "Four lines of context, and the plan describes your project.",
    },

    "outcomes": [
        ("list", "Write the four context lines from memory, every time"),
        ("chat", "Tell an instruction apart from a piece of context"),
        ("ban", "Use negative instructions to stop the three usual habits"),
        ("eye", "Recognise when extra context is making the answer worse"),
        ("cycle", "Rewrite a weak prompt into a specific one in 30 seconds"),
    ],

    "sections": [
        ("The four context lines", "Who, what, where, why", "s_four"),
        ("Instruction or context?", "Two different jobs", "s_vs"),
        ("Saying what not to do", "The three usual habits", "s_not"),
        ("How much is too much", "Where it starts to hurt", "s_much"),
        ("Do this now", "Rewrite one real prompt", "s_do"),
        ("Choose what you'd do", "A Thursday afternoon decision", "scenario"),
        ("Watch this", "A 6-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_four",
            "label": "The four context lines",
            "title": "Four lines it cannot guess",
            "lead": "Without these it invents a company, a reader and a "
                    "situation. All three will be wrong.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "WHO IS READING — \"a client who is already annoyed with "
                    "us\"",
                    "WHAT WE DO — \"we run bonded warehousing in Bhiwandi\"",
                    "WHERE — \"India, so rupees and Indian labour rules\"",
                    "WHY NOW — \"they escalated to my director this morning\"",
                ],
            },
        },
        {
            "label": "The four context lines",
            "title": "What each line prevents",
            "visual": {
                "type": "flow",
                "steps": [
                    ("No reader", "It writes for a general audience and "
                                  "pleases nobody."),
                    ("No business", "It assumes an industry, usually American "
                                    "software."),
                    ("No place", "You get dollars, US law and the wrong "
                                 "holidays."),
                    ("No urgency", "It writes a leisurely note when you needed "
                                   "three lines."),
                ],
            },
        },
        {
            "anchor": "s_vs",
            "label": "Instruction or context?",
            "title": "Instruction or context?",
            "gloss": ["Context"],
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Context", "tone": "neutral", "mark": "list",
                    "title": "Facts about the situation",
                    "items": [
                        "\"The client is in Sharjah\"",
                        "\"This is the third delay this quarter\"",
                        "\"We cannot offer a discount\"",
                        "\"Our contact there is new to the account\"",
                    ],
                },
                "right": {
                    "tag": "Instruction", "tone": "accent", "mark": "chat",
                    "title": "What to do with them",
                    "items": [
                        "\"Write a reply email\"",
                        "\"Under 120 words\"",
                        "\"Apologetic but do not accept liability\"",
                        "\"End with a question, not a statement\"",
                    ],
                },
            },
        },
        {
            "label": "Instruction or context?",
            "title": "Both, in one paragraph",
            "visual": {
                "type": "prompt",
                "text": "Write a reply email to a client in Sharjah. Context: "
                        "this is the third delay this quarter, our contact "
                        "there is new to the account, and we cannot offer a "
                        "discount. Instructions: under 120 words, apologetic "
                        "without accepting liability, end with a question "
                        "rather than a statement.",
                "caption": "Context first, instructions second. It works as "
                           "written.",
                "why": [
                    "The two words \"Context\" and \"Instructions\" do real "
                    "work.",
                    "Nothing about the situation is left for it to invent.",
                    "You can check each line of the reply against your own "
                    "text.",
                ],
            },
        },
        {
            "anchor": "s_not",
            "label": "Saying what not to do",
            "title": "Say what not to do",
            "lead": "Three habits show up in almost every AI draft. One line "
                    "each removes them.",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("The throat-clearing opener",
                     "\"I hope this email finds you well.\" Add: no opening "
                     "pleasantries, start with the point."),
                    ("The apology for everything",
                     "\"We sincerely apologise for any inconvenience.\" Add: "
                     "one apology only, and be specific."),
                    ("The summary of your own question",
                     "\"You asked me to write about...\" Add: no preamble, no "
                     "restating the request."),
                ],
            },
        },
        {
            "label": "Saying what not to do",
            "title": "The three lines to reuse",
            "visual": {
                "type": "prompt_out",
                "header": "Copy these three lines",
                "text": "Do not open with pleasantries — start with the point. "
                        "Do not restate my request back to me. Use one "
                        "apology at most, and make it specific rather than "
                        "general.",
                "caption": "Paste these under any writing prompt, every time.",
                "out_title": "What changes",
                "out": [
                    "The email starts with the actual news instead of a line "
                    "about hoping you are well.",
                    "Roughly forty words disappear, and none of them were "
                    "carrying meaning.",
                    "It reads like a person wrote it in a hurry, which is "
                    "usually what you want.",
                ],
            },
        },
        {
            "anchor": "s_much",
            "label": "How much is too much",
            "title": "Where extra context hurts",
            "visual": {
                "type": "tree",
                "question": "Would a new colleague need this to do the task?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Include it",
                    "detail": "If a capable new joiner could not write the "
                              "email without knowing it, the tool cannot "
                              "either. That is the whole test.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Leave it out",
                    "detail": "Extra background dilutes the instruction. The "
                              "tool starts weighing detail you did not care "
                              "about, and the reply drifts away from the "
                              "point.",
                },
            },
        },
        {
            "label": "How much is too much",
            "title": "Too little, right, too much",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Too little",
                "bad": [
                    "\"Write a reply about the delay.\"",
                    "You get a general apology letter with no dates and no "
                    "position.",
                    "Everything that mattered was left for it to invent.",
                ],
                "good_tag": "Too much",
                "good": [
                    "Four paragraphs of company history, then the request.",
                    "You get a reply that mentions the history and buries the "
                    "new date.",
                    "It weighted what you spent the most words on.",
                ],
                "note": "It reads emphasis from volume. Whatever you write "
                        "most about is what the answer will be about.",
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: rewrite one prompt",
            "visual": {
                "type": "steps",
                "items": [
                    "Think of a message you sent an AI tool this week that "
                    "disappointed you.",
                    "Write the four context lines for it: reader, business, "
                    "place, urgency.",
                    "Add your instructions: length, tone, format, and what not "
                    "to do.",
                    "Run it again and compare the two answers side by side.",
                ],
                "prompt": "Context: you are writing for me, a project "
                          "coordinator at an Indian logistics company. The "
                          "reader is a site contractor who has missed two "
                          "deadlines. Instructions: write a firm progress-"
                          "chasing email, under 100 words, no pleasantries, "
                          "end with a specific date request.",
                "caption": "Swap in your own reader and business. The shape "
                           "stays identical.",
            },
        },
        {
            "label": "Do this now",
            "title": "Context you should never add",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Context makes answers better. Some context makes "
                            "the company liable.",
                "sub": "Everything here can be described without identifying "
                       "anyone.",
                "cols": 2,
                "items": [
                    "The client's name, address or phone number",
                    "Prices, margins or wording lifted from a contract",
                    "A colleague's name attached to pay or performance",
                    "Anything marked internal, confidential or restricted",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth keeping",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Label your two blocks: \"Context:\" then \"Instructions:\"",
                    "Describe the reader in one clause, never in a paragraph.",
                    "Keep the three do-not lines pasted at the end.",
                    "Cut any background a new colleague would not need.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Giving the task but never the reader",
                     "The tool writes for nobody in particular, which reads as "
                     "a form letter to everybody."),
                    ("Assuming it knows the country",
                     "Without a location you get dollars, US holidays and the "
                     "wrong labour rules."),
                    ("Pasting the whole email thread for context",
                     "You have now shared every name and address in it, to "
                     "improve one paragraph."),
                    ("Writing context as one long story",
                     "It weights by volume. The longest part of your prompt "
                     "becomes the point of the answer."),
                    ("Never saying what to avoid",
                     "The pleasantries, the preamble and the triple apology "
                     "come back every single time."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "What good context looks like",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "person", "label": "One clause per fact",
                     "sub": "\"A new contact, already annoyed, in Sharjah.\" "
                            "Three facts, eight words, no names."},
                    {"icon": "clock", "label": "Front-loaded",
                     "sub": "Context first, instructions last. The final "
                            "instruction is the one it follows hardest."},
                    {"icon": "ban", "label": "Explicitly bounded",
                     "sub": "What to avoid is as useful as what to do, and "
                            "far more reliable than hoping."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The context rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Give it what a new colleague would need, and "
                            "nothing a new colleague would not.",
                "sub": "That single test settles both halves of the question.",
                "cols": 3,
                "items": [
                    "They would need it — include it.",
                    "They would not — cut it.",
                    "They must not see it — never type it.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Thursday, 2:30 pm",
        "situation": "A contractor has missed two deadlines. Your director "
                     "wants a firm email sent today. You have the dates, the "
                     "contract terms and thirty seconds to think.",
        "choices": [
            {
                "text": "Paste the whole email thread in and ask for a firm "
                        "reply.",
                "tone": "bad",
                "headline": "It works, and it costs more than you saved",
                "consequence": "The reply is good, because the thread carried "
                               "the context. It also carried the contractor's "
                               "name, phone number, site address and your "
                               "director's comments about them. All of that "
                               "left the company to save you two minutes of "
                               "typing.",
                "rule": "Describe the situation. Never forward the thread.",
            },
            {
                "text": "Write four context lines and three instructions, with "
                        "no names.",
                "tone": "good",
                "headline": "Two minutes, and nothing left the building",
                "consequence": "\"A site contractor, two missed deadlines, "
                               "eight and fifteen days late, no discount "
                               "available, escalated internally today.\" The "
                               "email that comes back is firm, specific and "
                               "carries no identifying detail at all.",
                "rule": "Context is facts about the situation, not the "
                        "documents it came from.",
            },
            {
                "text": "Type \"write a firm email chasing a late contractor\" "
                        "and edit the result.",
                "tone": "ok",
                "headline": "Safe, but you will do the work anyway",
                "consequence": "You get a generic chaser with no dates, no "
                               "position on the discount and no deadline. "
                               "Editing it into something sendable takes "
                               "longer than writing the four context lines "
                               "would have.",
                "rule": "The context you skip is the work you do afterwards.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=LrclePP0KRk",
        "title": "Your AI Prompt is Missing These 3 Things (ChatGPT & "
                 "Gemini)",
        "channel": "Simpletivity",
        "duration": "5:54",
        "heading": "Six minutes on what is missing",
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
            "q": "Which of these is context?",
            "remember": "Context is the situation. Instructions are the job.",
            "answers": [
                {"text": "\"Under 100 words\"", "ok": False,
                 "why": "That is an instruction — it tells the tool what to do "
                        "with the facts. Useful, but it describes the output "
                        "rather than the situation."},
                {"text": "\"The client escalated to my director this morning\"",
                 "ok": True,
                 "why": "A fact about the situation that changes how the whole "
                        "message should read. Nobody could infer it, and it "
                        "carries no identifying detail."},
                {"text": "\"End with a question\"", "ok": False,
                 "why": "An instruction about the shape of the output. Good to "
                        "include, but it tells the tool nothing about what is "
                        "actually going on."},
                {"text": "\"Apologetic but firm\"", "ok": False,
                 "why": "A tone instruction. It shapes the wording, but the "
                        "tool still has no idea what happened or who it is "
                        "writing to."},
            ],
        },
        {
            "q": "What does missing location cause?",
            "remember": "No place means American defaults.",
            "answers": [
                {"text": "Nothing — it writes neutrally", "ok": False,
                 "why": "There is no neutral. Without a location it falls back "
                        "on whatever dominated its training text, which means "
                        "dollars, US law and American conventions."},
                {"text": "Wrong currency, wrong rules, wrong holidays",
                 "ok": True,
                 "why": "Exactly. You get dollars instead of rupees or dirhams, "
                        "US labour assumptions, and references to holidays "
                        "nobody in your office takes."},
                {"text": "It asks you where you are", "ok": False,
                 "why": "Occasionally it will, and that is the good case. Far "
                        "more often it simply assumes, and the assumption is "
                        "invisible until a customer points it out."},
                {"text": "It uses British English by default", "ok": False,
                 "why": "Language style is the least of it. The real cost is "
                        "the legal, financial and calendar assumptions baked "
                        "into the answer."},
            ],
        },
        {
            "q": "How much context is right?",
            "remember": "What a new colleague would need. Nothing more.",
            "answers": [
                {"text": "As much as you can possibly give it", "ok": False,
                 "why": "More is not better past a point. It reads emphasis "
                        "from volume, so a long backstory pulls the answer "
                        "towards the backstory and away from your request."},
                {"text": "Whatever a capable new colleague would need",
                 "ok": True,
                 "why": "A clean, fast test that works both ways. If they "
                        "could not do the task without knowing it, include it. "
                        "If they could, leave it out."},
                {"text": "Only the task, nothing else", "ok": False,
                 "why": "That is the too-little end, and it is where most "
                        "disappointing answers come from. The tool fills every "
                        "gap you leave with a plausible invention."},
                {"text": "Everything in the email thread", "ok": False,
                 "why": "This gives good context and terrible data hygiene. "
                        "You have shared every name, address and internal "
                        "comment in that thread to improve one paragraph."},
            ],
        },
        {
            "q": "Why say what not to do?",
            "remember": "Naming the habit is what removes it.",
            "answers": [
                {"text": "It makes the tool try harder", "ok": False,
                 "why": "There is no effort dial. What changes is the range of "
                        "likely outputs — you have ruled out a pattern it "
                        "would otherwise have reached for."},
                {"text": "Some habits appear unless you rule them out",
                 "ok": True,
                 "why": "Pleasantries, restating your request and triple "
                        "apologies are extremely common in the text it learned "
                        "from. Without an instruction they come back every "
                        "single time."},
                {"text": "It shortens the answer", "ok": False,
                 "why": "It usually does, but that is a side effect. The real "
                        "gain is that the words removed were the ones carrying "
                        "no meaning."},
                {"text": "It stops hallucinations", "ok": False,
                 "why": "Different problem. Negative instructions control "
                        "style and habit. Invented facts are controlled by "
                        "supplying the facts and saying \"add nothing\"."},
            ],
        },
        {
            "q": "Where should instructions go?",
            "stem": "You have four lines of context and three instructions to "
                    "write into one prompt.",
            "remember": "Context first. Instructions last.",
            "answers": [
                {"text": "Instructions first, context after", "ok": False,
                 "why": "Workable, but weaker. The last thing in a prompt "
                        "tends to be followed most closely, and you want that "
                        "position spent on length, tone and format."},
                {"text": "Context first, instructions last", "ok": True,
                 "why": "Set the scene, then say what to do about it. The "
                        "instruction sits closest to the answer, which is "
                        "where it has most effect on length and tone."},
                {"text": "Alternate them line by line", "ok": False,
                 "why": "Hard to read and hard to edit later. When you reuse "
                        "the prompt next month you want two clean blocks you "
                        "can update separately."},
                {"text": "It makes no difference at all", "ok": False,
                 "why": "It makes a modest but real difference, and it costs "
                        "nothing to get right. More importantly, two labelled "
                        "blocks are far easier to reuse."},
            ],
        },
    ],

    "recap": {
        "title": "Context on one screen",
        "points": [
            ("Four lines it cannot guess",
             "Who is reading, what we do, where we are, why it matters now."),
            ("Context is not instruction",
             "One describes the situation, the other says what to do with it. "
             "Label both."),
            ("Say what not to do",
             "No pleasantries, no restating the request, one specific apology."),
            ("Volume equals emphasis",
             "Whatever you write most about becomes what the answer is about."),
            ("The new colleague test",
             "Would they need this to do the job? If not, leave it out."),
            ("Never identify anyone",
             "Every useful context line can be written without a name or a "
             "number."),
        ],
        "oneliner": "Give it what a new colleague would need, and nothing a "
                    "new colleague should never see.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The four context lines",
             "Reader, business, place, urgency. One clause each."),
            ("ban", "The three do-not lines",
             "No pleasantries, no preamble, one specific apology."),
            ("mail", "The context-and-instructions prompt",
             "Two labelled blocks, works as written."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-03, Role-Based Prompts. Telling it who to be "
                "changes the vocabulary, the assumptions and the level of "
                "detail you get back.",
    },

    "glossary": [
        ("Context", "The background you give so the tool knows who the text is "
                    "for and why it is being written."),
        ("Instruction", "What to do with that background: the task, the "
                        "length, the tone, the format."),
        ("Negative instruction", "Naming something you do not want, so a "
                                 "common habit is ruled out."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Token", "A small piece of text, roughly three quarters of a word. "
                  "Long prompts are counted in these."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
