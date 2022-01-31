""" binary search """
from math import floor


# TODO продумать не рекурсивный алгоритм
def binary_search(array, target):
    ind = floor(len(array) / 2) - 1
    el = array[ind]
    if el == target:
        return id(el)
    else:
        if el > target:
            array = array[:ind]
        else:
            array = array[ind + 1:]

        return binary_search(array, target)


if __name__ == '__main__':
    a = list(range(50))[1:]
    print(id(a[17]))
    print(binary_search(a, 18))
