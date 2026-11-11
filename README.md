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
| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `06137279-1d5b-4bc7-8f87-9c3a864bd50e` | human | 0.000 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `80ac57f4-15e3-404b-9bf4-657323e162cc` | human | 0.000 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c5638702-ea2e-4b15-8c60-824fe761432c` | unsure | 0.000 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2cc9b9c7-5896-490c-83c3-7d01a9e4d6b0` | unsure | 0.000 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `47c1c8b2-6652-4b67-b4f4-00c30d23513d` | human | 0.000 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `52281a18-bcd5-4b48-90ce-4267f1ed8a87` | human | 0.000 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c373bbb1-307a-438f-ad55-d1d0dad4c506` | unsure | 0.000 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `31053b5e-8be0-45c3-bb9a-b1c865357e9e` | human | 0.000 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7229aa40-227d-4986-9bfd-17fc7aa5819f` | unsure | 0.000 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `bea700df-ef28-4b6f-8fea-0e558e6ca85f` | ai | 0.000 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3699ea08-6d35-4048-a76e-5be71aa6316f` | unsure | 0.000 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `a737bcd3-9371-479b-b232-8fba659446fd` | unsure | 0.000 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `67564e6c-7265-4658-ad26-140348a51d07` | unsure | 0.000 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5e335c9a-5caf-473c-a66f-ad330ed4dc7d` | unsure | 0.000 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `0e087194-15af-46c1-941a-9e3cab770878` | ai | 0.000 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `8f1640ad-153f-424c-b9c6-a0a61cb0843c` | unsure | 0.000 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `2c84b9dc-d7d6-4b35-af33-f7413923d9c9` | unsure | 0.000 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `0df4337a-b9d0-475a-b7d8-a8103ee7ba09` | human | 0.000 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ec2d0854-f57d-4824-8ad4-ed9d1d2b5051` | unsure | 0.000 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e55b89f6-a304-403f-bd3d-7eab457c88f3` | human | 0.000 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `80f99747-51fc-4eed-bdc2-f4da522d078a` | unsure | 0.000 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4e02d62f-7b31-44bd-9191-efce62bcf539` | unsure | 0.000 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ab9f34fd-13f9-4236-8b54-8fde61be5db9` | human | 0.000 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `7cfb13ef-53be-4154-8611-afc23a57bcc3` | unsure | 0.000 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `9fb9a6a4-7735-44fd-8188-dfaa2672f218` | human | 0.000 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `384bd8d7-5d9a-4467-8659-3faeb51f9b38` | human | 0.000 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `034dc305-f497-44ca-8530-1f9834f0d704` | unsure | 0.000 | HELD |
| MF06 | malformed | text is emoji only | 200 | `a2591cf4-5b18-4528-b054-a11ab3ad95c5` | ai | 0.000 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `d5a50863-21d4-4f44-b988-de8b54c4627c` | ai | 0.000 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `14bfb005-4a7e-4360-8a68-e388e61bc766` | ai | 0.000 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `e704b529-411a-4a4c-aaac-a013925f1b84` | human | 0.000 | HELD |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `5bbea56c-3504-4a90-8e31-94c7c21d777c` | human | 0.000 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4ac4a3c6-7772-4717-acd6-f11cfd7751a0` | human | 0.000 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c21b9f21-3a83-4db0-a5be-75742447825a` | human | 0.000 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `074d9cb3-191f-43cd-995c-f3c3464dada4` | human | 0.000 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f86c3153-5748-4a34-a9e2-e195e0f4ac9f` | human | 0.000 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b4f3842e-fd43-4218-8889-24d521beeeff` | human | 0.000 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"combined_score": 0.5029, "content_id": "bfc88ed8-b79a-402c-ae75-3fed07ec0ad7", "creator_id": "giao_1", "guess": "unsure", "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.", "model_score": 0.434, "status": "decided", "style_score": 0.5718, "timestamp": "2026-11-04T05:47:12+00:00", "word_count": 25}
{"content_id": "a66bd206-2bd6-47ad-8515-02f8e054fdba", "creator_id": "giao_1", "event": "appeal", "reasoning": "I wrote this entirely myself.", "status": "under_review", "timestamp": "2026-11-04T05:57:33+00:00"}
{"combined_score": 0.3111, "content_id": "d9b4fc80-0c24-4cf6-b733-2899e05b70a8", "creator_id": "flood_tester", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.2588, "status": "decided", "style_score": 0.3635, "timestamp": "2026-11-04T23:29:12+00:00", "word_count": 27}
{"creator_id": "flood_tester", "event": "rejected", "limit": "6 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-04T23:29:15+00:00"}
{"combined_score": 0.1635, "content_id": "220c82be-5e44-4995-bd1d-bdbed72cf305", "creator_id": "attacker_EV01", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.1635, "status": "decided", "style_score": 0.5348, "timestamp": "2026-11-10T00:07:17+00:00", "word_count": 84}
{"combined_score": 0.7338, "content_id": "377ca543-44f6-40ce-8615-d7c14d042e89", "creator_id": "attacker_EV10", "guess": "ai", "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.", "model_score": 0.9792, "status": "decided", "style_score": 0.7338, "timestamp": "2026-11-10T00:07:20+00:00", "word_count": 78}
{"creator_id": "attacker_MF01", "event": "rejected", "reason": "empty_text", "status": "rejected", "timestamp": "2026-11-10T00:07:25+00:00"}
{"combined_score": 0.9224, "content_id": "93f3e936-d2bb-4511-b697-fb7d384f7a44", "creator_id": "attacker_MF08", "guess": "ai", "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.", "model_score": 0.9876, "status": "decided", "style_score": 0.8573, "timestamp": "2026-11-10T00:07:31+00:00", "word_count": 11330}
{"creator_id": "unknown", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-10T00:07:31+00:00"}
{"combined_score": 0.0287, "content_id": "40003a5f-5320-46aa-bb08-56fd9177ec9c", "creator_id": "attacker_flood", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.0287, "status": "decided", "style_score": 0.5758, "timestamp": "2026-11-10T00:07:31+00:00", "word_count": 9}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

A false positive where a genuine human writer's submission (such as a formal essay or technical document) gets misclassified as high-confidence AI due to predictable phrasing or low perplexity. Telling a hardworking author that their authentic work is an AI fabrication without room for immediate nuance damages trust and places an unfair burden on them to file an appeal.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->
- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-10 17:59

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | <= 1 of 10 | 1/10  | 1/10  | 1/10  | MET |
| 2. label coverage | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. bad input handling | 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 3. appeal path logging | - | - | - | - | UNMEASURABLE |
| 5. score spread separation | >= 0.40 | 0.325  | 0.325 | 0.325  | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.0,
    "model_score": 0.6525,
    "style_score": 0.5716,
    "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
    "sent": "I prayed to God that He will lead us to where we belong, whether that "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.0504,
    "style_score": 0.5608,
    "label": "We think this was probably written by a person.",
    "sent": "I want peace and space for growth."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7458,
    "style_score": 0.5658,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "You know, when you see your loved ones doing well, it radiates that po"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.2727,
    "style_score": 0.6,
    "label": "We think this was probably written by a person.",
    "sent": "Two peas in a pod"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.3613,
    "style_score": 0.4583,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "This year's midterm election, I generally think neither major parties "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.2911,
    "style_score": 0.5456,
    "label": "We think this was probably written by a person.",
    "sent": "You have a caring nature, which I really love it."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.6122,
    "style_score": 0.4634,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "I like going to my church. I found a purpose there. It's actually quit"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.1256,
    "style_score": 0.589,
    "label": "We think this was probably written by a person.",
    "sent": "I think of you whenever I go on hiking or just take morning walk that "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7172,
    "style_score": 0.4434,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "Love is a beautiful pain. I am willing to go through ups and downs in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5725,
    "style_score": 0.442,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "Do I feel that all my prayers have been answered? I have yet to know. "
  }
]
```
### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.4586,
    "style_score": 0.5897,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "The implementation of the proposed framework requires careful consider"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.0,
    "model_score": 0.6566,
    "style_score": 0.5658,
    "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
    "sent": "I went outside for a walk this morning."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.0514,
    "style_score": 0.5804,
    "label": "We think this was probably written by a person.",
    "sent": "This text might have some mixed patterns or ambiguous elements here."
  }
]
```
### bad input handling

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "test"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "hello world"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"text\": null, \"creator_id\": \"eval_null\"}"
  }
]
```
### appeal path logging

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.0271,
    "style_score": 0.5852,
    "label": "We think this was probably written by a person.",
    "sent": "This text will be submitted to generate an ID for testing the appeal p"
  }
]
```
### score spread separation

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5027,
    "style_score": 0.5365,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "I have plans for us, but without you, they are all meaningless."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.6809,
    "style_score": 0.4854,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "The phrase 'I love you' for me includes several layers of meaning. It "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.2783,
    "style_score": 0.5671,
    "label": "We think this was probably written by a person.",
    "sent": "Quick reminder: the fastest way to reduce stress with work is finishin"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.2391,
    "style_score": 0.4601,
    "label": "We think this was probably written by a person.",
    "sent": "People say that money goes then comes back. But I think my money has A"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.0,
    "model_score": 0.6721,
    "style_score": 0.6049,
    "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
    "sent": "They say I was born from the stage, but I was actually born at the hos"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5563,
    "style_score": 0.5865,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "The implementation of the proposed framework requires careful consider"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.3458,
    "style_score": 0.5716,
    "label": "We think this was probably written by a person.",
    "sent": "Furthermore, it is important to analyze the overarching systemic impli"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.4719,
    "style_score": 0.5719,
    "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
    "sent": "In conclusion, the data demonstrates a statistically significant corre"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.2202,
    "style_score": 0.586,
    "label": "We think this was probably written by a person.",
    "sent": "Optimization algorithms facilitate enhanced performance across diverse"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.0,
    "model_score": 0.0301,
    "style_score": 0.586,
    "label": "We think this was probably written by a person.",
    "sent": "This methodology establishes a robust paradigm for scalable enterprise"
  }
]
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

Criterion #5 Miss (Score Spread Separation)
- **Stage:** The combining rule and signal two (`scoring.py::combine_signals` and `stylometry.py`).
- **Mechanism:** The strict split threshold ($0.15$) and safety override mechanism default ambiguous text scores toward the lower, human-safe bound. This compresses the score distribution across both sets, resulting in a mean score gap of 0.325 rather than the targeted 0.40.

Criterion #3 Unmeasurable (Appeal Path Logging)
- **Stage:** The test harness and route (`run_eval.py` and `app.py::appeal`).
- **Mechanism:** The automated evaluation script only submits text to the `/submit` endpoint in a single step and lacks the multi-step flow required to trigger and test the `POST /appeal` endpoint, rendering the criterion unmeasurable by the harness.

Broken Attacks (MF02, RQ03, RQ04, RQ05, RQ07, RQ12 — HTTP 500 Errors)
- **Stage:** The route (`app.py::submit`).
- **Mechanism:** Non-string payloads (such as single characters, numbers, lists, `null` values, arrays, and deeply nested objects) bypassed input type validation. When text feature extraction and signal functions attempted to process these invalid data types, unhandled Python exceptions crashed the Flask application, resulting in a 500 server error instead of a clean 400 bad request.

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
