class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def convert(self):
        c = self
        while ((c.right == None and c.left != None) or (c.left == None and c.right != None)):
            if (c.left == None and c.right != None):
                c = c.right
            else:
                c = c.left
        if c != None and c.right != None:
            c.right = c.right.convert()
        if c != None and c.left != None:
            c.left = c.left.convert()
        return c

b = BT(0, BT(1, BT(3, None, BT(5))), BT(2, None, BT(4, BT(6), BT(7))))
b = b.convert()
print(b.val)
print(b.left.val)