intervals = [[0,3],[2,6],[3,4],[6,9]]
highs = []
lows = []
for i in intervals:
    highs.append(i[1])
    lows.append(i[0])
highs.sort()
lows.sort()
print("{" + str(highs[0]) + "," + str(lows[len(lows)-1]) + "}")