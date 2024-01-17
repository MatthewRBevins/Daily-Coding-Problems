options = []
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def findSum(self, curSum, level):
        global options
        curSum += self.val
        l = 0
        r = 0
        if self.left != None:
            l = self.left.findSum(curSum, 2)
        if self.right != None:
            r = self.right.findSum(curSum, 1)
        if l > r:
            curSum += l
        else:
            curSum += r
        if (self.left == None and self.right == None):
            options.append(curSum)
            print(curSum)
        if level == 0:
            return max(options)
        return curSum

t = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, right=Node(14, left=Node(13))))
print(t.findSum(0, 0))