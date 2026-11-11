# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 21:49
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `8db2dfd4-a4c7-47ac-936a-e7091bb04c81` | human | 0.000 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8852eda0-cf59-48a2-afc5-039e2f016fa5` | human | 0.000 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3c40d06b-9c10-4ac4-8cfa-864836693a87` | unsure | 0.000 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `70ee2d74-ec95-4a99-b65e-f50f46c82ad2` | unsure | 0.000 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `b4805cf5-377e-4241-aa9a-542991099550` | human | 0.000 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `7bfdf1fe-805d-499f-89f3-d45bbf8cf243` | human | 0.000 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `673e9b8e-c176-4577-af59-ba1573003f71` | unsure | 0.000 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `bf5f97a9-3953-4c37-9d0b-7dcb4a20611d` | human | 0.000 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1c94670c-9947-4b11-823e-8972b7050c06` | unsure | 0.000 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `594aac50-5267-4599-901f-133d35003b6e` | ai | 0.000 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b768607c-8eea-4641-94b1-35efb397ae63` | unsure | 0.000 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9a9afac4-7c93-4164-b778-af2e54a3af3d` | unsure | 0.000 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `eeed52c6-0428-44dc-9e79-e17e27da1f75` | unsure | 0.000 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `37350eb8-3bd2-443a-9a68-5cefe40a41ee` | unsure | 0.000 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `894f08d9-d5cb-495e-84df-4b2251a0b456` | ai | 0.000 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `26698f24-6dda-4d31-ab13-ea329a05d3f9` | unsure | 0.000 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `83b5a9eb-d4cf-4bf2-b457-3a8220d14b80` | unsure | 0.000 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `338278b1-c112-41a3-9644-6982da13da5e` | human | 0.000 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ab51f2af-36da-4b26-8537-c0020c0761b9` | unsure | 0.000 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ce9cead6-892f-49ed-b8f7-cc18c3773696` | human | 0.000 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `14e7898b-03ec-4e69-845d-8e2452ebd55a` | unsure | 0.000 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `9fa4ff2c-88cb-4e0e-a91b-80f4ac9b970e` | unsure | 0.000 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `74001629-5de3-42e4-a393-b7f903497dc2` | human | 0.000 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `53b907f2-a7ee-4aba-b403-2fc9b515a73c` | unsure | 0.000 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `11c52ff6-2290-41c6-a841-0884e46f8f92` | human | 0.000 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `016ff898-2768-46e1-898e-98fa55ecf939` | human | 0.000 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `12117576-0ccc-4368-bd47-db55aa88b96f` | unsure | 0.000 | HELD |
| MF06 | malformed | text is emoji only | 200 | `563dcc47-2bca-489f-af8f-8d0ea4468298` | ai | 0.000 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `0671a570-5df1-4746-bf71-497f7bf96df2` | ai | 0.000 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `531c6cce-b9a6-42f2-9d64-1a6760a1f431` | ai | 0.000 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `46da5bd4-b25a-4c2a-a1f5-00de0935f2cd` | human | 0.000 | HELD |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `b5f8f595-5af7-4439-b92b-09b71a935de3` | human | 0.000 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f746db0d-8c5b-449c-a869-48f4db0dae5f` | human | 0.000 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6c17f572-3aa6-4397-b848-ecb9f2343e55` | human | 0.000 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `01afffe9-8689-4a4c-a182-9ac3d6fb7ae4` | human | 0.000 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `03d202d2-48cd-4a6d-a5b8-877483c3c2b2` | human | 0.000 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b191efda-ae59-4d4e-93f4-811499b94c19` | human | 0.000 | HELD |
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
  "content_id": "8db2dfd4-a4c7-47ac-936a-e7091bb04c81",
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
  "content_id": "8852eda0-cf59-48a2-afc5-039e2f016fa5",
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
  "content_id": "3c40d06b-9c10-4ac4-8cfa-864836693a87",
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
  "content_id": "70ee2d74-ec95-4a99-b65e-f50f46c82ad2",
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
  "content_id": "b4805cf5-377e-4241-aa9a-542991099550",
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
  "content_id": "7bfdf1fe-805d-499f-89f3-d45bbf8cf243",
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
  "content_id": "673e9b8e-c176-4577-af59-ba1573003f71",
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
  "content_id": "bf5f97a9-3953-4c37-9d0b-7dcb4a20611d",
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
  "content_id": "1c94670c-9947-4b11-823e-8972b7050c06",
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
  "content_id": "594aac50-5267-4599-901f-133d35003b6e",
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
  "content_id": "b768607c-8eea-4641-94b1-35efb397ae63",
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
  "content_id": "9a9afac4-7c93-4164-b778-af2e54a3af3d",
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
  "content_id": "eeed52c6-0428-44dc-9e79-e17e27da1f75",
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
  "content_id": "37350eb8-3bd2-443a-9a68-5cefe40a41ee",
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
  "content_id": "894f08d9-d5cb-495e-84df-4b2251a0b456",
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
  "content_id": "26698f24-6dda-4d31-ab13-ea329a05d3f9",
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
  "content_id": "83b5a9eb-d4cf-4bf2-b457-3a8220d14b80",
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
  "content_id": "338278b1-c112-41a3-9644-6982da13da5e",
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
  "content_id": "ab51f2af-36da-4b26-8537-c0020c0761b9",
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
  "content_id": "ce9cead6-892f-49ed-b8f7-cc18c3773696",
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
  "content_id": "14e7898b-03ec-4e69-845d-8e2452ebd55a",
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
  "content_id": "9fa4ff2c-88cb-4e0e-a91b-80f4ac9b970e",
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
  "content_id": "74001629-5de3-42e4-a393-b7f903497dc2",
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
  "content_id": "53b907f2-a7ee-4aba-b403-2fc9b515a73c",
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
  "content_id": "11c52ff6-2290-41c6-a841-0884e46f8f92",
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
  "content_id": "016ff898-2768-46e1-898e-98fa55ecf939",
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
  "content_id": "12117576-0ccc-4368-bd47-db55aa88b96f",
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
  "content_id": "563dcc47-2bca-489f-af8f-8d0ea4468298",
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
  "content_id": "0671a570-5df1-4746-bf71-497f7bf96df2",
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
  "content_id": "531c6cce-b9a6-42f2-9d64-1a6760a1f431",
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
  "content_id": "46da5bd4-b25a-4c2a-a1f5-00de0935f2cd",
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
  "content_id": "b5f8f595-5af7-4439-b92b-09b71a935de3",
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
  "content_id": "f746db0d-8c5b-449c-a869-48f4db0dae5f",
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
  "content_id": "6c17f572-3aa6-4397-b848-ecb9f2343e55",
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
  "content_id": "01afffe9-8689-4a4c-a182-9ac3d6fb7ae4",
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
  "content_id": "03d202d2-48cd-4a6d-a5b8-877483c3c2b2",
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
  "content_id": "b191efda-ae59-4d4e-93f4-811499b94c19",
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
