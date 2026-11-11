"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I prayed to God that He will lead us to where we belong, whether that is together or separate.",
            "I want peace and space for growth.",
            "You know, when you see your loved ones doing well, it radiates that positive energy to you, which makes you happy too",
            "Two peas in a pod",
            "This year's midterm election, I generally think neither major parties are good. The middle class still suffers in this war among the rich and politicians. I can do so much by living up to my Catholic belief, being kind to those around me, maintaining my neutral position in politics.",
            "You have a caring nature, which I really love it.",
            "I like going to my church. I found a purpose there. It's actually quite nice to know more about God.",
            "I think of you whenever I go on hiking or just take morning walk that how I can share this level of refreshness with you.",
            "Love is a beautiful pain. I am willing to go through ups and downs in life with you. Maybe it is a selfish me that wants to stay with you even when you push me away.",
            "Do I feel that all my prayers have been answered? I have yet to know. I got immediate answer for some of my prayers, but some require more time for me understand God's work behind the scene. All I can do is entrusting all my life, worries, and concerns into His Hand."
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "The implementation of the proposed framework requires careful consideration of several key statistical and computational factors.",
            "I went outside for a walk this morning.",
            "This text might have some mixed patterns or ambiguous elements here.",
        ],
    },
    {
        "name": "bad input handling",
        "criterion": 4,
        "bodies": [
            {"text": "", "creator_id": "eval_empty"},
            {"creator_id": "eval_missing"},
            {"text": "test", "creator_id": "eval_1word"},
            {"text": "hello world", "creator_id": "eval_2words"},
            {"text": None, "creator_id": "eval_null"},
        ],
    },
    {
        "name": "appeal path logging",
        "criterion": 3,
        # Note: If your appeal test requires a manual submission first or specific ID tracking, 
        # add your test text here to trigger the initial log entry.
        "texts": [
            "This text will be submitted to generate an ID for testing the appeal path log reliability."
        ],
    },
    {
        "name": "score spread separation",
        "criterion": 5,
        "texts": [
            # 5 plain human writing samples
            "I have plans for us, but without you, they are all meaningless.",
            "The phrase 'I love you' for me includes several layers of meaning. It includes 'I miss you, love'. It also means 'Good morning' if sent or said in the morning. And it also means 'Good night, sweet drams' if send or said at night.",
            "Quick reminder: the fastest way to reduce stress with work is finishing the work.",
            "People say that money goes then comes back. But I think my money has Alzheimer's. It forgot to return.",
            "They say I was born from the stage, but I was actually born at the hospital.",
            # 5 GPT-2 generated text prompts
            "The implementation of the proposed framework requires careful consideration of several key factors.",
            "Furthermore, it is important to analyze the overarching systemic implications comprehensively.",
            "In conclusion, the data demonstrates a statistically significant correlation between variables.",
            "Optimization algorithms facilitate enhanced performance across diverse computational workloads.",
            "This methodology establishes a robust paradigm for scalable enterprise architecture deployment."
        ],
    }

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
