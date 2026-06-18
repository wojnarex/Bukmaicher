# Harmonogram — codzienne odpalanie briefingu

Silnik Bukmaichera to **zaplanowana sesja Claude Code on the web**, która każdego ranka
uruchamia komendę `/briefing` w tym repozytorium. Nie potrzebujesz własnego serwera ani crona.

## Jak ustawić poranny trigger

1. Wejdź na **claude.ai/code** (Claude Code on the web) i otwórz repo (`wojnarex/Bukmaicher`).
2. Utwórz **zaplanowany trigger** (scheduled session):
   - **harmonogram:** codziennie ok. **07:45** Europe/Warsaw (sesja generuje + pushuje ~kilka min,
     potem GitHub Action wysyła maila → wiadomość ląduje ~08:00; albo ustaw 08:00 bez tej rezerwy).
   - **branch:** **`main`** (gałąź produkcyjna = pamięć bota).
   - **prompt sesji (Instructions):** wklej DOKŁADNIE blok poniżej.
3. Zapisz.

### Prompt do wklejenia (Instructions rutyny)

```
Wykonaj codzienny briefing typerski „Bukmaicher" (repo wojnarex/Bukmaicher) zgodnie z playbook/BRIEFING.md.

PAMIĘĆ NA STAŁYM BRANCHU main (krytyczne — inaczej co dzień rozliczasz 1. kolejkę i gubisz typy):
- Start:  git fetch origin && git checkout main && git pull --no-edit origin main
- Koniec: git add -A && git commit -m "briefing <data>" && git push origin HEAD:main
- NIE twórz nowego brancha per uruchomienie.

Procedura (pełnia w playbook/BRIEFING.md):
0. „Dziś" turniejowe licz w strefie gospodarzy ET (focus.schedule_timezone). Wczytaj config/config.yaml i state/strategy.md.
1. Rozlicz TYLKO gotowe mecze: python3 scripts/state_tool.py pending --due ; dla każdego web search o wynik i python3 scripts/state_tool.py settle ... (idempotentne — nie rozliczy 2x ani meczu sprzed gwizdka).
2-5. Mecze dnia ET + lookahead; newsy kadrowe (ROZRÓŻNIAJ skład potwierdzony od przewidywanego); staty; kursy (de-vig).
6. Typy na kicktippa pod „9-tkę" + kicktipp.draw_bias (przemnóż remisy, renormalizuj); o typie decyduje siła ofensywna faworyta (cagey → remis; atak w formie → wygrana). Zapisz przez state_tool.py add-pick.
7. Value bety u Fortuny tylko przy edge ≥ progu i w limitach z configu.
8. Zaktualizuj state/strategy.md (pętla nauki).
9. Złóż maila (HTML, po polsku) → zapisz do outbox/briefing-latest.html oraz outbox/briefing-latest.subject (GitHub Action wyśle); odśwież CSV; commit + push na main (jak wyżej).

Zasady: po polsku; TYLKO rekomendacje (nie wpisuj typów za użytkownika); twarde dane vs estymacje („szac."); respektuj responsible_gambling; w mailu przypomnij o weryfikacji oficjalnych składów przed deadline (zwłaszcza mecze wieczorne/nocne).
```

> Pełna, aktualna instrukcja konfiguracji środowisk i triggerów:
> https://code.claude.com/docs/en/claude-code-on-the-web

## Uwaga o sieci (network policy)

Briefing korzysta z **web searcha** (newsy, kursy, staty) oraz z konektorów Google.
Upewnij się, że środowisko ma politykę sieciową pozwalającą na ruch wychodzący do internetu
(do researchu). Dostarczanie przez **draft Gmaila** idzie przez konektor i działa niezależnie
od polityki sieci; opcjonalny SMTP (`scripts/send_email.py`) może wymagać szerszej polityki.

## Uruchomienie ręczne (test / nadrobienie dnia)

W dowolnej sesji w tym repo po prostu napisz:
```
/briefing
```
albo „dry-run" (przygotuj draft, ale nie zapisuj/commituj stanu):
```
/briefing dry-run
```

## Co, jeśli pominiemy dzień?

Nic złego — następny run i tak zaczyna od **rozliczenia wszystkich otwartych typów**
(krok 1 playbooka), więc pamięć się „dogoni". Możesz też odpalić `/briefing` ręcznie z datą.
