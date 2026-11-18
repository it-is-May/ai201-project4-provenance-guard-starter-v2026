# Capstone run log - after

- Produced by: `run_capstone_eval.py::main`
- 6 and 7: `criteria_6_and_7` · 8: `criterion_8` · 9: `criterion_9` · 10: `criterion_10`
- Service: `app.py::submit`, `app.py::appeal`
- 3 trials per criterion · 2026-11-17 23:00

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 6. malformed requests: right status | 12 of 12 requests return their expected status | 12/12 | 12/12 | 12/12 | MET |
| 7. refusals: right log reason | 10 of 10 refused requests log the expected reason | 10/10 | 10/10 | 10/10 | MET |
| 8. odd text never crashes | 6 of 6 texts return 200 or 400 (never 500) | 6/6 | 6/6 | 6/6 | MET |
| 9. bad /appeal gets a clean answer | 5 of 5 bad appeals return their expected status | 5/5 | 5/5 | 5/5 | MET |
| 10. 20,000-word text: 200 within 10 s | 200 within 10 seconds | PASS (200, 3.015s) | PASS (200, 0.751s) | PASS (200, 1.294s) | MET |

---

## What actually came back

Real output from every trial. Paste the relevant parts into the README.

### Criterion 6: malformed requests: right status

**Trial 1**

```json
[
  {
    "id": "RQ01",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing required 'text' field.\"\n}\n"
  },
  {
    "id": "RQ02",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"f8e59e6c-e5b2-4b39-bee8-8de96b3d0074\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
  },
  {
    "id": "RQ03",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ04",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ05",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ06",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"8367de07-c0cf-4baa-a315-bfa90ca0464c\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
  },
  {
    "id": "RQ07",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ08",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ09",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ10",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ11",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ12",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  }
]
```

**Trial 2**

```json
[
  {
    "id": "RQ01",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing required 'text' field.\"\n}\n"
  },
  {
    "id": "RQ02",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"e6cb3d50-2ca9-4d25-96c9-5f26929e1482\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
  },
  {
    "id": "RQ03",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ04",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ05",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ06",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"b486eda6-60db-49f6-89ad-ced59250840a\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
  },
  {
    "id": "RQ07",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ08",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ09",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ10",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ11",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ12",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  }
]
```

**Trial 3**

```json
[
  {
    "id": "RQ01",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing required 'text' field.\"\n}\n"
  },
  {
    "id": "RQ02",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"36e36122-68b4-4ad1-849a-75524e04aeb9\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
  },
  {
    "id": "RQ03",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ04",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ05",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  },
  {
    "id": "RQ06",
    "expected_status": 200,
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"30b8075b-f0c6-432b-970c-60327b3817d3\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
  },
  {
    "id": "RQ07",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ08",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ09",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ10",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ11",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  },
  {
    "id": "RQ12",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"'text' must be a string.\"\n}\n"
  }
]
```

### Criterion 7: refusals: right log reason

**Trial 1**

```json
[
  {
    "id": "RQ01",
    "expected_reason": "missing_text",
    "reason": "missing_text",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ01",
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "timestamp": "2026-11-18T04:47:35+00:00"
    }
  },
  {
    "id": "RQ03",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ03",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:48:04+00:00"
    }
  },
  {
    "id": "RQ04",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ04",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:48:17+00:00"
    }
  },
  {
    "id": "RQ05",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ05",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:48:30+00:00"
    }
  },
  {
    "id": "RQ07",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:48:56+00:00"
    }
  },
  {
    "id": "RQ08",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:49:09+00:00"
    }
  },
  {
    "id": "RQ09",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:49:22+00:00"
    }
  },
  {
    "id": "RQ10",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:49:35+00:00"
    }
  },
  {
    "id": "RQ11",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:49:48+00:00"
    }
  },
  {
    "id": "RQ12",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ12",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:50:01+00:00"
    }
  }
]
```

**Trial 2**

```json
[
  {
    "id": "RQ01",
    "expected_reason": "missing_text",
    "reason": "missing_text",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ01",
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "timestamp": "2026-11-18T04:51:58+00:00"
    }
  },
  {
    "id": "RQ03",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ03",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:52:24+00:00"
    }
  },
  {
    "id": "RQ04",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ04",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:52:37+00:00"
    }
  },
  {
    "id": "RQ05",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ05",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:52:50+00:00"
    }
  },
  {
    "id": "RQ07",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:53:16+00:00"
    }
  },
  {
    "id": "RQ08",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:53:29+00:00"
    }
  },
  {
    "id": "RQ09",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:53:42+00:00"
    }
  },
  {
    "id": "RQ10",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:53:55+00:00"
    }
  },
  {
    "id": "RQ11",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:54:08+00:00"
    }
  },
  {
    "id": "RQ12",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ12",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:54:21+00:00"
    }
  }
]
```

**Trial 3**

```json
[
  {
    "id": "RQ01",
    "expected_reason": "missing_text",
    "reason": "missing_text",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ01",
      "event": "rejected",
      "reason": "missing_text",
      "status": "rejected",
      "timestamp": "2026-11-18T04:56:18+00:00"
    }
  },
  {
    "id": "RQ03",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ03",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:56:44+00:00"
    }
  },
  {
    "id": "RQ04",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ04",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:56:57+00:00"
    }
  },
  {
    "id": "RQ05",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ05",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:57:10+00:00"
    }
  },
  {
    "id": "RQ07",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:57:36+00:00"
    }
  },
  {
    "id": "RQ08",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:57:49+00:00"
    }
  },
  {
    "id": "RQ09",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:58:02+00:00"
    }
  },
  {
    "id": "RQ10",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:58:15+00:00"
    }
  },
  {
    "id": "RQ11",
    "expected_reason": "invalid_json_body",
    "reason": "invalid_json_body",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json_body",
      "status": "rejected",
      "timestamp": "2026-11-18T04:58:28+00:00"
    }
  },
  {
    "id": "RQ12",
    "expected_reason": "invalid_text_type",
    "reason": "invalid_text_type",
    "new_line": true,
    "ok": true,
    "newest_log_line": {
      "creator_id": "attacker_RQ12",
      "event": "rejected",
      "reason": "invalid_text_type",
      "status": "rejected",
      "timestamp": "2026-11-18T04:58:41+00:00"
    }
  }
]
```

### Criterion 8: odd text never crashes

**Trial 1**

```json
[
  {
    "n": 1,
    "text": "https://example.com https://example.org https://example.net",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"84fa855e-a91a-4bf6-bec3-659282419c09\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"e8d78602-f28f-4ecc-8252-c3993d6b55c3\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"9b0ba68b-a067-487a-bb0e-84f5860cde34\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"297d909d-8767-4c05-9946-534d177d9e66\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"fadd9bb9-a461-472e-94d9-dd0fbb2fdb83\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"cfa6f6ff-f359-4e16-a544-072579bdbe1d\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
  }
]
```

**Trial 2**

```json
[
  {
    "n": 1,
    "text": "https://example.com https://example.org https://example.net",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"4ad91ad0-b87b-4f35-9e6e-251c18380c65\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"743bcdfa-f26c-4880-903e-fcc74eb80609\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"11f1b2ce-edcf-454f-a309-4f3e0d88c466\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"8e98d6f8-8a9c-4c64-bff5-4a12cc816cd5\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"66abcaac-f1f6-456c-880b-eb424ec79b7b\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"2c27a5cb-1c06-4df2-a7a2-e8214a78f0dc\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
  }
]
```

**Trial 3**

```json
[
  {
    "n": 1,
    "text": "https://example.com https://example.org https://example.net",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"8b0f6d2a-8c1a-4015-a15d-7c731f438796\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"f94742fa-683e-4afd-aefc-90062d8b0ea4\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"d84598c6-132d-4f08-b07b-1097cecbd7f9\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"95b1fbba-8b1b-4976-a46c-692e82838470\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"0b04fba3-b506-45f4-980c-a50152c82a1c\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"4b27a6ea-85bd-4a5f-982b-01aca173eb59\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
  }
]
```

### Criterion 9: bad /appeal gets a clean answer

**Trial 1**

```json
[
  {
    "n": 1,
    "sent": "(empty body)",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 2,
    "sent": "{\"reasoning\": \"I wrote this myself\"}",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 3,
    "sent": "{\"content_id\": \"does-not-exist\", \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 4,
    "sent": "{\"content_id\": 12345, \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 5,
    "sent": "[\"a\"]",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  }
]
```

**Trial 2**

```json
[
  {
    "n": 1,
    "sent": "(empty body)",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 2,
    "sent": "{\"reasoning\": \"I wrote this myself\"}",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 3,
    "sent": "{\"content_id\": \"does-not-exist\", \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 4,
    "sent": "{\"content_id\": 12345, \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 5,
    "sent": "[\"a\"]",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  }
]
```

**Trial 3**

```json
[
  {
    "n": 1,
    "sent": "(empty body)",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 2,
    "sent": "{\"reasoning\": \"I wrote this myself\"}",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Missing content_id.\"\n}\n"
  },
  {
    "n": 3,
    "sent": "{\"content_id\": \"does-not-exist\", \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 4,
    "sent": "{\"content_id\": 12345, \"reasoning\": \"x\"}",
    "expected_status": 404,
    "status": 404,
    "ok": true,
    "response": "{\n  \"error\": \"not_found\",\n  \"message\": \"No decision found for that content_id.\"\n}\n"
  },
  {
    "n": 5,
    "sent": "[\"a\"]",
    "expected_status": 400,
    "status": 400,
    "ok": true,
    "response": "{\n  \"error\": \"bad_request\",\n  \"message\": \"Request body must be a JSON object.\"\n}\n"
  }
]
```

### Criterion 10: 20,000-word text: 200 within 10 s

**Trial 1**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.131,
    "status": 200,
    "seconds": 3.015,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"b3cb91a5-098c-441f-bb9a-aa72befcc823\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```

**Trial 2**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.104,
    "status": 200,
    "seconds": 0.751,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"bb71ea72-d606-4d7b-8fd6-97362ea8b8de\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```

**Trial 3**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.185,
    "status": 200,
    "seconds": 1.294,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"ebff8a4e-00f2-4d30-8945-5c448af06443\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```
