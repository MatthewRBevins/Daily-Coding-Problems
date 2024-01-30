def stringReverse(s):
    arr = []
    for i in s:
        arr.append(i)
    arr.reverse()
    s = ""
    for i in arr:
        s += i
    return s

class ll:
    def __init__(self, val):
        self.val = val
        self.next = None
    def hasNext(self):
        if self.next != None:
            return True
        return False
    def add(self, val):
        c = self
        while c.hasNext():
            c = c.next
        c.next = ll(val)
    def getNum(self):
        c = self
        val = ""
        while c.hasNext():
            val += str(c.val)
            c = c.next
        val += str(c.val)
        return int(stringReverse(val))

def addNums(ll1, ll2):
    added = ll1.getNum() + ll2.getNum()
    finalStr = ""
    for i in str(added):
        finalStr += i
    finalStr = stringReverse(finalStr)
    finalLL = ll(int(finalStr[0]))
    for i in range(1,len(finalStr)):
        finalLL.add(int(finalStr[i]))
    return finalLL

l1 = ll(9)
l1.add(9)
l2 = ll(5)
l2.add(2)
print(addNums(l1, l2).val)