class bt:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def check(self):
        if (self.left == None and self.right != None) or (self.left != None and self.right == None):
            return False
        elif (self.left == None and self.right == None):
            return True
        elif (self.left.val > self.val or self.right.val < self.val):
            return False
        else:
            if self.left.check() == False:
                return False
            if self.right.check() == False:
                return False
        return True

tree = bt(5, bt(4, bt(3), bt(5)), bt(6, bt(5), bt(7)))
print(tree.check())