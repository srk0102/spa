class Node:
    def __init__(self, data, next1):
        self.data = data
        self.next = next1


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def add_head(self, data):
        self.insert_with_index(0, data)

    def add_tail(self, data):
        self.insert_with_index(self.size, data)

    def find_3rd_to_last(self):
      index = self.length() - 3
      if index >= self.size or index < 0:
        print("check given", index, "index value and enter again")
        return False
      current = self.head
      for i in range(index):
        current = current.next
      return current.data

    def insert_with_index(self, index, data):
        if index > self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        if index == 0:
            self.head = Node(data, self.head)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
        self.size += 1


linked_list = Linkedlist()

def execute():
  linked_list.add_head(1)
  linked_list.add_head(2)
  linked_list.add_tail(3)
  linked_list.add_tail(4)
  linked_list.add_tail(5)
  linked_list.add_tail(6)
  print("------------------------------------> find 3rd element")
  print(linked_list.find_3rd_to_last())


if __name__ == "__main__":
  execute()