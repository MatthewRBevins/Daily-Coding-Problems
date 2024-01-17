class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def checkSubtrees(self, num):
        l = 0
        r = 0
        lval = -1
        rval = -1
        if self.left is not None:
            l = self.left.checkSubtrees(num)
            lval = self.left.val
        if self.right is not None:
            r = self.right.checkSubtrees(num)
            rval = self.right.val
        if  lval == rval:
            num += 1
        return num + l + r
node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(node.checkSubtrees(0))
