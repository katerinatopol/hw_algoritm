"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: [i] for i in range(1100)}
ordered_dict = OrderedDict({i: [i] for i in range(1100)})


def pop_simple():
    pop_dict = {i: [i] for i in range(1100)}
    pop_dict.pop(600)


def pop_ordered():
    pop_dict = OrderedDict({i: [i] for i in range(1100)})
    pop_dict.pop(600)


print(timeit("my_dict.keys()", globals=globals(), number=1000))         # 0.00015999999999999348
print(timeit("ordered_dict.keys()", globals=globals(), number=1000))    # 0.00016149999999999498

print(timeit("my_dict.values()", globals=globals(), number=1000))       # 0.00015460000000000473
print(timeit("ordered_dict.values()", globals=globals(), number=1000))  # 0.00016919999999999435

print(timeit("my_dict.items()", globals=globals(), number=1000))        # 0.0001598000000000016
print(timeit("ordered_dict.items()", globals=globals(), number=1000))   # 0.00016299999999999648

print(timeit("my_dict.get(80)", globals=globals(), number=1000))        # 0.0001361000000000001
print(timeit("ordered_dict.get(80)", globals=globals(), number=1000))   # 0.00014379999999999948

print(timeit("my_dict.popitem()", globals=globals(), number=1000))          # 0.0001895999999999981
print(timeit("ordered_dict.popitem()", globals=globals(), number=1000))     # 0.0003258000000000011

print(timeit("my_dict.setdefault(115)", globals=globals(), number=1000))        # 0.00015139999999999598
print(timeit("ordered_dict.setdefault(115)", globals=globals(), number=1000))   # 0.00014420000000001099

print(timeit("pop_simple()", globals=globals(), number=1))      # 0.00023729999999999585
print(timeit("pop_ordered()", globals=globals(), number=1))     # 0.0005194000000000032

print(timeit("my_dict.update({i: [i] for i in range(200, 300)})", globals=globals(), number=1000))          # 0.026754
print(timeit("ordered_dict.update({i: [i] for i in range(200, 300)})", globals=globals(), number=1000))     # 0.042436

print(timeit("my_dict.copy()", globals=globals(), number=1000))         # 0.002825499999999981
print(timeit("ordered_dict.copy()", globals=globals(), number=1000))    # 0.0329874

print(timeit("my_dict.clear()", globals=globals(), number=1000))        # 0.00018780000000001573
print(timeit("ordered_dict.clear()", globals=globals(), number=1000))   # 0.00016820000000000723


'''
Как видно из результатов, разница между обычным словарем и OrderedDict несущественная. В каких-то случаях
немного лучший результат принадлежит то одному варианту, то другому. Но разница не существена.
Так что в Python 3.6 и более поздних версиях использовать OrderedDict не имеет смысла.
'''
