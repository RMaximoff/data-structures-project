class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def to_list(self) -> list:
        """Возвращает список со значениями всех узлов связанного списка"""
        node = self.head
        result_list = []
        while node:
            result_list.append(node.data)
            node = node.next_node
        return result_list

    def get_data_by_id(self, id_value: int) -> dict:
        """Возвращает первый найденный словарь с ключом 'id' со значением, равным переданному значению"""
        try:
            node = self.head
            while node:
                if node.data['id'] == id_value:
                    return node.data
                node = node.next_node
            return None
        except TypeError:
            print('Данные не являются словарем или в словаре нет id')

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
