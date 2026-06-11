#!/usr/bin/env python3
"""
Bukmaicher — narzędzie do zarządzania stanem (pamięcią) bota.

Pamięć to pliki w katalogu state/:
  - history.jsonl   : append-only log typów (jeden JSON na linię), z cyklem życia pending->settled
  - bankroll.json   : stan wirtualnego bankrolla + suma punktów kicktipp
  - history.csv     : spłaszczony widok historii (do podejrzenia / importu do Arkuszy)

Wszystkie mutacje stanu robimy przez ten skrypt, żeby były spójne i deterministyczne.
Tylko biblioteka standardowa — działa wszędzie, bez instalacji.

Przykłady:
  python3 scripts/state_tool.py add-pick --json '{"match":"Mexico vs South Africa",
      "type":"kicktipp","market":"exact_score","selection":"2:0","model_prob":0.5,
      "rationale":"gospodarz-faworyt, niski O/U","match_date":"2026-06-11"}'

  python3 scripts/state_tool.py settle --id 2026-06-11-kicktipp-mexico-vs-south-africa \
      --status won --result "2:0" --points 4

  python3 scripts/state_tool.py pending
  python3 scripts/state_tool.py bankroll
  python3 scripts/state_tool.py rebuild-csv
  python3 scripts/state_tool.py show --date 2026-06-11
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
HISTORY = STATE / "history.jsonl"
BANKROLL = STATE / "bankroll.json"
CSV_PATH = STATE / "history.csv"

# Kolejność i zestaw kolumn w history.csv / w rekordzie typu.
FIELDS = [
    "id", "date", "match_date", "competition", "match", "type", "market",
    "selection", "odds", "stake", "model_prob", "fair_odds", "edge",
    "status", "result", "points", "pnl", "rationale", "created_at", "settled_at",
]


# --------------------------------------------------------------------------- #
# Pomocnicze I/O
# --------------------------------------------------------------------------- #
def _today() -> str:
    return date.today().isoformat()


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s or "x"


def load_history() -> list[dict]:
    if not HISTORY.exists():
        return []
    rows = []
    for line in HISTORY.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"OSTRZEŻENIE: pomijam uszkodzoną linię historii: {e}", file=sys.stderr)
    return rows


def write_history(rows: list[dict]) -> None:
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    with HISTORY.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_bankroll() -> dict:
    if BANKROLL.exists():
        return json.loads(BANKROLL.read_text(encoding="utf-8"))
    # Sensowny default, gdyby pliku brakło.
    return {
        "currency": "PLN",
        "starting_bankroll": 1000.0,
        "current_bankroll": 1000.0,
        "unit_pct": 0.02,
        "kicktipp_points_total": 0,
        "bets_settled": 0,
        "updated_at": _today(),
    }


def write_bankroll(bk: dict) -> None:
    bk["updated_at"] = _today()
    BANKROLL.parent.mkdir(parents=True, exist_ok=True)
    BANKROLL.write_text(json.dumps(bk, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rebuild_csv() -> int:
    rows = load_history()
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    return len(rows)


# --------------------------------------------------------------------------- #
# Komendy
# --------------------------------------------------------------------------- #
def cmd_add_pick(args) -> None:
    if args.json:
        data = json.loads(args.json)
    else:
        data = {}
    # Pozwól nadpisać/uzupełnić pojedynczymi flagami.
    for key in ("match", "type", "market", "selection", "rationale", "match_date", "status"):
        val = getattr(args, key, None)
        if val is not None:
            data[key] = val
    for key in ("odds", "stake", "model_prob", "fair_odds", "edge", "points", "pnl"):
        val = getattr(args, key, None)
        if val is not None:
            data[key] = val

    if not data.get("match") or not data.get("type"):
        sys.exit("BŁĄD: 'match' i 'type' są wymagane (kicktipp|sts).")

    today = _today()
    rec = {k: None for k in FIELDS}
    rec.update(data)
    rec["date"] = data.get("date") or today
    rec["match_date"] = data.get("match_date") or rec["date"]
    rec["competition"] = data.get("competition") or "WC2026"
    rec["status"] = data.get("status") or "pending"
    rec["created_at"] = _now()
    if not rec.get("id"):
        rec["id"] = f'{rec["match_date"]}-{_slug(rec["type"])}-{_slug(rec["match"])}-{_slug(str(rec.get("market","")))}'.rstrip("-")
    # fair_odds z model_prob, jeśli się da i nie podano.
    if rec.get("model_prob") and not rec.get("fair_odds"):
        try:
            rec["fair_odds"] = round(1.0 / float(rec["model_prob"]), 3)
        except (ValueError, ZeroDivisionError):
            pass

    rows = load_history()
    if any(r.get("id") == rec["id"] for r in rows):
        sys.exit(f"BŁĄD: typ o id '{rec['id']}' już istnieje (duplikat?). Użyj innego --id albo settle.")
    rows.append(rec)
    write_history(rows)
    n = rebuild_csv()
    print(f"OK: dodano typ {rec['id']}  ({rec['type']}/{rec.get('market')}: {rec.get('selection')}). Historia: {n} rekordów.")


def cmd_settle(args) -> None:
    rows = load_history()
    match = [r for r in rows if r.get("id") == args.id]
    if not match:
        sys.exit(f"BŁĄD: nie znaleziono typu o id '{args.id}'. Sprawdź `pending`.")
    rec = match[0]
    if rec.get("status") not in (None, "pending"):
        print(f"OSTRZEŻENIE: typ {args.id} był już rozliczony ({rec.get('status')}). Nadpisuję.", file=sys.stderr)

    rec["status"] = args.status
    if args.result is not None:
        rec["result"] = args.result
    if args.points is not None:
        rec["points"] = args.points
    if args.pnl is not None:
        rec["pnl"] = args.pnl
    rec["settled_at"] = _now()

    # Aktualizacja bankrolla / punktów.
    bk = load_bankroll()
    if args.pnl is not None and rec.get("type") == "sts":
        bk["current_bankroll"] = round(float(bk.get("current_bankroll", 0)) + float(args.pnl), 2)
        bk["bets_settled"] = int(bk.get("bets_settled", 0)) + 1
    if args.points is not None and rec.get("type") == "kicktipp":
        bk["kicktipp_points_total"] = int(bk.get("kicktipp_points_total", 0)) + int(args.points)

    write_history(rows)
    write_bankroll(bk)
    rebuild_csv()
    extra = []
    if args.points is not None:
        extra.append(f"+{args.points} pkt")
    if args.pnl is not None:
        extra.append(f"P/L {args.pnl:+.2f} {bk.get('currency','PLN')}")
    print(f"OK: rozliczono {args.id} -> {args.status} ({rec.get('result')}). " + " | ".join(extra))
    print(f"Bankroll: {bk['current_bankroll']} {bk.get('currency','PLN')} | punkty kicktipp: {bk['kicktipp_points_total']}")


def cmd_pending(args) -> None:
    rows = [r for r in load_history() if r.get("status") in (None, "pending")]
    if not rows:
        print("Brak otwartych (nierozliczonych) typów.")
        return
    rows.sort(key=lambda r: (r.get("match_date") or "", r.get("type") or ""))
    print(f"Otwarte typy ({len(rows)}):")
    for r in rows:
        line = f'  [{r.get("match_date")}] {r.get("id")}'
        line += f' | {r.get("type")}/{r.get("market")}: {r.get("selection")}'
        if r.get("odds"):
            line += f' @ {r.get("odds")}'
        if r.get("stake"):
            line += f' (stawka {r.get("stake")})'
        print(line)


def cmd_bankroll(args) -> None:
    bk = load_bankroll()
    cur = bk.get("currency", "PLN")
    start = float(bk.get("starting_bankroll", 0))
    now = float(bk.get("current_bankroll", 0))
    roi = ((now - start) / start * 100) if start else 0.0
    print(f"Bankroll: {now:.2f} {cur} (start {start:.2f}, zmiana {now-start:+.2f}, ROI {roi:+.1f}%)")
    print(f"Jednostka (1u): {now*float(bk.get('unit_pct',0.02)):.2f} {cur}  [{float(bk.get('unit_pct',0.02))*100:.1f}% bankrolla]")
    print(f"Punkty kicktipp łącznie: {bk.get('kicktipp_points_total', 0)}")
    print(f"Rozliczone zakłady STS: {bk.get('bets_settled', 0)} | aktualizacja: {bk.get('updated_at')}")


def cmd_show(args) -> None:
    rows = load_history()
    if args.date:
        rows = [r for r in rows if args.date in (r.get("date"), r.get("match_date"))]
    if args.status:
        rows = [r for r in rows if r.get("status") == args.status]
    if not rows:
        print("Brak rekordów dla podanych kryteriów.")
        return
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))


def cmd_rebuild_csv(args) -> None:
    n = rebuild_csv()
    print(f"OK: odświeżono {CSV_PATH.relative_to(ROOT)} ({n} rekordów).")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Bukmaicher state tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    ap = sub.add_parser("add-pick", help="dodaj nowy typ (pending)")
    ap.add_argument("--json", help="rekord typu jako JSON (zalecane)")
    for k in ("match", "type", "market", "selection", "rationale", "match-date", "status"):
        ap.add_argument(f"--{k}", dest=k.replace("-", "_"))
    for k in ("odds", "stake", "model_prob", "fair_odds", "edge", "pnl"):
        ap.add_argument(f"--{k}", type=float)
    ap.add_argument("--points", type=int)
    ap.set_defaults(func=cmd_add_pick)

    sp = sub.add_parser("settle", help="rozlicz istniejący typ")
    sp.add_argument("--id", required=True)
    sp.add_argument("--status", required=True, choices=["won", "lost", "void", "partial"])
    sp.add_argument("--result", help="faktyczny wynik meczu, np. '2:1'")
    sp.add_argument("--points", type=int, help="punkty kicktipp")
    sp.add_argument("--pnl", type=float, help="zysk/strata STS w walucie bankrolla")
    sp.set_defaults(func=cmd_settle)

    pp = sub.add_parser("pending", help="pokaż otwarte typy")
    pp.set_defaults(func=cmd_pending)

    bp = sub.add_parser("bankroll", help="pokaż stan bankrolla")
    bp.set_defaults(func=cmd_bankroll)

    shp = sub.add_parser("show", help="pokaż rekordy (filtry: --date, --status)")
    shp.add_argument("--date")
    shp.add_argument("--status")
    shp.set_defaults(func=cmd_show)

    rp = sub.add_parser("rebuild-csv", help="odśwież history.csv z history.jsonl")
    rp.set_defaults(func=cmd_rebuild_csv)
    return p


def main(argv=None) -> None:
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
