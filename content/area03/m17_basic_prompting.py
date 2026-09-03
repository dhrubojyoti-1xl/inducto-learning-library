# -*- coding: utf-8 -*-
"""PE-01 — Basic Prompting. Content only. No rendering code here."""

DECK = {
    "module_code": "PE-01",
    "area": "03-prompt-engineering",
    "filename": "03-01-basic-prompting.pptx",
    "title": "Basic Prompting",
    "subtitle": "The first prompt you ever write — and the six-part shape that "
                "makes it work every time, not just when you get lucky.",
    "duration_min": 20,
    "audience": "New joiners + staff",
    "motif": "prompt",
    "cover_image": "assets/hero-prompting-basics.jpg",

    "why": {
        "title": "Anjali types four words and gets junk",
        "icon": "chat",
        "scenario": "Anjali handles client escalations for a Dubai office. She "
                    "types \"write reply to angry customer\" and gets a bland "
                    "three-paragraph letter with no order number and no "
                    "promise in it. She deletes it and writes the email "
                    "herself, the way she always has.",
        "cost": "Twenty minutes lost — and a quiet decision that the tool "
                "does not work.",
        "fix": "Six short parts, in one paragraph. The first draft comes back "
               "usable instead of generic.",
    },

    "outcomes": [
        ("chat", "Write a prompt with all six parts, without looking anything up"),
        ("doc", "Turn a vague request into a specific one in under 30 seconds"),
        ("sheet", "Set length, tone and format so you are not fixing them "
                  "afterwards"),
        ("cycle", "Repair a weak answer with one follow-up instead of starting "
                  "again"),
        ("clip", "Keep your best prompts so you never have to write them twice"),
    ],

    "sections": [
        ("Why prompts fail", "The four-word problem", "s_fail"),
        ("The six parts", "The shape of every good prompt", "s_six"),
        ("Build one now", "Do it live, with your own email", "s_build"),
        ("Set the output", "Length, tone and format", "s_out"),
        ("Fix a weak answer", "One follow-up, not a restart", "s_fix"),
        ("Choose what you'd do", "A Tuesday afternoon decision", "scenario"),
        ("Watch this", "A 4-minute outside formula", "video"),
    ],

    "slides": [
        # ---------------- Why prompts fail ----------------
        {
            "anchor": "s_fail",
            "label": "Why prompts fail",
            "title": "Why \"write an email\" fails",
            "lead": "The tool is not guessing badly. It is guessing — because "
                    "you left it nothing else to do.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "What you typed", "tone": "neutral", "mark": "chat",
                    "title": "write reply to angry customer",
                    "items": [
                        "No order number, so it cannot mention one",
                        "No reason, so it apologises for nothing in particular",
                        "No length, so you get six paragraphs",
                        "No tone, so it sounds like a form letter",
                    ],
                },
                "right": {
                    "tag": "What it had to invent", "tone": "bad",
                    "title": "Everything else",
                    "items": [
                        "Who the customer is and what they bought",
                        "What actually went wrong, and whose fault it was",
                        "What you are willing to promise them",
                        "Whether this is an email, a WhatsApp or a call note",
                    ],
                },
            },
        },
        {
            "label": "Why prompts fail",
            "title": "A prompt is a briefing",
            "lead": "Think of it as briefing a capable temp on their first "
                    "morning. They will do exactly what you describe, and "
                    "invent the rest.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You brief it", "Task, context, facts, format — in plain "
                                     "sentences."),
                    ("It fills the gaps", "Anything you left out, it invents a "
                                          "reasonable version of."),
                    ("You get a draft", "Specific if you were specific. "
                                        "Generic if you were vague."),
                    ("You check and send", "Two minutes of checking, not "
                                           "twenty of rewriting."),
                ],
            },
        },

        # ---------------- The six parts ----------------
        {
            "anchor": "s_six",
            "label": "The six parts",
            "title": "The six parts of a good prompt",
            "lead": "Say these six things and there is almost nothing left for "
                    "the tool to guess.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "TASK — what you want made. \"Write a reply email.\"",
                    "CONTEXT — who it is for and why. \"To a client whose "
                    "delivery slipped.\"",
                    "FACTS — the details only you have. \"Order 4471, due 12 "
                    "March, now 15 March.\"",
                    "TONE — how it should sound. \"Apologetic but calm.\"",
                    "LENGTH — how long. \"Under 120 words.\"",
                    "FORMAT — the shape you want back. \"An email with a "
                    "subject line.\"",
                ],
            },
        },
        {
            "label": "The six parts",
            "title": "The six parts, in one paragraph",
            "lead": "You do not need headings or bullet points. Write it the "
                    "way you would say it out loud.",
            "visual": {
                "type": "prompt",
                "text": "Write a reply email to a client whose delivery "
                        "slipped. Order 4471 was promised on 12 March and will "
                        "now arrive on 15 March, delayed by a transport "
                        "strike. Tone: apologetic but calm. Under 120 words. "
                        "Give me a subject line too.",
                "caption": "Six parts, one paragraph, 42 words. It works as "
                           "written.",
                "why": [
                    "Every gap is filled, so nothing has to be invented.",
                    "Each fact in the reply can be checked against your prompt.",
                    "No headings needed — plain sentences are enough.",
                ],
            },
        },

        # ---------------- Build one now ----------------
        {
            "anchor": "s_build",
            "label": "Build one now",
            "title": "Build one now, with your own work",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick a real message you actually have to send today.",
                    "Say the six parts out loud first. It takes thirty seconds.",
                    "Type them as one paragraph. Do not format it, do not use "
                    "bullet points.",
                    "Read the reply and count how many of your facts it used.",
                ],
                "prompt": "Write a short WhatsApp message to a supplier "
                          "chasing a pending delivery. PO 2290 was due on 8 "
                          "April and has not arrived. This is the second time "
                          "we have followed up. Tone: firm but polite. Under "
                          "60 words. Just the message, no greeting block.",
                "caption": "Try this one first, then rewrite it with your own "
                           "PO number.",
            },
        },
        {
            "label": "Build one now",
            "title": "Four words versus six parts",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Four words",
                "bad": [
                    "You type:  write reply to angry customer",
                    "You get a letter that apologises for \"the "
                    "inconvenience\" three times and names nothing at all.",
                    "You delete it and write the email yourself. Twenty "
                    "minutes gone.",
                ],
                "good_tag": "Six parts",
                "good": [
                    "You type the six-part paragraph from two slides back.",
                    "You get a 110-word reply carrying the order number, both "
                    "dates and one clear apology.",
                    "You check the dates, change one word, and send. Three "
                    "minutes.",
                ],
                "note": "Same tool, same afternoon. The difference was thirty "
                        "seconds of typing.",
            },
        },

        # ---------------- Set the output ----------------
        {
            "anchor": "s_out",
            "label": "Set the output",
            "title": "Length, tone and format do the work",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Length",
                     "sub": "\"Under 120 words.\" \"Exactly five bullets.\" "
                            "\"Two sentences.\" Always say a number."},
                    {"icon": "chat", "label": "Tone",
                     "sub": "\"Apologetic but calm.\" \"Direct, no small "
                            "talk.\" \"Warm — this client has been with us "
                            "nine years.\""},
                    {"icon": "sheet", "label": "Format",
                     "sub": "\"A table with three columns.\" \"An email with a "
                            "subject line.\" \"Five bullets, no introduction.\""},
                ],
            },
        },
        {
            "label": "Set the output",
            "title": "Ask for a table, get a table",
            "visual": {
                "type": "prompt_out",
                "text": "Turn this into a table with three columns: item, "
                        "problem, who fixes it. One row per item and no extra "
                        "commentary. Items: printer on the 2nd floor jams "
                        "every third print; meeting room AC has not cooled "
                        "since Monday; visitor wifi password is not working "
                        "for guests.",
                "caption": "\"No extra commentary\" is the part people forget.",
                "out_title": "What comes back",
                "out": [
                    "A clean three-column table with three rows, and nothing "
                    "else around it.",
                    "No \"Here is your table\", no closing sentence — because "
                    "you asked for no extra commentary.",
                    "You can paste it straight into an email or a Word file "
                    "without deleting anything.",
                ],
            },
        },
        {
            "label": "Set the output",
            "title": "Words that make a prompt worse",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"Make it professional\"",
                     "It cannot tell what that means to you. Say \"no slang, "
                     "no exclamation marks, full sentences\"."),
                    ("\"Make it better\"",
                     "Better than what? Name the change: shorter, warmer, "
                     "fewer numbers, one apology instead of three."),
                    ("\"Urgent\" and \"ASAP\"",
                     "The tool has no clock and no queue. You spent a word on "
                     "urgency instead of on the order number."),
                    ("\"...and so on\"",
                     "It will invent the rest of your list. Write out every "
                     "item you actually want covered."),
                    ("\"Summarise this\" with nothing attached",
                     "There is nothing to summarise, so you get a general "
                     "paragraph about the topic. Paste the text first."),
                ],
            },
        },

        # ---------------- Fix a weak answer ----------------
        {
            "anchor": "s_fix",
            "label": "Fix a weak answer",
            "title": "One follow-up beats a restart",
            "visual": {
                "type": "prompt",
                "header": "Copy this follow-up",
                "text": "That is close. Keep the first two paragraphs exactly "
                        "as they are. Replace the last paragraph with one line "
                        "confirming the new delivery date of 15 March. Cut the "
                        "whole thing to under 100 words.",
                "caption": "Protect, then change, then give the new fact.",
                "why": [
                    "It keeps the part that already worked.",
                    "It names the change, so nothing else moves.",
                    "It supplies the new fact, so nothing gets invented.",
                ],
            },
        },
        {
            "label": "Fix a weak answer",
            "title": "Three follow-ups that always work",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Cut it down",
                     "sub": "\"Half the length, same facts, keep both dates.\" "
                            "A target plus something to protect."},
                    {"icon": "person", "label": "Change the reader",
                     "sub": "\"Rewrite this for a client who is already "
                            "annoyed with us.\" The facts stay, the tone moves."},
                    {"icon": "list", "label": "Ask for options",
                     "sub": "\"Give me three versions, numbered, and say what "
                            "is different about each.\""},
                ],
            },
        },
        {
            "label": "Fix a weak answer",
            "title": "When not to bother prompting",
            "visual": {
                "type": "tree",
                "question": "Is the answer already written down somewhere?",
                "yes": {
                    "path": "Yes", "tone": "neutral", "label": "Go and get it",
                    "detail": "The GST rate, a clause in the contract, last "
                              "month's dispatch number. Opening the file takes "
                              "less time than checking an answer that might be "
                              "invented.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Write the prompt",
                    "detail": "You have the facts in your head or on the "
                              "screen in front of you, and what you actually "
                              "need is the wording. This is exactly what "
                              "prompting is for.",
                },
            },
        },

        # ---------------- Keeping prompts ----------------
        {
            "label": "Fix a weak answer",
            "title": "Keep your best prompts",
            "lead": "The people who get the most out of these tools are not "
                    "the fastest typists. They are the ones with ten good "
                    "prompts saved.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "The day a prompt works, paste it into a notes file. Not "
                    "next week — that day.",
                    "Name it the way you would search for it: \"late delivery "
                    "email\".",
                    "Swap the specifics for brackets so you can refill them "
                    "next time.",
                    "Put it where the team can find it: [COMPANY INPUT "
                    "NEEDED: where the shared prompt library lives].",
                ],
            },
        },
        {
            "label": "Fix a weak answer",
            "title": "A prompt you can reuse tomorrow",
            "visual": {
                "type": "prompt_out",
                "header": "Your reusable template",
                "text": "Write a [type of message] to [who it is for]. "
                        "Situation: [what happened, in one sentence]. Facts: "
                        "[the dates, numbers and names you are willing to "
                        "share]. Tone: [how it should sound]. Length: under "
                        "[number] words. Format: [email with a subject line / "
                        "plain message / bullets].",
                "caption": "Six brackets. That is the whole method.",
                "out_title": "Filled in, it looks like this",
                "out": [
                    "\"Write a WhatsApp message to our transporter. Situation: "
                    "the 8 April pickup did not happen.\"",
                    "\"Facts: PO 2290, due 8 April, second follow-up. Tone: "
                    "firm but polite. Length: under 60 words. Format: plain "
                    "message.\"",
                    "Thirty seconds of filling in, and a message you can send.",
                ],
            },
        },
        {
            "label": "Fix a weak answer",
            "title": "Never put these in a prompt",
            "gloss": ["Context"],
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A prompt leaves your laptop. Write it as if it "
                            "will be read by someone outside the company.",
                "sub": "Because in most cases it is — the tool runs on "
                       "somebody else's servers.",
                "cols": 3,
                "items": [
                    "Customer names, phone numbers or addresses",
                    "Prices, margins or anything lifted from a contract",
                    "A colleague's name attached to pay or performance",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 4:15 pm",
        "situation": "Your manager forwards a 14-page site report and asks for "
                     "\"a summary by 5\". You have 45 minutes and you have not "
                     "read a word of it.",
        "choices": [
            {
                "text": "Paste the report in and type \"summarise this\".",
                "tone": "ok",
                "headline": "A good summary of the wrong things",
                "consequence": "You get a fair summary, weighted towards "
                               "whatever is longest in the document. The two "
                               "points your manager actually needs are in "
                               "paragraph three, or missing. You still have to "
                               "read all 14 pages to find out which.",
                "rule": "Say what the summary is for. That is what decides "
                        "which parts matter.",
            },
            {
                "text": "Ask your manager what the summary is for, then write "
                        "the prompt.",
                "tone": "good",
                "headline": "Ninety seconds very well spent",
                "consequence": "She needs to know whether the Chakan line "
                               "restarts on Monday. So you ask: \"From this "
                               "report, answer one question in under 100 "
                               "words — does the Chakan line restart on "
                               "Monday, and what would stop it?\" You send the "
                               "answer at 4:32.",
                "rule": "A summary with no purpose is just a shorter report.",
            },
            {
                "text": "Ask for five bullets and forward them straight on.",
                "tone": "bad",
                "headline": "You forwarded something you had not checked",
                "consequence": "The five bullets read beautifully. One says "
                               "the line restarts Monday. The report actually "
                               "says Monday is the earliest possible date, if "
                               "the spare part arrives. Your manager plans "
                               "around Monday. The part arrives Thursday.",
                "rule": "You own every sentence you forward. Check it against "
                        "the source before it leaves you.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=kOs8H4j0cFg",
        "title": "Master Prompt Engineering in 5 Minutes! (Copy This Formula)",
        "channel": "Prof. Ryan Ahmed",
        "duration": "4:30",
        "heading": "Four minutes, one clear formula",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The six parts above are all you actually need.",
            "Useful if you prefer hearing a method to reading one.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which prompt will work better?",
            "stem": "Both are asking for the same thing: an email about a "
                    "delivery that slipped by three days.",
            "remember": "Specific beats polite. Facts beat adjectives.",
            "answers": [
                {"text": "\"Write a professional email about the delay.\"",
                 "ok": False,
                 "why": "\"Professional\" gives it nothing to act on. You will "
                        "get a polite, empty letter with no order number and "
                        "no date, because you supplied neither. The word is "
                        "doing no work at all."},
                {"text": "\"Write a 100-word email. Order 4471 was due 12 "
                         "March, now arriving 15 March, delayed by a strike. "
                         "Apologetic but calm.\"", "ok": True,
                 "why": "Task, facts, tone and length are all there. Every "
                        "sentence it writes can be checked against something "
                        "you typed, so there is nothing left for it to invent."},
                {"text": "\"Write the best possible email about the delay.\"",
                 "ok": False,
                 "why": "\"Best possible\" is not an instruction — there is no "
                        "scale for it to measure against. It falls back on a "
                        "generic template, the same one everybody else gets."},
                {"text": "\"Write an email about the delay, ASAP.\"",
                 "ok": False,
                 "why": "The tool has no clock and no queue, so ASAP changes "
                        "nothing about the answer. You have spent a word on "
                        "urgency that could have been the order number."},
            ],
        },
        {
            "q": "Which part is missing here?",
            "stem": "\"Write a reply to our supplier about the late PO. Tone: "
                    "firm but polite. Under 60 words. Plain message.\"",
            "remember": "The facts are the part only you have. Never leave "
                        "them out.",
            "answers": [
                {"text": "The task", "ok": False,
                 "why": "The task is there — \"write a reply\". What is "
                        "missing is what actually happened. Look for the part "
                        "that nobody but you could supply."},
                {"text": "The tone", "ok": False,
                 "why": "Tone is present and doing its job: \"firm but "
                        "polite\". That is one of the six parts already "
                        "handled."},
                {"text": "The facts", "ok": True,
                 "why": "Correct. There is no PO number, no due date and no "
                        "mention that this is the second chase. The tool will "
                        "either leave those gaps visible or fill them with "
                        "something plausible."},
                {"text": "The length", "ok": False,
                 "why": "Length is there: \"under 60 words\". It is one of the "
                        "easiest parts to get right and one of the most "
                        "useful, and this prompt already has it."},
            ],
        },
        {
            "q": "How do you get exactly five bullets?",
            "remember": "If you want a number, say the number.",
            "answers": [
                {"text": "Ask for \"a few bullet points\"", "ok": False,
                 "why": "\"A few\" means nothing here. You will get three, or "
                        "seven, or a paragraph with dashes in it. Then you are "
                        "editing again."},
                {"text": "Ask for \"exactly five bullet points, no "
                         "introduction\"", "ok": True,
                 "why": "A number plus what to leave out. The \"no "
                        "introduction\" matters — without it you usually get a "
                        "lead-in sentence you then have to delete every time."},
                {"text": "Write them yourself, it is faster", "ok": False,
                 "why": "For five bullets out of notes you already have, it is "
                        "not. The whole point of saying \"exactly five\" is "
                        "that you stop editing the output at all."},
                {"text": "Ask twice and keep the better answer", "ok": False,
                 "why": "That doubles your work to fix something one word "
                        "would have solved. Save re-asking for when the "
                        "content is wrong, not the formatting."},
            ],
        },
        {
            "q": "The reply is too long. Now what?",
            "stem": "The structure and the tone are exactly right. It is just "
                    "180 words when you wanted about 80.",
            "remember": "Say the number, and say what to keep.",
            "answers": [
                {"text": "Type \"make it shorter\"", "ok": False,
                 "why": "It will shorten it by some amount of its own "
                        "choosing — maybe a tenth, maybe half. You will be "
                        "back here in a minute asking again."},
                {"text": "Type \"cut it to under 80 words, keep both dates\"",
                 "ok": True,
                 "why": "A number, plus something to protect. It now knows "
                        "exactly how much to cut and exactly what it is not "
                        "allowed to lose on the way."},
                {"text": "Start again with a shorter prompt", "ok": False,
                 "why": "You would throw away a draft that was right in every "
                        "way except length. Starting again also hands you a "
                        "fresh set of gaps to check."},
                {"text": "Delete the extra paragraphs yourself", "ok": False,
                 "why": "Fine once. But do it every time and you are still "
                        "hand-editing — which is the work you were trying to "
                        "get rid of."},
            ],
        },
        {
            "q": "What belongs in a saved prompt?",
            "remember": "Save the shape. Never save the customer's details.",
            "answers": [
                {"text": "The exact client name and order number you used",
                 "ok": False,
                 "why": "Those are the parts that change every single time, "
                        "and one of them is customer data. Swap them for "
                        "brackets before the prompt is saved anywhere."},
                {"text": "The shape, with brackets where the details go",
                 "ok": True,
                 "why": "The reusable part is the structure: task, context, "
                        "[facts], tone, length, format. You refill the "
                        "brackets in about ten seconds each time."},
                {"text": "Just the first line — you will remember the rest",
                 "ok": False,
                 "why": "You will not, and neither will the colleague you "
                        "share it with. A prompt is only reusable if the whole "
                        "thing is written down."},
                {"text": "Nothing. Write a fresh prompt every time",
                 "ok": False,
                 "why": "Then you pay the thinking cost again on every "
                        "message. Ten saved prompts is the difference between "
                        "using the tool and fighting it."},
            ],
        },
    ],

    "recap": {
        "title": "Basic Prompting on one screen",
        "points": [
            ("Six parts, one paragraph",
             "Task, context, facts, tone, length, format — in plain sentences."),
            ("The facts are your job",
             "Dates, numbers and names are the part only you have. Leave them "
             "out and they get invented."),
            ("Say the number",
             "\"Under 100 words.\" \"Exactly five bullets.\" \"Three "
             "columns.\" Vague in, vague out."),
            ("Adjectives do nothing",
             "\"Professional\", \"better\", \"urgent\" give it nothing to act "
             "on. Name the actual change."),
            ("Correct, don't restart",
             "\"Keep the first two paragraphs. Cut to 80 words.\" One line "
             "saves the whole draft."),
            ("Save the shape, not the details",
             "Store the prompt with brackets where the customer data used to "
             "be."),
        ],
        "oneliner": "A prompt is a briefing. Everything you leave out gets "
                    "filled in for you — and you may not notice which parts.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("mail", "The six-part prompt",
             "Task, context, facts, tone, length, format. One paragraph, works "
             "as written."),
            ("sheet", "The \"make it a table\" prompt",
             "Name the columns, then say \"no extra commentary\"."),
            ("cycle", "The one-line correction",
             "Keep what worked, name the change, supply the new fact."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-02, Instructions & Context. It shows you how "
                "much background to give — and the point where adding more "
                "context starts making the answer worse.",
    },

    "glossary": [
        ("Prompt", "Everything you type in: the request plus the facts you "
                   "choose to supply."),
        ("Context", "The background you give so the tool knows who the text is "
                    "for and why it is being written."),
        ("Token", "A small piece of text, roughly three quarters of a word. "
                  "Length limits are counted in tokens, not letters."),
        ("Zero-shot", "Asking for something without showing an example first. "
                      "Most everyday prompts are zero-shot."),
        ("Few-shot", "Giving one or two examples of what good looks like "
                     "before you make your request."),
        ("Output", "What comes back. A draft you are responsible for, never a "
                   "source you can quote."),
    ],
}
