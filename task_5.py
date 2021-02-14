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

    def __init__(self, max_count, name):
        self.max_count = max_count
        self.list_plates = []
        self.name = name

    def is_empty(self):
        return self.list_plates == []

    def store(self, obj):
        if self.max_count != 0:
            self.list_plates.append(obj)
            self.max_count -= 1
            return self
        else:
            max_count = int(input("Стопка достигла максимальной высоты. Начните складывать новую стопку. \n"
                                  "Сколько в ней будет максимум тарелок? "))
            name = input('Как она будет называться (номер): ')
            new_stack = StackOfPlates(max_count, name)
            new_stack.list_plates.append(obj)
            new_stack.max_count -= 1
            return new_stack

    def pop_out(self):
        self.list_plates.pop()
        return f'Вы убрали верхнюю тарелку в стопке {self.name}'

    def stack_size(self):
        return f'Высота стопки {self.name} {len(self.list_plates)}'

    def get_val(self):
        return self.list_plates[len(self.list_plates) - 1]


class Plates:
    def __init__(self):
        self.status = 'free'

    def be_kept(self, stack):
        if self.status == 'be kept':
            return 'Тарелка уже в стопке'
        use_stack1 = stack.store(self)
        self.status = 'be kept'
        return use_stack1


# Для проверки работы метода store сделала небольшую программку.
# Параметр "name" стопки сделан для простоты - хорошо видно, что стопка меняется.
use_stack = StackOfPlates(3, 'первая')

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
                use_stack = use_plate.be_kept(use_stack)
                print(f'Тарелка лежит в стопке номер {use_stack.name}')
            else:
                break
    else:
        print('Было весело. Пока.')
        break
