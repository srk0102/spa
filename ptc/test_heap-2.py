from heap import Heap

th = Heap()

th.add(56)
th.add(67)
th.add(43)
th.add(54)
th.add(66)
th.add(90)
th.add(123)

print(th.empty()) # result = False
print(th.remove_min()) # result = 43