# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
**1. Request Received**: Client sends a `POST` request to `/submit` containing JSON (`text` and `creator_id`).

**2. Validation:** `/submit` handler checks that `JSON` body contains valid text (e.g., minimum length check).

**3. Signal 1 Evaluation (`detector.py`):** Runs the GPT-2 local model to measure text perplexity and outputs `model_score` (0.0 to 1.0).

**4. Signal 2 Evaluation (`stylometry.py`):** Computes sentence length spread, type-token ratio, and punctuation density to output `style_score` (0.0 to 1.0).

**5. Score Combination (`scoring.py`):** Combines `model_score` and `style_score` into a single `combined_score` via a weighted average. 

**6. Label Classification and Response:** Maps `combined_score` against thresholds to select a human-readable label (high-confidence human, unsure, or high-confidence AI) and generates a unique `content_id`.

**7. Audit Logging:** Writes the decision details to `logs/audit.jsonl` using `audit.py` and returns the structured `JSON` response to the client.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal (`detector.py`)

**What it measures:** Text perplexity (how predictable/expected the text is to a language model like GPT-2).

**Why that might differ between human and AI writing:** AI models output average, predictable token sequences. Humans use surprising, erratic, or distinct phrasing.

**What it can't see:** It rewards common words in short, plain sentences. Plain human writing (e.g., non-native English speakers, younger writers, simple prose) has low perplexity and gets falsely flagged as AI.

### Signal two — the style signal (`stylometry.py`)

**What it measures:** Structural shape of text (sentence length variance/spread, vocabulary richness/TTR, punctuation density).

**Why that might differ between human and AI writing:** AI text tends to have uniform sentence lengths and repetitive word variety. Human text is uneven and "lumpy".

**What it can't see:** Meaning/semantics. Simple surface tweaks (like inserting intentional typos, adding quotations, or breaking sentences) alter the structural stats without changing content.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Use a 50/50 weighted average when signals align, but if they disagree by more than the split threshold, default to the more human-safe (lower) score to protect real writers from false positives.

**The numbers:** Weights = 0.5 model, 0.5 style; Split Threshold = 0.15.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
- **The text tested:** "I tell people that good politics doesnt negatively affect you, and as a normal person just living your life, you probably wont even notice it. But BAD politics will. Bad policies have to be so harmful that you actually feel their effects, lol. Good politics is like a guardian angel: its quietly working behind the scenes, doing its job without you even noticing. Bad politics, on the other hand, will slap you right in the face, lol."
- **The signal scores:** 
  - Model Signal: `0.6659` (leaning AI)
  - Style Signal: `0.4561` (leaning human)
- **The split gap:** The absolute difference between them was `0.2098`, which exceeds our `SPLIT_THRESHOLD` of `0.15`.
- **What the rule did:** Because the gap was greater than 0.15, the conditional logic triggered and defaulted to the lower, more human-safe score (`0.4561`), preventing a false accusation and prioritizing protection for the human writer.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 <= score < 0.40 | "This writing appears natural and human-authored. No further verification is needed." |
| unsure | 0.40 <= score <= 0.60 | "Our automated checks found mixed signals in this text. If this was flagged by mistake, you can submit an appeal for human review." |
| high-confidence AI | 0.60 < score <= 1.00 | "This text closely matches patterns commonly produced by AI models. If this is an error, please file an appeal." |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
It explicitly avoids accusatory language, acknowledges system limitations, and gives the writer a clear, non-stressful path to appeal.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl.exe -X POST [http://127.0.0.1:5000/submit](http://127.0.0.1:5000/submit) -H "Content-Type: application/json" -d '{"text": "I wrote this quick update on our project timeline completely by hand.", "creator_id": "giao_1"}'
```

```json
{
  "combined_score": 0.1619,
  "confidence": 0.0,
  "content_id": "a66bd206-2bd6-47ad-8515-02f8e054fdba",
  "guess": "human",
  "label": "We think this was probably written by a person.",
  "model_score": 0.1619,
  "style_score": 0.5807
}
```

**An appeal**

```bash
$$ curl.exe -X POST [http://127.0.0.1:5000/appeal](http://127.0.0.1:5000/appeal) -H "Content-Type: application/json" -d '{"content_id": "a66bd206-2bd6-47ad-8515-02f8e054fdba", "reasoning": "I wrote this entirely myself."}'
```

```json
{
  "content_id": "a66bd206-2bd6-47ad-8515-02f8e054fdba",
  "message": "Your appeal has been received and logged for human review.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5000/log?limit=1"
```

```json
  "count": 1,
  "entries": [
    {
      "content_id": "a66bd206-2bd6-47ad-8515-02f8e054fdba",
      "creator_id": "giao_1",
      "event": "appeal",
      "reasoning": "I wrote this entirely myself.",
      "status": "under_review",
      "timestamp": "2026-11-04T05:57:33+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Assistance in setting up the initial stylometry function to calculate sentence length variance and type-token ratio.
- *What came back:* A snippet utilizing standard string splitting and basic statistical variance calculations.
- *What I changed:* Adjusted the tokenization logic to properly handle punctuation and edge cases with short sentences so it doesn't throw division-by-zero errors.

**Moment 2**

- *What I asked for:* Guidance on structuring the `/appeal` endpoint error handling when a `content_id` cannot be found in the audit log.
- *What came back:* A conditional check using `audit.entries_for(content_id)` and returning a 404 response.
- *What I changed:* Added extraction of the original `creator_id` from the log entry to fulfill the signature requirement of `audit.log_appeal()`.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 requests per minute, 100 requests per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
A human writer drafting and manually submitting text for provenance analysis takes time to edit and review changes, rarely exceeding 2 to 4 submissions in a single minute. A low per-minute cap of 5 instantly blocks rapid automated script bursts trying to map scoring thresholds or flood the endpoint. Additionally, a ceiling of 100 requests per day accommodates intensive writing sessions where an author iteratively tests multiple chapters or paragraph variations throughout a long workday, providing ample headroom for normal daily use while protecting the service against sustained background scraping.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
Per `creator_id`. 

- **Pros:** Isolates limits to individual user accounts. Unlike IP address-based limiting, it prevents an entire household, college dorm, or shared office network from being blocked if one legitimate user is heavy-testing their work.
- **Cons:** It can be vulnerable to automated scripts that dynamically generate thousands of fake `creator_id` strings (e.g., `bot_001`, `bot_002`) to bypass the per-user rate limit. 
- **Why I chose it:** Despite the spoofing vulnerability, tracking per `creator_id` makes the most sense for an authorship verification platform because it correctly ties submissions to user identity and avoids collateral damage on shared networks.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
