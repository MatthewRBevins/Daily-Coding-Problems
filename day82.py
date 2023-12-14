class file:
    def __init__(self, contents):
        self.contents = contents
        self.index = 0
    def read7(self):
        toread = self.contents[self.index:self.index+7]
        self.index += 7
        return toread
    def readN(self, n):
        final = ""
        while n > 7:
            final += self.read7()
            n -= 7
        final += self.read7()[:n]
        return final
        
    
f = file("hello world")
print(f.readN(9))