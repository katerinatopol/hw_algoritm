import pytest

from tests.alphabet import alphabet


@pytest.mark.parametrize('s, true_result', [('MR Robot', '13,18,18,15,2,15,20'),
                                            ()])
def test_alphabet(s, true_result):
    check = alphabet(s)
    assert check == true_result, f"Получен результат {check}, ожидался {true_result}"

