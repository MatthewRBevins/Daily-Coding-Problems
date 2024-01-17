import copy
class ll:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
    def reverse(self):
        prev = None
        curr = self
        next = self.nextNode
        while curr is not None:
            curr.nextNode = prev
            prev = curr
            curr = next
            if next is None:
                break
            next = next.nextNode
        self = prev

h = ll(1, ll(2, ll(3, ll(4, ll(5, ll(6))))))
h.reverse()