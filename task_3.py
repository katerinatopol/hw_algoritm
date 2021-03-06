"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile()
def reverse_func(*args, **kwargs):
    def inner(num):
        if num // 10 == 0:
            print(f'Перевернутое число: {str(num % 10)}')
        else:
            print(f'Перевернутое число: {str(num % 10) + str(reverse_func(num // 10))}')


while True:
    try:
        user_number = int(input('Введите число, которое требуется перевернуть: '))
        reverse_func(user_number)
        break
    except ValueError as err:
        print(f'Возникла ошибка: {err}\nЭто не число, попробуйте еще раз.')

"""
При профилировании рекурсии возникает проблема - таблица создается для каждого шага.
Поэтому для получения корректного результата можно сделать функцию-обертку, которая и будеть профилироваться

Line #    Mem usage    Increment   Line Contents
================================================
    11     13.5 MiB     13.5 MiB   @profile()
    12                             def reverse_func(*args, **kwargs):
    13     13.5 MiB      0.0 MiB       def inner(num):
    14                                     if num // 10 == 0:
    15                                         print(f'Перевернутое число: {str(num % 10)}')
    16                                     else:
    17                                         print(f'Перевернутое число: {str(num % 10) + str(reverse_func(num // 10))}')
"""
