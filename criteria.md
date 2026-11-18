# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. At most 1 of 10 plain human samples incorrectly flagged as AI across 3 seeds

<!-- Your criterion. It must name a number. -->
(False Positives)

**Why this target:**
Because `detector.py` uses GPT-2 perplexity, it naturally rewards simple vocabulary and short sentences. Since plain human writing is the primary victim of false positives, holding a strict 10% ceiling ensures my threshold won't disproportionately penalize writers with simpler or non-native styling.


---

## 2. All 3 labels triggered at least once across a 15-item test suite

<!-- Your criterion. -->
(Label Coverage)

**Why this target:**
A safety layer with an `unsure` band is useless if it never triggers. This criterion forces my combined score thresholds in `scoring.py` to be wide enough to capture genuine gray areas rather than snapping everything into binary black-and-white.


---

## 3. 100% success rate logging valid `POST /appeal` requests to audit logs

<!-- Your criterion. -->
(Appeal Path Reliability)

**Why this target:**
False accusations are inevitable in automated detection. If a writer pushes back, the audit trail must reliably capture their defense without crashing or failing to write to the local `logs/audit.jsonl` file.


---

## 4. HTTP 400 response and zero perplexity calls for sub-3-word or empty input

<!-- Your criterion. -->
(Bad Input & Edge Cases Safety)

**Why this target:**
Feeding micro-lengths or empty strings into the GPT-2 tokenizer causes math errors or broken token shapes. Guarding the route prevents wasted compute cycles and prevents the log file from filling with junk data.


---

## 5. At least 0.40 mean score gap between default AI and human calibration inputs

<!-- Your criterion. -->
(Score Spread Separation)

**Why this target:**
If my `detector.py` perplexity score and `stylometry.py` features don't create a clean mathematical separation between human and machine patterns, the default threshold of 0.78 will constantly misclassify text, making the system unviable.

> **Revised criterion**: At least a 0.40 mean score gap between a benchmark set of 5 plain human writing samples and 5 default GPT-2 generated text prompts.
>
>**Why revised**: The original phrasing used undefined "calibration inputs," making it impossible for a reader to measure. Specifying countable sets of human and AI samples makes the score gap fully reproducible.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
---
## 6. In each of 3 trials, all 12 requests in `attack_set/attacks_malformed_requests.csv`, each sent as given in its `raw_body`, `send_as` and `content_type` columns, return their expected status: 200 for RQ02 and RQ06, and 400 for the other 10 rows, with requests sent at least 13 seconds apart so no 429 occurs.

(Extension: `/submit` input hardening)

**Why this target:**
Each row reaches a different branch of the checks in `app.py::submit`: a missing field, a wrong type, a body that isn't an object, unparseable JSON, an empty body, or the wrong content type. RQ02 and RQ06 check the other side, that an odd but usable request is still accepted and scored. Five of these 12 (RQ03, RQ04, RQ05, RQ07, RQ12) returned 500 before the fix, so this is the core job of the extension. I set 12 of 12 and not 11 because the 10 refused requests are turned away before the model runs, and the status for RQ02 and RQ06 comes from fixed checks too, so the same input gives the same status every time and nothing random can excuse a miss. A miss would be a kind of request the service still mishandles.

It fails if any row returns a different status than listed in any trial, including any 500 or 429.

---
## 7. In each of 3 trials, right after each of the 10 refused requests in `attack_set/attacks_malformed_requests.csv` (every row except RQ02 and RQ06), the newest line from `GET /log?limit=1` has the expected `reason` for 10 of 10: `missing_text` for RQ01, `invalid_text_type` for RQ03, RQ04, RQ05 and RQ12, and `invalid_json_body` for RQ07 to RQ11, with requests sent at least 13 seconds apart so no `rate_limited` entry appears.

(Extension: rejection audit trail)

**Why this target:**
Each refusal branch in `app.py::submit` writes its own reason, and the log is the only record that a request was refused at all. If a reason is wrong or missing, the audit trail misleads anyone trying to diagnose an attack. The `missing_text` branch has never appeared in `logs/audit.jsonl`, so RQ01 is the row most likely to fail. I set 10 of 10 because each reason comes from a fixed check in the code, so the same input always produces the same reason.

It fails if any of the 10 rows is followed by a log line with a different reason, no new line at all, or a `rate_limited` entry, in any trial.

---
## 8. In each of 3 trials, all 6 text inputs listed below return status 200 or 400 and never 500, when each is sent as the `text` field of a JSON body (`Content-Type: application/json`) to `POST /submit` at least 13 seconds apart.

| # | Category | Exact text |
|---|---|---|
| 1 | URLs only | `https://example.com https://example.org https://example.net` |
| 2 | URLs only | `http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log` |
| 3 | Numbers only | `3 14 159 265 358` |
| 4 | Numbers only | `1,000,000 2,500.75 -42 0.001` |
| 5 | No letters, 3+ words | `!!! ??? ...` |
| 6 | No letters, 3+ words | `*** @()! ^_^` |

(Extension: model and style steps don't crash)

**Why this target:**
All six inputs have at least 3 words, so they pass the length check in `app.py::submit` and reach the model and `style_signal`. Only the model call is wrapped in `try/except`, so `style_signal` is the step where an unexpected text could cause an unhandled crash and a 500. These are my own inputs, not from the attack set, so they test things I haven't tried. I accept either 200 or 400 because both are clean answers, and a 500 is the only outcome that means the service crashed. I set 6 of 6 because a crash on any one is a kind of text a real writer could paste, and the status code doesn't depend on the model's randomness, only the scores do.

It fails if any input returns anything other than 200 or 400 in any trial, including 500, 503 or 429.

---
## 9. In each of 3 trials, all 5 bad `POST /appeal` requests listed below, each sent with `Content-Type: application/json`, return the status shown for each row: 400 (bad request) for rows 1, 2 and 5, and 404 (not found) for rows 3 and 4, with no 500.

| # | Request body | Expected status |
|---|---|---|
| 1 | (empty body) | 400 |
| 2 | `{"reasoning": "I wrote this myself"}` (no `content_id`) | 400 |
| 3 | `{"content_id": "does-not-exist", "reasoning": "x"}` | 404 |
| 4 | `{"content_id": 12345, "reasoning": "x"}` | 404 |
| 5 | `["a"]` (a JSON array, not an object) | 400 |

(Bad input on `/appeal`)

**Why this target:**
`/appeal` is the only way a writer can challenge a decision, so if a malformed request crashes it, a wrongly accused writer has no recourse. I didn't harden this route when I hardened `/submit`, so it's the place I'd most expect to fail, and row 5 may return a 500 because the code calls `.get` on a list. This criterion differs from criterion 3, which checks that a valid appeal is logged. This one checks that bad appeals get a clean answer. I set 5 of 5 because each row is a different branch and the answers don't depend on the model. The route has no rate limit, so no spacing is needed.

It fails if any row returns a different status than the table in any trial, including a 500.

---
## 10. In each of 3 trials, after one normal warm-up request, a single `POST /submit` whose text is the word `word` repeated 20,000 times (separated by spaces) returns status 200 within 10 seconds, measured from sending the request to receiving the full response.

(Extension: huge input on `/submit`)

**Why this target:**
My detector truncates input to 400 tokens, so the model's cost shouldn't grow with input size, and a normal request takes about 2.6 seconds (from my README). 10 seconds is about four times that, which leaves room for tokenizing and style analysis of the whole text while staying well under the 30 to 60 second timeouts typical of web gateways. 20,000 words is about double the 11,330-word attack that already passed (MF08), so it tests beyond what I've tried. The service has no maximum length, so the text should simply be accepted and a 400 would be unexpected. A very large input is also where I'd expect a slowdown. The warm-up is there because the first request loads the model. It's one request per trial, so no spacing is needed. The 10 seconds comes from my laptop, so it's my baseline and not a universal number.

It fails if the response is anything other than 200, or takes longer than 10 seconds, in any trial.

---