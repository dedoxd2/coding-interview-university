"""implementation of Queue Linked Based"""


class Node:
    def __init__(self, value=None) -> None:
        self._data = value
        self._next = None


class QueueList(Node):
    def __init__(self) -> None:
        super().__init__()
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return False

    def get_size(self):
        return self._size

    def enqueue(self, value) -> bool:
        """Add Element to the Queue"""
        temp_node = Node(value)

        if self.is_empty():
            self._front = temp_node

        else:
            self._rear._next = temp_node  # run time error for empty queue

        self._rear = temp_node
        self._size += 1
        return True

    def dequeue(self):
        """Pop Element from the Queue"""
        if self.is_empty():
            raise IndexError("The Queue is empty")

        else:
            value = self._front._data

            self._front = self._front._next
            if self._front == None:  # Check if this is the last node
                self._rear = None
            self._size -= 1
        return value

    def front(self):
        """Just Retrun the value in the top without deleting the element"""
        if self.is_empty():
            raise IndexError("The Queue is empty")
        else:
            value = self._front._data
            return value

    def clear_queue(self) -> None:
        while self._front:
            self._rear = self._front._next
            self._front = None
            self._front = self._rear
        self._rear = None
        self._size = 0
