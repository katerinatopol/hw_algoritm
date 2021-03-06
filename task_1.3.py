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
def simple(i):      # O(n^2)
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
def eratosthenes_sieve(i):      # O(n log (log n))
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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosthenes_sieve(i))

"""
Введите порядковый номер искомого простого числа: 5000
Простой вариант:
Затрачено памяти: 0.0546875
Затрачено времени: 38.289618730545044
Решето:
Затрачено памяти: 0.3984375
Затрачено времени: 0.12265920639038086

"""