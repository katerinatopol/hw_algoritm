"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
import random
from statistics import median
from timeit import timeit


# Гномья сортировка
def gnome_sort(arr):
    data = arr.copy()
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


# Поиск с помощью создания списков
def list_clear(arr):
    left = []
    right = []
    for i in arr:
        for j in arr:
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)

        if len(left) == len(right):
            return i
        left.clear()
        right.clear()


# Алгоритм «quickselect»
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(arr, k, pivot_fn):
    l = arr.copy()
    if len(l) == 1:
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


# Замеры

print('Массив 11 элементов')
m = 10
orig_list = [random.randint(-200, 200) for i in range(2 * m + 1)]
sorted_list = gnome_sort(orig_list)

print(f'Гномья сортировка: {sorted_list[m]}')
print(timeit('gnome_sort(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Поиск с помощью списков: {list_clear(orig_list[:])}')
print(timeit('list_clear(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Алгоритм «quickselect»: {quickselect_median(orig_list[:])}')
print(timeit('quickselect_median(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Median statistics: {median(orig_list[:])}')
print(timeit('median(orig_list[:])',
             globals=globals(),
             number=1000))

print('Массив 101 элемент')
m = 100
orig_list = [random.randint(-200, 200) for i in range(2 * m + 1)]
sorted_list = gnome_sort(orig_list)

print(f'Гномья сортировка: {sorted_list[m]}')
print(timeit('gnome_sort(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Поиск с помощью списков: {list_clear(orig_list[:])}')
print(timeit('list_clear(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Алгоритм «quickselect»: {quickselect_median(orig_list[:])}')
print(timeit('quickselect_median(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Median statistics: {median(orig_list[:])}')
print(timeit('median(orig_list[:])',
             globals=globals(),
             number=1000))

print('Массив 1001 элемент')
m = 1000
orig_list = [random.randint(-200, 200) for i in range(2 * m + 1)]
sorted_list = gnome_sort(orig_list)

print(f'Гномья сортировка: {sorted_list[m]}')
print(timeit('gnome_sort(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Поиск с помощью списков: {list_clear(orig_list[:])}')
print(timeit('list_clear(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Алгоритм «quickselect»: {quickselect_median(orig_list[:])}')
print(timeit('quickselect_median(orig_list[:])',
             globals=globals(),
             number=1000))

print(f'Median statistics: {median(orig_list[:])}')
print(timeit('median(orig_list[:])',
             globals=globals(),
             number=1000))


"""
Массив 11 элементов
Гномья сортировка: 0.11262340000000001
Поиск с помощью списков: 0.033257900000000035
Алгоритм «quickselect»: 0.06790599999999997
Median statistics: 0.004273099999999974

Массив 101 элемент
Гномья сортировка: 8.2169159
Поиск с помощью списков: 9.486337
Алгоритм «quickselect»: 0.22456359999999975
Median statistics: 0.0204166999999984
Массив 1001 элемент
Гномья сортировка: 908.1307319
Поиск с помощью списков: 938.660314
Алгоритм «quickselect»: 2.2313936000000467
Median statistics: 0.44405060000008234

Median statistics я использовала для контроля правильности расчетов.
Гномья сортировка - это сортировка исходного массива, и в последствии мы определяем элемент с индексом m который
всегда будет являться медианой в отсортированном массиве.
Поиск медианы при помощи списков не выигрывает по времени у гномьей сортировки, а на небольших массивах даже
уступает. Но при этом он не использует сортировку.
Оптимальным является алгоритм «quickselect». Этот способ рекурсивный, у него есть улучшенная версия, но я остановилась
на этой, т.к. она проще для понимания. Быстрая сортировка показывает лучшие результаты времени, уступая только функции 
median из модуля statistics.

"""
