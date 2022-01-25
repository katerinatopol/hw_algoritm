"""
1. Алфавит
Зашифруйте сообщение меняя буквы на их порядковый номер в алфавите. Пробелы при этом не учитывать.
Строки будут даны без знаков препинания, только с пробелами. Регистр не учитывать.
Входные данные: шифруемая строка, длиной до 1000 символов, на латинице
Пример входных данных: 
MR Robot
Выходные данные: через запятую порядковый номер букв в алфавите
Пример выходных данных: 
13,18,18,15,2,15,20
"""
import string

LETTERS = {f'{el}': ind for ind, el in enumerate(string.ascii_lowercase, 1)}


def alphabet(s):
    s = s.lower().replace(' ', '')
    try:
        result = [LETTERS[el] for el in s]
        return ','.join(map(str, result))
    except KeyError as err:
        return "Некорректная исходная строка"
