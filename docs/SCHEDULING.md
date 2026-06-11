# Harmonogram — codzienne odpalanie briefingu

Silnik Bukmaichera to **zaplanowana sesja Claude Code on the web**, która każdego ranka
uruchamia komendę `/briefing` w tym repozytorium. Nie potrzebujesz własnego serwera ani crona.

## Jak ustawić poranny trigger

1. Wejdź na **claude.ai/code** (Claude Code on the web) i otwórz to repo (`wojnarex/Bukmaicher`).
2. Utwórz **zaplanowany trigger** (scheduled session) — w ustawieniach sesji/triggerów wybierz:
   - **harmonogram:** codziennie ok. **07:45** w strefie Europe/Warsaw.
     (Sesja najpierw *generuje* briefing i pushuje — to trwa kilka minut — a dopiero potem
     GitHub Action wysyła maila. Start o 07:45 sprawia, że wiadomość ląduje ~08:00.
     Jeśli nie przeszkadza Ci kilka minut po ósmej, ustaw po prostu 08:00.)
   - **branch:** ten, na którym pracujemy,
   - **prompt sesji:** dokładnie:
     ```
     Wykonaj /briefing
     ```
3. Zapisz. Od teraz codziennie rano sesja sama: rozliczy wczorajsze typy, zrobi research,
   zaproponuje typy, zaktualizuje strategię, utworzy briefing w Gmailu i wypchnie stan do gita.

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
