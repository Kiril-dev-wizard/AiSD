#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C3_51, Zadanie 4: suma cyfr iteracyjnie i rekurencyjnie."""
def read_number():
    return int(input("L = "))

def digit_sum_iterative(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def digit_sum_recursive(number):
    number = abs(number)
    return 0 if number == 0 else number % 10 + digit_sum_recursive(number // 10)

def print_results(number, iterative, recursive):
    print("Suma cyfr iteracyjnie:  {:d}".format(iterative))
    print("Suma cyfr rekurencyjnie:{:d}".format(recursive))

def run():
    number = read_number()
    print_results(number, digit_sum_iterative(number), digit_sum_recursive(number))

if __name__ == "__main__":
    run()
