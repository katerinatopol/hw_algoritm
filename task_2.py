"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify

users = {}


class Users:

    def __init__(self, login, password: str):
        self.login = login
        self.password = create_hash(login, password)
        users.update({self.login: self.password})


def create_hash(salt, obj):
    hash_obj = pbkdf2_hmac(hash_name='sha256',
                           password=obj.encode(),
                           salt=salt.encode(),
                           iterations=100000)
    return hash_obj


def check(login, password):
    obj = create_hash(login, password)
    if login in users:
        if users[login] == obj:
            print('пароль верный')
            return True
        else:
            print('пароль неверный')
            return False
    else:
        print('такой пользователь не существует')
        return False


Users('test_user', 'qwerty')

user_answer = input('Если вы новый пользователь - введите +, уже зарегистрированы - нажмите enter для продолжения: ')
if user_answer == '+':
    new_login = input('Введите логин: ')
    new_password = input('Введите пароль: ')
    new_user = Users(new_login, new_password)
    print(f'В базе данных хранится строка: {hexlify(new_user.password)}')
while True:
    check_login = input('Введите логин для проверки: ')
    check_password = input('Введите пароль для проверки: ')
    checkout = check(check_login, check_password)
    if checkout:
        break
