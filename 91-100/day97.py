class timedMap:
    def __init__(self):
        self.store = dict()
    def set(self, key, value, time):
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([time, value])
        self.store[key].sort()
    def get(self, key, time):
        val = None
        for i in range(len(self.store[key])-1):
            if self.store[key][i][0] <= time and self.store[key][i+1][0] > time:
                val = self.store[key][i][1]
        if val == None:
            val = self.store[key][len(self.store[key])-1][1]
        return val
m = timedMap()
m.set(1,1,0)
m.set(1,2,2)
print(m.get(1,3))