# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 22:06
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `81a78d7e-f1c2-4c8a-ad1a-da2585c15838` | human | 0.000 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ad3c4bc3-4d97-4662-997e-17e1a7be734d` | human | 0.000 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c9cb61d7-8172-4056-b5f6-212fd7ce6054` | unsure | 0.000 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `173be714-4d4d-49d5-99bc-8a7fd1db56be` | unsure | 0.000 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `90bb47d4-696f-4624-a8d9-22a64f36c645` | human | 0.000 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ee09c97a-7359-40d4-b8b4-9089b1530c7d` | human | 0.000 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `9a4a17af-6abf-4bf0-bb69-16c2e809afc2` | unsure | 0.000 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `7d4d9105-06a8-47e3-851f-3d2bd4afd89f` | human | 0.000 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1eb369dd-ea20-4ed0-ae54-7e3726a00adc` | unsure | 0.000 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `27209cdb-64b9-4b5d-95f3-7c31d9e1c854` | ai | 0.000 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `930075c1-b01e-432f-be6c-a43c792ce298` | unsure | 0.000 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `23b7273e-4db9-43de-a4e2-c207248ae69c` | unsure | 0.000 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `5d19763b-faba-43e0-a9d7-70b654aa832e` | unsure | 0.000 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `340a802c-a2a1-4a08-bf5f-bc6b7e409e33` | unsure | 0.000 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `76854ba0-8cf4-477d-83db-4b93c51b3621` | ai | 0.000 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `a8f8fc69-2c99-46f7-be06-4f0f9b9fedab` | unsure | 0.000 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `2cd786ed-bb9d-4e97-9062-977442a7643d` | unsure | 0.000 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `71b67403-1bcd-4e49-b0af-fbe324e150b8` | human | 0.000 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c7ace2aa-6d2e-4e58-9f60-75d60a126ae1` | unsure | 0.000 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d49c5675-9171-47e6-b93b-fad551f96455` | human | 0.000 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `590e0847-4695-4f30-a129-50f49fc10c30` | unsure | 0.000 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `dbd1b993-8890-42db-bcd2-ca2451dca4d7` | unsure | 0.000 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `fa27b630-a8e1-4da3-8a71-b899f6e592f1` | human | 0.000 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b7989b32-20ba-4a3f-bf71-3eb844202a2e` | unsure | 0.000 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `61269c9f-e511-446d-83b2-81c61ba40978` | human | 0.000 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `87a54162-c981-4816-b013-2de13fe1c0ab` | human | 0.000 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `d485636c-4e30-4c28-8d41-fa6fc448fee8` | unsure | 0.000 | HELD |
| MF06 | malformed | text is emoji only | 200 | `24cc8a5f-0700-4b35-b219-64348a8e9672` | ai | 0.000 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `f9f6b6ae-46e4-42a3-99f5-66f345892f79` | ai | 0.000 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `ed4ebd8d-c596-4e8f-bc32-ad2524198426` | ai | 0.000 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `80d14c82-73bb-4394-89ec-aaab4ec3a9cb` | human | 0.000 | HELD |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `10a49a0d-4473-4309-ac1e-b15aacb8a454` | human | 0.000 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c43b3d7f-e84a-41aa-83f9-df790a33cc0a` | human | 0.000 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f9f520c3-d43c-4930-9017-44abbb40453d` | human | 0.000 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `475ab4b1-703d-4d2a-9fbb-12141c6130b6` | human | 0.000 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a10e2d29-05a6-4c3f-a772-f4e1e9c035b5` | human | 0.000 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3aa294a1-b78b-4e45-9da0-33ef6fbefbc5` | human | 0.000 | HELD |
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
  "content_id": "81a78d7e-f1c2-4c8a-ad1a-da2585c15838",
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
  "content_id": "ad3c4bc3-4d97-4662-997e-17e1a7be734d",
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
  "content_id": "c9cb61d7-8172-4056-b5f6-212fd7ce6054",
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
  "content_id": "173be714-4d4d-49d5-99bc-8a7fd1db56be",
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
  "content_id": "90bb47d4-696f-4624-a8d9-22a64f36c645",
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
  "content_id": "ee09c97a-7359-40d4-b8b4-9089b1530c7d",
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
  "content_id": "9a4a17af-6abf-4bf0-bb69-16c2e809afc2",
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
  "content_id": "7d4d9105-06a8-47e3-851f-3d2bd4afd89f",
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
  "content_id": "1eb369dd-ea20-4ed0-ae54-7e3726a00adc",
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
  "content_id": "27209cdb-64b9-4b5d-95f3-7c31d9e1c854",
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
  "content_id": "930075c1-b01e-432f-be6c-a43c792ce298",
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
  "content_id": "23b7273e-4db9-43de-a4e2-c207248ae69c",
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
  "content_id": "5d19763b-faba-43e0-a9d7-70b654aa832e",
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
  "content_id": "340a802c-a2a1-4a08-bf5f-bc6b7e409e33",
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
  "content_id": "76854ba0-8cf4-477d-83db-4b93c51b3621",
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
  "content_id": "a8f8fc69-2c99-46f7-be06-4f0f9b9fedab",
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
  "content_id": "2cd786ed-bb9d-4e97-9062-977442a7643d",
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
  "content_id": "71b67403-1bcd-4e49-b0af-fbe324e150b8",
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
  "content_id": "c7ace2aa-6d2e-4e58-9f60-75d60a126ae1",
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
  "content_id": "d49c5675-9171-47e6-b93b-fad551f96455",
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
  "content_id": "590e0847-4695-4f30-a129-50f49fc10c30",
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
  "content_id": "dbd1b993-8890-42db-bcd2-ca2451dca4d7",
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
  "content_id": "fa27b630-a8e1-4da3-8a71-b899f6e592f1",
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
  "content_id": "b7989b32-20ba-4a3f-bf71-3eb844202a2e",
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
  "content_id": "61269c9f-e511-446d-83b2-81c61ba40978",
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
  "content_id": "87a54162-c981-4816-b013-2de13fe1c0ab",
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
  "content_id": "d485636c-4e30-4c28-8d41-fa6fc448fee8",
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
  "content_id": "24cc8a5f-0700-4b35-b219-64348a8e9672",
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
  "content_id": "f9f6b6ae-46e4-42a3-99f5-66f345892f79",
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
  "content_id": "ed4ebd8d-c596-4e8f-bc32-ad2524198426",
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
  "content_id": "80d14c82-73bb-4394-89ec-aaab4ec3a9cb",
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
  "content_id": "10a49a0d-4473-4309-ac1e-b15aacb8a454",
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
  "content_id": "c43b3d7f-e84a-41aa-83f9-df790a33cc0a",
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
  "content_id": "f9f520c3-d43c-4930-9017-44abbb40453d",
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
  "content_id": "475ab4b1-703d-4d2a-9fbb-12141c6130b6",
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
  "content_id": "a10e2d29-05a6-4c3f-a772-f4e1e9c035b5",
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
  "content_id": "3aa294a1-b78b-4e45-9da0-33ef6fbefbc5",
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
