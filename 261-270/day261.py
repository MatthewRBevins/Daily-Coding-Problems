freqs = dict({"a": 5, "b": 3, "c": 7, "d": 2, "e": 10, "f": 1})
class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def addOn(self, val, lR):
        if self.left == None:
            self.left = BT(val)
        elif self.right == None:
            self.right = BT(val)
        else:
            if lR:
                self.left.addOn(val, lR)
            else:
                self.right.addOn(val, lR)


freqsArr = []
for i in freqs.keys():
    freqsArr.append([i, freqs[i]])
for i in range(len(freqsArr)):
    for j in range(len(freqsArr)):
        if freqsArr[j][1] < freqsArr[i][1]:
            temp = freqsArr[i]
            freqsArr[i] = freqsArr[j]
            freqsArr[j] = temp

huffman = BT(freqsArr[0][0])
freqsArr.pop(0)
lR = True
for i in range(len(freqsArr)):
    huffman.addOn(freqsArr[i][0], lR)
    lR = not lR