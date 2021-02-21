from hashlib import pbkdf2_hmac
from binascii import hexlify
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='59808sKWRTn')

connection.cursor().execute("""drop database users""")

create = """create database users;
       use users;
       CREATE TABLE some_table(  `id` INT NOT NULL AUTO_INCREMENT,`user_login` VARCHAR(255) NULL, 
       `user_password` VARCHAR(255) NULL, PRIMARY KEY (`id`))"""
for element in create.split(';'):
    try:
        connection.cursor().execute(element)
        connection.commit()
    except ValueError as err:
        print(f"FAIL IN {str(element)}, {err}")

connection.close()

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='59808sKWRTn',
                          db='users',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor
                          )


class Users:

    def __init__(self, login, password: str):
        self.login = login
        self.password = create_hash(password, login)
        self.add_in_db()

    def add_in_db(self):
        with connect.cursor() as cursor:
            cursor.execute(f"""insert into some_table (user_login, user_password) values ('{self.login}', '{self.password}');""")
        connect.commit()


def create_hash(obj, salt):
    hash_obj = pbkdf2_hmac(hash_name='sha256',
                           password=obj.encode(),
                           salt=salt.encode(),
                           iterations=100000)
    return hexlify(hash_obj).decode('utf-8')


def check(login, password):
    hash_password = create_hash(password, login)
    with connect.cursor() as cursor:
        try:
            cursor.execute(f"""select user_password from some_table where user_login = '{login}';""")
            res = cursor.fetchall()[0]
        except IndexError:
            print('Пользователя с таким логином не существует')
            return False
    connect.commit()
    if res['user_password'] == hash_password:
        print('Пароль верный')
        return True
    else:
        print('Пароль неверный')
        return False


Users('test_user', 'qwerty')

user_answer = input('Если вы новый пользователь - введите +, уже зарегистрированы - нажмите enter для продолжения: ')
if user_answer == '+':
    new_login = input('Введите логин: ')
    new_password = input('Введите пароль: ')
    new_user = Users(new_login, new_password)
    print(f'В базе данных хранится строка: {new_user.password}')
while True:
    check_login = input('Введите логин для проверки: ')
    check_password = input('Введите пароль для проверки: ')
    checkout = check(check_login, check_password)
    if checkout:
        break

connect.close()
