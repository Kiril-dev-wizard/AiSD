#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C2_60, Zadanie 3: rok przestepny (4 funkcje, programowanie strukturalne)."""
def read_year():
    """Funkcja 1: czyta rok od uzytkownika i go zwraca."""
    return int(input("R = "))

def is_leap_year(year):
    """Funkcja 2:logiczna funkcja sprawdzajaca rok przestepny."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_result(year, leap):
    """Funkcja 3: procedure wypisujaca wynik."""
    if leap:
        print("Rok {} jest przestepny".format(year))
    else:
        print("Rok {} nie jest przestepny".format(year))

def run():
    """Funkcja 4: procedura sterujaca."""
    year = read_year()
    print_result(year, is_leap_year(year))

if __name__ == "__main__":
    run()
