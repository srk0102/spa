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
        self.v = None

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
        self.v = self.data[1]
        del self.data[1]
        self.size -= 1

    def insert_before_Last(self):
        # replace "pass" with your code to insert the element before last element in the queue
        self.data.insert(self.size-1, self.v)
        self.v = None
        self.size += 1

# ================================================================
# Second Scenario: Simple queue implemented using array-based (list)
class SimpleQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * SimpleQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.v = None

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
        self.v = self.data[1]
        del self.data[1]
        self.size -= 1

    def insert_before_Last(self):
        # replace "pass" with your code to insert the element before last element in the queue
        self.data.insert(self.size -1, self.v)
        self.v = None
        self.size += 1


# ================================================================
# Third Scenario: Circular queue implemented using array-based (list)
class CircularQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * CircularQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.v = None

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
        self.v = self.data[1]
        del self.data[1]
        self.size -= 1

    def insert_before_last(self):
        # replace "pass" with your code to insert the element before last element in the queue
        self.data.insert(self.size -1, self.v)
        self.v = None
        self.size += 1


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
        self.size = 0
        self.v = None  # number of queue elements

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
        self.size -= 1
        current = self.head
        for i in range(0):
            current = current.next
        temp = current.next
        current.next = current.next.next
        self.v = temp.element


    def insert_before_last(self):
        # replace "pass" with your code to insert the element before last element in the queue
        current = self.head
        for i in range(self.size-2):
            current = current.next
        current.next = self.Node(self.v, current.next)


# ================================================================
# Fifth Scenario: Queue implemented using Doubly linked list
class DoublyLinkedBase:

    # -------------------------- nested _Node class --------------------------
    # nested _Node class
    class Node:

        def __init__(self, element):  # initialize node's fields
            self.element = element  # user's element
            self.prev = None  # previous node reference
            self.next = None  # next node reference

    # -------------------------- list constructor --------------------------
    def __init__(self):
        """Create an empty list."""
        self.head = None
        self.last = None
        self.size = 0
        self.v = []

    # -------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def is_empty(self):
        """Return True if list is empty."""
        return self.size == 0

    # -------------------------- nonpublic utilities --------------------------

    def print_queue(self):
        n = self.head
        while n is not None:
            print(n.element, end=" ")
            n = n.next

    def insert_between(self, e):
        """Add element e between two existing nodes and return new node."""
        if self.last is None:
            self.head = self.Node(e)
            self.last = self.head
        else:
            self.last.next = self.Node(e)
            self.last.next.prev=self.last
            self.last = self.last.next
        self.size += 1

    # add your cade here
    def deque(self):
        if self.head is None:
            return None
        else:
            temp= self.head.element
            self.head = self.head.next
            self.head.prev=None
            return temp

    def remove_second_element(self):
        # replace "pass" with your code to remove second element in the 
        for i in range(self.size-1):
            self.v.append(self.deque())

    def insert_before_last(self):
        # replace "pass" with your code to insert the element before last element in the queue
        arr = self.v
        temp = arr[1]
        arr[1] = arr[-1]
        arr[-1] = temp
        for i in arr:
            self.insert_between(i)
        tempOfLastList = self.deque()
        self.insert_between(tempOfLastList)


# at least insert five values to the queue. print queue before and after
# ======================================================================

# add your code to test first scenario here

amq = ArrayModuleQueue()
def amqInto():
    amq.enqueue(1)
    amq.enqueue(2)
    amq.enqueue(3)
    amq.enqueue(4)
    amq.enqueue(5)
    amq.print_queue()
    print("")
    amq.remove_second_element()
    amq.insert_before_Last()
    amq.print_queue()
amqInto()


# # add your code to test second scenario here

# sq = SimpleQueue()
# def sqInto():
#     sq.enqueue(1)
#     sq.enqueue(2)
#     sq.enqueue(3)
#     sq.enqueue(4)
#     sq.enqueue(5)
#     sq.print_queue()
#     print("")
#     sq.remove_second_element()
#     sq._resize(10)
#     sq.insert_before_Last()
#     sq.print_queue()
# sqInto()

# # add your code to test third scenario here

# cq = CircularQueue()
# def cqInto():
#     cq.enqueue(1)
#     cq.enqueue(2)
#     cq.enqueue(3)
#     cq.enqueue(4)
#     cq.enqueue(5)
#     cq.print_queue()
#     print("")
#     cq.remove_second_element()
#     cq._resize(10)
#     cq.insert_before_last()
#     cq.print_queue()
# cqInto()

# add your code to test fourth scenario here

# sll = SinglyLinkedList()
# def sllInto():
#     sll.enqueue(1)
#     sll.enqueue(2)
#     sll.enqueue(3)
#     sll.enqueue(4)
#     sll.enqueue(5)
#     sll.print_queue()
#     print("")
#     sll.remove_second_element()
#     sll.insert_before_last()
#     sll.print_queue()
# sllInto()

# add your code to test fifth scenario here

# dlb = DoublyLinkedBase()
# def dlbInto():
#     dlb.__init__()
#     dlb.insert_between(1)
#     dlb.insert_between(2)
#     dlb.insert_between(3)
#     dlb.insert_between(4)
#     dlb.insert_between(5)
#     dlb.print_queue()
#     print("")
#     dlb.remove_second_element()
#     dlb.insert_before_last()
#     dlb.print_queue()
# dlbInto()
