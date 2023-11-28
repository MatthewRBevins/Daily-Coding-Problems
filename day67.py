class LRU:
    def __init__(self, n):
        self.n = n
        self.dict = dict()
    def set(self, key, value):
        if len(self.dict) == self.n:
            for i in self.dict.keys():
                if self.dict[i][0] == self.n:
                    del self.dict[i]
        self.dict[key] = [value,len(self.dict)]
    def get(self, key):
        return self.dict[key][0]
l = LRU(5)
l.set('name', 'matthew')
print(l.get('name'))
