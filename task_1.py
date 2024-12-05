"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

"""Сортировка пузырьком"""

import timeit
import random


def bubble_sort_waning(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(1, len(lst_obj)):
            if lst_obj[i] > lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_waning_2(lst_obj):
    n = 1
    change = 0
    while n < len(lst_obj):
        for i in range(1, len(lst_obj)):
            if lst_obj[i] > lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                change += 1
        if change == 0:
            break
        n += 1
    return lst_obj


# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
waning_list = bubble_sort_waning(orig_list[:])
waning_list_2 = bubble_sort_waning_2(orig_list[:])
print(f'Исходный массив: {orig_list}\n'
      f'Отсортированный массив: {waning_list}\n'
      f'Отсортированный массив (оптимизированная ф-я): {waning_list_2}')

print(
    timeit.timeit(
        "bubble_sort_waning(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_waning_2(orig_list[:])",
        globals=globals(),
        number=1000))


# замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]

print(
    timeit.timeit(
        "bubble_sort_waning(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_waning_2(orig_list[:])",
        globals=globals(),
        number=1000))


# замеры 1000
orig_list = [random.randint(-100, 100) for _ in range(1000)]

print(
    timeit.timeit(
        "bubble_sort_waning(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_waning_2(orig_list[:])",
        globals=globals(),
        number=1000))


"""
Исходный массив: [-76, 64, 70, -49, 47, -50, 92, -42, 46, -23]
Отсортированный массив: [92, 70, 64, 47, 46, -23, -42, -49, -50, -76]
Отсортированный массив (оптимизированная ф-я): [92, 70, 64, 47, 46, -23, -42, -49, -50, -76]
Массив 10:
0.0183264
0.018060800000000002
Массив 100:
1.6082512
1.6795950999999998
Массив 1000:
164.65353620000002
178.75705509999997
В качестве доработки я добавила переменную change, которая изменяется при переставлении элементов, и также
добавила ветку if с выходом из цикла если change осталась неизменной после прохода по списку.
Так как функции возвращают копию списка результаты корректны. При это время выполнения практически одинаковое.
Как и обсуждалось на вебинаре, вероятность создания изначально отсортированного массива практически 
отсутствует. 
"""
