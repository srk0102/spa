from unittest import TestCase
from App.heap import Heap


class TestHeap(TestCase):
    def setUp(self):
        self._heap = Heap()

    def empty(self):
        self.assertEqual(self._heap.empty(), True)

    def heap_with_greaterThan_zero(self):
        self._heap.add(10)
        self.assertEqual(self._heap.empty(), False)

    def delete_min(self):
        self._heap.add(1)
        self._heap.add(2)
        self._heap.add(3)
        self._heap.add(4)

        self.assertEqual(self._heap.remove_min(), 1)

    def deleter_empty_heap(self):
        with self.assertRaises(Exception):
            self._heap.remove_min()