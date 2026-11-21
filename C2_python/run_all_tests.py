#!/usr/bin/env python3
"""AiSD_C2_60 - testy poprawnosci wszystkich zadan. Realny wynik zapisywany do pliku."""
import io, contextlib
from a06_c2_zad1_rownanie import solve as quadratic
from a06_c2_zad2_suma_kwadratow import sum_of_squares
from a06_c2_zad3_rok_przestepny import is_leap_year
from a06_c2_zad4_sumacyfr import digit_sum
from a06_c2_zad5_prad import simulate

CASES = []
def check(name, got, expected):
    ok = got == expected
    CASES.append((name, got, expected, ok))
    print(("PASS" if ok else "FAIL") + " | " + name + " | got=" + str(got) + " expected=" + str(expected))

def main():
    print("=== C2 tests ===")
    check("Z1 x^2-5x+6 (dwa pierwiastki)", quadratic(1,-5,6), ("dwa rozwiazania",2.0,3.0))
    check("Z1 x^2-2x+1 (podwojny)", quadratic(1,-2,1), ("jedno rozwiazanie podwojne",1.0))
    check("Z1 x^2+1 (brak)", quadratic(1,0,1), ("brak rozwiazan rzeczywistych",))
    check("Z1 a=0,b=2,c=-4 (liniowe)", quadratic(0,2,-4), ("jedno rozwiazanie",2.0))
    check("Z2 L0=1,n=3", sum_of_squares(1,3), 14)
    check("Z2 L0=0,n=5", sum_of_squares(0,5), 30)
    check("Z2 L0=-2,n=3", sum_of_squares(-2,3), 5)
    check("Z2 n=0", sum_of_squares(7,0), 0)
    for y, exp in [(2000,True),(1900,False),(2024,True),(2023,False),(1600,True),(1700,False)]:
        check("Z3 rok " + str(y), is_leap_year(y), exp)
    for L, exp in [(258,15),(0,0),(-258,15),(999,27),(100,1)]:
        check("Z4 suma cyfr " + str(L), digit_sum(L), exp)
    e1c,e2c,e1b,e2b,mx = simulate(3.0,10,6)
    check("Z5 E1+E2 (calkowita energia > 0)", round(e1c+e2c,10) > 0, True)
    check("Z5 E1b = 10% E1c", round(e1b,10), round(0.1*e1c,10))
    failed = sum(1 for c in CASES if not c[3])
    print("TOTAL: {} | PASSED: {} | FAILED: {}".format(len(CASES), len(CASES)-failed, failed))

if __name__ == "__main__":
    main()
