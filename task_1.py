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

# Создаю классы для хранения информации о структуре дерева
# namedtuple принимает первым аргументом имя класса, кот-й мы хотим обявить, а вторым его атрибуты
# У внутреннего узла будет два атрибута - left и right


class Node(namedtuple("Node", ["left", "right"])):
    """
    Внутренний узел дерева
    """
    def walk(self, dict_encode, acc):
        """
        Рекурсивно обходим узел, спускаясь сначала в левого потомка, потом в правого
        """
        self.left.walk(dict_encode, acc + "0")
        self.right.walk(dict_encode, acc + "1")


# у листа будет атрибут - символ
class Leaf(namedtuple("Leaf", ["char"])):
    """Лист"""
    def walk(self, dict_encode, acc):
        """
        Записывает в словарь построенный код данного символа
        """
        dict_encode[self.char]= acc



def huffman_encode(s):
    """
    Функция возвращает словарь, где ключ - символ, значение - соответствующий ему код
    """
    dict_encode = {}
    # строим очередь в виде списка из троек, где первый элемент это частота символа, второй уникальный элемент,
    # необходимый для корректного сравнения, а третий сам символ
    # для подсчета частот использую класс Counter из модуля collections
    heap = []
    for elem, count_el in Counter(s).items():
        heap.append((count_el, len(heap), Leaf(elem)))
    # Построим очередь с приоритетами при помощи heapify
    heapq.heapify(heap)

    # if len(heap) == 1:
    #     _freq, char = heapq.heappop(heap)
    #     dict_encode[char] = str(0)

    # Пока в очереди есть хотя бы 2 элемента, достаем элемент с минимальной частотой (heappop)
    # и следующий за ним элемент с мин.частотой. А затем добавляем в очередь элемент с частотой
    # равной сумме частот вытащенных элементов и новый внутренний узел, с потомками left и right
    while len(heap) > 1:
        min_count, left = heapq.heappop(heap)
        min_count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (min_count + min_count2, Node(left, right)))
    # после выхода из цикла в очереди с приоритетами будет один элемент, приоритет которого
    # нам не важен. Сам элемент является корнем построенного дерева
    [(_count_el, root)] = heap
    # для кодирования необходимо обойти дерево начиная с корня и заполнить созданный ранее словарь
    # второй аргумент это префикс кода, который мы накопили спускаясь к данному узлу/листу
    root.walk(dict_encode, "")

        # for i, char_string in enumerate([min_elem, min_elem2]):
        #     for char in char_string:
        #         if char in dict_encode:
        #             dict_encode[char] = str(i) + dict_encode[char]
        #         else:
        #             dict_encode[char] = str(i)

    return dict_encode


def decode(dict_encode, str_encode):
    decoded_str = ''
    dict_encode = {value: key for key, value in dict_encode.items()}

    sequence = ''
    for char in str_encode:
        sequence += char
        if sequence in dict_encode:
            decoded_str += dict_encode[sequence]
            sequence = ''

    return decoded_str


while True:
    code_str = 'beep boop beer!'
    if code_str != 'q':
        encoding_dict = huffman_encode(code_str)
        # выводим соответствующий код для каждого символа строки
        for el in encoding_dict:
            print(f'{el}: {encoding_dict[el]}')
        # выводим закодированную строку
        encoded_str = ''.join([encoding_dict[el] for el in code_str])
        print(encoded_str)

       # print(decode(encoding_dict, encoded_str))
    else:
        break
