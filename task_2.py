"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
from random import randint


# O(n^2)
def min_number_bad(numbers):
    for i in numbers:               # O(n)
        test_min = i                # O(1)
        for j in numbers:           # O(n)
            if j < test_min:        # O(1)
                test_min = j        # O(1)
        return test_min             # O(1)


# O(n)
def min_number_good1(numbers):
    min_num = numbers[0]            # O(1)
    for i in numbers:               # O(n)
        if i < min_num:             # O(1)
            min_num = i             # O(1)
    return min_num                  # O(1)


# O(n)
def min_number_good2(numbers):
    return min(numbers)             # return - O(1), min(lst) - O(n)


my_list = [randint(0, 100) for el in range(10)]

print(min_number_bad(my_list))
print(min_number_good1(my_list))
print(min_number_good2(my_list))
