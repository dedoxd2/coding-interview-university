class Node:
    def __init__(self, entry) -> None:
        self.entry = entry
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def TreeSize(self) -> int:
        return self.size

    def is_Empty(self) -> bool:
        return self.size == 0

    def Inorder_Recursive(self):
        yield from self._Inorder_Recursive(self.root)

    def _Inorder_Recursive(self, node):
        # in order to implement the function Iteratively , it enforces me to use Stack structure
        # but according to the note that The OS will build the Stack Much more efficient, we should use the recursive version of the implementation
        # Therefore no need to implement the function in Iterative way

        if node:
            yield from self._Inorder_Recursive(node.left)
            yield node.entry
            yield from self._Inorder_Recursive(node.right)

    def Insert(self, value) -> None:
        self.root = self._Insert(self.root, value)
        self.size += 1

    def _Insert(self, node, value) -> Node:
        if node is None:
            return Node(value)
        elif value < node.entry:
            node.left = self._Insert(node.left, value)
        else:
            node.right = self._Insert(node.right, value)
        return node

    def _Insert_Iterative(self, value) -> None:
        newNode = Node(value)
        newNode.left = None
        newNode.right = None
        if self.is_Empty():
            self.root = newNode
        else:
            curr = self.root
            prev = curr
            while curr:
                prev = curr
                if value < curr.entry:
                    curr = curr.left
                else:
                    curr = curr.right
            if value < prev.entry:
                prev.left = newNode
            else:
                prev.right = newNode

    def Search(self, value):
        """Search for an entry in the tree Retrurn 1 in case the value exists"""
        tmp_ptr = self.root
        while tmp_ptr:
            if value == tmp_ptr.entry:
                return 1
            elif value < tmp_ptr.entry:
                tmp_ptr = tmp_ptr.left
            else:
                tmp_ptr = tmp_ptr.right

    def Delete(self, value):
        """Delete a node with a given value"""
        self.root = self._Delete(self.root, value)
        self.size -= 1

    def _Delete(self, node, value):
        """Helper method to delete a node with a given value"""
        if node is None:
            return node

        # If the value to be deleted is smaller than the root's value, then it lies in the left subtree
        if value < node.entry:
            node.left = self._Delete(node.left, value)

        # If the value to be deleted is greater than the root's value, then it lies in the right subtree
        elif value > node.entry:
            node.right = self._Delete(node.right, value)

        # If value is the same as root's value, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._MinValueNode(node.right)

            # Copy the inorder successor's content to this node
            node.entry = temp.entry

            # Delete the inorder successor
            node.right = self._Delete(node.right, temp.entry)

        return node

    def _MinValueNode(self, node):
        """Helper method to find the node with the minimum value in the subtree rooted at a given node"""
        current = node

        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current
