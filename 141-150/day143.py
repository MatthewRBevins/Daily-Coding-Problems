x = 10
lst = [9, 12, 3, 5, 14, 10, 10]
parts = [[], [], []]
partitioned = []
for i in lst:
    if i < x:
        parts[0].append(i)
    elif i == x:
        parts[1].append(i)
    else:
        parts[2].append(i)
for i in parts:
    for j in i:
        partitioned.append(j)
print(partitioned)