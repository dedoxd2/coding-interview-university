import unittest
from b_trees import BinaryTree


class TestBinarySearchTree(unittest.TestCase):

    def test_insert_and_search(self):
        bst = BinaryTree()
        values = [50, 30, 70, 20, 40, 60, 80]

        # Insert values into the binary search tree
        for value in values:
            bst.Insert(value)

        # Search for each inserted value
        for value in values:
            self.assertTrue(bst.Search(value),
                            f"Value {value} not found in the tree")

        # Search for a value that doesn't exist
        self.assertFalse(bst.Search(
            100), "Value 100 should not exist in the tree")

    def test_delete(self):
        bst = BinaryTree()
        values = [50, 30, 70, 20, 40, 60, 80]

        # Insert values into the binary search tree
        for value in values:
            bst.Insert(value)

        # Delete some values
        bst.Delete(20)
        bst.Delete(40)
        bst.Delete(70)

        # Ensure deleted values are not found
        self.assertFalse(bst.Search(
            20), "Value 20 should not exist in the tree")
        self.assertFalse(bst.Search(
            40), "Value 40 should not exist in the tree")
        self.assertFalse(bst.Search(
            70), "Value 70 should not exist in the tree")

        # Ensure other values still exist
        self.assertTrue(bst.Search(50), "Value 50 should exist in the tree")
        self.assertTrue(bst.Search(30), "Value 30 should exist in the tree")
        self.assertTrue(bst.Search(60), "Value 60 should exist in the tree")
        self.assertTrue(bst.Search(80), "Value 80 should exist in the tree")

    def test_empty_tree(self):
        bst = BinaryTree()
        self.assertTrue(bst.is_Empty(), "Newly created tree should be empty")
        self.assertEqual(len(bst), 0, "Size of newly created tree should be 0")
        self.assertEqual(bst.TreeDepth(), 0,
                         "Depth of newly created tree should be 0")
        self.assertIsNone(
            bst.root, "Root of newly created tree should be None")

    def test_inorder_traversal(self):
        bst = BinaryTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        expected_inorder = sorted(values)

        # Insert values into the binary search tree
        for value in values:
            bst.Insert(value)

        # Perform inorder traversal and compare with expected result
        inorder_result = list(bst.Inorder_Recursive())
        self.assertEqual(inorder_result, expected_inorder,
                         "Inorder traversal result is incorrect")


if __name__ == '__main__':
    unittest.main()
