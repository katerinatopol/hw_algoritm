"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""
from time import sleep


class StackOfPlates:
    list_stack = []

    def __init__(self, max_count):
        # number = pass
        self.max_count = max_count
        self.list_plates = []
        #self.number = count_stack
        StackOfPlates.list_stack.append(self)

    def store(self, obj):
        if self.max_count != 0:
            self.list_plates.append(obj)
            self.max_count -= 1
            return f'{obj} теперь хранится в стопке'
        else:
            max_count = int(input("Стопка достигла максимальной высоты. Начните складывать новую стопку. \n"
                                  "Сколько в ней будет максимум тарелок? "))
            return StackOfPlates(max_count)


class Plates:
    def __init__(self):
        self.status = 'free'
        # number = pass

    def be_kept(self, stack):
        if self.status == 'be kept':
            return 'Тарелка уже в стопке'
        stack.store(self)
        self.status = 'be kept'
        return f'Тарелка лежит в стопке номер ........'


use_stack = StackOfPlates(3)

while True:
    user_answer = input('-----------------------------\nПривет. Давай складывать тарелки в стопки?\n'
                        'Для начала нажми enter, для выхода Q\n'
                        'Введите ответ: ')
    if user_answer.lower() != 'q':
        while True:
            user_answer = input('-----------------------------\nДля выхода введи Q\n'
                                'Чтобы взять тарелку нажми enter\n'
                                'Введите ответ: ')
            if user_answer.lower() != 'q':
                use_plate = Plates()
                print("Ты взял тарелку. Кладем ее в стопку.")
                sleep(2)
                print(use_plate.be_kept(use_stack))

            else:
                break
    else:
        print('Было весело. Пока.')
        break
