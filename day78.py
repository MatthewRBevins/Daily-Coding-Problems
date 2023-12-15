class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.cur = self
        self.n = n
    def add(self, val):
        self.cur.n = Node(val)
        self.cur = self.cur.n
    def printll(self):
        cur = self
        while cur.n != None:
            print(cur.val)
            cur = cur.n
        print(cur.val)

ll1 = Node(3, Node(6, Node(9, Node(12, Node(15)))))
ll2 = Node(1, Node(5, Node(7, Node(11, Node(13)))))
ll3 = Node(2, Node(4, Node(8, Node(10, Node(14)))))

def checkHasNext(lls):
    for i in lls:
        if i.n != None:
            return True
    return False

def getVals(lls):
    arr = []
    for i in lls:
        arr.append(i.val)
    return arr

def mergells(lls):
    finalLL = Node()
    while(checkHasNext(lls)):
        vals = getVals(lls)
        finalLL.add(min(vals))
        lls[vals.index(min(vals))] = lls[vals.index(min(vals))].n
    a = getVals(lls)
    a.sort()
    for i in a:
        finalLL.add(i)
    return finalLL.n

f = mergells([ll1,ll2,ll3])
f.printll()