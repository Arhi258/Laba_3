#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    x = float(input("Введите x: "))

    if abs(x) > 20:
         print(
             "Слишком большое значение x для рекуррентного метода",
             file=sys.stderr
         )
         exit(1)

    if x == 0:
        C = 0.0
    else:
        sign = 1.0
        if x < 0:
            x = -x
            sign = -1.0

        # Однократные вычисления
        p2 = (math.pi / 2) ** 2
        x4 = x ** 4
        work = p2 * x4

        # Начальный член ряда
        a = x
        summ = a

        # Основной цикл рекурентного ряда
        k = 1
        while True:
            # Рекуррентный коэффициент
            r = - (
                    work * (4 * k - 3)
            ) / (
                    (2 * k) * (2 * k - 1) * (4 * k + 1)
            )

            a *= r
            summ += a

            # Проверка точности
            if abs(a) < 1e-10:
                break

            k += 1

        C = sign * summ

    print(f"C = {C}")

