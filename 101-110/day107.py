class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def printLevels(self):
        print(self.value)
        if self.left != None:
            self.left.printLevels()
        if self.right != None:
            self.right.printLevels()
bt = Node(1, Node(2), Node(3, Node(4), Node(5)))
bt.printLevels()