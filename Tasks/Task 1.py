#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    season_number = int(input("Введите номер времени года (1-4): "))

    if season_number == 1:
        print("Декабрь, Январь, Февраль")
    elif season_number == 2:
        print("Март, Апрель, Май")
    elif season_number == 3:
        print("Июнь, Июль, Август")
    elif season_number == 4:
        print("Сентябрь, Октябрь, Ноябрь")
    else:
        print("Неверно введённое число!", file=sys.stderr)
        sys.exit(1)
