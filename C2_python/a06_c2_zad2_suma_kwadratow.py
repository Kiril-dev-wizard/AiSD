#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C2_60, Zadanie 2: suma kwadratow kolejnych liczb calkowitych."""
def read_input():
    l0 = int(input("L0 = "))
    n = int(input("n = "))
    return l0, n

def sum_of_squares(l0, n):
    """Sumuje kwadraty n kolejnych liczb poczawszy od L0 (petla)."""
    total = 0
    for i in range(n):
        total += (l0 + i) ** 2
    return total

def print_result(l0, n, total):
    print("L0={}, n={}, S={}".format(l0, n, total))

def run():
    l0, n = read_input()
    print_result(l0, n, sum_of_squares(l0, n))

if __name__ == "__main__":
    run()
