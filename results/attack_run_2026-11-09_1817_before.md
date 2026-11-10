# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 18:17
- Auto-marked BROKE (5xx, crash, no response): **6**
- Left for you to judge: **50**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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
---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 6 | 14 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "06137279-1d5b-4bc7-8f87-9c3a864bd50e",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.1635,
  "style_score": 0.5348,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "80ac57f4-15e3-404b-9bf4-657323e162cc",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.3459,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c5638702-ea2e-4b15-8c60-824fe761432c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6662,
  "style_score": 0.4474,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "2cc9b9c7-5896-490c-83c3-7d01a9e4d6b0",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6114,
  "style_score": 0.5293,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "47c1c8b2-6652-4b67-b4f4-00c30d23513d",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.3212,
  "style_score": 0.4106,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "52281a18-bcd5-4b48-90ce-4267f1ed8a87",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.5727,
  "style_score": 0.3071,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c373bbb1-307a-438f-ad55-d1d0dad4c506",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5862,
  "style_score": 0.5879,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "31053b5e-8be0-45c3-bb9a-b1c865357e9e",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.2452,
  "style_score": 0.4835,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "7229aa40-227d-4986-9bfd-17fc7aa5819f",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7042,
  "style_score": 0.4439,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "bea700df-ef28-4b6f-8fea-0e558e6ca85f",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.0,
  "model_score": 0.9792,
  "style_score": 0.7338,
  "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3699ea08-6d35-4048-a76e-5be71aa6316f",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6175,
  "style_score": 0.5123,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a737bcd3-9371-479b-b232-8fba659446fd",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7387,
  "style_score": 0.5725,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "67564e6c-7265-4658-ad26-140348a51d07",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8051,
  "style_score": 0.5432,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5e335c9a-5caf-473c-a66f-ad330ed4dc7d",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8329,
  "style_score": 0.4869,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "0e087194-15af-46c1-941a-9e3cab770878",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.0,
  "model_score": 0.8005,
  "style_score": 0.6145,
  "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "8f1640ad-153f-424c-b9c6-a0a61cb0843c",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8814,
  "style_score": 0.4826,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "2c84b9dc-d7d6-4b35-af33-f7413923d9c9",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8816,
  "style_score": 0.5496,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0df4337a-b9d0-475a-b7d8-a8103ee7ba09",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.3223,
  "style_score": 0.3734,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ec2d0854-f57d-4824-8ad4-ed9d1d2b5051",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.4625,
  "style_score": 0.4025,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "e55b89f6-a304-403f-bd3d-7eab457c88f3",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.2044,
  "style_score": 0.3848,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "80f99747-51fc-4eed-bdc2-f4da522d078a",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.4838,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4e02d62f-7b31-44bd-9191-efce62bcf539",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.4998,
  "style_score": 0.4118,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "ab9f34fd-13f9-4236-8b54-8fde61be5db9",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.6401,
  "style_score": 0.3554,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "7cfb13ef-53be-4154-8611-afc23a57bcc3",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5583,
  "style_score": 0.5167,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "9fb9a6a4-7735-44fd-8188-dfaa2672f218",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "384bd8d7-5d9a-4467-8659-3faeb51f9b38",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "034dc305-f497-44ca-8530-1f9834f0d704",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "a2591cf4-5b18-4528-b054-a11ab3ad95c5",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.0,
  "model_score": 0.9969,
  "style_score": 0.8,
  "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "d5a50863-21d4-4f44-b988-de8b54c4627c",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.0,
  "model_score": 0.9064,
  "style_score": 0.9873,
  "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "14bfb005-4a7e-4360-8a68-e388e61bc766",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.0,
  "model_score": 0.9876,
  "style_score": 0.8573,
  "label": "We think this was probably generated by an AI model. If this is an error, please file an appeal.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "e704b529-411a-4a4c-aaac-a013925f1b84",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.2395,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;int&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=ye",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;NoneType&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger",
  "verdict": "BROKE"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "5bbea56c-3504-4a90-8e31-94c7c21d777c",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0492,
  "style_score": 0.5259,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;dict&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4ac4a3c6-7772-4717-acd6-f11cfd7751a0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c21b9f21-3a83-4db0-a5be-75742447825a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "074d9cb3-191f-43cd-995c-f3c3464dada4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "f86c3153-5748-4a34-a9e2-e195e0f4ac9f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "b4f3842e-fd43-4218-8889-24d521beeeff",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.5758,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
