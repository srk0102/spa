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

    def deleteDeepest(self,d_node):
        p = self.head
        q = []
        q.append(p)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def deletion(self, key):
        p = self.head
        if p == None:
            return None
        if p.left == None and p.right == None:
            if p.key == key :
                return None
            else :
                return p
        key_node = None
        q = []
        q.append(p)
        temp = None
        while(len(q)):
            temp = q.pop(0)
            if temp.value == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node :
            x = temp.value
            self.deleteDeepest(temp)
            key_node.value = x
        return p

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
print("Is element 5 in the tree? " + str(root.Search(5)))
print()
root.deletion(4)
root.Inorder(p)