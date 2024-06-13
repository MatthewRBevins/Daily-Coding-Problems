from random import randint
newSubs = []
for i in range(24):
    newSubs.append(randint(1,10))

class Subscribers:
    def __init__(self, arr):
        self.arr = arr
    def update(self, hour, value):
         self.arr[hour] += value
    def query(self, start, end):
        return sum(self.arr[start:end])

print(newSubs)
s = Subscribers(newSubs)
print(s.query(5, 10))