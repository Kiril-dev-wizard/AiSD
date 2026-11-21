#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C3_51, Zadanie 1: silnia iteracyjnie i rekurencyjnie (w kolumnach)."""
def read_number():
    """Funkcja a: czyta liczbe od uzytkownika."""
    return int(input("n = "))

def factorial_recursive(n):
    """Funkcja b: silnia rekurencyjnie."""
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Funkcja c: silnia iteracyjnie."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def print_results(n, iterative, recursive):
    """Procedura d: wypisuje wyniki w wyrownanych kolumnach."""
    print("Silnia iteracyjnie:  {:d}".format(iterative))
    print("Silnia rekurencyjnie:{:d}".format(recursive))

def run():
    """Procedura e: sterujaca."""
    n = read_number()
    print_results(n, factorial_iterative(n), factorial_recursive(n))

if __name__ == "__main__":
    run()
