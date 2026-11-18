# Capstone run log - capstone

- Produced by: `run_capstone_eval.py::main`
- 6 and 7: `criteria_6_and_7` · 8: `criterion_8` · 9: `criterion_9` · 10: `criterion_10`
- Service: `app.py::submit`, `app.py::appeal`
- 3 trials per criterion · 2026-11-17 21:29

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 6. malformed requests: right status | 12 of 12 requests return their expected status | 12/12 | 12/12 | 12/12 | MET |
| 7. refusals: right log reason | 10 of 10 refused requests log the expected reason | 10/10 | 10/10 | 10/10 | MET |
| 8. odd text never crashes | 6 of 6 texts return 200 or 400 (never 500) | 6/6 | 6/6 | 6/6 | MET |
| 9. bad /appeal gets a clean answer | 5 of 5 bad appeals return their expected status | 4/5 | 4/5 | 4/5 | MISSED |
| 10. 20,000-word text: 200 within 10 s | 200 within 10 seconds | PASS (200, 1.571s) | PASS (200, 1.498s) | PASS (200, 0.638s) | MET |

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
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"2f3daa69-e40b-4003-8019-e2bffee1e97e\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
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
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"a577fc47-d725-4de4-a8bf-c8da9a16751e\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
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
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"e6631106-8260-4b71-94ca-46ba045e3098\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
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
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"33d51efb-e6b7-4e40-8c66-c486bf1a3cb9\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
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
    "response": "{\n  \"combined_score\": 0.2395,\n  \"confidence\": 0.0,\n  \"content_id\": \"4dc34387-d524-47db-86f8-91952b8cd4a4\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.2395,\n  \"style_score\": 0.5758\n}\n"
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
    "response": "{\n  \"combined_score\": 0.0492,\n  \"confidence\": 0.0,\n  \"content_id\": \"e00298a6-4f41-49aa-915a-e9bff4253764\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0492,\n  \"style_score\": 0.5259\n}\n"
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
      "timestamp": "2026-11-18T03:16:43+00:00"
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
      "timestamp": "2026-11-18T03:17:19+00:00"
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
      "timestamp": "2026-11-18T03:17:32+00:00"
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
      "timestamp": "2026-11-18T03:17:45+00:00"
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
      "timestamp": "2026-11-18T03:18:11+00:00"
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
      "timestamp": "2026-11-18T03:18:24+00:00"
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
      "timestamp": "2026-11-18T03:18:37+00:00"
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
      "timestamp": "2026-11-18T03:18:50+00:00"
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
      "timestamp": "2026-11-18T03:19:03+00:00"
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
      "timestamp": "2026-11-18T03:19:16+00:00"
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
      "timestamp": "2026-11-18T03:21:13+00:00"
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
      "timestamp": "2026-11-18T03:21:39+00:00"
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
      "timestamp": "2026-11-18T03:21:52+00:00"
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
      "timestamp": "2026-11-18T03:22:05+00:00"
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
      "timestamp": "2026-11-18T03:22:31+00:00"
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
      "timestamp": "2026-11-18T03:22:44+00:00"
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
      "timestamp": "2026-11-18T03:22:57+00:00"
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
      "timestamp": "2026-11-18T03:23:10+00:00"
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
      "timestamp": "2026-11-18T03:23:23+00:00"
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
      "timestamp": "2026-11-18T03:23:36+00:00"
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
      "timestamp": "2026-11-18T03:25:33+00:00"
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
      "timestamp": "2026-11-18T03:25:59+00:00"
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
      "timestamp": "2026-11-18T03:26:12+00:00"
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
      "timestamp": "2026-11-18T03:26:25+00:00"
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
      "timestamp": "2026-11-18T03:26:51+00:00"
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
      "timestamp": "2026-11-18T03:27:04+00:00"
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
      "timestamp": "2026-11-18T03:27:17+00:00"
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
      "timestamp": "2026-11-18T03:27:30+00:00"
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
      "timestamp": "2026-11-18T03:27:43+00:00"
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
      "timestamp": "2026-11-18T03:27:56+00:00"
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
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"628db959-53a1-450b-abe7-b29ad009f9a2\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"da5ade88-20a3-4004-be96-a0e738f3dac2\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"49cf56e0-f281-4e9a-bb69-84b6e8bea62e\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"395ab0e4-2213-449b-9900-c14fc1b23fa9\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"794e17a1-15b7-42aa-a72f-d1cba9810b66\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"a4b7b12e-199c-4703-873d-bcefc20dc6ec\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
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
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"30478d6d-176e-40fe-9716-125af982c851\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"4d7d56e3-2467-49f0-9f99-64fc7f738129\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"4817f63c-3555-4f08-b456-265150873ad4\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"2c998327-9f61-4ce5-889b-fd54cd344df6\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"841c17a8-c655-4757-bbb7-27c4693dc9a5\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"f8e2604d-0fbf-4795-94f6-9567681053a1\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
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
    "response": "{\n  \"combined_score\": 0.5333,\n  \"confidence\": 0.0,\n  \"content_id\": \"b4c86405-b510-4d33-9f5d-7809d753901d\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 2,
    "text": "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4017,\n  \"confidence\": 0.0,\n  \"content_id\": \"75f60d92-c712-4e5f-9d3d-b7917489db25\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_scor"
  },
  {
    "n": 3,
    "text": "3 14 159 265 358",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0005,\n  \"confidence\": 0.0,\n  \"content_id\": \"f1c64a82-f9c6-4282-b801-34b92c6022cb\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0005,\n  \"style_score\": 0.6\n}\n"
  },
  {
    "n": 4,
    "text": "1,000,000 2,500.75 -42 0.001",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.4,\n  \"confidence\": 0.0,\n  \"content_id\": \"ddda66a9-eb88-4075-948b-da3899d19a71\",\n  \"guess\": \"unsure\",\n  \"label\": \"We found mixed signals in this text, and we're not sure who wrote it. If this was flagged by mistake, you can submit an appeal for human review.\",\n  \"model_score\":"
  },
  {
    "n": 5,
    "text": "!!! ??? ...",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0009,\n  \"confidence\": 0.0,\n  \"content_id\": \"27bda28d-9b17-49b0-9671-fa2a11c4957f\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0009,\n  \"style_score\": 0.8\n}\n"
  },
  {
    "n": 6,
    "text": "*** @()! ^_^",
    "status": 200,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.0321,\n  \"confidence\": 0.0,\n  \"content_id\": \"ec8a3ea3-e30a-43ce-91a1-7c1c115979cf\",\n  \"guess\": \"human\",\n  \"label\": \"We think this was probably written by a person.\",\n  \"model_score\": 0.0321,\n  \"style_score\": 0.8\n}\n"
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
    "status": 500,
    "ok": false,
    "response": "<!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resource&amp;f=style.css\">\n    <link rel=\"shortcut icon\"\n        href=\"?__debugger__=yes&am"
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
    "status": 500,
    "ok": false,
    "response": "<!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resource&amp;f=style.css\">\n    <link rel=\"shortcut icon\"\n        href=\"?__debugger__=yes&am"
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
    "status": 500,
    "ok": false,
    "response": "<!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;cmd=resource&amp;f=style.css\">\n    <link rel=\"shortcut icon\"\n        href=\"?__debugger__=yes&am"
  }
]
```

### Criterion 10: 20,000-word text: 200 within 10 s

**Trial 1**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.161,
    "status": 200,
    "seconds": 1.571,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"e03d12a9-16be-4e30-a75a-79cb05c2975f\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```

**Trial 2**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.151,
    "status": 200,
    "seconds": 1.498,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"035059de-e238-40da-b27e-282462458011\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```

**Trial 3**

```json
[
  {
    "warmup_status": 200,
    "warmup_seconds": 0.109,
    "status": 200,
    "seconds": 0.638,
    "limit_seconds": 10.0,
    "ok": true,
    "response": "{\n  \"combined_score\": 0.9988,\n  \"confidence\": 0.0,\n  \"content_id\": \"ead0ec95-b3b6-4fc9-884f-a3a21d0cbebd\",\n  \"guess\": \"ai\",\n  \"label\": \"We think this was probably generated by an AI model. If this is an error, please file an appeal.\",\n  \"model_score\": 0.9975,\n  \"style_score\": 1.0\n}\n"
  }
]
```
