class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.head = None

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
print("Is element 5 in the tree?" + str(root.Search(5)))
