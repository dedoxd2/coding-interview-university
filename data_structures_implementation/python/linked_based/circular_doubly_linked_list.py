class Node:

    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self._size = 0
        self._first = None
        self._last = None

    def get_size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self._size == 0

    def _insert_empty_list(self, item) -> None:
        newNode = Node(item)
        self._first = self._last = newNode
        newNode.next = newNode
        newNode.prev = newNode
        self._size += 1

    def insertFirst(self, item) -> None:  # Done
        newNode = Node(item)
        if self.isEmpty():
            self._insert_empty_list(item)
        else:
            old_node = self._first
            newNode.prev = self._last  # old_node.prev
            newNode.next = old_node
            old_node.prev = newNode
            self._last.next = newNode
            self._first = newNode
            self._size += 1

    def insertEnd(self, item) -> None:  # Done
        newNode = Node(item)
        if self.isEmpty():
            self._insert_empty_list(item)
        else:
            old_node = self._last
            newNode.prev = old_node
            newNode.next = self._first  # old_node.next
            self._last = newNode
            old_node.next = newNode
            self._size += 1

    def insert_n_first(self, index: int, item) -> None:  # Done
        # to avoid calling the function get size 2 times in the elif statement
        size = self.get_size()
        if index == 0:
            self.insertFirst(item)
        elif index == size:
            self.insertEnd(item)
        elif index > size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._first
            newNode = Node(item)
            while index > 1:
                index -= 1
                temp_ptr = temp_ptr.next

            newNode.next = temp_ptr.next
            newNode.prev = temp_ptr
            temp_ptr.next.prev = newNode
            temp_ptr.next = newNode

            self._size += 1

    def insert_n_end(self, index: int, item) -> None:
        size = self.get_size()
        if index == 0:
            self.insertEnd(item)
        elif index == size:
            self.insertFirst(item)
        elif index > size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._last
            newNode = Node(item)
            while index > 1:
                index -= 1
                temp_ptr = temp_ptr.prev

            newNode.next = temp_ptr
            newNode.prev = temp_ptr.prev
            temp_ptr.prev.next = newNode
            temp_ptr.prev = newNode
            self._size += 1

    def retrieve_Frist_Element(self):
        return self._first.item

    def delete_Frist_Element(self):
        """Delete and return the first element"""
        if self.isEmpty():
            raise RuntimeError("Can't delete Element from Empty List")
        else:

            value = self._first.item

            self._first.next.prev = self._last
            self._last.next = self._first.next
            self._first = self._first.next

            self._size -= 1
            return value

    def delete_Last_Element(self):
        """Delete and return the Last element"""
        if self.isEmpty():
            raise RuntimeError("Can't delete Element from Empty List")
        else:
            value = self._last.item
            self._last.prev.next = self._first
            self._first.prev = self._last.prev
            self._last = self._last.prev

            self._size -= 1
            return value

    def retrieve_Last_Element(self):
        return self._last.item

    def retrieve_n_Element_First(self, index: int):
        """Just return the N index from the Beggining , Not deleting the element"""
        size = self.get_size()
        if index == 0:
            return self._first.item
        elif index == size - 1:
            return self._last.item
        elif index >= size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._first
            while index > 1:
                index -= 1
                temp_ptr = temp_ptr.next

            return temp_ptr.next.item

    def retrieve_n_Element_Last(self, index: int):
        """Just return the N index from the End , Not deleting the element"""
        size = self.get_size()
        if index == 0:
            return self._last.item
        elif index == size - 1:
            return self._first.item
        elif index >= size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._last
            while index > 0:
                index -= 1
                temp_ptr = temp_ptr.prev

            return temp_ptr.item

    def delete_n_Element_First(self, index: int):
        """Returning the The Element in Index N from the beggining and Deleting it"""
        size = self.get_size()
        if index == 0:
            return self.delete_Frist_Element()
        elif index == size-1:
            return self.delete_Last_Element()
        elif index >= size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._first
            while index > 1:
                index -= 1
                temp_ptr = temp_ptr.next
            value = temp_ptr.next.item

            temp_ptr.next = temp_ptr.next.next
            temp_ptr.next.next.prev = temp_ptr
            self._size -= 1
            return value

    def delete_n_Element_End(self, index: int):
        """Returning the The Element in index N from the End and Deleting it"""
        size = self.get_size()
        if index == 0:
            return self.delete_Last_Element()
        elif index == size - 1:
            return self.delete_Frist_Element()
        elif index >= size or index < 0:
            raise IndexError("Out of Range")
        else:
            temp_ptr = self._last
            while index > 1:
                index -= 1
                temp_ptr = temp_ptr.prev

            value = temp_ptr.prev.item
            temp_ptr.prev.prev.next = temp_ptr
            temp_ptr.prev = temp_ptr.prev.prev
            self._size -= 1
            return value

    def traverse_from_First(self):
        count = 0
        size = self.get_size()  # To prevent call the function every time in the loop
        temp_ptr = self._first
        print("[", end=" ")
        while count < size:
            print(temp_ptr.item,  end=" ,")
            count += 1
            temp_ptr = temp_ptr.next

        print(" ]", end=" \n")

    def traverse_from_End(self):
        count = 0
        size = self.get_size()
        temp_ptr = self._last
        print("[", end=" ")
        while count < size:
            print(temp_ptr.item, end=" ,")
            count += 1
            temp_ptr = temp_ptr.prev
        print(" ]", end=" \n")
