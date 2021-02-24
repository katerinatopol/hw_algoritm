"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, ]


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memoize
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@memoize
def func_3():
    a = [array.count(i) for i in array]
    max_count = max(a)
    elem = array[a.index(max_count)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))
print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))
print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000))

"""
Время работы функций:
0.0558275
0.0679132
0.06557370000000001
Заметной разницы нет, только первая функция немного быстрее за счет отсутствия max()

Время работы функций с использованием декоратора:
0.003314399999999995
0.0035734000000000044
0.002770800000000004
Снова получаются близкие значения, причем при перезапуске и при использовании других входных данных за меньшее время
может выполняться любая из функций.

"""