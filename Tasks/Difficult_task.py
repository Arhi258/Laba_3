#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x = int(input("Введите x: "))
    n = 0
    c = 0

    while True:
        # Вычисление члена ряда.
        term = (
            ((-1) ** n * (math.pi / 2) ** (2 * n)) /
            (math.factorial(2 * n) * (4 * n + 1)) *
            x ** (4 * n + 1)
        )
        c += term
        # Условие точности.
        if abs(term) < 1e-10:
            break
        n += 1

    print(f"C({x}) ≈ {c:.10f}, число членов ряда = {n + 1}")
