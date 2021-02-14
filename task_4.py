"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


dict_users = {"user1": {"password": "12345", "active": True},
              "user2": {"password": "54321", "active": False},
              "user3": {"password": "abcdf", "active": False}}


def activation(login, password):
    pass


# 1 O(n)
def authentication_1(users, login, password):
    for key, value in users.items():        # O(n)
        if key == login:                    # O(1)
            if value["password"] == password and value["active"]:           # O(1)
                return "Доступ к ресурсу предоставлен."                     # O(1)
            elif value["password"] == password and not value["active"]:     # O(1)
                user_answer = input("Учетная запись не активна, хотите активировать сейчас? Y/N : ")    # O(1)
                if user_answer.lower() == "y":                      # O(1)
                    return activation(login, password)       # вызов функции активации аккаунта
                else:
                    return "В доступе к ресурсу отказано"           # O(1)
            elif value["password"] != password:                     # O(1)
                return "Неверный пароль"                            # O(1)

    return "Пользователь не зарегистрирован."                       # O(1)


print(authentication_1(dict_users, "user1", "12345"))
print(authentication_1(dict_users, "user2", "54321"))


# 2 O(1)
def authentication_2(users, login, password):
    if users.get(login):
        if users[login]["password"] == password and users[login]["active"]:
            return "Доступ к ресурсу предоставлен."
        elif users[login]["password"] == password and not users[login]["active"]:
            user_answer = input("Учетная запись не активна, хотите активировать сейчас? Y/N : ")
            if user_answer.lower() == "y":
                return activation(login, password)  # вызов функции активации аккаунта
            else:
                return "В доступе к ресурсу отказано"
        elif users[login]["password"] != password:
            return "Неверный пароль"
    else:
        return "Пользователь не зарегистрирован."


print(authentication_2(dict_users, "user1", "12345"))
print(authentication_2(dict_users, "user2", "54321"))

# Лучше 2 решение, т.к. время выполнения не зависит от объема входных данных, время всегда константное.
