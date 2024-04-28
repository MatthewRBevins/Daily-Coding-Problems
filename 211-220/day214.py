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
    longest = 0
    current = 0
    for i in bin:
        if i == "1":
            current += 1
        else:
            if current > longest:
                longest = current
            current = 0
    if current > longest:
        longest = current
    return longest
print(numToBinary(156))