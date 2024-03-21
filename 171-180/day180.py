class Stack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        temp = self.arr[len(self.arr)-1]
        del self.arr[len(self.arr)-1]
        return temp
class Queue:
    def __init__(self):
        self.arr = []
    def enqueue(self, val):
        self.arr.append(val)
    def dequeue(self):
        temp = self.arr[0]
        del self.arr[0]
        return temp

s = Stack()
q = Queue()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
n = 5
for i in range(n-1):
    q.enqueue(s.pop())
# 1
# 6, 5, 4, 3, 2
for i in range(n-1):
    if i % 2 != 0:
        for j in range(n-i-2):
            q.enqueue(q.dequeue())
    s.push(q.dequeue())

print(s.arr)