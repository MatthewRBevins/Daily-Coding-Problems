N = 6
s = "1"
print(s)
for j in range(N):
    nextVal = ""
    i = 0
    while i < len(s):
        cN = s[i]
        count = 0
        while s[i] == cN:
            count += 1
            i += 1
            if i >= len(s):
                break
        nextVal += str(count)
        nextVal += cN
    s = nextVal
    print(s)
