# CLAUDE.md — Bukmaicher

Projekt: **codzienny briefing typerski** na Mistrzostwa Świata 2026 i naszą ligę
kicktipp, dostarczany na Gmaila. Silnik to **zaplanowana sesja Claude + web search**
(bez zewnętrznych API), z pamięcią wersjonowaną w gicie.

## Jak to uruchomić
- Główne wejście: komenda **`/briefing`** (patrz `.claude/commands/briefing.md`),
  która wykonuje pełną procedurę z `playbook/BRIEFING.md`.
- W sesji zaplanowanej (trigger w Claude Code on the web) prompt to po prostu:
  „Wykonaj `/briefing`". Szczegóły: `docs/SCHEDULING.md`.

## Mapa repo
- `config/config.yaml` — JEDYNY plik, który zwykle edytuje użytkownik (odbiorca, liga, STS, limity).
- `playbook/BRIEFING.md` — krok-po-kroku procedura briefingu (rdzeń logiki).
- `scripts/state_tool.py` — wszystkie mutacje pamięci (add-pick / settle / pending / bankroll / rebuild-csv).
- `scripts/send_email.py` — opcjonalna realna wysyłka SMTP (domyślnie używamy draftu Gmaila).
- `state/` — pamięć: `history.jsonl` (typy), `bankroll.json`, `strategy.md` (wersjonowana), `history.csv`.
- `docs/` — `SCHEDULING.md`, `DELIVERY.md`, `SHEETS.md`.

## Zasady naczelne (NIE łamać)
1. **Po polsku.** Briefing i komunikacja z użytkownikiem po polsku.
2. **Tylko rekomendacje.** Nie logujemy się do kicktippa/STS i nie wysyłamy typów za użytkownika.
3. **Twarde dane vs estymacje.** Zawsze rozróżniaj; przy szacunkach pisz „szac." i podawaj źródła kursów/newsów.
4. **Najpierw rozliczenie.** Każdy run zaczyna od rozliczenia wczorajszych typów (pętla nauki).
5. **Stan = git.** Po briefingu zaktualizuj `state/` przez `state_tool.py`, odśwież CSV, **commit + push**.
6. **Odpowiedzialna gra.** Respektuj limity z `config.responsible_gambling`. Anty-tilt: nigdy nie podbijaj stawek na odrobienie strat.

## Ograniczenia środowiska (ważne)
- Konektor **Gmail** ma tylko `create_draft` (brak „wyślij") → domyślne dostarczanie to **draft** + etykieta.
  Realny inbox = opcjonalny `scripts/send_email.py` (SMTP + hasło aplikacji), patrz `docs/DELIVERY.md`.
- Konektor **Google Drive** tworzy/czyta pliki, ale **nie dopisuje wierszy do Arkuszy** → dlatego pamięć
  trzymamy w gicie, a do Arkuszy eksportujemy `state/history.csv` (patrz `docs/SHEETS.md`).
