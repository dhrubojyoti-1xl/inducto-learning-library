# -*- coding: utf-8 -*-
"""DW-09 — Brainstorming & Idea Generation with AI. Content only."""

DECK = {
    "module_code": "DW-09",
    "area": "02-ai-daily-work",
    "filename": "02-09-brainstorming-with-ai.pptx",
    "title": "Brainstorming with AI",
    "subtitle": "Twenty options in two minutes, and a way to tell which three "
                "are actually worth your time.",
    "duration_min": 16,
    "audience": "New joiners + staff",
    "motif": "network",

    "why": {
        "title": "The same four ideas, every time",
        "icon": "bulb",
        "scenario": "A cost-reduction meeting in Ahmedabad runs every month. "
                    "The same four ideas come up, in the same order, from the "
                    "same three people. Everyone knows they are not enough. "
                    "Nobody arrives with a fifth.",
        "cost": "Twelve meetings a year, four ideas, none of them new.",
        "fix": "Twenty starting points in two minutes, so the room argues "
               "instead of stalling.",
    },

    "outcomes": [
        ("bulb", "Get twenty usable starting points in under two minutes"),
        ("ban", "Ask for bad ideas on purpose, and see why it works"),
        ("list", "Sort twenty ideas down to three without a long debate"),
        ("person", "Use it to break a deadlock between two entrenched views"),
        ("eye", "Recognise the ideas it produces that are quietly impossible"),
    ],

    "sections": [
        ("Quantity first", "Why twenty beats four", "s_quantity"),
        ("Asking for range", "Safe, odd and impossible", "s_range"),
        ("Sorting fast", "Twenty down to three", "s_sort"),
        ("Breaking a deadlock", "When two people are stuck", "s_stuck"),
        ("Do this now", "Generate on a real problem", "s_do"),
        ("Choose what you'd do", "A cost-review decision", "scenario"),
        ("Watch this", "A 13-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_quantity",
            "label": "Quantity first",
            "title": "Twenty beats four",
            "lead": "Meetings stall because people arrive with their best "
                    "idea, not with twenty rough ones.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Four ideas in the room", "Each one somebody's, so each "
                                               "one gets defended."),
                    ("Twenty on a page", "Nobody owns them, so nobody "
                                         "defends them."),
                    ("The room sorts", "Arguing about ideas, not about "
                                       "people."),
                    ("Three get tested", "Usually including one nobody had "
                                         "thought of."),
                ],
            },
        },
        {
            "label": "Quantity first",
            "title": "Nobody owns a generated idea",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Ideas people brought", "tone": "neutral",
                    "mark": "person",
                    "title": "Attached to a person",
                    "items": [
                        "Rejecting it feels like rejecting them",
                        "The senior person's idea wins by default",
                        "People bring one idea, well defended",
                        "Quiet people bring none at all",
                    ],
                },
                "right": {
                    "tag": "Ideas on a list", "tone": "good",
                    "title": "Attached to nobody",
                    "items": [
                        "Anyone can dismiss any of them freely",
                        "Seniority stops deciding which survive",
                        "Twenty options, none of them precious",
                        "Quiet people argue as easily as loud ones",
                    ],
                },
            },
        },
        {
            "anchor": "s_range",
            "label": "Asking for range",
            "title": "Ask for the bad ones too",
            "visual": {
                "type": "prompt",
                "text": "Give me twenty ways to reduce packaging cost in a "
                        "warehouse. Number them. Include five that are "
                        "obvious, ten that are unusual, and five that are "
                        "probably impractical. Do not explain them and do not "
                        "recommend any. One line each.",
                "caption": "The five impractical ones are the point, not "
                           "padding.",
                "why": [
                    "Impractical ideas are where the unusual ones come from.",
                    "\"Do not recommend any\" stops it filtering for you.",
                    "One line each keeps it scannable in the meeting.",
                ],
            },
        },
        {
            "label": "Asking for range",
            "title": "Why impossible ideas help",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Asking for good ideas",
                "bad": [
                    "\"Give me ten good ways to reduce packaging cost.\"",
                    "You get ten sensible, familiar suggestions.",
                    "Nine of them were already on the whiteboard last month.",
                ],
                "good_tag": "Asking for range",
                "good": [
                    "\"Five obvious, ten unusual, five probably impractical.\"",
                    "The impractical ones include \"stop packaging entirely "
                    "for local deliveries\".",
                    "That is impractical everywhere except two routes, where "
                    "it works.",
                ],
                "note": "Nobody says an impossible thing out loud in a "
                        "meeting. That is exactly why the good version of it "
                        "never gets found.",
            },
        },
        {
            "anchor": "s_sort",
            "label": "Sorting fast",
            "title": "Twenty down to three",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "STRIKE — anything we have already tried and rejected",
                    "STRIKE — anything needing money we do not have this year",
                    "KEEP — anything one person could test in a week",
                    "KEEP — anything that made somebody in the room react",
                ],
            },
        },
        {
            "label": "Sorting fast",
            "title": "The sorting prompt",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this sorting prompt",
                "text": "Sort the twenty ideas below into three groups. GROUP "
                        "1: could be tested by one person within a week. GROUP "
                        "2: would need budget or approval. GROUP 3: not worth "
                        "pursuing. Put every idea in exactly one group. Do not "
                        "explain and do not add new ideas.",
                "caption": "Group 1 is where you start, every time.",
                "out_title": "What comes back",
                "out": [
                    "Three clean groups, with group one usually holding four "
                    "or five ideas.",
                    "No commentary, so the meeting argues about the sorting "
                    "rather than reading.",
                    "Twenty ideas triaged in about thirty seconds.",
                ],
            },
        },
        {
            "anchor": "s_stuck",
            "label": "Breaking a deadlock",
            "title": "When two people are stuck",
            "lead": "Deadlocks are rarely about the options. They are about "
                    "two people having stated a position out loud.",
            "visual": {
                "type": "prompt",
                "header": "Copy this deadlock prompt",
                "text": "Two people disagree. Option A is to insource the "
                        "packing line. Option B is to renegotiate with the "
                        "current vendor. Give me five options that are neither "
                        "A nor B, and two ways of combining A and B. One line "
                        "each, no recommendation.",
                "caption": "Seven new things to argue about, none of them "
                           "anybody's position.",
                "why": [
                    "It moves the argument off the two stated positions.",
                    "Combinations are what neither side proposes on their "
                    "own.",
                    "Nobody has to lose to accept a third option.",
                ],
            },
        },
        {
            "label": "Breaking a deadlock",
            "title": "Ideas that are quietly impossible",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "It does not know our contracts, our plant or our "
                            "regulator.",
                "sub": "Some ideas will be excellent and completely "
                       "unavailable to us.",
                "cols": 2,
                "items": [
                    "Things our supplier contract already prohibits",
                    "Things the site licence or regulator does not permit",
                    "Things requiring equipment we do not have",
                    "Things another team tried and rejected last year",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: generate twenty",
            "visual": {
                "type": "steps",
                "items": [
                    "Take a problem your team keeps circling.",
                    "Write it in one sentence, with no names or figures.",
                    "Run the twenty-ideas prompt on it.",
                    "Strike everything already tried, then sort what is left.",
                ],
                "prompt": "Give me twenty ways to [PROBLEM IN ONE SENTENCE]. "
                          "Number them. Five obvious, ten unusual, five "
                          "probably impractical. One line each. Do not explain "
                          "them, do not recommend any, and do not group them.",
                "caption": "Two minutes. Bring the page to the meeting instead "
                           "of your one idea.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits for idea sessions",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Generate before the meeting, not during it.",
                    "Print or share the list so nobody owns any of it.",
                    "Strike first, discuss second. Striking is fast.",
                    "Pick one to test this week, not three to plan.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Asking for \"good ideas\"",
                     "You get the familiar ones. The useful ones live next to "
                     "the impractical ones."),
                    ("Letting it recommend an option",
                     "It has no view worth having. Recommending is the part "
                     "the room is for."),
                    ("Treating the list as a plan",
                     "Twenty ideas is raw material. Nothing on it has been "
                     "checked against reality."),
                    ("Describing the problem with real figures",
                     "Cost structures and margins do not need to leave the "
                     "company to generate ideas."),
                    ("Generating in the meeting itself",
                     "Everyone reads instead of thinking. Bring the list "
                     "already made."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "When brainstorming is the wrong tool",
            "visual": {
                "type": "tree",
                "question": "Is the problem a shortage of options, or of "
                            "agreement?",
                "yes": {
                    "path": "Options", "tone": "good", "label": "Generate",
                    "detail": "You keep circling the same four ideas and none "
                              "of them is good enough. Twenty rough starting "
                              "points is exactly what is missing.",
                },
                "no": {
                    "path": "Agreement", "tone": "neutral",
                    "label": "Decide instead",
                    "detail": "Everybody knows what should happen and nobody "
                              "will commit. More options make that worse. What "
                              "is needed is a decision and an owner.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What good use looks like",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Twenty ideas, generated alone",
                     "sub": "Two minutes, before anybody is in the room."},
                    {"label": "Struck down to eight",
                     "sub": "Already tried, not affordable, not permitted."},
                    {"label": "One tested this week",
                     "sub": "By one person, with a date."},
                ],
                "note": "The tool contributes the first layer only. Everything "
                        "that makes it useful happens after that, in the room "
                        "and on the floor.",
            },
        },
        {
            "label": "Do this now",
            "title": "The brainstorming rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Use it for quantity. Use the room for judgement.",
                "sub": "It is genuinely good at producing options and has no "
                       "idea which of them we can actually do.",
                "cols": 3,
                "items": [
                    "Twenty options — its job.",
                    "Striking and sorting — yours.",
                    "Testing one — this week.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Cost review, Monday",
        "situation": "The monthly cost meeting is at two. The same four "
                     "packaging ideas will be raised, as they have been for "
                     "five months. You have twenty minutes free.",
        "choices": [
            {
                "text": "Go in as usual and hope somebody has something new.",
                "tone": "bad",
                "headline": "Month six of the same four ideas",
                "consequence": "The same three people raise the same four "
                               "options. Two of them are rejected for the same "
                               "reasons as last month. The meeting ends with "
                               "an agreement to think about it, and nothing is "
                               "different in December.",
                "rule": "A meeting cannot generate what nobody brought into "
                        "it.",
            },
            {
                "text": "Generate twenty options first, strike the known ones, "
                        "bring the rest.",
                "tone": "good",
                "headline": "Two minutes of preparation changes the meeting",
                "consequence": "You bring a page of sixteen surviving ideas "
                               "that belong to nobody. The room strikes nine "
                               "immediately, argues productively about four, "
                               "and picks one to test. It is one nobody in the "
                               "room had said out loud before.",
                "rule": "Bring options nobody owns and the room starts "
                        "choosing instead of defending.",
            },
            {
                "text": "Paste last year's cost breakdown in and ask for "
                        "savings.",
                "tone": "bad",
                "headline": "Good ideas, and our cost structure is now "
                            "outside",
                "consequence": "The suggestions are sharper because they use "
                               "real figures. Those figures are our margins, "
                               "our vendor rates and our volumes, and they now "
                               "sit on a system we do not control. The ideas "
                               "were available without any of it.",
                "rule": "Describe the problem. Never paste the cost sheet.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=LuHx6KdQPHQ",
        "title": "3 Ways to Brainstorm ANYTHING in ChatGPT! (+ Free "
                 "Prompt!)",
        "channel": "AI Foundations",
        "duration": "12:43",
        "heading": "Thirteen minutes, three methods",
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
            "q": "Why ask for impractical ideas?",
            "remember": "The unusual ones live next to the impossible ones.",
            "answers": [
                {"text": "To make the list look longer", "ok": False,
                 "why": "Length is not the aim. If you wanted twenty sensible "
                        "ideas you could ask for twenty sensible ideas and get "
                        "twenty familiar ones."},
                {"text": "Impractical ideas point at unusual workable ones",
                 "ok": True,
                 "why": "\"Stop packaging entirely\" is impossible everywhere "
                        "except on two short local routes, where it works. "
                        "Nobody says that out loud in a meeting, so the "
                        "workable version never gets found."},
                {"text": "It shows the tool's limitations", "ok": False,
                 "why": "That is not what is happening. It produces the "
                        "impractical ones perfectly well on request — the "
                        "point is what they suggest to the humans reading "
                        "them."},
                {"text": "They are easier to strike, which feels productive",
                 "ok": False,
                 "why": "Striking is fast either way. The value is that some "
                        "of them survive contact with a specific route, "
                        "product or site."},
            ],
        },
        {
            "q": "Why is an unowned idea useful?",
            "remember": "Nobody has to lose to reject it.",
            "answers": [
                {"text": "It is more likely to be correct", "ok": False,
                 "why": "Correctness is unaffected by who suggested it. What "
                        "changes is how freely the room can dismiss it."},
                {"text": "People can reject it without rejecting a colleague",
                 "ok": True,
                 "why": "Most meeting deadlocks are social rather than "
                        "analytical. A list nobody authored removes seniority "
                        "and ego from the sorting entirely."},
                {"text": "It saves the meeting time", "ok": False,
                 "why": "It usually does save time, but as a consequence. The "
                        "mechanism is that people stop defending positions."},
                {"text": "It has already been checked for feasibility",
                 "ok": False,
                 "why": "The opposite — nothing on the list has been checked "
                        "against contracts, licences or equipment. That is the "
                        "room's job."},
            ],
        },
        {
            "q": "Which idea should you test first?",
            "remember": "The one one person can try in a week.",
            "answers": [
                {"text": "The one with the biggest possible saving", "ok": False,
                 "why": "Biggest usually means slowest and most political. Six "
                        "months later nothing has been learned and the meeting "
                        "is still monthly."},
                {"text": "The one a single person could test within a week",
                 "ok": True,
                 "why": "A week-long test by one person produces real "
                        "information quickly, without budget or approval. Two "
                        "of those beat one twelve-month proposal."},
                {"text": "The one everybody agrees with", "ok": False,
                 "why": "Universal agreement usually means it is familiar, "
                        "which usually means it has already been tried in some "
                        "form."},
                {"text": "The most unusual one on the list", "ok": False,
                 "why": "Unusual is worth keeping on the list, not necessarily "
                        "worth doing first. Testability is the better sorting "
                        "criterion."},
            ],
        },
        {
            "q": "What must not go in the prompt?",
            "remember": "Ideas do not need our real figures.",
            "answers": [
                {"text": "A one-sentence description of the problem",
                 "ok": False,
                 "why": "Essential. Without it you get generic ideas about "
                        "cost reduction in general, which is exactly what you "
                        "already had."},
                {"text": "Our margins, vendor rates and volumes", "ok": True,
                 "why": "They would sharpen the suggestions slightly and they "
                        "are among the most commercially sensitive numbers we "
                        "hold. The ideas are available without them."},
                {"text": "The type of operation, such as a warehouse",
                 "ok": False,
                 "why": "General context with nothing confidential in it. It "
                        "makes the ideas relevant without identifying anything "
                        "about us."},
                {"text": "The constraint that there is no budget this year",
                 "ok": False,
                 "why": "A useful constraint and not a secret. It stops half "
                        "the list being capital projects you cannot pursue."},
            ],
        },
        {
            "q": "When is generating the wrong move?",
            "remember": "More options do not fix a lack of commitment.",
            "answers": [
                {"text": "When the problem is technical", "ok": False,
                 "why": "Technical problems benefit from range as much as any "
                        "other. You simply need somebody technical to strike "
                        "the impossible ones afterwards."},
                {"text": "When everybody knows what to do and nobody will "
                         "commit", "ok": True,
                 "why": "That is a decision problem, not an options problem. "
                        "Twenty more ideas give the room something new to "
                        "avoid deciding about."},
                {"text": "When the meeting is short", "ok": False,
                 "why": "A short meeting is where a pre-made list helps most. "
                        "Generate beforehand and spend the meeting sorting."},
                {"text": "When you already have four ideas", "ok": False,
                 "why": "Four ideas that keep failing is the textbook case for "
                        "generating twenty. That is precisely the situation "
                        "this is for."},
            ],
        },
    ],

    "recap": {
        "title": "Brainstorming on one screen",
        "points": [
            ("Twenty beats four",
             "Meetings stall because people bring their best idea, not twenty "
             "rough ones."),
            ("Ask for range deliberately",
             "Five obvious, ten unusual, five impractical. The last five earn "
             "their place."),
            ("Nobody owns a generated idea",
             "Seniority and ego stop deciding which options survive."),
            ("Strike before you discuss",
             "Already tried, no budget, not permitted. Striking is fast."),
            ("Test what one person can try in a week",
             "Two quick tests beat one twelve-month proposal."),
            ("It does not know our constraints",
             "Contracts, licences and equipment are the room's job, not its "
             "own."),
        ],
        "oneliner": "Use it for quantity. Use the room for judgement.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("bulb", "The twenty-ideas prompt",
             "Five obvious, ten unusual, five impractical."),
            ("list", "The sorting prompt",
             "Testable in a week, needs budget, not worth pursuing."),
            ("cycle", "The deadlock prompt",
             "Five options that are neither A nor B, plus two combinations."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-10, Planning & Personal Productivity. "
                "Turning a long list of intentions into a week you can "
                "actually finish.",
    },

    "glossary": [
        ("Divergent thinking", "Producing many options without judging them. "
                               "The part AI does well."),
        ("Convergent thinking", "Narrowing many options down to a decision. "
                                "The part the room does."),
        ("Constraint", "Something that rules an option out: a contract, a "
                       "licence, a budget, a piece of equipment."),
        ("Prompt", "Everything you type in: the problem, the range you want "
                   "and the format."),
        ("Output", "What comes back. Raw material, none of which has been "
                   "checked against reality."),
        ("Deadlock", "Two stated positions and no movement. Usually social "
                     "rather than analytical."),
    ],
}
