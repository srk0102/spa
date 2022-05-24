class Heap:
    def __init__(self):
        self._heap = [0]

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _last_idx(self):
        return len(self._heap) - 1

    def _left(self, i):
        return i * 2

    def _right(self, i):
        return i * 2 + 1

    def _parent(self, i):
        return i // 2

    def _has_left(self, i):
        return self._left(i) < len(self._heap)

    def _has_right(self, i):
        return self._right(i) < len(self._heap)

    def empty(self):
        return len(self._heap) == 1

    def add(self, key):
        self._heap.append(key)

        j = self._last_idx()

        while j > 1 and self._heap[j] < self._heap[self._parent(j)]:
            self._swap(j, self._parent(j))
            j = self._parent(j)


    def remove_min(self):
        if self.empty():
            raise Exception()

        self._swap(1, self._last_idx())
        result = self._heap[-1]
        self._heap.pop()

        # push new element down the heap
        j = 1
        while True:
            min = j
            if self._has_left(j) and self._heap[self._left(j)] < self._heap[min]:
                min = self._left(j)

            if self._has_right(j) and self._heap[self._right(j)] < self._heap[min]:
                min = self._right(j)

            if min == j:
                #found right location for min, break
                break

            self._swap(j, min)
            j = min

        return result


def heap_sort(l):
    heap = Heap()
    #phase I: nlogn
    for e in l:
        heap.add(e)

    sorted_list = []
    #phase II: nlogn
    while not heap.empty():
        sorted_list.append(heap.remove_min())

    return sorted_list

print(heap_sort([3, 1, 10, 5, 0, 50]))