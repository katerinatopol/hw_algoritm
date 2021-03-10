"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


numb = int(input('Введите число элементов: '))
orig_list = [random.uniform(0, 50) for _ in range(numb)]
sorted_list = merge_sort(orig_list[:])
print(f'Исходный массив: {orig_list}')
print(f'Отсортированный: {sorted_list}')

# замеры 10
orig_list = [random.uniform(0, 50) for _ in range(10)]
print(timeit(
    'merge_sort(orig_list[:])',
    globals=globals(),
    number=1000))

# замеры 100
orig_list = [random.uniform(0, 50) for _ in range(100)]
print(timeit(
    'merge_sort(orig_list[:])',
    globals=globals(),
    number=1000))

# замеры 1000
orig_list = [random.uniform(0, 50) for _ in range(1000)]
print(timeit('merge_sort(orig_list[:])',
             globals=globals(),
             number=1000))


"""
Введите число элементов: 5
Исходный массив: [43.81625326034019, 30.8575459567424, 30.714754621325547, 39.37577528980714, 15.629488246645963]
Отсортированный: [15.629488246645963, 30.714754621325547, 30.8575459567424, 39.37577528980714, 43.81625326034019]
Длина массива 10: 0.03316680000000005
Длина массива 100: 0.37318260000000025
Длина массива 1000: 5.461328
В данной реализации алгоритм разделен на две части(функции). По существу он не сильно отличается от предложенного
в методичке, хотя и выглядит совсем по другому. 
Результаты такой сортировки значительно превосходят результаты из первого задания(пузырьковую сортировку).
"""
