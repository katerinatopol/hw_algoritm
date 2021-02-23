"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


test_list = [i for i in range(10000)]
print(timeit("func_1(test_list)", setup="from __main__ import func_1, test_list", number=1000))
print(timeit("func_2(test_list)", setup="from __main__ import func_2, test_list", number=1000))

"""
Для оптимизации я изпользовала списковое включение. Так как метод append является очень затратным, необходимо было от 
него избавиться. Оптимизированный вариант в func_2. Время исполнения:
func_1   3.17613
func_2   1.6733885000000002
Соответственно списковое включении сократило время выполнения в два раза.
"""