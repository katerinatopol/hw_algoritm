"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете усложнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from _hashlib import pbkdf2_hmac
from binascii import hexlify
from uuid import uuid4

cash = {}


def to_hash(obj: str):
    hash_obj = pbkdf2_hmac(hash_name='sha256',
                           password=obj.encode(),
                           salt=uuid4().hex.encode(),
                           iterations=100000)
    return hexlify(hash_obj)


def check_url(url: str):
    if url in cash:
        return f'{url} есть в кэше'
    else:
        url_hash = to_hash(url)
        cash[url] = url_hash
        return f'{url} добавлен в кэш'


while True:
    user_answer = input('Введите url: ')
    if user_answer == 'q':
        break
    print(check_url(user_answer))
