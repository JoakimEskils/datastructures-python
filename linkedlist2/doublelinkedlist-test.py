import unittest
from listnode import ListNode
from doublelinkedlist import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):

    def test_doublelinkedlist(self):
        node1 = ListNode(1)
        node2 = ListNode(5)
        node3 = ListNode(10)
        node4 = ListNode(5)

        linked_list = DoubleLinkedList()

        linked_list.add_list_item(node1)
        linked_list.add_list_item(node2)
        linked_list.add_list_item(node3)
        linked_list.add_list_item(node4)
        
        self.assertEqual(linked_list.list_length(), 4)
        self.assertEqual(linked_list.unordered_search(5), [1, 3])

        linked_list.remove_list_item_by_index(1)

        self.assertEqual(linked_list.list_length(), 3)
        self.assertEqual(linked_list.unordered_search(5), [2])


if __name__ == '__main__':
    unittest.main()