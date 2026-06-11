#!/usr/bin/env python3
"""
Bukmaicher — OPCJONALNA realna wysyłka briefingu na inbox przez Gmail SMTP.

Domyślny tryb bota to "draft" (wersja robocza w Gmailu przez konektor) i nie wymaga
tego skryptu. Użyj go tylko, jeśli chcesz, żeby briefing realnie WCHODZIŁ na skrzynkę
(z powiadomieniem na telefon). Wymaga "hasła aplikacji" Google — instrukcja w docs/DELIVERY.md.

Konfiguracja przez zmienne środowiskowe (sekrety — NIE commituj ich):
  GMAIL_ADDRESS        adres nadawcy = odbiorcy (np. mwmw91@gmail.com)
  GMAIL_APP_PASSWORD   16-znakowe hasło aplikacji Google (bez spacji)

Użycie:
  python3 scripts/send_email.py --to mwmw91@gmail.com \
      --subject "Bukmaicher — briefing 2026-06-11" --html-file /tmp/briefing.html
  # albo HTML ze stdin:
  cat briefing.html | python3 scripts/send_email.py --to mwmw91@gmail.com --subject "..." --html-stdin

Kod wyjścia: 0 = wysłano, !=0 = błąd (bot powinien wtedy zrobić fallback na draft).
"""
from __future__ import annotations

import argparse
import os
import smtplib
import sys
from email.message import EmailMessage

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def main() -> int:
    ap = argparse.ArgumentParser(description="Wyślij briefing przez Gmail SMTP")
    ap.add_argument("--to", required=True)
    ap.add_argument("--subject", required=True)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--html-file", help="ścieżka do pliku HTML z treścią")
    src.add_argument("--html-stdin", action="store_true", help="czytaj HTML ze stdin")
    ap.add_argument("--text", default="Twój klient poczty nie wyświetla HTML. Otwórz w widoku HTML.")
    args = ap.parse_args()

    user = os.environ.get("GMAIL_ADDRESS")
    pwd = os.environ.get("GMAIL_APP_PASSWORD")
    if not user or not pwd:
        print("BŁĄD: brak GMAIL_ADDRESS / GMAIL_APP_PASSWORD w środowisku.", file=sys.stderr)
        return 2

    html = sys.stdin.read() if args.html_stdin else open(args.html_file, encoding="utf-8").read()

    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = args.to
    msg["Subject"] = args.subject
    msg.set_content(args.text)
    msg.add_alternative(html, subtype="html")

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as s:
            s.starttls()
            s.login(user, pwd)
            s.send_message(msg)
    except Exception as e:  # noqa: BLE001 — chcemy czytelny komunikat + niezerowy kod
        print(f"BŁĄD wysyłki SMTP: {e}", file=sys.stderr)
        return 1
    print(f"OK: wysłano '{args.subject}' do {args.to}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
