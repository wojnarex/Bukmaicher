# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dnia — dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

---

## 2026-07-20 — v1.41 (ROZLICZENIE FINAŁU + ZAMKNIĘCIE SEZONU MŚ 2026: Hiszpania 1:0 Argentyna po dogrywce — typ 1:0 trafiony DOKŁADNIE, 4/4 pkt max; koniec turnieju, brak meczów; podsumowanie całego cyklu MŚ2026)

**Rozliczenie 19.07 — FINAŁ Hiszpania–Argentyna:** wynik **Hiszpania 1 : 0 Argentyna (po dogrywce)** — gol Ferran Torres w 106. minucie, Enzo Fernández czerwona kartka w doliczonym czasie 90 min (Argentyna dogrywkę grała w 10), Messi kompletnie zablokowany przez defensywę Hiszpanii — 0 celnych strzałów Argentyny w całym meczu (120 min). Nasz zapisany typ **1:0** = **TRAFIONY DOKŁADNIE (exact score), +4 pkt** — maksymalny wynik dostępny w skali "9-tki" dla tego typu wyniku (win: exact=4). Model (zbieżność 3 niezależnych źródeł ~58%/42%, najlepsza defensywa turnieju Hiszpanii, zmęczenie Argentyny po dwóch dogrywkach wcześniej w turnieju) trafił i kierunek, i dokładny margines — potwierdza słuszność zasady 31 (ufaj zbieżności niezależnych źródeł) i zasady 29 (elitarna defensywa > forma ofensywna rywala) zastosowanych łącznie na tym meczu.

**Nagrody indywidualne turnieju (twarda dana, FIFA/Opta):** Złoty But — Kylian Mbappé (Francja, 10 goli, pierwszy dwukrotny zdobywca w historii); Złota Piłka (najlepszy zawodnik) — Rodri (Hiszpania); Srebrna Piłka — Leo Messi (Argentyna); Brązowa Piłka — Mbappé; Złota Rękawica — Unai Simón (Hiszpania); najlepszy młody zawodnik — Pau Cubarsí (Hiszpania). Hiszpania zdobywa 2. tytuł mistrzowski w historii (pierwszy od 2010).

**Bilans końcowy MŚ 2026 (CAŁY CYKL, 79 typów kicktipp):** **127 pkt kicktipp** (36 trafień pełnych/partial + korzyści z tendencji na chybionych typach, 40 kompletnie chybionych). Fortuna: **14 rozliczonych zakładów** (5 wygranych, 8 przegranych, 1 zwrot) — **bilans -44,43 PLN (ROI -4,4%)** na starcie 1000 PLN, bankroll końcowy **955,57 PLN**. Fortuna spędziła większość drugiej połowy turnieju (od ok. 16.07) bez żadnego zakładu — rygorystyczne trzymanie progu `value_threshold=5%` skutecznie odcięło słabe spoty, ale też oznacza, że nie zrealizowaliśmy edge'u tam, gdzie mogliśmy go source'ować z ograniczonym dostępem do `efortuna.pl` (403 przez cały turniej, korzystaliśmy z konsensusu US ksiąg/Kalshi jako namiastki).

**KLUCZOWE WNIOSKI Z CAŁEGO CYKLU (do wykorzystania w następnym turnieju/lidze):**
1. **Zbieżność niezależnych źródeł prawdopodobieństwa = wysoka wiarygodność** (zasada 31) — sprawdziła się na finale. Gdy rynek trofeum, rynek predykcyjny (Kalshi) i własny rozkład 90-min+remis dają niemal identyczny wynik, nie szukaj kontrariańskiego sygnału — inwestuj wysiłek analityczny w MARGINES, nie w kierunek.
2. **Elitarna defensywa > pojedynczy dobry napastnik** (zasada 29) — dwukrotnie potwierdzone w tym turnieju (Francja-Hiszpania PF, finał). Waż twarde staty defensywne rywala (gole stracone/mecz, czyste konta) NIE MNIEJ niż newsy o formie/zdrowiu gwiazdy ofensywnej.
3. **Mecze dead-rubber (bez stawki tabelowej, np. o 3. miejsce) mają EKSTREMALNĄ wariancję kierunku, nie tylko marginesu** (zasada 32, boleśnie potwierdzona: Anglia 6:4 Francja mimo typu na Francję 2:1) — przy silnym sygnale Over w meczu bez stawki, rozważ spłaszczenie przewagi tendencji zamiast podbijania marginesu.
4. **Gwiazda może rozstrzygnąć mecz samą kreacją (asysty), nie tylko golami** (zasada 30, Messi vs Anglia) — waż xA/kluczowe podania na równi z golami przy ocenie wpływu zawodnika w końcówce meczu.
5. **Fortuna: rygorystyczny próg edge ≥5% jest słuszny, ale ograniczony dostęp do `efortuna.pl` (403 przez CAŁY turniej) ograniczał jakość porównania** — na przyszłość warto rozważyć alternatywne, stabilniejsze źródło polskich kursów (STS/betfan mają być prościej dostępne wg wcześniejszych wpisów) zamiast wyłącznie US ksiąg jako namiastki.
6. **Ogólny bilans kicktipp (127 pkt / 79 typów) i Fortuna (-4,4% ROI)** pokazują, że model dobrze łapie TENDENCJĘ w większości meczów pucharowych (dużo częściowych trafień na "won" z niepełnym marginesem), ale MARGINES (exact score) pozostaje trudny do trafienia konsekwentnie — dead-rubbery i mecze z dogrywką/karnymi to główne źródło całkowitych pudeł.

**KONIEC SEZONU MŚ 2026.** Turniej zakończony 19.07 (finał). Świeży research (20.07) potwierdza: brak jakichkolwiek meczów MŚ 2026 zaplanowanych po finale — to definitywnie ostatni mecz turnieju. Brak też naturalnej kontynuacji w kicktippie w najbliższym czasie: MLS wraca 22.07, ale główne europejskie ligi (Premier League, Bundesliga) startują dopiero 21-22 sierpnia, Liga Mistrzów (kwalifikacje/faza ligowa) jeszcze później (wrzesień) — więc w kolejnych briefingach, dopóki `config/config.yaml.focus.competition` nie zostanie zaktualizowany na nowe rozgrywki, **brak meczów do typowania i rozliczania**. Kolejny briefing powinien to sprawdzić i, jeśli konfiguracja nadal wskazuje MŚ 2026, jasno zakomunikować w mailu, że sezon jest zamknięty i czeka na aktualizację `config.yaml` (nowa liga/turniej) zanim silnik znów zacznie typować. Zasady 1-32 pozostają w mocy jako baza wiedzy do wykorzystania przy następnym turnieju/lidze.

---

## 2026-07-19 — v1.40 (Rozliczenie: Francja-Anglia CAŁKOWICIE CHYBIONE — Anglia wygrała 6:4 (mecz o 3. miejsce), nie Francja 2:1 jak typowaliśmy; 10-golowy thriller potwierdza sygnał Over, ale odwrócił tendencję; dziś FINAŁ Hiszpania-Argentyna, typ 1:0 bez zmian po świeżym researchu — Yamal potwierdzony gotowy, rynek stabilny ~58%/42%, brak nowego value)

**Rozliczenie 18.07 — Francja–Anglia (mecz o 3. miejsce):** wynik **Francja 4 : Anglia 6** (ESPN/Fox Sports/101greatgoals potwierdzone, "10-goal thriller" — Kane, Bellingham, Saka hat-trick i Gordon dla Anglii; Mbappé, Dembélé, Barcola i jeszcze jeden gol dla Francji, Mbappé umocnił się na szczycie klasyfikacji strzelców turnieju mimo porażki drużyny). Nasz zapisany typ **selection "2:1" pod `match="France vs England"`** = Francja 2 : Anglia 1. Rzeczywisty wynik: **CAŁKOWICIE CHYBIONA TENDENCJA I WYNIK (0 pkt)** — Anglia wygrała, nie Francja, a mecz był przy tym wyjątkowo bramkowy (10 goli łącznie), znacznie powyżej nawet naszej podniesionej estymacji Over.

**Nowa zasada 32 — mecz o 3. miejsce z silnym sygnałem Over (dead-rubber + osłabione defensywy + indywidualna motywacja obu stron, np. wyścig o Złoty But) niesie EKSTREMALNĄ wariancję KIERUNKU wyniku, nie tylko marginesu:** Sygnał Over 2.5 (68-70% de-vig) i historyczna baza (16/20 ostatnich meczów o 3. miejsce Over 2.5) trafiły — mecz faktycznie był bramkowy (10 goli). Ale wysoka bramkowość w dead-rubber, gdzie obie defensywy grają rotacjami/luźno, oznacza że KAŻDA drużyna może strzelić dużo, więc umiarkowana przewaga tendencji faworyta (tu: Francja ~50% w 90 min) staje się mniej wiarygodna niż w meczu o stawkę — otwarty, chaotyczny mecz łatwiej odwraca się w dowolną stronę w ostatnich minutach. Wniosek na przyszłość (kolejne turnieje): przy silnym sygnale Over w meczu bez stawki tabelowej, rozważ SPŁASZCZENIE przewagi tendencji (bliżej 50/50 nawet przy umiarkowanym faworycie rynkowym) zamiast automatycznego podnoszenia marginesu (2:1/3:1) — wysoka bramkowość koreluje z nieprzewidywalnością kierunku, nie tylko z większą różnicą bramek zwycięzcy.

**Bilans:** kicktipp 123 pkt (bez zmian, 0 z rozliczenia). Bankroll 955,57 PLN (ROI -4,4%, bez zmian — brak zakładu). Jednostka 1u = 19,11 PLN. Fortuna: kolejny dzień z rzędu bez zakładu (13 rozliczonych łącznie, bez zmian od 16.07).

**Dziś (19.07) — FINAŁ Hiszpania–Argentyna** (15:00 ET/21:00 CEST, East Rutherford NJ, MetLife Stadium): typ **1:0 bez zmian**. Świeży research rano potwierdza stabilność oceny sprzed 1-2 dni, bez istotnych zmian: **Yamal (Hiszpania) potwierdzony w „optymalnym stanie"** przez trenera de la Fuente — trenował osobno w piątek z zabezpieczonym udem (ostrożność/zarządzanie obciążeniem, nie nowa kontuzja), dołączył do drużyny w sobotę, oczekiwany w wyjściowej 11. **Messi i Argentyna bez nowych kontuzji/zawieszeń** — Romero (skurcze po ćwierćfinale) rozegrał pełne 90 min w półfinale z Anglią i jest gotowy. Rynek 90-min świeży (FanDuel +125/+200/+260) de-vig: Hiszpania ~42,1%/remis ~31,6%/Argentyna ~26,3% — niemal identyczne z wczorajszym (~41-42%/32%/26-27%), brak przesunięcia. Do podniesienia pucharu: Hiszpania -150/Argentyna +130 (Kalshi 58%/42%) → de-vig ~58,0%/42,0% — zbieżne z wczoraj i z niezależnym rynkiem predykcyjnym, wysoka spójność utrzymana. O/U2.5 (FanDuel +138/-170, ~60% de-vig Under) i BTTS (-116/-110, ~51,4%/48,6% de-vig) bez zmian względem wczoraj — oba rynki nadal blisko naszej własnej estymacji (λ_ESP szac. ~1,35, λ_ARG szac. ~0,93), brak dodatkowego edge. **1:0 pozostaje najlepszym EV, alternatywa 2:1.**

**Fortuna dziś:** BRAK zakładu — rynek zwycięstwa (58%/42%), O/U2.5 (~60% Under) i BTTS (~51%/49%) wszystkie stabilne i zbieżne z naszą oceną od kilku dni, zero rozjazdu ≥5% wymaganego progu. `efortuna.pl` nadal niedostępne dla WebFetch (403, potwierdzone dziś ponownie) — konsensus FanDuel/DraftKings/Kalshi jako namiastka, jak w poprzednich dniach. Zgodnie z zasadą 32 — mimo że wczorajszy mecz o 3. miejsce eksplodował bramkowo wbrew naszej tendencji, dzisiejszy finał ma ODMIENNY profil (mecz O STAWKĘ, nie dead-rubber, obie strony grają pełnym składem o wynik) — zasada 32 nie ma tu zastosowania, nie spłaszczamy typu.

**Kontynuujemy:** Zasady 1-32 w mocy (nowa zasada 32 dot. wariancji kierunku w meczach dead-rubber z silnym sygnałem Over — do zastosowania w PRZYSZŁYCH turniejach, nie zmienia dzisiejszego typu na finał). Tryb pucharowy aktywny (draw_bias wyłączony) na dzisiejszy finał — ostatni mecz turnieju. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403, potwierdzone ponownie dziś) — ostatnia znana pozycja z 29.06 (5. miejsce), traktuj jako nieaktualną. To OSTATNI briefing z aktywnym typowaniem w tym cyklu — po dzisiejszym finale turniej się kończy; **kolejny briefing (20.07) rozliczy finał i zamknie sezon MŚ 2026** (podsumowanie całego cyklu: bilans kicktipp + Fortuna, kluczowe wnioski/zasady do wykorzystania w następnym turnieju/lidze).

---

## 2026-07-18 — v1.39 (Rozliczenie: brak — `pending --due` puste, mecz o 3. miejsce gra się dopiero DZIŚ wieczorem, ET-dzień jeszcze trwa; oba typy [Francja-Anglia 2:1, Hiszpania-Argentyna 1:0] BEZ ZMIAN po świeżym researchu — sygnał Over/BTTS na 3. miejsce jeszcze mocniejszy, Yamal potwierdzony w pełni zdrowy na finał)

**Rozliczenie:** brak — `python3 scripts/state_tool.py pending --due` pusty. Francja-Anglia (mecz o 3. miejsce) gra się dziś dopiero o 17:00 ET/23:00 CEST, a briefing leci rano — mecz jeszcze nierozegrany w momencie rozliczenia.

**Bilans:** bez zmian — 123 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN. Fortuna: kolejny dzień bez zakładu (13 rozliczonych zakładów łącznie, bez zmian od 16.07).

**Dziś (18.07) — mecz o 3. miejsce Francja–Anglia** (17:00 ET/23:00 CEST, Miami Gardens, Hard Rock Stadium): typ **2:1 bez zmian**. Świeży research potwierdza i WZMACNIA wczorajszą ocenę: **Saliba (Francja) potwierdzony OUT** (uraz pleców z półfinału) — najbardziej prawdopodobny zastępca to **Maxence Lacroix** obok Upamecano (wybrany nad Konaté ze względu na doświadczenie po lewej stronie pary stoperów, choć część źródeł nadal wskazuje Konaté jako alternatywę) — **PROWIZORYCZNE** do potwierdzenia tuż przed kick-offem. Sygnał Over/BTTS jeszcze mocniejszy niż wczoraj: Over 2.5 teraz -250/+198 (FanDuel, ~68% de-vig, wczoraj ~63-64%), BTTS Tak -290/+210 (~70% de-vig, wczoraj ~64-69%) — rynek systematycznie podbija bramkowość tego meczu w miarę zbliżania się kick-offu, spójne z naszą już wcześniej podniesioną estymacją. Dodatkowy twardy fakt z dzisiejszego researchu: 16 z ostatnich 20 meczów o 3. miejsce na MŚ skończyło się Over 2.5, a BTTS w 14 z 20 — silne historyczne wsparcie dla profilu tego konkretnego typu meczu (dead-rubber + osłabione defensywy), nie tylko bieżącego składu. Rynek 90-min (FanDuel -110/+280/+280) de-vig: Francja ~50%/remis ~25%/Anglia ~25%; do awansu (tie-win z ET+karnymi) Francja ~60-63% (Kalshi 51%/26%/25%, Polymarket 63%/37%) — spójne z wcześniejszą oceną (~59-61%), umiarkowany, nie miażdżący faworyt. Mbappé i Kane potwierdzeni zdrowi, obaj wciąż z osobistym interesem bramkowym (Złoty But, ostatni mecz Deschampsa). **2:1 pozostaje najlepszym EV, alternatywa 3:1.**

**Lookahead (19.07) — FINAŁ Hiszpania–Argentyna** (15:00 ET/21:00 CEST, East Rutherford NJ, MetLife Stadium): typ **1:0 bez zmian**. Świeży research **usuwa wczorajszą drobną wątpliwość o Yamalu** — dzisiejsze źródła (Forbes, FanDuel Research) potwierdzają: „Spain has no injuries to report for the final", Yamal „has returned to full fitness" — trening oddzielny z 17.07 to było rutynowe zarządzanie obciążeniem, jak zakładaliśmy (szac.), teraz POTWIERDZONE jako brak zagrożenia. Rynek 90-min świeży (FanDuel +125/+200/+260) de-vig: Hiszpania ~42%/remis ~26%/Argentyna ~21% (nieco silniejsza przewaga Hiszpanii niż wczorajsze ~41%/32%/27% z innego bukmachera — różnica głównie w wycenie remisu, kierunek ten sam) — do zwycięstwa w turnieju Kalshi nadal 58%/42%, identycznie jak wczoraj. O/U2.5 (FanDuel +138/-170, ~60% de-vig Under) i BTTS (~51%/49%) bez zmian względem wczoraj — oba rynki nadal blisko naszej własnej estymacji, brak dodatkowego edge. Argentyna: 12 goli strzelonych i 5 straconych w ostatnich 5 meczach (najbardziej produktywny atak turnieju wg dzisiejszego researchu) — mocna ofensywa, ale wciąż przegrywa bilans defensywny z Hiszpanią (1 stracony gol w 7 meczach, rekordowe 6 czystych kont Unaia Simóna). **1:0 pozostaje najlepszym EV, alternatywa 2:1.**

**Fortuna dziś:** BRAK zakładów na oba mecze. Francja-Anglia: mimo jeszcze mocniejszego sygnału Over/BTTS (68-70% de-vig) nasza własna estymacja (~64% Over) pozostaje NIŻEJ niż rynek — rynek wyprzedza nas w wycenie tego sygnału, więc brak edge (ujemny rozjazd, nie dodatni). Hiszpania-Argentyna: rynek zwycięstwa (58%/42%) bez zmian od wczoraj, O/U i BTTS też stabilne — zero rozjazdu ≥5%. `efortuna.pl` nadal niedostępne dla WebFetch (403, potwierdzone dziś ponownie) — korzystamy z konsensusu US ksiąg (FanDuel/DraftKings) i rynków predykcyjnych (Kalshi/Polymarket) jako namiastki.

**Kontynuujemy:** Zasady 1-31 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju — oba pozostałe mecze (dziś mecz o 3. miejsce, jutro finał) rozstrzygane ET+karnymi przy remisie. To PRZEDOSTATNI briefing sezonu — po jutrzejszym finale (19.07) turniej się kończy, kolejny briefing rozliczy finał i będzie ostatnim tego cyklu. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403, potwierdzone ponownie dziś) — ostatnia znana pozycja z 29.06 (5. miejsce), traktuj jako nieaktualną. Pościg top3: oba typy dziś pod max EV z profilem meczu, bez zmian względem wczoraj — świeży research jedynie WZMACNIA istniejące uzasadnienia (mocniejszy Over-sygnał na 3. miejsce, usunięta wątpliwość o Yamalu na finał), nie zmienia kierunku ani marginesu żadnego typu.

---

## 2026-07-17 — v1.38 (Rozliczenie: brak — `pending --due` puste, oba otwarte typy jeszcze nierozegrane; dziś dzień przerwy bez meczów [potwierdzone]; typ na Francja-Anglia 18.07 bez zmian, ale Saliba POTWIERDZONY OUT wzmacnia sygnał Over/BTTS; NOWY typ na FINAŁ Hiszpania-Argentyna 19.07 — 1:0, wchodzi dziś w okno lookahead po raz pierwszy)

**Rozliczenie:** brak — `python3 scripts/state_tool.py pending --due` pusty. Jedyny otwarty typ sprzed dziś (Francja-Anglia, 18.07) jeszcze się nie odbył.

**Bilans:** bez zmian — 123 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN. Fortuna: kolejny dzień bez zakładu (13 rozliczonych zakładów łącznie, bez zmian od 16.07).

**Dziś (17.07) — dzień przerwy, BEZ MECZÓW** (potwierdzone świeżym researchem: Wikipedia/Yahoo Sports/World Soccer Talk — jedyne mecze w oknie 17-19.07 ET to mecz o 3. miejsce (18.07) i finał (19.07), brak innych spotkań). **Korekta lokalizacji:** mecz o 3. miejsce gra się na Hard Rock Stadium w Miami Gardens (NIE na MetLife) — MetLife zarezerwowany wyłącznie na finał. Okno lookahead (17-19.07 ET, +2 dni) obejmuje oba pozostałe mecze turnieju:

- **Francja–Anglia (18.07, 17:00 ET/23:00 CEST, Miami, Hard Rock Stadium) — typ 2:1 bez zmian z 16.07.** Świeża, ISTOTNA informacja: **William Saliba (Francja, środkowy obrońca) POTWIERDZONY OUT** — zszedł we łzach w półfinale z Hiszpanią (14.07) z urazem pleców, który się "pogorszył"; rozważana operacja (4-5 mies. przerwy, nie potwierdzona ostatecznie), ale nieobecność na mecz o 3. miejsce jest twardym faktem. Konaté ma zastąpić go u boku Upamecano — nowa, nieobkatana para środkowych obrońców Francji. To WZMACNIA (nie zmienia kierunku) już wcześniej zidentyfikowany silny sygnał Over/BTTS: rynek Over 2.5 jeszcze mocniejszy niż 16.07 (FanDuel -250, ~63% de-vig, wcześniej -180/~64% — spójne), BTTS Tak też wyraźnie faworyzowany (FanDuel -290, bet365 4/9, ~64-69% de-vig) — konsystentne z naszą własną estymacją Over (λ_total szac. ~3,25-3,3 -> P(Over2.5) ok. 64%, niemal identyczne z rynkiem, WIĘC brak dodatkowego edge Fortuny ponad rynek). Dodatkowy kontekst: to OSTATNI mecz Deschampsa jako selekcjonera Francji (14 lat kadencji) — może zwiększać motywację do "godnego pożegnania" lub odwrotnie, sprzyjać większym rotacjom; Tuchel otwarcie przyznał, że "żaden z zawodników nie chce grać tego meczu" (dead-rubber) — obaj trenerzy prawdopodobnie rotują. Kane i Mbappé POTWIERDZENI zdrowi, obaj z osobistym interesem (wyścig o Złoty But, Mbappé remisuje z Messim na 8 goli i gra swój ostatni mecz turnieju). Rynek 90-min (DraftKings +105/+255/+255, FanDuel -110/+280/+280) de-vig: Francja ~46-50%/remis ~25-28%/Anglia ~25-28% — spójne z 16.07. Tryb pucharowy (ET+karne przy remisie): po doliczeniu połowy remisu do obu stron, Francja tie-win ok. 59-61% (umiarkowany faworyt, nie blowout) — margines +1 zgodnie z 6P pkt.3, wzmocniony sygnałem Over: **2:1 pozostaje najlepszym EV**, alternatywa **3:1** (jeśli osłabiona defensywa Francji po stracie Saliby przełoży się na więcej straconych bramek, wciąż z przewagą tendencji Francji).
- **NOWY: Hiszpania–Argentyna (19.07, 15:00 ET/21:00 CEST, East Rutherford NJ, MetLife Stadium) — FINAŁ: typ 1:0 (Hiszpania wygrywa wąsko).** Trzy NIEZALEŻNE źródła prawdopodobieństwa zwycięstwa w meczu (z ET/karnymi) zbieżne co do grosza: rynek "kto podniesie puchar" (BetMGM/FanDuel Hiszpania -160/Argentyna +125, STS 1,65/2,25) de-vig ~58%/42%; Kalshi (rynek predykcyjny) 58,1%/42,7%; własna kalkulacja z rozkładu 90-min 1X2 (FanDuel Hiszpania +130/remis +195/Argentyna +255 -> de-vig 41,2%/32,1%/26,7%) + doliczenie połowy remisu do zwycięzcy -> Hiszpania ok. 57,3%/Argentyna ok. 42,8%. Ta zbieżność trzech niepowiązanych metod daje wysoką pewność co do umiarkowanej (nie miażdżącej) przewagi Hiszpanii. TWARDA DANA kluczowa dla marginesu: Hiszpania straciła w całym turnieju tylko 1 gola (Belgia w ćwierćfinale) — najlepsza defensywa MŚ, potwierdzone czyste konto w półfinale z Francją (2:0). Argentyna kontrastowo traciła gola w KAŻDYM z ostatnich 5 meczów (twarda dana) i rozegrała o 60 minut więcej w dogrywkach (Egipt 3:2 AET w 1/8, Szwajcaria 3:1 AET w ćwierćfinale) niż Hiszpania (wszystkie mecze rozstrzygnięte w czasie regulaminowym) — realny czynnik zmęczenia na niekorzyść Argentyny przed finałem. Kadrowo: BRAK zawieszonych po obu stronach (potwierdzone). Messi potwierdzony zdrowy mimo otarcia oka z ćwierćfinału. Yamal (Hiszpania) zdrowy, ale z przewlekłym urazem uda sprzed turnieju — trenował dziś oddzielnie z Porro przed finałem, co traktujemy jako szac. rutynowe zarządzanie obciążeniem (NIE potwierdzona wątpliwość, źródła nie podają go jako zagrożonego). Rynek O/U2.5 wyraźnie Under (FanDuel -170/+138, BetMGM -150/+135, ~60% de-vig) — spójne z profilem defensywnym Hiszpanii, nasza własna estymacja (λ_total szac. ~2,3) daje niemal identyczny wynik (~60% Under), więc brak dodatkowego edge Fortuny. BTTS blisko pół na pół (FanDuel -116/-110, ~51%/49% de-vig) — brak jednoznacznego sygnału. H2H: tylko 1 mecz na MŚ w historii (1966, Argentyna 2:1), pierwsze pucharowe starcie tych reprezentacji od tamtej pory — neutralne psychologicznie. Wg 6P: umiarkowany faworyt (~58%, nie blowout) + silny sygnał Under + dominująca twarda przewaga defensywna Hiszpanii + zmęczenie Argentyny -> niskobramkowy margines +1: **1:0** zamiast szerszego 2:1. Model (λ_ESP szac. ~1,35, λ_ARG szac. ~0,93, blend rynek/własne wg `model.market_weight`=0,55) daje najwyższe oczek. pkt dla 1:0 (P szac. ~13,8%, fair odds ~7,25). Alternatywa top-2: **2:1** (gdyby Messi/Lautaro powtórzyli scenariusz z ostatnich sekund półfinału z Anglią — gol w 92' dzięki asyście Messiego, twarda forma z ostatniego meczu).

**Fortuna dziś:** BRAK zakładów na oba mecze w oknie. Francja-Anglia: nasza własna estymacja Over 2.5 (~64%) i BTTS niemal identyczna z rynkiem (~63-69% de-vig) — brak rozjazdu ≥5% wymaganego progu, mimo świeżego potwierdzenia Saliby OUT (rynek to już zdążył wycenić, odczyty z 16-17.07). Hiszpania-Argentyna: trzy niezależne źródła (rynek trofeum, Kalshi, własny rozkład 90-min+remis) dają niemal identyczny wynik ~58%/42% — zero rozjazdu, model rynkowy potwierdzony z wysoką pewnością, brak edge. O/U2.5 na finale też zbieżne (~60% Under rynek vs ~60% własne). efortuna.pl NADAL niedostępne dla WebFetch (403, problem ciągnący się od tygodni, potwierdzone dziś ponownie) — korzystamy z konsensusu STS/betfan.pl/US ksiąg (DraftKings/FanDuel/BetMGM) jako namiastki.

**Nowa zasada 31 — gdy niezależne metody estymacji prawdopodobieństwa zwycięstwa (rynek advance/trofeum, rynek predykcyjny typu Kalshi, i własny rozkład 90-min+redystrybucja remisu) zbiegają się blisko co do grosza, to silny sygnał wysokiej wiarygodności tej oceny — nie szukaj sztucznie kontrowersyjnego typu wbrew takiej zgodności:** Na finale Hiszpania-Argentyna trzy niezależne źródła (rynek "kto podniesie puchar" 58%/42%, Kalshi 58,1%/42,7%, własna kalkulacja z 90-min 1X2 + pół remisu 57,3%/42,8%) dały niemal identyczny wynik. W takiej sytuacji nie ma sensu przeszukiwać newsów w poszukiwaniu kontrariańskiego sygnału — trzymaj się środka tej zbieżności i skup wysiłek analityczny na MARGINESIE (Krok 6 pkt.4), gdzie twarde dane (tu: defensywa Hiszpanii, zmęczenie Argentyny) wciąż różnicują typ.

**Kontynuujemy:** Zasady 1-31 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju (mecz o 3. miejsce i finał, oba rozstrzygane ET+karnymi przy remisie — zweryfikowane regulaminowo). Terminarz: dziś (17.07) przerwa potwierdzona, mecz o 3. miejsce 18.07 (Francja-Anglia, Miami, Hard Rock Stadium — skorygowana lokalizacja), **finał 19.07 (Hiszpania-Argentyna, MetLife Stadium)** — oba mecze mają już zapisane typy. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403, potwierdzone ponownie dziś trzema metodami: WebFetch dwa razy + bezpośredni curl przez proxy) — ostatnia znana pozycja z 29.06 (5. miejsce), traktuj jako nieaktualną. Pościg top3: żaden z typów dziś nie jest czystym spotem dźwigni Fortuny (oba rynki zbieżne z naszą oceną) — na kicktippie oba typy (2:1 i 1:0) pod max EV z profilem meczu, zgodnie z twardymi danymi (Over-sygnał wzmocniony Salibą; defensywa Hiszpanii + zmęczenie Argentyny).

---

## 2026-07-16 — v1.37 (Rozliczenie: Anglia-Argentyna CHYBIONE — Argentyna 2:1 po golach w 85' i 92', nie Anglia 1:0; Argentyna w finale z Hiszpanią; dziś dzień przerwy bez meczów; NOWY typ na mecz o 3. miejsce 18.07 Francja-Anglia — silny sygnał Over łamie standardowy cagey profil pucharowy)

**Rozliczenie 15.07 — Anglia–Argentyna:** wynik **Argentyna 2:1 Anglia** (Anthony Gordon dał prowadzenie Anglii w 55', ale Enzo Fernández wyrównał w 85' i Lautaro Martínez dobił w 92' — przy obu golach asystował Messi). Nasz typ **1:0 (Anglia wygrywa wąsko)**: **CHYBIONA TENDENCJA I WYNIK (0 pkt)**. Model dał Anglii nieznaczną przewagę (~53-55% do awansu) opartą na potwierdzonych powrotach Rice'a/Konsy/Jamesa i silnym sygnale Under — trafiliśmy z niskim marginesem (1 gol różnicy, zgodne z Under-lean), ale pomyliliśmy KIERUNEK: Anglia prowadziła do 85', po czym Argentyna odwróciła losy meczu w ostatnich minutach dzięki indywidualnej klasie Messiego (2 asysty, mecz rozstrzygnięty bez jego gola). Argentyna awansuje do finału przeciw Hiszpanii (19.07).

**Nowa zasada 30 — gwiazda może zdecydować o meczu samymi asystami, nie tylko golami; nie redukuj jej wpływu do statystyki strzeleckiej:** Przy Anglia-Argentyna skupiliśmy się na tym, że Messi "nie strzelił" w poprzednich rundach relatywnie rzadko wpływając na wynik, ale w decydującym momencie (85' i 92') to jego podania, nie gole, przesądziły mecz. Przy ocenie gwiazd ofensywnych (Krok 3-4) waż KREACJĘ (asysty, kluczowe podania, xA) na równi z samymi golami — "chłodny" napastnik/rozgrywający wciąż może rozstrzygnąć mecz jako playmaker w ostatnich minutach, zwłaszcza gdy rywal broni wąskiego wyniku.

**Bilans:** kicktipp 123 pkt (bez zmian, 0 z rozliczenia), bankroll 955,57 PLN (bez zmian, ROI -4,4%). Jednostka 1u = 19,11 PLN. Fortuna: 11. dzień z rzędu bez zakładu.

**Dziś (16.07) — dzień przerwy, BEZ MECZÓW** (potwierdzone: 16-17.07 to dni bez gier między półfinałami a meczem o 3. miejsce). Okno lookahead (16-18.07 ET) obejmuje 1 mecz:

- **NOWY: Francja–Anglia** (18.07, 17:00 ET/23:00 CEST, Miami, Miami Stadium/Hard Rock Stadium) — mecz o 3. miejsce: typ **2:1** (Francja wygrywa, Anglia strzela). Obie drużyny odpadły z gry o finał (Francja przegrała 0:2 z Hiszpanią w PF, Anglia 1:2 z Argentyną) — mecz bez stawki tabelowej, ale z WYRAŹNĄ motywacją indywidualną: **Mbappé (8 goli, remis z Messim w klasyfikacji) rozgrywa swój OSTATNI mecz turnieju i ostatnią szansę na samodzielne prowadzenie w Złotym Bucie** (Messi gra w niedzielnym finale, nie doda goli w tym meczu) — silny bodziec do gry mimo dead-rubber dla drużyny; Kane (6 goli) też ma osobisty interes w dopisywaniu bramek. Newsy: Mbappé zdrowy po urazie kostki z QF (odegrał pełne 90 min w półfinale), Tchouaméni wrócił z urazu uda na mecz z Hiszpanią — Francja bez większych ubytków ofensywnych. Reece James (Anglia) wrócił do treningów po urazie — Anglia z niemal pełnym składem. Oczekiwane rotacje na obu ławkach (Deschamps sięga po Doué/Cherki, Anglia może dać szansę rezerwowym) — dodaje niepewności, ale nie zmienia kierunku. Rynek: Francja umiarkowany faworyt (DraftKings +105/+255/+255, FanDuel +100/+260/+260 → de-vig ~46-47% Francja / 26-27% remis / 26-27% Anglia). **Kluczowy sygnał: Over 2.5 mocno faworyzowany (-180, ~64% de-vig)** — mecze o brązowy medal historycznie bramkowe (luźniejsza defensywa, motywacja indywidualna zamiast taktycznej dyscypliny) — to PRZECIWIEŃSTWO standardowego cagey profilu pucharowego (6P), więc zamiast bezpiecznego 1:0 wybieramy **2:1** z realną alternatywą **3:1**, gdyby atak Francji w pełni wykorzystał luźniejszą defensywę Anglii (spójne z mocnym sygnałem Over). Tryb pucharowy: remis niemożliwy jako wynik końcowy (przy remisie po 90 min — dogrywka i karne, wynik zapisywany łącznie), więc typujemy tendencję (Francja) + margines (+1, powiększony do +1/+2 przez sygnał Over).

**Fortuna dziś:** BRAK zakładu na Francja-Anglia — mamy tylko orientacyjne kursy 1X2 z zagranicznych bukmacherów (DraftKings/FanDuel) i sygnał Over 2.5 (-180), ale BRAK potwierdzonego, dwustronnego kursu Under/Over ani rynku efortuna.pl (nadal niedostępne dla WebFetch, 403 — problem ciągnący się od tygodni) do policzenia rzetelnego edge. Nasza własna estymacja Over 2.5 (λ_total≈2,8, P(≥3 goli)≈53%) wypada NIŻEJ niż rynkowe ~64% implikowane przez -180 — sugeruje to, że Over jest już przewartościowany przez rynek (ujemny edge), a bez potwierdzonego kursu Under nie liczymy zakładu zgodnie z zasadą 27 (brak pewności = brak zakładu).

**Kontynuujemy:** Zasady 1-30 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do meczu o 3. miejsce i finału włącznie (oba rozstrzygane ET+karnymi przy remisie). Terminarz: 16-17.07 przerwa (dziś potwierdzone), mecz o 3. miejsce 18.07 (Francja-Anglia, Miami), **finał 19.07 potwierdzony: Hiszpania-Argentyna (MetLife Stadium, East Rutherford NJ, 15:00 ET)** — poza dzisiejszym oknem lookahead (+2 dni sięga tylko do 18.07), pełna analiza w jutrzejszym briefingu. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: typ na Francja-Anglia (2:1) różnicuje się od "bezpiecznego" 1:0 typowego dla dead-rubber, korzystając z realnego sygnału Over i motywacji Golden Boot Mbappé — brak dziś czystego spotu dźwigni Fortuny (za mało potwierdzonych danych kursowych).

---

## 2026-07-15 — v1.36 (Rozliczenie: Francja-Hiszpania CHYBIONE na całej linii — Hiszpania 2:0, nie Francja 2:1; nowa zasada 29 o elitarnej defensywie kontra gwiazdorski atak; dziś 2. półfinał Anglia-Argentyna, typ 1:0 bez zmian po świeżych newsach — Rice/Konsa/James zdrowi, Messi gotowy, rynek lekko przesunięty w stronę Anglii)

**Rozliczenie 14.07 — Francja–Hiszpania:** wynik **Hiszpania 2:0 Francja** (Oyarzabal karny 22', Porro 58') — Hiszpania awansuje do finału. Nasz typ **2:1 (Francja wygrywa, traci gola)**: **CHYBIONA TENDENCJA I WYNIK (0 pkt)**. Model dał Francji ~40-42% w 90 min i nie doszacował hiszpańskiej defensywy (najlepszej w turnieju, teraz czyste konto w półfinale wobec Mbappé "completely fine") — atak Francji, mimo zdrowego Mbappé, ponownie "zamarzł" w meczu pucharowym (podobnie jak Maroko w QF przy xG 3,04 na 2 gole), a tym razem defensywa Hiszpanii to skończyła czystym kontem zamiast typowego 2:1.

**Nowa zasada 29 — elitarna defensywa rywala potrafi anulować zdrowego, formowego napastnika, nawet gdy news o jego dyspozycji jest jednoznacznie pozytywny:** Francja-Hiszpania to już drugi w tym turnieju przypadek (po serii "gole zmarnowane mimo zdrowego składu" u Francji z Marokiem), gdzie potwierdzona dobra dyspozycja gwiazdy ofensywnej (Mbappé "completely fine") nie przełożyła się na gole, bo rywal miał najlepszą defensywę turnieju. Przy wyborze marginesu (Krok 6 pkt.4) waż realne dane defensywne rywala (bramki stracone/mecz, clean sheets) NIE MNIEJ niż formę/zdrowie napastnika — hard defensive stats > pozytywny news o ataku, gdy są w konflikcie.

**Bilans:** kicktipp 123 pkt (bez zmian, 0 z rozliczenia), bankroll 955,57 PLN (bez zmian, ROI -4,4%). Jednostka 1u = 19,11 PLN. Fortuna: 10. dzień z rzędu bez zakładu.

**Dziś (15.07) — Anglia–Argentyna** (15:00 ET/21:00 CEST, Atlanta, Mercedes-Benz Stadium) — 2. półfinał, decyduje kto zagra w finale z Hiszpanią: typ **1:0 bez zmian** z 13-14.07. Świeże potwierdzenia dziś: Declan Rice otrząsnął się z infekcji/zmęczenia sprzed QF, oczekiwany w wyjściowej 11; Ezri Konsa (skurcz w QF) dostępny; Reece James wraca do gry (jedyny zdrowy prawy obrońca) — przewidywana XI Anglii: Pickford; James, Konsa, Guéhi, O'Reilly; Rice, Anderson; Saka, Bellingham, Gordon; Kane. Jarell Quansah nadal zawieszony (2. mecz kary), Henderson poza turniejem (złamanie nadgarstka) — bez zmian względem wcześniejszych wpisów. Argentyna: Messi oczekiwany zdrowy na debiut przeciw Anglii mimo otarcia oka od Xhaki w QF (opatrzone, bez ryzyka); Romero bez nowej kontuzji po zejściu zmęczonym w dogrywce QF — obie strony bez świeżych negatywnych niespodzianek kadrowych. Rynek dziś (konsensus kilku bukmacherów, FanDuel/DraftKings): 90-min Anglia ~35-37% de-vig (+155/+165, remis +185/+190, Argentyna +200/+205) — blisko wpisu z 14.07 (~35,8%/31,6%/32,7%). Do awansu Anglia **~53-55%** de-vig (DraftKings -135/+110, inne -124/+106) — nieznaczna poprawa względem wczorajszego zacieśnienia (~51,6%), rynek wraca lekko w stronę Anglii. Dokładnej dwustronnej linii O/U 2.5 z dzisiejszego researchu nie potwierdzono liczbowo (jeden serwis wskazuje Under jako "plus-money" opcję), ale nie ma sygnału odwrotnego względem utrzymującego się od dni Under-lean (-155/+125, ~57,8% de-vig z 13-14.07) — margines 1:0 zamiast 2:1 pozostaje uzasadniony. Zgodnie z zasadą 29: elitarne, teraz w pełni zdrowe defensywy obu stron (Anglia z kompletem obrońców, Argentyna bez nowych ubytków) wspierają niskobramkowy scenariusz, nie odwrotnie.

**Fortuna dziś:** BRAK zakładu — rynek do awansu (~53-55% Anglia) blisko naszej własnej oceny, brak rozjazdu ≥5% wymaganego progu; O/U 2.5 bez potwierdzonej dwustronnej linii z dzisiejszego researchu, więc nie liczymy edge na tym rynku. efortuna.pl nadal niedostępne dla WebFetch (403, problem ciągnący się od tygodni) — konsensus zagranicznych ksiąg jako namiastka.

**Kontynuujemy:** Zasady 1-29 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju. Terminarz: dziś (15.07) drugi półfinał, przerwa 16-17.07, mecz o 3. miejsce 18.07, finał 19.07 (MetLife Stadium) — Hiszpania już potwierdzona w finale. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: typ na Anglia-Argentyna pod max EV z profilem meczu (1:0), zgodny z nową zasadą 29 (dwie zdrowe, solidne defensywy → niski total) — brak dziś czystego spotu dźwigni Fortuny.

---

## 2026-07-14 — v1.35 (dzień meczowy: 1. półfinał Francja-Hiszpania dziś wieczorem — typ 2:1 bez zmian po świeżych newsach; Anglia-Argentyna (15.07) typ 1:0 bez zmian mimo lekkiego zacieśnienia rynku; potwierdzono terminarz: przerwa 16-17.07, mecz o 3. miejsce 18.07, finał 19.07)

**Rozliczenie:** brak — `pending --due` puste, oba otwarte typy jeszcze nierozegrane. Francja-Hiszpania gra się dziś dopiero o 15:00 ET/21:00 CEST (po porannym uruchomieniu briefingu), Anglia-Argentyna jutro (15.07).

**Bilans:** bez zmian — 123 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN. Fortuna: 9. dzień z rzędu bez zakładu.

**Terminarz POTWIERDZONY dziś świeżym researchem:** po półfinałach (14.07 Francja-Hiszpania, 15.07 Anglia-Argentyna) będzie **przerwa 16-17.07 (2 dni, bez meczów)** — potwierdza wcześniejsze "do potwierdzenia". Mecz o 3. miejsce **18.07**, **finał 19.07 (MetLife Stadium, East Rutherford NJ)** — daty teraz twarde, nie estymacja. Okno lookahead (14-16.07 ET) nie obejmuje żadnego nowego meczu poza już zapisanymi dwoma półfinałami.

**Dziś (14.07) — Francja–Hiszpania** (15:00 ET/21:00 CEST, Arlington, AT&T Stadium): typ **2:1 bez zmian** z 12-13.07. Świeże potwierdzenia: Mbappé "completely fine" po otarciu kostki, oczekiwany w wyjściowej 11. Tchouameni to "game-time decision" (uraz uda, opuścił 2 ostatnie mecze) — nadal wątpliwy (szac.), rywalizuje z Kone o miejsce w środku pola. Nowy drobny sygnał: Saliba i Upamecano (obrona Francji) nie trenowali w sobotę — "slight cause for concern", ale obaj oczekiwani do gry (Saliba dzień odpoczynku, Upamecano indywidualna sesja) — nie zmienia oceny defensywy Francji. Rynek świeży (FanDuel): 90-min Francja ~39,7% de-vig (+135/+210/+210, przeliczone), do awansu ~57,8% (-150/+128), O/U2.5 blisko pickem z lekkim Over lean (~50,9%/49,1%, -114/-106) — wszystko spójne z oceną z 12-13.07 (wcześniej 41,4%/56,8%), brak istotnego przesunięcia. Typ i uzasadnienie bez zmian.

**Lookahead (15.07) — Anglia–Argentyna** (15:00 ET/21:00 CEST, Atlanta, Mercedes-Benz Stadium): typ **1:0 bez zmian**. Świeże newsy: Declan Rice zmagał się z infekcją przed QF, zszedł w przerwie po słabszej 1. połowie — dodatkowy defensywny znak zapytania obok Jarella Quansaha (zawieszony) i Reece'a Jamesa (kontuzjogenny, mało prawdopodobny w wyjściowej 11) — Ezri Konsa lub Djed Spence mają wypełnić prawą flankę. Messi doznał rozcięcia przy oku po starciu z Xhaką w QF, opatrzony, oczekiwany gotowy na debiut przeciw Anglii mimo ryzyka obrzęku. **Rynek zauważalnie się zacieśnił** względem wpisu z 13.07: 90-min de-vig Anglia ~35,8%/remis ~31,6%/Argentyna ~32,7% (+165/+200/+190, wcześniej +160/+190/+210 dawało Anglii wyraźniejszą przewagę), do awansu Anglia ~51,6% vs Argentyna ~48,4% (-120/-105, wcześniej ~54-57%/43-46%) — Kalshi pokazuje niemal remis (52¢/50¢). Mimo zacieśnienia Anglia wciąż nieznaczny faworyt, kierunek typu bez zmian. Sygnał Under 2.5 utrzymuje się (-155/+125, ~57,8% de-vig, identycznie jak 13.07) — nadal wskazuje niskobramkowy mecz, wspiera margines 1:0 zamiast 2:1 mimo formy Bellinghama/Kane'a. Rice/James/Quansah to defensywne osłabienie Anglii, ale nie na tyle jednoznaczne (nie potwierdzony konkretny brak w składzie, tylko doubt/unlikely), by zmienić kierunek — traktuj jako czynnik ryzyka do zweryfikowania jutro rano przed deadline'em.

**Fortuna dziś:** BRAK zakładów na oba półfinały — Francja-Hiszpania: świeży rynek (~39,7%/57,8%) w granicach szumu względem naszej oceny z 12-13.07, brak rozjazdu ≥5%. Anglia-Argentyna: mimo zacieśnienia rynku (Anglia advance spadła z ~54-57% do ~51,6%) nasza własna ocena podąża za tym samym trendem (mecz coraz bliżej 50/50), więc rozjazd modelu z rynkiem się nie otworzył — Under 2.5 też bez zmian względem rynku. efortuna.pl/legalsport.pl nadal niedostępne dla WebFetch (403, problem ciągnący się od tygodni) — konsensus zagranicznych ksiąg (FanDuel/DraftKings) jako namiastka, jak w poprzednich dniach.

**Kontynuujemy:** Zasady 1-28 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju. Terminarz kompletny i potwierdzony: półfinały 14-15.07, przerwa 16-17.07, mecz o 3. miejsce 18.07, finał 19.07. Tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: oba typy dziś pod max EV z profilem meczu — brak czystego spotu dźwigni Fortuny (rynki na obu meczach zbieżne z naszą oceną, w tym po zacieśnieniu linii Anglia-Argentyna).

---

## 2026-07-13 — v1.34 (dzień przerwy bez meczów, potwierdzony; typ na Francja-Hiszpania bez zmian po świeżych newsach; NOWY typ na Anglia-Argentyna 15.07 — mecz wchodzi dziś w okno lookahead, silny sygnał Under przechyla margines na niskobramkowy 1:0)

**Rozliczenie:** brak — żaden otwarty typ nie ma jeszcze rozegranego meczu (`pending --due` pusty). Francja-Hiszpania gra się dopiero jutro (14.07), Anglia-Argentyna pojutrze (15.07).

**Bilans:** bez zmian — 123 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN.

**Dziś (13.07) — dzień przerwy, BEZ MECZÓW** (potwierdzone: 12-13.07 to dni bez gier przed półfinałami). Okno lookahead (13-15.07, +2 dni) obejmuje oba półfinały:

- **Francja–Hiszpania (14.07, 15:00 ET/21:00 CEST, Arlington/AT&T Stadium) — typ 2:1 bez zmian.** Świeże potwierdzenia: Mbappé sam ocenił się jako "completely fine" po otarciu kostki z QF (Maroko) — powinien zacząć w wyjściowej 11. Tchouameni robi postępy w rehabilitacji, może wrócić do składu (walczy o miejsce z Kone, który zagrał solidnie w QF) — wciąż wątpliwy (szac.), decyzja bliżej meczu. Rynek: Francja 90-min ~41,4% de-vig (FanDuel +130/+220/+230), do awansu ~56,8% (-148/+120) — spójne z oceną z 12.07, brak istotnej zmiany. Yamal (Hiszpania) nadal nie w pełnej dyspozycji (wg wcześniejszych newsów). Typ i uzasadnienie bez zmian względem wpisu z 12.07.
- **NOWY: Anglia–Argentyna (15.07, 15:00 ET/21:00 CEST, Atlanta/Mercedes-Benz Stadium — 2. półfinał): typ 1:0 (Anglia wygrywa wąsko).** Mecz blisko wyrównany w 90 min (de-vig Anglia ~36,6%/remis ~32,8%/Argentyna ~30,7% wg +160/+190/+210), Anglia nieco wyraźniejszym faworytem do awansu (~54-57% de-vig, zgodne FanDuel -130/+106 i DraftKings -135/+110). **Kluczowy sygnał: O/U2.5 wyraźnie Under** (-155/+125, ~57,8% de-vig) — wskazuje niskobramkowy, spięty półfinał, MIMO że obie drużyny mają gorące ataki: Bellingham 6 goli w 6 meczach (dublet w R16 z Meksykiem i w QF z Norwegią, w tym zwycięski gol w doliczonym czasie dogrywki — pierwszy zawodnik od Maradony 1986 z 2+ golami w kolejnych meczach pucharowych jednego turnieju), Kane też 6 goli. Anglia dodatkowo POTWIERDZONA zdrowsza przed półfinałem — Rice, Guehi i James wrócili do treningów (byli wątpliwi z powodu choroby/urazu). Argentyna: Messi (współlider Złotego Buta, 8 goli) rozegrał pełne 120 min QF mimo drobnego otarcia oka od Xhaki (opatrzone, bez ryzyka), Romero zszedł zmęczony w dogrywce ale bez nowej kontuzji — gotowy, brak zawieszonych. H2H: pierwszy pucharowy mecz od MŚ 1998 (słynny remis 2:2 po dogrywce, Argentyna wygrała na karne) — historycznie ciasne starcia tych reprezentacji. Wg 6P: mecz bliski 50/50 (prawdopodobne karne) → tym mocniej +1 dla wytypowanego awansera, ale silny sygnał Under przechylił margines na niskobramkowy **1:0** zamiast **2:1** (mimo formy Bellingham/Kane) — zgodnie z pkt.3 playbooka ("2:1, lub 1:0 gdy niskobramkowo"). Alternatywa top-2: 2:1 (gdyby atak Anglii przebił się jak w meczach grupowych z wysokim wynikiem, np. 4:2 z Chorwacją).

**Fortuna dziś:** BRAK zakładów na oba półfinały. Francja-Hiszpania: rynek (~41,4%/56,8%) zbieżny z naszą oceną z 12.07, brak rozjazdu ≥5% (kontynuacja wcześniejszej decyzji). Anglia-Argentyna: zarówno rynek awansu (~54-57% Anglia), jak i O/U2.5 (~57,8% Under) są blisko naszej własnej oceny — nie znaleźliśmy wystarczająco pewnego, świeżego czynnika (kadrowego/taktycznego) dającego przewagę ≥5% ponad konsensus kilku bukmacherów (FanDuel/DraftKings/inne, zgodne ze sobą). efortuna.pl/legalsport.pl nadal niedostępne dla WebFetch (403, problem ciągnący się od tygodni) — korzystamy z konsensusu zagranicznych ksiąg jako namiastki, jak w poprzednich dniach.

**Kontynuujemy:** Zasady 1-28 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju. Terminarz: 12-13.07 przerwa (potwierdzone), półfinały 14.07 (Francja-Hiszpania) i 15.07 (Anglia-Argentyna), finał (data do potwierdzenia bliżej terminu, zwyczajowo ok. 19.07). Tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: oba typy dziś pod max EV z profilem meczu (Francja-Hiszpania 2:1 bez zmian, Anglia-Argentyna nowy 1:0 z naciskiem na sygnał Under) — brak dziś czystego spotu dźwigni Fortuny (rynek zbieżny z naszą oceną na obu meczach).

---

## 2026-07-12 — v1.33 (Rozliczenie QF: Anglia awansuje mimo zapisanego typu na Norwegię — wykryty błąd kolejności zespołów w selection z 09.07 (nowa zasada 28); Argentyna trafia tendencję; dziś dzień przerwy [12-13.07 potwierdzone], NOWY typ na 1. półfinał Francja-Hiszpania 14.07)

**Rozliczenie 11.07 (ostatnie 2 mecze QF):**
- Norwegia **1:2** Anglia (po dogrywce; Schjelderup dla Norwegii, Bellingham x2 dla Anglii, zwycięski gol w 93') — zapisany typ z 09.07 to selection **"2:1"** w polu `match: "Norway vs England"`. Zgodnie z konsekwentną konwencją zapisu (kolejność liczb w `selection` odpowiada kolejności zespołów w `match`, potwierdzoną na 7+ wcześniejszych wpisach, np. Canada-Morocco 1:2, Uruguay-Spain 0:1) oznacza to **Norwegia 2 : Anglia 1**. To sprzeczne z ówczesnym uzasadnieniem, które jednoznacznie opisywało Anglię jako faworyta wygrywającego z golem straconym (λ_ENG 1,5 > λ_NOR 1,3, "gramy wygraną z golem rywala", margines +1 dla awansera wg 6P) — realna intencja to najpewniej Anglia 2:1, ale zapisano odwrotnie względem pola `match`. Rozliczono zgodnie z tym, co faktycznie zarejestrowano (bo to jest nasz oficjalny rekord rekomendacji) — Norwegia 2:1 vs faktyczne Anglia 2:1: **CHYBIONA TENDENCJA (0 pkt)**.
- Argentyna **3:1** Szwajcaria (po dogrywce; Mac Allister, Alvarez, Lautaro Martínez dla Argentyny, Ndoye dla Szwajcarii, Embolo czerwona kartka) — typ 1:0: **TENDENCJA ✓ (+2 pkt)**, różnica bramek chybiona (model +1, faktyczna +2) — potwierdzenie osłabienia Szwajcarii bez Manzambiego nie uchroniło ich przed odpadnięciem, ale mecz i tak był bardziej otwarty niż nasz cagey/Under-lean profil zakładał.

**Bilans dnia 11.07:** kicktipp +2 pkt (0+2). Fortuna 0 PLN (brak zakładów, zgodnie z decyzją z 09-11.07).
**Łącznie:** 123 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN.

**Nowa zasada 28 — KRYTYCZNA: kolejność liczb w `selection` MUSI dokładnie odpowiadać kolejności zespołów w `match`, weryfikuj to jawnie przy każdym `add-pick`:** Wpis Norwegia-Anglia z 09.07 pokazuje realny koszt takiej pomyłki — poprawna intencja (Anglia wygrywa 2:1) zapisana została jako "2:1" pod `match="Norway vs England"`, co w naszej konwencji czyta się jako Norwegia wygrywa 2:1 — dokładne przeciwieństwo. Efekt: 0 zamiast prawdopodobnych 2-4 pkt. Od teraz PRZED każdym `add-pick` czytaj selection na głos w formie „TeamZMatch1 X : TeamZMatch2 Y" i porównaj z intencją z rationale, zwłaszcza gdy w tekście uzasadnienia drużyny pojawiają się w innej kolejności niż w polu `match` (np. rationale pisane pod kątem „faworyt:rywal", a `match` w kolejności z terminarza).

**Dziś (12.07) — dzień przerwy, BEZ MECZÓW** (potwierdzone: 12-13.07 to dni bez gier przed półfinałami). Okno lookahead (12-14.07, +2 dni) obejmuje 1 mecz:
- **NOWY: Francja–Hiszpania** (14.07, 15:00 ET/21:00 CEST, Arlington, AT&T Stadium — 1. półfinał): typ **2:1** (Francja wygrywa, ale traci gola). Francja umiarkowany faworyt do awansu (~56% de-vig, US ksiegarnie -144/+118), w 90 min blisko wyrównany (~40% Francja/30% remis/30% Hiszpania, STS/Betclic/Betfan zbieżne z FanDuel/DraftKings) — nie mismatch. Francja: elitarny atak (Mbappé 8 goli, współlider Złotego Buta; Dembélé w formie), ale "chłodniejszy" wykańczająco w pucharach (2:0 z Marokiem przy xG 3,04 — sporo zmarnowanych sytuacji). Hiszpania: najlepsza defensywa turnieju (1 stracony w 6 meczach — Belgia w QF przerwała serię 5 czystych kont), ale Yamal nie w pełnej dyspozycji (tylko 30 min z Zielonym Przylądkiem, 4 mecze bez udziału przy golu). H2H: Hiszpania wygrała 2 ostatnie spotkania z Francją, w tym półfinał Euro 2024 2:1 — realny czynnik psychologiczny. Wg 6P: umiarkowany faworyt (nie blowout) → margines domyślny +1 dla awansera → **2:1**, łapiący i wąską wygraną w regulaminowym, i typową wygraną po dogrywce/karnych. O/U2.5 blisko pickem (-110 obie strony, lekki Over lean) — spójne z umiarkowanie bramkowym meczem, nie grindem 0:0/1:0. Alternatywa top-2: **1:0** (gdyby defensywa Hiszpanii zamknęła atak Francji tak jak większości wcześniejszych rywali).

**Zapowiedź (poza oknem lookahead, deadline za >72h):** 2. półfinał 15.07 (Atlanta, 15:00 ET) to **Anglia – Argentyna** (obie drużyny potwierdzone po wczorajszych QF) — pełna analiza w kolejnym briefingu, gdy wejdzie w 2-dniowe okno lookahead.

**Fortuna dziś:** BRAK zakładu na Francja-Hiszpania — nasza ocena (Francja ~40-42% w 90 min, do awansu ~56-58%) jest blisko rynkowego konsensusu (STS/Betclic/Betfan/FanDuel/DraftKings zgodne: Francja de-vig ~40%/56%) — brak rozjazdu ≥5% wymaganego progu (zasada 27: nie obstawiaj bez solidnej własnej przewagi, zwłaszcza gdy cudze/rynkowe wyceny są już spójne). efortuna.pl i legalsport.pl nadal niedostępne dla WebFetch (403) — utrzymujący się od tygodni problem techniczny (patrz zasady z 06-07.07); korzystamy z konsensusu STS/Betclic/Betfan/US ksiegarni jako namiastki.

**Kontynuujemy:** Zasady 1-28 w mocy. Tryb pucharowy aktywny (draw_bias wyłączony) do końca turnieju. Terminarz: 12-13.07 przerwa, półfinały 14.07 (Francja-Hiszpania) i 15.07 (Anglia-Argentyna), finał (data do potwierdzenia bliżej terminu, zwyczajowo ok. 19.07). Tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: typ na Francja-Hiszpania (2:1) pod max EV z profilem meczu (umiarkowany faworyt, nie blowout) — brak dziś czystego spotu dźwigni (rynek zbieżny z naszą oceną).

---

## 2026-07-11 — v1.32 (Hiszpania-Belgia: EXACT trafiony 2:1, kolejny idealny odczyt "umiarkowany faworyt + traci gola"; dziś ostatnie 2 QF — Norwegia-Anglia i Argentyna-Szwajcaria — typy bez zmian, Manzambi TERAZ POTWIERDZONY OUT przez trenera Yakina, 12-13.07 potwierdzone jako dni przerwy przed półfinałami 14-15.07)

**Rozliczenie 10.07:** Hiszpania **2:1** Belgia — typ 2:1: **EXACT ✓ (+4 pkt!)**. Fabián Ruiz otworzył wynik, De Ketelaere wyrównał dla Belgii, a Mikel Merino (rezerwowy) strzelił zwycięską bramkę w 88' (dobitka po interwencji bramkarza Belgii Lammensa). Belgia grała bez kapitana Tielemansa (uraz na rozgrzewce) i straciła bramkarza Courtois (uraz w 2. połowie) — kolejne potwierdzenie, że umiarkowany faworyt z solidną defensywą + osłabiony rywal = wąska wygrana z golem przeciwnika, model trafił drugi dzień z rzędu w exact. Hiszpania awansuje do półfinału na Francję (14.07).

**Bilans dnia 10.07:** kicktipp +4 pkt (exact). Fortuna 0 PLN (brak zakładów — rynek już w pełni wyceniał przewagę Hiszpanii, zgodnie z decyzją z 08-10.07).
**Łącznie:** 121 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN.

**Terminarz półfinałów POTWIERDZONY:** 14.07 Francja–Hiszpania (Dallas, 15:00 ET), 15.07 zwycięzca(Norwegia/Anglia)–zwycięzca(Argentyna/Szwajcaria) (Atlanta, 15:00 ET). **12-13.07 to dni przerwy bez meczów** — potwierdzone (dawniej "do potwierdzenia" w v1.31). Dzisiejsze (11.07) 2 mecze QF to ostatnie przed przerwą.

**Dziś (11.07) — 2 ostatnie mecze QF, oba typy bez zmian:**
- Norwegia–Anglia (17:00 ET/23:00 CEST, Miami): typ **2:1** — bez zmian. Haaland potwierdzony w wyjściowej 11, w hicie formy (7 goli, współlider Złotego Buta z Mbappe/Messim), Kane (6 goli) w formie dla Anglii. Rynek (bet365) 90-min: Anglia ~48-50% de-vig (-106/+250/+280), Fortuna/Superbet zbliżone (Anglia 1,91/remis 3,55/Norwegia 4,10 → de-vig Anglia ~50%, remis ~27%, Norwegia ~23%). Opta supercomputer: Anglia 50,4% w regulaminowym czasie. Zgodne z naszą oceną z poprzednich dni — brak zmiany typu.
- Argentyna–Szwajcaria (21:00 ET/03:00 CEST 12.07, Kansas City): typ **1:0** — bez zmian, ale **Manzambi TERAZ POTWIERDZONY OUT** — trener Yakin oficjalnie: "Unfortunately, Johan Manzambi's injury hurts us enormously" (nie doszedł do siebie po urazie kolana z treningu przed R16). To rozstrzyga niepewność z wczorajszego wpisu (v1.31, zasada 26) na "OUT" - twarda dana, nie estymacja. Manzambi brał udział we wszystkich 9 golach Szwajcarii w turnieju (3G+2A) — jego brak dodatkowo osłabia i tak już ograniczony atak Szwajcarii, wzmacniając nasz Under-lean/cagey profil (rynek Under 2.5 nadal ~57% de-vig z +120 Over/1,67 Under). Argentyna do awansu ~72-75% de-vig (spójne z 08-10.07). Nie zmienia kierunku ani marginesu typu.

**Fortuna dziś:** BRAK zakładów na oba mecze QF — Norwegia-Anglia: nasza ocena 1X2 zbieżna z rynkiem Fortuny/Superbet (Anglia ~50% wymaga >52,4% by dać edge na kursie 1,91 — poniżej progu), Over/Under 2.5 też blisko rynku. Argentyna-Szwajcaria: mimo twardego potwierdzenia OUT Manzambiego, nie udało się zdobyć precyzyjnego kursu Fortuny na rynek awansu/BTTS z wystarczającą pewnością (efortuna.pl znów niedostępne dla WebFetch — 403, patrz niżej), a jedyna napotkana rekomendacja BTTS Tak @2,05 z zewnętrznego serwisu tipsterskiego stoi w sprzeczności z naszą własną analizą (potwierdzony brak Manzambiego obniża, nie podnosi, prawdopodobieństwo gola Szwajcarii) — pomijamy zgodnie z zasadą "brak pewności = brak zakładu". Szósty dzień z rzędu bez zakładów Fortuna, portfel niezmieniony (955,57 PLN).

**Nowa zasada 27 — brak dostępu do precyzyjnych kursów Fortuny (WebFetch 403) nie usprawiedliwia obstawiania na podstawie cudzych rekomendacji tipsterskich bez własnej weryfikacji edge:** Napotkana sugestia BTTS Tak @2,05 na Argentyna-Szwajcaria z zewnętrznego serwisu ignorowała świeże, twarde potwierdzenie nieobecności Manzambiego — pokazuje, że treści tipsterskie bywają nieaktualne względem najnowszych newsów kadrowych. Trzymaj się własnego modelu (kroki 3-6) i nie kopiuj cudzych rekomendacji bez przeliczenia edge na podstawie najświeższych, potwierdzonych danych.

**Kontynuujemy:** Zasady 1–27 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Dzisiejsze 2 mecze kończą QF — **12-13.07 dni przerwy (potwierdzone)**, półfinały 14.07 (Francja-Hiszpania) i 15.07 (Norwegia/Anglia vs Argentyna/Szwajcaria). Tabela ligi kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: oba typy dziś pod max EV z profilem meczu (Norwegia-Anglia 2:1 zamiast bezpiecznego 1:0, Argentyna-Szwajcaria wąskie 1:0 wzmocnione twardym potwierdzeniem OUT Manzambiego) — różnicują się od typowych wyborów tłumu bez odchodzenia od najlepszego EV.

---

## 2026-07-10 — v1.31 (Francja-Maroko: EXACT trafiony 2:0, model idealnie złapał mismatch; dziś Hiszpania-Belgia, typy na Norwegię-Anglię i Argentynę-Szwajcarię bez zmian, korekta statusu Manzambiego)

**Rozliczenie 09.07:** Francja **2:0** Maroko — typ 2:0: **EXACT ✓ (+4 pkt!)**. Mbappé (60', po niewykorzystanym karnym) i Dembélé (66') dały Francji spokojną wygraną (xG 3,04 vs 0,14 Maroka) — Saibari POTWIERDZONY OUT osłabił atak Maroka dokładnie tak, jak zakładaliśmy. Model idealnie trafił: wyraźny faworyt + "chłodzący się w pucharach, ale wciąż dominujący" atak Francji = margines +1 zamiast napompowanego 3:0.

**Bilans dnia 09.07:** kicktipp +4 pkt (exact). Fortuna 0 PLN (brak zakładów — rynek już w pełni wyceniał przewagę Francji).
**Łącznie:** 117 pkt kicktipp, 955,57 PLN bankroll (ROI -4,4%). Jednostka 1u = 19,11 PLN.

**Dziś (10.07) — Hiszpania–Belgia** (15:00 ET/21:00 CEST, Inglewood/SoFi): typ **2:1** — bez zmian z 08-09.07. Świeże potwierdzenia: **De Bruyne POTWIERDZONY w wyjściowej 11** (był tylko rotowany/odpoczywał przeciw USA, nie kontuzjowany), Debast nadal pod znakiem zapytania (późny test fitness) — skład obrony Belgii bez zmian. Nico Williams (Hiszpania) fit tylko do ławki, Baena kontynuuje na skrzydle. Rynek (bet365/ESPN): Hiszpania 90-min ~58% de-vig (-160/+425/+290), do awansu ~76% (kurs 1,31). Over 2.5 lekko faworyzowany (-125, ~53% de-vig), BTTS @1,78 — potwierdza sygnał goli z obu stron, nie czyste konto Hiszpanii mimo 5 clean sheets w grupie+R16. Brak rozjazdu z naszą oceną → **brak edge Fortuna** (piąty dzień z rzędu, szac. <3%, rynek już dyskontuje Onanę).

**Lookahead (11.07, 2 ostatnie mecze QF):**
- Norwegia–Anglia (17:00 ET/23:00 CEST, Miami): typ **2:1** — bez zmian. Haaland **ZDROWY** — nowa twarda informacja: nieobecność w ostatnim meczu grupowym z Francją to była rotacja/zarządzanie zmęczeniem (10 zawodników odpoczywało), NIE kontuzja — usuwa wcześniejszą niepewność, wzmacnia typ na jego udział w pełnej formie. Rynek (bet365): Anglia 90-min ~48% de-vig (-106/+250/+280), remis ~27%, Norwegia ~25% — spójne z oceną z 09.07. Brak edge Fortuna (nasz szac. Over 2.5 nadal poniżej rynkowego de-vig).
- Argentyna–Szwajcaria (21:00 ET/03:00 CEST 12.07, Kansas City): typ **1:0** — bez zmian, ale **korekta statusu Manzambiego**: wczoraj (09.07) oznaczony jako "POTWIERDZONY OUT", dziś świeże cytaty trenera Yakina ("mamy nadzieję, ale tylko jeśli ma to sens i nie ma ryzyka... zobaczymy w ciągu najbliższego dnia/dwóch") pokazują, że status jest **wątpliwy/niepewny**, nie definitywnie zamknięty — koryguję oznaczenie na "wątpliwy (szac. raczej nie zagra, ale niepotwierdzone ostatecznie)". Nie zmienia kierunku typu (Argentyna nadal umiarkowany faworyt, Under 2.5 nadal wyceniany ~57-60% de-vig, cagey profil), ale to przypomnienie z zasady 23 działa też dla kontuzji, nie tylko zawieszeń — zobacz nowa zasada niżej. Rynek do awansu: Argentyna ~76% (kurs 1,31 na advance). Brak edge Fortuna (sygnały ofensywne mieszane po obu stronach).

**Fortuna dziś:** BRAK zakładów na wszystkie 3 mecze w oknie (Hiszpania-Belgia, Norwegia-Anglia, Argentyna-Szwajcaria) — piąty dzień z rzędu bez zakładów, portfel niezmieniony (955,57 PLN). Zgodnie z zasadą "brak value to OK" — rynki dla wszystkich 3 są już blisko naszej własnej oceny, brak rozjazdu ≥5%.

**Nowa zasada 26 — status kontuzji potrafi się wahać dzień do dnia nawet po wcześniejszym "potwierdzeniu":** Manzambi (Szwajcaria) był wczoraj oznaczony jako "POTWIERDZONY OUT" na bazie cytatu trenera o "wysoce nieprawdopodobnym" powrocie, a dziś ten sam trener mówi o "nadziei" i decyzji "w ciągu najbliższego dnia/dwóch". Rozszerzenie zasady 23 (weryfikuj zawieszenia tuż przed deadline'em) na kontuzje: przy zawodnikach kluczowych dla drużyny, status "OUT" sprzed >24h wart jest ponownej weryfikacji rano w dniu meczu, zwłaszcza gdy pierwotny cytat trenera zawierał słowo "prawdopodobnie/hope"/"unlikely" zamiast twardego potwierdzenia listy kadrowej. Nie obniża to pewności typu (kierunek pozostaje ten sam), ale trzyma nas uczciwych względem odbiorcy co do tego, co jest twardą daną a co estymacją.

**Kontynuujemy:** Zasady 1–26 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. QF kończy się jutro (11.07, Norwegia-Anglia + Argentyna-Szwajcaria), **12.07 dzień przerwy** (półfinały startują dopiero 14.07 wg zapowiedzi FIFA — do potwierdzenia w kolejnym briefingu). Tabela ligi kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: żaden z 3 typów w oknie dziś nie jest czystym spotem dźwigni (wszystkie pod max EV z profilem meczu, zbieżne z rynkiem) — Norwegia-Anglia (2:1 zamiast bezpiecznego 1:0) i Argentyna-Szwajcaria (1:0, nie szerszy 2:0) nadal różnicują się od typowych wyborów tłumu.

---

## 2026-07-09 — v1.30 (dzień bez rozliczenia — QF Francja-Maroko dopiero dziś wieczorem; NOWE typy na oba QF soboty: Norwegia-Anglia i Argentyna-Szwajcaria)

**Rozliczenie:** brak — oba otwarte typy (Francja-Maroko 09.07, Hiszpania-Belgia 10.07) jeszcze się nie odbyły (mecz dzisiejszy startuje dopiero o 16:00 ET, czyli po tym uruchomieniu o 05:46 ET). Zgodnie z zasadą idempotentności `pending --due` poprawnie nie pokazał nic do rozliczenia.

**Dziś (09.07) — 1 mecz: Francja–Maroko** (16:00 ET/22:00 CEST, Boston/Gillette): typ **2:0** — bez zmian z 07.07. Nowe twarde dane: Saibari (Maroko) POTWIERDZONY OUT (uraz dwugłowego, zastąpi go Rahimi) — wcześniej był tylko "wątpliwy", teraz to fakt. Tchouameni (Francja) wątpliwy (przywodziciel) — drobne osłabienie środka pola Francji, nie zmienia oceny. Rynek: Francja 90-min ~61-64% (de-vig z -180/+295/+550), do awansu ~76% (z -400/+300). O/U2.5 lekko Under (-115 vs -105, ~51% de-vig) — potwierdza "chłodzący się" atak Francji w pucharach z 07.07. Brak zmiany typu.

**Lookahead (10-11.07, 3 kolejne mecze QF — komplet rundy 4 meczów):**
- Hiszpania–Belgia (10.07, 15:00 ET/21:00 CEST, Inglewood/SoFi): typ **2:1** — bez zmian z 08.07. Onana (Belgia) POTWIERDZONY koniec turnieju (ACL) — już znane. Nowe: Debast (Belgia) wymaga późnego testu fitness, De Bruyne typowany do gry w środku pola. Hiszpania w pełni zdrowa (Nico Williams wraca po drobnym urazie). Rynek: Hiszpania 90-min ~58-61% de-vig (1.63/5.40/3.90 i -160/+450/+290), BTTS i Over 2.5 "backed confidently" wg analityków (Belgia strzeliła we wszystkich meczach poza 0:0 z Iranem) — potwierdza typ 2:1 (nie czyste konto Hiszpanii).
- **NOWY: Norwegia–Anglia** (11.07, 17:00 ET/23:00 CEST, Miami): typ **2:1** (Anglia wygrywa, ale Norwegia/Haaland strzela) — mecz blisko wyrównany w 90 min (de-vig ~48% ENG/27% remis/25% NOR wg bet365 -106/+250/+280), ale Anglia wyraźniejszy faworyt do awansu (~69% z kursu 4/9 qualify). Over 2.5 mocno faworyzowany (-146, szac. ~57% de-vig) — obie ofensywy w hicie formy: Haaland 7 goli/4 mecze (współlider Złotego Buta z Mbappe i Messim), Kane+Bellingham prowadzą atak Anglii. Henderson (Anglia) kończy turniej (uraz nadgarstka, operacja) — nie wpływa na formację ataku. Zgodnie z zasadą 6P (umiarkowany faworyt z realnym atakiem w formie = analogia "Anglia-Kane" z playbooka) → typujemy wygraną z golem rywala (2:1), nie bezpieczne 1:0. Model (λ_ENG≈1.5, λ_NOR≈1.3 szac. z linii total) daje wyższe oczek. punkty dla 2:1 (E≈1.27) niż dla 1:0 (E≈1.12) — margines wyraźny.
- **NOWY: Argentyna–Szwajcaria** (11.07, 21:00 ET/03:00 CEST 12.07, Kansas City): typ **1:0** (Argentyna wygrywa wąsko) — Argentyna umiarkowany faworyt w 90 min (de-vig ~56% wg -145/+260/+425), ale Under 2.5 wyraźnie faworyzowany (-150, szac. ~57% de-vig) — cagey/niskobramkowy mecz oczekiwany, nie mismatch. Szwajcaria OSŁABIONA: Manzambi (najlepszy strzelec kadry, 3G+2A) POTWIERDZONY OUT (uraz kolana z treningu, trener Yakin przyznaje że powrót "wysoce nieprawdopodobny"), plus Aebischer i Jaquez również niedostępni — poważne straty w ataku, środku pola i obronie. Messi (Argentyna) nadal lider Złotego Buta (8 goli), ale J. Álvarez pcha się w miejsce słabszej formy Lautaro Martíneza, a Almada/Molina też w dołku formy — obie strony mają pewne wątpliwości ofensywne, stąd cagey, a nie szeroki mismatch. Model (λ_ARG≈1.3, λ_SUI≈0.9 szac.) daje najwyższe oczek. punkty dla 1:0 (E≈1.28) vs 2:1 (E≈1.22) vs 2:0 (E≈1.12) — margines wąski między 1:0 a 2:1, ale Under-lean + 3 nieobecności Szwajcarii przechylają w stronę niskobramkowego wyniku.

**Fortuna dziś:** BRAK zakładów na wszystkie 4 mecze QF w oknie. Francja-Maroko: rynek już w pełni wycenia przewagę Francji (do awansu -400), brak rozjazdu. Hiszpania-Belgia: mimo potwierdzonej kontuzji Onany, rynek (-160) już to dyskontuje, szac. edge <3% (kontynuacja oceny z 08.07). Norwegia-Anglia: nasz szac. Over 2.5 (~53%, λ_total=2.8) WYCHODZI PONIŻEJ rynkowego de-vig (~57%) — brak edge, a konkretnych kursów BTTS nie znaleziono w researchu (nie obstawiamy bez potwierdzonego kursu). Argentyna-Szwajcaria: sygnały mieszane (osłabiona Szwajcaria ofensywnie i w obronie jednocześnie, Argentyna też z wątpliwościami w ataku) — brak wystarczająco pewnego kierunku edge ≥5%. Zgodnie z zasadą "brak value to OK" — czwarty dzień z rzędu bez zakładów Fortuna, portfel niezmieniony (955.57 PLN).

**Kontynuujemy:** Zasady 1–25 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju — QF to teraz KOMPLETNA runda 4 meczów w oknie lookahead (Francja-Maroko 09.07, Hiszpania-Belgia 10.07, Norwegia-Anglia + Argentyna-Szwajcaria 11.07), półfinały dopiero po 11.07. Tabela ligi kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: żaden z 4 typów QF dziś nie jest czystym spotem dźwigni (wszystkie pod max EV z profilem meczu — 2 wyraźne faworyty z marginesem, 2 umiarkowane/cagey), ale Norwegia-Anglia (2:1 zamiast bezpiecznego 1:0) i Argentyna-Szwajcaria (1:0, nie szerszy 2:0) już same w sobie różnicują się od "oczywistych" typów tłumu.

---

## 2026-07-08 — v1.29 (R16 zamknięte: Argentyna odrabia 0:2 z Egiptem, ale Szwajcaria-Kolumbia poszła w złą stronę na karnych; dziś dzień przerwy, jutro QF Francja-Maroko, w oknie NOWY typ Hiszpania-Belgia — Onana z World Cup-ending ACL)

**Wyniki 07.07 (R16, ostatni dzień 1/8 finału):**
- Argentyna **3:2** Egipt — typ 2:0 (Argentyna wyg.): **TENDENCJA ✓ (+2 pkt)**, różnica bramek i exact chybione. Egipt prowadził 2:0 (Ibrahim, Zico) po tym jak Shobeir obronił karnego Messiemu (plus 2 inne interwencje) — kolejny "bramkarz-bohater prawie niszczy mismatch" (zasada 6), zanim Romero (79'), Messi (83') i Enzo Fernández (90+2') dopięli odwrócenie wyniku. Model poprawnie wskazał kierunek, ale mocno nie doszacował dramatyzmu — Egipt był bliżej sensacji niż nasz margines +2 sugerował.
- Szwajcaria **0:0** Kolumbia (po dogrywce, karne 4:3 dla Szwajcarii → zapis **4:3**) — typ 0:1 (Kolumbia wyg. wąsko): **CHYBIONA TENDENCJA (0 pkt)**. Mecz bez goli w 120 min, Akanji spudłował z 11 m, ale Sánchez i Cucho Hernández nie trafili za Kolumbię — Vargas dał awans Szwajcarii. Nasza ocena (Kolumbia ~59% de-vig) była tylko lekką przewagą, a w meczu idącym do karnych kierunek jest praktycznie monetą — potwierdzenie, że przy 50/50 blisko progu 55-60% nie warto budować silnego przekonania co do kierunku.

**Bilans dnia 07.07:** kicktipp +2 pkt (2+0). Fortuna 0 PLN (brak zakładów na te dwa mecze — zgodnie z wcześniejszą decyzją o braku edge).
**Łącznie:** 113 pkt kicktipp, 955.57 PLN bankroll (ROI -4.4%). Jednostka 1u = 19.11 PLN.

**Nowa zasada 25 — mecz blisko 50/50 idący w stronę dogrywki/karnych: kierunek jest praktycznie losowy, nawet przy przewadze modelu 55-60%:** Szwajcaria-Kolumbia to kolejny (po Belgia-Senegal 01.07, USA-Belgia 06.07) przypadek, gdzie umiarkowana przewaga jednej strony (tu: Kolumbia ~59%) nie przełożyła się na wynik — 120 min bez goli i karne to czysta loteria. Wniosek: kicktipp i tak wymaga wyniku (regulamin), więc typujemy zgodnie z modelem, ale NIE warto stawiać Fortuny na kierunek awansu w takich meczach, nawet przy pozornym edge blisko progu — wariancja karnych/dogrywki dominuje nad niewielką przewagą probabilistyczną. Traktuj mecze z Under 2.5 mocno faworyzowanym + wyrównanymi drużynami jako kandydatów do wysokiej niepewności kierunkowej niezależnie od modelu.

**Dziś (08.07) — dzień przerwy, BEZ MECZÓW** (potwierdzone: R16 zamknięte, ćwierćfinały startują jutro). Okno lookahead (08-10.07) obejmuje 2 mecze QF:
- Francja–Maroko (09.07, 16:00 ET/22:00 CEST, Boston/Gillette): typ **2:0** — bez zmian z 07.07. Saibari (Maroko) nadal "major doubt" (uraz uda/dwugłowego z R16 vs Kanadą), brak nowej twardej informacji zmieniającej ocenę. Rynek: Francja ~76-77% do awansu (FanDuel -410/Maroko +310 de-vig), 90-min ~61%. Brak edge Fortuna (rynek już w pełni wycenia francuską przewagę).
- **NOWY: Hiszpania–Belgia** (10.07, 15:00 ET/21:00 CEST, Inglewood/SoFi): typ **2:1** (Hiszpania wyg., ale traci gola) — Hiszpania wyraźny faworyt do awansu (de-vig szac. ~72-75%, 90-min ~59%), najlepsza defensywa turnieju (0 straconych w 5 meczach). **Amadou Onana (kluczowy defensywny pomocnik Belgii) POTWIERDZONY koniec turnieju — zerwane ACL** z meczu z USA (nowa twarda informacja, dodatkowo osłabia Belgię). Mimo to Lukaku (8 goli, wyrównał rekord Maradony) i De Bruyne to realne zagrożenie ofensywne, a rynek O/U 2.5 lekko faworyzuje "over" (~54%) — sygnał, że gole padną z obu stron, nie czyste konto Hiszpanii jak w poprzednich rundach. Margines +1 wg 6P → **2:1** zamiast bezpiecznego 2:0.

**Fortuna dziś:** Brak zakładów — Francja-Maroko w pełni wyceniona przez rynek (brak rozjazdu), Hiszpania-Belgia: mimo potwierdzonej kontuzji Onany rynek (-320 na awans) już to dyskontuje, nasz szac. edge <3%, poniżej progu 5%. Zgodnie z zasadą "brak value to OK".

**Kontynuujemy:** Zasady 1–25 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. QF startuje 09.07 (Francja-Maroko), 10.07 Hiszpania-Belgia, 11.07 Norwegia-Anglia + Argentyna-Szwajcaria (obie poza dzisiejszym oknem lookahead, ale już wiadomo: Argentyna i Szwajcaria potwierdzone jako przeciwnicy w dolnej połowie drabinki). Tabela ligi kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: dziś brak nowych spotów dźwigni (oba typy QF pod max EV, rynek zbieżny z naszą oceną po uwzględnieniu kontuzji Onany).

---

## 2026-07-07 — v1.28 (Hiszpania z Portugalią exact w doliczonym czasie; korekta USA-Belgia i tak chybiona — Belgia rozjechała 4:1; R16 kończy się dziś, QF startuje 09.07 Francja-Maroko)

**Wyniki 06.07 (R16, dzień 3, ostatni dzień 1/8 finału):**
- Portugalia **0:1** Hiszpania — typ 0:1 (Hiszpania wyg. wąsko): **EXACT ✓ (+4 pkt!)**. Mikel Merino (wszedł z ławki) strzelił w 90+1', kończąc karierę mundialową Ronaldo. Rozstrzygnięte w regulaminowym czasie (91' to doliczony czas, nie dogrywka) — model idealnie złapał "umiarkowany faworyt + wąska wygrana z bramką w końcówce".
- USA **1:4** Belgia — typ 2:1 (USA wyg. wąsko, po korekcie z 06.07 ws. Baloguna): **CHYBIONA TENDENCJA (0 pkt)**. Belgia zdominowała: De Ketelaere dublet (9', 32'), Vanaken (57' po błędzie bramkarza USA), Lukaku w doliczonym czasie. Tillman odpowiedział wolnym z 31', ale to jedyny gol USA. Balogun (dostępny po cofniętym zawieszeniu) nie zdobył gola — czynnik, na którym oparliśmy korektę typu, okazał się nieistotny wobec ogólnej przewagi jakościowej Belgii.

**Bilans dnia 06.07:** kicktipp +4 pkt (4+0). Fortuna 0 PLN (brak zakładów — rekomendacja na USA-Belgię wycofana dzień wcześniej z powodu edge poniżej progu).
**Łącznie:** 111 pkt kicktipp, 955.57 PLN bankroll (ROI -4.4%). Jednostka 1u = 19.11 PLN.

**Nowa zasada 24 — pojedynczy czynnik (dostępność/zawieszenie) nie kompensuje ogólnej przewagi jakościowej rywala:** Korekta typu USA-Belgia (z zasady 23) była logicznie poprawna — Balogun rzeczywiście zagrał — ale i tak przegraliśmy tendencję, bo Belgia (De Bruyne, Lukaku, De Ketelaere) była po prostu lepsza jakościowo, niezależnie od jednego zawodnika USA. Lekcja: gdy korygujesz typ na podstawie POJEDYNCZEGO odwróconego czynnika (kontuzja/zawieszenie), sprawdź, czy ten czynnik faktycznie odwraca WIĘKSZOŚĆ przewagi rywala, czy tylko jeden z wielu elementów przewagi jakościowej — w tym wypadku Belgia miała przewagę nawet bez czynnika zawieszenia.

**R16 kończy się dziś (07.07) — 2 ostatnie mecze, oba już wcześniej typowane (lookahead z 05.07), potwierdzone świeżymi newsami bez zmian:**
- Argentyna–Egipt (12:00 ET/18:00 CEST, Atlanta): typ **2:0** — bez zmian. Salah POTWIERDZONY w składzie (wrócił z naderwania dwugłowego, przeszedł pełne 120 min + karne z Australią). Rynek do awansu: Argentyna ~84% (devig z -750/+510) — blisko naszej oceny ~85%, brak edge Fortuna (zgodnie z decyzją z 05.07).
- Szwajcaria–Kolumbia (16:00 ET/22:00 CEST, Vancouver): typ **0:1** — bez zmian. Szwajcaria ma w pełni zdrowy, ustabilizowany skład (trener Yakin). Rynek do awansu: Kolumbia ~59% (devig z -162/+132) — identyczne z naszą oceną ~59%, brak edge Fortuna.

**NOWY typ (QF, 09.07, lookahead — deadline za ~48h): Francja–Maroko** (16:00 ET/22:00 CEST, Boston): typ **2:0** — rewanż półfinału MŚ 2022 (Francja wygrała wtedy 2:0). Francja niepokonana (5/5), najlepszy atak turnieju (14 goli), ale ostatnie 2 mecze pucharowe wygrała wąsko (Paragwaj 1:0 zamiast oczekiwanego szerszego wyniku) — atak "chłodnieje" w pucharach. Maroko niepokonane (5/5), zorganizowane defensywnie (Bono, Hakimi), ale **Saibari (kluczowy ofensywny pomocnik) zszedł z urazem dwugłowego w R16 vs Kanadą** — osłabia atak Maroka na QF. Rynek (Kalshi): Francja ~62% w 90 min, remis 25%, Maroko 15%; do awansu szac. Francja ~75%. Brak wyraźnego rozjazdu z naszą oceną — brak zakładu Fortuna na ten mecz na razie (zweryfikować kursy efortuna.pl bliżej meczu).

**Terminarz potwierdzony:** R16 kończy się dziś (07.07). **08.07 — dzień przerwy bez meczów.** QF startuje 09.07 (Francja-Maroko), 10.07 Hiszpania-Belgia (Los Angeles), 11.07 Norwegia-Anglia + mecz Kansas City (zwycięzca Argentyna/Egipt vs zwycięzca Szwajcaria/Kolumbia — poznamy dziś wieczorem).

**Kontynuujemy:** Zasady 1–24 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Tabela ligi kicktipp.pl nadal niedostępna dla WebSearch/WebFetch — ostatnia znana pozycja z 29.06 (5. miejsce). Pościg top3: dziś brak nowych spotów dźwigni (oba mecze R16 rynek zbieżny z naszą oceną, potwierdzamy typy z lookahead); QF Francja-Maroko typowany pod max EV (wyraźny faworyt, margines +1 skorygowany w dół wobec trendu "chłodnącego" ataku Francji w pucharach).

---

## 2026-07-06 — v1.27 (PODWÓJNY szok R16: Norwegia rozjeżdża Brazylię, Anglia w 10 wygrywa na Azteca; zawieszenie Baloguna cofnięte — typ USA-Belgia zmieniony)

**Wyniki 05.07 (R16, dzień 2) — najgorszy dzień kicktippa w tym turnieju:**
- Brazylia **1:2** Norwegia — typ 2:1 (Brazylia wyg.): **CHYBIONA TENDENCJA (0 pkt)**. Haaland dublet (79', 90'), w tym trafienie głową po dośrodkowaniu i strzał z dystansu — bohaterem meczu bramkarz Norwegii Ørjan Nyland, który obronił karnego Bruno Guimarãesowi (pierwszy niewykorzystany karny Brazylii na MŚ od Zico w 1986!). Neymar honorowo z karnego w 90+10'. Fortuna BTTS Tak @1.78 → **WON (+15.60 PLN)** — jedyny plus dnia.
- Meksyk **2:3** Anglia — typ 1:0 (Meksyk wyg.): **CHYBIONA TENDENCJA (0 pkt)**. Bellingham x2 (36', 38'), Kane z karnego (60') dały Anglii 3:0, mimo czerwonej kartki Quansaha (54') Anglia utrzymała wynik w dziesiątkę >40 min. Jiménez z karnego (69') tylko ładniej ustawił wynik. Fortuna Meksyk wygrana (90 min) @3.55 → **LOST (-20.00 PLN)**.

**Bilans dnia 05.07:** kicktipp +0 pkt (2x chybiona tendencja — pierwszy taki dzień w turnieju). Fortuna -4.40 PLN (15.60-20.00).
**Łącznie:** 107 pkt kicktipp, 955.57 PLN bankroll (ROI -4.4%). Jednostka 1u = 19.11 PLN.

**Nowa zasada 22 — R16 to dalej chaos, nawet przy "twardych" argumentach (wysokość, forma):** Oba typy dziś padły na **wyraźnym faworycie rynkowym korygowanym przez konkretny czynnik** (Meksyk: forteca Azteca + wysokość; Brazylia: umiarkowany faworyt w formie). Anglia pokazała, że jakość indywidualna (Bellingham, Kane) potrafi przełamać i wysokość, i grę w dziesiątkę — argument "nie zdążą się zaaklimatyzować" (Tuchel) okazał się nietrafny. Norwegia z kolei pokazała, że drużyna z jednym dominującym snajperem (Haaland) + bohaterem-bramkarzem może rozjechać nawet "umiarkowanego faworyta w formie ofensywnej" — kolejne potwierdzenie zasady 6 (bramkarz-bohater niszczy mismatch) w rundzie pucharowej. **Wniosek:** w R16+ obniżaj pewność siebie nawet przy pozornie solidnych argumentach jakościowych — pojedynczy mecz eliminacyjny ma wysoką wariancję, zwłaszcza gdy rywal ma formę indywidualną (snajper/bramkarz) zdolną przeważyć przewagę drużynową.

**Nowa zasada 23 — weryfikuj status zawieszeń/kar DYSCYPLINARNYCH tuż przed deadline'em, nie tylko dzień wcześniej:** Typ na USA-Belgia z 04.07 opierał się na "potwierdzonym" zawieszeniu Baloguna (czerwona kartka). Dziś rano wyszło na jaw, że **FIFA warunkowo zawiesiła wykonanie kary** (po naciskach politycznych/proteście Belgii) — Balogun jednak zagra. Kary dyscyplinarne w pucharach bywają przedmiotem odwołań/decyzji tuż przed meczem — sprawdzaj status **rano w dniu meczu**, nie polegaj na informacji sprzed 1-2 dni, zwłaszcza gdy sprawa jest głośna medialnie/politycznie.

**Korekta typu dziś (06.07, R16 dzień 3):**
- **USA–Belgia (zmieniony typ):** poprzedni 1:2 (Belgia) → **NOWY: 2:1 (USA)**. Powód: Balogun jednak dostępny (patrz zasada 23) — kluczowy czynnik unieważniony. Rynek awansu teraz lekko faworyzuje USA (~54% de-vig) nad Belgią (~46%), Belgia dodatkowo grała 120 min (dogrywka z Senegalem) — większy deficyt regeneracji niż USA. USA gospodarzem (Seattle, doping). Fortuna: **WYCOFANO** rekomendację "Belgia awans @2.05" (edge był zbudowany na nieaktualnej informacji) — po korekcie edge na USA wychodzi ~4.7%, poniżej progu 5%. Brak zakładu na ten mecz dzisiaj.
- **Portugalia–Hiszpania:** typ **0:1** bez zmian — Hiszpania umiarkowany faworyt (~52-55% de-vig), najlepsza defensywa turnieju (0 straconych w 4 meczach), ale Portugalia wygrała ostatni ważny mecz H2H (finał Ligi Narodów 06.2025, karne) — czynnik psychologiczny zwiększający wariancję, stąd nadal wąska wygrana (nie szerszy margines) dla Hiszpanii. Nico Williams/Pino nadal wątpliwi (niepotwierdzeni). Brak edge Fortuna (rynek blisko naszej oceny).

**Kontynuujemy bez zmian:** Argentyna-Egipt (2:0) i Szwajcaria-Kolumbia (0:1) z wczoraj — brak nowych twardych newsów zmieniających ocenę. Zasady 1-23 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Terminarz potwierdzony: R16 kończy się 07.07 (Argentyna-Egipt, Szwajcaria-Kolumbia), **08.07 dzień przerwy bez meczów**, ćwierćfinały startują 09.07. Pościg top3: tabela kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce); dzisiejszy spot dźwigni to właśnie odwrócony typ USA-Belgia (jeśli pole utknęło na "starym" Baloguna-zawieszony USA-Belgia, nasza świeża korekta na USA daje przewagę informacyjną).

---

## 2026-07-05 — v1.26 (R16 w toku: 2× tendencja trafiona, mismatch amplifikacja ponownie zaniżona; nowe typy na Argentynę-Egipt i Szwajcarię-Kolumbię)

**Wyniki 04.07 (R16, dzień 1):**
- Kanada **0:3** Maroko — typ 1:2 (Maroko wyg. wąsko): tendencja ✓ (**+2 pkt**, różnica bramek chybiona — model +1, faktyczna +3). Ounahi dublet (w tym wolny z 50m) + gol w doliczonym czasie. Kolejna mismatch amplifikacja (zasada 2/10) — Kanada pierwszym gospodarzem odpadającym w 1/8.
- Paragwaj **0:1** Francja — typ 3:1: tendencja ✓ (**+2 pkt**, różnica bramek chybiona — model +2, faktyczna +1). Mbappé karny 68' (VAR, faul na Dou). Paragwaj po dramatycznych karnych z Niemcami zagrał dyscyplinie obronnej (zasada 20) — tylko 1 stracony, model spodziewał się więcej goli u Francji.

**Bilans dnia 04.07:** kicktipp +4 pkt (2+2). Fortuna 0 PLN (brak zakładów na te mecze).
**Łącznie:** 107 pkt kicktipp, 959.97 PLN bankroll (ROI -4.0%). Jednostka 1u = 19.20 PLN.

**Lekcja (mismatch amplifikacja działa w OBIE strony w pucharach):** Kanada-Maroko potwierdza zasadę 2/10 (Maroko rozjechało bardziej niż nasz margines +1), ale Paragwaj-Francja pokazuje zasadę 20 w akcji (dyscyplina obronna pucharowa ograniczyła oczekiwane gole Francji) — dwa przeciwstawne efekty w jednym dniu, obie tendencje trafione. Wniosek: w trybie pucharowym priorytet to TENDENCJA (2 pkt pewne), margines to premia zmienna zależna od konkretnego stylu rywala (dyscyplina obronna vs otwarta wymiana ciosów).

**Dziś (05.07, R16 dzień 2) — kontynuacja typów bez zmian, ale ze świeżymi newsami:**
- Brazylia–Norwegia (16:00 ET/22:00 CEST, MetLife Stadium NJ): typ **2:1** — bez zmian. NOWA twarda informacja: **Lucas Paquetá POTWIERDZONY nieobecny** (uraz uda z meczu z Japonią, dodatkowo do wcześniej potwierdzonego Militão) — Ancelotti potwierdza Neymara jako w pełni zdrowego i typowanego do wyjściowej 11 w miejsce Paquety. Casemiro (strzelec w R32) zszedł "ostrożnie" z boiska, ale bez oficjalnego komunikatu o kontuzji. Rynek: Brazylia do awansu ~73% (FanDuel), BTTS ok. 60% (rozbieżne kursy 11-10 do 1.67 zależnie od bukmachera). Osłabiona obrona Brazylii (Militão+ryzyko Casemiro) wzmacnia sens zakładu BTTS.
- Meksyk–Anglia (~20:00 ET/02:00 CEST 06.07, Estadio Azteca): typ **1:0** — bez zmian, dodatkowo wzmocniony: **Reece James (prawy obrońca Anglii) POTWIERDZONY mało prawdopodobny do startu** (uraz mięśnia dwugłowego uda) — kolejny konkretny czynnik osłabiający obronę Anglii na spocie dźwigni pościgu. Saka nie kontuzjowany, ale zarządzany ostrożnie (Achilles). Tuchel ponownie w mediach tego tygodnia: "niemożliwe fizycznie zaadaptować się" do wysokości w 4 dni. Rynek do awansu: Anglia ~60-64% (książki), nasz model podbija Meksyk do ~52% z powodu fortecy Azteca (10/10 niepokonani z drużynami MŚ).

**NOWE typy (R16 dzień 4, 07.07 — mecze wchodzące dziś w okno lookahead):**
- Argentyna–Egipt (Atlanta, ~12:00 ET): typ **2:0** — Argentyna ogromny faworyt do awansu (szac. ~85% wg rynku -800/+520), Messi potwierdzony zdrowy, lider strzelców (7 goli), Argentyna 3 czyste konta w grupie. Egipt: Salah gra mimo wcześniejszego naderwania mięśnia (brak nowego pogorszenia), ale Egipt wyszedł z R32 PO KARNYCH (Australia, 120 min + rzuty karne) — większy deficyt regeneracji niż Argentyna (wygrana w dogrywce bez karnych). Egipt pokazał dyscyplinę obronną (1 stracony w 120 min) → umiarkowany mismatch (nie ekstremalny), stąd 2:0 zamiast 3:0.
- Szwajcaria–Kolumbia (Vancouver, ~16:00 ET): typ **0:1** (Kolumbia wygrywa wąsko) — mecz blisko wyrównany, Kolumbia lekki faworyt do awansu (de-vig szac. ~59%). Kolumbia ma najlepszą defensywę turnieju (1 stracony gol w 4 meczach), ale skromny atak (głównie wąskie 1:0). Szwajcaria traci gola w PRAWIE każdym meczu (3/3 w grupie, czyste konto dopiero w R32 vs Algierią) — przewaga defensywna Kolumbii > przewaga ofensywna Szwajcarii. Rynek Under 2.5 faworyzowany (~62%) → niskobramkowo, zgodnie z zasadą 6P.3 (niskobramkowo → margines +1 = wąska 1-bramkowa wygrana).

**Fortuna dziś:** Brak nowych zakładów — Argentyna-Egipt (faworyt zbyt oczywisty, rynek już wycenia ryzyko Salaha/zmęczenia Egiptu, brak wyraźnego rozjazdu) i Szwajcaria-Kolumbia (nasza ocena ~59% blisko rynkowych ~58-61%, brak edge ≥5%) nie spełniają progu — zgodnie z zasadą "brak value to OK". Istniejące pozycje pozostają otwarte: Brazylia-Norwegia BTTS Tak @1.78 (1u), Meksyk-Anglia wygrana @3.55 (1u), USA-Belgia awans @2.05 (1u, mecz 06.07) — WERYFIKUJ aktualne kursy na efortuna.pl przed postawieniem.

**Kontynuujemy:** Zasady 1–21 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Pościg top3: aktywne spoty dźwigni w oknie to Meksyk-Anglia (kontuzje osłabiające obronę Anglii) i USA-Belgia (zawieszenie Baloguna) — reszta meczów pod max EV z profilem dyscypliny obronnej/ofensywnej rywala. Tabela ligi kicktipp.pl nadal niedostępna (403) — ostatnia znana pozycja z 29.06 (5. miejsce).

---

## 2026-07-04 — v1.25 (R32 zakończone: Egipt sensacyjnie awansuje na karnych, Argentyna o włos unika upsetu; nowe typy R16 na Portugalię-Hiszpanię i USA-Belgię)

**Wyniki 03.07 (ostatni dzień R32):**
- Australia **1:1** Egipt (dogrywka, karne 4:2 dla Egiptu) — typ 1:0 (Australia wyg.): **CHYBIONY (0 pkt)**. Egipt odrobił własnego gola (Hany, samobój 55') i wygrał w karnych (Ryan wszedł w 119', nie obronił żadnej jedenastki) — pierwsze zwycięstwo Egiptu w fazie pucharowej MŚ. Fortuna Australia wyg. (90 min) @3.25 → **PRZEGRANA (-20.00 PLN)**, bo mecz był remisem po 90 min (dopiero karne rozstrzygnęły).
- Argentyna **3:2** Zielony Przylądek (po dogrywce) — typ 3:0 (Argentyna wyg.): tendencja ✓ (**+2 pkt**, różnica bramek i exact chybione). Messi otworzył wynik (20. gol na MŚ), ale Zielony Przylądek dwukrotnie doprowadzał do remisu — Argentyna o włos uniknęła jednej z największych sensacji w historii turnieju (samobój Diney Borgesa w dogrywce zdecydował).
- Kolumbia **1:0** Ghana — typ 2:0 (Kolumbia wyg.): tendencja ✓ (**+2 pkt**, różnica bramek chybiona). Arias trafił wcześnie po podaniu Suareza, Ghana 0 celnych strzałów w całym meczu.

**Bilans dnia 03.07:** kicktipp +4 pkt (0+2+2). Fortuna -20.00 PLN (Australia 90-min ML przegrana).
**Łącznie:** 103 pkt kicktipp, 959.97 PLN bankroll (ROI -4.0%). Jednostka 1u = 19.20 PLN.

**Lekcja (kolejne potwierdzenie zasady 19 — R32 to chaos, i zasady o rynkach "90 min" w pucharach):** Egipt to trzecia drużyna w tym R32, która wygrywa dopiero w karnych po remisie z regulaminowego czasu (po Niemczech-Paragwaju i Holandii-Maroku odwrotnie tym razem to "słabszy" na papierze zespół awansuje). Ważniejsza lekcja techniczna: zakład Fortuna "wygrana (90 min)" to INNY rynek niż "awans/to qualify" — w R32 różnica jest krytyczna, bo mecz 50/50 kończący się remisem w regulaminowym czasie zawsze przegrywa zakład na "wygraną 90 min", niezależnie od tego, kto wygra karne. Od teraz przy niepewnych meczach pucharowych preferuj rynek "awans/to qualify" (rekomendacja z playbooka 6P już to sugerowała — dziś boleśnie potwierdzona).

**R32 zamknięte. Startuje pełne okno R16 (04-06.07, 6 meczów):**
- Kanada–Maroko (04.07, R16, 13:00 ET/19:00 CEST, Houston): typ **1:2** (Maroko awansuje) — bez zmian, Maroko umiarkowany faworyt (devig ~51%/26%/21%), brak nowych newsów kontuzyjnych.
- Francja–Paragwaj (04.07, R16, 17:00 ET/23:00 CEST, Filadelfia): typ **3:1** — bez zmian, Francja zdecydowany faworyt (devig 90% do awansu), Alderete (CB Paragwaju) nadal wątpliwy/niepełny trening (najnowszy cytat trenera Alfaro), ale nie potwierdzona nieobecność.
- Brazylia–Norwegia (05.07, R16, 16:00 ET/22:00 CEST, MetLife): typ **2:1** — bez zmian, ale **Éder Militão (CB Brazylii) POTWIERDZONY niedostępny** (nowa twarda informacja) — osłabia defensywę Brazylii, wzmacnia sens zakładu BTTS. Haaland nadal w hicie formy (5 goli/3 mecze).
- Meksyk–Anglia (05.07, R16, ~19:00 ET/01:00 CEST 06.07, Azteca): typ **1:0** — bez zmian, dodatkowo wzmocniony: Stones i Saka pod znakiem zapytania (Anglia), Tuchel z ograniczonymi opcjami na prawej obronie — kolejny argument za spotem dźwigni na Meksyk (wysokość + forma osłabień Anglii).
- **NOWY: Portugalia–Hiszpania** (06.07, R16, 15:00 ET/21:00 CEST, Dallas): typ **0:1** (Hiszpania wyg. wąsko) — rewanż finału Ligi Narodów, Hiszpania umiarkowany faworyt (90-min devig ~50%, do awansu ~65%), rynek Under 2.5 (-120) sugeruje niskobramkowy, nerwowy mecz pucharowy mimo jakości ofensywnej (Yamal, Ronaldo). Ronaldo potwierdzony zdrowy; Nico Williams/Pino (Hiszpania) wątpliwi po urazach z Urugwaju.
- **NOWY: USA–Belgia** (06.07, R16, 20:00 ET/02:00 CEST 07.07, Seattle): typ **1:2** (Belgia wyg. wąsko) — mecz bliski 50/50 (advance-devig USA ~54%/Belgia ~46%), ale **Balogun (najlepszy strzelec USA) ZAWIESZONY** (czerwona kartka z meczu z Bośnią) — realne osłabienie ataku USA, przechyla nasz model ku Belgii mimo rynkowego faworyta USA. Belgia po heroicznym comebacku z Senegalem (De Bruyne/Lukaku dostępni, zarządzani ostrożnie po kontuzjach).

**Fortuna dziś/lookahead:** USA-Belgia "awans/to qualify" Belgia @ szac. 2.05, edge ~8.7% (Balogun zawieszony to konkretny, potwierdzony czynnik nieuwzględniony w pełni przez rynek) — 1u (19.20 PLN), **rynek "awans" nie "90 min"** (lekcja z dzisiejszego rozliczenia). WERYFIKUJ kurs na efortuna.pl. Portugalia-Hiszpania: brak potwierdzonego kursu Fortuny w researchu + edge na granicy progu (~5%) — pomijamy zgodnie z zasadą "brak value to OK".

**Kontynuujemy:** Zasady 1–20 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Nowa zasada 21 (rynek 90-min ≠ awans w pucharach, patrz wyżej). Pościg top3: 2 spoty dźwigni w oknie (Meksyk-Anglia kontynuacja, USA-Belgia nowy przez konkretną kontuzję/zawieszenie — nie czysty fade). Tabela ligi kicktipp.pl nadal niedostępna (403 + brak w indeksie wyszukiwarki) — ostatnia znana pozycja z 29.06 (5. miejsce).

---

## 2026-07-03 — v1.24 (R32 finał: exact Portugalia, ale BTTS Szwajcaria-Algieria padł na dyscyplinie obronnej pucharowej; nowa zasada 20)

**Wyniki 02.07 (R32):**
- Hiszpania **3:0** Austria — typ 2:0: tendencja ✓ (**+2 pkt**). Oyarzabal dublet, Porro. Kolejna mismatch amplifikacja (model 2:0, fakt. 3:0) — zasada 10 nadal w mocy.
- Portugalia **2:1** Chorwacja — typ 2:1: **EXACT ✓ (+4 pkt!)**. Ronaldo karny 68', G.Ramos 94' po tym jak Perisic dał prowadzenie Chorwacji 53'. Model idealnie złapał "umiarkowany faworyt + leaky rywal = wąska wygrana z golem przeciwnika".
- Szwajcaria **2:0** Algieria — typ 2:1: tendencja ✓ (**+2 pkt**, różnica bramek chybiona). Embolo 10', Ndoye 46'. Fortuna BTTS Tak @1.87 → **PRZEGRANA (-20.00 PLN)** — Algieria (Mahrez w formie) nie strzeliła wcale, mimo że "Szwajcaria traci gole w KAŻDYM meczu grupy" — tym razem czyste konto.

**Bilans dnia 02.07:** kicktipp +8 pkt (2+4+2). Fortuna -20.00 PLN (BTTS chybiony).
**Łącznie:** 99 pkt kicktipp, 979.97 PLN bankroll (ROI -2.0%). Jednostka 1u = 19.60 PLN.

**Nowa zasada 20 — dyscyplina obronna pucharowa łamie trendy grupowe:** Szwajcaria "traciła gole w każdym meczu grupy" (trend grupowy), ale w R32 (wyższa stawka, eliminacja) zagrała dyscyplinie i utrzymała czyste konto. Lekcja: NIE ekstrapoluj trendów "leaky defense"/BTTS z fazy grupowej wprost na rundy pucharowe bez dyskontu — drużyny często zacieśniają organizację defensywną, gdy stawką jest odpadnięcie. Traktuj grupowe % BTTS/GA jako punkt wyjścia, ale obniż wagę o ok. 10-15 pkt proc. w R32+, chyba że newsy potwierdzają identyczne osłabienia defensywne (kontuzje kluczowych obrońców) co w grupie.

**Dziś (03.07, dokończenie R32) + lookahead do 05.07 (R16 startuje 04.07) — 5 meczów w oknie:**
- Australia–Egipt (03.07, 14:00 ET/20:00 CEST): typ **1:0** — kontynuacja z wczoraj, Salah nadal wątpliwy (naderwanie dwugłowego uda, rosnący optymizm po treningu w środę, ale start niepotwierdzony). Spot dźwigni dnia.
- Argentyna–Zielony Przylądek (03.07, 18:00 ET/00:00 CEST): typ **3:0** — Messi lider strzelców turnieju (6 goli), Zielony Przylądek najmniejsza reprezentacja w historii fazy pucharowej MŚ.
- Kolumbia–Ghana (03.07, 21:30 ET/03:30 CEST): typ **2:0** — Kudus POTWIERDZONY nieobecny (uraz czworogłowego), Ghana tylko 2 gole w 3 meczach grupy.
- Kanada–Maroko (04.07, R16, 13:00 ET/19:00 CEST): typ **1:2** — bez zmian z wczoraj.
- Francja–Paragwaj (04.07, R16, 17:00 ET/23:00 CEST): typ **3:1** — bez zmian z wczoraj.

**Nowe typy dziś na mecze wchodzące w okno lookahead (05.07, R16 dzień 2):**
- Brazylia–Norwegia (05.07, 16:00 ET/22:00 CEST, MetLife Stadium NJ): typ **2:1** — Brazylia umiarkowany faworyt (~64% do awansu), Paqueta zagrożony końcem turnieju, Neymar na peryferiach formy, ale Vinicius Jr (4 gole w grupie) + Martinelli w formie. Haaland (Norwegia) w hicie formy (5 goli, trafia w 13 kolejnych meczach kadry) — zasada 9 (snajper > draw_bias) nieistotna w pucharach (brak remisów), ale sygnalizuje realne zagrożenie kontrą. Rynek: BTTS ~56%, Over 2.5 faworyzowane.
- Meksyk–Anglia (05.07, 20:00 ET/02:00 CEST 06.07, Estadio Azteca): typ **1:0** — **SPOT DŹWIGNI RUNDY** (pościg top3): Estadio Azteca 2240m n.p.m., Tuchel wprost: Anglia "nie może fizycznie zaadaptować się" w 4 dni. Meksyk niepokonany z drużynami MŚ na tym stadionie w 10 próbach (89 meczów/13 lat, tylko 2 porażki), 0 goli straconych w całym turnieju. Rynek daje Meksykowi ~28% w 90 min / ~41% do awansu (double chance) — nasz model podbija do ~32%/52% z powodu udokumentowanego czynnika wysokości. Pole prawdopodobnie bierze markową Anglię (Kane w formie) — to nasza dźwignia.

**Fortuna dziś/lookahead:** Brazylia-Norwegia BTTS Tak @ szac. 1.78, edge ~10,4% (obie ofensywy w formie) — 1u (19.60 PLN). Meksyk wygrana (90 min) @ szac. 3.55, edge ~13,6% (forteca Azteca + wysokość) — 1u (19.60 PLN, konserwatywnie mimo wyższego wyliczonego edge — pojedynczy mecz pucharowy, wysoka wariancja). WERYFIKUJ oba kursy na efortuna.pl przed postawieniem.

**Kontynuujemy:** Zasady 1–20 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) do końca turnieju. Pościg top3: dziś/jutro 2 spoty dźwigni (Australia-Egipt kontynuacja, Meksyk-Anglia nowy) — reszta meczów pod max EV z profilem ofensywnym faworyta. Tabela ligi kicktipp.pl nadal niedostępna dla WebFetch (403) — ostatnia znana pozycja z 29.06 (5. miejsce).

---

## 2026-07-02 — v1.23 (pościg-upset chybił u Belgii, ale BTTS uratował dzień; R32 kończy się 3.07, R16 startuje 4.07)

**Wyniki 01.07 (dokończenie R32):**
- Anglia **2:1** DR Kongo — typ 2:0: tendencja ✓ (**+2 pkt**). Kane x2 w końcówce (w tym gol w 90+4), DR Kongo prowadziło do 76'.
- Belgia **3:2** Senegal (AET, karny Tielemans 125') — typ 1:2 (upset Senegalu, spot dźwigni pościgu): **PRZEGRANA 0 pkt**. Belgia odrobiła straty 0:2 golami w 86'/89', a w dogrywce wygrała kontrowersyjnym karnym. Fortuna BTTS Tak @1.90 → **WON +8.92 PLN** (2:2 było już po 90 min, więc BTTS spełniony niezależnie od wyniku pucharowego).
- USA **2:0** Bośnia i Hercegowina (Balogun czerwona kartka) — typ 3:1: tendencja + różnica bramek ✓ (**+3 pkt**).

**Bilans dnia 01.07:** kicktipp +5 pkt (2+0+3). Fortuna +8.92 PLN (BTTS trafiony).
**Łącznie:** 91 pkt kicktipp, 999.97 PLN bankroll (ROI ~0%, praktyczny break-even). Jednostka 1u = 20.00 PLN.

**Lekcja (dźwignia pościgu ma dwustronną wariancję):** Belgia-Senegal był naszym najlepszym spotem dźwigni dnia (mecz ~44-55%), ale osłabiony faworyt (bez Debasta, Lukaku niepełnosprawny) i tak znalazł drogę do zwycięstwa w dogrywce. To potwierdza zasadę 19 (R32 jest chaosem) w drugą stronę — czasem to faworyt wygrywa dramatycznie, nie underdog. Dźwignia w pościgu pozostaje uzasadniona (asymetria: duży zysk przy trafieniu, mały koszt przy chybieniu w tabeli), ale świadomie akceptujemy wyższą wariancję pojedynczego wyniku. Osobny cel Fortuny (BTTS, niezależny od kierunku wygranej) okazał się dobrym zabezpieczeniem — rynki niezależne od tendencji warto premiować przy wysokiej niepewności kierunkowej.

**Dziś (02.07) + lookahead do 04.07 — 8 meczów (R32 kończy się 3.07, R16 startuje 4.07):**
- Hiszpania–Austria (02.07, 15:00 ET/21:00 CEST): **2:0** — wyraźny faworyt (~82% do awansu), 0 goli straconych w grupie.
- Portugalia–Chorwacja (02.07, 19:00 ET/01:00 CEST): **2:1** — Ronaldo potwierdzony zdrowy, Chorwacja leaky (BTTS blisko coinflip).
- Szwajcaria–Algieria (02.07, 23:00 ET/05:00 CEST): **2:1** — Szwajcaria traci gole w każdym meczu, Algieria najsłabsza defensywa 1/16 ale Mahrez w formie.
- Australia–Egipt (03.07, 14:00 ET/20:00 CEST): **1:0** — SPOT DŹWIGNI DNIA (najbliższy 50/50: ~47/53), Salah wątpliwy (uraz uda, niepotwierdzony start).
- Argentyna–Zielony Przylądek (03.07, 18:00 ET/00:00 CEST): **3:0** — Messi w hicie formy (hattrick, rekord Klose), mismatch amplifikacja.
- Kolumbia–Ghana (03.07, 21:30 ET/03:30 CEST): **2:0** — Ghana bez Kudusa (potwierdzone), Kolumbia tylko 1 gol stracony w grupie.
- Kanada–Maroko (04.07, 13:00 ET/19:00 CEST, R16): **1:2** — Maroko niepokonane z Kanadą historycznie, ale gra 4 dni po dogrywce+karnych (szac. zmęczenie) vs gospodarz z pełnym odpoczynkiem.
- Francja–Paragwaj (04.07, 17:00 ET/23:00 CEST, R16): **3:1** — Mbappé w hicie formy, Paragwaj po dramatycznych karnych z Niemcami.

**Fortuna dziś:** Australia wygrana (90 min) @ szac. 3.25, edge ~10,5% (Salah wątpliwy) — 1u (20 PLN). Szwajcaria–Algieria BTTS Tak @ szac. 1.87, edge ~12,2% (Szwajcaria traci gole zawsze, Algieria strzela regularnie) — 1u (20 PLN). WERYFIKUJ oba kursy na efortuna.pl przed postawieniem.

**Kontynuujemy:** Zasady 1–19 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY) dla reszty turnieju. Pościg top3: dziś 1 spot dźwigni (Australia-Egipt), reszta meczów typowana pod max EV z profilem ofensywnym faworyta.

---

## 2026-07-01 — v1.22 (dobry dzień R32: 2 tendencje trafione, 1 chybiona goal_diff nie zaszkodziła; kontynuacja pościgu)

**Wyniki 30.06 (R32, dokończenie dnia):**
- WKŚ **1:2** Norwegia — typ 0:1: tendencja + różnica bramek ✓ (**+3 pkt**). Haaland 86' decydujący (5. gol turnieju), Norwegia zdała egzamin mimo wyrównania WKŚ w 74'. Fortuna Norwegia wygrana @2.10 → **WON +20.85 PLN**.
- Francja **3:0** Szwecja — typ 3:1: tendencja ✓ (+2 pkt, różnica bramek chybiona — model dał +2, faktyczna +3). Mbappé x2, Barcola. Francja rozjechała mocniej niż zakładaliśmy — kolejny przypadek mismatch amplifikacji (zasada 2/10).
- Meksyk **2:0** Ekwador — typ 1:0: tendencja ✓ (+2 pkt, różnica bramek chybiona — model +1, faktyczna +2). Quiñones + Jiménez. Fortuna Meksyk wygrana @2.20 → **WON +22.74 PLN**.

**Bilans dnia 30.06:** kicktipp +7 pkt (3+2+2). Fortuna +43.59 PLN (obie stawki trafione).
**Łącznie:** 86 pkt kicktipp, 991.05 PLN bankroll (ROI -0.9%, znaczna poprawa z -5.3%). Jednostka 1u = 19.82 PLN.

**Lekcja potwierdzona (mismatch amplifikacja x2 w jednym dniu):** FRA i MEX obie wygrały większą różnicą niż model. Kontynuujemy zasadę: przy λ_rywala < 0.6 rozważ +1 gol do typu w R32, zwłaszcza gdy faworyt ma real formę ofensywną i rywal nie ma bramkarza-bohatera.

**Dziś (01.07) — 3 mecze R32 (dokończenie rundy, R16 startuje dopiero 4.07):**
- Anglia vs DR Kongo (12:00 ET/18:00 CEST, Atlanta): typ **2:0** — Anglia wyraźny faworyt (Opta 73.9%), James+Quansah OUT ale Rice wraca; DR Kongo niski blok + kontra (Wissa). Rynek: Under 2.5 + BTTS Nie faworyzowane → czyste konto ENG prawdopodobne. Pościg: różnicujemy od tłumowego 2:1.
- Belgia vs Senegal (16:00 ET/22:00 CEST, Seattle): typ **1:2 (upset Senegalu)** — mecz naprawdę wyrównany (Belgia ~44-55% w zależności od źródła kursu), Belgia bez Debasta i z niepełnosprawnym Lukaku, Senegal bez Mendy'ego (Diaw w bramce) ale z jakością w ataku (I.Sarr, Mane, Ndiaye). To NAJLEPSZY spot dźwigni dnia w trybie pościgu (gonimy top3, 5. miejsce) — pole niemal na pewno bierze Belgię.
- USA vs Bośnia i Hercegowina (20:00 ET/02:00 CEST, Santa Clara): typ **3:1** — USA wyraźny faworyt (~74-90% do awansu), Pulisic wraca do wyjściowej 11, gospodarz. Bośnia: Muharemović wraca z zawieszenia, ale Dzeko/Demirović dają kontrę. Rynek: Over 2.5 + BTTS blisko coinflip (USA tylko 1 czyste konto w 11 meczach!) → gole obu stron prawdopodobne.

**Fortuna dziś:** BTTS Tak (Belgia-Senegal) @ szac. 1.90 (WERYFIKUJ efortuna.pl), edge szac. ~7.4% — obie defensywy osłabione kontuzjami (Debast/Mendy), obie ofensywy z jakością. 0.5u (9.91 PLN). Anglia-DR Kongo i USA-Bośnia: brak edge ≥5% wobec silnych faworytów rynkowych (public heavily na USA) — pomijamy zgodnie z zasadą 3 (nie obstawiaj przeciw dominującemu faworytowi bez realnego sygnału).

**Kontynuujemy:** Zasady 1–19 w mocy, tryb pucharowy aktywny (draw_bias WYŁĄCZONY do końca turnieju). Pościg: nadal ok. 5. miejsce (ostatnia znana pozycja z 29.06 — tabela kicktipp.pl niedostępna dla WebFetch, 403), różnicujemy selektywnie (1 spot dźwigni: Senegal dziś).

---

## 2026-06-30 — v1.21 (R32: 2 sensacje dzień → chaos; Brazil exact; pościg kontynuowany)

**Wyniki 29.06 (R32):**
- Brazylia **2:1** Japonia — typ 2:1 (Brazylia wyg.): **EXACT ✓ (+4 pkt!)**. Martinelli 90+2'. Model trafił perfekcyjnie.
- Niemcy **1:1** Paragwaj AET → Paragwaj **4-3 karny** — typ 2:0 (Niemcy wyg.): PRZEGRANA 0 pkt. Ogromna sensacja! Enciso 42', Havertz wyrównał. Paragwaj wygrał karne (goalkeeper Gill hero). Wynik końcowy: 4:5 (agg).
- Holandia **1:1** Maroko AET → Maroko **3-2 karny** — typ 2:1 (Holandia wyg.): PRZEGRANA 0 pkt. Gakpo 72', Issa Diop 91'. Maroko awansuje (Bounou hero). Wynik końcowy: 3:4 (agg).

**Bilans dnia 29.06:** kicktipp +4 pkt (1 exact). Fortuna 0 PLN (nie logowano zakładów).
**Łącznie:** 79 pkt kicktipp, 947.46 PLN bankroll (ROI -5.3%). Jednostka 1u = 18.95 PLN.

**NOWA zasada 19 — R32 jest chaosem: silni faworyci padają:**
Niemcy (top-10 FIFA) i Holandia (top-5 FIFA) odpadli w tym samym dniu. W R32 upsets są realną normą — żaden typ na faworyta w karnych nie jest "pewny". Konsekwencje:
1. **W pościgu R32**: ostrożniej typuj outright favors, chyba że masz konkretny powód (forma/kontuzje wyraźne)
2. **Pościg leverage w R32**: szansa na podbicie jest DUŻA (upset = skaczysz nad całym polem). Upsets w R32 to nie rarytety — to regularność turnieju.
3. **Wyraźny faworyt z realną formą** (jak FRA vs SWE) = nadal typuj faworyta z odpowiednim marginesem. Ale "po papierze dobry faworyt + obrońca w formie" = flaguj niepewność.

**Dziś (30.06) — typy R32:**
- WKŚ vs Norwegia @ 19:00 CEST: NOR **0:1** (Norwegia wygrywa 1:0) — cagey/defensive match, Haaland zdrowy, CIV z niskim blokiem (2 czyste konta). Pościg: diferenciacja od popularnego 0:2.
- Francja vs Szwecja @ 23:00 CEST: FRA **3:1** — Francja dominant (avg 3.33 gola/mecz, 10-2 GD), Szwecja leaky (7 straconych). Gyokeres/Isak strzeli 1. Pościg: 3:1 vs tłumowe 2:1 (jeśli FRA wygra różnicą 2).
- Meksyk vs Ekwador @ 03:00 CEST (1.07): MEX **1:0** — Azteca 2240m, MEX perfekcyjny (6G 0 straconych), O/U=1.5 (niskobramkowy), λ_MEX=0.9 λ_ECU=0.58 → P(1:0)=20.5% najwyższy.

**Fortuna dziś (WERYFIKUJ efortuna.pl przed postawieniem):**
- NOR wygrana (90 min) vs WKŚ @ szac. 2.10 → 1u (19 PLN), szac. edge ~9%
- MEX wygrana (90 min) vs ECU @ szac. 2.20 → 1u (19 PLN), szac. edge ~10%

**Kontynuujemy:** Zasady 1–19 w mocy. Tryb pucharowy aktywny. Pościg: nadal 5. miejsce (stan przed dzisiejszymi meczami), różnicujemy selektywnie.

---

## 2026-06-29 — v1.20 (TRYB POŚCIGU: gramy o MIEJSCE w tabeli, nie o sumę punktów)

Użytkownik jest **5. (R=146), traci 5 pkt do top3**, a koledzy typują bezpiecznie/podobnie →
kopiowanie pola = utknięcie w środku. Cel = **pozycja (top3)**, nie suma punktów. Dodany **krok 6C**
(contest leverage):
- **gonisz** → RÓŻNICUJ się selektywnie: **upset** na meczach ~50/50, gdzie pole jest na faworycie
  (maks. dźwignia); **inny-prawdopodobny-wynik** w mismatchach (2:0 zamiast tłumowego 2:1);
  1–2 spoty dźwigni na rundę, NIE blanket-kontra.
- **prowadzisz** → kopiuj konsensus (chroń pozycję, blokuj goniących).
Świadomy trade-off EV↔wariancja, uzasadniony tylko w pościgu. Config: `kicktipp.objective=top3`, `contest_mode=auto`.

**Dziś (29.06) — pościg, najlepszy spot dźwigni: Holandia–Maroko** (pole na Holandii, realny toss-up)
→ weź **Maroko 1:2** (jak Maroko przejdzie, przeskakujesz wszystkich na Holandii). Brazylia/Niemcy
zostaw faworytami, ale distinct score (Brazylia 2:0, Niemcy 2:0) zamiast tłumowego 2:1.

---

## 2026-06-29 — v1.19 (R32 tryb pucharowy pełny; błąd 0:0 potwierdzony i wyeliminowany; Kanada historycznie 1. zwycięstwo R32)

**Wynik 28.06:**
- RPA **0:1** Kanada — typ 0:0 (remis): **PRZEGRANA 0 pkt**. Eustáquio 90+2' zdecydował. Kanada awansuje po HISTORYCZNYM pierwszym zwycięstwie w fazie pucharowej MŚ. Błąd był podwójny: (a) w R32 remis jest niemożliwy (reguła 6P), (b) nawet patrząc na 90 min, Kanada była lepsza jakościowo. POPRAWNY typ: 0:1 (Kanada 1:0) = co najmniej +2 pkt tendencja, potencjalnie +4 exact!

**Bilans dnia 28.06:** kicktipp 0 pkt. Fortuna 0 PLN (brak zakładów).
**Łącznie:** 75 pkt kicktipp, 947.46 PLN bankroll (ROI -5.3%). Jednostka 1u = 18.95 PLN.

**NOWA zasada 18 — Hardlock trybu pucharowego:**
W R32 i dalej, przed wpisaniem KAŻDEGO typu, wykonaj kontrolę:
1. Czy jesteśmy w fazie pucharowej? (TAK = R32+)
2. draw_bias = WYŁĄCZONY. NIGDY nie wpisuj 0:0 ani 1:1 jako finalnego wyniku.
3. Najpierw ustal TENDENCJĘ (kto awansuje), POTEM margines (+1 standardowo, +2 dla wyraźnego faworyta w 90 min).
Model MUSI odmówić zastosowania draw_bias w trybie pucharowym — to hardlock, nie opcja.

**Lekcja z błędu:** 0:0 był logicznie niemożliwy (liga liczy wynik PO dogrywce i karnych). Byłby to błąd automatycznego zastosowania draw_bias bez sprawdzenia fazy turnieju. Korekta: w playbooku 6P jest to opisane — teraz EGZEKWUJEMY.

**Dziś (29.06) — wszystkie 3 mecze = R32, tryb pucharowy:**
- Brazil 2:1 Japan (Neymar OUT, ale Vinicius+Rodrygo wystarczą; Japan Kubo OUT; lambda_BRA=1.45, lambda_JPN=0.87)
- Germany 2:0 Paraguay (Germany dominuje jakościowo; PAR niski blok, brak grozy ofensywnej; Schlotterbeck OUT ale Rudiger wystarczy)
- Netherlands 2:1 Morocco (NED 5:1 Szwecja = forma; MAR defensywne + Hakimi kontra; Timber OUT dla NED)

**Fortuna potencjał (WERYFIKUJ na efortuna.pl przed postawieniem):**
- Japan advance vs Brazil @ szac. ≥2.70 — P(JPN awans) szac. 38-42% (Neymar OUT = realna szansa); edge szac. ~8-15% jeśli odds ≥2.70.
- Morocco advance vs Netherlands @ szac. ≥2.30 — P(MAR awans) szac. 40-45% (defensive quality + Timber OUT); edge szac. ~5-10% jeśli odds ≥2.30.
- MEX @ szac. ~2.10 vs ECU (30.06, Azteca 2200m) — flagowane wczoraj, szac. edge ~9-20%. Meksyk ma przewagę domową (Azteca, wysokość, kibice) + ECU z niskim rankingiem. WERYFIKUJ jutro rano.
- NOR @ szac. ~2.05 vs CIV (30.06) — flagowane wczoraj, szac. edge ~6%. Haaland w formie (4 gole w turnieju). WERYFIKUJ jutro.

**Kontynuujemy:** Zasady 1–18 w mocy. Tryb pucharowy aktywny dla WSZYSTKICH pozostałych meczów turnieju.

---

## 2026-06-28 — v1.18 (POTWIERDZONE zasady pucharowe: wynik liczony PO dogrywce I karnych)

Użytkownik potwierdził regułę ligi dla fazy pucharowej (pytanie z v1.17 rozstrzygnięte):
**liczony jest wynik po dogrywce I karnych** — wszystkie bramki dogrywki + karne doliczone.
Przykład: 2:2 po dogrywce, 5:4 w karnych → zapisany wynik **7:6**.

Konsekwencje (dodane do playbooka — krok **6P, tryb pucharowy**):
- **BRAK REMISÓW** w wyniku końcowym → `draw_bias` WYŁĄCZONY, NIE typujemy 1:1/0:0.
  (Błąd do korekty: dzisiejszy typ „RPA 0:0 Kanada" jest w pucharach NIEMOŻLIWY — trzeba wskazać zwycięzcę!)
- Najpierw **tendencja** (kto awansuje); archetypy grupowe znikają — wracamy do jakości/formy/kontuzji.
- **Margines domyślnie +1** (2:1, lub 1:0 niskobramkowo) — łapie i wąską wygraną w 90', i karne
  (5:4 / 4:3 / nagła śmierć = zawsze +1). Napompowanego exact (7:6) się nie trafi → celuj w tendencję + różnicę.
- Wyraźny faworyt mogący rozstrzygnąć w 90 min → większy margines (2:0 / 3:1).
- Fortuna: rynki „awans/to qualify" lub wynik po 90 min (tam remis 1X2 nadal istnieje).

---

## 2026-06-28 — v1.17 (start Rundy Pucharowej: brak dead-rubberów, powrót do jakości; Austria 3:3 Algieria = B potwierdzone; Under CRO/GHA chybiony)

**Wyniki 27.06 (ostatni dzień fazy grupowej):**
- Panama **0:2** Anglia — typ 0:3 (Anglia wyg.): tendencja ✓ (+2 pkt). Anglia wygrała, ale skromniej niż model (my 0:3, fakt. 0:2). Mismatch amplifikacja tym razem nie zadziałała.
- Chorwacja **2:1** Ghana — typ 1:1 (remis): CHYBIONY (0 pkt). Chorwacja potrzebowała wygranej — archetyp D. Błąd: draw_bias nudge przesłonił motywację CRO.
- Kolumbia **0:0** Portugalia — typ 0:1 (Portugalia wyg.): CHYBIONY (0 pkt). Remis. Kolumbia desperacko broniła się (potrzebowała wyniku), Portugalia nie zmusiła do wygranej. Archetyp D obrońcy skuteczny.
- DR Kongo **3:1** Uzbekistan — typ 1:0 (DRC wyg.): tendencja ✓ (+2 pkt). DRC wygrało, goal diff chybiony (my 1, fakt. 2).
- Jordania **1:3** Argentyna — typ 1:1 (remis): CHYBIONY (0 pkt). Argentyna rozjechała Jordanię. Zasada 13 + zasada 9 (Messi): desperacja słabszego ≠ skuteczność vs dominujący atakujący faworyt.
- Algieria **3:3** Austria — typ 1:1 (remis): tendencja ✓ (+3 pkt!). Dramatyczny remis, archetyp B (remis awansował obie) potwierdzony nawet przy 6 golach.
- Fortuna: Under 2.5 Chorwacja-Ghana @ 1.58 → PRZEGRANA -9.57 PLN (3 gole = Over).

**Bilans dnia 27.06:** kicktipp +7 pkt (2+0+0+2+0+3). Fortuna -9.57 PLN.
**Łącznie:** 75 pkt kicktipp, 947.46 PLN bankroll (ROI -5.3%). Jednostka 1u = 18.95 PLN.

**Nowa zasada 17 — Under w meczu dwóch ofensywnych desperatów = ryzyko:**
CRO vs GHA: obie drużyny musiały wygrać → archetyp C (oba muszą wygrać) = ofensywa, a nie Under. Pod-typy Under działają przy B (niskobramkowy pakt) lub D (jedna drużyna muruje). Przy C (obie atakują) → Over jest naturalny. Błąd: weszliśmy w Under 2.5 przy meczu archetyp C.

**Wejście w Rundę Pucharową (R32):**
- Znikają archetypy grupowe (A/B/C/E — dead rubber, pakt o nieagresji, wyścig bramkowy).
- Każdy mecz = czysta walka o awans. Wracamy do: jakość, forma, kontuzje, taktyka.
- Nowa dynamika: „nerwowość pierwszego KO meczu" (zwłaszcza nowe drużyny jak RPA/Kanada) → bias w stronę ostrożności + Under w pierwszych meczach.
- Mecz R32 trwa 90 min; przy remisie → dogrywka → ewentualnie karne. **KICKTIPP: sprawdź zasady ligi** (czy oceniają po 90 min czy po całości).

**Kontynuujemy:** draw_bias=1.4 (nadal istotny w R32 przy zbliżonych siłach). Zasady 1–17 w mocy.
Dziś: RPA 0:0 Kanada (EP max, Zwane zawieszony, Kone OUT, obie defensywne). Brak value Fortuna dziś.
Lookahead Fortuna: MEX @ ~2.10 vs ECU (30.06, Azteca 2200m) szac. edge ~9-20% — WERYFIKUJ na efortuna.pl.
Lookahead Fortuna: NOR @ ~2.05 vs WKŚ (30.06) szac. edge ~6% — WERYFIKUJ.

---

## 2026-06-27 — v1.16 (lekcja: EXACT Urugwaj-Hisz 0:1; Iran desperacki = remis, nie wygrana; 3. kolejka = archetypy dominują)

**Wyniki 26.06:**
- Norwegia **1:4** Francja — typ 0:2 (Francja wyg.): tendencja ✓ (+2 pkt). Francja rozjechała mocniej niż model (mismatch amplifikacja).
- Senegal **5:0** Irak — typ 2:1 (Senegal wyg.): tendencja ✓ (+2 pkt). Senegal rozjechał Irak zdecydowanie.
- Zielony Przylądek **0:0** Arabia Saudyjska — typ 1:1 (remis): tendencja ✓ (+3 pkt). Remis trafiony (choć typ 0:0 byłby exact). Draw_bias zadziałał.
- Urugwaj **0:1** Hiszpania — typ 0:1: **EXACT ✓ (+4 pkt!)**. Archetyp D idealnie: Urugwaj desperacki atakował, Hiszpania spokojna, strzeliła kontra i broniła.
- Egipt **1:1** Iran — typ 1:0 (Egipt wyg.): CHYBIONY (0 pkt). Iran desperacki zremisował. Fortuna Iran wyg. przegrana (-9.77 PLN).

**Bilans dnia 26.06:** kicktipp +11 pkt (2+2+3+4+0). Fortuna -9.77 PLN.
**Łącznie:** 68 pkt kicktipp, 957.03 PLN bankroll (ROI -4.3%). Jednostka 1u = 19.14 PLN.

**Nowa zasada 15 — Desperacja słabszego przy silnej defensywie rywala = remis (nie wygrana):**
Iran był desperacki (musiał wygrać), ale miał też jakość defensywną. Egipt z 2 obrońcami OUT nie był wystarczająco ofensywny. Wynik: 1:1. Lekcja: przy zakładzie na "drużyna desperacka wygra" sprawdź czy rywal NIE ma mocnej obrony — może efektywnie bronić mimo presji i wystarczyć na remis. Iran-Syria, Iran-Belgia w historii = remisy przy desperacji. Wyjątek: gdy desperacka strona WYRAŹNIE dominuje jakościowo.

**Nowa zasada 16 — 3. kolejka i dead rubbers:** Przy remisach "martwy mecz" (Jordan-ARG, DRC-UZB) typuj ostrożnie (1:1 lub 1:0 faworycie) i UNIKAJ pewnych wyników. Archetyp A = duża niepewność, rezerwy w składzie = wynik losowy.

**Kontynuujemy:** draw_bias=1.4, zasady 1–16 w mocy. Dziś final meczów grupowych: PAR/ENG 0:3, CRO/GHA 1:1, COL/POR 0:1, DRC/UZB 1:0, JOR/ARG 1:1, ALG/AUT 1:1. Fortuna: CRO/GHA Under 2.5 @ szac. 1.58, 0.5u (9.57 PLN), edge szac. ~7%.

---

## 2026-06-26 — v1.15 (lekcja: 3 chybione tendencje z rzędu — TUR, ECU-GER, JPN-SWE; diagnostyka błędów archetypu)

**Wyniki 25.06:**
- Ekwador **2:1** Niemcy — typ 0:2 (Niemcy wyg.): CHYBIONY (0 pkt). Niespodzianka! Niemcy przegrały. Nie sprawdziliśmy dokładnej stawki dla obu drużyn — jeśli Niemcy miały już punkty i mogły rotować, to był archetyp A lub D dla ECU. Lekcja: przed każdym meczem sprawdzaj TABELĘ GROUP, nawet przy "oczywistych" faworytach.
- Curaçao **0:2** WKŚ — typ 0:1 (CIV wyg. 1:0): tendencja ✓ (+2 pkt). Różnica bramek chybiona (my 1, faktyczna 2).
- Japonia **1:1** Szwecja — typ 1:0 (Japonia wyg.): CHYBIONY (0 pkt). Remis. Fortuna Sweden win przegrana (-9.77 PLN). Archetyp D (Sweden musiała wygrać) był poprawny, ale Sweden jakościowo nie wystarczyła.
- Tunezja **1:3** Holandia — typ 0:2 (NED diff 2): tendencja+diff ✓ (+3 pkt). Excellent — margines 2 gole trafiony!
- Turcja **3:2** USA — typ 1:1 (remis): CHYBIONY (0 pkt). Turcja wygrała w ostatnich sekundach. Archetyp błędny — nie była to sytuacja "remis pasuje obu". Turcja była bardziej zmotywowana niż sądziliśmy.
- Paragwaj **0:0** Australia — typ 1:1 (remis): tendencja ✓ (+3 pkt). Remis trafiony mimo różnicy wyniku.

**Bilans dnia 25.06:** kicktipp +8 pkt (0+2+0+3+0+3). Fortuna: -9.77 PLN (Sweden przegrana).
**Łącznie:** 57 pkt kicktipp, 966.80 PLN bankroll (ROI -3.3%).

**Nowa zasada 14 — Sprawdź TABELĘ GRUPY przed każdym typem (krytyczne):**
3 chybione typy z rzędu mają wspólny mianownik: nie sprawdziliśmy dokładnej stawki dla OBIE drużyny przed klasyfikacją archetypu. ECU miał powody by gonić wygraną (desperacja) a GER mógł odpuścić (wystarczało). TUR był zmotywowany (miał powody walczyć), a my zakładaliśmy "remis pasuje obu" bez weryfikacji punktów. Zasada: zanim wpiszesz typ, ZAWSZE sprawdź: (a) ile pkt ma każda drużyna, (b) co daje jej remis/przegrana/wygrana w kontekście tabeli i 3. miejsc. Jeśli masz wątpliwości co do archetypu — sprawdź standings web search, nie zgaduj.

**Dzisiejsze priorytety:** NOR-FRA 0:2, SEN-IRQ 2:1, CPV-KSA 1:1, URU-ESP 0:1, EGY-IRN 1:0.
**Fortuna:** Iran wyg. vs Egypt @ szac. 5.75 (SPRAWDŹ efortuna.pl), 0.5u (9.77 PLN), szac. edge 20-27% — Iran desperacki + Egypt rotacja + 2 obrońcy OUT.
**Kontynuujemy:** draw_bias=1.4, zasady 1–14 w mocy.

---

## 2026-06-25 — v1.14 (lekcja: archetyp B ≠ automatyczny 1:1 gdy faworyt może klinczować; desperacja słabszego ≠ skuteczność)

**Wyniki 24.06:**
- Szwajcaria **2:1** Kanada — typ 1:1: CHYBIONY (0 pkt). Archetyp błędnie sklasyfikowany jako B (remis pasuje obu) — SUI mogła klinczować wygraną, a CAN desperacko potrzebowała wygraj. SUI MIAŁA powód GONIĆ wygraną. Właściwy archetyp: D (asymetria z motywacją SUI do wygranej).
- Bośnia **3:1** Katar — typ 2:0: RÓŻNICA BRAMEK ✓ (+3 pkt). Margines 2 gole trafiony!
- Brazylia **3:0** Szkocja — typ 0:2: tendencja ✓ (+2 pkt). Mismatch amplifikacja: powinniśmy pisać 0:3 (≥1 gol więcej przy λ_rywal<0.5). Szkocja była desperacka ale zbyt słaba.
- Maroko **4:2** Haiti — typ 2:0: RÓŻNICA BRAMEK ✓ (+3 pkt). Ponownie margines 2 gole trafiony!
- Meksyk **3:0** Czechy — typ 1:1: CHYBIONY (0 pkt). Błąd: CZE (0 pkt, desperate) vs MEX (3 pkt, safe) — właściwy archetyp D. Lekcja z v1.6 niewyciągnięta: faworyt z punktami kontruje desperata 1:0 lub mocniej. CZE był za słaby by wymusić cokolwiek.
- RPA **1:0** Korea Płd. — typ 0:1: CHYBIONY (0 pkt). Zła tendencja. RPA miała 0 pkt, KOR miała 0 pkt — oba do-or-die. Błędna ocena względnej jakości.

**Bilans dnia 24.06:** kicktipp +8 pkt (0+3+2+3+0+0). 2× goal_diff w jednym dniu — solidnie!
**Łącznie:** 49 pkt kicktipp, 976.57 PLN bankroll (ROI -2.3%).

**Nowe zasady:**
12. **Archetyp B wymaga symetrii:** „Remis pasuje obu" działa TYLKO gdy OBIE strony mają powód, żeby się zadowolić remisem. Gdy JEDNA strona (nawet niewielki faworyt) może klinczować wygraną i jest silniejsza — to archetyp D, nie B. Sprawdź punkty OBIE drużyn przed klasyfikacją.
13. **Desperacja słabszego ≠ skuteczność:** Gdy desperacka drużyna jest jakościowo znacznie gorsza (np. CZE vs MEX, SCO vs BRA) — desperacja nie pomaga; silniejsza strona wygrywa swobodnie. Obniżaj typ ku wygranej faworyta, nie ku remisowi.

**Dzisiejsze priorytety:** ECU-GER 0:2, CUR-CIV 0:1, JPN-SWE 1:0, TUN-NED 0:2, TUR-USA 1:1, PAR-AUS 1:1.
**Fortuna:** SWE to win @ 4.50, 0.5u (szac. edge ~12–15%), Kubo OUT + Sweden must-win motivation.
**Kontynuujemy:** draw_bias=1.4, reguły 1–13 w mocy.

---

## 2026-06-24 — v1.13 (model STAWKI: 3. kolejka i mecze decydujące)

Na bazie analizy ostatniej kolejki (AbsurDB): w meczach o stawkę MOTYWACJA i kalkulacja tabeli
biją jakość i kursy. Dodany **Krok 2.5** (archetypy stawki) — wchodzi do λ_własne i często dominuje:
- **A) martwy mecz** (oba nic nie grają) → rotacja, losowo, Under, niska pewność, Fortuna PAS;
- **B) remis pasuje obu** → zachowawczy niskobramkowy remis (Gijón '82) → 1:1/0:0 + Under;
- **C) oba muszą wygrać/strzelać** → otwarcie, Over, typ na wygraną;
- **D) asymetria** (jedna potrzebuje, druga bezpieczna / „wystarczy niska porażka") → nudge ku potrzebującej lub murowanie (Under);
- **E) wyścig o różnicę bramek / 3. miejsce** → przeładowana ofensywa (Over).
Plus: drabinka (łatwiejszy rywal w pucharze) = flaga niepewności; ostatnia kolejka grana równolegle.
Mapowanie z analizy: Algieria-Austria = **B** (remis awansuje obu → 1:1, uwaga na pakt à la Gijón),
USA-Turcja = **A** (martwy), Irak-Senegal = **C/E** (gonią bramki → Over), Szkocja-Brazylia = **D**
(Szkocji wystarczy niska porażka → mur/Under), Paragwaj-Australia = **B** (remis = awans obu → nudny).
ZASADA: najpierw ustal scenariusze tabeli (web search), potem typuj.

---

## 2026-06-24 — v1.12 (2× exact = model działa; Ghana beton niszczy Anglię; nowa reguła: defensywna kompresja rywala)

**Wyniki 23.06:**
- Portugalia **5:0** Uzbekistan — typ 3:0: tendencja ✓ (+2 pkt). Mismatch amplifikacja po raz kolejny (model 3:0, rzecz. 5:0). Ronaldo brace.
- Anglia **0:0** Ghana — typ 2:0: CHYBIONY (0 pkt). Ghana zagrała beton (organizacja defensywna, parking the bus). Draw_bias 1.4 powinien był wysunąć 1:1 → dałby 3 pkt. **Lekcja**: λ_ENG≈1.86 był technicznie poprawny, ale Ghana skompresowała przestrzenie. Przed meczem "wyraźny faworyt vs drużyna z historią defensywną" sprawdź xGA i styl rywala.
- Chorwacja **1:0** Panama — typ 0:1: EXACT ✓ (+4 pkt!). Perfekcyjny typ: cagey mecz dwóch desperatów, model trafiony co do bramki.
- Kolumbia **1:0** DR Kongo — typ 1:0: EXACT ✓ (+4 pkt!). Model 1.47:0.68 sprawdził się idealnie.

**Bilans dnia 23.06:** kicktipp +10 pkt (2+0+4+4). 2× exact w jednym dniu — rekord sezonu.
**Łącznie:** 41 pkt kicktipp, 976.57 PLN bankroll (ROI -2.3%).

**Nowa zasada 11 — defensywna kompresja rywala (parking the bus):**
Przed meczem "wyraźny faworyt (λ>1.5) vs drużyna z historią defensywną lub niskim blokiem" (Ghana, Iran, Curaçao, Korea Płd.) sprawdź xGA i styl gry rywala. Jeśli rywal ma styl 5-4-1 / niski blok, albo ich xGA < 1.0/match → obniż λ_faworyta o 10–15% i rozważ 1:0 zamiast 2:0, lub draw_bias może wyłonić 0:0/1:1. Model Poissona nie uwzględnia „parking the bus".

**Dzisiejsze priorytety:** SUI-CAN 1:1, BIH-QAT 2:0, SCO-BRA 0:2, MAR-HAI 2:0, CZE-MEX 1:1, RSA-KOR 0:1.
**Kontynuujemy:** draw_bias=1.4, wszystkie zasady 1–11 w mocy. Kurs na value bety Fortuna dziś niespełniony (brak edge ≥5% przy dostępnych kursach rynkowych).

---

## 2026-06-23 — v1.11 (lekcja: draw_bias nie działa przy dominującym snajperze + mismatch amplifikacja x2)

**Wyniki 22.06:**
- Argentyna **2:0** Austria — typ 1:0: tendencja ✓ (+2 pkt). Mismatch amplifikacja potwierdzona: model 1:0, rzecz. 2:0. Messi 2 gole (rekord WC: 17+18. gol).
- Francja **3:0** Irak — typ 2:0: tendencja ✓ (+2 pkt). Mbappé 2 gole, Dembélé 1. Model 2:0, rzecz. 3:0 — znowu amplifikacja. Mecz opóźniony burzą nad Philadelphią.
- Norwegia **3:2** Senegal — typ 1:1: CHYBIONY (0 pkt). Haaland brace (4 gole w 2 meczach). **Kluczowa lekcja**: draw_bias (1.4) zadziałał jak OVERRIDE przy faworycie ofensywnym z dominującym snajperem. Norwegia nie była pick'em — miała Haalanda "on fire". Typ 1:1 był błędem.
- Jordania **1:2** Algieria — typ 0:1 (Alg wygrywa 1:0): TENDENCJA ✓ + RÓŻNICA -1 TRAFIONA (+3 pkt!). Gouiri 82'. Świetna robota.

**Bilans dnia 22.06:** kicktipp +7 pkt (3×tendencja, 1×diff). Fortuna 0 PLN.
**Łącznie:** 31 pkt kicktipp, 976.57 PLN bankroll (ROI -2.3%).

**Nowe zasady:**
9. **draw_bias NIE nadpisuje dominującego snajpera:** gdy jeden z faworytów ma napastnika "in hot form" (Haaland 4 gole, Kane 3+, Messi) → ignoruj nudge remisu, graj wygraną (tendencja+profil wynikowy). Draw_bias to nudge statystyczny dla "normalnych" meczów, nie kontruje jednostkowego geniusza.
10. **Mismatch amplifikacja stabilna:** ARG 2:0 (model 1:0), FRA 3:0 (model 2:0) — faworyci z atakiem potrafią rozjechać. Dla λ_rywal < 0.6 zawsze rozważ +1 gol w typie (lepiej 3:0 niż 2:0 u wyraźnego faworyta).

**Dzisiejsze priorytety:** POR 3:0 UZB, ENG 2:0 GHA, CRO 0:1 (via PAN), COL 1:0 DRC.
**Kontynuujemy:** draw_bias=1.4 (nudge), reguła snajpera (zasada 9) dodana, mismatch amplifikacja w modelu.

---

## 2026-06-22 — v1.10 (model multi-czynnikowy: nie tylko kursy)

Uwaga użytkownika: decyzje były zakotwiczone w kursach (λ liczone z odds), a czynniki (forma,
kontuzje, taktyka, motywacja, xG) bywały tylko komentarzem, nie ruszały liczb. Zmiana w configu/playbooku:
- buduj DWIE oceny λ: **rynkową** (kursy + O/U) i **własną** (z czynników), i **blenduj** (`model.market_weight`=0.55);
- typ kontra rynkowi + value bierze się z **rozjazdu** obu ocen (np. de Jong out → fade Holandii; Cape Verde 0:0 ze Spain → remis żywszy);
- w mailu raportuj, które czynniki przeważyły (nie sam kurs).
To spina dotychczasowe lekcje (mismatch amplifikacja, bramkarz-bohater, motywacja tabelowa) — one
WŁAŚNIE są „czynnikami". Rynek zostaje mocnym baseline (jest efektywny), ale nie wyrocznią.

---

## 2026-06-22 — v1.9 (lekcja: bramkarz-bohater x2, Urugwaj-niespodzianka; pick'em → remis)

**Wyniki 21.06:**
- Hiszpania **4:0** Arabia Saudyjska — typ 2:0: tendencja ✓ (+2 pkt). Mismatch amplifikacja: model 2:0, rzecz. 4:0. Reguła v1.8 potwierdzona (mismatch > Poisson sugeruje).
- Belgia **0:0** Iran — typ 1:0: CHYBIONY (0 pkt). Beiranvand 15 parad (rekord?) — klasyczny bramkarz-bohater niszczy mismatch. Belgia przez 20 min z 10 zawodnikami. **Lekcja potwierdzona z v1.8**: sprawdzaj GK rywala i dyscyplinarnę ryzyko; 1:1 byłoby właściwsze.
- Urugwaj **2:2** Zielony Przylądek — typ 1:0: CHYBIONY (0 pkt). Historyczny wynik — Zielony Przylądek ma 1 pkt na mundialu! Urugwaj nie zamknął meczu (błąd koncentracji). **Lekcja**: "umiarkowany mismatch" to nie gwarancja; przy drużynach spoza top-50 FIFA zachowaj rezerwę — 1:1 ma wyższy EV niż wydaje się.
- Nowa Zelandia **1:3** Egipt — typ 0:1: tendencja ✓ (+2 pkt). Egyptt odrobił straty po 1:0 dla NZ. Tendencja trafna.

**Bilans dnia 21.06:** kicktipp +4 pkt (2 mecze tendencja), Fortuna 0 PLN.
**Łącznie:** 24 pkt kicktipp, 976.57 PLN bankroll (ROI -2.3%).

**Nowe/potwierdzone zasady:**
7. **Pick'em mecze 3-way ≈50/50 z draw_bias:** przy P(draw) ≥ 25% i draw_bias=1.4 → remis = wyższy EV (~1.19 vs ~1.15). Norwegia-Senegal dziś to idealny przykład.
8. **Urugwaj-test:** W meczach "umiarkowany faworyt vs chwila historii" (drużyna debiutuje lub nie ma co stracić) rozważ 1:1 zamiast 1:0, bo desperacja podbija odporność słabszej strony.

**Kontynuujemy:** draw_bias=1.4, wszystkie zasady v1.8 w mocy. Dziś priorytety: ARG 1:0, FRA 2:0, NOR-SEN 1:1, JOR-ALG 0:1.

---

## 2026-06-21 — v1.8 (lekcja: bramkarz-bohater niszczy mismatch; mismatch amplifikacja x2)

**Wyniki 20.06:**
- Holandia **5:1** Szwecja — typ kicktipp 2:1: tendencja trafiona (+2 pkt). Kolejny mismatch który rozjechał się bardziej niż model sugerował (my 2:1, rzecz. 5:1). Gakpo + Brobbey po 2 gole.
- Niemcy **2:1** WKŚ (Wybrzeże Kości Słoniowej) — typ kicktipp 1:0: tendencja PLUS różnica bramek trafiona (+3 pkt!). Undav dał brace z ławki. Idealny typ: złapał tendencję i diff.
- Ekwador **0:0** Curaçao — typ kicktipp 3:0: CHYBIONY (0 pkt). Historyczna niespodzianka: Eloy Room 15 parad (rekord MŚ!), Curaçao historyczny punkt. LEKCJA: "mismatch" nie gwarantuje goli – sprawdź defensywę rywala, zwłaszcza bramkarza.
- Tunezja **0:3** Japonia — typ kicktipp 0:1: tendencja trafiona (+2 pkt). Japonia wygrała 3:0 zamiast 1:0 – ponowna mismatch amplifikacja.

**Bilans dnia:** kicktipp +7 pkt (3 mecze tendencja, 1 z różnicą bramek), Fortuna 0 PLN (brak zakładów).

**Nowe zasady:**
5. **Precyzja mismatch:** dla umiarkowanego mismatch (λ_rywal ~0.5–0.8) → typ **2:0**, NIE 3:0. Dla wyraźnego mismatch (λ_rywal <0.4) → 3:0 rozważyć. Ekwador vs Curaçao był umiarkowany (Curaçao nie=Haiti/Katar), a 3:0 był zbyt ambitny.
6. **Bramkarz-heroj:** przed typem mismatch sprawdź bramkarza rywala. "Gorący" lub wybitny GK może zepsuć typ – rozważ zejście o 1 gola w dół lub DNB zamiast dokładnego wyniku.

**Kontynuujemy:** draw_bias=1.4, podejście EV-kicktipp bez zmian.

---

## 2026-06-20 — v1.7 (lekcja: notacja kierunku wyniku; mismatch margin > model)

**Wyniki 19.06:**
- USA **2:0** Australia — typ kicktipp 1:0: tendencja trafiona (+2 pkt). Typ Fortuna X (remis) @ 4.4 → **przegrany (-19.93 PLN)**. USA bez Pulisica nadal wygrało. Zakład na remis przy 88% faworycie (edge był ujemny od początku) — błąd wyceny (edge był < -2%, nie powinniśmy tego wchodzić).
- Szkocja **0:1** Maroko — typ kicktipp 1:0 → **0 pkt (zła tendencja)**. **Krytyczny błąd notacji:** wpisano "1:0" jako "Szkocja 1-0 Maroko" podczas gdy intencją było "Maroko wins 1-0 = 0:1". Saibari strzelił w 72s.
- Brazylia **3:0** Haiti — typ kicktipp 2:0: tendencja trafiona (+2 pkt). Model 2:0, rzeczywistość 3:0 — mismatche rozjechały się bardziej niż λ-Poisson sugeruje (jak Kanada 6:0 Katar, Niemcy 7:1 Curaçao).

**Bilans dnia:** kicktipp +4 pkt (2 mecze tendencja), Fortuna -19.93 PLN.

**Nowe zasady:**
1. **Notacja kierunkowa (krytyczne):** W meczu "Drużyna A vs Drużyna B" wynik "1:0" = A wygrywa. Jeśli chcemy wygraną B, MUSISZ wpisać "0:1". Zawsze sprawdź, czyją perspektywą jest wynik przed submit.
2. **Mismatch amplifikacja:** Przy λ_rywal < 0.5 (Curaçao, Haiti, Katar), model Poissona **niedoszacowuje** rozmiar wygranej. Rozważ wyższy wynik niż sugeruje Poisson (np. 4:0 zamiast 3:0) dla takich mismatch.
3. **Zakłady na remis przy dominującym faworycie:** Edge był ujemny dla USA vs AUS X@4.4. Zasada: przy faworycie >85% de-vig, zakłady Fortuna na remis/przegranie są zazwyczaj poniżej progu — pomijaj.

**Potencjalny sygnał dziś:** Kubo kontuzjowany (JPN) → Under 2.5 TUN vs JPN może mieć edge >5% jeśli kurs ≥1.73. Weryfikuj na Fortunie.

**Kontynuujemy:** draw_bias=1.4, podejście EV-kicktipp bez zmian.

---

## 2026-06-19 — v1.6 (lekcja: motywacja > kursy przy tabelowym niedoborze)

**Wyniki 18.06:**
- Szwajcaria **4:1** Bośnia — typ 1:0 trafił tendencję (+2 pkt), ale nie antycypował niespodziewanej erupcji goli po 74' + czerwona Bośni. Under 2.5 przegrana (-10 PLN).
- Kanada **6:0** Katar — typ 2:0 trafił tendencję (+2 pkt). Historyczny wynik, trudny do przewidzenia.
- Meksyk **1:0** Korea Płd. — typ 1:1 chybiony (+0 pkt). **Kluczowa lekcja:** Meksyk miał 3 pkt, Korea 0 pkt → Korea MUSIAŁA wygrać, ale to Meksyk miał spokój i zagrał skutecznie. Typ 1:1 był błędem kontekstualnym — gdy faworyt jest na 3 pkt, a rywal na 0 pkt desperacko atakuje, faworyt może spokojnie kontrować → **wynik 1:0 był bardziej naturalny niż remis**.

**Nowa zasada (motywacja tabelowa):** Gdy faworyt jest na 3 pkt, a rywal na 0 pkt → wyżej niż zwykle prawdopodobieństwo **wygrania zamkniętego meczu 1:0** (faworyt nie musi ryzykować, rywal musi). Typuj wygraną, nie remis, nawet gdy % są bliskie 50/50.

**Kalibracja Under:** Market pod Szwajcarię-Bośnię miał rację (52% Under), mój szac. model 60% był za pewny. Gole późne (kontuzje, zmęczenie, czerwone kartki) są czynnikiem, który model Poissona pomija → zachować pokorę przy Under w meczach wyrównanych.

**Kontynuujemy:** draw_bias=1.4, podejście EV-kicktipp bez zmian.

---

## 2026-06-18 — v1.5 (value on Under; kalibracja λ wg meczu otwarcia)

**Obserwacja.** Czechia 1:1 RPA — klasyczny mecz dwóch zespołów na 0 punktach (musi wygrać obie
strony), ale wynik bardzo przewidywalny: niskie bramkowanie, gol z karnego (Mokoena 83'), Czechy
prowadziły do 83'. Model draw_bias=1.4 nadal trafny dla takich meczów.

**Nowy insight: kalibracja λ z meczu otwarcia.** Gdy obie drużyny zdobyły dokładnie 1 gola
w swoim pierwszym meczu (nawet przy różnej liczbie strzałów), sensowne jest zejście z prognozą
λ do okolic 1.0-1.3 na drużynę (total ≈ 2.2-2.5). Porównanie z rynkową linią O/U to dobra
metoda sanity-check. W dzisiejszym meczu Szwajcaria vs Bośnia market daje Under -123 (ok. 52.5%
de-vig), a model wychodzi na ≈60% Under — różnica wystarczająca na value bet Under 2.5 @1.81
(szac. edge ~7.7%). Uwaga: zawsze weryfikuj kurs na Fortunie przed wejściem.

**Kontynuujemy.** draw_bias=1.4 zostawiamy bez zmian — działa jako nudge (nie override).
Kicktipp: stosujemy profil „siła ofensywna faworyta": Kanada (Davies wraca, 74%) → 2:0;
Meksyk-Korea (~50/50 w Guadalajarze) → 1:1; Szwajcaria-Bośnia (62% Szw., wasteful) → 1:0.

---

## 2026-06-17 — v1.4 (korekta: draw_bias 1.7 był za wysoki)

Anglia **4:2** Chorwacja (6 bramek!) — wysokobramkowa wygrana umiarkowanego faworyta, odwrotność
„cagey opener". Typ 1:1 (z draw_bias=1.7) dał 0 pkt. 1.7 *zawsze* nadpisywał umiarkowanego faworyta
na remis, ignorując siłę ofensywną (Kane w formie, Bellingham) — to overfitting do serii remisów.

**Zmiana:** draw_bias 1.7 → **1.4** (nudge, nie override). Plus w kroku 6 liczy się SIŁA OFENSYWNA
faworyta, nie tylko %: cagey/defensywny faworyt → remis-ish; faworyt z atakiem w formie → wygrana.

**Meta-lekcja:** nie przekręcać kalibracji po KAŻDYM wyniku — wariancja działa w obie strony,
cel to oczekiwane punkty w wielu meczach, nie reakcja na ostatni mecz.

---

## 2026-06-17 — v1.3 (kalibracja: więcej remisów)

**Obserwacja (dane).** Faza grupowa MŚ 2026 to festiwal remisów faworytów: Kanada 1:1 (Bośnia),
Brazylia 1:1 (Maroko), Katar 1:1 (Szwajcaria), **Portugalia 1:1 (DR Kongo)**, Ameryka Płd. 0/4.
Model za bardzo szedł za faworytem (1:0/2:0) i przegapiał remisy — a „9-tka" płaci za remis 3 pkt.

**Zmiana.** Wprowadzony `kicktipp.draw_bias` (mnożnik prawdopodobieństwa remisu przed liczeniem
oczekiwanych punktów), **dobrany empirycznie na 1.7**: flipuje UMIARKOWANEGO faworyta w otwarciu
na **1:1** (model: 1:1≈1,37 vs 1:0≈1,17), a wyraźnego faworyta i mismatch (typ Norwegia/Haaland)
zostawia na wygranej. Spójne z zasadą jakościową: umiarkowany faworyt (~45–62%) w otwarciu → 1:1
(0:0 przy niskim O/U); 2:0/3:0 tylko na realne mismatche.

**Uczciwie.** Dokładny wynik to duża wariancja — konkretnych niespodzianek (Portugalia 1:1)
nie da się pewnie typować; metryką są oczekiwane punkty w wielu meczach, nie pojedyncze trafienia.
Ta kalibracja łapie głównie remisy umiarkowanych faworytów (typ Kanada), gdzie traciliśmy najwięcej.
Do rewizji, gdy nazbiera się więcej wyników (dostroić draw_bias w górę/dół).

---

## 2026-06-11 — v1.2 (zmiana bukmachera: STS → Fortuna)

Bukmacher do value-betów zmieniony na **Fortuna** (efortuna.pl). Wcześniejsze wpisy
mówiące o „STS" odnoszą się teraz do Fortuny — to samo podejście i limity, inny dostawca
kursów. W `state/history.jsonl` zakłady realne mają teraz `type: "fortuna"`.

---

## 2026-06-11 — v1.1 (kalibracja punktacji ligi)

**Co ustaliliśmy.** Liga *Mamalova MŚ 2026* gra regułą **„9-tka" w wariancie turniejowym**
(boiska neutralne → brak home/away). Realne wagi:
- **wygrana:** tendencja 2 / różnica bramek 3 / dokładny wynik 4,
- **remis:** tendencja 3 / dokładny wynik 4 (bez tieru różnicy bramek).

**Wniosek strategiczny (ważny).** Remis na samej tendencji daje **3 pkt**, czyli więcej niż
**2 pkt** za trafioną tendencję wygranej. Dokładny wynik jest tak samo wart (4) dla obu.
Efekt: w meczach blisko 50/50 (a w fazie grupowej MŚ jest ich sporo) **typ na remis jest
relatywnie bardziej opłacalny** niż przy symetrycznej skali — częściej wybieraj 1:1 / 0:0,
gdy rynek nie wskazuje wyraźnego faworyta. Przy wyraźnym faworycie nadal rządzi wąska wygrana
(1:0 / 2:1), bo to największy kubełek tendencji + szansa na różnicę bramek.

**Sprawdzenie na dziś (11.06).** Po przeliczeniu pod 9-tkę typy bez zmian: Meksyk–RPA **1:0**
i Korea–Czechy **1:0** wciąż maksymalizują oczekiwane punkty (faworyci na tyle wyraźni, że
wygrana > remis). Korea–Czechy było najbliżej progu remisu.

**Operacyjnie.** Dostarczanie przełączone na **SMTP** (realny inbox) — do czasu ustawienia
sekretów Gmaila bot robi fallback na draft.

---

## 2026-06-11 — v1 (założenia startowe)

**Filozofia.** Rynek (kursy bukmacherów po usunięciu marży) jest naszym punktem
odniesienia. Nie ścigamy się z rynkiem na siłę — szukamy sytuacji, gdzie mamy
*konkretny powód* sądzić inaczej niż rynek (świeża kontuzja, rotacja, kontekst,
motywacja, warunki). Bez powodu = idziemy z konsensusem.

**Kicktipp (gra typerska — punkty).**
- Typujemy pod **maksymalizację oczekiwanych punktów** wg punktacji ligi, nie pod
  „efektowny wynik".
- Domyślnie ostrożne wyniki bliskie medianie rozkładu: lekki faworyt → 1:0 / 2:1;
  mecz wyrównany / niski O/U → 1:1 lub 1:0; wysoki O/U + faworyt → 2:1 / 2:0.
- Faza grupowa MŚ bywa zachowawcza (drużyny nie chcą stracić) → uważać na przeszacowanie bramek.

**Fortuna (realne value, tylko rekomendacje).**
- Zakład tylko przy edge ≥ 5% i kursie w rozsądnym przedziale (1.50–6.00).
- Sizing ostrożny (ułamkowy Kelly), maks. 2 jednostki na typ, maks. 3 typy dziennie.
- Preferujemy rynki, które łatwiej modelować z newsów: 1X2, double chance, O/U 2.5, DNB.
- BTTS i handicapy — selektywnie, dopiero gdy mamy mocny sygnał.
- Zero akumulatorów (mnożą marżę i wariancję, zabijają EV).

**Bankroll & dyscyplina.**
- Start: 1000 PLN wirtualnie, 1u = 2% (20 PLN).
- Twardy stop: jeśli miesięczna strata > 30% bankrolla — pauza na zakłady, tylko kicktipp.
- Nigdy nie podnosimy stawek, żeby „odrobić" stratę (anty-tilt).

**Czego się uczymy (do weryfikacji w kolejnych dniach).**
- Czy nasze prawdopodobieństwa są skalibrowane (czy typy ~60% wchodzą ~60% razy?).
- Czy w kicktippie nie przepalamy punktów na zbyt odważne wyniki.
- Które rynki u Fortuny realnie dają nam value, a które tylko wariancję.
