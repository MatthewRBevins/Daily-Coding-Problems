def numToBinary(n):
    b = 0
    while 2**b < n:
        b += 1
    b -= 1
    final = 2**b
    bin = "1"
    while b > 0:
        b -= 1
        if final + (2**b) <= n:
            final += (2**b)
            bin += "1"
        else:
            bin += "0"
    lastOne = False
    for i in bin:
        if lastOne and i == "1":
            return False
        elif i == "1":
            lastOne = True
        elif i == "0":
            lastOne = False
    return True
n = 22
for i in range(n,0,-1):
    if numToBinary(i):
        print(i)
        break