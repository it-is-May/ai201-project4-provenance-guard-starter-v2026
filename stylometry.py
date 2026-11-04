"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re               # regular expressions
import statistics       # stdev


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies (Coefficient of Variation: stdev / mean).
    
    Returns:
        A float representing normalized sentence length variability.
        Lower values mean uniform sentence lengths (more AI-like).
    """
    s_list = sentences(text)
    # Edge case: 0 or 1 sentence has no spread at all
    if len(s_list) < 2:
        return 0.0
    
    lengths = [len(words(s)) for s in s_list]
    mean_len = statistics.mean(lengths)
    if mean_len == 0:
        return 0.0
        
    stdev = statistics.stdev(lengths)
    # Return coefficient of variation (stdev divided by mean)
    return stdev / mean_len


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words (Vocabulary richness).

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.
    """
    w_list = words(text)
    if not w_list:
        return 0.0
    return len(set(w_list)) / len(w_list)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to total text length.

    Returns:
        A float representing punctuation frequency.
    """
    if not text.strip():
        return 0.0
    
    # Count all non-word, non-whitespace characters (punctuation)
    punc_count = len(re.findall(r"[^\w\s]", text))
    return punc_count / len(text)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. Higher means more likely AI.
    Combined using Sentence Spread (40%), TTR (40%), and Punctuation Density (20%).
    """
    if not text.strip():
        return 0.5  # Neutral fallback for empty input

    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punc = punctuation_density(text)

    # 1. Invert and scale spread: low spread -> high AI score
    ai_spread_score = max(0.0, 1.0 - min(spread / 1.5, 1.0))

    # 2. Invert and scale TTR: low TTR -> high AI score
    ai_ttr_score = max(0.0, 1.0 - min(ttr * 1.2, 1.0))

    # 3. Punctuation density: lower/predictable density leans AI (normalized against a 0.15 max cap).
    ai_punc_score = max(0.0, 1.0 - min(punc / 0.15, 1.0))

    # 4. Weighted combination: 40% spread, 40% TTR, 20% punctuation
    combined = (0.4 * ai_spread_score) + (0.4 * ai_ttr_score) + (0.2 * ai_punc_score)

    return round(min(max(combined, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
