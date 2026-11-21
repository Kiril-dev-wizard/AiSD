#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C3_51, Zadanie 5: potega a^n - 4 metody, licznik mnozen."""
def power_iterative(a, n):
    """Iloczyn n raisonow a, licznik mnozen."""
    result, counter = 1.0, 0
    for _ in range(n):
        result *= a
        counter += 1
    return result, counter

def power_recursive(a, n):
    """Rekurencja: a^n = a * a^(n-1)."""
    if n == 0:
        return 1.0, 0
    value, counter = power_recursive(a, n - 1)
    return value * a, counter + 1

def power_square_iterative(a, n):
    """Podnoszenie do kwadratu (iteracyjnie, bitowy rozklad wykladnika)."""
    result, factor, counter = 1.0, a, 0
    exponent = n
    while exponent > 0:
        if exponent & 1:
            result *= factor
            counter += 1
        factor *= factor
        counter += 1
        exponent >>= 1
    return result, counter - 1 if n else 0

def power_square_recursive(a, n):
    """Podnoszenie do kwadratu (rekurencyjnie).

    a^0=1; a^(2k)=(a^k)^2; a^(2k+1)=a*(a^k)^2
    """
    if n == 0:
        return 1.0, 0
    half, c1 = power_square_recursive(a, n // 2)
    square, c2 = half * half, c1 + 1
    if n % 2 == 0:
        return square, c2
    return square * a, c2 + 1

def print_table(a, methods):
    print("a = {}".format(a))
    print("{:>3} | {:>12} | {:>3} | {:>12} | {:>3} | {:>12} | {:>3} | {:>12} | {:>3}".format(
        "n", "iter", "mul", "rec", "mul", "sq-iter", "mul", "sq-rec", "mul"))
    for n in range(0, 16):
        vi, ci = methods["iterative"](a, n)
        vr, cr = methods["recursive"](a, n)
        si, cs = methods["square_iterative"](a, n)
        sr, csr = methods["square_recursive"](a, n)
        print("{:>3} | {:>12.0f} | {:>3} | {:>12.0f} | {:>3} | {:>12.0f} | {:>3} | {:>12.0f} | {:>3}".format(
            n, vi, ci, vr, cr, si, cs, sr, csr))

def run():
    methods = {
        "iterative": power_iterative,
        "recursive": power_recursive,
        "square_iterative": power_square_iterative,
        "square_recursive": power_square_recursive,
    }
    print_table(2.0, methods)

if __name__ == "__main__":
    run()
