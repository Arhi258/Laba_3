#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    a = float(input("Введите координату a = "))
    b = float(input("Введите координату b = "))
    r = math.sqrt(a ** 2 + b ** 2)
    if 0.5 <= r <= 1:
        print(f"Точка A({a}, {b}) принадлежит кольцу")
    else:
        print(f"Точка A({a}, {b}) не принадлежит кольцу")
