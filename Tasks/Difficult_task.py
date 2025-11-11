#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x = int(input("Введите x: "))
    n = 0
    c = 0

    sign = 1    # (-1) ** n
    factorial_part = 1.0    # factorial(2 * n)
    pi2_sq = (math.pi / 2) ** 2
    pi_power = 1.0    # (pi / 2) ** (2 * n)
    x_power = x    # x ** (4 * n + 1), при n = 0 -> x ** 1

    while True:
        # Вычисление члена ряда.
        term = sign * pi_power * x_power / (factorial_part * (4 * n + 1))
        c += term

        # Условие точности.
        if abs(term) < 1e-10:
            break

        # Подготовка для следующего n
        n += 1
        sign = -sign
        factorial_part *= (2 * n - 1) * (2 * n)
        pi_power *= pi2_sq
        x_power *= x ** 4

    print(f"C({x}) ≈ {c:.10f}, число членов ряда = {n + 1}")
