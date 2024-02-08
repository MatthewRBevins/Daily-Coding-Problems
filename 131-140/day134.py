class SparseArray:
    def __init__(self, arr, size):
        self.arrDict = dict()
        for index, val in enumerate(arr):
            if val != 0:
                self.arrDict[index] = val

    def set(self, i, val):
        self.arrDict[i] = val

    def get(self, i):
        if not i in self.arrDict:
            return 0
        return self.arrDict[i]


origArr = [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 1, 2, 0, 0, 0]
sa = SparseArray(origArr, len(origArr))
print(sa.get(6))
