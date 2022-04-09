import array as arr


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# ================================================================
# First Scenario: Queue implemented using Array module
class ArrayModuleQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self.data = arr.array("i", [] * ArrayModuleQueue.DEFAULT_CAPACITY)
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        for i in range(self.front, self.size + self.front):
            print(self.data[i], end=" ")

    def enqueue(self, e):
        """Add an element to the back of queue."""
        self.data.append(e)
        self.size += 1

    # add your cade here
    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the queue
        pass

    def insert_before_Last(self, v):
        # replace "pass" with your code to insert the element before last element in the queue
        pass

# ================================================================
# Second Scenario: Simple queue implemented using array-based (list)
class SimpleQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * SimpleQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        for i in range(self.front, self.size + self.front):
            print(self.data[i], end=" ")

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self.size == len(self.data):
            self._resize(2 * len(self.data))  # double the array size
        avail = self.size
        self.data[avail] = e
        self.size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self.data  # keep track of existing list
        self.data = [None] * cap  # allocate list with new capacity
        walk = self.front
        for k in range(self.size):  # only consider existing elements
            self.data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self.front = 0  # front has been realigned

    # add your cade here
    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the queue
        pass

    def insert_before_Last(self, v):
        # replace "pass" with your code to insert the element before last element in the queue
        pass


# ================================================================
# Third Scenario: Circular queue implemented using array-based (list)
class CircularQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * CircularQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        walk = self.front - 1
        for i in range(self.size):
            walk = (1 + walk) % len(self.data)
            print(self.data[walk], end=" ")

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self.size == len(self.data):
            self._resize(2 * len(self.data))  # double the array size
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self.data  # keep track of existing list
        self.data = [None] * cap  # allocate list with new capacity
        walk = self.front
        for k in range(self.size):  # only consider existing elements
            self.data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self.front = 0  # front has been realigned

    # add your cade here
    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the queue
        pass

    def insert_before_last(self, e):
        # replace "pass" with your code to insert the element before last element in the queue
        pass


# ================================================================
# Fourth Scenario: Queue implemented using Singly Linked list
class SinglyLinkedList:

    # -------------------------- nested _Node class --------------------------
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next):
            self.element = element
            self.next = next

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def print_queue(self):
        n = self.head
        while n is not None:
            print(n.element, end=" ")
            n = n.next

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self.Node(e, None)  # node will be new tail node
        if self.is_empty():
            self.head = newest  # special case: previously empty
        else:
            self.tail.next = newest
        self.tail = newest  # update reference to tail node
        self.size += 1

    # add your cade here
    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the queue
        pass

    def insert_before_last(self, e):
        # replace "pass" with your code to insert the element before last element in the queue
        pass


# ================================================================
# Fifth Scenario: Queue implemented using Doubly linked list
class DoublyLinkedBase:

    # -------------------------- nested _Node class --------------------------
    # nested _Node class
    class Node:

        def __init__(self, element, prev, next):  # initialize node's fields
            self.element = element  # user's element
            self.prev = prev  # previous node reference
            self.next = next  # next node reference

    # -------------------------- list constructor --------------------------
    def __init__(self):
        """Create an empty list."""
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer  # trailer is after header
        self.trailer.prev = self.header  # header is before trailer
        self.size = 0  # number of elements

    # -------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def is_empty(self):
        """Return True if list is empty."""
        return self.size == 0

    # -------------------------- nonpublic utilities --------------------------

    def print_queue(self):
        n = self.header.next
        while n != self.trailer:
            print(n.element, end=" ")
            n = n.next

    def insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self.Node(e, predecessor, successor)  # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    # add your cade here
    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the queue
        pass

    def insert_before_last(self, e):
        # replace "pass" with your code to insert the element before last element in the queue
        pass


# at least insert five values to the queue. print queue before and after
# ======================================================================

# add your code to test first scenario here


# # add your code to test second scenario here


# # add your code to test third scenario here


# add your code to test fourth scenario here


# add your code to test fifth scenario here


