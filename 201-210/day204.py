class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    def checkLen(self):
        len = 1
        c = self
        while c.left != None:
            c = c.left
            len += 1
        print(2**len-1)
bt = BT(1, BT(2, BT(3), BT(4)), BT(5, BT(6), BT(7)))
bt.checkLen()