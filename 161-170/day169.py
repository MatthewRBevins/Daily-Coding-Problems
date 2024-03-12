class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    def add(self, val):
        self.next = LinkedList(val)