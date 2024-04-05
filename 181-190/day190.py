array = [8, -1, 3, 4]
bestSum = 0
ranges = [[0]]
index = 0

for i in range(len(array)):
    if array[i] < 0:
        ranges[index].append(i-1)
        ranges.append([i+1])
        index += 1
ranges[index].append(len(array)-1)
ranges[index].append(ranges[0][1])
for i in ranges:
    s = -1
    if len(i) == 2:
        s = sum(array[i[0]:i[1]+1])
    else:
        s = sum(array[i[0]:i[1]+1]) + sum(array[0:i[2]+1])
    if s > bestSum:
        bestSum = s
print(bestSum)