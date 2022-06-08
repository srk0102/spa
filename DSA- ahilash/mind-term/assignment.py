def find_gt_lt_eq(lst, num): # -----> time complexity is O(n)
  gt = 0
  lt = 0
  eq = 0
  for i in lst:
    if(i>num):
      gt += 1
    elif(i<num):
      lt += 1
    else:
      eq += 1
  return [gt, lt, eq]

gt, lt, eq = find_gt_lt_eq([1, -2, 5, 0, 10, 8], -2)
print(gt, lt, eq)

def reverse(lst):  # ---------> Time Complexity is O(n)
  return lst[::-1]

print(reverse([1,2,3,4]))

def twoSum(arr, s): # -------> Time Complexity is O(n^2)
  sums = []
  for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
      if(arr[i]+arr[j] == s):
        sums.append([arr[i], arr[j]])
  return sums

print(twoSum([1,2,3,4,5,6],5))

def UpgradedTwoSum(arr, s): # --------> Time Complexity is O(n)
  sums = []
  hashTable = {}
  for i in range(0, len(arr)):
    sumMinusElement = s - arr[i]
    if(str(sumMinusElement) in hashTable):
      sums.append([arr[i], sumMinusElement])
    hashTable[str(arr[i])] = arr[i]
  return sums

print(UpgradedTwoSum([1,2,3,4,5,6],5))

#In Python, a function is a group of related statements that performs a specific task.

#Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

#Furthermore, it avoids repetition and makes the code reusable.

def factorial(n): # ---------> Recursive function example
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Time complexity of an algorithm quantifies the amount of time taken by 
#an algorithm to run as a function of the length of the input. 
#Similarly, Space complexity of an algorithm quantifies the amount of 
#space or memory taken by an algorithm to run as a function of the length 
#of the input.

class Node:
   
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
   
   
# Linked List class contains a Node object
class LinkedList:
   
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
 
    # Print the linked list
    def printList(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")
 
    # Function that returns middle.
    def find_median(self):
        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
        slow = self.head
        fast = self.head
 
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # return the slow's data, which would be the middle element.
        print("The median element is ", slow.data)
 
# Code execution starts here
if __name__=='__main__':
   
    # Start with the empty list
    llist = LinkedList()
   
    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.find_median()