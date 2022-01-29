import pytest

from tasks import alphabet, binary_search


@pytest.mark.parametrize('s, true_result', [('MR Robot', '13,18,18,15,2,15,20'),
                                            ('Aa Bb', '1,1,2,2'),
                                            ('кириллица', 'Некорректная исходная строка'),
                                            ('!-text', 'Некорректная исходная строка')])
def test_alphabet(s, true_result):
    check = alphabet(s)
    assert check == true_result, f"Получен результат {check}, ожидался {true_result}"


@pytest.mark.parametrize('array, target', [(list(range(50))[1:], 18),
                                           ([1, 3, 5, 7, 10, 14, 25, 26, 28, 29, 30, 31, 32], 30),
                                           ([1, 7, 8, 9, 10, 14, 16, 20, 29, 45, 70, ], 14)])
def test_binary_search(array, target):
    true_result = id(array[array.index(target)])
    check = binary_search(array, target)
    assert check == true_result, f"Получен результат {check}, ожидался {true_result}"
