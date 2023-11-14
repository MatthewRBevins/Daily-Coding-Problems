class stack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        if len(self.arr) > 0:
            removed = self.arr[len(self.arr)-1]
            self.arr.pop()
            return removed
        return -1

class queue:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
    def enqueue(self, val):
        while len(self.stack2.arr) > 0:
            self.stack1.push(self.stack2.pop())
        self.stack1.push(val)
    def dequeue(self):
        while len(self.stack1.arr) > 0:
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print(q.stack1.arr)
print(q.stack2.arr)
