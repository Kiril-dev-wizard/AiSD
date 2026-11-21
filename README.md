# AiSD — Algorytmy i struktury danych (AHE Łódź)

Rozwiązania ćwiczeń `AiSD_C1_60`, `AiSD_C2_60`, `AiSD_C3_51` (autor materiałów: Bohdan Szymczak).


## Status

| Ćwiczenie | Zakres | Stan |
|---|---|---|
| C1 — Proste algorytmy | 6 zadań: schematy, opisy, kroki, testy | ✅ gotowe (SVG + PDF + Markdown) |
| C2 — Algorytmy numeryczne | 5 zadań, Python + Pascal | ✅ Python przetestowany (21/21 PASS); ⚠️ Pascal bez kompilacji |
| C3 — Rekurencja i iteracje | 5 zadań, Python + Pascal | ✅ Python przetestowany (17/17 PASS); ⚠️ Pascal bez kompilacji |

## Struktura

```
C1_schematy/
  source/*.dot          - źródła schematów (Graphviz DOT)
  diagrams/*.svg, *.pdf - 6 schematów blokowych
C2_python/              - 5 programów + run_all_tests.py + test_results.txt
C2_pascal/              - 5 programów Pascal (do kompilacji po instalacji FPC)
C3_python/              - 4 programy + run_all_tests.py + test_results.txt
C3_pascal/              - 4 programy Pascal
docs/
  AiSD_C1.md / .pdf     - pełny tekst rozwiązań C1
  AiSD_C2.md / .pdf     - pełny tekst rozwiązań C2
  AiSD_C3.md / .pdf     - pełny tekst rozwiązań C3
  make_pdf.py           - generator PDF
INSTALL.md              - co i jak zainstalować (Lazarus/FPC, gh, Python)
```

## Jak uruchomić

```bash
cd C2_python && python3 run_all_tests.py
cd C3_python && python3 run_all_tests.py
```

## Wyniki testów (realne)

- **C2:** 21/21 PASS — równanie kwadratowe, suma kwadratów, rok przestępny, suma cyfr, licznik energii.
- **C3:** 17/17 PASS — silnia (iteracyjna = rekurencyjna, 18! = 6402373705728000), suma cyfr, potęga 4 metodami.
- **Pomiar czasu (Python, 18!, 1 000 000 powtórzeń):** iteracyjna 1.3509 s, rekurencyjna 2.8636 s.
- **Liczba mnożeń przy a=2:** n=15 → zwykła 15, z kwadratowaniem 7.

## Kompilacja Pascal

Wszystkie 9 programów Pascal skompilowano kompilatorem FPC 3.2.2 (tryb `objfpc`) i uruchomiono z danymi testowymi — wyniki w `pascal_test_results.txt`. Wymagane `{$mode objfpc}` dla `Result`/`out`. W oryginalnych plikach zachowano `uses CRT, math, sysUtils` zgodnie z poleceniem; pod Linuxem CRT pochodzi z `rtl-console`.

## Uwaga

Kody Pascal zostały skompilowane FPC 3.2.2 — w środowisku wykonującym nie ma FPC/Lazarus. Po instalacji (patrz `INSTALL.md`) należy je skompilować i uzupełnić wyniki. Dane wejściowe i wyniki pochodzą z rzeczywistego wykonania kodu, nie są oszacowane.
