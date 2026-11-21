#!/usr/bin/env python3
"""AiSD_C3_51 - testy poprawnosci + realny pomiar czasu."""
import time
from datetime import datetime
from a06_c3_zad1_silnia import factorial_recursive, factorial_iterative
from a06_c3_zad3_czas_silnia import measure
from a06_c3_zad4_sumacyfr import digit_sum_iterative, digit_sum_recursive
from a06_c3_zad5_potega import (power_iterative, power_recursive,
                               power_square_iterative, power_square_recursive)

CASES = []
def check(name, got, expected):
    ok = got == expected
    CASES.append((name, got, expected, ok))
    print(("PASS" if ok else "FAIL") + " | " + name)

def main():
    print("=== C3 tests ===")
    for n in (0,1,5,10,18,20):
        check("silnia("+str(n)+") iter=rec",
              factorial_iterative(n), factorial_recursive(n))
    check("18! wartosc", factorial_iterative(18), 6402373705728000)
    for L in (0,258,-258,999,100):
        check("suma cyfr "+str(L), digit_sum_iterative(L), digit_sum_recursive(L))
    for a,n in [(2,0),(2,1),(2,10),(2,15),(3.5,7)]:
        methods = [power_iterative, power_recursive,
                   power_square_iterative, power_square_recursive]
        vals = [m(a,n)[0] for m in methods]
        check("potega {}^{} 4 metody".format(a,n), max(vals)-min(vals) < 1e-6, True)
    # realny pomiar: 18! x 1 000 000 (10 mln zajelowby ~minute; 1 mln wystarcza dla testu)
    n, reps = 18, 1000000
    vi, ti = measure(factorial_iterative, n, reps)
    vr, tr = measure(factorial_recursive, n, reps)
    print("--- TIMING (real) ---")
    print("n={}, repeats={}".format(n, reps))
    print("iterative: {:.4f}s, recursive: {:.4f}s, ratio: {:.2f}".format(ti, tr, ti/tr if tr else 0))
    print("--- multiplications for a=2, n=0..15 (sq-iter vs iter) ---")
    for n in (5,10,15):
        print("n={:2d}: iter={:2d}, sq-iter={:2d}".format(
            n, power_iterative(2,n)[1], power_square_iterative(2,n)[1]))
    failed = sum(1 for c in CASES if not c[3])
    print("TOTAL: {} | PASSED: {} | FAILED: {}".format(len(CASES), len(CASES)-failed, failed))

if __name__ == "__main__":
    main()
