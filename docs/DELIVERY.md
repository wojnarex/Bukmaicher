# Dostarczanie briefingu — draft (domyślnie) vs realny inbox (SMTP)

## Dlaczego domyślnie „draft"?

Podłączony konektor **Gmail** w tym środowisku udostępnia tworzenie wersji roboczej
(`create_draft`), ale **nie ma operacji „wyślij"**. Dlatego domyślnie (`config.delivery.mode: draft`)
bot tworzy briefing jako **wersję roboczą w Twoim Gmailu**, adresowaną na `delivery.recipient`,
i nakłada etykietę `delivery.gmail_label` (`Bukmaicher`).

Jak czytać: Gmail → **Wersje robocze** (Drafts) → albo filtr po etykiecie `Bukmaicher`.
Plus: zero konfiguracji, działa od ręki. Minus: nie ma powiadomienia „nowa wiadomość".

## Upgrade: realna wysyłka na skrzynkę (powiadomienie na telefon)

Jeśli chcesz, by briefing **wchodził na inbox** (i pingował telefon), włącz tryb SMTP.
Wymaga to jednorazowo **hasła aplikacji Google** (5 minut):

1. Włącz weryfikację dwuetapową na koncie Google (jeśli nie masz).
2. Wejdź na https://myaccount.google.com/apppasswords i wygeneruj **hasło aplikacji**
   (16 znaków). Skopiuj je (bez spacji).
3. Ustaw sekrety środowiska (NIE commituj ich do repo):
   - `GMAIL_ADDRESS` = Twój adres (np. `mwmw91@gmail.com`)
   - `GMAIL_APP_PASSWORD` = wygenerowane hasło aplikacji
   W Claude Code on the web dodaj je jako zmienne środowiskowe/sekrety środowiska
   (patrz https://code.claude.com/docs/en/claude-code-on-the-web).
4. Ustaw w `config/config.yaml`: `delivery.mode: "smtp"`.

Wtedy krok 9 playbooka wyśle maila realnie:
```
python3 scripts/send_email.py --to mwmw91@gmail.com \
    --subject "Bukmaicher — briefing 2026-06-11" --html-file /tmp/briefing.html
```
Jeśli wysyłka się nie powiedzie (np. sieć blokuje SMTP) — bot robi **fallback na draft**,
więc nigdy nie zostajesz bez briefingu.

> Uwaga: smtp.gmail.com:587 wymaga, by polityka sieciowa środowiska pozwalała na ruch wychodzący SMTP.
> Jeśli jest restrykcyjna, zostań przy trybie `draft`.

## Inne kanały (na przyszłość)

Telegram/Discord/Slack też są możliwe (webhook), gdyby kiedyś jednak chciał wrócić
do powiadomień push poza mailem — wystarczy dołożyć analogiczny mały skrypt-sender
i przełącznik w `config.delivery`.
