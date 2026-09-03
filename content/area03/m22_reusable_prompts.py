# -*- coding: utf-8 -*-
"""PE-06 — Reusable Prompts. Content only."""

DECK = {
    "module_code": "PE-06",
    "area": "03-prompt-engineering",
    "filename": "03-06-reusable-prompts.pptx",
    "title": "Reusable Prompts",
    "subtitle": "Turning the prompts that worked into a library you and your "
                "team stop rewriting every week.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "prompt",
    "cover_image": "assets/hero-prompt-library.jpg",

    "why": {
        "title": "Karthik rewrites the same prompt weekly",
        "icon": "cycle",
        "scenario": "Karthik runs IT support for a Chennai office. Every "
                    "Monday he writes a prompt to turn the week's ticket log "
                    "into a summary. Every Monday it takes four attempts, "
                    "because he cannot remember what worked last week.",
        "cost": "Fifteen minutes a week rediscovering something he already "
                "knew.",
        "fix": "Saved once, with brackets. Ten seconds a week from then on.",
    },

    "outcomes": [
        ("clip", "Turn a prompt that worked into a reusable template today"),
        ("list", "Name and store prompts so you can actually find them again"),
        ("shield", "Strip a prompt of anything that must not be stored"),
        ("person", "Share a prompt so a colleague can use it without you"),
        ("cycle", "Improve a stored prompt instead of starting over"),
    ],

    "sections": [
        ("Why prompts get lost", "The Monday morning tax", "s_lost"),
        ("Turning one into a template", "Brackets and a name", "s_template"),
        ("Naming and storing", "So you find it in ten seconds", "s_store"),
        ("Sharing safely", "What must never be saved", "s_share"),
        ("Do this now", "Build your first three", "s_do"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "An 8-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_lost",
            "label": "Why prompts get lost",
            "title": "The Monday morning tax",
            "lead": "The prompt that worked is thinking you already did. "
                    "Almost nobody keeps it.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You get it right", "After three or four attempts, the "
                                         "answer is exactly right."),
                    ("You use the answer", "The job is done, so you close the "
                                           "tab."),
                    ("The prompt disappears", "It was in a chat you will never "
                                              "scroll back to."),
                    ("Next week, from scratch", "Four attempts again, for the "
                                                "same job."),
                ],
            },
        },
        {
            "label": "Why prompts get lost",
            "title": "Which prompts are worth keeping",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Keep it", "tone": "good",
                    "title": "Worth ten seconds to save",
                    "items": [
                        "You will do this job again this month",
                        "It took more than two attempts to get right",
                        "A colleague does the same job",
                        "The format matters and drifts easily",
                    ],
                },
                "right": {
                    "tag": "Let it go", "tone": "neutral", "mark": "list",
                    "title": "Not worth the filing",
                    "items": [
                        "A one-off question you will never repeat",
                        "It worked on the first attempt anyway",
                        "It only makes sense for today's document",
                        "You would rewrite it faster than find it",
                    ],
                },
            },
        },
        {
            "anchor": "s_template",
            "label": "Turning one into a template",
            "title": "Brackets do the work",
            "visual": {
                "type": "prompt",
                "header": "The template pattern",
                "text": "Turn the [WHAT: ticket log / delay list / site notes] "
                        "below into a [FORMAT: 200-word summary / table / five "
                        "bullets] for [READER: my manager / the client / the "
                        "team]. Use only what I have pasted. Do not add "
                        "anything I have not given you. [TONE: brief and "
                        "factual].",
                "caption": "Four brackets. Ten seconds to fill, every time.",
                "why": [
                    "Brackets say what belongs there, not just that something "
                    "does.",
                    "The unchanging half is the half you kept getting wrong.",
                    "Anyone can use it without asking you what you meant.",
                ],
            },
        },
        {
            "label": "Turning one into a template",
            "title": "Make the template for me",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this template-builder",
                "text": "Below is a prompt that worked well for me. Turn it "
                        "into a reusable template. Keep every instruction "
                        "exactly as it is, and replace only the specific facts "
                        "with clearly labelled brackets saying what belongs "
                        "there. Do not improve the wording.",
                "caption": "\"Do not improve the wording\" protects what "
                           "already worked.",
                "out_title": "What comes back",
                "out": [
                    "The same prompt with your one-off details swapped for "
                    "labelled brackets.",
                    "Instructions untouched, because you told it not to touch "
                    "them.",
                    "A template you can paste next week without thinking about "
                    "it.",
                ],
            },
        },
        {
            "anchor": "s_store",
            "label": "Naming and storing",
            "title": "Name it the way you search",
            "lead": "A prompt you cannot find in ten seconds is a prompt you "
                    "will rewrite.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Name it after the job, not the technique: \"weekly ticket "
                    "summary\"",
                    "Put the reader in the name if there are two versions",
                    "Keep them all in one file, not scattered across chats",
                    "Add one line saying what good output looked like",
                ],
            },
        },
        {
            "label": "Naming and storing",
            "title": "Where a library actually lives",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "One shared file",
                     "sub": "A single document everyone can open beats a "
                            "clever system nobody updates."},
                    {"icon": "list", "label": "One line per prompt",
                     "sub": "Name, what it is for, the prompt itself. Nothing "
                            "else needed to start."},
                    {"icon": "person", "label": "One owner",
                     "sub": "Somebody who tidies it monthly. Otherwise it "
                            "becomes a graveyard within a quarter."},
                ],
            },
        },
        {
            "anchor": "s_share",
            "label": "Sharing safely",
            "title": "What must never be saved",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A stored prompt gets copied, shared and pasted "
                            "for years. Everything in it travels too.",
                "sub": "The parts that change are exactly the parts that must "
                       "not be stored.",
                "cols": 2,
                "items": [
                    "Customer names, sites, contacts or order numbers",
                    "Prices, margins or wording taken from a contract",
                    "Colleague names beside performance or pay",
                    "Anything marked internal, confidential or restricted",
                ],
            },
        },
        {
            "label": "Sharing safely",
            "title": "Strip it before you save it",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Saved as used",
                "bad": [
                    "\"Summarise the ticket log for Ashirwad Traders, account "
                    "4471, contact Ramesh Nair...\"",
                    "The template now carries a real customer, a real account "
                    "and a real name.",
                    "It gets shared with four colleagues and pasted for two "
                    "years.",
                ],
                "good_tag": "Saved as template",
                "good": [
                    "\"Summarise the ticket log for [CLIENT], account "
                    "[NUMBER], contact [NAME]...\"",
                    "Identical usefulness, and nothing identifying is stored "
                    "anywhere.",
                    "Safe to share with anyone, including a new joiner on day "
                    "one.",
                ],
                "note": "The brackets are not only convenience. They are what "
                        "makes a prompt safe to keep.",
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: build three",
            "visual": {
                "type": "steps",
                "items": [
                    "Open a blank document and call it \"My prompts\".",
                    "Write down the three jobs you do most often in writing.",
                    "For each, paste the prompt you last used and add "
                    "brackets.",
                    "Put it where your team can reach it: [COMPANY INPUT "
                    "NEEDED: shared location].",
                ],
                "prompt": "Turn the [WHAT] below into a [FORMAT] for [READER]. "
                          "Use only what I have pasted and do not add anything "
                          "I have not given you. Keep it under [NUMBER] words. "
                          "[TONE]. No introduction and no closing summary.",
                "caption": "Start with this one. It covers most writing jobs "
                           "as it stands.",
            },
        },
        {
            "label": "Do this now",
            "title": "Improving a stored prompt",
            "visual": {
                "type": "tree",
                "question": "Did the stored prompt give a weak answer today?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Fix the template",
                    "detail": "Add the missing line to the stored version "
                              "straight away, not just to today's chat. "
                              "Otherwise you meet the same gap next month.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Leave it alone",
                    "detail": "A template that works does not need polishing. "
                              "Tinkering with a good prompt is how teams end "
                              "up with six versions of one thing.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits that keep it alive",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Save it the day it works, not the day you have time.",
                    "Fix the stored version, never just today's copy.",
                    "Delete anything nobody has used in six months.",
                    "Show a new joiner the file in their first week.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Meaning to save it later",
                     "The tab closes, the week moves on, and Monday costs you "
                     "fifteen minutes again."),
                    ("Saving the version with real data in it",
                     "One customer's details get copied into a file four "
                     "people share for two years."),
                    ("Naming it after the technique",
                     "\"Few-shot summary v2\" is unfindable. \"Weekly ticket "
                     "summary\" is not."),
                    ("Keeping six near-identical versions",
                     "Nobody knows which one is current, so everyone writes a "
                     "seventh."),
                    ("Fixing today's copy and not the template",
                     "You solve the same gap every month and never notice you "
                     "are doing it."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "What a good library looks like",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "One file everyone can open",
                     "sub": "Not a folder, not an app nobody logs into."},
                    {"label": "Ten to twenty prompts",
                     "sub": "Named after jobs people actually do."},
                    {"label": "Every one with brackets",
                     "sub": "No customer, no colleague, no contract in any of "
                            "them."},
                ],
                "note": "Twenty good prompts covers most of what an office "
                        "writes in a week. Beyond that, teams stop reading the "
                        "list and start rewriting again.",
            },
        },
        {
            "label": "Do this now",
            "title": "The reusable prompt rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Save the shape the day it works. Never save the "
                            "details.",
                "sub": "The shape is what you keep rediscovering. The details "
                       "are what you must not store.",
                "cols": 3,
                "items": [
                    "Worked today — save it today.",
                    "Real names in it — bracket them out.",
                    "Nobody uses it — delete it.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 9:00 am",
        "situation": "The weekly ticket summary is due at 10. You wrote a "
                     "prompt for this three weeks ago that worked beautifully, "
                     "and you cannot find it.",
        "choices": [
            {
                "text": "Scroll back through your chat history to find it.",
                "tone": "ok",
                "headline": "Sometimes works, never reliably",
                "consequence": "Twelve minutes of scrolling. You find "
                               "something close, but you are not sure whether "
                               "it is the version that worked or the one "
                               "before it. You use it anyway and spend another "
                               "five minutes fixing the output.",
                "rule": "Chat history is not storage. It is a place things go "
                        "to be lost.",
            },
            {
                "text": "Write it fresh, then save it with brackets straight "
                        "away.",
                "tone": "good",
                "headline": "Costs today. Free every week after.",
                "consequence": "Four attempts, as usual, and eight minutes. "
                               "Then thirty seconds pasting it into a shared "
                               "file with [CLIENT] and [WEEK] in place of the "
                               "specifics. Next Monday the same job takes "
                               "under a minute, and so does the Monday after.",
                "rule": "The saving is the cheap part. Doing it the same day "
                        "is what makes it happen.",
            },
            {
                "text": "Copy the prompt from last week's chat, real names and "
                        "all, into a shared file.",
                "tone": "bad",
                "headline": "You just filed a customer record",
                "consequence": "The prompt works, and the file now contains a "
                               "real client name, an account number and a "
                               "named contact. Four colleagues have access to "
                               "it, and it will still be there in two years, "
                               "long after that account has closed.",
                "rule": "Bracket the details before anything is stored or "
                        "shared.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=f3IeLIT_HRc",
        "title": "Why You Need an AI Prompt Library Now & How to Build One",
        "channel": "Marketing Explained",
        "duration": "8:17",
        "heading": "Eight minutes on building one",
        "note": "An outside video, not company material. A single shared "
                "file is still enough to start.",
        "how": [
            "Optional. A single shared file is enough to start.",
            "Useful if your team wants something more organised.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which prompt is worth saving?",
            "remember": "Repeated, and hard to get right first time.",
            "answers": [
                {"text": "One that worked on the first attempt", "ok": False,
                 "why": "If it worked immediately, you will get it right "
                        "immediately next time too. The filing costs more than "
                        "the rewriting would."},
                {"text": "One that took four attempts and you will need again",
                 "ok": True,
                 "why": "Those four attempts were real thinking. Saving it "
                        "means you never repeat that work, and a colleague "
                        "gets it without doing it at all."},
                {"text": "A one-off question about today's document",
                 "ok": False,
                 "why": "It only makes sense alongside a document you will "
                        "never open again. Storing it clutters the file "
                        "without helping anyone."},
                {"text": "Any prompt at all — save everything", "ok": False,
                 "why": "A library of two hundred prompts is one nobody reads. "
                        "Ten to twenty good ones is the range where people "
                        "actually look before writing."},
            ],
        },
        {
            "q": "What do brackets actually do?",
            "remember": "They make it reusable and safe to store.",
            "answers": [
                {"text": "They tell the tool to search for the value",
                 "ok": False,
                 "why": "It cannot search. If you leave a bracket unfilled it "
                        "will either ask you or invent something plausible to "
                        "put there."},
                {"text": "They mark what changes, and keep real data out",
                 "ok": True,
                 "why": "Both at once. [CLIENT] tells the next person what "
                        "belongs there, and it means no real client name is "
                        "sitting in a file four people can open."},
                {"text": "They make the prompt shorter", "ok": False,
                 "why": "Length is roughly unchanged. The gain is that the "
                        "unchanging part — the part you kept getting wrong — "
                        "is now settled permanently."},
                {"text": "They stop the tool inventing facts", "ok": False,
                 "why": "That is what \"do not add anything I have not given "
                        "you\" does. Brackets are about reuse and safety, not "
                        "invention."},
            ],
        },
        {
            "q": "How should you name a prompt?",
            "remember": "After the job, not the technique.",
            "answers": [
                {"text": "\"Few-shot structured summary v3\"", "ok": False,
                 "why": "Nobody searches for that, including you in six weeks. "
                        "The name describes how it works rather than what it "
                        "is for."},
                {"text": "\"Weekly ticket summary for my manager\"", "ok": True,
                 "why": "It names the job and the reader, which is exactly "
                        "what someone types when they go looking. A colleague "
                        "who has never met you can find it."},
                {"text": "\"Prompt 7\"", "ok": False,
                 "why": "Findable only by opening every prompt in turn. Within "
                        "a month the file is unusable and people start "
                        "rewriting from scratch."},
                {"text": "The first line of the prompt itself", "ok": False,
                 "why": "Usually too long and too similar to its neighbours. "
                        "Three prompts starting \"Turn the following into...\" "
                        "are indistinguishable in a list."},
            ],
        },
        {
            "q": "The stored prompt gave a weak answer.",
            "remember": "Fix the template, not just today's copy.",
            "answers": [
                {"text": "Fix it in today's chat and move on", "ok": False,
                 "why": "You have solved it for an hour. Next month the stored "
                        "version has the same gap and somebody solves it "
                        "again, probably differently."},
                {"text": "Add the missing line to the stored version",
                 "ok": True,
                 "why": "Thirty seconds, and the fix belongs to everyone from "
                        "now on. This is the single habit that separates a "
                        "living library from a graveyard."},
                {"text": "Write a new prompt and save that too", "ok": False,
                 "why": "Now there are two versions and nobody knows which is "
                        "current. Six months later there are five, and people "
                        "write a sixth rather than choose."},
                {"text": "Delete the template — it clearly does not work",
                 "ok": False,
                 "why": "One weak answer is not a broken template. It usually "
                        "means one missing constraint, which is a one-line "
                        "repair, not a reason to throw away the work."},
            ],
        },
        {
            "q": "What must never go in a saved prompt?",
            "remember": "Anything that identifies a person or a deal.",
            "answers": [
                {"text": "The word count", "ok": False,
                 "why": "Word counts belong in the stored version. They are "
                        "part of the shape you are trying to keep, and they "
                        "identify nobody."},
                {"text": "A real client name and account number", "ok": True,
                 "why": "A stored prompt is copied, shared and pasted for "
                        "years. Anything identifying inside it travels to "
                        "everyone who ever opens the file, long after the "
                        "account has closed."},
                {"text": "The tone instruction", "ok": False,
                 "why": "Tone is exactly what you want to preserve. \"Brief "
                        "and factual\" took you three attempts to settle on "
                        "the first time."},
                {"text": "The reader description", "ok": False,
                 "why": "\"For my manager\" or \"for a client who is already "
                        "annoyed\" is a role, not an identity. It names nobody "
                        "and improves every answer."},
            ],
        },
    ],

    "recap": {
        "title": "Reusable prompts on one screen",
        "points": [
            ("Save it the day it works",
             "The tab closes and the thinking goes with it. Later never "
             "arrives."),
            ("Brackets mark what changes",
             "[CLIENT], [WEEK], [NUMBER]. Ten seconds to fill, every time."),
            ("Brackets also keep it safe",
             "No real name, account or price is ever stored in the file."),
            ("Name it after the job",
             "\"Weekly ticket summary\", never \"structured prompt v3\"."),
            ("Fix the template, not the copy",
             "One line added to the stored version fixes it for everybody."),
            ("Twenty is plenty",
             "A library nobody reads is a library that gets rewritten from "
             "scratch."),
        ],
        "oneliner": "Save the shape the day it works. Never save the details.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("clip", "The four-bracket template",
             "What, format, reader, tone. Covers most writing jobs."),
            ("cycle", "The template-builder prompt",
             "Turns a prompt that worked into a reusable one."),
            ("shield", "The strip-before-saving check",
             "Bracket every name, number and price first."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-07, Evaluating AI Responses. A short way to "
                "score an answer so you know whether to send it, fix it or "
                "throw it away.",
    },

    "glossary": [
        ("Template", "A prompt with brackets where the specifics go, so it can "
                     "be reused without rewriting."),
        ("Prompt library", "A shared file of named prompts your team reuses "
                           "instead of writing from scratch."),
        ("Bracket", "A labelled gap like [CLIENT] that says what belongs "
                    "there, and keeps real data out."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Context", "The background you give so the tool knows the situation "
                    "it is writing about."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
