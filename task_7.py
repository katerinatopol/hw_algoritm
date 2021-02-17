"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_number(n):
    if n == 1:
        return n
    else:
        return sum_number(n - 1) + n


while True:
    try:
        user_number = int(input('Введите число: '))
        if sum_number(user_number) == user_number * (user_number + 1) / 2:
            print("Выражения равны")
        else:
            print("Выражения не равны")
        break
    except ValueError as err:
        print(f'Возникла ошибка: {err}\nЭто не число, попробуйте еще раз.')