class PrefixMapSum:
    def __init__(self):
        self.d = dict()
    def insert(self, key, value):
        self.d[key] = value
    def sum(self, prefix):
        s = 0
        for i in self.d.keys():
            if i[:len(prefix)] == prefix:
                s += self.d[i]
        return s

mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
mapsum.insert("colu", 5)
mapsum.insert("co", 4)
print(mapsum.sum("col"))