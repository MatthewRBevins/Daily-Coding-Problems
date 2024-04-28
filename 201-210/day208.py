class ll:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def add(self, value):
        if value == None:
            self.value = value
        else:
            c = self
            while c.next != None:
                c = c.next
            c.next = ll(value)
    def traverse(self):
        c = self
        while c.next != None:
            print(c.value)
            c = c.next
        print(c.value)
l = ll(5)
l.add(1)
l.add(8)
l.add(0)
l.add(3)
l.traverse()

k = 3
c = l
nl1 = ll()
nl2 = ll()
while c.next != None:
    if c.value < k:
        nl1.add(c.value)
    else:
        nl2.add(c.value)
    c = c.next
if c.value < k:
    nl1.add(c.value)
else:
    nl2.add(c.value)
c = nl2
while c.next != None:
    nl1.add(c.value)
    c = c.next
nl1.add(c.value)
nl1.traverse()