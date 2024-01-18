
from queue import QueueList
import unittest


class TestQueueList(unittest.TestCase):
    def setUp(self):
        self.myqueue = QueueList()

    def test_enqueue(self):
        self.myqueue.enqueue(5)
        self.assertEqual(self.myqueue.get_size(), 1)
        self.assertEqual(self.myqueue.dequeue(), 5)

    def test_dequeue(self):
        self.myqueue.enqueue(5)
        self.myqueue.enqueue(10)
        value = self.myqueue.dequeue()
        self.assertEqual(value, 5)
        self.assertEqual(self.myqueue.get_size(), 1)

    def test_clear_queue(self):
        self.myqueue.enqueue(5)
        self.myqueue.enqueue(10)
        self.myqueue.clear_queue()
        self.assertTrue(self.myqueue.is_empty())
        self.assertEqual(self.myqueue.get_size(), 0)

    def test_dequeue_empty_queue(self):
        try:
            value = self.myqueue.dequeue()
        except IndexError:
            value = None
        self.assertIsNone(value)
        self.assertTrue(self.myqueue.is_empty())

    def test_front(self):
        self.myqueue.enqueue(5)
        value = self.myqueue.front()
        self.assertEqual(value, 5)
        self.assertEqual(self.myqueue.get_size(), 1)

    def tearDown(self):
        del self.myqueue


if __name__ == '__main__':
    unittest.main()
