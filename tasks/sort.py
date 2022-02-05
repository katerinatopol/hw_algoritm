""" selection sort """


def selection_sort(array):

    start_el = array[0]
    for ind, el in enumerate(array[1:]):
        if el < start_el:
            min_el = el
            index = ind
    array[0] = min_el
    array[index] = start_el


if __name__ == '__main__':
    test_lst = [4, 5, 1, 11, 24, 3, 2]
    selection_sort(test_lst)
