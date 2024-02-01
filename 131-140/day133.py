class bt:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
    def hasParent(self):
        return self.parent != None
    def checkSuccessor(self):
        c = self
        init = self.val
        lowestDiff = 100
        successor = 0
        while c.hasParent():
            diff = c.val - init
            if diff > 0 and diff < lowestDiff:
                successor = c.val
            c = c.parent
        diff = c.val - init
        if diff > 0 and diff < lowestDiff:
            successor = c.val
        return successor

rrr = bt(35)
rrl = bt(22)
rr = bt(30)
rl = bt(5)
r = bt(10)
r.left = rl
r.right = rr
rl.parent = r
rr.parent = r
rr.left = rrl
rr.right = rrr
rrl.parent = rr
rrr.parent = rr
print(rrl.checkSuccessor())