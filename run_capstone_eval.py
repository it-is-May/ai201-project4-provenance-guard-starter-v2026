#!/usr/bin/env python3
"""
Run capstone criteria 6-10 three times each.  <- CAPSTONE, MILESTONE 5

    python app.py                                   # in one terminal
    python run_capstone_eval.py --label capstone    # in another

What it does, per trial (nothing is changed between trials):

    criteria_6_and_7   the 12 requests in attack_set/attacks_malformed_requests.csv,
                       each sent as written. Criterion 6 checks the status code.
                       Criterion 7 checks the audit log after each refused request.
    criterion_8        six odd texts sent to /submit as JSON (200 or 400, never 500)
    criterion_9        five bad bodies sent to /appeal (exact status per row)
    criterion_10       one warm-up request, then one 20,000-word request, timed

Every /submit request is sent at least PACE_SECONDS after the previous one, so
the rate limiter (5 per minute) never returns a 429 that isn't the thing being
tested. /appeal is not rate limited, so it is not paced.

This script only sends requests and reads the answers. It never edits the
service, the log, or the attack set. Running it does ADD lines to the real
logs/audit.jsonl, because the service logs every request it handles.
"""

import argparse
import csv
import datetime as dt
import json
import sys
import time

import config

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

# Criteria 6, 7, 8 say "at least 13 seconds apart". 5 per minute is one every 12.
PACE_SECONDS = 13.0

MALFORMED_CSV = config.ROOT / "attack_set" / "attacks_malformed_requests.csv"

# Criterion 6: these two rows should be accepted (200). The other ten, refused (400).
ACCEPTED_ROWS = {"RQ02", "RQ06"}

# Criterion 7: the reason each refused row should leave in the log.
EXPECTED_REASON = {
    "RQ01": "missing_text",
    "RQ03": "invalid_text_type",
    "RQ04": "invalid_text_type",
    "RQ05": "invalid_text_type",
    "RQ07": "invalid_json_body",
    "RQ08": "invalid_json_body",
    "RQ09": "invalid_json_body",
    "RQ10": "invalid_json_body",
    "RQ11": "invalid_json_body",
    "RQ12": "invalid_text_type",
}

# Criterion 8: the six texts, exactly as listed in criteria.md.
C8_TEXTS = [
    "https://example.com https://example.org https://example.net",
    "http://a.b/c?d=1 https://x.y/z#w http://localhost:5000/log",
    "3 14 159 265 358",
    "1,000,000 2,500.75 -42 0.001",
    "!!! ??? ...",
    "*** @()! ^_^",
]

# Criterion 9: (request body exactly as sent, expected status), as in criteria.md.
C9_ROWS = [
    ("", 400),                                                       # empty body
    ('{"reasoning": "I wrote this myself"}', 400),                   # no content_id
    ('{"content_id": "does-not-exist", "reasoning": "x"}', 404),     # unknown id
    ('{"content_id": 12345, "reasoning": "x"}', 404),                # id is a number
    ('["a"]', 400),                                                  # array, not object
]

# Criterion 10.
C10_WARMUP_TEXT = "This is a normal sentence used to warm up the model before timing."
C10_BIG_TEXT = " ".join(["word"] * 20000)
C10_LIMIT_SECONDS = 10.0

TARGETS = {
    6: "12 of 12 requests return their expected status",
    7: "10 of 10 refused requests log the expected reason",
    8: "6 of 6 texts return 200 or 400 (never 500)",
    9: "5 of 5 bad appeals return their expected status",
    10: "200 within 10 seconds",
}
NAMES = {
    6: "malformed requests: right status",
    7: "refusals: right log reason",
    8: "odd text never crashes",
    9: "bad /appeal gets a clean answer",
    10: "20,000-word text: 200 within 10 s",
}


class Context:
    """Holds what every request needs, and when the last /submit went out."""

    def __init__(self, requests_module, url, timeout):
        self.requests = requests_module
        self.url = url
        self.timeout = timeout
        self.last_submit = None   # time.monotonic() of the last /submit send

    def pace(self):
        """Wait until PACE_SECONDS have passed since the last /submit was sent."""
        if self.last_submit is None:
            return
        wait = PACE_SECONDS - (time.monotonic() - self.last_submit)
        if wait > 0:
            time.sleep(wait)

    def post(self, path, *, data=None, json_body=None, content_type="application/json"):
        """
        Send one request and return what came back.

        /submit requests are paced. Never raises: a failure comes back as an
        'error' so one bad request can't end the whole run.
        """
        if path == "/submit":
            self.pace()
            self.last_submit = time.monotonic()
        started = time.perf_counter()
        try:
            if json_body is not None:
                response = self.requests.post(f"{self.url}{path}", json=json_body,
                                              timeout=self.timeout)
            else:
                response = self.requests.post(f"{self.url}{path}", data=data,
                                              headers={"Content-Type": content_type},
                                              timeout=self.timeout)
            return {"status": response.status_code,
                    "seconds": round(time.perf_counter() - started, 3),
                    "body": response.text[:300]}
        except Exception as exc:  # noqa: BLE001
            return {"status": None,
                    "seconds": round(time.perf_counter() - started, 3),
                    "error": f"{type(exc).__name__}: {exc}"}

    def log_count(self):
        """How many lines the audit log has now (read from /health)."""
        return self.requests.get(f"{self.url}/health", timeout=10).json()["log_entries"]

    def newest_log_entry(self):
        entries = self.requests.get(f"{self.url}/log", params={"limit": 1},
                                    timeout=10).json()["entries"]
        return entries[-1] if entries else {}


def load_malformed_rows():
    with open(MALFORMED_CSV, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["id"].startswith("RQ")]
    ids = [r["id"] for r in rows]
    expected = [f"RQ{n:02d}" for n in range(1, 13)]
    if ids != expected:
        sys.exit(f"Expected rows {expected[0]}..{expected[-1]} in {MALFORMED_CSV.name}, got {ids}")
    return rows


def criteria_6_and_7(ctx, rows):
    """
    Criterion 6: each row gets its expected status.
    Criterion 7: after each REFUSED row, the log grew by one line and the newest
    line has the expected reason.

    One pass answers both, because they use the same 12 requests.
    """
    c6, c7 = [], []
    for row in rows:
        rid = row["id"]
        content_type = row["content_type"] or "application/json"
        before = ctx.log_count()
        result = ctx.post("/submit", data=row["raw_body"].encode("utf-8"),
                          content_type=content_type)
        after = ctx.log_count()
        newest = ctx.newest_log_entry()

        expected_status = 200 if rid in ACCEPTED_ROWS else 400
        c6.append({"id": rid, "expected_status": expected_status,
                   "status": result["status"], "ok": result["status"] == expected_status,
                   "response": result.get("body") or result.get("error")})

        if rid not in ACCEPTED_ROWS:
            expected_reason = EXPECTED_REASON[rid]
            new_line = after == before + 1
            got = newest.get("reason")
            c7.append({"id": rid, "expected_reason": expected_reason, "reason": got,
                       "new_line": new_line, "ok": new_line and got == expected_reason,
                       "newest_log_line": newest})
        print(f"    {rid}: status {result['status']}")
    return c6, c7


def criterion_8(ctx):
    """Six odd texts, sent as JSON to /submit. Pass = 200 or 400 for each."""
    records = []
    for i, text in enumerate(C8_TEXTS, 1):
        result = ctx.post("/submit",
                          json_body={"text": text, "creator_id": f"capstone_c8_{i}"})
        records.append({"n": i, "text": text, "status": result["status"],
                        "ok": result["status"] in (200, 400),
                        "response": result.get("body") or result.get("error")})
        print(f"    text {i}: status {result['status']}")
    return records


def criterion_9(ctx):
    """Five bad bodies sent to /appeal as JSON. Pass = the exact status for each."""
    records = []
    for i, (body, expected) in enumerate(C9_ROWS, 1):
        result = ctx.post("/appeal", data=body.encode("utf-8"))
        records.append({"n": i, "sent": body or "(empty body)", "expected_status": expected,
                        "status": result["status"], "ok": result["status"] == expected,
                        "response": result.get("body") or result.get("error")})
        print(f"    appeal {i}: status {result['status']}")
    return records


def criterion_10(ctx):
    """One normal warm-up request, then the 20,000-word text, timed."""
    warmup = ctx.post("/submit", json_body={"text": C10_WARMUP_TEXT,
                                            "creator_id": "capstone_c10_warmup"})
    big = ctx.post("/submit", json_body={"text": C10_BIG_TEXT,
                                         "creator_id": "capstone_c10_big"})
    ok = big["status"] == 200 and big["seconds"] <= C10_LIMIT_SECONDS
    print(f"    warm-up: status {warmup['status']} in {warmup['seconds']}s")
    print(f"    20,000 words: status {big['status']} in {big['seconds']}s")
    return [{"warmup_status": warmup["status"], "warmup_seconds": warmup["seconds"],
             "status": big["status"], "seconds": big["seconds"],
             "limit_seconds": C10_LIMIT_SECONDS, "ok": ok,
             "response": big.get("body") or big.get("error")}]


def cell(number, records):
    """The run-log cell for one criterion in one trial."""
    if number == 10:
        r = records[0]
        return f"{'PASS' if r['ok'] else 'FAIL'} ({r['status']}, {r['seconds']}s)"
    passed = sum(1 for r in records if r["ok"])
    return f"{passed}/{len(records)}"


def trial_met(records):
    return all(r["ok"] for r in records)


def write_report(all_trials, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"capstone_run_{stamp}{label}.md"
    n = len(all_trials)

    lines = [
        f"# Capstone run log{f' - {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_capstone_eval.py::main`",
        "- 6 and 7: `criteria_6_and_7` · 8: `criterion_8` · 9: `criterion_9` · 10: `criterion_10`",
        "- Service: `app.py::submit`, `app.py::appeal`",
        f"- {n} trials per criterion · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"| Criterion | Target | {' | '.join(f'Run {i}' for i in range(1, n + 1))} | Verdict |",
        f"|---|---|{'|'.join(['---'] * n)}|---|",
    ]
    for number in (6, 7, 8, 9, 10):
        cells = [cell(number, t[number]) for t in all_trials]
        verdict = "MET" if all(trial_met(t[number]) for t in all_trials) else "MISSED"
        lines.append(f"| {number}. {NAMES[number]} | {TARGETS[number]} | "
                     f"{' | '.join(cells)} | {verdict} |")

    lines += ["", "---", "", "## What actually came back", "",
              "Real output from every trial. Paste the relevant parts into the README.", ""]
    for number in (6, 7, 8, 9, 10):
        lines += [f"### Criterion {number}: {NAMES[number]}", ""]
        for i, t in enumerate(all_trials, 1):
            lines += [f"**Trial {i}**", "", "```json",
                      json.dumps(t[number], indent=2), "```", ""]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Check the Verdict column yourself before you paste it anywhere.")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        sys.exit("The `requests` package isn't installed.\nRun: pip install -r requirements.txt")

    try:
        health = requests.get(f"{args.url}/health", timeout=5).json()
    except Exception:  # noqa: BLE001
        sys.exit(f"Nothing answering at {args.url}. Start it:  python app.py")

    rows = load_malformed_rows()
    ctx = Context(requests, args.url, args.timeout)

    submits = len(rows) + len(C8_TEXTS) + 2
    print(f"Rate limiting on: {health.get('rate_limiting')}")
    print(f"{submits} paced /submit requests per trial, {PACE_SECONDS:.0f}s apart: "
          f"about {submits * PACE_SECONDS / 60:.1f} minutes per trial.")
    if args.trials < 3:
        print(f"!! {args.trials} trial(s). The submission asks for three.")

    all_trials = []
    for trial in range(1, args.trials + 1):
        print(f"\n=== Trial {trial} of {args.trials} ===")
        print("  criteria 6 and 7")
        c6, c7 = criteria_6_and_7(ctx, rows)
        print("  criterion 8")
        c8 = criterion_8(ctx)
        print("  criterion 9")
        c9 = criterion_9(ctx)
        print("  criterion 10")
        c10 = criterion_10(ctx)
        all_trials.append({6: c6, 7: c7, 8: c8, 9: c9, 10: c10})
        print("  trial summary: " + ", ".join(
            f"{n}: {cell(n, all_trials[-1][n])}" for n in (6, 7, 8, 9, 10)))

    write_report(all_trials, args)


if __name__ == "__main__":
    main()
