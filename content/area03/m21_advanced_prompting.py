# -*- coding: utf-8 -*-
"""PE-05 — Advanced Prompting. Content only."""

DECK = {
    "module_code": "PE-05",
    "area": "03-prompt-engineering",
    "filename": "03-05-advanced-prompting.pptx",
    "title": "Advanced Prompting",
    "subtitle": "Breaking a big job into steps, setting limits the answer must "
                "respect, and checking the work as you go.",
    "duration_min": 20,
    "audience": "Staff who already prompt daily",
    "motif": "layers",

    "why": {
        "title": "Zainab asks for everything at once",
        "icon": "list",
        "scenario": "Zainab handles compliance for an Abu Dhabi group. She "
                    "asks one AI tool to read a policy, find the gaps, write "
                    "the fixes and draft the board note. What comes back is "
                    "confident, tidy and wrong in the middle, where nobody "
                    "looks.",
        "cost": "A board note built on a gap analysis nobody checked.",
        "fix": "Four small asks instead of one big one, checked between "
               "each.",
    },

    "outcomes": [
        ("list", "Split a large request into steps you can check individually"),
        ("ban", "Set constraints the answer is not allowed to break"),
        ("cycle", "Chain one answer into the next without losing control"),
        ("eye", "Ask it to show its reasoning where the reasoning matters"),
        ("check", "Build a self-check step into the prompt itself"),
    ],

    "sections": [
        ("Why one big ask fails", "The middle nobody checks", "s_big"),
        ("Chaining", "Four small asks, checked", "s_chain"),
        ("Constraints", "Limits it must respect", "s_limits"),
        ("Show the working", "Where reasoning matters", "s_work"),
        ("Do this now", "Chain a real task", "s_do"),
        ("Choose what you'd do", "A quarter-end decision", "scenario"),
        ("Watch this", "A 13-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_big",
            "label": "Why one big ask fails",
            "title": "The middle nobody checks",
            "lead": "A four-stage request produces one polished answer. You "
                    "can only check the ends of it.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Stage one is fine", "You gave it the document, so this "
                                          "part is grounded."),
                    ("Stage two drifts", "It infers gaps you cannot see it "
                                         "inferring."),
                    ("Stage three builds on it", "Fixes for problems that may "
                                                 "not exist."),
                    ("Stage four reads well", "A confident note resting on "
                                              "stage two."),
                ],
            },
        },
        {
            "label": "Why one big ask fails",
            "title": "One ask versus four",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "One big ask", "tone": "bad",
                    "title": "Everything at once",
                    "items": [
                        "One answer, four stages hidden inside it",
                        "You can only judge the final wording",
                        "An early error is invisible by the end",
                        "Correcting it means starting again",
                    ],
                },
                "right": {
                    "tag": "Four small asks", "tone": "good",
                    "title": "Checked between each",
                    "items": [
                        "Four answers you can each judge in a minute",
                        "An error is caught where it happened",
                        "You correct one step, not the whole job",
                        "The final draft rests on things you approved",
                    ],
                },
            },
        },
        {
            "anchor": "s_chain",
            "label": "Chaining",
            "title": "Four asks instead of one",
            "gloss": ["Chaining"],
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "STEP 1 — \"List what this policy actually requires. Facts "
                    "only.\"",
                    "STEP 2 — \"Which of those does the attached process not "
                    "cover?\"",
                    "STEP 3 — \"For the three gaps I have ticked, suggest a "
                    "fix each.\"",
                    "STEP 4 — \"Write a 200-word note covering only those three "
                    "fixes.\"",
                ],
            },
        },
        {
            "label": "Chaining",
            "title": "The tick between the steps",
            "lead": "The value is not the four prompts. It is the ten seconds "
                    "you spend between them.",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "eye", "label": "Read step one",
                     "sub": "Does this list match the document I pasted? "
                            "Delete anything that does not."},
                    {"icon": "check", "label": "Approve or cut",
                     "sub": "Tick the items you accept. The next step uses "
                            "only those."},
                    {"icon": "cycle", "label": "Feed forward",
                     "sub": "\"Using only the three I ticked...\" Every later "
                            "step rests on approved ground."},
                ],
            },
        },
        {
            "anchor": "s_limits",
            "label": "Constraints",
            "title": "Limits it must respect",
            "visual": {
                "type": "prompt",
                "header": "Copy these constraint lines",
                "text": "Constraints: use only the text I have pasted. Do not "
                        "add clauses, dates or figures that do not appear in "
                        "it. If something needed is missing, write [MISSING: "
                        "what it is] and continue. Maximum 200 words. No "
                        "introduction and no closing summary.",
                "caption": "Paste this block under any serious prompt.",
                "why": [
                    "\"Only the text I pasted\" is the strongest single line "
                    "here.",
                    "[MISSING] converts silent invention into a visible flag.",
                    "The word limit stops it padding a thin answer.",
                ],
            },
        },
        {
            "label": "Constraints",
            "title": "Four constraints worth reusing",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "SOURCE — \"use only what I pasted, nothing else\"",
                    "GAPS — \"write [MISSING: …] rather than filling it in\"",
                    "SIZE — a word count, not \"be concise\"",
                    "SHAPE — \"no introduction, no closing summary\"",
                ],
            },
        },
        {
            "anchor": "s_work",
            "label": "Show the working",
            "title": "Ask it to show its working",
            "lead": "For anything with reasoning in it, the steps are more "
                    "checkable than the conclusion.",
            "visual": {
                "type": "prompt_out",
                "text": "Work through this in visible steps before answering. "
                        "First list the figures you are using and where each "
                        "came from in my text. Then show the calculation. Then "
                        "give the answer. If a figure is not in my text, stop "
                        "and say so instead of estimating it.",
                "caption": "Useful for anything with arithmetic or a "
                           "judgement chain.",
                "out_title": "What comes back",
                "out": [
                    "A short list of figures with their origin marked against "
                    "each one.",
                    "The working set out in lines you can follow and check.",
                    "An answer you can accept or reject for a specific "
                    "reason.",
                ],
            },
        },
        {
            "label": "Show the working",
            "title": "What visible steps do not fix",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Shown working is easier to check. It is not "
                            "evidence that the working is right.",
                "sub": "The steps are generated the same way the answer is.",
                "cols": 3,
                "items": [
                    "It can show tidy, wrong arithmetic.",
                    "It can cite a figure it invented.",
                    "You still have to open the source.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: chain a task",
            "visual": {
                "type": "steps",
                "items": [
                    "Take a job you would normally ask for in one message.",
                    "Write down the stages you would do it in by hand.",
                    "Ask for stage one only, with the constraint block "
                    "attached.",
                    "Read it, delete what is wrong, then ask for stage two.",
                ],
                "prompt": "Step 1 of 4. Using only the text I have pasted "
                          "below, list what it requires us to do. Facts only, "
                          "one line each, no interpretation and no "
                          "recommendations. If something is unclear, write "
                          "[UNCLEAR] beside it rather than guessing.",
                "caption": "Say \"step 1 of 4\" out loud in the prompt. It "
                           "keeps the answer narrow.",
            },
        },
        {
            "label": "Do this now",
            "title": "Chained versus all at once",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "One message",
                "bad": [
                    "\"Read this policy, find the gaps, fix them and write the "
                    "board note.\"",
                    "Nine hundred confident words. The gap list inside it was "
                    "never shown to you.",
                    "You approve a note whose middle you have not seen.",
                ],
                "good_tag": "Four messages",
                "good": [
                    "Four short answers, each judged in about a minute.",
                    "You cut two invented requirements at step one.",
                    "The board note covers three gaps you personally "
                    "confirmed.",
                ],
                "note": "The same total time. The difference is where your "
                        "attention went.",
            },
        },
        {
            "label": "Do this now",
            "title": "When chaining is worth it",
            "visual": {
                "type": "tree",
                "question": "Would a wrong middle step reach a customer or a "
                            "board?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Chain it",
                    "detail": "Compliance, pricing, proposals, anything "
                              "signed. Break it up and approve each stage "
                              "before the next one uses it.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "One ask is fine",
                    "detail": "Internal notes, first drafts, rough summaries "
                              "you will rewrite anyway. Chaining here is "
                              "ceremony, not control.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Three habits worth keeping",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Number your steps out loud: \"step 2 of 4\".",
                    "Start each step with \"using only what I approved\".",
                    "Delete a wrong line immediately, before the next step.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Asking for the whole job in one message",
                     "You get one polished answer and can only check its "
                     "beginning and its end."),
                    ("Chaining without reading between steps",
                     "Four prompts with no checks is just a slower version of "
                     "one prompt."),
                    ("Saying \"be concise\" instead of a number",
                     "Concise means nothing. Two hundred words means two "
                     "hundred words."),
                    ("Trusting shown working as proof",
                     "Tidy steps can lead to a wrong answer, confidently and "
                     "legibly."),
                    ("Letting step three quote step one loosely",
                     "Say \"using only the three I ticked\" or it will quietly "
                     "reintroduce the ones you cut."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The advanced prompting rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Break the job at the points where a mistake would "
                            "be invisible later.",
                "sub": "That is what separates a chain from four prompts in a "
                       "row.",
                "cols": 3,
                "items": [
                    "Split where errors hide.",
                    "Check before you feed forward.",
                    "Constrain what it may invent.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Quarter-end, 4:00 pm",
        "situation": "You must produce a compliance summary for the board by "
                     "tomorrow. It needs a requirements list, a gap analysis "
                     "and a set of recommended fixes.",
        "choices": [
            {
                "text": "Ask for all three in one message and edit what comes "
                        "back.",
                "tone": "bad",
                "headline": "You will edit the wording, not the substance",
                "consequence": "The output reads like a finished board paper, "
                               "so you review it as one. The gap list inside "
                               "it contains two requirements the policy does "
                               "not actually make. Those two carry through "
                               "into recommendations the board then approves.",
                "rule": "A polished answer invites a wording review, not a "
                        "substance review.",
            },
            {
                "text": "Ask for the requirements list first, check it against "
                        "the policy, then continue.",
                "tone": "good",
                "headline": "Ten minutes longer, and defensible",
                "consequence": "Step one gives eleven requirements. You open "
                               "the policy and strike two that are not there. "
                               "Steps two, three and four use only the nine "
                               "you confirmed. The board paper rests entirely "
                               "on ground you checked yourself.",
                "rule": "Approve each stage before the next one is allowed to "
                        "use it.",
            },
            {
                "text": "Write the requirements list yourself and use AI only "
                        "for the note.",
                "tone": "ok",
                "headline": "Safe, and you gave away the easy half",
                "consequence": "Perfectly sound, and slower than it needed to "
                               "be. Extracting a requirements list from a "
                               "document you paste in is well-grounded work "
                               "the tool does quickly — as long as you read "
                               "the list afterwards.",
                "rule": "Hand over the extraction. Keep the approval.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=1c9iyoVIwDs",
        "title": "4 Methods of Prompt Engineering",
        "channel": "IBM Technology",
        "duration": "12:41",
        "heading": "Thirteen minutes, four methods",
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
            "q": "Why does one big ask fail?",
            "remember": "You can only check what you can see.",
            "answers": [
                {"text": "The tool runs out of memory", "ok": False,
                 "why": "Length limits exist but are rarely the issue here. "
                        "The problem is not that it cannot hold the job — it "
                        "is that you cannot inspect the middle of it."},
                {"text": "The middle stages are never shown to you", "ok": True,
                 "why": "You get one polished result. The gap analysis inside "
                        "it was performed invisibly, so you review the "
                        "wording of the conclusion instead of the reasoning "
                        "that produced it."},
                {"text": "Long prompts confuse it", "ok": False,
                 "why": "It handles long prompts perfectly well. The risk is "
                        "not confusion, it is that an early error becomes "
                        "undetectable by the final paragraph."},
                {"text": "It takes longer to answer", "ok": False,
                 "why": "Speed is not the concern. A fast wrong answer that "
                        "reaches a board is far more expensive than a slower "
                        "checked one."},
            ],
        },
        {
            "q": "What makes a chain different?",
            "remember": "The check between the steps.",
            "answers": [
                {"text": "Using four separate tools", "ok": False,
                 "why": "One tool is fine. What matters is that you break the "
                        "job at the points where a mistake would otherwise "
                        "become invisible."},
                {"text": "Reading and approving each step before the next",
                 "ok": True,
                 "why": "That is the whole technique. Four prompts with no "
                        "reading between them is just a slower single prompt "
                        "with more places to go wrong."},
                {"text": "Making each prompt shorter", "ok": False,
                 "why": "Shorter prompts are a side effect. A short prompt "
                        "whose output you do not read gives you no more "
                        "control than a long one."},
                {"text": "Asking the same question four ways", "ok": False,
                 "why": "That gives four generations of the same thing, which "
                        "can agree and all be wrong. Chaining moves forward "
                        "through stages, not sideways."},
            ],
        },
        {
            "q": "Which constraint does most work?",
            "remember": "\"Use only what I pasted.\"",
            "answers": [
                {"text": "\"Be accurate and thorough\"", "ok": False,
                 "why": "Nothing to act on. It cannot assess its own accuracy, "
                        "so the instruction changes the tone and nothing "
                        "else."},
                {"text": "\"Use only the text I pasted, nothing else\"",
                 "ok": True,
                 "why": "It closes the main route by which invented clauses, "
                        "dates and figures enter the answer. Pair it with "
                        "[MISSING] so gaps surface instead of closing "
                        "silently."},
                {"text": "\"Answer as an expert would\"", "ok": False,
                 "why": "A role line. It changes vocabulary and confidence, "
                        "and constrains nothing at all about what may be "
                        "invented."},
                {"text": "\"Take your time\"", "ok": False,
                 "why": "There is no time being taken. It produces text at the "
                        "same rate regardless, and the instruction has no "
                        "effect on care."},
            ],
        },
        {
            "q": "What does shown working give you?",
            "remember": "Checkability, not correctness.",
            "answers": [
                {"text": "Proof the answer is right", "ok": False,
                 "why": "The steps are generated the same way the answer is. "
                        "Tidy working can lead to a wrong result, presented "
                        "very legibly indeed."},
                {"text": "Something you can check line by line", "ok": True,
                 "why": "That is the real gain. Instead of accepting or "
                        "rejecting a conclusion whole, you can point at the "
                        "line where a figure came from nowhere."},
                {"text": "A faster answer", "ok": False,
                 "why": "It is usually longer and slower to read. You are "
                        "trading speed for the ability to inspect what "
                        "happened."},
                {"text": "Fewer hallucinations", "ok": False,
                 "why": "It does not reduce them. It makes them easier to "
                        "spot, which matters, but the invention rate is "
                        "unchanged."},
            ],
        },
        {
            "q": "When is chaining not worth it?",
            "remember": "Chain where a wrong middle would escape.",
            "answers": [
                {"text": "Anything going to a customer", "ok": False,
                 "why": "That is exactly where it is worth it. A wrong middle "
                        "step in a customer document becomes a written "
                        "commitment you have to defend."},
                {"text": "An internal first draft you will rewrite anyway",
                 "ok": True,
                 "why": "You are going to read and rework every line yourself, "
                        "so the checking is already built in. Chaining here "
                        "adds ceremony without adding control."},
                {"text": "A compliance summary", "ok": False,
                 "why": "One of the strongest cases for chaining. The gap "
                        "analysis is the step most likely to drift, and the "
                        "least visible in a finished paper."},
                {"text": "A pricing proposal", "ok": False,
                 "why": "Also a strong case. Anything with figures that carry "
                        "forward into later stages needs each stage approved "
                        "before it is used."},
            ],
        },
    ],

    "recap": {
        "title": "Advanced prompting on one screen",
        "points": [
            ("Split where errors hide",
             "Break the job at the points a mistake would be invisible in the "
             "final answer."),
            ("Check between every step",
             "Four prompts with no reading between them is one prompt with "
             "extra steps."),
            ("Feed forward only what you approved",
             "\"Using only the three I ticked\" stops cut items reappearing."),
            ("Constrain the source",
             "\"Use only what I pasted\" plus [MISSING] for anything absent."),
            ("Numbers, not adjectives",
             "\"200 words\" works. \"Be concise\" does not."),
            ("Shown working is checkable, not correct",
             "It makes an error findable. It does not make the answer right."),
        ],
        "oneliner": "Break the job where a mistake would otherwise be "
                    "invisible, and check it there.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The four-step chain",
             "Requirements, gaps, fixes, note. Approve each one."),
            ("shield", "The constraint block",
             "Source, [MISSING], word count, no padding."),
            ("eye", "The show-your-working prompt",
             "Figures and origins first, then the calculation."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-06, Reusable Prompts. Turning the ones that "
                "worked into a library you and your team stop rewriting.",
    },

    "glossary": [
        ("Chaining", "Breaking one large request into ordered steps, checking "
                     "each before the next uses it."),
        ("Constraint", "A limit the answer must respect: a source, a word "
                       "count, a forbidden habit."),
        ("Step-by-step", "Asking the tool to show its intermediate reasoning "
                         "rather than only the conclusion."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Hallucination", "A confident, invented answer. Chaining makes these "
                          "easier to catch early."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
