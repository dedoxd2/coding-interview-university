import unittest
from simple_linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.my_linked_list = LinkedList()

    def test_insert_first(self):
        self.my_linked_list.insertFirst(5)
        self.assertEqual(self.my_linked_list.retrieve_First(), 5)

    def test_insert_last(self):
        self.my_linked_list.insertLast(5)
        self.assertEqual(self.my_linked_list.remove_end(), 5)

    def test_insert_at_n(self):
        self.my_linked_list.insertFirst(5)
        self.my_linked_list.insertFirst(4)
        self.my_linked_list.insertFirst(3)
        self.my_linked_list.insert_at_n(1, 100)
        self.assertEqual(self.my_linked_list.retrieve_from_n(1), 100)

    def test_remove_first(self):
        self.my_linked_list.insertFirst(5)
        self.my_linked_list.insertFirst(4)
        self.my_linked_list.remove_first()
        self.assertEqual(self.my_linked_list.remove_first(), 5)

    def test_remove_end(self):
        self.my_linked_list.insertLast(5)
        self.my_linked_list.insertLast(4)
        self.my_linked_list.remove_end()
        self.assertEqual(self.my_linked_list.retrieve_End(), 5)

    def test_remove_at_n(self):
        self.my_linked_list.insertFirst(5)
        self.my_linked_list.insertFirst(4)
        self.my_linked_list.insertFirst(3)
        self.my_linked_list.remove_at_n(1)
        self.assertEqual(self.my_linked_list.retrieve_from_n(1), 5)

    def tearDown(self):
        del self.my_linked_list


if __name__ == '__main__':
    unittest.main()
