import pytest

from tasks import alphabet


@pytest.mark.parametrize('s, true_result', [('MR Robot', '13,18,18,15,2,15,20'),
                                            ('Aa Bb', '1,1,2,2'),
                                            ('кириллица', 'Некорректная исходная строка'),
                                            ('!-text', 'Некорректная исходная строка')])
def test_alphabet(s, true_result):
    check = alphabet(s)
    assert check == true_result, f"Получен результат {check}, ожидался {true_result}"

