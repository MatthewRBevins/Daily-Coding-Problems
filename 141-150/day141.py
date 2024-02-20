def removeAtIndex(l, i):
    finalL = []
    for j in range(len(l)):
        if j != i:
            finalL.append(l[j])
    return finalL
class Stack:
    def __init__(self):
        self.list = ['*', '*', '*']

    def pop(self, stack_number):
        n = 0
        for i in range(len(self.list)):
            if self.list[i] == "*":
                n += 1
            if n == stack_number:
                self.list = removeAtIndex(self.list, i+1)
                break

    def push(self, item, stack_number):
        n = 0
        for i in range(len(self.list)):
            if self.list[i] == "*":
                n += 1
            if n == stack_number:
                self.list.insert(i + 1, item)
                break


s = Stack()
s.push(1,1)
s.push(5,1)
s.pop(1)
s.push(2,2)
s.push(3,3)
print(s.list)
