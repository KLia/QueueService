import unittest
from controllers.queue import Queue

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue_is_empty_on_startup(self):
        self.assertTrue(self.queue.isEmpty())

    def test_queue_size_is_0_on_startup(self):
        self.assertEqual(self.queue.size(), 0)

    def test_enqueue_queue_size_is_1(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)

    def test_enqueue_queue_size_is_5(self):
        limit = 5
        for i in range(1, limit+1):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size(), limit)

    def test_dequeue_queue_size_is_0(self):
        self.queue.enqueue(1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)
    
    def test_dequeue_returns_pushed_item(self):
        self.queue.enqueue(1)
        item = self.queue.dequeue()
        self.assertEqual(item, 1)

    def test_dequeue_empty_raises_IndexError_exception(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

if __name__ == '__main__':
    unittest.main()