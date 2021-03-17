"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            try:
                if new_node > self.root:
                    raise ValueError('Недопустимое значение левого потомка')
            except ValueError as err:
                print(f'Ошибка: {err}')

            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            try:
                if new_node < self.root:
                    raise ValueError('Недопустимое значение правого потомка')
            except ValueError as err:
                print(f'Ошибка: {err}')
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise AttributeError('Узел не существует')
            else:
                return self.right_child
        except AttributeError as err:
            print(f'Ошибка: {err}')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise AttributeError('Узел не существует')
            else:
                return self.left_child
        except AttributeError as err:
            print(f'Ошибка: {err}')

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            if self.root is None:
                raise AttributeError('Узел не существует')
            else:
                return self.root
        except AttributeError as err:
            print(f'Ошибка: {err}')


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(6)
print(r.get_left_child())
r = BinaryTree(70)
r.insert_right(60)
r.insert_left(500)
print(r.get_left_child().get_root_val())
r.insert_right(10)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
r.get_right_child().set_root_val(20)
print(r.get_right_child().get_root_val())
r.get_left_child().set_root_val(100)
print(r.get_left_child().get_root_val())
r.get_left_child().insert_right(1000)
print(r.get_left_child().get_right_child().get_root_val())

"""
Добавила обработку исключений при попытке вставить некорректное значение. Также обработку попытки доступа к
несуществующим узлам.
"""
