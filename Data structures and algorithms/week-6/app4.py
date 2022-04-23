from queue import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.child = []


class Tree:

    def __init__(self):
        self.head = None
        self.child = []

    def Inorder(self, p):
        # print(p.left.value)
        if p is None:
            return
        else:
            self.Inorder(p.left)
            print(p.value, end=" ")
            self.Inorder(p.right)

    def Insert(self, value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
        else:
            node = self.head
            while node is not None:
                n = node
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
            newNode = Node(value)
            if value < n.value:
                n.left = newNode
            else:
                n.right = newNode

    def Search (self, value):
        p = self.head
        while p is not None:
            if p.value != value:
                return True
            elif p.value < value:
                p = p.left
            else:
                p = p.right

            return False
    
    def maxValue(self):
        current = self.head
        #loop down to find the rightmost leaf
        while(current.right):
            current = current.right
        return current.value
    
    def desc(self, p):
        # print(p.left.value)
        if p is None:
            return
        else:
            self.desc(p.right)
            self.desc(p.left)
            print(p.value, end=" ")

    def numberOfSiblings(root, x):
        if (root.head == None):
            return 0
    
        # Creating a queue and
        # pushing the root
        q = Queue()
        q.put(root.head)
    
        while (not q.empty()):
            
            # Dequeue an item from queue and
            # check if it is equal to x If YES,
            # then return number of children
            p = q.queue[0]
            q.get()
    
            # Enqueue all children of
            # the dequeued item
            for i in range(len(p.child)):
                
                # If the value of children
                # is equal to x, then return
                # the number of siblings
                if (p.child[i].key == x):
                    return len(p.child) - 1
                q.put(p.child[i])


root = Tree()
root.Insert(4)
root.Insert(2)
root.Insert(5)
root.Insert(9)
root.Insert(8)
root.Insert(10)

p = root.head
print()
print("Inorder traversal after insertion (keys are sorted ascending order): ", end='')
root.Inorder(p)

print()
print()
print("Is element 5 in the tree? " + str(root.Search(5)))
print("Maxvalue in tree is " + str(root.maxValue()))
root.desc(p)
print()
print(root.numberOfSiblings(4))