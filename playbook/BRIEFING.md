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

1. Ustal „dziś" w strefie `delivery.timezone` (data + dzień tygodnia).
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
3. Dla typów **STS**: ustal czy wygrany/przegrany/zwrot i policz P/L:
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

## Krok 2 — Mecze w zakresie

1. Znajdź mecze `focus.competition` na dziś oraz najbliższe `focus.lookahead_days` dni
   (web search: terminarz + godziny w strefie `delivery.timezone`).
2. Wypisz dla każdego: data, godzina (czas lokalny PL), faza/grupa, stadion, znaczenie.
3. Zaznacz, dla których jest **deadline kicktippa** w najbliższych ~24h (te są priorytetem do typowania dziś).
4. Jeśli `focus.favorite_teams` niepuste — wyróżnij mecze tych drużyn.

---

## Krok 3 — Newsy kadrowe i kontekst (per mecz)

Dla każdego meczu do typowania, web search (preferuj `research.preferred_news_sources`):
- Kontuzje, zawieszenia, wątpliwości w składach; przewidywane XI.
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

Dla każdego meczu zbierz aktualne kursy (preferuj `research.preferred_odds_sources`, w tym `sts.pl`):
- 1X2 (1/X/2), Over/Under 2.5, BTTS; w razie potrzeby double chance / DNB / handicap.
- Zapisz źródło i przelicz kursy na **prawdopodobieństwa po usunięciu marży** (de-vig):
  - implied = 1/kurs; suma implied = overround; prob = implied / overround.
- To rynkowy „konsensus" — twój punkt odniesienia. Wartość (value) znajdujesz tam,
  gdzie TWOJE prawdopodobieństwo (z newsów + statów) istotnie odbiega od rynkowego.

---

## Krok 6 — Rekomendacje na kicktippa (dokładne wyniki)

Cel: **maksymalizować oczekiwane punkty** wg `kicktipp.scoring`, a nie zgadywać „ładny wynik".

Metoda (dla każdego meczu z deadlinem):
1. Z kursów 1X2 + O/U 2.5 oszacuj **oczekiwane bramki** każdej drużyny
   (λ_dom, λ_goście). Skoryguj o newsy/staty z kroków 3–4.
2. Zbuduj siatkę prawdopodobieństw wyników (model Poissona po λ, wyniki 0:0…5:5).
3. Dla każdego kandydata na typ policz **oczekiwane punkty** =
   Σ P(wynik) × punkty(typ, wynik), używając wag **per typ wyniku** z `kicktipp.scoring`:
   - osobne wagi dla **wygranej** (`win.tendency/goal_diff/exact`) i **remisu** (`draw.tendency/exact`);
   - remis **nie ma** tieru różnicy bramek (różnica zawsze 0);
   - jeśli liga ma asymetrię home/away — przy turnieju na boiskach neutralnych traktuj ją symetrycznie.
4. Wybierz typ o **najwyższych oczekiwanych punktach**. Wskazówka dla reguły „9-tka":
   remis na tendencji bywa wyżej punktowany niż wygrana (3 vs 2), więc w meczach ~50/50
   **częściej opłaca się typować remis** niż przy symetrycznej punktacji.
5. Sanity-check zdrowym rozsądkiem i newsami; jeśli coś zgrzyta — opisz dlaczego.
Zapisz każdy typ przez `state_tool.py add-pick` (type=kicktipp, market=exact_score).

---

## Krok 7 — Value bety na STS (jeśli `sts.enabled`)

Dla każdego rynku z `sts.markets` w meczach dnia:
1. Porównaj TWOJE prawdopodobieństwo (z modelu/newsów) z kursem STS po de-vig.
2. Policz **edge** = prob_twoje × kurs − 1 (czyli oczekiwany zwrot na 1 zł).
3. Rekomenduj zakład TYLKO gdy:
   - edge ≥ `sts.value_threshold`, oraz
   - kurs w `[min_odds, max_odds]`, oraz
   - nie przekraczasz `max_bets_per_day`.
4. Sizing stawki (ostrożny, ułamkowy Kelly dopasowany do `risk_profile`):
   - baza: `unit = bankroll × unit_pct`;
   - mnożnik wg edge (np. edge 5–8% → 0.5u, 8–12% → 1u, >12% → do `max_stake_units`),
   - przytnij do `max_stake_units`. Niżej dla `risk_profile: low`, wyżej dla `high`.
5. Respektuj `responsible_gambling`: jeśli miesięczna strata > `monthly_loss_limit_pct`
   bankrolla — **nie rekomenduj** nowych zakładów, napisz o tym w mailu.
6. Brak value? To jest OK i częste — napisz „dziś brak zakładów spełniających próg".
Zapisz każdy rekomendowany zakład przez `state_tool.py add-pick` (type=sts, z odds/stake/edge).

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
- **💰 Bankroll & forma:** stan bankrolla, suma punktów kicktipp, bilans STS (np. ostatnie 7 dni).
- **🗓️ Mecze dnia:** lista z godzinami PL i kontekstem (1–2 zdania/mecz).
- **🎯 Typy na kicktippa:** tabela `Mecz | Typ | Uzasadnienie (1 zdanie) | szac. oczek. pkt`.
- **🔎 Value bety STS:** tabela `Mecz | Rynek | Typ | Kurs | Stawka | Edge | Uzasadnienie` (lub „brak value dziś").
- **🧠 Strategia:** 2–3 zdania co kontynuujemy/zmieniamy i dlaczego.
- **⚙️ Konfiguracja do dograna:** tylko jeśli w configu są pola „TODO".
- **Stopka:** `responsible_gambling.footer`.

Trzymaj ton rzeczowy i zwięzły — to ma się czytać przy porannej kawie.

### 9b. Dostarcz wg `delivery.mode`:
- `draft` (domyślnie): `mcp__Gmail__create_draft` na `delivery.recipient` (temat+htmlBody),
  potem nałóż etykietę `delivery.gmail_label` (utwórz etykietę, jeśli nie istnieje).
- `smtp`: uruchom `python3 scripts/send_email.py` (patrz `docs/DELIVERY.md`); jeśli brak
  sekretów/sieci — zrób fallback na `draft` i zaznacz to w logu.

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
