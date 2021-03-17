"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
from collections import Counter, namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    """Внутренний узел дерева"""
    def walk(self, dict_encode, acc):
        """
        Функция рекурсивно обходит узел, спускаясь сначала в левого потомка, потом в правого,
        собирая при этом префиксы.
        """
        self.left.walk(dict_encode, acc + "0")
        self.right.walk(dict_encode, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    """Лист"""
    def walk(self, dict_encode, acc):
        """
        Функция записывает в словарь построенный код данного символа
        """
        dict_encode[self.char] = acc or "0"


def huffman_encode(s):
    """
    Функция возвращает словарь, где ключ - символ, значение - соответствующий ему код.
    Для этого строим очередь в виде списка из троек, где первый элемент это частота символа, второй уникальный элемент,
    необходимый для корректного сравнения, а третий сам символ.
    Для подсчета частот использую класс Counter из модуля collections.
    При помощи heapify строим очередь с приоритетами. В цикле пока в очереди есть хотя бы 2 элемента, достаем элемент
    с мин. частотой (heappop) и следующий за ним элемент с мин.частотой. А затем добавляем в очередь элемент с частотой
    равной сумме частот вытащенных элементов и новый внутренний узел, с потомками left и right.
    После выхода из цикла в очереди с приоритетами будет один элемент, приоритет которого нам не важен. Сам элемент
    является корнем построенного дерева.
    Для кодирования обрабатываем случай с пустой строкой и обходим дерево начиная с корня. Используем метод walk,
    передавая ему словарь, который заполняем, и префикс кода, который мы накопили спускаясь к данному узлу/листу.
    """
    dict_encode = {}
    heap = []
    for elem, count_el in Counter(s).items():
        heap.append((count_el, len(heap), Leaf(elem)))
    heapq.heapify(heap)

    count = len(heap)
    while len(heap) > 1:
        min_count, _count1, left = heapq.heappop(heap)
        min_count2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (min_count + min_count2, count, Node(left, right)))
        count += 1

    if heap:
        [(_count_el, _count, root)] = heap
        root.walk(dict_encode, "")

    return dict_encode


while True:
    code_str = input('Для выхода введите q\nВведите любую строку для кодирования: ')
    if code_str != 'q':
        encoding_dict = huffman_encode(code_str)
        # выводим соответствующий код для каждого символа строки
        for el in encoding_dict:
            print(f'{el}: {encoding_dict[el]}')
        # выводим закодированную строку
        encoded_str = ''.join([encoding_dict[el] for el in code_str])
        print(encoded_str)
    else:
        break


"""
При выполнении задания я использовала готовую реализацию алгоритма кодирования по Хаффману, адаптировав его под себя.
Я добавила развернутые комментарии, так как подробное описание каждого шага помогло разобраться мне с этим алгоритмом.
Алгоритм корректно работает также на строках из 1 символа и на пустой строке

Введите любую строку для кодирования: 12345
3: 00
4: 01
5: 10
1: 110
2: 111
110111000110

Введите любую строку для кодирования: abracadabra
a: 0
c: 100
d: 101
b: 110
r: 111
01101110100010101101110

Введите любую строку для кодирования: a
a: 0
0

Введите любую строку для кодирования: aaa
a: 0
000

Введите любую строку для кодирования:  
 : 0
0
"""
