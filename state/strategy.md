# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

---

## 2026-06-16 — v1.3 (kalibracja lambda przez rynek O/U + AH jako nowy rynek)

**Wnioski z 11.06:**
- Fortuna OU25 Meksyk-RPA (poniżej 2.5 @ 1.65): **WYGRANA** +6,50 PLN. Model się sprawdził.
- Kicktipp Meksyk-RPA (typ 1:0, wynik 2:0): **2 pkt** (tendencja). Typowaliśmy 1:0, padło 2:0.
  Straciliśmy 1 pkt bo lambda Meksyku była niedoszacowana — rynek O/U był bliżej 2.0 niż 1.5 gola.
- Kicktipp Korea-Czechy (typ 1:0, wynik 2:1): **3 pkt** (różnica bramek = 1). Dobry wynik.

**Korekta metodyczna.** Zaczynamy kalibrować sumę lambda od linii O/U rynkowej (de-vig),
a dopiero potem korygujemy o newsy. To zapobiega systematycznemu zaniżaniu sumy bramek
i typowaniu zbyt niskich wyników (pułapka „1:0 do wszystkiego").

**Nowy rynek: Asian Handicap (AH).** Dla meczów z wyraźną asymetrią (np. silny faworyt vs
debiutant) AH -1 może mieć dobre EV gdy faworyt dominuje ofensywnie. Dziś rekomendacja:
Norwegia AH -1 vs Irak (szac. edge ~20% przy kursie ~1.75, model oparty na kalibracji O/U).

**Kicktipp — wzorzec dnia:** Przy O/U ~2.5 i faworycie ≥65% → typ 1:0 nadal lideruje EV
(~1.66-1.80 pkt). Przy mocniejszym faworycie + wyższym O/U (Norwegia) → 2:0 wygrywa (~1.96 pkt).

**Co monitorujemy.** Czy typy ~65-70% wchodzą ~65-70% razy (kalibracja prawdopodobieństw).
Czy AH -1 sprawdza się lepiej niż 1X2 dla meczów mocny-słaby.

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
