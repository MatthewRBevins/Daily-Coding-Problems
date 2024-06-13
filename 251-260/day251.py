stream = [1, 3, 2, 5] # Theoretically a million integers long
sorted = []
for i in stream:
    if len(sorted) == 0:
        sorted.append(i)
    else:
        p = False
        for j in range(len(sorted)-1):
            if sorted[j+1] > i:
                sorted.insert(j+1, i)
                p = True
        if not p:
            sorted.append(i)
print(sorted)