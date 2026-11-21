#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C2_60, Zadanie 4: suma cyfr metoda iteracyjna (4 funkcje)."""
def read_number():
    """Funkcja 1: czyta liczbe calkowita."""
    return int(input("L = "))

def digit_sum(number):
    """Funkcja 2: suma cyfr obliczana iteracyjnie (% i //)."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def print_result(number, total):
    """Funkcja 3: wypisuje wynik."""
    print("L={}, suma cyfr S={}".format(number, total))

def run():
    """Funkcja 4: procedura sterujaca."""
    number = read_number()
    print_result(number, digit_sum(number))

if __name__ == "__main__":
    run()
