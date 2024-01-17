class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def evaluate(self, prev, firstLevel):
        if str(type(self.left)) == "<class 'int'>":
            s = '(' + str(self.left) + self.val + str(self.right) + ')'
            prev += s
        else:
            s = self.val
            tprev = prev
            prev += self.left.evaluate(prev, False)
            prev += s
            prev += self.right.evaluate(tprev, False)
        if firstLevel:
            return eval(prev)
        else:
            return prev

node = BinaryTree('*',BinaryTree('+',3,2),BinaryTree('+',4,5))
print(node.evaluate('', True))
