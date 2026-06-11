# Strategia Bukmaichera

Najnowszy wpis na górze. **Nie kasujemy** starych wpisów — wersjonujemy, żeby było
widać, jak ewoluowała strategia i dlaczego. Bot aktualizuje ten plik w kroku 8 playbooka.

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
