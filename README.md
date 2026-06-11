# ⚽ Bukmaicher

Codzienny **briefing typerski** na Mistrzostwa Świata 2026 i naszą ligę kicktipp —
prosto na Gmaila. Inspirowany botem kolegi (cron → API → LLM → Telegram), ale w wersji
**bez własnego serwera i bez zewnętrznych kluczy API**: napędza go zaplanowana sesja
**Claude Code + web search**, a pamięć żyje w tym repo (git).

## Co robi każdego ranka

1. **Rozlicza wczorajsze typy** — sprawdza wyniki, liczy punkty kicktipp i P/L na STS, aktualizuje bankroll.
2. **Bada mecze dnia** — terminarz, godziny (czas PL), kontekst.
3. **Newsy kadrowe** — kontuzje, zawieszenia, przewidywane składy, motywacja, warunki.
4. **Statystyki** — forma, xG (szac.), H2H, kontekst historyczny.
5. **Kursy** — zbiera kursy rynkowe (1X2, O/U, BTTS…) i liczy prawdopodobieństwa po marży.
6. **Typy na kicktippa** — dokładne wyniki maksymalizujące oczekiwane punkty wg punktacji ligi.
7. **Value bety na STS** — tylko gdy jest realna przewaga (edge), z rozsądnym sizingiem stawki.
8. **Aktualizuje strategię** — uczy się na wynikach, koryguje lub kontynuuje podejście.
9. **Wysyła briefing na Gmaila** i zapisuje historię (commit do gita).

> **Tryb: tylko rekomendacje.** Bot podpowiada, co wpisać na kicktippie i co rozważyć na STS —
> typy wpisujesz samodzielnie. Nie loguje się nigdzie w Twoim imieniu.

## Architektura w jednym akapicie

Nie ma osobnego backendu. Każdego ranka **zaplanowana sesja Claude Code on the web**
uruchamia komendę `/briefing`, która wykonuje procedurę z [`playbook/BRIEFING.md`](playbook/BRIEFING.md):
research robi **web search**, pamięć (typy, bankroll, strategia) trzyma **git** w katalogu
[`state/`](state/), a podsumowanie ląduje w **Gmailu** (domyślnie jako wersja robocza z etykietą `Bukmaicher`).

```
trigger (co rano) ──▶ /briefing ──▶ playbook
                                     ├─ web search: newsy, kursy, staty
                                     ├─ state_tool.py: rozlicz + zapisz typy + bankroll
                                     ├─ strategy.md: aktualizacja strategii
                                     └─ outbox/ + git push ─▶ GitHub Action ─▶ Gmail (inbox)
```

## Szybki start

1. **Uzupełnij `config/config.yaml`** (jedyny plik, który zwykle ruszasz):
   - `delivery.recipient` — Twój Gmail (domyślnie już ustawiony),
   - `kicktipp.league_name` / `league_url` — nazwa i link naszej ligi (pola „TODO"),
   - `kicktipp.scoring` — **realna punktacja** waszej ligi (kluczowe dla jakości typów!),
   - `focus.favorite_teams` — np. `["Polska"]`, jeśli chcesz dodatkowy fokus,
   - `sts.*` — bankroll, limity, profil ryzyka.
2. **Ustaw poranny trigger** — patrz [`docs/SCHEDULING.md`](docs/SCHEDULING.md).
3. (opcjonalnie) **Realna wysyłka na inbox** zamiast draftu — [`docs/DELIVERY.md`](docs/DELIVERY.md).
4. Test od ręki: w sesji w tym repo napisz `/briefing` (albo `/briefing dry-run`).

## Personalizacja

Wszystko siedzi w `config/config.yaml` (odbiorca, godzina, liga + punktacja, rynki STS,
bankroll, profil ryzyka, limity odpowiedzialnej gry). Strategię bot rozwija sam w
[`state/strategy.md`](state/strategy.md) — możesz tam też dopisać własne wskazówki, a uszanuje je.

## Ograniczenia (świadome wybory projektowe)

- **Dane z web searcha** — świetne na newsy/kursy/formę; głębokie xG bywa za paywallem,
  więc część statystyk to oznaczone estymacje („szac.").
- **Realny inbox** = GitHub Action wysyła maila (bezpośredni SMTP z sandboxa jest zablokowany); albo tryb `draft` bez setupu.
- **Pamięć w gicie, nie w Arkuszach** (konektor Drive nie dopisuje wierszy) — eksport CSV do Arkuszy
  jest opisany w [`docs/SHEETS.md`](docs/SHEETS.md).

## Odpowiedzialna gra

Tylko 18+. STS to licencjonowany bukmacher w PL. Bot pilnuje bankrolla i twardych limitów
(`config.responsible_gambling`), nigdy nie namawia do gry ponad budżet i stosuje zasadę anty-tilt
(żadnego „odrabiania" stawkami). To narzędzie analityczne, nie gwarancja wygranej.

## Pomysły na rozbudowę

- Twarde dane z API (The Odds API / API-Football) zamiast/oprócz web searcha.
- Żywa synchronizacja z Arkuszem Google (konto serwisowe).
- Powiadomienia push (Telegram/Discord) obok maila.
- Backtesting strategii na historii z `state/history.jsonl`.
