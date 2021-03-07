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
import time
from random import randint


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


# Задача №1. Алгоритмы нахождения i-того по счету простого числа.

@decor
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@decor
def eratosthenes_sieve(i):
    """С использованием «Решета Эратосфена»"""
    n = 2
    l = 100000
    search_list = [num for num in range(l)]
    search_list[1] = 0
    while n < l:
        if search_list[n] != 0:
            x = n * 2
            while x < l:
                search_list[x] = 0
                x += n
        n += 1
    return [el for el in search_list if el != 0][i - 1]


"""
Введите порядковый номер искомого простого числа: 5000
Простой вариант:
Затрачено памяти: 0.0546875
Затрачено времени: 38.289618730545044
Решето:
Затрачено памяти: 0.3984375
Затрачено времени: 0.12265920639038086

Алгоритм «Решето Эратосфена» затрачивает на решение немного больше памяти, но при этом имеет огромное
преимущество во времени выполнения. Но это работает только на больших данных. 
Связано это со сложностью алгоритмов - простой имеет сложность O(n^2), а решето O(n log (log n)).
"""


# Задача № 2. Осуществить перевод числа в строку для каждого элемента списка.

@decor
def func_1():
    test_list = [str(i) for i in range(30000000)]
    return test_list


@decor
def func_2():
    test_list = map(str, range(30000000))
    return test_list


"""
func_1:
Затрачено памяти: 1195.84375
Затрачено времени: 8.658836841583252
func_2
Затрачено памяти: 0.0
Затрачено времени: 0.0

Получить для второй функции числа отличные от нуля так и не удалось. При увеличении количества элементов получаю
MemoryError. Так что оптимизация при помощи map показала себя прекрасно, на максимально больших данных минимальные затраты.
"""


# Задача №3. Найти минимальное число в списке.

@decor
def min_number_bad(numbers):
    new_lst = list(range(100000000))
    for i in numbers:
        test_min = i
        for j in numbers:
            if j < test_min:
                test_min = j
        return test_min


@decor
def min_number_good1(numbers):
    new_lst = list(range(100000000))
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num


@decor
def min_number_good2(numbers):
    new_lst = list(range(100000000))
    return min(numbers)


"""
min_number_bad O(n^2):
Затрачено памяти: 0.328125
Затрачено времени: 2.720921039581299
min_number_good1 O(n):
Затрачено памяти: 0.0
Затрачено времени: 2.682525157928467
min_number_good2 O(n):
Затрачено памяти: 0.0
Затрачено времени: 2.6925699710845947

По сложности алгоритма первый вариант функции является неудачным, это заметно и по объему памяти.
"""


# Задача №4. Заполнение данными кортежа и списка.

@decor
def create_list(old_list):
    new_lst = list(range(100000000))
    new_list = [x ** 3 for x in old_list if x % 2 == 1]
    return new_list


@decor
def create_tuple(old_list):
    new_lst = list(range(100000000))
    new_tuple = (x ** 3 for x in old_list if x % 2 == 1)
    return new_tuple


"""
Создание списка:
Затрачено памяти: 13.4921875
Затрачено времени: 2.942030668258667
Создание кортежа:
Затрачено памяти: 0.0
Затрачено времени: 2.70406436920166

Для кортежа не удалось получить отличные от нуля затраты памяти, так что разница со списком очень большая. 
Но при этом функции имеют равные показатели во времени.
"""


simple(5000)
eratosthenes_sieve(5000)

func_1()
func_2()

my_list = [randint(10, 1000) for el in range(1000000)]

min_number_bad(my_list)
min_number_good1(my_list)
min_number_good2(my_list)

create_list(my_list)
create_tuple(my_list)
