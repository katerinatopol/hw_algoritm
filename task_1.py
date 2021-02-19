"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def time_manager(func):
    def timer(*args, **kwargs):
        start_val = time.time()
        result = func(*args, **kwargs)
        end_val = time.time()
        print(end_val - start_val)
        return result

    return timer


@time_manager
def create_list(n):
    my_list = [i for i in range(n)]
    return my_list


@time_manager
def create_dict(n):
    my_dict = {i: f"val {i}" for i in range(n)}
    return my_dict


@time_manager
def search_list(my_list):
    for i in my_list:
        if i == 500000:
            return i


@time_manager
def search_dict(my_dict):
    return my_dict.get(500000)


@time_manager
def pop_list(my_list):
    return my_list.pop(100000)


@time_manager
def pop_dict(my_dict):
    return my_dict.pop(100000)


@time_manager
def add_list(my_list, n):
    for i in range(n):
        my_list.append({i})


@time_manager
def add_dict(my_dict, n):
    for i in range(n):
        my_dict.update({i: f"val {i}"})


@time_manager
def clear_list(my_list):
    my_list.clear()


@time_manager
def clear_dict(my_dict):
    my_dict.clear()


test_list = create_list(15000000)  # 1.312520980834961
test_dict = create_dict(15000000)  # 10.159784317016602
print()
# Генерация (создание) словаря заняло существенно больше времени, т.к. для каждого ключа вычисляется хеш.
# Но разница во времени становится заметной только при генерации очень большого количества элементов.

search_list(test_list)      # 0.09470462799072266
search_dict(test_dict)      # 0.0
print()
# Поиск элемента по значению в списке происходит значительно дольше, т.к. в словаре поиск по ключу использует хеш.

pop_list(test_list)  # 0.14760446548461914
pop_dict(test_dict)  # 0.0
print()
# Несмотря на то, что .pop и для списка и для словаря имеют константное время, у словаря он работает быстрее.
# Так как поиск элемента происходит по хешу ключа.

add_list(test_list, 10000)       # 0.9604291915893555
add_dict(test_dict, 10000)       # 0.013962030410766602
print()
# Всегда получается очень близкое время выполнения.

clear_list(test_list)       # 0.5385589599609375
clear_dict(test_dict)       # 1.9757165908813477
print()
# .clear выполняется за константное время, но у словаря получается время в среднем 3-4 раза больше
