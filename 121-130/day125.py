class bt:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
    def listify(self, arr, level, k):
        arr.append(self.val)
        if self.l != None:
            arr.append(self.l.listify(arr, 1, k))
        if self.r != None:
            arr.append(self.r.listify(arr, 1, k))
        narr = []
        if level == 0:
            for i in arr:
                if type(i) == int:
                    narr.append(i)
            for i in range(len(narr)):
                for j in range(len(narr)):
                    if i != j and narr[i] + narr[j] == k:
                        return [narr[i], narr[j]]
        return -1

node = bt(10, bt(5), bt(15, bt(11), bt(15)))
print(node.listify([], 0, 20))