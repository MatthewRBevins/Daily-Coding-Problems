class Iterator:
    def __init__(self, arr):
        self.arr = arr
        self.index1 = 0
        self.index2 = 0
    def next(self):
        while self.index1 >= len(self.arr) or self.index2 >= len(self.arr[self.index1]):
            if self.index2 >= len(self.arr[self.index1]):
                self.index1 += 1
                self.index2 = 0
            if self.index1 >= len(self.arr):
                return False
        i2 = self.index2
        self.index2 += 1
        return self.arr[self.index1][i2]
    def hasNext(self):
        if self.index2 < len(self.arr[self.index1]):
            return True
        for i in range(self.index1+1,len(self.arr)):
            if len(self.arr[i]) > 0:
                return True
        return False

lst = [[1,2],[3],[],[4,5,6]]
i = Iterator(lst)
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())
print(i.next())
print(i.hasNext())