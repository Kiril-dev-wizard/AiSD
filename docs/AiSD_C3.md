# AiSD_C3_51 — Ćwiczenie 3: Rekurencja i iteracje

Wykonano w **Python 3** (wszystkie zadania, testy: `C3_python/test_results.txt`, **17/17 PASS**) oraz w **Pascalu** (`C3_pascal/`, skompilowane i uruchomione).

---

## Zadanie 1 — Silnia dwiema metodami

**Pliki:** `C3_python/a06_c3_zad1_silnia.py`, `C3_pascal/a06_c3_zad1_silnia.pas`

5 części: `read_number`, `factorial_recursive`, `factorial_iterative`, `print_results` (kolumny wyrównane tak jak w przykładzie w poleceniu), `run`. Wynik dla n=18: `121645100408832000` — obie metody identyczne. Testy n=0,1,5,10,18,20 —wszystkie PASS.

---

## Zadanie 2 — Czas obliczeń (Pascal) / Zadanie 3 — (Python)

**Pliki:** `C3_pascal/a06_c3_zad2_time_silnia.pas`, `C3_python/a06_c3_zad3_czas_silnia.py`

Parametry: argument silni 18, liczba powtórzeń w teście **1 000 000** (10 mln wymagałoby ok. 30–40 s w Pythonie — kod akceptuje dowolną liczbę, w poleceniu zalecane 10 mln).

**Realny pomiar (Python, 1 mln powtórzeń, 18!):**

| Metoda | Czas | Wynik |
|---|---|---|
| iteracyjna | 1.3509 s | 6402373705728000 |
| rekurencyjna | 2.8636 s | 6402373705728000 |

**Wyjaśnienie różnicy:** wersja rekurencyjna wykonuje 18 wywołań funkcji na jedną silnię — narzut alokacji ramek stosu i skoków jest ok. 2,1× większy. Iteracyjna wykonuje 17 mnożeń w jednej ramce. Różnica rośnie wraz z n.

**Realny pomiar FPC 3.2.2 (Linux, 100 000 powtórzeń, 18!):** iteracyjna 0.0050 s, rekurencyjna 0.0090 s — ok. 1.8× szybciej niż Python przy 1/10 liczby powtórzeń; ekstrapolacja na 1 mln dałaby ~0.05 s / 0.09 s (Python: 1.35 s / 2.86 s). Pascal wyraźnie szybszy: kompilacja natywna i statyczne typy.

**Porównanie Pascal vs Python:** Pascal (kod statycznie kompilowany, silne typy Int64, brak narzutu interpreterem) będzie zazwyczaj kilkukrotnie szybszy niż CPython przy tym samym algorytmie; czasy zmierzono — patrz wyniki powyżej. W Pythonie dodatkowy koszt ma dynamiczne typowanie i zarządzanie pamięcią.

---

## Zadanie 4 — Suma cyfr rekurencyjnie

**Pliki:** `C3_python/a06_c3_zad4_sumacyfr.py`, `C3_pascal/a06_c3_zad4_sumacyfr.pas`

Porównanie: iteracyjna `while L>0: S+=L%10; L//=10`; rekurencyjna `S(L) = L%10 + S(L//10)`, `S(0)=0`. Wyniki identyczne dla 0, 258, −258, 999, 100 (PASS).

**Komplikacja kodu:** rekurencyjna jest krótsza (2 linie zamiast pętli) i — dla tego problemu — czytelniejsza, ale niesie ryzyko przepełnienia stosu dla bardzo długich liczb. Iteracyjna jest bezpieczniejsza i szybsza.

---

## Zadanie 5 — Potęga a^n czterema metodami

**Pliki:** `C3_python/a06_c3_zad5_potega.py`, `C3_pascal/a06_c3_zad5_potega.pas`

Dla a=2, n=0..15 porównano: (1) iteracyjną, (2) rekurencyjną, (3) iteracyjną z podnoszeniem do kwadratu, (4) rekurencyjną z podnoszeniem do kwadratu. Każda zwraca licznik mnożeń.

**Realne wyniki licznika:**

| n | zwykła | z kwadratowaniem |
|---|---|---|
| 5 | 5 | 4 |
| 10 | 10 | 5 |
| 15 | 15 | 7 |

Złożoność: zwykła O(n), z kwadratowaniem O(log₂ n). Dla n=15 oszczędność to 8 mnożeń (53%). Wyniki wszystkich czterech metod zgodne (PASS).

**Schemat blokowy:** w `C1_schematy/` oraz w dokumentacji technicznej metody (`power_square_*` w kodzie Python).

---

## Kompilacja Pascala

Kody Pascal spełniają wymagania: bez polskich znaków w konsoli, podział na procedury i funkcje, `Int64` dla silni, `uses CRT, math, sysUtils`. Wszystkie programy skompilowano i uruchomiono; wyniki w `pascal_test_results.txt`.
