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
import memory_profiler
from numpy import array
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


# 1 Оптимизирование памяти с помощью генератора

@decor
def even_numbers_1(num):
    result = [el for el in range(num + 1) if el % 2 == 0]
    return result


@decor
def even_numbers_2(num):
    num_list = list(range(num + 1))
    for el in num_list:
        if el % 2 == 0:
            yield el


even_numbers_1(100000000)
even_numbers_2(100000000)

'''
Вариант со списковым включением:
Затрачено памяти: 559.21875
Затрачено времени: 28.091166973114014
Вариант с генератором:
Затрачено памяти: 0.30078125
Затрачено времени: 0.0

Полученные результаты однозначно показывают преимущества генератора, т.к. сокращение затрат памяти существенное.
Но недостаток этого способа в том, что результаты вычислений генератора мы не можем в дальнейшем использовать,
получаем только один раз. Если это удовлетворяет требования, то стоит сделать выбор в пользу генератора.
'''


# 2 Использование array из библиотеки numpy вместо обычного списка

@decor
def simple_list(num):
    return list(range(num))


@decor
def numpy_array(num):
    return array(range(num))


simple_list(10000000)
numpy_array(10000000)

"""
Обычный список:
Затрачено памяти: 191.9375
Затрачено времени: 0.3569808006286621
Array:
Затрачено памяти: 38.35546875
Затрачено времени: 2.092564582824707

Использование библиотеки NumPy позволяет существенно сэкономить память при работе с большим списком. Но при этом она
показывает худшие результаты во времени. Для маленьких массивов лучше использовать обычный list.
"""


# 3 Использование слотов

class User:

    def __init__(self, name, surname, city, phone, birthday):
        self.name = name
        self.surname = surname
        self.city = city
        self.phone = phone
        self.birthday = birthday

    def info(self):
        return ' '. join([self.name, self.surname, self.city, self.phone, self.birthday])


@decor
def info_simple(obj):
    return obj.info()


class User2:
    __slots__ = ['name', 'surname', 'city', 'phone', 'birthday']

    def __init__(self, name, surname, city, phone, birthday):
        self.name = name
        self.surname = surname
        self.city = city
        self.phone = phone
        self.birthday = birthday

    def info(self):
        return ' '. join([self.name, self.surname, self.city, self.phone, self.birthday])


@decor
def info_slots(obj):
    return obj.info()


user_1 = User('Nick', 'User', 'Omsk', '89999999999', '12.12.2012')
user_2 = User2('Nick', 'User2', 'Tomsk', '89999999999', '12.12.2012')

info_simple(user_1)
info_slots(user_2)

'''
Обычный класс, на основе словаря
Затрачено памяти: 0.00390625
Затрачено времени: 0.0
С использованием слотов
Затрачено памяти: 0.0
Затрачено времени: 0.0

Количество затраченой памяти уменьшилось при использовании слотов, но не на много. Также при использовании слотов
есть сложности с множественным наследованием классов. Так что необходимо тестировать такой способ оптимизации
относительно каждой конкретной задачи.
'''
