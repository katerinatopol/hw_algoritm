"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
from timeit import timeit
from random import randint


# O(n^2)
#@profile()
def min_number_bad(numbers):
   # new_lst = list(range(1000000))
    for i in numbers:  # O(n)
        test_min = i  # O(1)
        for j in numbers:  # O(n)
            if j < test_min:  # O(1)
                test_min = j  # O(1)
        return test_min  # O(1)


# O(n)
#@profile()
def min_number_good1(numbers):
    min_num = numbers[0]  # O(1)
    for i in numbers:  # O(n)
        if i < min_num:  # O(1)
            min_num = i  # O(1)
    return min_num  # O(1)


# O(n)
#@profile()
def min_number_good2(numbers):
    return min(numbers)  # return - O(1), min(lst) - O(n)


my_list = [randint(10, 1000) for el in range(1000000)]

print(min_number_bad(my_list))
print(timeit(
    'min_number_bad(my_list)',
    globals=globals(),
    number=1000))
# print(min_number_good1(my_list))
# print(timeit(
#     'min_number_good1(my_list)',
#     globals=globals(),
#     number=1000))
# print(min_number_good2(my_list))
# print(timeit(
#     'min_number_good2(my_list)',
#     globals=globals(),
#     number=1000))

'''
Line #    Mem usage    Increment   Line Contents
================================================
    30     29.0 MiB     29.0 MiB   @profile()
    31                             def min_number_bad(numbers):
    32     48.2 MiB     19.2 MiB       new_lst = list(range(1000000))
    33     48.2 MiB      0.0 MiB       for i in numbers:  # O(n)
    34     48.2 MiB      0.0 MiB           test_min = i  # O(1)
    35     48.2 MiB      0.0 MiB           for j in numbers:  # O(n)
    36     48.2 MiB      0.0 MiB               if j < test_min:  # O(1)
    37     48.2 MiB      0.0 MiB                   test_min = j  # O(1)
    38     48.1 MiB      0.0 MiB           return test_min  # O(1)
    
    
Line #    Mem usage    Increment   Line Contents
================================================
    42     29.3 MiB     29.3 MiB   @profile()
    43                             def min_number_good1(numbers):
    44     29.3 MiB      0.0 MiB       min_num = numbers[0]  # O(1)
    45     29.3 MiB      0.0 MiB       for i in numbers:  # O(n)
    46     29.3 MiB      0.0 MiB           if i < min_num:  # O(1)
    47     29.3 MiB      0.0 MiB               min_num = i  # O(1)
    48     29.3 MiB      0.0 MiB       return min_num  # O(1)
    
Line #    Mem usage    Increment   Line Contents
================================================
    52     29.3 MiB     29.3 MiB   @profile()
    53                             def min_number_good2(numbers):
    54     29.3 MiB      0.0 MiB       return min(numbers)  # return - O(1), min(lst) - O(n)

121.9608413 / 73.53679699999999
78.3048479
36.867253500000004

'''
