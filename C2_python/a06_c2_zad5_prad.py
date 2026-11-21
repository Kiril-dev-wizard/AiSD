#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AiSD_C2_60, Zadanie 5 (opcjonalne): symulacja licznika energii.

Symulacja kilku sekund zamiast 365 dni. Moc czynna = P_INST * (1 + sin(t))/2,
moc bierna = 10% mocy czynnej. Taryfa I: 6-13 i 15-22, Taryfa II: reszta.
"""
import math

P_INST = 3.0  # kW, stala moc instalacji
DURATION = 10  # sekund symulacji (zamiast 365 dni)
START_HOUR = 6  # godzina startu symulacji

def control():
    """Procedura sterujaca programem."""
    e1c, e2c, e1b, e2b, max_power = simulate(P_INST, DURATION, START_HOUR)
    print_results(e1c, e2c + 0, e1b, e2b, max_power)

def simulate(p_inst, duration, start_hour):
    """Procedura wykonujaca algorytm: zlicza energie w kWh i maks. moc."""
    e1c = e2c = e1b = e2b = 0.0
    max_power = 0.0
    for t in range(duration):
        hour = (start_hour + t // 3600) % 24
        active = p_inst * (1 + math.sin(t)) / 2.0
        reactive = 0.1 * active
        tariff_i = (6 <= hour < 13) or (15 <= hour < 22)
        if tariff_i:
            e1c += active / 3600.0
            e1b += reactive / 3600.0
        else:
            e2c += active / 3600.0
            e2b += reactive / 3600.0
        max_power = max(max_power, active)
    return e1c, e2c, e1b, e2b, max_power

def print_results(e1c, e2c, e1b, e2b, max_power):
    """Procedura wyswietlajaca wyniki koncowe."""
    print("E1_active={:.8f} kWh".format(e1c))
    print("E2_active={:.8f} kWh".format(e2c))
    print("E1_reactive={:.8f} kWh".format(e1b))
    print("E2_reactive={:.8f} kWh".format(e2b))
    print("Max_active_power={:.4f} kW".format(max_power))

if __name__ == "__main__":
    control()
