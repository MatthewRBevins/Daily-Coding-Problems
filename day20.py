class LinkedList:
    def __init__(self, startingNode):
        self.startingNode = startingNode
        self.currentNode = startingNode
    def add(self, node):
        self.currentNode.next = node
        self.currentNode = node
    def len(self):
        c = self.startingNode
        l = 1
        while c.hasNext():
            c = c.next
            l += 1
        return l
class Node:
    def __init__(self, val):
        self.value = val
    def hasNext(self):
        return hasattr(self, 'next')

def findIntersection(l1, l2):
    # After intersecting node, linked lists must end at the same node since nodes with same val are the same
    l1c = l1.startingNode
    l2c = l2.startingNode
    l1len = l1.len()
    l2len = l2.len()
    if l1len > l2len:
        while l1len > l2len:
            l2len += 1
            l1c = l1c.next
    elif l2len > l1len:
        while l2len > l1len:
            l1len += 1
            l2c = l2c.next

    while l1c.hasNext():
        if l1c.value == l2c.value:
            return l1c.value
            break
        l1c = l1c.next
        l2c = l2c.next
    return None
    
l1 = LinkedList(Node(2))
l1.add(Node(7))
l1.add(Node(8))
l1.add(Node(10))

l2 = LinkedList(Node(99))
l2.add(Node(1))
l2.add(Node(8))
l2.add(Node(10))

print(findIntersection(l1, l2))
