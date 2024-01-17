m = 5
bishops = [
    (0,0),
    (1,2),
    (2,2),
    (4,0)
]
pairs = []
for ii,i in enumerate(bishops):
    r = i[0]
    c = i[1]
    s = [r,c]
    while s[0] > 0 and s[1] > 0:
        s[0] -= 1
        s[1] -= 1
    while s[0] < m-1 and s[1] < m-1:
        s[0] += 1
        s[1] += 1
        if (s[0], s[1]) in bishops and (s[0], s[1]) != i:
            a = [bishops.index((s[0], s[1])), ii]
            a.sort()
            if not a in pairs:
                pairs.append(a)
    s = [r,c]
    while s[0] < m-1 and s[1] > 0:
        s[0] += 1
        s[1] -= 1
    while s[0] > 0 and s[1] < m-1:
        s[0] -= 1
        s[1] += 1
        if (s[0], s[1]) in bishops and (s[0], s[1]) != i:
            a = [bishops.index((s[0], s[1])), ii]
            a.sort()
            if not a in pairs:
                pairs.append(a)
print(len(pairs))