# -*- coding: utf-8 -*-
"""DW-06 — Presentations with AI. Content only."""

DECK = {
    "module_code": "DW-06",
    "area": "02-ai-daily-work",
    "filename": "02-06-presentations-with-ai.pptx",
    "title": "Presentations with AI",
    "subtitle": "Get the argument straight before you open PowerPoint. The "
                "slides are the easy part.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "layers",

    "why": {
        "title": "Tanvi builds 34 slides nobody needs",
        "icon": "doc",
        "scenario": "Tanvi prepares a quarterly review for a Mumbai group "
                    "office. She opens PowerPoint first and builds 34 slides "
                    "over two evenings. In the meeting she is stopped on slide "
                    "four and asked the one question the deck never answers.",
        "cost": "Two evenings, and the question still unanswered.",
        "fix": "Settle the argument in ten lines. Then build only what "
               "supports it.",
    },

    "outcomes": [
        ("list", "Write the argument before you open any slide software"),
        ("chat", "Turn a rough argument into a slide-by-slide outline"),
        ("eye", "Cut a deck to the slides that carry the point"),
        ("person", "Predict the three questions you will actually be asked"),
        ("doc", "Write speaker notes you can genuinely say out loud"),
    ],

    "sections": [
        ("Argument before slides", "The ten-line test", "s_argument"),
        ("Outline, then build", "One slide, one point", "s_outline"),
        ("Cutting the deck", "Half the slides, same message", "s_cut"),
        ("Preparing for questions", "Before you are asked", "s_questions"),
        ("Do this now", "Outline a real deck", "s_do"),
        ("Choose what you'd do", "A review-week decision", "scenario"),
        ("Watch this", "A 13-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_argument",
            "label": "Argument before slides",
            "title": "Write the argument first",
            "lead": "If you cannot say it in ten lines, thirty slides will not "
                    "rescue it.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("The point", "One sentence. What you want them to agree "
                                  "with."),
                    ("The reasons", "Three, no more. Each one defensible."),
                    ("The evidence", "One figure or example per reason."),
                    ("The ask", "What you want them to decide or do."),
                ],
            },
        },
        {
            "label": "Argument before slides",
            "title": "The ten-line test",
            "visual": {
                "type": "prompt",
                "header": "Copy this argument prompt",
                "text": "Below are my rough notes for a presentation. Turn "
                        "them into an argument in exactly this shape: THE "
                        "POINT, one sentence. THREE REASONS, one line each. "
                        "EVIDENCE, one line under each reason. THE ASK, one "
                        "sentence. Use only my notes. Write [WEAK] beside any "
                        "reason I have not evidenced.",
                "caption": "Ten lines. If they do not convince you, the deck "
                           "will not convince anyone.",
                "why": [
                    "[WEAK] shows you which reason will get you stopped.",
                    "Three reasons is a limit, and limits force choices.",
                    "You find the hole at your desk, not in the room.",
                ],
            },
        },
        {
            "anchor": "s_outline",
            "label": "Outline, then build",
            "title": "One slide, one point",
            "visual": {
                "type": "prompt_out",
                "text": "Turn this argument into a slide outline. One slide "
                        "per point, maximum eight slides. For each, give me a "
                        "title that states the point as a full sentence, and "
                        "one line saying what the visual should show. Do not "
                        "write slide content and do not suggest stock images.",
                "caption": "A title that states the point is worth more than "
                           "any layout.",
                "out_title": "What comes back",
                "out": [
                    "Eight slide titles that each say something, rather than "
                    "naming a topic.",
                    "One line per slide telling you what to actually draw or "
                    "chart.",
                    "A deck you can build in an hour because every decision is "
                    "made.",
                ],
            },
        },
        {
            "label": "Outline, then build",
            "title": "Titles that say something",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Topic titles",
                "bad": [
                    "\"Q3 Performance\"",
                    "\"Challenges\"",
                    "The reader has to work out your point from the chart "
                    "underneath.",
                ],
                "good_tag": "Sentence titles",
                "good": [
                    "\"Dispatch volumes held, but rejections doubled\"",
                    "\"Two of six machines are idle waiting for one part\"",
                    "Someone reading only the titles understands the whole "
                    "argument.",
                ],
                "note": "If your titles alone tell the story, the deck works "
                        "even when it is forwarded without you.",
            },
        },
        {
            "anchor": "s_cut",
            "label": "Cutting the deck",
            "title": "Half the slides, same message",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Cut any slide that does not support one of your three "
                    "reasons.",
                    "Cut the agenda slide. Nobody has ever needed one.",
                    "Move anything you would only use if asked into an "
                    "appendix.",
                    "Merge two slides whenever the second only adds detail.",
                ],
            },
        },
        {
            "label": "Cutting the deck",
            "title": "The appendix is your friend",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "Main deck",
                     "sub": "Only what carries the argument. Usually six to "
                            "eight slides for a routine review."},
                    {"icon": "clip", "label": "Appendix",
                     "sub": "Everything you might be asked for. Nobody "
                            "penalises you for having it ready."},
                    {"icon": "eye", "label": "Nothing deleted",
                     "sub": "Cutting is reordering, not throwing away. That "
                            "makes it much easier to do."},
                ],
            },
        },
        {
            "anchor": "s_questions",
            "label": "Preparing for questions",
            "title": "Know the questions first",
            "lead": "Being stopped on slide four is normal. Being unprepared "
                    "for it is a choice.",
            "visual": {
                "type": "prompt",
                "header": "Copy this question prompt",
                "text": "Here is my argument and the evidence behind it. List "
                        "the five questions a sceptical senior manager would "
                        "ask, hardest first. For each, say in one line what "
                        "evidence would answer it. Do not answer the "
                        "questions and do not soften them.",
                "caption": "\"Hardest first\" and \"do not soften them\" are "
                           "what make this useful.",
                "why": [
                    "You find your weakest reason before the room does.",
                    "\"What evidence would answer it\" tells you what to go "
                    "and get.",
                    "Three of the five usually get asked, almost word for "
                    "word.",
                ],
            },
        },
        {
            "label": "Preparing for questions",
            "title": "Speaker notes you can say",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this notes prompt",
                "text": "For each slide title below, write speaker notes as "
                        "spoken sentences, maximum 40 words per slide. Write "
                        "them the way somebody would actually say them out "
                        "loud, not the way they would be written. No bullet "
                        "points and no formal phrasing.",
                "caption": "Notes you can read aloud beat notes you have to "
                           "translate.",
                "out_title": "What comes back",
                "out": [
                    "Forty spoken words per slide, in sentences you could say "
                    "without editing.",
                    "No \"it should be noted that\", because you asked for "
                    "spoken English.",
                    "Something you can actually glance at while talking.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: outline a deck",
            "visual": {
                "type": "steps",
                "items": [
                    "Take the next presentation you owe someone.",
                    "Write your rough notes in any order, for five minutes.",
                    "Run the ten-line argument prompt on them.",
                    "Fix anything marked [WEAK] before you open PowerPoint.",
                ],
                "prompt": "Turn my notes into an argument: THE POINT (one "
                          "sentence), THREE REASONS (one line each), EVIDENCE "
                          "(one line each), THE ASK (one sentence). Use only "
                          "my notes, add no figures, and mark any unevidenced "
                          "reason [WEAK].",
                "caption": "Ten minutes here saves two evenings of building.",
            },
        },
        {
            "label": "Do this now",
            "title": "What not to paste in",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A review deck usually contains the most "
                            "commercially sensitive material you handle.",
                "sub": "Describe the shape of the numbers instead of pasting "
                       "them.",
                "cols": 2,
                "items": [
                    "Customer names against revenue or margin",
                    "Unpublished results, forecasts or board figures",
                    "Employee names against performance",
                    "Anything from a contract or a tender response",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Opening PowerPoint first",
                     "You spend the evening on layout and discover the "
                     "argument has a hole in the meeting."),
                    ("Asking AI to \"make a presentation\"",
                     "You get thirty generic slides with headings and no "
                     "position in any of them."),
                    ("Topic titles instead of sentences",
                     "\"Q3 Performance\" makes the reader do the work. Forwarded "
                     "without you, it says nothing."),
                    ("Using generated images on customer slides",
                     "Almost-words and odd details read as carelessness about "
                     "everything else."),
                    ("Skipping the question rehearsal",
                     "The hardest question is entirely predictable, and you "
                     "had ten minutes to predict it."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Should AI build the slides?",
            "visual": {
                "type": "tree",
                "question": "Does the deck carry a decision or a number?",
                "yes": {
                    "path": "Yes", "tone": "neutral", "label": "You build it",
                    "detail": "Board papers, customer proposals, budget "
                              "reviews. Use AI for the argument, the outline "
                              "and the questions. Build the slides yourself.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Draft it freely",
                    "detail": "Team updates, training material, internal "
                              "explainers. Let it draft structure and notes, "
                              "then edit hard.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What good preparation looks like",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Ten lines of argument",
                     "sub": "Written and tested before anything is designed."},
                    {"label": "Eight slide titles",
                     "sub": "Each a full sentence that states a point."},
                    {"label": "Five questions rehearsed",
                     "sub": "Hardest first, with the evidence located."},
                ],
                "note": "Thirty minutes of this beats two evenings of "
                        "building, and it is the part that decides whether the "
                        "meeting goes well.",
            },
        },
        {
            "label": "Do this now",
            "title": "The presentation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If the titles alone do not tell the story, the "
                            "deck is not finished.",
                "sub": "Slides get forwarded without you far more often than "
                       "you present them.",
                "cols": 3,
                "items": [
                    "Argument first — always.",
                    "One slide, one point.",
                    "Titles that say something.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Review week, Tuesday evening",
        "situation": "The quarterly review is on Thursday. You have a folder "
                     "of charts, no structure, and two evenings before you "
                     "present.",
        "choices": [
            {
                "text": "Start building slides now — there is a lot to get "
                        "through.",
                "tone": "bad",
                "headline": "Two evenings, and the hole is still there",
                "consequence": "You build 34 slides. On Thursday you are "
                               "stopped on slide four and asked why rejections "
                               "rose. The deck covers what happened in "
                               "detail and never once addresses why, because "
                               "nobody wrote the argument down.",
                "rule": "Building is not thinking. It only feels like it.",
            },
            {
                "text": "Write the ten-line argument first, then build only "
                        "what supports it.",
                "tone": "good",
                "headline": "Thirty minutes of thinking, one evening of "
                            "building",
                "consequence": "The argument prompt marks one reason [WEAK] — "
                               "the rejection cause you had assumed. You spend "
                               "Wednesday morning finding out the real one. "
                               "The deck is eight slides, and the question you "
                               "feared is answered on slide three.",
                "rule": "Find the hole at your desk. It is much cheaper "
                        "there.",
            },
            {
                "text": "Ask AI to generate the whole presentation from your "
                        "charts.",
                "tone": "ok",
                "headline": "Fast, generic, and still yours to defend",
                "consequence": "You get thirty tidy slides with topic headings "
                               "and no position in any of them. It is a "
                               "starting point, but every slide still needs "
                               "your judgement, and you have not saved the "
                               "part that mattered.",
                "rule": "It can shape an argument you have. It cannot have one "
                        "for you.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=ZpXN9M0WLQ4",
        "title": "The Top 1% Build AI Presentations Differently. Here's "
                 "How.",
        "channel": "Jeff Su",
        "duration": "12:52",
        "heading": "Thirteen minutes on AI decks",
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
            "q": "What comes before opening PowerPoint?",
            "remember": "Ten lines of argument.",
            "answers": [
                {"text": "Choosing a template", "ok": False,
                 "why": "Templates are the last decision, not the first. A "
                        "beautiful deck with no argument fails in exactly the "
                        "same way as an ugly one."},
                {"text": "The point, three reasons, evidence and the ask",
                 "ok": True,
                 "why": "Ten lines you can test at your desk. If they do not "
                        "convince you, no amount of slide building will "
                        "convince the room."},
                {"text": "Gathering all the charts", "ok": False,
                 "why": "You will gather charts you never use and miss the one "
                        "you need. The argument tells you which evidence "
                        "matters."},
                {"text": "Booking the room", "ok": False,
                 "why": "Necessary, and it has nothing to do with whether the "
                        "presentation will work."},
            ],
        },
        {
            "q": "What makes a good slide title?",
            "remember": "A sentence that states the point.",
            "answers": [
                {"text": "It names the topic in two words", "ok": False,
                 "why": "\"Q3 Performance\" makes every reader work out your "
                        "point for themselves, and they will each reach a "
                        "different one."},
                {"text": "It states the point as a full sentence", "ok": True,
                 "why": "\"Volumes held, but rejections doubled\" carries the "
                        "message on its own. Read the titles in order and you "
                        "have the whole argument."},
                {"text": "It matches the chart underneath", "ok": False,
                 "why": "Describing the chart wastes the title. The chart is "
                        "already visible — the title should say what it "
                        "means."},
                {"text": "It is short enough to fit on one line", "ok": False,
                 "why": "Useful for layout, irrelevant to whether the title "
                        "communicates anything. A two-line sentence beats a "
                        "one-word label."},
            ],
        },
        {
            "q": "What does [WEAK] tell you?",
            "remember": "Which reason will get you stopped.",
            "answers": [
                {"text": "The wording needs improving", "ok": False,
                 "why": "It is not about wording. It marks a reason you have "
                        "asserted without evidence, which is a research "
                        "problem rather than a writing one."},
                {"text": "You have a reason with no evidence behind it",
                 "ok": True,
                 "why": "That is exactly where a senior manager will stop you. "
                        "Finding it at your desk on Tuesday costs you a "
                        "morning. Finding it on Thursday costs you the "
                        "meeting."},
                {"text": "The slide should be deleted", "ok": False,
                 "why": "Often the reason is sound and simply unevidenced. Go "
                        "and get the evidence before deciding to drop it."},
                {"text": "The tool disagrees with your reason", "ok": False,
                 "why": "It has no view on whether you are right. It is "
                        "flagging that your own notes contain no support for "
                        "the claim."},
            ],
        },
        {
            "q": "Where does extra detail belong?",
            "remember": "In an appendix, not in the main deck.",
            "answers": [
                {"text": "In the main deck, in case it is needed", "ok": False,
                 "why": "That is how a six-slide argument becomes 34 slides. "
                        "Everything you might need buries everything you "
                        "definitely need."},
                {"text": "In an appendix after the final slide", "ok": True,
                 "why": "Ready if asked, invisible if not. It also makes "
                        "cutting psychologically easy, because nothing is "
                        "being thrown away."},
                {"text": "Deleted — if it is not central it is not needed",
                 "ok": False,
                 "why": "Then you have nothing when the detailed question "
                        "comes, and detailed questions do come. Move it, do "
                        "not destroy it."},
                {"text": "In the speaker notes", "ok": False,
                 "why": "Notes are for what you will say, not for evidence you "
                        "may need to show. A table in a note cannot be put on "
                        "screen."},
            ],
        },
        {
            "q": "Which deck should you build yourself?",
            "remember": "Anything carrying a decision or a number.",
            "answers": [
                {"text": "An internal training explainer", "ok": False,
                 "why": "Low risk and repeated. Let it draft the structure and "
                        "notes, then edit. Nothing here binds the company."},
                {"text": "A customer proposal with pricing", "ok": True,
                 "why": "It carries commitments and figures, and the material "
                        "itself should never be pasted anywhere. Use AI for "
                        "the argument and the likely questions only."},
                {"text": "A team update on last month's activity", "ok": False,
                 "why": "Routine and factual. As long as you supply the "
                        "figures and it adds no causes, this is a good drafting "
                        "case."},
                {"text": "A how-to session for new joiners", "ok": False,
                 "why": "Ideal drafting territory. Structure, outline and "
                        "spoken notes all save real time, and nothing "
                        "confidential is involved."},
            ],
        },
    ],

    "recap": {
        "title": "Presentations on one screen",
        "points": [
            ("Argument before slides",
             "Point, three reasons, evidence, ask. Ten lines, at your desk."),
            ("Fix [WEAK] before you build",
             "An unevidenced reason is where you will be stopped."),
            ("One slide, one point",
             "Eight slides for a routine review is usually plenty."),
            ("Titles that say something",
             "Read the titles alone and the argument should be complete."),
            ("Appendix, not delete",
             "Move detail out of the way instead of throwing it away."),
            ("Rehearse the five questions",
             "Hardest first, with the evidence located before the meeting."),
        ],
        "oneliner": "If the titles alone do not tell the story, the deck is "
                    "not finished.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The ten-line argument prompt",
             "Point, reasons, evidence, ask, with [WEAK] flags."),
            ("doc", "The slide outline prompt",
             "Eight sentence titles and what each visual shows."),
            ("person", "The hard-questions prompt",
             "Five questions, hardest first, unsoftened."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-07, Documentation with AI. Writing an SOP "
                "somebody can actually follow without ringing you.",
    },

    "glossary": [
        ("Argument", "The point you want agreed, the reasons for it, and what "
                     "you are asking for."),
        ("Sentence title", "A slide heading that states the point rather than "
                           "naming the topic."),
        ("Appendix", "Slides kept after the end, ready if asked, invisible if "
                     "not."),
        ("Speaker notes", "What you will actually say, written as spoken "
                          "sentences."),
        ("[WEAK]", "A marker showing a reason you have asserted without "
                   "evidence."),
        ("Prompt", "Everything you type in: your notes, the structure and the "
                   "constraints."),
    ],
}
