"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import timeit
from memory_profiler import profile
import memory_profiler
import time


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_val = time.time()
        res = func(*args, **kwargs)
        end_val = time.time()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_res = end_val - start_val
        print(f'Затрачено памяти: {mem_diff}')
        print(f'Затрачено времени: {time_res}')
        return res
    return wrapper


@decor
def func_1():
    my_list = [str(i) for i in range(10000000)]
    return my_list


@decor
def func_2():
    my_list = map(str, range(10000000))
    return my_list


func_1()
func_2()
# print(timeit(
#     'func_1',
#     globals=globals(),
#     number=1000))
# print(timeit(
#     'func_2',
#     globals=globals(),
#     number=1000))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    26     13.4 MiB     13.4 MiB   @profile()
    27                             def func_1():
    28     16.9 MiB      0.2 MiB       my_list = [str(i) for i in range(100000)]
    29     16.9 MiB      0.0 MiB       return my_list
    
Line #    Mem usage    Increment   Line Contents
================================================
    32     13.6 MiB     13.6 MiB   @profile()
    33                             def func_2():
    34     13.6 MiB      0.0 MiB       my_list = map(str, range(100000))
    35     13.6 MiB      0.0 MiB       return my_list
    

"""