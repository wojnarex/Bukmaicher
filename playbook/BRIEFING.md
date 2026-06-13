# Bukmaicher — Playbook codziennego briefingu

To jest **procedura**, którą wykonujesz (Claude) przy każdym porannym uruchomieniu.
Trzymaj się kolejności kroków. Wszystkie ustawienia bierz z `config/config.yaml`,
a pamięć (historia, strategia, bankroll) żyje w katalogu `state/`.

Zasady naczelne:
- **Język:** pisz briefing po polsku (wg `delivery.language`).
- **Tylko rekomendacje.** Nie logujesz się nigdzie i nie wysyłasz typów za użytkownika — proponujesz, on wpisuje.
- **Uczciwość danych.** Wyraźnie oddzielaj TWARDE dane (kursy, wynik, potwierdzona kontuzja) od ESTYMACJI (twoje xG/prawdopodobieństwa). Przy estymacjach pisz „szac.".
- **Odpowiedzialna gra.** Respektuj limity z sekcji `responsible_gambling`. Nigdy nie zwiększaj stawek „na odrobienie straty".
- **Stan zawsze aktualizuj i commituj** na końcu (krok 9), żeby jutro był kontekst.

---

## Krok 0 — Przygotowanie i kontekst

1. Ustal „dziś" **turniejowe w strefie gospodarzy** `focus.schedule_timezone` (domyślnie America/New_York = ET) — bo MŚ 2026 grają w obu Amerykach. Mecze grupuj wg daty ET, NIE polskiej. Godziny w mailu podawaj i w ET, i w CEST. (Strefa `delivery.timezone` służy tylko do godziny wysyłki briefingu.)
2. Wczytaj konfigurację: `Read config/config.yaml`.
3. Wczytaj pamięć:
   - `state/strategy.md` — aktualna strategia i wnioski.
   - `python3 scripts/state_tool.py pending` — otwarte (nierozliczone) typy z poprzednich dni.
   - `python3 scripts/state_tool.py bankroll` — stan bankrolla i punktów.
4. Jeśli `kicktipp.league_url` lub `league_name` zawiera „TODO" — działaj dalej, ale w mailu dopisz wyraźną prośbę o uzupełnienie (sekcja „Konfiguracja do dograna").

---

## Krok 1 — Rozliczenie wczorajszych typów (najpierw patrzymy wstecz)

Dla każdego otwartego typu z `state_tool.py pending`, którego mecz już się odbył:
1. Web search o wynik końcowy meczu (twarda dana — podaj źródło).
2. Dla typów **kicktipp**: policz zdobyte punkty wg `kicktipp.scoring` (exact/goal_diff/tendency).
3. Dla zakładów **Fortuna**: ustal czy wygrany/przegrany/zwrot i policz P/L:
   - wygrana: `stake*(odds-1)`; przegrana: `-stake`; zwrot (void): `0`.
4. Zapisz rozliczenie:
   ```
   python3 scripts/state_tool.py settle --id <ID> --status <won|lost|void> \
       --result "<wynik>" [--points N] [--pnl KWOTA]
   ```
   (To automatycznie zaktualizuje bankroll i CSV.)
5. Zbierz wnioski: czy nasze prawdopodobieństwa były trafne? Gdzie był błąd (kontuzja, której nie wyłapaliśmy? przeszacowany faworyt?). Te wnioski wykorzystasz w kroku 8.

> Jeśli wczoraj nie było typów (np. pierwszy dzień) — pomiń, zaznacz w mailu „brak otwartych typów do rozliczenia".

---

## Krok 2 — Mecze w zakresie (UWAGA: strefa gospodarzy!)

„Dzień meczowy" definiuje strefa `focus.schedule_timezone` (ET), a NIE polski kalendarz.
Mecz z kick-offem np. 22:00 ET to wciąż „ten" dzień ET, choć w Polsce jest już po północy —
**MUSI** być uwzględniony. Nigdy nie odrzucaj meczu tylko dlatego, że po CEST wypada „jutro".

1. Wyznacz zakres dat **ET**: od dziś-ET do dziś-ET + `focus.lookahead_days` włącznie.
   Znajdź **wszystkie** mecze `focus.competition` w tym zakresie (web search po datach ET).
   Sprawdź pełną rozpiskę (różne grupy i strefy gospodarzy: ET/CT/MT/PT), żeby nie pominąć
   żadnego meczu — np. późnego spotkania w Toronto czy Los Angeles. Policz, ile meczów ma być,
   i upewnij się, że masz komplet.
2. Dla każdego meczu podaj: data ET, **godzina w ET oraz w CEST**, faza/grupa, stadion, znaczenie.
3. Zaznacz **deadline kicktippa** (= moment kick-offu) i które typy trzeba postawić już dziś
   (deadline w ~24–48h). Mecze z jutra (lookahead) zapowiadaj wyprzedzająco.
4. Jeśli `focus.favorite_teams` niepuste — wyróżnij mecze tych drużyn.

---

## Krok 3 — Newsy kadrowe i kontekst (per mecz)

Dla każdego meczu do typowania, web search (preferuj `research.preferred_news_sources`):
- Składy: **rozróżniaj POTWIERDZONY skład (oficjalny, ~1h przed KO) od PRZEWIDYWANEGO/„expected"**.
  Nigdy nie deklaruj, że ktoś „nie gra", wyłącznie na podstawie zapowiedzi/preview — to często projekcja, nie fakt.
  Status zawodnika oznaczaj: „potwierdzony / wątpliwy (szac.) / nieznany" + źródło i godzina.
  UWAGA: briefing leci rano, więc składy są jeszcze NIEpotwierdzone — pisz o nich jako prowizorycznych
  i wyraźnie przypomnij, by zweryfikować oficjalny XI przed deadline'em (zwłaszcza mecze wieczorne).
- Kluczowi zawodnicy (strzelcy, wykonawcy rzutów karnych/stałych fragmentów).
- Kontekst: motywacja (czy gra „o coś"), zmęczenie/rotacja, podróże, pogoda, wysokość n.p.m., nawierzchnia.
- Kara/bonus sytuacyjny (np. trener pod presją, debiut, powrót gwiazdy).
Zbierz zwięźle — 2–4 twarde fakty na mecz. Oznaczaj źródła datą (newsy szybko się dezaktualizują).

---

## Krok 4 — Statystyki: forma, xG, H2H, historia

Dla każdego meczu (preferuj `research.preferred_stats_sources`):
- Forma: ostatnie 5–8 spotkań, bramki strzelone/stracone, czyste konta.
- xG / xGA jeśli dostępne (często za paywallem → użyj przybliżeń i oznacz „szac.").
- H2H: bezpośrednie mecze, charakter (otwarte/zamknięte, liczba bramek).
- Kontekst turniejowy / historyczny (np. bilans w fazie grupowej MŚ, mecze otwarcia).
Skondensuj do tego, co zmienia ocenę (a nie ściana liczb).

---

## Krok 5 — Kursy rynkowe

Dla każdego meczu zbierz aktualne kursy (preferuj `research.preferred_odds_sources`, w tym `efortuna.pl`):
- 1X2 (1/X/2), Over/Under 2.5, BTTS; w razie potrzeby double chance / DNB / handicap.
- Zapisz źródło i przelicz kursy na **prawdopodobieństwa po usunięciu marży** (de-vig):
  - implied = 1/kurs; suma implied = overround; prob = implied / overround.
- To rynkowy „konsensus" — twój punkt odniesienia. Wartość (value) znajdujesz tam,
  gdzie TWOJE prawdopodobieństwo (z newsów + statów) istotnie odbiega od rynkowego.

---

## Krok 6 — Rekomendacje na kicktippa (dokładne wyniki)

Cel: **maksymalizować oczekiwane punkty** wg `kicktipp.scoring`, a nie zgadywać „ładny wynik".

Metoda (dla każdego meczu z deadlinem):
1. Z kursów oszacuj **oczekiwane bramki** drużyn (λ_dom, λ_goście). **KALIBRACJA (ważne!):**
   suma λ ≈ rynkowy total z linii O/U (po de-vig), a podział wg przewagi z 1X2 (faworyt = większa λ).
   Dopiero potem koryguj o newsy/staty (kroki 3–4). Bez tego model systematycznie zaniża bramki i typuje 1:0.
2. Zbuduj siatkę prawdopodobieństw wyników (Poisson po λ, 0:0…5:5).
3. Dla każdego kandydata policz **oczekiwane punkty** = Σ P(wynik) × punkty(typ, wynik),
   wagi **per typ wyniku** z `kicktipp.scoring`: osobno **wygrana** (tendency/goal_diff/exact)
   i **remis** (tendency/exact; remis bez tieru różnicy bramek). Turniej = symetria home/away.
4. Wybierz typ o **najwyższych oczekiwanych punktach** — niech zdecyduje policzone EV, NIE nawyk.
   Profil meczu rządzi typem (unikaj monotonnego 1:0):
   - mecz wyrównany → zwykle **1:1** (a „9-tka" premiuje remis: tendency 3 > 2, więc tym częściej);
   - umiarkowany faworyt + niski O/U → **1:0**;
   - mocny faworyt lub wysoki O/U → **2:1 / 2:0**; duża przewaga + dużo bramek → nawet 3:1.
5. Raportuj **top-2 typy + ich oczekiwane punkty** (widać margines decyzji) i zrób sanity-check newsami.
Zapisz każdy typ przez `state_tool.py add-pick` (type=kicktipp, market=exact_score).

---

## Krok 7 — Value bety u Fortuny (jeśli `fortuna.enabled`)

Dla każdego rynku z `fortuna.markets` w meczach dnia:
1. Porównaj TWOJE prawdopodobieństwo (z modelu/newsów) z kursem Fortuny po de-vig.
2. Policz **edge** = prob_twoje × kurs − 1 (czyli oczekiwany zwrot na 1 zł).
3. Rekomenduj zakład TYLKO gdy:
   - edge ≥ `fortuna.value_threshold`, oraz
   - kurs w `[min_odds, max_odds]`, oraz
   - nie przekraczasz `max_bets_per_day`.
4. Sizing stawki (ostrożny, ułamkowy Kelly dopasowany do `risk_profile`):
   - baza: `unit = bankroll × unit_pct`;
   - mnożnik wg edge (np. edge 5–8% → 0.5u, 8–12% → 1u, >12% → do `max_stake_units`),
   - przytnij do `max_stake_units`. Niżej dla `risk_profile: low`, wyżej dla `high`.
5. Respektuj `responsible_gambling`: jeśli miesięczna strata > `monthly_loss_limit_pct`
   bankrolla — **nie rekomenduj** nowych zakładów, napisz o tym w mailu.
6. Brak value? To jest OK i częste — napisz „dziś brak zakładów spełniających próg".
Zapisz każdy rekomendowany zakład przez `state_tool.py add-pick` (type=fortuna, z odds/stake/edge).

---

## Krok 8 — Aktualizacja strategii

1. Przejrzyj `state/strategy.md` + skuteczność z ostatnich dni (krok 1 + historia).
2. Zdecyduj: **kontynuować czy korygować?** Przykłady korekt:
   - systematycznie przeszacowujemy faworytów → tnij stawki na krótkich kursach;
   - kicktipp: za często typujemy 2:1, lepiej schodzić do 1:0 przy niskim O/U;
   - dany rynek (np. BTTS) słabo działa → wyłącz go czasowo.
3. Dopisz **nowy wpis z datą** na górze `state/strategy.md` (nie kasuj historii — wersjonujemy).
   Wpis: co zmieniamy, dlaczego, na podstawie jakich danych.

---

## Krok 9 — Briefing e-mail + zapis stanu

### 9a. Złóż maila (HTML, po polsku). Struktura:
- **Temat:** `⚽ Bukmaicher — briefing {DATA} ({liczba meczów} mecze, {liczba typów} typy)`
- **Nagłówek:** data, skrót dnia.
- **📊 Rozliczenie wczoraj:** typy + wynik + punkty/PL + krótki wniosek (lub „brak").
- **💰 Bankroll & forma:** stan bankrolla, suma punktów kicktipp, bilans Fortuna (np. ostatnie 7 dni).
- **🗓️ Mecze dnia:** lista z godzinami PL i kontekstem (1–2 zdania/mecz).
- **🎯 Typy na kicktippa:** tabela `Mecz | Typ | Uzasadnienie (1 zdanie) | szac. oczek. pkt`.
- **🔎 Value bety Fortuna:** tabela `Mecz | Rynek | Typ | Kurs | Stawka | Edge | Uzasadnienie` (lub „brak value dziś").
- **🧠 Strategia:** 2–3 zdania co kontynuujemy/zmieniamy i dlaczego.
- **⚙️ Konfiguracja do dograna:** tylko jeśli w configu są pola „TODO".
- **Stopka:** `responsible_gambling.footer`.

Trzymaj ton rzeczowy i zwięzły — to ma się czytać przy porannej kawie.

### 9b. Dostarcz wg `delivery.mode`:
- `github_action` (domyślnie — realny inbox): zapisz HTML maila do `outbox/briefing-latest.html`
  oraz temat (jedna linia) do `outbox/briefing-latest.subject`. Faktyczną wysyłką zajmie się
  GitHub Action (`.github/workflows/send-briefing.yml`) zaraz po pushu w kroku 9c.
  ⚠️ Bezpośredni SMTP z tego środowiska jest zablokowany — dlatego wysyła Action (patrz `docs/DELIVERY.md`).
  Opcjonalnie utwórz też draft w Gmailu (`mcp__Gmail__create_draft`) jako podgląd od ręki.
- `draft`: `mcp__Gmail__create_draft` na `delivery.recipient` (temat+htmlBody),
  potem nałóż etykietę `delivery.gmail_label` (utwórz etykietę, jeśli nie istnieje).

### 9c. Zapisz stan i zacommituj:
1. Upewnij się, że wszystkie dzisiejsze typy są w historii (`state_tool.py add-pick`).
2. `python3 scripts/state_tool.py rebuild-csv` (odśwież `state/history.csv` dla ew. importu do Arkuszy).
3. Dopisz krótki wpis do logu dnia (jedno-linijkowy) — patrz `state/strategy.md` sekcja „Dziennik" lub po prostu commit message.
4. Commit + push na bieżący branch:
   ```
   git add -A && git commit -m "briefing {DATA}: rozliczenie + typy + strategia" && git push -u origin <branch>
   ```

---

## Szybka ściąga metod liczbowych

- **de-vig (2 wyniki):** prob_A = (1/kursA) / (1/kursA + 1/kursB).
- **de-vig (1X2):** podziel każde 1/kurs przez sumę wszystkich 1/kurs.
- **fair odds:** 1 / prob.
- **edge (value):** prob_twoje × kurs − 1.
- **Poisson:** P(k goli) = e^(−λ) · λ^k / k!  → siatkę P(i:j)=P_dom(i)·P_gosc(j).
- **oczek. punkty kicktipp(typ):** Σ_{i,j} P(i:j) × punkty(typ vs i:j), wagi **per typ wyniku** (wygrana/remis) z `kicktipp.scoring`.
- **Kelly (ułamkowy):** f* = edge / (kurs − 1); stawka = bankroll × f* × frakcja_ryzyka (np. 0.25–0.5).
