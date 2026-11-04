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
