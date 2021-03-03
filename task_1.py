"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


def average_profit():
    quantity = int(input('Укажите количество предприятий: '))
    companies = namedtuple('Предприятие', 'name quarter_1 quarter_2 quarter_3 quarter_4')
    aver_profit = {}
    for i in range(quantity):
        company_name = input(f'Укажите название предприятия: ')
        company_profit = [int(i) for i in input('через пробел введите прибыль данного предприятия \n'
                                                'за каждый квартал(Всего 4 квартала): ').split()]
        company = companies(
            name=company_name,
            quarter_1=company_profit[0],
            quarter_2=company_profit[1],
            quarter_3=company_profit[2],
            quarter_4=company_profit[3]
        )
        aver_profit[company.name] = (company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4

    average = sum(aver_profit.values()) * 4 / quantity
    print(f'Средняя годовая прибыль всех предприятий: {average}')

    above_aver_profit = [key for key, value in aver_profit.items() if value > average]
    below_aver_profit = [key for key, value in aver_profit.items() if value < average]

    return f"Предприятия с прибылью выше среднего: {','.join(above_aver_profit)}\n" \
           f"Предприятия с прибылью ниже среднего: {','.join(below_aver_profit)}"


print(average_profit())
