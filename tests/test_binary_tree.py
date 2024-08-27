# Unit tests for Linked List
import unittest
from src.data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.head.next.data, 2)

    def test_print_list(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        with self.assertLogs() as captured:
            ll.print_list()
        self.assertEqual(captured.output, ['1', '2'])

if __name__ == '__main__':
    unittest.main()
