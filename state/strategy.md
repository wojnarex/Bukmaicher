# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

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
