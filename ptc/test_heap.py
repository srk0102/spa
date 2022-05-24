from heap import Heap

test = Heap()
# Adding numbers into heap
arr = [1,2,3,4,5,6]
for i in arr:
  test.add(i)

# after adding heap location -> [0, 1, 3, 5, 10 ,50]

print(test.empty()) # testing empty result = False
print(test.remove_min()) # testing remove_min result = 1