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
        if l < r:
            curSum += l
        else:
            curSum += r
        if (self.left == None and self.right == None):
            options.append(curSum)
            print(curSum)
        if level == 0:
            return min(options)
        return curSum


t = Node(10, Node(5, right=Node(2)), Node(5, right=Node(1, Node(-1))))
print(t.findSum(0, 0))