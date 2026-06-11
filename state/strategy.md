# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

---

## 2026-06-11 — v1.2 (Dzień otwarcia MŚ 2026 — korekta pozycjonowania Under)

**Kontekst.** MŚ 2026 startuje dziś. Pierwsze 4 mecze fazy grupowej (11–12.06) to "zimne" otwieracze — drużyny ostrożne, dużo stawek.

**Kluczowa obserwacja kadrowa.**
- Meksyk–RPA: Santiago Gimenez **wątpliwy**, brak Malagóna i Marcela Ruiza. Meksyk osłabiony ofensywnie.
- Kanada–BIH: Alphonso Davies **OUT** — kluczowy gracz Kanady poza składem na otwieracz.
  Rynek wycenia Kanadę na -125 (szac. 52.7% po de-vig), ale nasza korekta sprowadza wygraną do ~47%.
- Korea–Czechy: Bae Jun-ho wątpliwy, Cho Yu-min out, ale Son fit.
- USA–Paragwaj: pełne składy; Paragwaj defensywny (ostatnie 4 mecze <3 goli).

**Under 2.5 jako leitmotiv dnia.**
We wszystkich 4 meczach rynek wycenia Under 2.5 jako wariant z lekką premią:
Meksyk–RPA Under -148 (~56% de-vig), Kanada–BIH Under -144 (~57%), USA–Paragwaj lean Under.
Nasze modele Poissona przy korektach kadrowych sugerują Under ≈ 62–68%.
→ Rekomendujemy Under 2.5 jako podstawowy rynek STS w dniach z nieobecnymi gwiazdami.

**Punkt do nauki (Meksyk Under 2.5 @ 1.65).**
STS @ 1.65 vs. rynek FanDuel @1.676 → szac. edge ok. +2% (poniżej progu 5%).
Bet był marginalny lub niedomiar; następnym razem weryfikować STS-specyficzny kurs przed wejściem.
*Na przyszłość: sprawdź kurs STS.pl ZANIM logujesz zakład, nie bierz kursu z US-market jako pewnik.*

**Kicktipp: potwierdzone 1:0 we wszystkich 4 otwieraczach.**
Model Poissona daje 1:0 jako typ z najwyższym E(pkt) (ok. 1.35–1.46) dla każdego meczu.
Jedyna alternatywa to 1:1, ale dopiero przy P(draw) ≥ 40–45% (nie osiągamy tego progu).

**Operacyjnie.**
- Delivery: github_action (Action wysyła SMTP po pushu).
- 2 nowe typy STS dla 12.06 (Kanada Under 2.5 szac. edge ~15%, USA Under 2.5 szac. ~11%).
- Łącznie 3 typy STS dzisiaj (w tym Mexico sprzed) — na granicy dziennego limitu 3.
- USA–Paragwaj o 03:00 PL — jeśli nie chcesz grać o tej porze, pomiń ten zakład.

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

**STS (realne value, tylko rekomendacje).**
- Zakład tylko przy edge ≥ 5% i kursie w rozsądnym przedziale (1.50–6.00).
- Sizing ostrożny (ułamkowy Kelly), maks. 2 jednostki na typ, maks. 3 typy dziennie.
- Preferujemy rynki, które łatwiej modelować z newsów: 1X2, double chance, O/U 2.5, DNB.
- BTTS i handicapy — selektywnie, dopiero gdy mamy mocny sygnał.
- Zero akumulatorów (mnożą marżę i wariancję, zabijają EV).

**Bankroll & dyscyplina.**
- Start: 1000 PLN wirtualnie, 1u = 2% (20 PLN).
- Twardy stop: jeśli miesięczna strata > 30% bankrolla — pauza na STS, tylko kicktipp.
- Nigdy nie podnosimy stawek, żeby „odrobić" stratę (anty-tilt).

**Czego się uczymy (do weryfikacji w kolejnych dniach).**
- Czy nasze prawdopodobieństwa są skalibrowane (czy typy ~60% wchodzą ~60% razy?).
- Czy w kicktippie nie przepalamy punktów na zbyt odważne wyniki.
- Które rynki STS realnie dają nam value, a które tylko wariancję.
