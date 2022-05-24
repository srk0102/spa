from heap import Heap

test_heap = Heap()
# Adding numbers into heap sort
test_arr = [3,4,5,6,7,8,9,4,333]
for i in test_arr:
  test_heap.add(i)

print(test_heap.empty()) # result = False
print(test_heap.remove_min()) # result = 3