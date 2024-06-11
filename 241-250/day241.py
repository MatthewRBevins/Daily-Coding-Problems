N = 5
c = [4, 3, 0, 1, 5]
hIndex = 0
for i in range(N):
    h = 0
    for j in c:
        if j >= i:
            h += 1
    if h >= i:
        hIndex = i
print(hIndex)