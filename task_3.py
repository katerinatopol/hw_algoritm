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
    i, j, size = 1, 2, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i, j = j, j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return arr


# Поиск с помощью создания списков
def list_clear(arr):
    left = []
    right = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                left.append(arr[j])
            if arr[i] < arr[j]:
                right.append(arr[j])
            if arr[i] == arr[j] and i > j:
                left.append(arr[j])
            if arr[i] == arr[j] and i < j:
                right.append(arr[j])

        if len(left) == len(right):
            return arr[i]
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
sorted_list = gnome_sort(orig_list[:])

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
sorted_list = gnome_sort(orig_list[:])

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
sorted_list = gnome_sort(orig_list[:])

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
Гномья сортировка: 0.05461359999999999
Поиск с помощью списков: 0.202471
Алгоритм «quickselect»: 0.017477699999999985
Median statistics: 0.0011638999999999955
Массив 101 элемент
Гномья сортировка: 3.6699583
Поиск с помощью списков: 15.043529900000001
Алгоритм «quickselect»: 0.09482669999999871
Median statistics: 0.010804900000000117
Массив 1001 элемент
Гномья сортировка: 369.89616470000004
Поиск с помощью списков: 632.1794522
Алгоритм «quickselect»: 0.7774408999999878
Median statistics: 0.2298672000000579
Median statistics я использовала для контроля правильности расчетов.
Гномья сортировка - это сортировка исходного массива, и в последствии мы определяем элемент с индексом m который
всегда будет являться медианой в отсортированном массиве.
Поиск медианы при помощи списков существенно хуже всех остальных во времени. Но при этом он не использует сортировку.
Оптимальным является алгоритм «quickselect». Этот способ рекурсивный, у него есть улучшенная версия, но я остановилась
на этой, т.к. она проще для понимания. Быстрая сортировка показывает лучшие результаты времени, уступая только функции 
median из модуля statistics.
"""
