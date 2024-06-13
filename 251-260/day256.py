class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def switch_indices(self, index1, index2):
        if index1 == index2:
            return

        prev1 = None
        current1 = self.head
        index = 0
        while current1 and index != index1:
            prev1 = current1
            current1 = current1.next
            index += 1

        prev2 = None
        current2 = self.head
        index = 0
        while current2 and index != index2:
            prev2 = current2
            current2 = current2.next
            index += 1

        if not current1 or not current2:
            print("One or both indices are out of bounds.")
            return

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current1

        temp = current1.next
        current1.next = current2.next
        current2.next = temp

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

current_node = ll.head
prevData = -1
i = 0
while current_node:
    if i > 0 and i % 2 == 0 and prevData < current_node.data:
        ll.switch_indices(i, i-1)
    if current_node:
        prevData = 0
        prevData += current_node.data
    current_node = current_node.next
    i += 1
ll.print_list()