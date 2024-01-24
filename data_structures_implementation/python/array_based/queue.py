"""implementation of Circular Queue Array based"""


class QueueArr:
    def __init__(self, max_size=10) -> None:
        self._front = 0
        self._rear = -1
        self._size = 0
        self._max_size = max_size
        self._arr = [None] * max_size

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._max_size

    def enqueu(self, value) -> None:
        """Add Element to the queue"""
        if self.is_full():
            raise IndexError("The queue is full")
        else:
            self._rear = (self._rear + 1) % self._max_size
            self._arr[self._rear] = value
            self._size = self._size + 1

    def dequeu(self):
        """Remove  element from the queue """
        if self.is_empty():
            raise IndexError("The queue is empty")
        else:
            value = self._arr[self._front]
            self._front = (self._front + 1) % self._max_size
            self._size = self._size - 1
            return value

    def clear_queue(self) -> None:
        self._front = 0
        self._rear = -1
        self._size = 0
        self._max_size = self._max_size

    def __len__(self) -> int:
        return self.size
