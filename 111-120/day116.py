from random import random, randint
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def generate(self, node, prob=0.75):
        if random() > prob:
            return
        if random() < prob:
            node.left = Node(randint(1,1000))
            self.generate(node)
        if random() < prob:
            node.right = Node(randint(1,1000))
            self.generate(node)
    def printSelf(self):
        print(self.value)
        if self.left != None:
            self.left.printSelf()
        if self.right != None:
            self.right.printSelf()

bt = Node(randint(1,1000))
bt.generate(bt)
bt.printSelf()