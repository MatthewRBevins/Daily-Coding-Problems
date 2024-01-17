class stack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        t = self.arr[len(self.arr)-1]
        self.arr = self.arr[0:len(self.arr)-1]
        return t
    def max(self):
        return max(self.arr)
