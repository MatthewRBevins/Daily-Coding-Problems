class Heap:
    def __init__(self):
        self.arr = []
    def push(self, item):
        self.arr.append(item)
    def pop(self):
        largest = 0
        largestI = 0
        for i in range(len(self.arr)):
            if self.arr[i] > largest:
                largest = self.arr[i]
                largestI = i
        del self.arr[largestI]
        return largest

class Stack:
    def __init__(self):
        self.h = Heap()
        self.lastAdded = []
    def push(self, item):
        self.h.push(item)
        self.lastAdded.append(item)
    def pop(self):
        popped = self.h.pop()
        newH = Heap()
        while popped != self.lastAdded[len(self.lastAdded)-1]:
            newH.push(popped)
            popped = self.h.pop()
        for i in self.h.arr:
            newH.push(i)
        self.lastAdded.pop()
        self.h = newH

s = Stack()
s.push(1)
s.push(2)
s.push(5)
s.push(4)
s.push(3)
s.pop()
print(s.h.arr)