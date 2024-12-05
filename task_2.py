"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        globals=globals(),
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        globals=globals(),
        number=10000))


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
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(),
        number=10000))


"""
Результат работы функций:
Не оптимизированная функция recursive_reverse
0.1353411
0.20576219999999995
0.16745290000000002
Оптимизированная функция recursive_reverse_mem
0.0059306999999999555
0.005247700000000077
0.008271299999999981
Мемоизация нужна, если планируется многократный вызов функции с повторяющимися числами. Тогда время выполнения 
оптимизированной функции значительно меньше. Так как при каждом последующем вызове используются ранее вычисленные 
значения. В случае если функция вызывается однократно - мемоизация не нужна (вычисленные значения не пригодятся.
"""
