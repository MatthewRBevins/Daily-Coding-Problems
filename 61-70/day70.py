n = 100
cn = 1
i = 19
while True:
    if n == cn:
        print(i)
        break
    i += 1
    s = 0
    for j in str(i):
        s += int(j)
    if s == 10:
        cn += 1
