a = 4
b = 13
frac = a/b
c = 0
i = 1
l = []
while c != frac:
    if c + (1/i) <= frac:
        c += (1/i)
        l.append(i)
    i += 1
print(l)