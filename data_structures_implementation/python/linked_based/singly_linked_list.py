

class Node:
    def __init__(self, item) -> None:
        self.item = item
        self._next = None


class LinkedList():
    def __init__(self) -> None:
        self._first = None
        self._last = None
        self._size = 0

    def isEmpty(self) -> bool:
        return self._size == 0

    def get_size(self) -> int:
        return self._size

    def _handle_insert_Empty(self, item):
        # Inserting in empty list is a special case for inserting from the beginning or from the end
        # so instead of repeating code i made this function to handle this special case
        # DRY!!
        newNode = Node(item)
        self._first = newNode
        self._last = newNode
        newNode._next = None

    def insertFirst(self, item) -> None:
        """Insert Element from the beginning of the list """
        if self.isEmpty():
            self._handle_insert_Empty(item)
        else:
            newNode = Node(item)
            newNode._next = self._first
            self._first = newNode

        self._size = self._size + 1

    def insertLast(self, item) -> None:
        """Insert Element from the end of the list """
        if self.isEmpty():
            self._handle_insert_Empty(item)
        else:
            newNode = Node(item)
            self._last._next = newNode
            self._last = newNode
            newNode._next = None
        self._size = self._size + 1

    def retrieve_First(self):
        """Just Return the first element of the list """
        if self.isEmpty():
            raise IndexError("Can't retrieve from empty list")
        else:
            return self._first.item

    def retrieve_End(self):
        """Just Return the last element of the list """
        if self.isEmpty():
            raise IndexError("Can't retrieve from empty list")
        else:
            return self._last.item

    def insert_at_n(self, index: int, item) -> None:
        if index == 0:
            self.insertFirst(item)
        elif index == self.get_size():
            self.insertLast(item)
        elif self.get_size() > index:
            index -= 1  # indexs are 0 Based and i want to stop right before the N th element
            temp_ptr = self._first
            newNode = Node(item)
            while index > 0:
                index -= 1
                temp_ptr = temp_ptr._next

            newNode._next = temp_ptr._next
            temp_ptr._next = newNode
            self._size += 1

        else:
            raise IndexError("Index Out of range")

    def retrieve_from_n(self, index: int):
        if self.isEmpty():
            raise IndexError("Can't retrieve from empty list")
        elif index >= self.get_size() or index < 0:
            raise IndexError("Index Out of range")
        else:
            temp_ptr = self._first
            while index > 0:
                if temp_ptr is None:
                    raise IndexError("Index Out of range")
                temp_ptr = temp_ptr._next
                index -= 1
            return temp_ptr.item

    def remove_first(self):
        """Remove and Rerturn the first element"""
        if self.isEmpty():
            raise IndexError("Can't remove Element From empty list")
        else:
            value = self._first.item
            self._first = self._first._next
            self._size -= 1
            return value

    def remove_end(self):
        """Remove and Rerturn the last element"""

        if self.isEmpty():
            raise IndexError("Can't remove Element From empty list")
        else:
            temp_ptr = self._first
            if self.get_size() == 1:
                value = temp_ptr.item
                self._first = self._last = None
            else:

                while temp_ptr._next._next:
                    temp_ptr = temp_ptr._next

                value = temp_ptr._next.item
                temp_ptr._next = None
                self._last = temp_ptr
            self._size -= 1
            return value

    def remove_at_n(self, n: int):
        """Remove and return value from index n"""
        size = self.get_size()
        if n == 0:
            value = self.remove_first()
            return value
        elif n == size - 1:
            value = self.remove_end()
            return value
        elif n >= size or n < 0:
            raise IndexError("Out of Scope")
        else:
            temp_ptr = self._first
            while n > 1:
                n -= 1
                temp_ptr = temp_ptr._next
            value = temp_ptr._next.item
            temp_ptr._next = temp_ptr._next._next
            self._size -= 1
            return value

    def traverseList(self):
        temp_ptr = self._first
        print("[", end=" ")
        while temp_ptr._next:

            print(temp_ptr.item, end=", ")
            temp_ptr = temp_ptr._next
        print(temp_ptr.item, end="]\n")
