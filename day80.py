class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverse(self, layer):
        biggestLayer = 0
        biggestVal = 0
        if self.left == None and self.right == None:
            return [self.val, layer]
        if self.left != None:
            t = self.left.traverse(layer+1)
            if t[1] > biggestLayer:
                biggestVal = t[0]
                biggestLayer = t[1]
        if self.right != None:
            t = self.right.traverse(layer+1)
            if t[1] > biggestLayer:
                biggestVal = t[0]
                biggestLayer = t[1]
        return [biggestVal, biggestLayer]
a = Node(1,Node(2,Node(3)),Node(4))
print(a.traverse(1))
