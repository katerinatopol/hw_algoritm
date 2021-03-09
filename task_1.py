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
    copy_list = lst_obj.copy()
    while n < len(copy_list):
        for i in range(1, len(copy_list)):
            if copy_list[i] > copy_list[i - 1]:
                copy_list[i], copy_list[i - 1] = copy_list[i - 1], copy_list[i]
        n += 1
    return copy_list


def bubble_sort_waning_2(lst_obj):
    n = 1
    change = 0
    copy_list = lst_obj.copy()
    while n < len(copy_list):
        for i in range(1, len(copy_list)):
            if copy_list[i] > copy_list[i - 1]:
                copy_list[i], copy_list[i - 1] = copy_list[i - 1], copy_list[i]
                change += 1
        if change == 0:
            break
        n += 1
    return copy_list


orig_list = list(reversed(range(100)))
#orig_list = [random.randint(-100, 100) for _ in range(10)]
waning_list = bubble_sort_waning(orig_list)
print(f'Исходный массив: {orig_list}\n'
      f'Отсортированный массив: {waning_list}')

waning_list_2 = bubble_sort_waning_2(orig_list)
print(f'Исходный массив: {orig_list}\n'
      f'Отсортированный массив: {waning_list_2}')

# замеры 10
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

#orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
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

#orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
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
0.1477274
0.05670120000000001
4.4305145
4.3303354
419.1640423
452.19307129999993
"""