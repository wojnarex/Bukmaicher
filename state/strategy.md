# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

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
