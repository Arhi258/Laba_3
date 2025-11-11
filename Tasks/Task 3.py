#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    time = int(input("Введите время, которое дается амебе на размножение (часы): "))

    # Сколько раз поделится амеба за указанное время.
    number_of_divisions = time // 3
    number_of_amoebas = 2 ** number_of_divisions

    print(f"За {time} ч. количество клеток составит: {number_of_amoebas} ")
