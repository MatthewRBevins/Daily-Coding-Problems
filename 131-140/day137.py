class BitArray:
    def __init__(self, size):
        self.arr = []
        for i in range(size):
            self.arr.append(0)
    def set(self, i, val):
        self.arr[i] = val
    def get(self, i):
        return self.arr[i]

ba = BitArray(10)
ba.set(0,1)
print(ba.get(0))