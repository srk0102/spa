class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Function to print the inorder traversal on a given binary tree
def inorder(root):
 
    if root is None:
        return
 
    # recur for the left subtree
    inorder(root.left)
 
    # print the current node's data
    print(root.data, end=' ')
 
    # recur for the right subtree
    inorder(root.right)
 
 
# Recursive function to clone a binary tree
def cloneBinaryTree(root):
 
    # base case
    if root is None:
        return None
 
    # create a new node with the same data as the root node
    root_copy = Node(root.data)
 
    # clone the left and right subtree
    root_copy.left = cloneBinaryTree(root.left)
    root_copy.right = cloneBinaryTree(root.right)
 
    # return cloned root node
    return root_copy

# Given two trees, return true if they are structurally
# identical
def identicalTrees(a, b):
     
    # 1. Both empty
    if a is None and b is None:
        return True
 
    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right))
     
    # 3. one empty, one not -- false
    return False
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)

    clone = cloneBinaryTree(root)

    if identicalTrees(root, root2):
        print("Both trees are identical")
    else:
        print ("Trees are not identical")
 
    print('Inorder traversal of the cloned tree: ', end='')
    inorder(clone)