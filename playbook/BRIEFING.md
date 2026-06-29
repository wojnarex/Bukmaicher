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
   - `python3 scripts/state_tool.py pending --due` — otwarte typy, których mecz JUŻ się odbył (gotowe do rozliczenia).
   - `python3 scripts/state_tool.py bankroll` — stan bankrolla i punktów.
4. Jeśli `kicktipp.league_url` lub `league_name` zawiera „TODO" — działaj dalej, ale w mailu dopisz wyraźną prośbę o uzupełnienie (sekcja „Konfiguracja do dograna").
5. **CIĄGŁOŚĆ STANU (krytyczne):** na starcie zrób `git pull` najnowszego, STAŁEGO brancha pamięci,
   a na końcu (krok 9) commit+push na **TEN SAM** branch. Nie zostawiaj zmian na nowym, jednorazowym
   branchu per uruchomienie — inaczej pamięć się rozjeżdża i każdy run rozlicza wciąż 1. kolejkę.

---

## Krok 1 — Rozliczenie wczorajszych typów (najpierw patrzymy wstecz)

Pobierz listę gotowych: `python3 scripts/state_tool.py pending --due` (pokazuje TYLKO mecze już rozegrane,
match_date < dziś). Rozliczaj wyłącznie te. `settle` jest **idempotentne** — pominie typ już rozliczony
i nie ruszy meczu sprzed gwizdka, więc nie da się wpaść w pętlę „ciągle 1. kolejka". Dla każdego typu:
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

## Krok 2.5 — Stawka, scenariusze grupowe i drabinka (KLUCZOWE w 3. kolejce i pucharach)

W decydujących meczach MOTYWACJA i kalkulacja tabeli często biją jakość/kursy. Dla każdego meczu
USTAL, czego każda drużyna potrzebuje (tabela + scenariusze awansu, ranking 3. miejsc, bilans
bezpośredni) i sklasyfikuj mecz do archetypu — to wchodzi do λ_własne (Krok 6) i bywa DOMINUJĄCE:

- **A) Martwy mecz** (oba nic nie ugrają — awans/odpadnięcie/lokata przesądzone): rotacja, niska
  intensywność, wynik losowy. → obniż pewność, lekko Under, UNIKAJ odważnych wyników; kicktipp
  bezpiecznie (1:1/1:0); Fortuna **PAS** (nieprzewidywalne, rezerwy w składzie).
- **B) Remis pasuje OBU** (podział pkt awansuje/satysfakcjonuje obie): ryzyko zachowawczego,
  niskobramkowego remisu („pakt o nieagresji", echo Gijón '82). → mocny boost remisu + Under;
  kicktipp **1:1 / 0:0**; Fortuna Under + ew. remis (value).
- **C) Oba muszą wygrać / strzelać** (do-or-die): otwarcie, ofensywa, wyższy total, mniej remisu.
  → Over; typ na wygraną (lepsza / mniej potrzebująca goli drużyna), wynik z bramkami (2:1).
- **D) Asymetria** (jedna potrzebuje wyniku, druga bezpieczna): bezpieczna rotuje/gra na luzie →
  potrzebująca groźniejsza niż sugeruje jakość. Wariant: komuś **wystarczy niska porażka** →
  murowanie bramki, niski total (np. „Szkocja vs Brazylia"). → nudge ku potrzebującej / Under.
- **E) Różnica bramek / wyścig o 3. miejsce**: drużyna musi wygrać RÓŻNICĄ lub strzelić N goli →
  przeładowana ofensywa (Over), odsłony na kontry.

**Drabinka:** czasem niższa lokata = łatwiejszy rywal w pucharze → drużyna może NIE gonić wygranej.
Traktuj jako flagę niepewności (nie nadawaj wysokiej pewności typowi). Ostatnia kolejka grupy grana
jest RÓWNOLEGLE → drużyny reagują na wyniki z innych boisk (możliwe późne gole / wygaszenie).

Najpierw USTAL scenariusze (web search: tabele + „co daje awans"), DOPIERO potem typuj.

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
1. Zbuduj DWIE oceny oczekiwanych bramek (λ) i je połącz — NIE opieraj się wyłącznie na kursach:
   a) **λ_rynek** — z kursów (suma λ ≈ total z O/U po de-vig; podział wg przewagi z 1X2).
   b) **λ_własne** — NIEZALEŻNIE z czynników (kroki 3–4): forma/xG, kluczowe absencje, solidność
      defensywy rywala, **STAWKA/scenariusz tabeli (w 3. kolejce: archetyp z Kroku 2.5 — często
      dominujący!)**, zmęczenie/rotacja, wysokość/upał/podróż, matchup taktyczny (niski blok
      kompresuje λ faworyta), H2H. Stosuj orientacyjne korekty z sekcji `model` w configu.
   c) **λ_final = blend** wg `model.market_weight` (np. 0.55·λ_rynek + 0.45·λ_własne).
   GDZIE λ_własne istotnie odbiega od λ_rynek → to jest sygnał (typ kontra rynkowi + potencjalne value).
2. Zbuduj siatkę prawdopodobieństw wyników (Poisson po λ, 0:0…5:5).
2b. **KALIBRACJA REMISÓW (ważne!):** przemnóż komórki remisowe (i==j: 0:0, 1:1, 2:2…) przez
   `kicktipp.draw_bias` i renormalizuj całą siatkę do sumy 1. Powód: „9-tka" premiuje remis
   ORAZ faza grupowa MŚ 2026 jest mocno proremisowa (faworyci się potykają). To NIE psuje typów
   na wyraźne mismatche — tam remis ma małą masę i wygrana i tak wygrywa EV.
3. Dla każdego kandydata policz **oczekiwane punkty** = Σ P(wynik) × punkty(typ, wynik),
   wagi **per typ wyniku** z `kicktipp.scoring` (wygrana: tendency/goal_diff/exact; remis: tendency/exact).
4. Wybierz typ o **najwyższych oczekiwanych punktach** — decyduje EV + profil meczu (NIE nawyk
   „zawsze faworyt" ani „zawsze remis"). Realia MŚ 2026 są MIESZANE: dużo remisów faworytów
   (Kanada/Portugalia 1:1), ale i wysokobramkowe wygrane (Anglia 4:2). Kluczowa jest **siła ofensywna**
   faworyta, nie tylko %:
   - mecz wyrównany / brak wyraźnego faworyta → **1:1** (niski O/U → **0:0**);
   - umiarkowany faworyt cagey/defensywny lub na ogranego rywala → **1:1 / 1:0**;
   - umiarkowany faworyt z realnym ATAKIEM w formie (typ Anglia-Kane) → **1:0 / 2:1** (graj wygraną);
   - wyraźny faworyt → **2:1 / 2:0**; mismatch / ofensywny faworyt (Norwegia-Haaland) → **2:0 / 3:0**.
   - **Mismatch amplifikacja** (potw. wynikami): przy wyraźnym faworycie Poisson ZANIŻA wygraną
     (Kanada 6:0, Hiszpania 4:0, Holandia 5:1) → przy λ_rywala <0.6 rozważ +1 gol. ALE sprawdź
     **bramkarza-bohatera** rywala i ryzyko czerwonej — potrafią zepsuć mismatch (Iran 0:0, Curaçao 0:0).
5. Raportuj **top-2 typy + oczekiwane punkty** ORAZ **czynniki, które przeważyły** (forma / absencje /
   taktyka / motywacja — nie sam kurs) i ewentualny rozjazd z rynkiem. Sanity-check newsami.
Zapisz każdy typ przez `state_tool.py add-pick` (type=kicktipp, market=exact_score).

### 6P — TRYB PUCHAROWY (R32 i dalej) — inne zasady!

Liga liczy wynik **PO dogrywce I karnych** (wszystkie bramki z dogrywki + karne doliczone):
np. 2:2 po dogrywce, 5:4 w karnych → zapisany wynik **7:6**. To zmienia typowanie:
1. **NIE MA REMISÓW** — każdy mecz ma zwycięzcę (karne rozstrzygają). **Wyłącz `draw_bias`, NIGDY nie typuj 1:1/0:0** (są niemożliwe jako wynik końcowy).
2. **Najpierw TENDENCJA** — typuj drużynę, która Twoim zdaniem AWANSUJE (jakość, forma, kontuzje, nerwy 1. meczu KO). Archetypy grupowe A–E **znikają** (nie ma już kalkulacji tabeli).
3. **Margines: domyślnie +1** dla awansera → **2:1** (lub **1:0** gdy niskobramkowo). Powód: +1 łapie i wąską wygraną w regulaminowym, i typową wygraną w karnych (5:4, 4:3, nagła śmierć = zawsze +1). Dokładnego, napompowanego wyniku po karnych (7:6) i tak się nie trafi — celuj w **tendencję + różnicę**, nie w exact.
4. **Wyraźny faworyt mogący rozstrzygnąć w 90 min** → większy margines **2:0 / 3:1** (szansa na exact w regulaminowym).
5. **Mecz ~50/50 (prawdopodobne karne)** → tym mocniej **+1** dla wytypowanego awansera (margines +1 to modalny margines i rozstrzygnięć, i karnych).
Fortuna w pucharach: graj rynki „awans / to qualify" albo wynik **po 90 min** (tam remis 1X2 nadal istnieje) — czytaj, czego dotyczy kurs.

---

### 6C — TRYB POŚCIGU (contest leverage) — gdy grasz o MIEJSCE, nie o sumę punktów

Cel ligi = `kicktipp.objective` (np. top3). Jeśli kopiujesz pole, zostajesz w środku stawki.
Wczytaj tabelę typerów: pozycja, luka do celu, ile meczów/rund zostało, oraz **typy rywali** (kicktipp je pokazuje).

- **GONISZ cel (trailing):** RÓŻNICUJ SIĘ od pola — ale SELEKTYWNIE:
  - mecz ~50/50, na którym **pole jest na faworycie** → weź **UPSET** (maks. dźwignia: trafienie = przeskakujesz całe pole; pudło = tracisz tyle, co oni typowo);
  - **mismatch** (faworyt prawie pewny) → NIE fade'uj, ale wybierz **inny, wciąż prawdopodobny wynik** niż tłumowy (np. 2:0 zamiast 2:1) → wygrywasz na exact/diff, gdy pole bierze inny margines;
  - skaluj odwagę do luki i liczby meczów (większa luka / mniej meczów → odważniej);
  - NIE rób blanket-kontry (fade wszystkiego tonie EV) — wybierz **1–2 najlepsze spoty dźwigni** na rundę.
- **PROWADZISZ / chronisz miejsce:** odwrotnie — **kopiuj konsensus** (minimalizuj wariancję, „blokuj" goniących).

Świadomy trade-off: oddajesz trochę EV za wariancję — uzasadniony TYLKO, gdy walczysz o pozycję, nie o punkty.

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
4. Commit + push na **STAŁY branch pamięci** (ten sam, z którego czytałeś stan w kroku 0 —
   NIE twórz nowego brancha per run, bo pamięć się rozjedzie):
   ```
   git add -A && git commit -m "briefing {DATA}: rozliczenie + typy + strategia" && git push origin <stały-branch>
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
