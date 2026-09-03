# -*- coding: utf-8 -*-
"""PS-06 — Problem-Solving. Content only."""

DECK = {
    "module_code": "PS-06",
    "area": "04-professional-skills",
    "filename": "04-06-problem-solving.pptx",
    "title": "Problem-Solving",
    "subtitle": "Finding the actual cause before you spend a fortnight fixing "
                "the wrong thing.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "flow",
    "cover_image": "assets/hero-problem-solving.jpg",

    "why": {
        "title": "Bhavesh fixes it three times",
        "icon": "cycle",
        "scenario": "Bhavesh maintains packing machines in Rajkot. The sealer "
                    "keeps jamming. He replaces the belt in March, the roller "
                    "in May and the motor in July. It jams again in August. "
                    "Nobody has asked why it started jamming in February.",
        "cost": "Three repairs, three shutdowns, and the same fault.",
        "fix": "Five questions before any money is spent.",
    },

    "outcomes": [
        ("eye", "Separate the symptom from the cause, deliberately"),
        ("list", "Use five questions to reach the real cause in ten minutes"),
        ("check", "Test a suspected cause before committing to a fix"),
        ("clock", "Know when to stop analysing and just try something"),
        ("person", "Write up a problem so somebody else can help you"),
    ],

    "sections": [
        ("Symptom and cause", "Fixing the wrong thing", "s_symptom"),
        ("Five whys", "Ten minutes, no cost", "s_why"),
        ("Testing before spending", "The cheap experiment", "s_test"),
        ("When to stop analysing", "Analysis has a limit", "s_stop"),
        ("Do this now", "Work through a real problem", "s_do"),
        ("Choose what you'd do", "A breakdown decision", "scenario"),
        ("Watch this", "An 8-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_symptom",
            "label": "Symptom and cause",
            "title": "Fixing what you can see",
            "lead": "The symptom is what interrupts you. The cause is usually "
                    "somewhere quieter, and further back.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "The symptom", "tone": "bad",
                    "title": "What you notice",
                    "items": [
                        "The sealer jams",
                        "The report is late every month",
                        "The customer complains about damage",
                        "Fixing this brings it back next month",
                    ],
                },
                "right": {
                    "tag": "The cause", "tone": "good",
                    "title": "What actually changed",
                    "items": [
                        "Film thickness changed with a new supplier",
                        "The source data arrives two days late",
                        "Pallets are being stacked one layer higher",
                        "Fixing this ends it permanently",
                    ],
                },
            },
        },
        {
            "label": "Symptom and cause",
            "title": "The question nobody asks",
            "visual": {
                "type": "flow",
                "steps": [
                    ("It broke", "Everyone focuses here, because it hurts."),
                    ("When did it start?", "The single most useful question "
                                           "there is."),
                    ("What changed then?", "Suppliers, people, settings, "
                                           "volumes, weather."),
                    ("That is your candidate", "Test it before spending "
                                               "anything."),
                ],
            },
        },
        {
            "anchor": "s_why",
            "label": "Five whys",
            "title": "Five whys, ten minutes",
            "gloss": ["Root cause"],
            "visual": {
                "type": "prompt",
                "header": "Copy this structure",
                "text": "The sealer jams. Why? — The film is not feeding "
                        "evenly. Why? — The tension arm is slipping. Why? — "
                        "The film roll is heavier than before. Why? — We "
                        "changed supplier in February. Why? — The new film is "
                        "20 microns thicker.",
                "caption": "Stop when the answer is something you can actually "
                           "change.",
                "why": [
                    "Each answer must be a fact, not a guess.",
                    "If you cannot answer a why, that is what to go and check.",
                    "Five is a guide. Sometimes three is enough.",
                ],
            },
        },
        {
            "label": "Five whys",
            "title": "Where the chain goes wrong",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Answering with a guess",
                     "One guessed link and everything after it is fiction, "
                     "confidently pursued."),
                    ("Stopping at \"human error\"",
                     "Almost never the end. Why was the error possible, and "
                     "why was it not caught?"),
                    ("Stopping at something you cannot change",
                     "\"Because it is monsoon season\" ends the chain without "
                     "producing an action."),
                    ("Only asking why once",
                     "The first answer is the symptom wearing a different "
                     "coat."),
                ],
            },
        },
        {
            "anchor": "s_test",
            "label": "Testing before spending",
            "title": "The cheap experiment first",
            "lead": "Before you spend money or a fortnight, find the smallest "
                    "test that would prove you wrong.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "REVERSE IT — put the old film back on one machine for a "
                    "day",
                    "ISOLATE IT — run one line with the suspected cause "
                    "removed",
                    "COMPARE — is the fault on all machines, or only this one?",
                    "TIMELINE — does the fault date match the change date?",
                ],
            },
        },
        {
            "label": "Testing before spending",
            "title": "One day beats three repairs",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Fixing without testing",
                "bad": [
                    "Replace the belt. It jams again in six weeks.",
                    "Replace the roller. It jams again in eight weeks.",
                    "Three parts, three shutdowns, same fault in August.",
                ],
                "good_tag": "One day of testing",
                "good": [
                    "Run the old film on one machine for a single shift.",
                    "No jams on that machine. Jams on the other three.",
                    "Cause confirmed for the cost of one day and no parts.",
                ],
                "note": "A test that could prove you wrong is worth more than "
                        "three fixes that assumed you were right.",
            },
        },
        {
            "anchor": "s_stop",
            "label": "When to stop analysing",
            "title": "Analysis has a limit",
            "visual": {
                "type": "tree",
                "question": "Is the fix cheaper than another day of "
                            "investigation?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Just try it",
                    "detail": "If a change costs an hour and reverses easily, "
                              "trying it is the cheapest experiment available. "
                              "Analysis is not free either.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Keep digging",
                    "detail": "If the fix costs real money, a shutdown, or is "
                              "hard to undo, another day of asking why is very "
                              "well spent indeed.",
                },
            },
        },
        {
            "label": "When to stop analysing",
            "title": "Write it up so others can help",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this problem write-up",
                "text": "PROBLEM: what is happening, in one sentence. STARTED: "
                        "the date it first appeared. CHANGED THEN: anything "
                        "that changed around that date. RULED OUT: what we "
                        "have already tested and eliminated. NEXT TEST: the "
                        "cheapest thing that would prove us wrong.",
                "caption": "Five lines. Anybody can now help you without a "
                           "meeting.",
                "out_title": "Why it works",
                "out": [
                    "\"Started\" and \"changed then\" together do most of the "
                    "diagnostic work.",
                    "\"Ruled out\" stops three colleagues suggesting the same "
                    "thing.",
                    "\"Next test\" turns a complaint into a plan somebody can "
                    "act on.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: one real problem",
            "visual": {
                "type": "steps",
                "items": [
                    "Pick something that keeps coming back.",
                    "Write down exactly when it first appeared.",
                    "List everything that changed in that fortnight.",
                    "Design the cheapest test that would prove you wrong.",
                ],
                "prompt": "I have a recurring problem. Ask me one question at "
                          "a time to work through five whys. Do not suggest "
                          "causes yourself and do not skip ahead. If I answer "
                          "with a guess rather than a fact, say so and ask how "
                          "I could check it.",
                "caption": "\"Do not suggest causes yourself\" is what keeps "
                           "this honest.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Ask when it started before asking what is wrong.",
                    "Write the five whys down. Chains kept in the head skip "
                    "links.",
                    "Design a test that could prove you wrong, not right.",
                    "Record what you ruled out, so nobody retests it.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Replacing the part that broke",
                     "The part broke for a reason. The new one will meet the "
                     "same reason."),
                    ("Stopping the chain at human error",
                     "The real question is why the error was possible and why "
                     "nothing caught it."),
                    ("Testing to confirm rather than to disprove",
                     "You will find confirmation for almost any theory if that "
                     "is what you look for."),
                    ("Not writing down what was ruled out",
                     "Three people test the same thing across two months and "
                     "nobody knows."),
                    ("Analysing something that costs an hour to just try",
                     "Analysis is not free. Cheap, reversible fixes are their "
                     "own experiment."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Problems that are not technical",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "The late report",
                     "sub": "Started in April. What changed? The source data "
                            "moved to a different team."},
                    {"icon": "person", "label": "The repeated complaint",
                     "sub": "Started when a shift pattern changed. Nobody "
                            "connected the two."},
                    {"icon": "sheet", "label": "The rising rejection rate",
                     "sub": "Started with a new material grade, three weeks "
                            "before anyone noticed."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The problem-solving rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Ask when it started, find what changed then, and "
                            "test that before you spend anything.",
                "sub": "Most recurring problems at work have a start date and "
                       "a change beside it.",
                "cols": 3,
                "items": [
                    "When did it start?",
                    "What changed then?",
                    "What would prove me wrong?",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Wednesday, 7:20 am",
        "situation": "The sealer has jammed again, the third time this "
                     "quarter. Production is stopped. Your supervisor wants to "
                     "order a new motor today.",
        "choices": [
            {
                "text": "Order the motor — it is the one part not yet "
                        "replaced.",
                "tone": "bad",
                "headline": "The fourth part, and the same fault",
                "consequence": "The motor arrives in nine days, is fitted over "
                               "a weekend, and the machine jams again in "
                               "October. Three parts and a motor have now been "
                               "replaced, and nobody has yet asked what "
                               "changed in February.",
                "rule": "Replacing parts in sequence is not diagnosis. It is "
                        "elimination by spending.",
            },
            {
                "text": "Ask when it started, find what changed, and test that "
                        "today.",
                "tone": "good",
                "headline": "One shift, and the cause is confirmed",
                "consequence": "It started in February. The film supplier "
                               "changed in February. You run the old film on "
                               "this machine for one shift and it does not "
                               "jam. The fix is a tension setting, not a "
                               "motor.",
                "rule": "A start date plus a change beside it solves most "
                        "recurring problems.",
            },
            {
                "text": "Order the motor and investigate in parallel.",
                "tone": "ok",
                "headline": "Safe, and it usually stops the investigating",
                "consequence": "Reasonable when a shutdown is genuinely "
                               "expensive. In practice, once the part is "
                               "ordered the pressure lifts and the "
                               "investigation quietly stops. If you do this, "
                               "book the test before you place the order.",
                "rule": "Ordering the part removes the urgency that was "
                        "driving the diagnosis.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=t7FcK8jV2yA",
        "title": "The 5 Whys Explained - Root Cause Analysis",
        "channel": "EPM",
        "duration": "8:25",
        "heading": "Eight minutes on five whys",
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
            "q": "What is the most useful first question?",
            "remember": "When did it start?",
            "answers": [
                {"text": "What is broken?", "ok": False,
                 "why": "You usually already know what is broken — that is the "
                        "symptom that interrupted you. Knowing it rarely "
                        "points at the cause."},
                {"text": "When did this start happening?", "ok": True,
                 "why": "A start date lets you ask what changed around it, and "
                        "changes are where causes live. It is the single "
                        "highest-value question in the whole method."},
                {"text": "Who was operating it?", "ok": False,
                 "why": "It invites human error as an answer, which is almost "
                        "always the end of a chain that should have continued "
                        "for two more steps."},
                {"text": "How much will it cost to fix?", "ok": False,
                 "why": "An important question later. Asked first, it pushes "
                        "you towards fixing the symptom because that is the "
                        "thing with a price on it."},
            ],
        },
        {
            "q": "Why not stop at \"human error\"?",
            "remember": "Ask why it was possible, and why nothing caught it.",
            "answers": [
                {"text": "It is unfair to the person involved", "ok": False,
                 "why": "Fairness matters, and it is not the analytical "
                        "reason. Even where somebody did make a mistake, "
                        "stopping there produces no fix."},
                {"text": "It produces no change you can make", "ok": True,
                 "why": "\"Be more careful\" is not a fix. The useful questions "
                        "are why the error was possible at all, and why "
                        "nothing downstream caught it before it mattered."},
                {"text": "People rarely make mistakes", "ok": False,
                 "why": "People make mistakes constantly. Good processes "
                        "assume that and are built so the mistake is caught "
                        "cheaply."},
                {"text": "It is usually not true", "ok": False,
                 "why": "It is often perfectly true and still not the end of "
                        "the chain. Truth and usefulness are different things "
                        "here."},
            ],
        },
        {
            "q": "What makes a good test?",
            "remember": "It could prove you wrong.",
            "answers": [
                {"text": "It confirms your theory", "ok": False,
                 "why": "You can find confirmation for almost any theory if "
                        "that is what you are looking for. Confirmation is the "
                        "cheapest and least informative result."},
                {"text": "It would show you were wrong, if you were", "ok": True,
                 "why": "Running the old film for one shift either clears the "
                        "fault or does not. Both outcomes teach you something, "
                        "which is what makes it worth a day."},
                {"text": "It is thorough and takes a week", "ok": False,
                 "why": "Cheap and fast beats thorough here. A one-shift test "
                        "you actually run is worth more than a perfect one "
                        "nobody schedules."},
                {"text": "It fixes the problem at the same time", "ok": False,
                 "why": "If a test fixes it, you learn nothing about why — and "
                        "you will not know what to do when it returns on a "
                        "different machine."},
            ],
        },
        {
            "q": "When should you stop analysing?",
            "remember": "When trying it is cheaper than another day of "
                        "thinking.",
            "answers": [
                {"text": "When you are confident in your theory", "ok": False,
                 "why": "Confidence is not the criterion — people are "
                        "confident about wrong theories all the time. Cost and "
                        "reversibility are."},
                {"text": "When the fix is cheap and easy to reverse", "ok": True,
                 "why": "If a change costs an hour and can be undone, trying "
                        "it is the cheapest experiment available. Analysis "
                        "consumes time too."},
                {"text": "When your manager wants an answer", "ok": False,
                 "why": "Pressure is real and it is not evidence. This is "
                        "exactly the moment the five-line write-up helps, "
                        "because it shows progress without a false "
                        "conclusion."},
                {"text": "After exactly five whys", "ok": False,
                 "why": "Five is a rule of thumb, not a count. Stop when you "
                        "reach something you can actually change, whether that "
                        "is at three or at seven."},
            ],
        },
        {
            "q": "What does \"ruled out\" achieve?",
            "remember": "It stops three people retesting the same thing.",
            "answers": [
                {"text": "It proves you worked hard", "ok": False,
                 "why": "Not the point, and it would be a poor reason to keep "
                        "records. The value is entirely in what other people "
                        "then do not repeat."},
                {"text": "It stops colleagues repeating the same test",
                 "ok": True,
                 "why": "Without it, three people test the belt across two "
                        "months and none of them knows the others did. Written "
                        "down, the investigation moves forward instead of in "
                        "circles."},
                {"text": "It shortens the write-up", "ok": False,
                 "why": "It lengthens it slightly, and saves far more time "
                        "than the extra two lines cost."},
                {"text": "It assigns responsibility", "ok": False,
                 "why": "Nothing to do with responsibility. It is a record of "
                        "what the evidence has already eliminated."},
            ],
        },
    ],

    "recap": {
        "title": "Problem-solving on one screen",
        "points": [
            ("Symptom is not cause",
             "The symptom interrupts you. The cause is quieter and further "
             "back."),
            ("Ask when it started",
             "Then ask what changed around that date. Most causes live "
             "there."),
            ("Five whys, written down",
             "Chains kept in your head skip links. Each answer must be a "
             "fact."),
            ("Never stop at human error",
             "Ask why it was possible, and why nothing downstream caught it."),
            ("Test to be proved wrong",
             "One shift with the old film beats three replacement parts."),
            ("Write down what you ruled out",
             "Otherwise three colleagues test the same thing over two "
             "months."),
        ],
        "oneliner": "When did it start, what changed then, and what would "
                    "prove me wrong?",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("list", "The five whys chain",
             "Each answer a fact, stopping at something you can change."),
            ("doc", "The five-line write-up",
             "Problem, started, changed then, ruled out, next test."),
            ("check", "The cheap experiment",
             "Reverse, isolate, compare, check the timeline."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-07, Critical Thinking. Telling evidence from "
                "assertion, including in your own reasoning.",
    },

    "glossary": [
        ("Symptom", "What you notice when something is wrong. Usually not the "
                    "thing to fix."),
        ("Root cause", "The change that started it. Fixing this stops the "
                       "problem returning."),
        ("Five whys", "Asking why repeatedly, with a fact at each step, until "
                      "you reach something changeable."),
        ("Falsification", "Designing a test that would show you were wrong. "
                          "Worth more than confirmation."),
        ("Ruled out", "Something already tested and eliminated. Record it so "
                      "nobody repeats it."),
        ("Reversible", "A change you can undo cheaply. Reversible fixes make "
                       "good experiments."),
    ],
}
