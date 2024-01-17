class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def findSecondLargest(self, chain):
        chain.append(self.value)
        chain.sort()
        if self.left is not None:
            self.left.findSecondLargest(chain)
        if self.right is not None:
            self.right.findSecondLargest(chain)
        return chain[len(chain)-2]


n = Node(5,Node(6,Node(7),Node(4)),Node(1))
print(n.findSecondLargest([]))
