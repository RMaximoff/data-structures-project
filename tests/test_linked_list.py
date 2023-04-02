"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

import unittest
from src.linked_list import Node, LinkedList

class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node({'key': 'value'})
        self.assertEqual(node.data, {'key': 'value'})
        self.assertIsNone(node.next_node)

    def test_init_with_next_node(self):
        next_node = Node({'key2': 'value2'})
        node = Node({'key': 'value'}, next_node)
        self.assertEqual(node.data, {'key': 'value'})
        self.assertEqual(node.next_node, next_node)


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_insert_beginning(self):
        linked_list = LinkedList()
        data = {'key': 'value'}
        linked_list.insert_beginning(data)
        self.assertEqual(linked_list.head.data, data)
        self.assertEqual(linked_list.tail.data, data)

        data2 = {'key2': 'value2'}
        linked_list.insert_beginning(data2)
        self.assertEqual(linked_list.head.data, data2)
        self.assertEqual(linked_list.tail.data, data)

    def test_insert_at_end(self):
        linked_list = LinkedList()
        data = {'key': 'value'}
        linked_list.insert_at_end(data)
        self.assertEqual(linked_list.head.data, data)
        self.assertEqual(linked_list.tail.data, data)

        data2 = {'key2': 'value2'}
        linked_list.insert_at_end(data2)
        self.assertEqual(linked_list.head.data, data)
        self.assertEqual(linked_list.tail.data, data2)

    def test_str(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')

        data = {'key': 'value'}
        linked_list.insert_beginning(data)
        self.assertEqual(str(linked_list), f' {str(data)} -> None')

        data2 = {'key2': 'value2'}
        linked_list.insert_at_end(data2)
        self.assertEqual(str(linked_list), f' {str(data)} -> {str(data2)} -> None')

    def test_to_list_method(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 'test1'})
        test_linked_list.insert_at_end({'id': 'test2'})
        data_list = test_linked_list.to_list()
        self.assertEqual(data_list, [{'id': 'test1'}, {'id': 'test2'}])

    def test_get_data_by_id(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 'home'})
        test_linked_list.insert_at_end({'id': 'jim'})
        test_linked_list.to_list()
        search_data = test_linked_list.get_data_by_id('jim')
        self.assertEqual(search_data, {'id': 'jim'})