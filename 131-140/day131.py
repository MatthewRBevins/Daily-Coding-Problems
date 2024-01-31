from random import randint
class ll:
    def __init__(self, val):
        self.val = val
        # placeholder
        self.random = randint(0, 50)
        self.next = None
    def hasNext(self):
        if self.next != None:
            return True
        return False
    def add(self, val):
        c = self
        while c.hasNext():
            c = c.next
        c.next = ll(val)
    def deepcopy(self):
        c = self
        newL = ll(c.val)
        newL.random = c.random
        print(c.val)
        while c.hasNext():
            c = c.next
            newL.add(c.val)
            n = newL.next
            n.random = c.random
            print(c.val)
        return newL

l = ll(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
lll = l.deepcopy()
lll.deepcopy()