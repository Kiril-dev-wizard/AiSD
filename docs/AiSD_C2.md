# AiSD_C2_60 — Ćwiczenie 2: Implementacja prostych algorytmów numerycznych

Wykonano w **Python 3** (wszystkie 5 zadań) oraz w **Pascalu** (`C2_pascal/` — wszystkie 5 programów skompilowane FPC 3.2.2 i uruchomione; wyniki w `pascal_test_results.txt`).

Każdy program podzielony jest na funkcje zgodnie z zasadami programowania strukturalnego, zawiera komentarze i został przetestowany. Wynik testów: `C2_python/test_results.txt` — **21/21 PASS**.

---

## Zadanie 1 — Równanie kwadratowe

**Pliki:** `C2_python/a06_c2_zad1_rownanie.py`, `C2_pascal/a06_c2_zad1_rownanie.pas`

**Analiza:** ax²+bx+c=0. Dla a=0 mamy równanie liniowe (lub sprzeczne). Dla a≠0 liczymy wyróżnik Δ=b²−4ac: Δ<0 → brak pierwiastków rzeczywistych; Δ=0 → jeden podwójny x=−b/2a; Δ>0 → dwa x=(−b∓√Δ)/2a.

**Struktura (4 części):** `read_coefficients` (wejście), `solve` (logika), `print_result` (wyjście), `run` (sterowanie).

**Scenariusze testowe i wyniki (realne):**

| Wejście (a,b,c) | Oczekiwane | Otrzymane | Wynik |
|---|---|---|---|
| 1,−5,6 | x1=2, x2=3 | 2.0, 3.0 | PASS |
| 1,−2,1 | podwójny x=1 | 1.0 | PASS |
| 1,0,1 | brak rzeczywistych | brak | PASS |
| 0,2,−4 | liniowe x=2 | 2.0 | PASS |

---

## Zadanie 2 — Suma kwadratów kolejnych liczb

**Pliki:** `C2_python/a06_c2_zad2_suma_kwadratow.py`, `C2_pascal/a06_c2_zad2_suma_kwadratow.pas`

Sumowanie w pętli: S ← S + (L0+i)² dla i=0..n−1. Testy: (1,3)→14, (0,5)→30, (−2,3)→5, (7,0)→0 —wszystkie PASS.

---

## Zadanie 3 — Rok przestępny

**Pliki:** `C2_python/a06_c2_zad3_rok_przestepny.py`, `C2_pascal/a06_c2_zad3_rok_przestepny.pas`

**Wymagana struktura 4 funkcji:** `read_year` (całkowita, czyta rok), `is_leap_year` (logicznа, warunek `(R%4==0 and R%100!=0) or R%400==0`), `print_result` (procedura wypisująca), `run` (procedura sterująca wywołująca pozostałe).

Testy lat: 2000 (tak), 1900 (nie), 2024 (tak), 2023 (nie), 1600 (tak), 1700 (nie) —wszystkie PASS.

---

## Zadanie 4 — Suma cyfr (metodą iteracyjną)

**Pliki:** `C2_python/a06_c2_zad4_sumacyfr.py`, `C2_pascal/a06_c2_zad4_sumacyfr.pas`

**Struktura 4 funkcji:** `read_number`, `digit_sum` (pętla: `S += L%10; L//=10`), `print_result`, `run`. Obsługa ujemnych przez `abs()`. Testy: 258→15, 0→0, −258→15, 999→27, 100→1 —wszystkie PASS.

---

## Zadanie 5 (opcjonalne) — Zużycie energii elektrycznej

**Pliki:** `C2_python/a06_c2_zad5_prad.py`, `C2_pascal/a06_c2_zad5_prad.pas`

**Struktura 3 procedur:** `control` (sterowanie), `simulate` (algorytm), `print_results` (wyniki).

Zamiast 365 dni: 10 sekund symulacji, P_INST=3 kW, Mc=P·(1+sin(t))/2, Mb=0.1·Mc. Taryfa I w godz. 6–13 i 15–22. Wyniki: E1b = 0.1·E1c (PASS), energia > 0 (PASS).

**Odpowiedzi na pytania:**
- *Problemy przy testowaniu:* ciągły strumień danych z interfejsu, niepowtarzalność sygnału, czas symulacji 365 dni, stan liczników zależny od historii, granice taryf, przepełnienia i zaokrąglenia.
- *Gdy interfejs niedostępny:* zastosować test doubles — stub zwracający znany sygnał `sin(t)`, mock interfejsu z ustawioną datą/godziną, testy graniczne przejść między taryfami, testy regresji z zapisanymi danymi (record/replay), a w środowisku produkcyjnym — logowanie i monitoring nieprawidłowych odczytów.
