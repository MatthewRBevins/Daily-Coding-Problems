class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    def hasNext(self):
        return self.next != None
    def add(self, val):
        c = self
        while c.hasNext():
            c = c.next
        c.next = LinkedList(val)
    def length(self):
        l = 0
        c = self
        while c.hasNext():
            l += 1
            c = c.next
        return l+1
    def rotate(self, k):
        c = self
        i = 0
        toMakeStart = None
        toMakeEnd = LinkedList(c.val)
        while c.hasNext():
            c = c.next
            i += 1
            if i == self.length()-k:
                toMakeStart = c
                break
            else:
                toMakeEnd.add(c.val)
        while toMakeEnd.hasNext():
            toMakeStart.add(toMakeEnd.val)
            toMakeEnd = toMakeEnd.next
        toMakeStart.add(toMakeEnd.val)
        return toMakeStart
    def printList(self):
        c = self
        while c.hasNext():
            print(c.val)
            c = c.next
        print(c.val)

ll = LinkedList(7)
ll.add(7)
ll.add(3)
ll.add(5)
ll.printList()
print("***")
ll.rotate(2).printList()