"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
from random import randint


def my_func(true_answer, max_try_count=10, try_count=1):
    try:
        user_answer = int(input("Введите число: "))
        if try_count == max_try_count or user_answer == true_answer:
            if user_answer == true_answer:
                print("Ты выиграл")
            return f"Правильный ответ {true_answer}"
        else:
            if user_answer > 100 or user_answer < 0:
                print(f"Число должно быть больше 0 и меньше 100. Осталось {max_try_count - try_count} попыток")
            elif user_answer > true_answer:
                print(f"Правильное число меньше. Осталось {max_try_count - try_count} попыток")
            elif user_answer < true_answer:
                print(f"Правильное число больше. Осталось {max_try_count - try_count} попыток")
            return my_func(true_answer, max_try_count, try_count + 1)
    except ValueError as err:
        print(f"Это не число.\n {err}")
        return my_func(true_answer, max_try_count, try_count + 1)


print(my_func(randint(0, 100)))
