# Pamięć i Arkusze Google

## Dlaczego pamięć jest w gicie, a nie w Arkuszach?

Bot kolegi zapisywał historię w Google Sheets. U nas konektor **Google Drive** potrafi
**tworzyć i czytać** pliki, ale **nie ma operacji „dopisz wiersz / zaktualizuj komórkę"**
w istniejącym Arkuszu. Codzienne dopisywanie wierszy przez konektor jest więc zawodne.

Dlatego źródłem prawdy jest **pamięć wersjonowana w gicie** (`state/`):
- `history.jsonl` — pełny log typów z cyklem życia (pending → won/lost/void),
- `bankroll.json` — bankroll + suma punktów kicktipp,
- `strategy.md` — wersjonowana strategia (widać historię decyzji),
- `history.csv` — spłaszczony widok (odświeżany przez `state_tool.py rebuild-csv`).

To dla agenta jest wręcz lepsze niż Arkusze: pełna historia zmian (git log), diffy,
brak limitów API, łatwy rollback.

## Chcę i tak widzieć to w Arkuszu Google

Najprościej — **import CSV**:
1. Otwórz `state/history.csv` w repo (albo pobierz z GitHuba).
2. W Arkuszach Google: *Plik → Importuj → Prześlij* i wskaż CSV (albo wklej zawartość).
3. Powtórz, gdy chcesz odświeżyć (CSV jest aktualizowany przy każdym briefingu).

Możemy też w briefingu **tworzyć nowy Arkusz** kopią danych (konektor to potrafi),
ale skończyłoby się to mnożeniem plików — dlatego domyślnie tego nie robimy.

## Prawdziwa, automatyczna synchronizacja z Arkuszami (opcja na później)

Jeśli zależy Ci na żywym Arkuszu aktualizowanym automatycznie, są dwie drogi:
- **Konto serwisowe Google Sheets API** + mały skrypt `append`/`batchUpdate`
  (wymaga klucza JSON jako sekret — jednorazowy setup).
- **MCP z zapisem do Sheets**, gdyby taki konektor pojawił się w środowisku.

Daj znać, a dołożę `scripts/sheets_sync.py` i przełącznik w `config`.
