s = "thisisazigzag"
k = 4
i = 0
j = -1
dec = True
a = []
while i < len(s):
    if dec:
        j += 1
        if j == k-1:
            dec = False
    else:
        j -= 1
        if j == 0:
            dec = True
    a.append([s[i], j])
    i += 1
for i in range(k):
    s = ""
    for j in a:
        if j[1] == i:
            s += j[0]
        else:
            s += " "
    print(s)