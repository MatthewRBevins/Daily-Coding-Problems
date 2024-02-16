class ll:
    def __init__(self, val):
        self.val = val
        self.n = None
    def add(self, val):
        cc = self
        while cc.hasNext():
            cc = cc.n
        cc.n = ll(val)
    def hasNext(self):
        return self.n != None
    def printList(self):
        cc = self
        while cc.hasNext():
            print(cc.val)
            cc = cc.n
        print(cc.val)
    def peekNext(self):
        return self.n.val
    def swap(self):
        i = 0
        cc = self
        temp = None
        tempVal = 0
        while cc.hasNext():
            if i % 2 == 0:
                tempVal = cc.val
                cc.val = cc.peekNext()
            else:
                cc.val = tempVal
            i += 1
            cc = cc.n
        if i % 2 != 0:
            cc.val = tempVal

l = ll(1)
l.add(2)
l.add(3)
l.add(4)
l.printList()
print("***")
l.swap()
l.printList()