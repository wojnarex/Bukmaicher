---
description: Wykonaj codzienny briefing typerski Bukmaichera (rozliczenie + research + typy + e-mail)
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Bash(git:*), Bash(python3:*), mcp__Gmail__create_draft, mcp__Gmail__create_label, mcp__Gmail__list_labels, mcp__Gmail__label_message
---

Wykonaj **codzienny briefing** dokładnie według procedury w `playbook/BRIEFING.md`.

Zanim zaczniesz:
1. `git pull --rebase` na bieżącym branchu (żeby mieć najnowszy stan/pamięć).
2. Wczytaj `config/config.yaml` i `state/strategy.md`, sprawdź `python3 scripts/state_tool.py pending` oraz `bankroll`.

Następnie przejdź kroki 0–9 z playbooka:
- najpierw **rozlicz** otwarte typy z poprzednich dni (krok 1),
- zbadaj mecze, newsy, staty, kursy (kroki 2–5),
- zaproponuj **typy na kicktippa** i **value bety STS** wg zasad z configa (kroki 6–7),
- zaktualizuj **strategię** (krok 8),
- złóż i dostarcz **briefing e-mail** wg `delivery.mode`, zapisz stan przez `state_tool.py`,
  odśwież CSV i **zacommituj + wypchnij** zmiany (krok 9).

Pamiętaj o zasadach naczelnych: po polsku, tylko rekomendacje (nie wpisujesz typów za użytkownika),
oddzielaj twarde dane od estymacji, respektuj limity odpowiedzialnej gry.

Argument opcjonalny ($ARGUMENTS): jeśli podano datę lub „dry-run", uwzględnij to
(np. „dry-run" = przygotuj briefing jako draft, ale NIE commituj stanu).
