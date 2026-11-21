#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C2_60, Zadanie 1: rownanie kwadratowe ax^2+bx+c=0."""
import math

def read_coefficients():
    """Czyta wspolczynniki a, b, c od uzytkownika."""
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    return a, b, c

def solve(a, b, c):
    """Zwraca opis rozwiazania rownania kwadratowego."""
    if a == 0:
        if b == 0:
            return "rownanie sprzeczne" if c != 0 else "nieskonczona liczba rozwiazan"
        return ("jedno rozwiazanie", -c / b)
    delta = b*b - 4*a*c
    if delta < 0:
        return ("brak rozwiazan rzeczywistych",)
    if delta == 0:
        return ("jedno rozwiazanie podwojne", -b / (2*a))
    return ("dwa rozwiazania", (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a))

def print_result(result):
    """Wypisuje wynik na konsoli (bez polskich znakow diakrytycznych)."""
    kind = result[0]
    if kind == "dwa rozwiazania":
        print("x1 = {:.4f}, x2 = {:.4f}".format(result[1], result[2]))
    elif kind in ("jedno rozwiazanie", "jedno rozwiazanie podwojne"):
        print("x = {:.4f}".format(result[1]))
    else:
        print(kind)

def run():
    """Procedura sterujaca."""
    a, b, c = read_coefficients()
    print_result(solve(a, b, c))

if __name__ == "__main__":
    run()
