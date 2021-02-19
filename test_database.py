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
# Устанавливаю драйвер для MySQL pip install mysql-connector-python

from hashlib import pbkdf2_hmac
from binascii import hexlify
import mysql.connector
from mysql.connector import Error


# Создание подключения к MySQL
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Подключение к БД MySQL прошло успешно")
    except Error as err:
        print(f"Возникла ошибка: '{err}'")

    return connection


connection = create_connection("localhost", "root", "")           # подключение


# Создание базы данных
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("База данных успешно создана")
    except Error as err:
        print(f"Возникла ошибка: {err}")


create_database_query = "CREATE DATABASE users"
#create_database(connection, create_database_query)



#
# class Users:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = create_hash(login, password)
#         users.update({self.login: self.password})
#
#
# def create_hash(salt, obj):
#     hash_obj = pbkdf2_hmac(hash_name='sha256',
#                            password=obj.encode('utf-8'),
#                            salt=salt.encode('utf-8'),
#                            iterations=100000)
#     return hash_obj
#
#
# def check(login, password):
#     obj = create_hash(login, password)
#     if login in users:
#         if users[login] == obj:
#             print('пароль верный')
#             return True
#         else:
#             print('пароль неверный')
#             return False
#     else:
#         print('такой пользователь не существует')
#         return False
#
#
# Users('test_user', 'qwerty')
#
# user_answer = input('Если вы новый пользователь - введите +, уже зарегистрированы - нажмите enter для продолжения: ')
# if user_answer == '+':
#     new_login = input('Введите логин: ')
#     new_password = input('Введите пароль: ')
#     new_user = Users(new_login, new_password)
#     print(f'В базе данных хранится строка: {hexlify(new_user.password)}')
# while True:
#     check_login = input('Введите логин для проверки: ')
#     check_password = input('Введите пароль для проверки: ')
#     checkout = check(check_login, check_password)
#     if checkout:
#         break
