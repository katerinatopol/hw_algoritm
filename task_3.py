"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from timeit import timeit
from collections import deque

my_list = [i for i in range(100)]
my_deque = deque([i for i in range(100)])


# Добавление элементов в конец списка
def list_append_post(nums):
    for i in nums:
        my_list.append(i)


def deque_append_post(nums):
    for i in nums:
        my_deque.append(i)


# Добавление элементов в начало списка
def list_append_start(nums):
    for i in nums:
        my_list.insert(0, i)


def deque_append_start(nums):
    for i in nums:
        my_deque.appendleft(i)


# Удаление элементов из конца списка
def list_pop_post():
    for i in range(100):
        my_list.pop()


def deque_pop_post():
    for i in range(100):
        my_deque.pop()


# Удаление элементов из начала списка
def list_pop_start():
    for i in range(100):
        my_list.pop(0)


def deque_pop_start():
    for i in range(100):
        my_deque.popleft()


# Стандартные методы
def list_check():
    my_list.extend([i for i in range(100)])
    my_list.insert(0, 1000)
    my_list.remove(80)
    my_list.count(10)
    my_list.reverse()
    my_list.clear()


def deque_check():
    my_deque.extend([i for i in range(100)])
    my_deque.insert(0, 1000)
    my_deque.remove(80)
    my_deque.count(10)
    my_deque.reverse()
    my_deque.clear()


test_nums = [i for i in range(150, 300)]
print('Добавление элементов в конец списка')
print(timeit("list_append_post(test_nums)", globals=globals(), number=1000))        # 0.028197299999999995
print(timeit("deque_append_post(test_nums)", globals=globals(), number=1000))       # 0.021489900000000006

print('Добавление элементов в начало списка')
print(timeit("list_append_start(test_nums)", globals=globals(), number=1000))       # 21.0396133
print(timeit("deque_append_start(test_nums)", globals=globals(), number=1000))      # 0.021558899999998715

print('Удаление элементов из конца списка')
print(timeit("list_pop_post()", globals=globals(), number=1000))        # 0.015097900000000664
print(timeit("deque_pop_post()", globals=globals(), number=1000))       # 0.013035500000000866

print('Удаление элементов из начала списка')
print(timeit("list_pop_start()", globals=globals(), number=1000))       # 2.7724551999999996
print(timeit("deque_pop_start()", globals=globals(), number=1000))      # 0.013205899999999104

print('Стандартные методы')
print(timeit("list_check()", globals=globals(), number=1000))       # 0.015509399999999118
print(timeit("deque_check()", globals=globals(), number=1000))      # 0.017891499999997507

'''
appendleft и popleft работают существенно быстрее аналогов для списка. 
Время выполнения стандартных методов примерно одинаковое. Соответственно если не требуются специфические
методы deque, то стоит использовать обычный список.
'''
