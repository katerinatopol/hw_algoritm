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
import json

from memory_profiler import memory_usage
from timeit import default_timer
from random import randint


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start_val = default_timer()
        res = func(*args, **kwargs)
        end_val = default_timer()
        m2 = memory_usage()
        mem_res = m2[0] - m1[0]
        time_res = end_val - start_val
        print(f'Затрачено памяти: {mem_res}')
        print(f'Затрачено времени: {time_res}')
        return res

    return wrapper

# json-object


@decor
def my_dict():
    return {i: i for i in range(100000)}


@decor
def json_dict():
    result = {i: i for i in range(100000)}
    result = json.dumps(result)
    return result


my_dict()
json_dict()

print(
    'При приведении словаря в json наблюдается понижение затрат памяти в несолько раз, при этом дополнительно затрачивается больше времени. Отдам предпочтение в пользу экономии памяти')

