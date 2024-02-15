class bt:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
    def checkZeroes(self):
        if self.val == 1:
            return False
        if self.r == None and self.l == None:
            return True
        ll = None
        if self.l != None:
            ll = self.l.checkZeroes()
        rr = None
        if self.r != None:
            rr = self.r.checkZeroes()
    def delZeroed(self):
        if self.checkZeroes():
            self.val = None
            self.l = None
            self.r = None
        if self.l != None:
            self.l.delZeroed()
        if self.r != None:
            self.r.delZeroed()
    def printTree(self):
        if self.val != None:
            print(self.val)
        if self.l != None:
            self.l.printTree()
        if self.r != None:
            self.r.printTree()

b = bt(0, bt(1), bt(0, bt(1, bt(0), bt(0)), bt(0)))
b.printTree()
b.delZeroed()
print("***")
b.printTree()