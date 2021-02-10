import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_binarySearchTree(self):
        bst = BinarySearchTree(7)

        bst.insert(5)
        bst.insert(10)
        bst.insert(6)
        bst.insert(3)
        bst.insert(2)
        bst.insert(15)
        
        self.assertFalse(bst.findval(9))
        self.assertFalse(bst.findval(4))
        self.assertTrue(bst.findval(3))

if __name__ == '__main__':
    unittest.main()