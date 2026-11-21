#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C3_51, Zadanie 3: pomiar czasu silni (18!, 10 mln wywolan)."""
from datetime import datetime

def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def measure(func, n, repeats):
    """Mierzy czas wykonania func(n) repeats razy. Zwraca (wynik, sekundy)."""
    t0 = datetime.today()
    for _ in range(repeats):
        value = func(n)
    t1 = datetime.today()
    elapsed = (t1 - t0).total_seconds()
    return value, elapsed

def read_parameters():
    n = int(input("Argument silni (np. 18) = "))
    repeats = int(input("Liczba powtorzen = "))
    return n, repeats

def print_results(n, repeats, vi, ti, vr, tr):
    print("Argument silni: {}".format(n))
    print("Liczba powtorzen: {}".format(repeats))
    print("Silnia iteracyjnie: {}, czas: {:.2f} s".format(vi, ti))
    print("Silnia rekurencyjnie: {}, czas: {:.2f} s".format(vr, tr))
    if ti != tr:
        print("Roznica: iterator/recursion = {:.2f}x".format(ti / tr if tr else 0))

def run():
    n, repeats = read_parameters()
    vi, ti = measure(factorial_iterative, n, repeats)
    vr, tr = measure(factorial_recursive, n, repeats)
    print_results(n, repeats, vi, ti, vr, tr)

if __name__ == "__main__":
    run()
