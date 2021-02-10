"""
Задание 3.

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
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
company = {"amazon": 100500, "google": 200100, "apple": 80000, "yandex": 30000, "mail": 50000}


# 1  O(n^3)
def top_company_1(dict_company):
    top_company = []   # O(n)
    profit = dict_company.values()    # O(n)
    top = sorted(profit)[-3:]      # O(1) O(n log n) O(n)
    for i in top: # O (n^3)
        for key, value in dict_company.items():     # O(n^2)
            if value == i:      # O(n)
                top_company.append(key)      # O(1)
    return top_company      # O(1)


print("\n".join(top_company_1(company)))
print()


# 2   O(n^2)
def top_company_2(dict_company):
    top_company = []                            # O(n)
    profit = list(dict_company.values())        # O(n)
    while len(profit) > 3:                      # O(n^2)
        profit.remove(min(profit))                 # O(n)
    for key, value in dict_company.items():     # O(n^2)
        if value in profit:                        # O(n)
            top_company.append(key)                # O(1)
    return top_company                          # O(1)


print("\n".join(top_company_2(company)))
print()


# 3  O(n log n)
def top_company_3(dict_company):
    return [i[0] for i in sorted(dict_company.items(), key=lambda x: x[1])[-3:]]
    # O(1) O(n)[ O(n)    O(n log n) (              O(n),                 O(n)) ]      => O(n log n)


print("\n".join(top_company_3(company)))


# Оптимальным является 3 вариант решения, т.к. у него минимальный рост времени при росте входных данных.
