# Dostarczanie briefingu — realny inbox (GitHub Action) vs draft

## TL;DR

- **`delivery.mode: github_action`** (domyślnie) → briefing realnie **wchodzi na skrzynkę** (powiadomienie na telefon).
  Sesja Claude zapisuje maila do `outbox/` i pushuje; wysyła go **GitHub Action**.
- **`delivery.mode: draft`** → briefing ląduje w **Wersjach roboczych** Gmaila (zero setupu, ale bez powiadomienia).

## Dlaczego GitHub Action, a nie SMTP prosto z sesji Claude?

Sprawdzone: środowisko Claude Code on the web **blokuje wychodzący ruch SMTP**
(surowe gniazda do `smtp.gmail.com:587/465` są niedostępne). A konektor Gmaila ma tylko
`create_draft` (brak „wyślij"). Dlatego realną wysyłkę zrzucamy na **runner GitHub Actions**,
który dostęp do SMTP ma. Hasło aplikacji Gmaila trzymamy bezpiecznie w **GitHub Secrets**
(nie w repo, nie w czacie, nie w logach).

```
poranna sesja Claude ──▶ zapisuje outbox/briefing-latest.html + .subject ──▶ git push
                                                                                  │
                          GitHub Action (.github/workflows/send-briefing.yml) ◀───┘
                                          │ scripts/send_email.py (SMTP)
                                          ▼
                                   Twoja skrzynka Gmail 📬
```

## Konfiguracja realnej wysyłki (jednorazowo, ~5 min)

1. **Hasło aplikacji Google** (wymaga włączonej weryfikacji dwuetapowej):
   wejdź na https://myaccount.google.com/apppasswords i wygeneruj 16-znakowe hasło. Skopiuj (bez spacji).
2. **Dodaj sekrety w repo GitHub**: *Settings → Secrets and variables → Actions → New repository secret*:
   - `GMAIL_ADDRESS` = `mwmw91@gmail.com`
   - `GMAIL_APP_PASSWORD` = (wygenerowane hasło aplikacji)
3. **Włącz Actions** (jeśli wyłączone): zakładka *Actions* w repo → zaakceptuj uruchamianie workflow.
4. **Test**: zakładka *Actions* → *Wyślij briefing (Bukmaicher)* → *Run workflow* (wybierz branch) →
   po chwili mail powinien być na skrzynce. Od teraz każdy nowy briefing wysyła się sam po pushu.

> Bezpieczeństwo: hasło aplikacji jest wąsko ograniczone i **odwoływalne** w każdej chwili
> (https://myaccount.google.com/apppasswords). Nigdy nie podawaj go w czacie ani nie commituj do repo —
> wpisz je tylko w GitHub Secrets.

## Fallback / wariant bez GitHub Actions

Jeśli nie chcesz używać Actions, ustaw `delivery.mode: draft`. Wtedy briefing tworzy się jako
**wersja robocza** w Gmailu (etykieta `Bukmaicher`) — czytasz go w *Wersje robocze*. Działa od ręki,
bez sekretów, ale Gmail nie przyśle powiadomienia „nowa wiadomość".

## Uruchomienie sendera lokalnie (np. z własnego komputera)

`scripts/send_email.py` działa też samodzielnie wszędzie tam, gdzie SMTP nie jest blokowany:
```
export GMAIL_ADDRESS=mwmw91@gmail.com
export GMAIL_APP_PASSWORD=xxxxxxxxxxxxxxxx
python3 scripts/send_email.py --to mwmw91@gmail.com \
    --subject "$(head -n1 outbox/briefing-latest.subject)" --html-file outbox/briefing-latest.html
```

## Inne kanały (na przyszłość)

Powiadomienia push poza mailem (Telegram/Discord/Slack przez webhook) też są możliwe —
wystarczy dołożyć analogiczny krok wysyłki w workflow i przełącznik w `config.delivery`.
