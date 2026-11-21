# AiSD_C1_60 — Ćwiczenie 1: Proste algorytmy

Autor rozwiązania: Kiril Kaminskyi · AHE Łódź · 21.11.2026
Materiał źródłowy: Bohdan Szymczak, `AiSD_C1_60.pdf`

Każde zadanie zawiera: **schemat blokowy** (SVG/PDF w `C1_schematy/diagrams/`), **opis językiem naturalnym**, **listę kroków** i **test poprawności** (analiza → scenariusze → wykonanie).

---

## Zadanie 1 — Suma kwadratów kolejnych liczb całkowitych

**Dane:** L0 (liczba początkowa), n (liczba kolejnych liczb). **Wynik:** S.
**Przykład:** L0=1, n=3 → S=1²+2²+3²=14.

**Schemat blokowy:** `C1_schematy/diagrams/z1_suma_kwadratow.svg`

**Opis naturalny:** Ustawiamy zerowy akumulator S i licznik i. Dopóki i<n, dodajemy do S kwadrat liczby L0+i i zwiększamy i o jeden. Po wyjściu z pętli S jest sumą kwadratów.

**Lista kroków:**
1. Wczytaj L0, n.
2. S ← 0, i ← 0.
3. Jeśli i ≥ n — przejdź do kroku 7.
4. S ← S + (L0+i)·(L0+i).
5. i ← i + 1.
6. Wróć do kroku 3.
7. Wypisz S.

**Test poprawności (wykonany w Pythonie, `C2_python/run_all_tests.py`):**

| Scenariusz | Wejście | Oczekiwane S | Otrzymane S | Wynik |
|---|---|---|---|---|
| Podstawowy | L0=1, n=3 | 14 | 14 | PASS |
| Od zera | L0=0, n=5 | 30 | 30 | PASS |
| Liczby ujemne | L0=−2, n=3 | 5 | 5 | PASS |
| Puste | n=0 | 0 | 0 | PASS |

**Algorytm alternatywny:** wzór na sumę kwadratów ciągu: S = Σ(k=0..n−1)(L0+k)² = n·L0² + 2L0·n(n−1)/2 + (n−1)n(2n−1)/6 — bez pętli, O(1). Pętla jest jednak wymagana treścią zadania i jest bardziej uniwersalna.

---

## Zadanie 2 — Rok przestępny

**Schemat blokowy:** `C1_schematy/diagrams/z2_rok_przestepny.svg`

**Opis naturalny:** Rok jest przestępny, gdy jest podzielny przez 4 i niepodzielny przez 100, albo gdy jest podzielny przez 400. W schemacie używamy operatora mod (reszta z dzielenia).

**Lista kroków:**
1. Wczytaj R.
2. Jeśli R mod 4 ≠ 0 → wypisz „nieprzestępny”, koniec.
3. Jeśli R mod 100 ≠ 0 → wypisz „przestępny”, koniec.
4. Jeśli R mod 400 = 0 → wypisz „przestępny”, inaczej „nieprzestępny”.

**Testy (wykonane):**

| R | Oczekiwane | Otrzymane | Wynik |
|---|---|---|---|
| 2000 | przestępny | przestępny | PASS |
| 1900 | nieprzestępny | nieprzestępny | PASS |
| 2024 | przestępny | przestępny | PASS |
| 2023 | nieprzestępny | nieprzestępny | PASS |
| 1600 | przestępny | przestępny | PASS |
| 1700 | nieprzestępny | nieprzestępny | PASS |

---

## Zadanie 3 — Suma cyfr liczby całkowitej

**Schemat blokowy:** `C1_schematy/diagrams/z3_sumacyfr.svg`

**Opis naturalny:** Bierzemy wartość bezwzględną L. W pętli dodajemy do S ostatnią cyfrę (L mod 10) i obcinamy ją (L div 10), aż L==0.

**Lista kroków:**
1. Wczytaj L; jeśli L<0 → L ← −L.
2. S ← 0.
3. Jeśli L = 0 → wypisz S, koniec.
4. S ← S + (L mod 10).
5. L ← L div 10; wróć do 3.

**Testy (wykonane):** 258→15, 0→0, −258→15, 999→27, 100→1 — wszystkie PASS.

**Dyskusja definicji algorytmu:** Treść zadania nie precyzuje zachowania dla liczb ujemnych i zera — to typowa niekompletność specyfikacji. Przyjęto L=|L| oraz S(0)=0. Algorytm spełnia cechy algorytmu: skończoność (L maleje), determinizm, jednoznaczność, wykonalność (mod/div) i wynik (S). Zapis `div` w języku naturalnym odpowiada `//` w Pythonie.

---

## Zadanie 4 — Zużycie energii elektrycznej

**Schemat blokowy:** `C1_schematy/diagrams/z4_prad.svg`

**Opis naturalny:** Miernik co sekundę dostarcza moc czynną Mc, bierną Mb, datę Dt i godzinę Gd. Zgodnie z godziną wybieramy taryfę: I dla 6–13 i 15–22, II dla 22–6 i 13–15. Energia w kWh przyrasta o Mc/3600 (moc w kW × 1/3600 h). Osobno sumujemy czynną i bierną w obu taryfach i śledzimy maksymalną moc czynną w miesiącu; na końcu miesiąca zapisujemy maksimum i zerujemy licznik.

**Lista kroków:**
1. Zeruj E1c, E2c, E1b, E2b, MaxMoc.
2. Dla każdego z 365 dni, dla sekund t=0..86399:
   a. Wczytaj Mc, Mb, Gd.
   b. Jeśli Gd∈[6,13)∪[15,22) → E1c+=Mc/3600, E1b+=Mb/3600, inaczej E2c+=Mc/3600, E2b+=Mb/3600.
   c. Jeśli Mc>MaxMoc → MaxMoc←Mc.
3. Jeśli nastąpił koniec miesiąca → wypisz MaxMoc, MaxMoc←0.
4. Po 365 dniach wypisz E1c, E1b, E2c, E2b.

**Analiza testów:** pełna symulacja 365×86400 sekund jest niepraktyczna w teście; zastosowano symulację 10 sekund z mocą P_INST=3 kW i Mb=0.1·Mc (zgodnie z C2 zad.5). Wynik: E1b = 0.1·E1c (PASS), suma energii > 0 (PASS). Testy graniczne taryfy: godz. 5:59→II, 6:00→I, 12:59→I, 13:00→II, 14:59→II, 15:00→I, 21:59→I, 22:00→II — zgodne ze specyfikacją.

**Problemy testowania:** niedostępny interfejs miernika → testy z danymi syntetycznymi (stub/funkcja sin(t)); testowanie zmiany miesiąca wymaga przyspieszenia zegara lub wstrzyknięcia daty; trudno odtworzyć rzeczywisty szczyt mocy — stosujemy znany sygnał testowy.

---

## Zadanie 5 — Najszybsze nawiązanie połączenia telefonicznego

**Schemat blokowy:** `C1_schematy/diagrams/z5_telefon.svg`

**Opis naturalny:** Szukamy ścieżki o najmniejszej liczbie czynności. Kolejność wyboru: (1) ostatnie połączenie na ekranie głównym/widget → jedno dotknięcie „oddzwoń”; (2) ulubiony kontakt widoczny na ekranie/widżecie → jedno dotknięcie; (3) kontakt w książce → otwarcie telefonu, wyszukanie po imieniu, wybór, „połącz”; (4) numer niezapisany → klawiatura, wpisanie numeru, „połącz”. Dodatkowo: skrót z ekranu blokady, asystent głosowy oraz NFC/QR tylko gdy dostępne. Kryterium minimalizacji: liczba dotknięć ekranu.

**Lista kroków:**
1. Sprawdź ekran główny/widget: czy dostępne „ostatnie połączenie”? Jeśli tak → dotknij „oddzwoń” (1 czynność).
2. Sprawdź ulubione/widżet: dotknij kontaktu (1–2).
3. Inaczej otwórz aplikację Telefon → wyszukaj imię → dotknij kontaktu → „połącz”.
4. Inaczej wpisz numer na klawiaturze → „połącz”.
5. Zakończ po nawiązaniu połączenia.

**Test poprawności (scenariusze):**

| Scenariusz | Oczekiwana ścieżka | Liczba czynności |
|---|---|---|
| Oddzwanianie do ostatniej osoby | widget → oddzwoń | 1 |
| Ulubiony kontakt na widżecie | dotknięcie | 1 |
| Kontakt w książce | wyszukaj → wybierz | 3–4 |
| Nowy numer | klawiatura → połącz | 2+wpisanie |

Weryfikacja: dla każdego scenariusza wybrana ścieżka ma najmniejszą liczbę czynności spośród dostępnych — PASS.

---

## Zadanie 6 — Wyjście robota z magazynu

**Schemat blokowy:** `C1_schematy/diagrams/z6_robot.svg`

**Dane:** magazyn 22×12 m, roboty w poleach 1×2 m, krok 0,75 m, wyjście w środku krótszego boku (y=6); roboty zwrócone przodem do wyjścia, poruszają się tylko kolumnami, omijają miejsca zajęte przez inne roboty (nawet puste po ich usunięciu).

**Założenia przyjęte w rozwiązaniu (bo rysunek w PDF jest graficzny, a nie opis słowny):** osie: x wzdłuż 22 m, y wzdłuż 12 m; wyjście przy (x=22, y=6); kolumna = ruch wzdłuż y; korytarz wyjściowy wzdłuż y=6. Liczba kroków = ceil(dystans_m / 0,75).

**Opis naturalny:** Robot wyznacza wiersz wyjścia y=6. Wybiera najbliższą wolną kolumnę (pomijając kolumny zajęte przez inne roboty). Idzie w tej kolumnie do y=6, obraca się o 90° w stronę wyjścia i idzie korytarzem do x=22, omijając zajęte pola najkrótszym possible objazdem.

**Lista kroków:**
1. Wczytaj xr, yr.
2. yE ← 6 (środek krótszego boku).
3. Wybierz wolną kolumnę xK minimalizującą |xr−xK|.
4. n1 ← ceil(|yr−yE|·2 / 0,75); idź n1 kroków w kolumnie do yE; obróć się o 90°.
5. n2 ← ceil(|xK−22| / 0,75); idź do wyjścia, omijając zajęte pola.
6. Wyjdź z magazynu.

**Testy (scenariusze i wyniki):**

| Pozycja (xr,yr) | Oczekiwany kierunek | Dystans (krokach) | Wynik |
|---|---|---|---|
| (10, 6) | wprost do wyjścia | ceil(12/0,75)=16 | PASS |
| (10, 2) | w górę kolumny, potem w prawo | ceil(8/0,75)+16 ≈ 27 | PASS |
| (10, 10) | w dół kolumny, potem w prawo | ≈27 | PASS |
| (20, 6) | wprost, krótki | ceil(2/0,75)=3 | PASS |
| kolumna zajęta | objazd najbliższą wolną kolumną | dłużej o 2·0,75 m | PASS |

Algorytm jest deterministyczny, skończony i zawsze wybiera najkrótszą trasę przy zadanym zbiorze przeszkód (zgodnie z przyjętym modelem korytarzy).
