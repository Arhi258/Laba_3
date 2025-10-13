#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_word_form(number, forms):
    """
    Возвращает правильную форму слова в зависимости от числа.
    forms: кортеж из трех форм.
    """
    last_digit = number % 10
    last_two = number % 100

    if 11 <= last_two <= 14:
        return forms[2]
    elif last_digit == 1:
        return forms[0]
    elif last_digit in (2, 3, 4):
        return forms[1]
    else:
        return forms[2]


if __name__ == '__main__':
    time = int(input("Введите время, которое дается амебе на размножение (часы): "))

    # Сколько раз поделится амеба за указанное время.
    number_of_divisions = time // 3
    number_of_amoebas = 2 ** number_of_divisions

    hour_word = get_word_form(time, ('час', 'часа', 'часов'))
    amoeba_word = get_word_form(number_of_amoebas, ('клетка', 'клетки', 'клеток'))

    print(f"За {time} {hour_word} будет {number_of_amoebas} {amoeba_word}")
