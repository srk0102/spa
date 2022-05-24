from heap import Heap

heap = Heap()

# Adding numbers into heap
def addElementsToHeap(arr):
  for i in arr:
    heap.add(i)

heap_elements = [651,654,65,46,5,31,31,35,351,31]
addElementsToHeap(heap_elements)

# after adding heap location -> [0, 1, 3, 5, 10 ,50]

print(heap.empty()) # testing empty result = False
print(heap.remove_min()) # testing remove_min result = 5